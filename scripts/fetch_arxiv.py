#!/usr/bin/env python3
"""Fetch the adjacent-lab and import streams from the arXiv API into a weekly seeds file.

Reference implementation for SPEC.md §4 stage 0 (arXiv part). Standard library + PyYAML only.

  python scripts/fetch_arxiv.py --days 7            # write data/seeds/<ISO-week>.jsonl, dedupe vs data/seen_ids.txt
  python scripts/fetch_arxiv.py --days 7 --dry-run  # print the queries and stop
  python scripts/fetch_arxiv.py --days 30 --week 2026-W40 --max 100

Behaviour that the orchestrator relies on:
  * idempotent: a second identical run writes zero new seeds (seen_ids) and appends a run record
  * polite: 3 s between requests (arXiv policy), one retry on HTTP 5xx
  * cached: raw Atom responses under data/cache/<sha1(url)>.xml with a 30-day TTL
  * degraded, not blocked: a failing query is logged in the run record and skipped
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    print("PyYAML missing: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "config" / "sources.yaml"
SEEDS_DIR = ROOT / "data" / "seeds"
CACHE_DIR = ROOT / "data" / "cache"
RUNS_DIR = ROOT / "data" / "runs"
SEEN = ROOT / "data" / "seen_ids.txt"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
CACHE_TTL = dt.timedelta(days=30)


def iso_week(d: dt.date) -> str:
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def arxiv_id(entry_id: str) -> str:
    # http://arxiv.org/abs/2609.20004v1 -> 2609.20004
    m = re.search(r"/abs/([^v]+)(v\d+)?$", entry_id)
    return m.group(1) if m else entry_id


def cached_get(url: str, pause: float) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(url.encode()).hexdigest()
    path = CACHE_DIR / f"{key}.xml"
    if path.exists() and dt.datetime.now() - dt.datetime.fromtimestamp(path.stat().st_mtime) < CACHE_TTL:
        return path.read_text()
    # Retry policy (2026-10-17): arXiv answers 429 when a client has been busy (a kill-search session can issue
    # dozens of API calls before the weekly fetch runs). Back off 30 s, 60 s, 120 s on 429; one retry on 5xx.
    backoff_429 = [30, 60, 120]
    attempts = 1 + len(backoff_429)
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "idea-pipeline/0.1 (research tooling)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode("utf-8")
            path.write_text(body)
            time.sleep(pause)
            return body
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < len(backoff_429):
                wait = backoff_429[attempt]
                print(f"  429 from arXiv; backing off {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            if 500 <= e.code < 600 and attempt == 0:
                time.sleep(pause * 3)
                continue
            raise
    raise RuntimeError("unreachable")


def build_url(base: str, q: str, cats: list[str], start: str, end: str, max_results: int) -> str:
    cat_clause = " OR ".join(f"cat:{c}" for c in cats)
    full = f"({q}) AND ({cat_clause}) AND submittedDate:[{start} TO {end}]"
    params = {"search_query": full, "sortBy": "submittedDate", "sortOrder": "descending", "max_results": str(max_results)}
    return base + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def parse(body: str) -> list[dict]:
    root = ET.fromstring(body)
    out = []
    for e in root.findall("a:entry", NS):
        pid = arxiv_id(e.findtext("a:id", default="", namespaces=NS))
        out.append({
            "id": pid,
            "title": re.sub(r"\s+", " ", e.findtext("a:title", default="", namespaces=NS)).strip(),
            "authors": [a.findtext("a:name", default="", namespaces=NS) for a in e.findall("a:author", NS)],
            "abstract": re.sub(r"\s+", " ", e.findtext("a:summary", default="", namespaces=NS)).strip(),
            "categories": [c.get("term") for c in e.findall("a:category", NS)],
            "published": e.findtext("a:published", default="", namespaces=NS)[:10],
            "url": f"https://arxiv.org/abs/{pid}",
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=None, help="window in days (default: sources.yaml window_days)")
    ap.add_argument("--week", default=None, help="ISO week label for the output file (default: this week)")
    ap.add_argument("--max", type=int, default=None, help="max results per query")
    ap.add_argument("--only", default=None, help="comma-separated query ids to run")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(SOURCES.read_text())["arxiv"]
    days = args.days or cfg["window_days"]
    max_results = args.max or cfg["max_results_per_query"]
    pause = float(cfg.get("pause_seconds", 3))
    today = dt.date.today()
    week = args.week or iso_week(today)
    end = dt.datetime.utcnow().strftime("%Y%m%d%H%M")
    start = (dt.datetime.utcnow() - dt.timedelta(days=days)).strftime("%Y%m%d%H%M")
    queries = cfg["queries"]
    if args.only:
        keep = set(args.only.split(","))
        queries = [q for q in queries if q["id"] in keep]

    if args.dry_run:
        for q in queries:
            print(q["id"], "->", build_url(cfg["base_url"], q["q"], cfg["categories"], start, end, max_results))
        return 0

    SEEDS_DIR.mkdir(parents=True, exist_ok=True)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    seen = set(SEEN.read_text().split()) if SEEN.exists() else set()
    out_path = SEEDS_DIR / f"{week}.jsonl"
    existing: dict[str, dict] = {}
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            if line.strip():
                rec = json.loads(line)
                existing[rec["id"]] = rec

    run = {"ts": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z", "stage": "fetch_arxiv", "week": week,
           "window_days": days, "per_query": {}, "new": 0, "degraded": []}
    for q in queries:
        url = build_url(cfg["base_url"], q["q"], cfg["categories"], start, end, max_results)
        try:
            entries = parse(cached_get(url, pause))
        except Exception as e:  # degraded, not blocked
            run["degraded"].append({"query": q["id"], "error": str(e)[:200]})
            continue
        run["per_query"][q["id"]] = len(entries)
        for ent in entries:
            if ent["id"] in existing:
                if q["id"] not in existing[ent["id"]]["matched_queries"]:
                    existing[ent["id"]]["matched_queries"].append(q["id"])
                continue
            if ent["id"] in seen:
                continue
            rec = {**ent, "source": "arxiv", "stream": q["stream"], "themes_hint": q.get("themes", []),
                   "matched_queries": [q["id"]], "status": "new", "triage_reason": "",
                   "history": [{"date": today.isoformat(), "status": "new", "note": f"fetched by {q['id']}"}]}
            existing[ent["id"]] = rec
            seen.add(ent["id"])
            run["new"] += 1

    with out_path.open("w") as f:
        for rec in sorted(existing.values(), key=lambda r: r["published"], reverse=True):
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    SEEN.write_text("\n".join(sorted(seen)) + "\n")
    (RUNS_DIR / f"{run['ts'].replace(':', '')}_fetch_arxiv.json").write_text(json.dumps(run, indent=2))
    print(json.dumps({"week": week, "seeds_file": str(out_path.relative_to(ROOT)), "total_in_file": len(existing),
                      "new": run["new"], "per_query": run["per_query"], "degraded": len(run["degraded"])}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
