# A GPU simulator's physics budget is a dose: transferable policy return follows one dose-response curve in solver budget per task class, so fidelity can be scheduled during training like a learning rate instead of fixed by a config file.

`CL-W43-J02` · lane **L5** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G2B (G4 fails with it). Grade on paper: killed at the concept-level kill search. Next action: see First steps.

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
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K=1 in R_conv and rho… | killed | — |

## Kill search

### Concept level (CL-W43-J02) — killed (2026-11-22)
The dose half has two knob-isolated readings on its axis, both flat inside noise (2610.32277 Table 2; SimuGuard D.2), so the expected response equals the owners' sentence; the schedule half is the published recipe of adaptive multi-grid RL (2207.03253), PRDP (2502.19611) and MFPG-PPO's online allocation (2610.02505), and the cross-fidelity matrix came out flat in 2610.06874.
Full record: [`data/reports/2026-W47-kill-CL-W43-J02.md`](../../../data/reports/2026-W47-kill-CL-W43-J02.md).
**Occupied by:** none on the exact cell; the schedule mechanism is occupied by 2207.03253 (grid fidelity, PPO, plateau criterion), 2502.19611 (solver iterations, plateau criterion, differentiable physics) and 2610.02505 (per-iteration two-fidelity budget allocation in Isaac Lab); the measurement shape by 2610.06874 (five-level cross-fidelity PPO matrix, flat)
**Why not done before:** it is hard because every community positioned to run it holds a flat reading: engine owners (MJX tuning page), sim-to-sim attribution (2610.32277: solver row < 0.006 rad, time step decisive), simulator audit (SimuGuard: sign against exploitation), multi-fidelity RL (schedules on grids and linear solvers; bundles engine knobs; its one robotics matrix flat). Enabling pieces exist (Playground 2025-02; PRDP 2025-02; MFPG-PPO stack 2026-10-01) and their owners are positioned to write the schedule paper.
Closest neighbors (one-sentence trick; one-line difference):
- `2207.03253` Robust optimal well control using an adaptive multi-grid reinforcement learning framework — Train PPO on a coarse PDE grid first and step the grid fidelity up each time the return plateaus, comparing cost in fine-grid-equivalent episodes. *Difference:* Occupies the schedule half as a method (coarse early, fine late; fixed vs adaptive schedules; 61-76% saved); axis is grid resolution of a reservoir PDE, not a contact solver cap; no transferable-return curve; asks for the optimal schedule as future work.
- `2502.19611` PRDP: Progressively Refined Differentiable Physics — Start differentiable-physics training at one linear-solver iteration, add iterations whenever the validation metric plateaus, stop below full convergence. *Difference:* The schedule on the solver-iteration axis itself with a plateau rule, for a network trained through the solver, not a policy trained inside it; limited to iterative linear solvers; names temporal resolution as future work.
- `2610.02505` Multi-Fidelity Policy Gradients Stabilize Data-Scarce Reinforcement Learning — Use rollouts from a simplified Isaac Lab configuration as a control variate for the high-fidelity PPO gradient and re-solve a two-fidelity budget allocation every iteration from the measured correlation. *Difference:* Only in-window RL consumer of a fidelity dose in a GPU rigid-body engine; allocation changes over training and LF pre-training is routine; knobs bundled (collision model, time step, solver iterations, self-collision); return never plotted against fidelity.
- `2610.06874` Statistical Turbulence and High-Fidelity Disturbance Fields for Quadrotor Flight Control — Train one PPO policy per wind-fidelity level (five levels), test every policy at every level, read the matrix. *Difference:* The claim's measurement shape and its if_false result on another axis: 'the matrix is remarkably flat', no diagonal advantage, cheapest level ranks first, rule 'fidelity investment should scale with platform wind sensitivity'.
- `2503.18229` Adaptive Multi-Fidelity Reinforcement Learning for Variance Reduction in Engineering Desi… — Weight several non-hierarchical low-fidelity models' data by their alignment with the high-fidelity policy. *Difference:* States 'manual fidelity scheduling' as a known burden being automated; design optimisation, not robot control.
*Search degraded:* ['s2', 'conference exports not built', 'complaint stream not searched (claim names no repository)', "Q4 OR list poisoned by 'coarse-to-fine' (action-discretisation sense) — recorded as a defect", "Q2 sim-to-real community with numerics words: 0 on shape, sixth occurrence of the lane's vocabulary de…

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- None until CL-W43-01's 2x2 has run; then: fund C-W43-16 (50 GPU-h) or not.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-21 — claim thought: captured in the 2026-10-21 discuss session: the systems half of L5 re-framed as the consequence of a dose-response measurement; probe rides on CL-W43-01's 2x2
- 2026-11-02 — claim thought: pressure #5 (2026-11-02): the dose's shipped values are documented by the builders — Q21 Isaac Lab Franka cube 'MJWarp solver iterations = 20, line-search iterations = 100, njmax = 2000, nconmax = 1000' at '475x for manipulation tasks'; Q20 Isaac Lab 'Keeping this number low is important for performance'; C-W44-OWN-4 (under CL-W43-01) is the fidelity-dose cousin; records Q19-Q21 routed here; stil…
- 2026-11-22 — claim killed: concept-level kill search (data/reports/2026-W47-kill-CL-W43-J02.md): killed — gate G2B (G4 fails with it); The dose half has two knob-isolated readings on its axis, both flat inside noise (2610.32277 Table 2; SimuGuard D.2), so the expected response equals the owners' sentence; the schedule half is the published recipe of adaptive multi-grid RL (2207.03253), PRDP (2502.19611) and MFPG-PPO's onli…
- 2026-11-22 — C-W43-16 killed: W47 concept-level kill search of CL-W44-08: probe verdict killed. kill clause (b) is the expected result (two flat knob-isolated readings; MJX tuning page); the fidelity-mixture recipe has no premise on the solver cap; a time-step version at fixed control period is a new record, not a redesign of this one (CL-W44-08 asked for the re-home two weeks ago and none was filed)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J02`, version 3)
- `P-W43-01-2x2`: seed or import record (no candidate yet)
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
