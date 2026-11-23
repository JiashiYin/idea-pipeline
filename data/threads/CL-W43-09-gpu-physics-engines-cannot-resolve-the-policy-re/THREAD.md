# GPU physics engines cannot resolve the policy-return differences that robot-RL papers report as improvements: engine-only repeatability and batch-position variance exceed 30% of the policy-to-policy spread on contact-rich tasks.

`CL-W43-09` · lane **L5** · status **killed** · rank None · position both · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: Gate 2B (GPUSimBench 2607.13059 owns the premise and magnitudes; MJX and Genesis 0.00 drift); Gate 0 (the per-episode noise is already inside the reported seed interval); Gate 4 (the consequence shipped: Warp/Newton/MuJoCo Warp deterministic modes, Isaac Lab --deterministic). Grade on paper: open. Next action: see First steps.

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
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: %GRR and ndc are identifiable with deterministic frozen policies (temperature 0 by construction, so the policy contributes no decision variance); pre-registered surprise — expected %GRR above 30% on contact-rich tasks at batch sizes >= 4096, field assumes seed variance is the algorithm's, the ruler is a service if %GRR is under 10% everywhere; 2026-11-02, pressure #5: the engine documentation itself names the non-determinism and overflow regimes (Q19 'If warnings are disabled and Data.overflow is not checked, overflows will lead to undefined behavior'); Q21 quotes speedups with… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: robot-RL authors, engine builders, simulation leaderboard owners, reproducibility researchers |
| G4 | mechanism and consequence | pass: mechanism — floating-point reduction order under GPU thread scheduling flips contact ordering and diverges on contact-rich states; consequence — a minimum reportable gap per task, or a certified deterministic mode |
| G5 | durability; lab-adjacent | pass: a ruler on any engine; lab-adjacent to engine builders |
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W43-09.md): killed; gate failed G2B; occupied_by none (premise: 2607.13059; mechanism and consequence: Newton docs/concepts/determinism.rst 2026-11-03, mujoco_warp #1925 2026-11-08, IsaacLab #3824 2025-10-24; signal-vs-repeat ratio shape: 2609.34666); why not done: The owners chose removal over measurement: three engines shipped deterministic modes in Aug-Nov 2026 for regression tests and replay; the per-episode component is not a floor because the reported statistic averages it, and the configuration-level shift that could b… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-09-lit | Day-1 literature table ($0): for 20 recent GPU-simulator robot-RL papers, tabulate the reported improvement, the seed i… | Dead as a headline if fewer than 10% of reported improvements fall inside the engine divergence (then the floor is a footnote); pre-registered expectation (judgment): 20-40% on contact-rich tasks. Lesson from CL-W43-02: the quantifier is m… | thought | not run (no candidate record yet) |

Also under this claim (no scorecard yet): import:2026-W43-S4xF9 (gauge R&R on 10 checkpoints x 50 states x repeats x slots x batch sizes x 2 GPUs; <30 GPU-h; no scorecard)

## Kill search

### Concept level (CL-W43-09) — killed (2026-11-15)
Per-episode engine noise enters the reported mean over N resets as sigma_omega/sqrt(N) and is already inside the reported interval, so the headline's quantity is the probe protocol's, not the statistic papers report (G0); the premise and its per-engine magnitudes are GPUSimBench's and the owners' own text, with MJX and Genesis measured 0.00 on both metrics (G2B); the if_true consequence, a certified deterministic mode, shipped in Warp 1.19 / Newton 1.8 / MuJoCo Warp DeterminismType / Isaac Lab --deterministic between 2026-08 and 2026-11 without the measurement (G4); the $0 literature table's third column has no source in return units (G1).
Full record: [`data/reports/2026-W46-kill-CL-W43-09.md`](../../../data/reports/2026-W46-kill-CL-W43-09.md).
**Occupied by:** none (premise: 2607.13059; mechanism and consequence: Newton docs/concepts/determinism.rst 2026-11-03, mujoco_warp #1925 2026-11-08, IsaacLab #3824 2025-10-24; signal-vs-repeat ratio shape: 2609.34666)
**Why not done before:** The owners chose removal over measurement: three engines shipped deterministic modes in Aug-Nov 2026 for regression tests and replay; the per-episode component is not a floor because the reported statistic averages it, and the configuration-level shift that could be a floor has no datum in return units for or against it.
Closest neighbors (one-sentence trick; one-line difference):
- `2607.13059` GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI — Run seven GPU simulators on one real-matched incline scene with seeds fixed and randomisation off, and measure how far identical environments drift inside a batch and how far whole runs drift from each other, sorting engines into four regimes. *Difference:* Owns the premise and its per-engine magnitude at N_env=16 (Isaac Lab parallel 4.21 cm vs 5.40 cm to reality; MJX and Genesis 0.00 on both metrics); no policy, no return, no batch-size axis; the confound is a guideline sentence, not a measurement against an ef…
- `2609.34666` On the Numerical Reliability of Differentiable Physics-Based Optimization for Robotic Mat… — Show that scheduling-dependent GPU sums flip the sign of long-horizon MPM gradients and that the perturbation-induced loss change falls from 93-806 times the repeated-run spread at two steps to 2-14 times at ten or more. *Difference:* The signal-to-repeat-spread ratio in print for soft-body gradients; not rigid-body return, no batch-size or slot axis; recommends deterministic accumulation, not an acceptance criterion.
- `newton-physics/newton docs/concepts/determinism.rst (PR #5041, 2026-11-03; epic #5049)` Deterministic Simulation — Document per-solver RUN_TO_RUN determinism, its sources (atomics, slot allocation), its scope and its cost, checked by comparing two independent 100-step rollouts bitwise in fresh processes. *Difference:* The owners' statement of the mechanism and the shipped consequence; measures bitwise equality, never the drift's size in a task unit.
- `google-deepmind/mujoco_warp #562 (2025-07-31), #1925 (2026-11-08)` Determinism; Complete contact and constraint ordering behind DeterminismType.ALL — A user request for a determinism option, then DeterminismType.ALL with canonical contact and constraint ordering: 0.000796 m maximum inter-run root difference on G1 over 100 control steps before, bitwise identical after. *Difference:* The one engine-only drift number in a robot-state unit; no return, no policy comparison.
- `isaac-sim/IsaacLab #3824 (2025-10-24) and docs/source/how-to/reproducibility.rst` Reproducibility: Physics depend on environment index / permutation — Permute environment indices with seed and initial states fixed and get a 0.35 m maximum state error on a cone after 1000 steps; 'This breaks benchmarking: eval(poses) != eval(randperm(poses))'. *Difference:* The batch-position clause posed as a complaint in state units; the owners' page states run-to-run determinism for rigid bodies on fixed hardware and ships --deterministic.
*Search degraded:* ['s2', 'conference-exports (not built)', 'Q7 (HTTP 503 x2)', 'Q8 (Rate exceeded x2)', 'Genesis tracker (not searchable from this session)', 'IsaacLab PR #940 (referenced by the docs, not retrievable)']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim open: new claim from import:2026-W43-S4xF9 (gauge R&R); second L5 claim this week
- 2026-10-21 — claim open: discuss session with Jacob (2026-10-21): this is the resolution-floor claim of the L5 program; literature table P-W43-09-lit written as the $0 first step (quantifier before headline, per CL-W43-02's refutation); noted as the twin of CL-W43-J01
- 2026-10-25 — claim open: claims (closing W43): re-ranked to 12 — no new probe, Gate 6 still not established; scorecards still owed on import probes
- 2026-11-01 — claim open: ranked 7 after the W44 kill searches: Gate 1 blocked on paperwork
- 2026-11-02 — claim open: pressure #5 (2026-11-02): Q19 MJWarp docs on overflow as undefined behaviour and the all-worlds early exit; Q21 Newton '252x [...] 475x' with no accuracy number; records Q19-Q21 routed here as the premise in the builders' words
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): no new probe; P-W43-09-lit ($0, 2 d) still the first step and still unrun; rank 12 -> 15
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 7 -> 16; ranked 16 (was 7): Gate 1 still blocked on paperwork; no new probe
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 5: kill search owed; Gate 1 blocked on paperwork
- 2026-11-15 — claim open: claims (W46, 2026-11-15): rank 5 -> 12; kill search owed; Gate 1 blocked on paperwork
- 2026-11-15 — claim killed: concept-level kill search (data/reports/2026-W46-kill-CL-W43-09.md): killed — gate G2B; Per-episode engine noise enters the reported mean over N resets as sigma_omega/sqrt(N) and is already inside the reported interval, so the headline's quantity is the probe protocol's, not the statistic papers report (G0); the premise and its per-engine magnitudes are GPUSimBench's and the owners' own text, wit…
- 2026-11-15 — claim killed: failing gate recorded after the W46 kill search: Gate 2B (GPUSimBench 2607.13059 owns the premise and magnitudes; MJX and Genesis 0.00 drift); Gate 0 (the per-episode noise is already inside the reported seed interval); Gate 4 (the consequence shipp

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-09`, version 10)
- `P-W43-09-lit`: seed or import record (no candidate yet)
