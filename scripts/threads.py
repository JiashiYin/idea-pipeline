#!/usr/bin/env python3
"""Build or refresh the thread notes — Jacob's uniform interface to every idea thread.

One folder per claim under data/threads/<claim-id>-<slug>/ holding THREAD.md, regenerated from the records
(claims, candidates, kill records, red teams, reports). Records stay the source of truth; the note is the view.
The `## Jacob` section of an existing note is preserved verbatim across regenerations — it is where Jacob
writes marks and questions; the operator reads it and applies marks to the records (CLAUDE.md "What Jacob sees").

  python scripts/threads.py            # refresh every thread note and data/threads/README.md
  python scripts/threads.py CL-W43-01  # one thread
Standard library only.
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "data" / "claims" / "claims.jsonl"
THREADS = ROOT / "data" / "threads"
JACOB_HEADER = "## Jacob"
JACOB_DEFAULT = (
    "## Jacob\n\n"
    "<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,\n"
    "     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->\n\n"
    "- status mark: (none)\n- notes:\n"
)


def slug(s: str, n: int = 48) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def latest_claims() -> dict[str, dict]:
    """Append-only file: the last record per id wins."""
    out: dict[str, dict] = {}
    for r in load_jsonl(CLAIMS):
        out[r["id"]] = r
    return out


def all_candidates() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(glob.glob(str(ROOT / "data" / "candidates" / "*.jsonl"))):
        for r in load_jsonl(Path(p)):
            cid = r.get("id") or r.get("cid")
            if cid:
                out[cid] = r
    return out


def probe_ids(claim: dict) -> list[str]:
    ids = []
    for p in claim.get("probes", []):
        m = re.match(r"\s*([A-Za-z]+-[A-Za-z0-9]+-[A-Za-z0-9]+)", p if isinstance(p, str) else p.get("id", ""))
        if m:
            ids.append(m.group(1))
    return ids


def sc(c: dict, key: str, default: str = "—") -> str:
    v = (c.get("scorecard") or {}).get(key)
    if v is None:
        return default
    if isinstance(v, dict):
        return "; ".join(f"**{k}**: {str(x).strip()}" for k, x in v.items())
    return str(v).strip()


def gate_table(claim: dict, probes: list[dict]) -> str:
    gates = claim.get("gates") or {}
    rows = []
    names = {
        "G0": "premise hygiene (conditioning set, whose temperature, fetched numbers)",
        "G1": "cheap to kill (cheapest probe under one GPU-week, kill result pre-registered)",
        "G2": "pressure (stated strain, or ruler with pre-registered surprise)",
        "G3": "consumers (three classes, the action each changes; community-wide for golden)",
        "G4": "mechanism and consequence",
        "G5": "durability; lab-adjacent",
        "G6": "ownership, density, race window; position clause",
    }
    for g, desc in names.items():
        v = gates.get(g)
        if v is None and g == "G1" and probes:
            v = f"untested — cheapest probe listed: {claim.get('cheapest_probe', '—')}"
        rows.append(f"| {g} | {desc} | {v if v is not None else 'untested'} |")
    return "| Gate | Test | Verdict |\n| --- | --- | --- |\n" + "\n".join(rows)


def probe_table(ids: list[str], cands: dict[str, dict], listed: list) -> str:
    rows = []
    for i, pid in enumerate(ids):
        c = cands.get(pid)
        label = listed[i] if i < len(listed) else pid
        if not c:
            rows.append(f"| {pid} | {label} | — | — | not found in records |")
            continue
        title = (c.get("title") or c.get("statement") or "")[:110]
        probe = sc(c, "kill_probe", c.get("killing_experiment", "—"))
        ks = c.get("kill_search")
        verdict = ks.get("verdict", "") if isinstance(ks, dict) else ""
        rows.append(f"| {pid} | {title} | {probe[:220]} | {c.get('status', '—')} | {verdict or '—'} |")
    return "| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |\n| --- | --- | --- | --- | --- |\n" + "\n".join(rows)


def kill_section(ids: list[str], cands: dict[str, dict]) -> str:
    parts = []
    for pid in ids:
        c = cands.get(pid) or {}
        ks = c.get("kill_search")
        if isinstance(ks, dict) and ks:
            parts.append(f"**{pid}** — verdict: {ks.get('verdict', '—')}. {str(ks.get('reason') or ks.get('summary') or '')[:600]}")
            for n in (ks.get("neighbors") or [])[:4]:
                parts.append(f"  - {str(n)[:300]}")
    return "\n".join(parts) if parts else "Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml)."


def redteam_section(ids: list[str], cands: dict[str, dict]) -> str:
    parts = []
    for pid in ids:
        rt = (cands.get(pid) or {}).get("redteam")
        if rt:
            parts.append(f"**{pid}** — {str(rt)[:800]}")
    return "\n".join(parts) if parts else "Not run. A red team runs only on a probe that survived its kill search."


def first_steps(claim: dict, ids: list[str], cands: dict[str, dict]) -> str:
    cheapest = claim.get("cheapest_probe", "")
    c = cands.get(cheapest) or {}
    probe = sc(c, "kill_probe", c.get("killing_experiment", "—"))
    return (
        f"1. Read the kill-search record of **{cheapest or ids[0] if ids else '—'}** when it lands; if killed, read what killed it before anything else.\n"
        f"2. If it survived: run its probe exactly as pre-registered — {probe[:300]}\n"
        f"3. Write the result into the probe's record and this thread's Log; the claim's status moves only on evidence.\n"
        f"4. Only then: red team (`/redteam <probe>`), then the next probe under this claim by cost."
    )


def existing_jacob_section(path: Path) -> str:
    if not path.exists():
        return JACOB_DEFAULT
    text = path.read_text()
    i = text.find(JACOB_HEADER)
    if i < 0:
        return JACOB_DEFAULT
    j = text.find("\n## ", i + len(JACOB_HEADER))
    return text[i:] if j < 0 else text[i:j] + "\n"


def render(claim: dict, cands: dict[str, dict], today: str, jacob: str) -> str:
    ids = probe_ids(claim)
    probes = [cands[i] for i in ids if i in cands]
    hist = claim.get("history", [])
    log = "\n".join(f"- {h[0]} — {h[1]}: {h[2]}" for h in hist if isinstance(h, list) and len(h) >= 3) or "- (none)"
    first = cands.get(claim.get("cheapest_probe", ""), {})
    status_line = {
        "open": "Open claim, ungraded or partly graded; nothing under it has survived a kill search yet.",
        "supported": "A probe survived its kill search and red team; the claim stands on evidence.",
        "refuted": "A probe came out against the claim.",
        "killed": "Killed — see the kill section.",
        "parked": f"Parked — re-open trigger: {claim.get('reopen_trigger', '—')}",
    }.get(claim.get("status", "open"), claim.get("status", "open"))
    records = [f"- claim record: `data/claims/claims.jsonl` (id {claim['id']})"]
    for pid in ids:
        records.append(f"- probe `{pid}`: `data/candidates/*.jsonl`")
    return f"""# {claim['headline']}

`{claim['id']}` · lane **{claim.get('lane', '—')}** · status **{claim.get('status', 'open')}** · position {claim.get('position', '—')} · refreshed {today}

## Status

{status_line} Failing gate: {claim.get('failing_gate', 'none recorded')}. Next action: see First steps.

## The claim

- **Headline:** {claim['headline']}
- **Current belief (the field's):** {claim.get('current_belief', '—')}
- **If true:** {claim.get('if_true', '—')}
- **If false:** {claim.get('if_false', '—')}

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** {sc(first, 'target_value')}
- **Impact ceiling:** {sc(first, 'impact_ceiling')}
- **Relevance:** {sc(first, 'relevance')}
- **Kill probe:** {sc(first, 'kill_probe', first.get('killing_experiment', '—'))}
- **Density and ownership:** {sc(first, 'density_and_ownership')}
- **Why now:** {sc(first, 'why_now')}
- **Register, and what it is not:** {sc(first, 'register')}

## Gates (config/standards.md)

{gate_table(claim, probes)}

## Probes under this claim

{probe_table(ids, cands, claim.get('probes', []))}

## Kill search

{kill_section(ids, cands)}

## Red team

{redteam_section(ids, cands)}

## First steps if pursued

{first_steps(claim, ids, cands)}

## Decisions for Jacob

{chr(10).join('- ' + d for d in (claim.get('decisions') or ['(none pending)']))}

{jacob}
## Log

{log}

## Records

{chr(10).join(records)}
"""


def main(argv: list[str]) -> int:
    today = dt.date.today().isoformat()
    claims = latest_claims()
    cands = all_candidates()
    want = argv[1:] or list(claims)
    THREADS.mkdir(parents=True, exist_ok=True)
    index_rows = []
    for cid, claim in claims.items():
        folder = THREADS / f"{cid}-{slug(claim['headline'])}"
        note = folder / "THREAD.md"
        if cid in want:
            folder.mkdir(parents=True, exist_ok=True)
            jacob = existing_jacob_section(note)
            note.write_text(render(claim, cands, today, jacob))
        ids = probe_ids(claim)
        index_rows.append((claim.get("lane", ""), cid, claim.get("status", ""), claim["headline"], len(ids),
                           claim.get("cheapest_probe", ""), folder.name))
    index_rows.sort()
    lines = ["# Threads — one folder per claim, one note per folder", "",
             f"Refreshed {today}. Each `THREAD.md` is regenerated from the records by `python scripts/threads.py`;",
             "your `## Jacob` section is preserved verbatim. Read the Status line, then Probes, then First steps.", "",
             "| Lane | Claim | Status | Headline | Probes | Cheapest | Folder |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for lane, cid, status, headline, n, cheapest, folder in index_rows:
        lines.append(f"| {lane} | {cid} | {status} | {headline} | {n} | {cheapest} | [`{folder}`](./{folder}/THREAD.md) |")
    (THREADS / "README.md").write_text("\n".join(lines) + "\n")
    print(f"threads refreshed: {len(want)} of {len(claims)}; index at data/threads/README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
