# At the solver budgets MuJoCo Playground ships (Go1 iterations=1, Leap iterations=5), the cap-isolated share of return — the train-in / evaluate-in interaction at matched wall-clock — is inside the seed interval of zero for Go1 locomotion and is X percent of return for Leap cube manipulation, and that Leap share is attributable to the solver budget and not to the collision pipeline. (Exploit defined as 2605.15960's preference reversal; quantity is SPOTA's bias with the converged engine as the held-out domain.)

`CL-W44-08` · lane **L5** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 2B (route B ruler: expected result equals the field's assumption); Gate 5 also fails for golden (numbers expire with the next Playground release; MJWarp early exit removes the caps' performance motive). Next action: see First steps.

## The claim

- **Headline:** At the solver budgets MuJoCo Playground ships (Go1 iterations=1, Leap iterations=5), the cap-isolated share of return — the train-in / evaluate-in interaction at matched wall-clock — is inside the seed interval of zero for Go1 locomotion and is X percent of return for Leap cube manipulation, and that Leap share is attributable to the solver budget and not to the collision pipeline. (Exploit defined as 2605.15960's preference reversal; quantity is SPOTA's bias with the converged engine as the held-out domain.)
- **Current belief (the field's):** MJX documentation (grep-verified in the kill report): 'Accurate solver forces are not so important in reinforcement learning in which domain randomization is often used to add noise'
- **If true:** Engine builders and robot-RL groups report the cap-isolated return share at shipped budgets; Playground's shipped caps carry a measured consequence per task class
- **If false:** The cap-isolated share is inside the seed interval of zero on both tasks: the shipped caps are free and the lane's exploit premise moves to the collision pipeline (SimuGuard's finding)

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** —
- **Impact ceiling:** —
- **Relevance:** —
- **Kill probe:** —
- **Density and ownership:** —
- **Why now:** —
- **Register, and what it is not:** measurement; inherits the parent's scorecard with the neighbours' numbers; to be rewritten at its own kill search

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | warm start, dtype and the collision pipeline are part of the state (checklist 2026-10-20, SimuGuard 2610.41857) |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: 6-14 GPU-h |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler is the 2x2 interaction at matched wall-clock; the owners' stated assumption is that caps are free under DR |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; SimuGuard (three days old) audits frozen policies and never retrains — the train-in/evaluate-in interaction is the open cell |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-01-2x2 | P-W43-01-2x2 (redesigned: third training arm with the collision pipeline changed so the interaction is attributed; 6-14… | — | — | not a candidate record (seed or import) |
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K=1 in R_conv and rho… | proposed | — |
| C-W43-27 | Price the lockstep barrier in batched GPU physics from the solver's own iteration log | Half a day of source reading, then 4 tasks x 3 checkpoints x 1000 steps x 4096 worlds with the cap lifted plus an eight-point timing sweep, about 8 GPU-hours (about $30), 4 days; kills if the Amdahl upper bound $S < 1.15$ on all four tasks… | proposed | — |
| C-W43-14 | Does the real winner survive the engine's speed knobs? | Pilot: 2 tasks x 3 policies x 5 iteration settings x 3 batch seeds x 100 episodes with d_t against the finest setting; ~15 GPU-hours, $0 on public assets, 5 days; dead if absolute rates move < 5 points everywhere and no resolvable pair fli… | proposed | — |
| C-W44-14 | Re-solve what the agent shipped: the per-command physics audit on agent-written simulators | Six simulations, 50 initial states each, per-command re-solve at $(h/2, 2K, 2m)$ and end-to-end refined runs, a second refinement level on the two worst; about 120 GPU-hours, about $300, 10 days; dead if median $d_k / \kappa < 0.1$, $\rho… | proposed | — |
| C-W44-OWN-4 | How much of MuJoCo Warp's batched Newton solve is waiting for the slowest world: the per-world iteration distribution t… | The histogram and wait share on the nightly box (1 GPU-hour, one day) and the compacted-launch prototype (one engineer-week); dead if $W < 0.15$ everywhere and solve time moves under 10%. | parked | — |
| C-W44-DEF-L5 | Reference return versus solver budget: the compute-matched comparison of shipped fidelity settings across five GPU engi… | The 90 GPU-hour one-engine sweep; dead if the shipped cap's reference return is within 5% of the converged cap's and the exploit share does not separate the policies. | parked | — |

## Kill search

### Concept level (CL-W44-08) — killed (2026-11-08)
Gate 2B: after 2610.32277 (solver-iteration row flat, time step and floor decisive, cap-trained MuJoCo policy), SimuGuard (more iterations raised success; collision constant decisive) and Playground's own Leap attribution to collision geometry, the honest expected result equals the owners' stated assumption on both tasks; the 2x2 at shipped caps is a documentation service, unoccupied but not a paper.
**Occupied by:** none on the exact shape (one solver knob, retrain both ways, cross-evaluate at matched wall-clock, attribute). Coarser shapes occupied: frozen-policy rerun under a solver-iteration change — 2610.32277 (MuJoCo, solver row flat, time step decisive) and 2610.41857 SimuGuard (PhysX, sign against exploitation, collision constant decisive); bundled train-in-LF / evaluate-in-HF with task contrast — 2610…
**Why not done before:** enabling pieces landed: Playground caps with checkpoints (2025-02), MuJoCo 3.11.0 certificate (2026-07-27), SimuGuard reruns (2026-10-30), 2610.32277's verified-harness one-at-a-time attribution protocol (2026-10-23); unrun because each of the three communities holds the answer and now a published datum agreeing with it (MJX page; 2610.32277 Table 2; SimuGuard D.2-D.3), so the measurement's expected reading is the belief.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.32277` Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers — Train humanoid motion trackers in mjlab (MuJoCo Warp), export them to an independent CPU MuJoCo harness rebuilt from the robot description, restore the training model's settings one at a time until the harness reproduces training, then stress-test command del… *Difference:* The frozen-policy exploit cell for a cap-trained MuJoCo policy, attributed one knob at a time: solver iterations 0.577 -> 0.577 rad, time step 0.577 -> 1.719, floor -> 6.969 (Table 2); no retraining at the second setting, iteration counts not printed, one hum…
- `2610.02505` Multi-Fidelity Policy Gradients Stabilize Data-Scarce Reinforcement Learning — Use abundant rollouts from a simplified Isaac Lab configuration (5x coarser time step, solver iterations 4->2 and 4->0, self-collisions off, simplified collision geometry) as a control variate for the high-fidelity PPO gradient, and report the LF-only policy… *Difference:* The train-in-LF / evaluate-in-HF cell with a task-class contrast (easy on ANYmal-D, hard on H1) with the solver knob bundled with time step and collision model; no reverse cell, no wall-clock matching, no attribution; the per-knob split is not in its future w…
- `2610.41857` When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot B… — Record every physics step of benchmark rollouts, flag objects that gain speed at a contact faster than the robot or gravity can supply, replay bit for bit, rerun with one engine parameter changed. *Difference:* Frozen policies on PhysX and MuJoCo; the one manipulation rerun under a solver-iteration change has the sign against exploitation (74.4% -> 86.7% success with more iterations; artefact removed by a collision constant). Never retrains. Inherited from the paren…
- `2502.08844` MuJoCo Playground — Ship MJX environments with per-task XML changes to solver iterations, line-search iterations and contact parameters, train in minutes, deploy zero-shot on Go1, G1, T1, Berkeley Humanoid, Leap and Franka. *Difference:* Owner of the shipped caps and the hardware prior; Leap failures attributed by the owners to wedging, hardware flex and collision geometry, not the solver; no solver sweep.
- `2511.06667` Rapidly Learning Soft Robot Control via Implicit Time-Stepping — Train soft-manipulator policies in an implicit soft-body simulator and in Elastica, evaluate each policy in the other, and show the implicit stepper's speed-up costs no cross-simulator accuracy. *Difference:* The train-in / evaluate-in matrix as the test of a numerics choice (implicit vs explicit), soft bodies, two engines not one knob, no wall-clock-matched retraining, no contact-solver cap.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- C-W44-OWN-4 is parked — access to the MuJoCo Warp nightly machine and its per-world solver_niter arrays, or a stated need from the MJWarp / Newton maintainers: fund it, or leave it parked?
- C-W44-DEF-L5 is parked — lab compute of >= 2200 GPU-hours and a shared harness (one MJCF task set that loads unchanged into MJX, MuJoCo Warp, Newton, Genesis and Isaac Lab behind one PPO code path, about three person-months): fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-01 — claim open: filed as the narrowest surviving headline of CL-W43-01 (killed at concept level the same day); its own concept-level kill search is owed next week (W44 budget of 12 spent) before any probe is designed (rule 17)
- 2026-11-01 — claim open: ranked 1 after the W44 kill searches: lane program narrowed to the measurable cell; cheapest probe 6-14 GPU-h; consumers: engine builders and every Playground user
- 2026-11-01 — C-W44-OWN-4 parked: stage 8 owned-artifact prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-OWN-4 parked: claim CL-W43-01 concept-level kill search (killed): probe effect 'unchanged' — parked, lab; cite the MJWarp early-exit sentence in its scorecard
- 2026-11-01 — C-W44-OWN-4 parked: claim_id CL-W43-01 -> CL-W44-08 (re-homed after the kill searches)
- 2026-11-01 — C-W44-DEF-L5 parked: stage 9 definitive-comparison prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-DEF-L5 parked: claim CL-W43-01 concept-level kill search (killed): probe effect 'unchanged' — parked, lab; must cite SPOTA (quantity), 2605.15960 (definition) and SimuGuard (rerun protocol, collision confound) before any report
- 2026-11-01 — C-W44-DEF-L5 parked: claim_id CL-W43-01 -> CL-W44-08 (re-homed after the kill searches)
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 1 -> 2; ranked 2 (was 1): lane program narrowed to the measurable cell, 6-14 GPU-h, engine builders and every Playground user as consumers; below CL-W45-J01 only because its own kill search is still owed and its numbers expire with the next Playground release
- 2026-11-08 — claim killed: concept-level kill search (data/reports/2026-W45-kill-CL-W44-08.md): killed — Gate 2B: after 2610.32277 (solver-iteration row flat, time step and floor decisive, cap-trained MuJoCo policy), SimuGuard (more iterations raised success; collision constant decisive) and Playground's own Leap attribution to collision geometry, the honest expected result equals the owners' stated assumption on both task…
- 2026-11-08 — C-W44-OWN-4 parked: W45 concept-level kill search of CL-W44-08 (data/reports/2026-W45-kill-CL-W44-08.md): survives (parked, lab; unchanged)
- 2026-11-08 — C-W44-DEF-L5 parked: W45 concept-level kill search of CL-W44-08 (data/reports/2026-W45-kill-CL-W44-08.md): survives (parked, lab; must cite 2610.32277 Table 2 and MFPG-PPO's settings table)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-08`, version 4)
- `P-W43-01-2x2`: seed or import record (no candidate yet)
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-27`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-14`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-14`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-OWN-4`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-DEF-L5`: `data/candidates/2026-W44.jsonl`
