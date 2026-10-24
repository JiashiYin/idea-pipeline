# GPU physics engines cannot resolve the policy-return differences that robot-RL papers report as improvements: engine-only repeatability and batch-position variance exceed 30% of the policy-to-policy spread on contact-rich tasks.

`CL-W43-09` · lane **L5** · status **open** · rank 9 · position both · refreshed 2026-10-23

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; Gate 1 blocked on paperwork (no scorecard). Grade on paper: open. Next action: see First steps.

## The claim

- **Headline:** GPU physics engines cannot resolve the policy-return differences that robot-RL papers report as improvements: engine-only repeatability and batch-position variance exceed 30% of the policy-to-policy spread on contact-rich tasks.
- **Current belief (the field's):** GPUSimBench 2607.13059 documents that identical initial conditions produce different trajectories run-to-run and across batch slots and sorts the causes into regimes, as a reliability nuisance; robot-RL papers report standard deviations over training seeds and treat the simulator as a noiseless oracle (import:2026-W43-S4xF9 field answer)
- **If true:** Papers report the engine's gauge uncertainty beside the seed std and stop claiming gaps inside it; engine builders ship a gauge R&R card per release; simulation leaderboards add a resolution-floor (ndc) column
- **If false:** Engine noise is a small share of the reported spread (%GRR under 10% everywhere): the simulator is a precise gauge and seed variance is the algorithm's — a reassuring measurement engine teams cite

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
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-09-lit (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: %GRR and ndc are identifiable with deterministic frozen policies (temperature 0 by construction, so the policy contributes no decision variance); pre-registered surprise — expected %GRR above 30% on contact-rich tasks at batch sizes >= 4096, field assumes seed variance is the algorithm's, the ruler is a service if %GRR is under 10% everywhere |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: robot-RL authors, engine builders, simulation leaderboard owners, reproducibility researchers |
| G4 | mechanism and consequence | pass: mechanism — floating-point reduction order under GPU thread scheduling flips contact ordering and diverges on contact-rich states; consequence — a minimum reportable gap per task, or a certified deterministic mode |
| G5 | durability; lab-adjacent | pass: a ruler on any engine; lab-adjacent to engine builders |
| G6 | ownership, density, race window; position clause | open: kill search owed; the premise half (non-determinism exists, its magnitude per regime) is occupied by GPUSimBench; the acceptance criterion against the signal read off the engine is the import; shares its ruler shape with CL-W43-02 (can the instrument resolve what it ranks) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-09-lit | Day-1 literature table ($0): for 20 recent GPU-simulator robot-RL papers, tabulate the reported improvement, the seed i… | Dead as a headline if fewer than 10% of reported improvements fall inside the engine divergence (then the floor is a footnote); pre-registered expectation (judgment): 20-40% on contact-rich tasks. Lesson from CL-W43-02: the quantifier is m… | thought | not run (no candidate record yet) |

Also under this claim (no scorecard yet): import:2026-W43-S4xF9 (gauge R&R on 10 checkpoints x 50 states x repeats x slots x batch sizes x 2 GPUs; <30 GPU-h; no scorecard)

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-09-lit** (Sunday run), or run `/kill P-W43-09-lit` in a session.
2. If it survives: `/redteam P-W43-09-lit`, then the probe as pre-registered — Dead as a headline if fewer than 10% of reported improvements fall inside the engine divergence (then the floor is a footnote); pre-registered expectation (judgment): 20-40% on contact-rich tasks. Lesson from CL-W43-02: the quantifier is measured before it is written. $0, two days, no GPU.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim open: new claim from import:2026-W43-S4xF9 (gauge R&R); second L5 claim this week
- 2026-10-21 — claim open: discuss session with Jacob (2026-10-21): this is the resolution-floor claim of the L5 program; literature table P-W43-09-lit written as the $0 first step (quantifier before headline, per CL-W43-02's refutation); noted as the twin of CL-W43-J01

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-09`, version 2)
- `P-W43-09-lit`: seed or import record (no candidate yet)
