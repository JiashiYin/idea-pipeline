# Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.

`CL-W43-02` · lane **L1** · status **open** · position solo · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.
- **Current belief (the field's):** Real-to-sim papers report rank agreement as point estimates over a handful of pairs (YUBI 2610.17521: 9 pairs, no interval; PhAIL 2605.29710 on cohort sizes)
- **If true:** Real-to-sim validation papers report resolvable fraction and chance-corrected agreement; benchmark owners publish the sample-size table
- **If false:** Rank agreement is robust even on unresolvable pairs — then the field's practice is fine and the note says so

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** Asked for in print: YUBI 2610.17521 ('These results do not yet establish a generally reliable scene-acceptance rule'; point estimates over 9 pairs, no interval); PhAIL 2605.29710 ('these cohort sizes struggle to resolve close comparisons reliably'); Robot Learning as an Empirical Science 2409.09491 (success rate reported 'with little to no information regarding the number of runs'). Who pays: every group selecting VLA checkpoints in a reconstructed simulator (Physical Intelligence, Google DeepMind robotics, NVIDIA GEAR, the SIMPLER/ManiSkill maintainers) and every reviewer reading a real-to-sim correlation table.
- **Impact ceiling:** **floor**: A two-page re-analysis note: resolvable fraction and agreement split for 5-7 published tables plus the sample-size table; requires only the tables; p ~0.85 (judgment) that the SIMPLER-style split reproduces in at least two more papers.; **middle**: A measurement paper: 'resolvable pairs' and chance-corrected agreement become the reported columns for real-to-sim validity, adopted by the SIMPLER metrics file and one 2026 follow-up; requires the 2026 same-family papers to show < 40% resolvable; p ~0.35 (judgment).; **ceiling**: A standard: real-to-sim papers report (n_real, resolvable fraction, kappa) and hardware budgets are set from the sample-size rule; requires one lab to run the new-trials check and one benchmark (PhAIL or RoboArena) to adopt the column; p ~0.10 (judgment).
- **Relevance:** Narasimhan (tau-family) and HAL: the same attenuation argument applies when a cheap proxy (simulated user, LLM judge) is validated against a small human-rated criterion; the ruler transfers as a template, the data do not. Evaluators and benchmark owners: direct (a column). Industry: checkpoint-selection teams in robotics, direct. Jacob's edge: error propagation and reliability bounds are physics habits; the computer-engineering edge is zero here, and so is the systems route.
- **Kill probe:** Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or unresolvable-pair agreement >= 0.9.
- **Density and ownership:** —
- **Why now:** PhAIL (2026-05-28) and AnyRank (2026-10-10) made real-side statistics a live topic; YUBI (2026-10-13) stated the interval gap in its own text; seven real-to-sim validity claims in 12 months form the sample; SIMPLER's public REAL_PERF table (fetched 2026-10-19) makes the first computation free.
- **Register, and what it is not:** Ruler / measurement with a recipe consequence (how many real trials to buy). It is not a new estimator (AnyRank, SureSim own that), not a benchmark, and not a simulator-fidelity method.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-13 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-13 | Resolvable pairs: the noise ceiling on real-to-sim rank agreement | Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-13** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or unresolvable-pair agreement >= 0.9.
3. Write the result into the probe's record and this thread's Log; the claim's status moves only on evidence.
4. Only then: red team (`/redteam <probe>`), then the next probe under this claim by cost.

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-10-19 — open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run

## Records

- claim record: `data/claims/claims.jsonl` (id CL-W43-02)
- probe `C-W43-13`: `data/candidates/*.jsonl`
