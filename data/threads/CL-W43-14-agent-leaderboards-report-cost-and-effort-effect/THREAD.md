# Agent leaderboards report cost and effort effects from single runs whose run-to-run spread is larger than the differences they rank.

`CL-W43-14` · lane **L1** · status **open** · rank 7 · position solo · refreshed 2026-10-30

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 1 blocked on paperwork (no scorecarded probe); Gate 6 not yet established. Grade on paper: open pending scorecards and kill search. Next action: see First steps.

## The claim

- **Headline:** Agent leaderboards report cost and effort effects from single runs whose run-to-run spread is larger than the differences they rank.
- **Current belief (the field's):** HAL 2510.11977 states 'we were forced to rely on single runs without statistical validation for most evaluations' and reports higher effort giving equal or lower accuracy in 21 of 36 model-agent-benchmark combinations; the released 2610.00917 cost table holds exactly one run per (model, harness, task) cell in all 6,204 cells (import S6xF1's arithmetic, 2026-10-25).
- **If true:** Leaderboards add a replicate rule and a resolvable-ratio column for cost; effort non-monotonicity is re-read as an interaction component plus run noise; harness and model cost comparisons under the resolvable ratio are withdrawn
- **If false:** Run share of cost variance under 5% and the effort x task interaction identified from single runs: single-run tables are adequate and the lane's replicate rule is a service

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** —
- **Impact ceiling:** —
- **Relevance:** —
- **Kill probe:** —
- **Density and ownership:** —
- **Why now:** —
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe import:2026-W43-S8xF1 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B with a stated strain: the ruler is the run-within-cell variance component for cost and for the effort effect; the field itself states the single-run limitation |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every leaderboard with a cost or effort column; harness papers; cost-per-success reporting |
| G4 | mechanism and consequence | pass: mechanism — heavy-tailed per-run cost (log-cost SD 1.4-1.6) and binomial single-run success make one-replicate cells noisy; consequence — replicate rule and resolvable-ratio column |
| G5 | durability; lab-adjacent | pass as a ruler; G-theory for scores is already imported (2610.00651, 2608.11323) so the new ground is cost and effort as measurands |
| G6 | ownership, density, race window; position clause | open: imports found no fetched source decomposing cost or the effort x task interaction; kill search owed; Gate 1 blocked on paperwork — neither probe carries a scorecard (checklist 2026-10-20: write it at import time or in the first /mutate) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |


Also under this claim (no scorecard yet): import:2026-W43-S8xF1 (step 0: $0 re-analysis of HAL per-task logs for the 36 cells; step 1: 4 effort x 60 tasks x 5 runs crossed G-study, 60-100 GPU-h or $2-4…; import:2026-W43-S6xF1 (step 1: $0 variance decomposition of the released 2610.00917 cost table; step 2: 3 harnesses x 63 Terminal-Bench 4 tasks x 5 runs, $400-…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **import:2026-W43-S8xF1** (Sunday run), or run `/kill import:2026-W43-S8xF1` in a session.
2. If it survives: `/redteam import:2026-W43-S8xF1`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Promote? Princeton-local consumer (HAL); $0 first step; part of the proposed L1 'noise floor' program.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written top-down by the closing-W43 claims run; the two cost/effort imports attached as probes; scorecards owed before it is kill-applicable
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 7 (unchanged)
- 2026-10-30 — claim open: nominated as a core-ML champion candidate (Jacob asked for a champion outside L5); kill search requested ahead of rank order; see PROGRAM-L1-evaluation-floors.md

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-14`, version 3)
