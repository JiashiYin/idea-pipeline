#!/usr/bin/env python3
"""Build or refresh the thread notes — Jacob's uniform interface to every idea thread.

One folder per claim under data/threads/<claim-id>-<slug>/ holding THREAD.md, regenerated from the records
(claims, candidates with their kill searches and red teams, reports). Records stay the source of truth; the note
is the view. The `## Jacob` section of an existing note is preserved verbatim across regenerations — it is where
Jacob writes marks and questions; the operator reads it and applies marks to the records (CLAUDE.md "What Jacob
sees"). Orphan registers (records with kind: orphan_register) are listed in the index, not given a folder.

  python scripts/threads.py            # refresh every thread note and data/threads/README.md
  python scripts/threads.py CL-W43-01  # one thread (the index is always rewritten)
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
GATE_NAMES = {
    "G0": "premise hygiene (conditioning set, whose temperature, fetched numbers)",
    "G1": "cheap to kill (cheapest probe under one GPU-week, kill result pre-registered)",
    "G2": "pressure (stated strain, or ruler with pre-registered surprise)",
    "G3": "consumers (three classes, the action each changes; community-wide for golden)",
    "G4": "mechanism and consequence",
    "G5": "durability; lab-adjacent",
    "G6": "ownership, density, race window; position clause",
}


# ----------------------------------------------------------------------------- records

def slug(s: str, n: int = 48) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-")


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def latest_claims() -> tuple[dict[str, dict], list[dict]]:
    """Append-only file: the last record per id wins. Returns (claims, orphan registers)."""
    out: dict[str, dict] = {}
    for r in load_jsonl(CLAIMS):
        out[r["id"]] = r
    claims = {k: v for k, v in out.items() if v.get("kind") != "orphan_register" and v.get("headline")}
    orphans = [v for v in out.values() if v.get("kind") == "orphan_register"]
    return claims, orphans


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
        text = p if isinstance(p, str) else p.get("id", "")
        m = re.match(r"\s*([A-Za-z]+-[A-Za-z0-9]+-[A-Za-z0-9]+)", text)
        if m and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def clip(x, n: int) -> str:
    s = str(x).strip().replace("\n", " ")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def sc(c: dict, key: str, default: str = "—") -> str:
    card = c.get("scorecard") or {}
    v = card.get(key)
    if v is None and key == "density_and_ownership":
        v = card.get("density_ownership")
    if v is None:
        return default
    if isinstance(v, dict):
        return "; ".join(f"**{k}**: {clip(x, 400)}" for k, x in v.items())
    if isinstance(v, list):
        return "; ".join(clip(x, 300) for x in v)
    return clip(v, 900)


def ks_of(c: dict) -> dict:
    ks = c.get("kill_search")
    return ks if isinstance(ks, dict) else {}


def hist_rows(h) -> list[tuple[str, str, str, str]]:
    """Normalise history entries — lists (date, status, note) or dicts {date, status, note} — to tuples."""
    rows = []
    for e in h or []:
        if isinstance(e, list) and len(e) >= 3:
            rows.append((str(e[0]), str(e[1]), str(e[2]), ""))
        elif isinstance(e, dict):
            rows.append((str(e.get("date", "")), str(e.get("status", "")), str(e.get("note", "")), str(e.get("model", ""))))
    return rows


# ----------------------------------------------------------------------------- sections

def grade_line(claim: dict) -> tuple[str, str]:
    g = claim.get("grading") or {}
    gates = claim.get("gates") or {}
    failing = claim.get("failing_gate") or g.get("failing_gate") or gates.get("failing_gate") or "none recorded"
    grade = claim.get("grade") or g.get("grade") or ""
    return str(failing), str(grade)


def gate_table(claim: dict) -> str:
    g = claim.get("grading") or {}
    gates = dict(claim.get("gates") or {})
    for k, v in g.items():                      # grading uses gate2..gate6; map onto G2..G6
        m = re.fullmatch(r"gate(\d)", k)
        if m:
            gates.setdefault(f"G{m.group(1)}", v)
    rows = []
    for gid, desc in GATE_NAMES.items():
        v = gates.get(gid)
        if v is None and gid == "G1" and claim.get("cheapest_probe"):
            v = f"carried by the cheapest probe {claim['cheapest_probe']} (see Probes for its cost and verdict)"
        rows.append(f"| {gid} | {desc} | {clip(v, 600) if v is not None else 'untested'} |")
    return "| Gate | Test | Verdict |\n| --- | --- | --- |\n" + "\n".join(rows)


def probe_table(ids: list[str], cands: dict[str, dict], listed: list) -> str:
    rows = []
    for i, pid in enumerate(ids):
        c = cands.get(pid)
        label = listed[i] if i < len(listed) and isinstance(listed[i], str) else pid
        if not c:
            rows.append(f"| {pid} | {clip(label, 120)} | — | — | not a candidate record (seed or import) |")
            continue
        title = clip(c.get("title") or c.get("statement") or "", 120)
        probe = sc(c, "kill_probe", c.get("killing_experiment", "—"))
        ks = ks_of(c)
        verdict = ks.get("verdict", "") or ""
        report = ks.get("report")
        if report:
            verdict += f" ([record](../../../{report}))"
        rows.append(f"| {pid} | {title} | {clip(probe, 240)} | {c.get('status', '—')} | {verdict or '—'} |")
    extras = [x for x in listed if isinstance(x, str) and not re.match(r"\s*[A-Za-z]+-[A-Za-z0-9]+-[A-Za-z0-9]+", x)]
    tail = ("\n\nAlso under this claim (no scorecard yet): " + "; ".join(clip(x, 160) for x in extras)) if extras else ""
    return ("| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |\n| --- | --- | --- | --- | --- |\n"
            + "\n".join(rows) + tail)


def kill_section(ids: list[str], cands: dict[str, dict]) -> str:
    parts = []
    for pid in ids:
        c = cands.get(pid) or {}
        ks = ks_of(c)
        if not ks:
            continue
        parts.append(f"### {pid} — {ks.get('verdict', '—')} ({ks.get('date', '')})")
        if ks.get("verdict_reason") or ks.get("reason") or ks.get("summary"):
            parts.append(clip(ks.get("verdict_reason") or ks.get("reason") or ks.get("summary"), 900))
        if ks.get("report"):
            parts.append(f"Full record: [`{ks['report']}`](../../../{ks['report']}).")
        vbp = c.get("verdict_by_position")
        if isinstance(vbp, dict):
            parts.append("Per position — " + "; ".join(f"**{k}**: {clip(v, 220)}" for k, v in vbp.items()))
        if ks.get("why_not_done"):
            parts.append(f"**Why not done before:** {clip(ks['why_not_done'], 700)}")
        if ks.get("occupied_by") and str(ks["occupied_by"]).lower() != "none":
            parts.append(f"**Occupied by:** {clip(ks['occupied_by'], 300)}")
        nb = ks.get("neighbors") or []
        if nb:
            parts.append("Closest neighbors (one-sentence trick; one-line difference):")
            for n in nb[:5]:
                if isinstance(n, dict):
                    parts.append(f"- `{n.get('id', '')}` {clip(n.get('title', ''), 90)} — {clip(n.get('trick', ''), 260)} "
                                 f"*Difference:* {clip(n.get('difference', ''), 260)}")
                else:
                    parts.append(f"- {clip(n, 300)}")
        if ks.get("killing_experiment_check"):
            parts.append(f"**Probe as pre-registered (checked):** {clip(ks['killing_experiment_check'], 700)}")
        if ks.get("degraded"):
            parts.append(f"*Search degraded:* {clip(ks['degraded'], 300)}")
        parts.append("")
    return "\n".join(parts).rstrip() if parts else (
        "Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); "
        "`/kill <probe>` runs one by hand.")


def redteam_section(ids: list[str], cands: dict[str, dict]) -> str:
    parts = []
    for pid in ids:
        rt = (cands.get(pid) or {}).get("redteam")
        if rt:
            parts.append(f"**{pid}** — {clip(json.dumps(rt) if isinstance(rt, (dict, list)) else rt, 1200)}")
    return "\n".join(parts) if parts else (
        "Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its "
        "kill search; nothing is called proper before it.")


def first_steps(claim: dict, ids: list[str], cands: dict[str, dict]) -> str:
    cheapest = claim.get("cheapest_probe") or (ids[0] if ids else "—")
    c = cands.get(cheapest) or {}
    ks = ks_of(c)
    status = c.get("status", "proposed") if c else "no candidate record"
    probe = ks.get("killing_experiment_check") or sc(c, "kill_probe", c.get("killing_experiment", "—"))
    if claim.get("status") in ("killed", "refuted"):
        return "1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section)."
    if claim.get("status") == "parked":
        return f"1. Nothing until the re-open trigger fires: {claim.get('reopen_trigger', '—')}"
    if status == "survived-kill" and not c.get("redteam"):
        return (f"1. Red team **{cheapest}** (`/redteam {cheapest}`): three personas with fetched evidence; it survives only with no unanswered objection.\n"
                f"2. If it survives: run the probe exactly as pre-registered — {clip(probe, 500)}\n"
                f"3. Write the result into the probe's record and this Log; the claim's status moves only on evidence.\n"
                f"4. Then `/report {cheapest}` (eight sections, three decisions), and the next probe under this claim by cost.")
    if status == "survived-kill":
        return (f"1. Run **{cheapest}** exactly as pre-registered — {clip(probe, 500)}\n"
                f"2. Write the result into the probe's record and this Log.\n3. `/report {cheapest}`; then the next probe by cost.")
    if status == "killed":
        nxt = next((p for p in ids if p != cheapest and (cands.get(p) or {}).get("status") == "proposed"), None)
        return (f"1. Read what killed **{cheapest}** before anything else.\n"
                f"2. Next probe by cost: **{nxt or 'none — the claim needs a new probe or is a thought'}**; its kill search runs automatically or by `/kill`.")
    return (f"1. Wait for the automatic kill search on **{cheapest}** (Sunday run), or run `/kill {cheapest}` in a session.\n"
            f"2. If it survives: `/redteam {cheapest}`, then the probe as pre-registered — {clip(probe, 400)}\n"
            f"3. Write results into the records and this Log; status moves only on evidence.")


def decisions(claim: dict, ids: list[str], cands: dict[str, dict]) -> list[str]:
    if claim.get("decisions"):
        return [clip(d, 400) for d in claim["decisions"]][:3]
    out = []
    for pid in ids:
        c = cands.get(pid) or {}
        if c.get("status") == "survived-kill" and not c.get("redteam"):
            out.append(f"Spend a session on the red team of {pid} now, or wait for the next automatic run? (write `promote` or leave it)")
        if c.get("status") == "parked":
            out.append(f"{pid} is parked — {clip(c.get('reopen_trigger') or sc(c, 'kill_probe'), 200)}: fund it, or leave it parked?")
    if not out and claim.get("status") == "open":
        out.append("None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.")
    return out[:3] or ["(none pending)"]


def status_sentence(claim: dict, ids: list[str], cands: dict[str, dict]) -> str:
    st = claim.get("status", "open")
    survivors = [p for p in ids if (cands.get(p) or {}).get("status") == "survived-kill"]
    killed = [p for p in ids if (cands.get(p) or {}).get("status") == "killed"]
    base = {
        "thought": "A thought from `/capture`: not yet graded against the gates; its kill search has not run.",
        "open": "Open claim.",
        "supported": "A probe survived its kill search and red team; the claim stands on evidence.",
        "refuted": "A probe came out against the claim.",
        "killed": "Killed — see the kill section.",
        "parked": f"Parked — re-open trigger: {claim.get('reopen_trigger', '—')}",
    }.get(st, st)
    if st == "open":
        if survivors:
            base += f" Probe{'s' if len(survivors) > 1 else ''} {', '.join(survivors)} survived the kill search; red team owed before anything is called proper."
        elif killed and len(killed) == len([p for p in ids if p in cands]):
            base += " Every probe under it has been killed; the claim needs a new probe or dies."
        else:
            base += " Nothing under it has survived a kill search yet."
    return base


def existing_jacob_section(path: Path) -> str:
    if not path.exists():
        return JACOB_DEFAULT
    text = path.read_text()
    i = text.find(JACOB_HEADER)
    if i < 0:
        return JACOB_DEFAULT
    j = text.find("\n## ", i + len(JACOB_HEADER))
    return text[i:] if j < 0 else text[i:j] + "\n"


def log_section(claim: dict, ids: list[str], cands: dict[str, dict]) -> str:
    rows = [(d, f"claim {s}", n) for d, s, n, _ in hist_rows(claim.get("history"))]
    for pid in ids:
        for d, s, n, _ in hist_rows((cands.get(pid) or {}).get("history")):
            if s in ("killed", "parked", "survived-kill", "jacob-dropped", "promoted", "supported", "refuted"):
                rows.append((d, f"{pid} {s}", n))
    rows.sort(key=lambda r: r[0])
    return "\n".join(f"- {d} — {s}: {clip(n, 400)}" for d, s, n in rows) or "- (none)"


def render(claim: dict, cands: dict[str, dict], today: str, jacob: str) -> str:
    ids = probe_ids(claim)
    first = cands.get(claim.get("cheapest_probe", ""), {}) or (cands.get(ids[0], {}) if ids else {})
    failing, grade = grade_line(claim)
    records = [f"- claim record: `data/claims/claims.jsonl` (id `{claim['id']}`, version {claim.get('version', 1)})"]
    for pid in ids:
        c = cands.get(pid)
        if c:
            records.append(f"- probe `{pid}`: `data/candidates/{c.get('week', '*')}.jsonl`"
                           + (f"; kill record `{ks_of(c)['report']}`" if ks_of(c).get("report") else ""))
        else:
            records.append(f"- `{pid}`: seed or import record (no candidate yet)")
    grade_txt = f" Grade on paper: {grade}." if grade else ""
    return f"""# {claim['headline']}

`{claim['id']}` · lane **{claim.get('lane', '—')}** · status **{claim.get('status', 'open')}** · rank {claim.get('rank', '—')} · position {claim.get('position', '—')} · refreshed {today}

## Status

{status_sentence(claim, ids, cands)} Failing gate: {failing}.{grade_txt} Next action: see First steps.

## The claim

- **Headline:** {claim['headline']}
- **Current belief (the field's):** {claim.get('current_belief', '—')}
- **If true:** {claim.get('if_true', '—')}
- **If false:** {claim.get('if_false', '—')}

## Scorecard (from the cheapest probe's record)

- **Target value:** {sc(first, 'target_value')}
- **Impact ceiling:** {sc(first, 'impact_ceiling')}
- **Relevance:** {sc(first, 'relevance')}
- **Kill probe:** {sc(first, 'kill_probe', first.get('killing_experiment', '—'))}
- **Density and ownership:** {sc(first, 'density_and_ownership')}
- **Why now:** {sc(first, 'why_now', first.get('why_now', '—'))}
- **Register, and what it is not:** {sc(first, 'register')}

## Gates (config/standards.md)

{gate_table(claim)}

## Probes under this claim

{probe_table(ids, cands, claim.get('probes', []))}

## Kill search

{kill_section(ids, cands)}

## Red team

{redteam_section(ids, cands)}

## First steps if pursued

{first_steps(claim, ids, cands)}

## Decisions for Jacob

{chr(10).join('- ' + d for d in decisions(claim, ids, cands))}

{jacob}
## Log

{log_section(claim, ids, cands)}

## Records

{chr(10).join(records)}
"""


# ----------------------------------------------------------------------------- index

def write_index(claims: dict[str, dict], orphans: list[dict], cands: dict[str, dict], today: str) -> None:
    rows = []
    for cid, claim in claims.items():
        ids = probe_ids(claim)
        survivors = sum(1 for p in ids if (cands.get(p) or {}).get("status") == "survived-kill")
        failing, grade = grade_line(claim)
        rank = claim.get("rank")
        rows.append((rank if isinstance(rank, int) else 99, claim.get("lane", ""), cid, claim.get("status", ""),
                     claim["headline"], len(ids), survivors, claim.get("cheapest_probe", ""), failing,
                     f"{cid}-{slug(claim['headline'])}"))
    rows.sort()
    lines = ["# Threads — one folder per claim, one note per folder", "",
             f"Refreshed {today}. Each `THREAD.md` is regenerated from the records by `python scripts/threads.py`; your",
             "`## Jacob` section is preserved verbatim. Read a note top to bottom: Status, the claim, scorecard, gates, probes,",
             "kill search, red team, first steps, decisions — then write in your section. Ranked by the claims stage.", "",
             "| Rank | Lane | Claim | Status | Headline | Probes (survived) | Cheapest | Failing gate | Folder |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for rank, lane, cid, status, headline, n, surv, cheapest, failing, folder in rows:
        lines.append(f"| {rank if rank != 99 else '—'} | {lane} | {cid} | {status} | {clip(headline, 160)} | {n} ({surv}) | {cheapest} | "
                     f"{clip(failing, 60)} | [`{folder}`](./{folder}/THREAD.md) |")
    if orphans:
        lines += ["", "## Orphan probes (no claim yet)", "",
                  "Probes without a headline are footnotes until a claim is written over them (three on one theme = a missing claim).", ""]
        for reg in orphans:
            for o in reg.get("orphans", []):
                lines.append(f"- `{o.get('id', '')}` ({o.get('lane', '')}; {clip(o.get('theme', ''), 60)}) — {clip(o.get('note', ''), 220)}")
            if reg.get("flag"):
                lines.append(f"- *Flag:* {clip(reg['flag'], 240)}")
    (THREADS / "README.md").write_text("\n".join(lines) + "\n")


def main(argv: list[str]) -> int:
    today = dt.date.today().isoformat()
    claims, orphans = latest_claims()
    cands = all_candidates()
    want = [a for a in argv[1:] if a != "all"] or list(claims)
    unknown = [w for w in want if w not in claims]
    if unknown:
        print(f"no claim with id {', '.join(unknown)} in {CLAIMS.relative_to(ROOT)}", file=sys.stderr)
    THREADS.mkdir(parents=True, exist_ok=True)
    done = 0
    for cid, claim in claims.items():
        if cid not in want:
            continue
        folder = THREADS / f"{cid}-{slug(claim['headline'])}"
        # a headline rewrite renames the folder: move the old note so the Jacob section survives
        for old in THREADS.glob(f"{cid}-*"):
            if old.is_dir() and old != folder:
                folder.mkdir(parents=True, exist_ok=True)
                old_note = old / "THREAD.md"
                if old_note.exists() and not (folder / "THREAD.md").exists():
                    old_note.rename(folder / "THREAD.md")
                for leftover in old.iterdir():
                    leftover.rename(folder / leftover.name)
                old.rmdir()
        folder.mkdir(parents=True, exist_ok=True)
        note = folder / "THREAD.md"
        jacob = existing_jacob_section(note)
        note.write_text(render(claim, cands, today, jacob))
        done += 1
    write_index(claims, orphans, cands, today)
    print(f"threads refreshed: {done} of {len(claims)}; index at data/threads/README.md")
    return 0 if not unknown else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
