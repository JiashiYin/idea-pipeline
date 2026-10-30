# Frontier coding agents can speed up shipped physics engines 10-100x at fixed accuracy by generic optimisation (kernel fusion and the like), because the engines predate agents and are poorly optimised.

`CL-W43-J05` · lane **L5** · status **thought** · rank — · position solo · refreshed 2026-10-30

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

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

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-J05-a** (Sunday run), or run `/kill P-W43-J05-a` in a session.
2. If it survives: `/redteam P-W43-J05-a`, then the probe as pre-registered — Pre-registered: the '10-100x on modern engines' clause is dead if the GPU-native target gains under 2x at matched accuracy; the port clause is dead as a contribution if the ported CPU code, however much faster than itself, is slower than Genesis/Newton on the same scene. Expected (judgment): GPU-native 1.0-1.5x (p = 0.7); CPU-to-GPU port 10-50x over itself but below Genesis/Newton (p = 0.6). Cost…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Run P-W43-J05-a this week to test the collaborators' claim before any pivot is agreed?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim thought: captured from the collaborators' proposal; current belief assembled from GPUPhysBench, KernelBench-Verified, Sakana and WorldSolver fetched 2026-10-25

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J05`, version 1)
- `P-W43-J05-a`: seed or import record (no candidate yet)
