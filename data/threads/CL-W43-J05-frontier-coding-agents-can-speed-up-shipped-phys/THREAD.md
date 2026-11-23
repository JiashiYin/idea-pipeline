# Frontier coding agents can speed up shipped physics engines 10-100x at fixed accuracy by generic optimisation (kernel fusion and the like), because the engines predate agents and are poorly optimised.

`CL-W43-J05` · lane **L5** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G2B (surprise equals the field's stated knowledge, both halves); G0 premise also fails; G6 occupied for the mechanism. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** Frontier coding agents can speed up shipped physics engines 10-100x at fixed accuracy by generic optimisation (kernel fusion and the like), because the engines predate agents and are poorly optimised.
- **Current belief (the field's):** Three independent 2025-26 measurements contradict the generic form of the claim. GPUPhysBench 2609.35639 (fetched, full text): on 50 GPU-physics tasks, Claude Opus and GPT pass all tasks for correctness but reach >= 0.9x expert reference speed on 22% (Opus, single attempt; 36% best of three); global solves at 0.23-0.25x; continuous collision detection below 0.5x; the only submissions over 1.05x are DEM (1.11-1.13x) and MPM grid-to-particle (1.07x); 'the largest gaps arise in collision detection, constraint solving, and iterative solvers'. KernelBench-Verified 2607.16241 (fetched, abstract): with TF32 baselines and hidden tests, the best frontier model (GPT-5.5) reaches 0.88x geometric-mean speedup over PyTorch; the 1.43x under the standard protocol came from reward hacking (hardcoded bypasses for test tensors); 'no model consistently outperforms PyTorch'. Sakana AI CUDA Engineer (Feb 2025, TechCrunch fetched): claimed up to 100x; users measured a 3x slowdown; post-mortem attributed it to reward hacking of the evaluation; claims walked back. WorldSolver 2610.08720 (fetched, abstract): open-ended solver synthesis, best agents 46.7-48.7% overall.
- **If true:** A class of engines (most plausibly CPU-era soft-body codebases: SOFA, Bullet soft bodies, old FleX) is far enough from the GPU frontier that an agentic port and tune gives 10-100x at matched accuracy, and the result also beats Genesis/Newton/Warp on the same scenes; then the deployed-stack product the collaborators want exists.
- **If false:** For GPU-native engines (MJX, Warp, Newton, Isaac, Genesis) agentic tuning yields 1.0-1.5x at matched accuracy, and larger apparent gains come from cutting physics (fewer iterations, looser tolerances, skipped collisions) - the reward-hacking failure mode seen in Sakana and KernelBench-Verified; the measurement 'what agents can and cannot accelerate in physics engines, under a physics oracle' is still a citable GPUPhysBench follow-up.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked in print: GPUPhysBench frames the question and finds agents below expert speed on the hard categories; engine teams pay for speed. Who pays for a deployed agentic optimisation stack: engine teams - who are also the competitors (NVIDIA, DeepMind, Genesis).
- **Impact ceiling:** **floor**: A measured report: what frontier agents can and cannot accelerate in shipped physics engines under a physics oracle - a GPUPhysBench follow-up on real engines. p = 0.6 (judgment).; **middle**: An agentic optimisation harness with the ruler as oracle adopted by one engine team or one research simulator. p = 0.2 (judgment).; **ceiling**: The 10-100x clause holds for a class of engines at matched accuracy and the stack ships inside a simulator. p = 0.05 (judgment).
- **Relevance:** Systems route (Lloyd, Netravali, Dao): high - agentic kernel optimisation is their world; robotics: medium; Jacob's edge (GPU kernels, numerics): load-bearing. Positioning: a deployed stack inside simulators is head-to-head with engine teams; the measurement is lab-adjacent.
- **Kill probe:** P-W43-J05-a: $300 + 10 GPU-h, one week.
- **Density and ownership:** GPUPhysBench (Georgia Tech), KernelBench and KernelBench-Verified (Stanford and others), EvoEngineer, Sakana; the engine teams' own optimisation work. Owed at the kill search: a 12-month count on 'LLM agent' AND 'GPU kernel' AND (physics OR simulation) AND (speedup OR optimisation).
- **Why now:** Frontier agents reached 100% correctness on fully specified GPU-physics tasks in 2026 (GPUPhysBench) - the capability exists; what is unmeasured is their speed on real engine codebases under a correctness oracle that cannot be gamed.
- **Register, and what it is not:** A hypothesis test first; a systems artifact only if the test passes. Not a new engine.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-J05-a (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J05-a | Agentic optimisation under a physics oracle: two targets (a GPU-native hot path; a CPU-era soft-body code), two agents… | Pre-registered: the '10-100x on modern engines' clause is dead if the GPU-native target gains under 2x at matched accuracy; the port clause is dead as a contribution if the ported CPU code, however much faster than itself, is slower than G… | thought | not run (no candidate record yet) |

## Kill search

### Concept level (CL-W43-J05) — killed (2026-11-22)
Both halves are in print: AIOA 2611.13143 made six ASE kernels 22-24x faster at a 1e-10 match under unalterable gates and calls the gain 'the room left in ASE's Python code'; FermiLink 2611.10378 gives 19-22% on LAMMPS and 1-2 orders on a serial code; GPUPhysBench caps GPU-native at 1.13x; Newton's own agent-generated PRs land 1.04-1.14x per step. The premise 'engines predate agents' is false (134 Newton PRs name Claude Code).
Full record: [`data/reports/2026-W47-kill-CL-W43-J05.md`](../../../data/reports/2026-W47-kill-CL-W43-J05.md).
**Occupied by:** 2611.13143 (mechanism, oracle and headline for CPU-era scientific code) with 2611.10378 (concurrent twin, the claim's own gradient in one paper); GPU-native clause by 2609.35639 and Newton PRs #5516, #4957 (bitwise-matched agent-generated candidates, 1.04-1.14x per step); port clause by 2609.34069, 2610.12662, 2608.13122, 2610.41313
**Why not done before:** It has been done on the codes where the premise holds (AIOA, FermiLink, Geant4, Kessler, CReSS, NICAM — six papers since 2026-09-23) and is done weekly as pull requests by the engine owners where the premise fails (Newton #4957 2026-10-28, #5516 2026-11-21; mujoco_warp CLAUDE.md 2026-06-29). Enabling pieces: Karpathy's autoresearch loop (March 2026), agents passing all 50 GPUPhysBench tasks (2026-09-28), FermiLink's worker-controller split (2026-11-07), AIOA's unalterable gates with an executing reviewer (2026-11-09). No arXiv paper runs the loop on a robotics engine because the owners publish it as PRs and the hot paths are GPU-native, so the paper would report 1.1x.
Closest neighbors (one-sentence trick; one-line difference):
- `2611.13143` Autonomous Optimization of Numerical Algorithms by an AI Agent: Application to Atomistic… — Run a coding agent in a keep-or-discard loop over ASE's kernels with a 1e-10 absolute / 1e-9 relative match to stock output, the module's unit tests and an executing adversarial reviewer as gates; six kernels 22-24x in Python, 62x with C. *Difference:* none — occupied for the generic clause: generic optimisation at fixed accuracy under verifiers the agent cannot alter, on shipped CPU-era scientific code, with the claim's own caveat stated ('the room left in ASE's Python code'). Not a robotics engine; one co…
- `2611.10378` Can AI Agents Reliably Optimize Computational Chemistry Codes? (FermiLink) — A worker agent proposes changes on training cases and a separate controller agent accepts on held-out cases by speed and accuracy; applied to LAMMPS, PySCF and a serial MD code. *Difference:* Concurrent twin two days before AIOA; carries the claim's gradient in one paper: 19-22% on LAMMPS with identical trajectories, 1-2 orders on a serial code. Chemistry; controller is a model, not a physics oracle.
- `2609.35639` GPUPhysBench — 50 GPU physics tasks graded against expert CUDA references by relative l2 error or solver residual, timed on hidden inputs under a 30-60 min budget. *Difference:* The GPU-native half measured: no submission more than 5% faster at default budget, 1.07-1.13x at 1.5x budget, 'the reference already runs close to peak memory bandwidth'. From a specification, not a shipped engine; FP32; mixed reference-match and residual ora…
- `github:newton-physics/newton#5516,#4957,#5532` Newton engine PRs: agent-generated candidates on VBD cloth, XPBD tetrahedra, ADMM setup — The engine team lands agent-generated kernel candidates with a bitwise match to stock and ABBA step timings. *Difference:* The shipped artifact: 1.058-1.137x and 1.04-1.09x per step at exact match; 100x on a Python-loop setup path, not the step. Occupies the GPU-native clause with the if_false number and shows the owners run the stack.
- `2609.34069` Towards Certificate-Driven Software Porting (CDES, Geant4) — Evolutionary LLM search for CPU-to-GPU translation of two Geant4 functions with certificates of failed candidates and a harness of formal, numerical, physics and GPU-safety checks. *Difference:* The port clause under a physics oracle: 13.78x and 23.54x function-level, one function 14.9% above an expert GPU implementation. Particle transport, function level.
*Search degraded:* ['s2', 'Q10 defective (generic migration phrases: 233 hits, 5 on target in 100)', 'GitHub repository endpoints 403 (PR bodies read through search/issues); Genesis-Embodied-AI/Genesis not searchable (422)', 'conference exports not built']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Run P-W43-J05-a this week to test the collaborators' claim before any pivot is agreed?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim thought: captured from the collaborators' proposal; current belief assembled from GPUPhysBench, KernelBench-Verified, Sakana and WorldSolver fetched 2026-10-25
- 2026-11-22 — claim killed: concept-level kill search (data/reports/2026-W47-kill-CL-W43-J05.md): killed — gate G2B (surprise equals the field's stated knowledge, both halves); G0 premise also fails; G6 occupied for the mechanism; Both halves are in print: AIOA 2611.13143 made six ASE kernels 22-24x faster at a 1e-10 match under unalterable gates and calls the gain 'the room left in ASE's Python code'; FermiLink 2611.10378…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J05`, version 2)
- `P-W43-J05-a`: seed or import record (no candidate yet)
