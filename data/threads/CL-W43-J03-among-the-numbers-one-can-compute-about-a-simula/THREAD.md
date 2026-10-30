# Among the numbers one can compute about a simulator without a robot, the fidelity scores engines report predict policy transfer worst, and the worst-case physical violation a budgeted optimiser can extract predicts it best.

`CL-W43-J03` · lane **L5** · status **thought** · rank — · position solo · refreshed 2026-10-30

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Among the numbers one can compute about a simulator without a robot, the fidelity scores engines report predict policy transfer worst, and the worst-case physical violation a budgeted optimiser can extract predicts it best.
- **Current belief (the field's):** Engines and simulator benchmarks report average fidelity on chosen motions: GPUSimBench 2607.13059 (fetched) scores distributional alignment of an inclined-plane task with real data; RGBench 2511.06434 (fetched) scores simulated garment dynamics against measured real ones and reports a 20 percent error reduction; 2603.14634 (fetched) ships analytical-solution tests for rigid bodies. Policy-Aware Simulator Learning 2605.29032 (fetched) argues the right objective for LEARNED simulators is strategic robustness to an adversarial policy rather than predictive accuracy, and proves the worst-case policy is dual to RL on the critic's one-step error - the same move for engineered simulators is unmeasured. Whether any reported fidelity number predicts sim-to-real transfer is, in the fetched set, untested (density check at the kill search; arXiv API throttled on 2026-10-23).
- **If true:** Engine releases and simulator benchmarks report an exploitability curve beside fidelity; robot-RL authors quote it when they claim transfer; synthetic-data and world-model builders audit their generators with it; the ruler becomes a reviewer's ask.
- **If false:** Either both predict (then the cheap fidelity number suffices and the adaptive layer is a service) or neither does (then transfer is governed by modelling error outside the engine's numerics, a result that redirects the lane to validation against real data).

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked: every robot-RL paper that claims transfer quotes a simulator with no number for how much that simulator can be gamed; 2605.29032 states the objective should be robustness to an adversarial policy but measures it only for learned models; GPUSimBench (fetched) names fidelity, scalability and determinism and stops before transfer. Who pays: engine teams (what to report), robot-RL authors (what to quote), synthetic-data labs (what to audit).
- **Impact ceiling:** **floor**: A correlation table over tens of policy-sim-real triples, with intervals; a note cited when fidelity numbers are quoted. p = 0.6 (judgment).; **middle**: Exploitability predicts and fidelity does not: simulator benchmarks add the curve, and 'report exploitability' becomes a reviewer's ask in robot RL. p = 0.25 (judgment).; **ceiling**: The ruler becomes the standard card engines ship per release, with the agent-ported scene set; the standards artifact of the lane. p = 0.1 (judgment).
- **Relevance:** L5 direct; L1 (benchmark validity) direct - this is benchmark validity for simulators; robotics faculty and engine teams direct; systems route through the adversary infrastructure; Jacob's edge (numerics, conservation laws, GPU batching) load-bearing. Zero for LLM-agent consumers.
- **Kill probe:** P-W43-J03-a above: $0 fidelity side, 20-60 GPU-h exploitability side, 3 weeks; dead if neither predicts or both predict equally.
- **Density and ownership:** To be measured at the kill search (arXiv API throttled 2026-10-23). Fetched neighbours: GPUSimBench, GPUPhysBench, RGBench, PBD-R 2603.14634, IcFuzz 2608.06088 (fuzzes Isaac Sim for crashes with LLM stage segmentation), Policy-Aware Simulator Learning 2605.29032, 2610.00415. Race flags: the GPUSimBench team (soft-body extension), NVIDIA Newton validation, the 2605.29032 group.
- **Why now:** Minutes-scale GPU training makes budgeted adversarial search per engine-task affordable (Playground 2025); learned-simulator work (2605.29032, May 2026) has just stated the adversarial objective in theory; the public real-to-sim tables that make the correlation computable without hardware appeared in 2026.
- **Register, and what it is not:** Measurement (benchmark validity for simulators) with a standards consequence. Not a new simulator, not a benchmark suite, not a world-model paper.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-J03-a (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J03-a | Horse race of trace-free predictors on the public paired sim/real policy tables (R2S-Eval n=20, SimFoundry n=25, Kaedim… | Pre-registered: dead if no predictor reaches Spearman 0.3 with the gap (all trace-free numbers are services), dead as a headline if fidelity or sim-to-sim robustness predicts as well as X (the adaptive layer adds nothing). Expected (judgme… | thought | not run (no candidate record yet) |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-J03-a** (Sunday run), or run `/kill P-W43-J03-a` in a session.
2. If it survives: `/redteam P-W43-J03-a`, then the probe as pre-registered — Pre-registered: dead if no predictor reaches Spearman 0.3 with the gap (all trace-free numbers are services), dead as a headline if fidelity or sim-to-sim robustness predicts as well as X (the adaptive layer adds nothing). Expected (judgment): fidelity under 0.2, sim-to-sim robustness 0.3-0.5, X above 0.5 on contact-rich tasks. Power: tens of triples; report intervals; the register is a first cor…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Is claim A the headline experiment of the program (it decides whether the ruler is mandatory or a service), run before any engine-ranking paper?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-23 — claim thought: captured in the 2026-10-23 session on the meta-benchmark; consequence claim of the ruler; kill search owed
- 2026-10-24 — claim thought: Jacob's critiques answered (program note addendum): incumbents inspected, functionals are self-consistency against the declared model, adversary = calibrated optimiser portfolio on an auxiliary MDP, both capacity and realised exploitation reported
- 2026-10-24 — claim thought: kill search (concept-level, data/reports/2026-W43-kill-CL-W43-J03-J04.md): survived-kill, weak; redesigned as a horse race of trace-free predictors incl. RoboGauge-style sim-to-sim robustness and GAUGE fidelity; headline reworded; exploitability defined against game theory, MBRL model exploitation, 2605.15960, 2605.29032; still a thought until a probe runs

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J03`, version 3)
- `P-W43-J03-a`: seed or import record (no candidate yet)
