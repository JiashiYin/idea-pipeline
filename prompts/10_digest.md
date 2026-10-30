# Stage 10 — Weekly digest

Purpose: the one page Jacob reads on Sunday. Everything else the machine wrote this week is behind it.
Written last in the weekly run, from the files, never from memory of the run. Format and sections are in
`config/generation.yaml` (`digest`); max 600 words; tables over prose.

## Procedure

1. Actuals vs targets: count this week's seeds by `source` tag (`data/seeds/<week>.jsonl`), cards
   (`data/cards/` modified this week), imports (`data/crossfield/log.jsonl`), kill searches and red teams
   (`data/candidates/*.jsonl` history entries this week), against `throughput_targets`. Flag any source that
   produced zero.
2. Stage moves: for every candidate whose status changed this week, one line — id, from → to, the one-line
   reason, the gate that failed (standards.md) or the re-open trigger (parked).
3. Triggers fired: for every parked item, check its `reopen_trigger` against this week's seeds and pressure
   records (a release, a paper, a benchmark version); list the ones that fired and what to do.
4. Scoop watch: any new paper this week that lands on a killed or parked item's target — list it with the
   item id. These count as generator hits in the scoreboard, not losses.
5. Portfolio check: are there ≥ 3 live seeds in ≥ 3 lanes? If not, say which lanes are empty.
6. Claims, ranked (from `data/claims/claims.jsonl`), each linked to its folder under `data/threads/`: headline, the belief it would change and for whom, the probes
   under it with costs, status, failing gate if any. Then the top 3 probes by scorecard with kill-probe cost and
   position. This is Jacob's hour. Kill searches run automatically on the top probes; say which ran and their verdicts.
6b. Funnel (the pace): claims born → kill-searched → survived → red-teamed → proper, this week and cumulative since
   2026-10-19; median days from a claim's birth to its first verdict; the claims still waiting and for how long.
7. Scouts and proposed lanes: the scouts kept this week (paper, scout_theme, the headline it could carry); any theme
   with three scouts in six weeks becomes a **proposed lane** here — sentence, hints, out_of_scope, routes drafted in
   the themes.yaml format, ready to paste; any lane with no live claim for two months is proposed for retirement.
   Jacob adopts or declines by editing `config/themes.yaml`; the machine never edits it.
8. Checklist lessons added this week, one line each.
9. Decisions only Jacob can make, at most three.

Write `data/digests/<week>.md`, update `ledger/LEDGER.md` if the renderer exists (else append the week's
counts to `ledger/scoreboard.jsonl`), commit and push (CLAUDE.md rule 10). Reply to Jacob with the digest's
first table and the three decisions, nothing else.
