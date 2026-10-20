Run the full weekly cycle for ISO week $ARGUMENTS (Sunday run; also what the scheduled task executes).
The week label is the ISO week of today's date in America/New_York, never UTC: a Sunday-evening run belongs to the
week that is ending. If $ARGUMENTS is empty, compute it that way.

Read `CLAUDE.md`, `config/themes.yaml`, `config/standards.md`, `config/generation.yaml` first. Then, in order:
1. `/fetch` — `bash scripts/run_week.sh` (arXiv watch and import streams; complaint stream if GitHub access exists).
2. `/triage $ARGUMENTS` — against the lanes; record `source` and lane fits on every seed.
3. `/card <id>` for each kept seed, up to 8, newest first; append limitations as complaint seeds.
4. `/crossfield $ARGUMENTS` — 4 imports.
5. `/mutate <id>` for the cards whose `information_asymmetry` field is non-empty, up to 20 candidates total.
6. Monthly only (first run of the month): `/pressure $ARGUMENTS`, `/owned $ARGUMENTS`, `/definitive $ARGUMENTS`.
6b. `/claims $ARGUMENTS` — attach every candidate to a claim or mark it orphan; write and rank claims.
7. If `auto_kill_monday` is true in `config/generation.yaml` (it is): `/kill` on the top `kill_budget_per_week` probes,
   taken claim by claim in claim rank order (the cheapest probe of the top claim first); record each verdict on the
   candidate and its effect on the claim's status.
7b. If `auto_redteam` is true in `config/generation.yaml` (it is): `/redteam` on every probe that survived a kill search
   and has no `redteam` block yet, up to `redteam_budget_per_week`, claim rank order; a probe Jacob marked
   `jacob-dropped` is skipped. Record the verdict on the probe and its effect on the claim.
8. `python scripts/threads.py` — refresh every thread note and the threads index (read Jacob's sections first and apply marks).
9. `/digest $ARGUMENTS` — one page, each claim linked to its thread folder; commit and push.
Budget: ≤ 40 seeds triaged, ≤ 8 cards, ≤ 20 candidates, ≤ 3 kill searches. Stop and write the digest if a stage
fails; a degraded week with a digest beats a complete week without one.
