# At the solver budgets MuJoCo Playground ships (Go1 iterations=1, Leap iterations=5), the cap-isolated share of return — the train-in / evaluate-in interaction at matched wall-clock — is inside the seed interval of zero for Go1 locomotion and is X percent of return for Leap cube manipulation, and that Leap share is attributable to the solver budget and not to the collision pipeline. (Exploit defined as 2605.15960's preference reversal; quantity is SPOTA's bias with the converged engine as the held-out domain.)

`CL-W44-08` · lane **L5** · status **open** · rank 1 · position both · refreshed 2026-11-03

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed next week); P-W43-01-2x2 still needs a scorecarded candidate record. Next action: see First steps.

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

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-01-2x2** (Sunday run), or run `/kill P-W43-01-2x2` in a session.
2. If it survives: `/redteam P-W43-01-2x2`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

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

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-08`, version 2)
- `P-W43-01-2x2`: seed or import record (no candidate yet)
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-27`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-14`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-14`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-OWN-4`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-DEF-L5`: `data/candidates/2026-W44.jsonl`
