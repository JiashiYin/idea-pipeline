# A GPU simulator's physics budget is a dose: transferable policy return follows one dose-response curve in solver budget per task class, so fidelity can be scheduled during training like a learning rate instead of fixed by a config file.

`CL-W43-J02` · lane **L5** · status **thought** · rank — · position solo · refreshed 2026-10-24

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** A GPU simulator's physics budget is a dose: transferable policy return follows one dose-response curve in solver budget per task class, so fidelity can be scheduled during training like a learning rate instead of fixed by a config file.
- **Current belief (the field's):** Solver budgets are fixed per task in model files (Playground XML iterations=1 Go1, 5 Leap; legged_gym num_position_iterations=4) and justified by DR (MJX docs, fetched 2026-10-20 in the C-W43-15 red team); numerical settings are treated as a randomization axis (Dactyl randomized the time step), not a dial; the only fetched RL consumer of a fidelity scalar is a control-variate estimator (MFPG-PPO 2610.02505).
- **If true:** Training recipes gain a fidelity schedule (coarse early, converged late) at matched wall-clock; engine teams expose the budget per world as a runtime knob rather than a file constant; the iteration-level scheduler (the lane's systems piece) has a stated consumer.
- **If false:** Response is task-specific or non-monotone: fixed budgets are right and the scheduler has no consumer - a result engine teams would still cite when choosing defaults.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: 2610.17221's recipe needs a known fidelity law and declines the solver axis (fetched 2026-10-19); MFPG-PPO uses a low-fidelity simulator as a control variate without isolating any knob. Who pays: anyone training in GPU simulators under a wall-clock budget; engine teams choosing defaults.
- **Impact ceiling:** **floor**: Two dose-response curves on public tasks; a note cited when budgets are chosen. p = 0.6 (judgment).; **middle**: A shared curve shape licenses a fidelity schedule; C-W43-16 shows it beats fixed budgets at matched wall-clock; Playground or Isaac Lab exposes the knob. p = 0.2 (judgment).; **ceiling**: Fidelity scheduling becomes a standard training lever and the iteration-level scheduler ships inside an engine. p = 0.05 (judgment) - this scenario is head-to-head with engine teams and is reached only from a lab position.
- **Relevance:** L5 direct; the systems route (GPU scheduling) via the scheduler consequence; robotics faculty via training recipes; Jacob's edge (numerics, GPU scheduling) load-bearing; zero for L1-L2 and LLM consumers.
- **Kill probe:** Rides on the 2x2 (+2-4 GPU-h): dead if curves are non-monotone or do not share a shape.
- **Density and ownership:** Unknown until the kill search; incumbents: engine defaults, MFPG-PPO (bundled knobs), curriculum-over-fidelity work in other fields (to search: multi-fidelity optimisation, progressive refinement - PRDP 2502.19611 is the linear-solver precedent).
- **Why now:** Minutes-scale training in GPU engines (Playground, Feb 2025) makes a budget sweep a one-day job; before, each point was a day.
- **Register, and what it is not:** Measurement (a dose-response) with a recipe consequence (a schedule) and, only from a lab position, a systems artifact. Not a new engine, not a contact model.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-01-2x2 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-01-2x2 | Dose-response arm of the 2x2: add budgets {2, 10} to {shipped, 100}; plot transferable return (evaluated in the converg… | Dead for this claim if the curves for Go1 and Leap are not monotone or do not share a shape up to scale (pre-registered: Spearman of the two normalised curves above 0.8); then budgets are task constants, not a dose. Cost rides on CL-W43-01… | thought | not run (no candidate record yet) |
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K=1 in R_conv and rho… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-01-2x2** (Sunday run), or run `/kill P-W43-01-2x2` in a session.
2. If it survives: `/redteam P-W43-01-2x2`, then the probe as pre-registered — Dead for this claim if the curves for Go1 and Leap are not monotone or do not share a shape up to scale (pre-registered: Spearman of the two normalised curves above 0.8); then budgets are task constants, not a dose. Cost rides on CL-W43-01's probe (+2 budgets, +2-4 GPU-h).
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None until CL-W43-01's 2x2 has run; then: fund C-W43-16 (50 GPU-h) or not.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-21 — claim thought: captured in the 2026-10-21 discuss session: the systems half of L5 re-framed as the consequence of a dose-response measurement; probe rides on CL-W43-01's 2x2

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J02`, version 1)
- `P-W43-01-2x2`: seed or import record (no candidate yet)
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
