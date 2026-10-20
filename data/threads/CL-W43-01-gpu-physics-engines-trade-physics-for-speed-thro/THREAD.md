# GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference.

`CL-W43-01` · lane **L5** · status **open** · rank 1 · position both · refreshed 2026-10-19

## Status

Open claim. Probe C-W43-15 survived the kill search; red team owed before anything is called proper. Failing gate: none on paper; red team owed before any report (standards: nothing is proper before an independent red team). Grade on paper: golden-shaped pending probe result and red team. Next action: see First steps.

## The claim

- **Headline:** GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference.
- **Current belief (the field's):** Engine defaults (MJX/Warp capped Newton; Playground iterations=1 for Go1) are treated as adequate; 2610.17221 declines the solver axis because 'convergence is non-monotone in the outer-iteration count'; MuJoCo XML reference: 'accurate results are obtained with fewer iterations' only when warmstart is enabled (fetched 2026-10-20); Playground XMLs 'modified for performance' (iterations=1 Go1, 5 Leap)
- **If true:** Every GPU-RL robotics paper must report its solver settings and a fidelity check; engine builders expose a per-step fidelity flag; the audit becomes a standard column
- **If false:** Caps are harmless at the states policies visit — a reassuring measurement engine teams would still cite

## Scorecard (from the cheapest probe's record)

- **Target value:** Asked in print: 2610.17221 declines the SIMPLEC solver axis because 'convergence is non-monotone in the outer-iteration count' and its recipe needs a known law (card, method and limitations); the MuJoCo XML reference asserts warm-start accuracy without a number; Playground ships iterations=1 (go1_mjx_feetonly.xml). Who pays: every group choosing `iterations` in MJX/Warp/Newton, and engine teams choosing defaults.
- **Impact ceiling:** **floor**: A measured dose-response table (e vs K, e vs substep) for four Playground tasks and two policies; an engineering note others cite when choosing caps. Requires the 10 GPU-hour probe. p = 0.85 (judgment).; **middle**: The law is per state and contact-driven; a per-state fidelity tag built from n_t and the residual becomes the stated missing ingredient for fidelity scheduling in GPU RL, and the exploit heatmap shows return concentrated on cap-hit steps. Requires the bimodal result on at least two tasks. p = 0.4 (judgment).; **ceiling**: Playground or Warp adds a per-task iteration audit or changes a default; the result is the measurement half of the lane's 'iteration caps silently trade physics for speed' paper, with the scheduler as the systems half. Requires rho_L5 separation on Go1 and a real-impact validation (lane kill test 3). p = 0.1 (judgment).
- **Relevance:** Robotics and learning faculty: a measurement with a recipe consequence, direct. Systems route: the per-world rho_t and cap-hit distribution is exactly the input the iteration-level scheduler needs (lane kill test 2). Engine builders: consumers of the audit. Industry: every GPU-simulator RL shop. Jacob's edge: convergence order and numerics (theoretical physics), GPU batch behavior (computer engineering), both load-bearing. Zero for L1-L4 routes and for any LLM-agent consumer.
- **Kill probe:** Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of contact steps everywhere, or if e(K_default) < kappa on >= 99% of steps and rho_L5 does not separate the two policies.
- **Density and ownership:** Card neighbors occupy the regressor case with known laws (2610.17221, 2511.01830, 2105.00856, 2204.06684) and iteration truncation inside differentiable-physics training (PRDP 2502.19611, fetched: 'full accuracy of the network is achievable through physics significantly coarser than fully converged solvers', linear solvers, no policy). Lane neighbors: GPUSimBench 2607.13059 (distribution-level fidelity), GPUPhysBench 2609.35639 (code correctness), SAPU 2305.17110 (1 mm interpenetration threshold), Acosta RA-L 2022 (real impacts), 2304.06372 (fetched: per-engine 'physical relaxations' and numerical limitations, benchmarks of physical and computational aspects; pre-window, model-form across engines, not along a policy's states). This week's import S4xF4 (Kalman innovations) whitens and tests the audit residual; this candidate measures the dose-response the residual comes from; complementa…
- **Why now:** Capped Newton became the production path (MJX 2023, Warp 2025); Playground shipped iterations=1 for Go1 in Feb 2025; Warp exposes solver_niter per world (read 2026-10-19); 2610.17221 (Oct 2026) states the recipe that needs the law.
- **Register, and what it is not:** Measurement (a dose-response law along visited states) with a ruler consequence (what it grades first: the shipped `iterations` values in Playground model files and Isaac Lab's solver iteration defaults). It is not a new simulator, not a contact model, not a method, not a benchmark suite.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-15 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: three source types quoted — engine source and docs (Playground XMLs set caps for performance; MuJoCo docs tie low-cap accuracy to warm start), a simulator benchmark (GPUSimBench names solver early termination and contact ordering as variability sources, holds settings fixed), a meta-paper (2610.17221 App. G declines the solver axis: convergence non-monotonic in the outer iteration count) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: engine teams (expose the residual at the cap; set caps per task class), every GPU-RL robotics paper (report solver settings and an audit column), simulator benchmark owners (per-knob dose-response column) |
| G4 | mechanism and consequence | pass: mechanism — the capped Newton solve stops short on steps with many active contacts or contact-set changes, and policies trained there earn return on those steps; consequence — one geometric rate per task means fidelity is a scalar dose (2610.17221 recipe ports), a spread means per-state or per-world scheduling |
| G5 | durability; lab-adjacent | pass: a ruler on any engine and any policy generation; lab-adjacent to engine builders, not a frontier post-training problem |
| G6 | ownership, density, race window; position clause | pass after kill search of C-W43-15 (13 queries, 10 neighbors, 4 pre-window precedents, 8 limitation quotes): no in-window paper sweeps a contact solver cap along visited states; incumbents are shipped caps and Warp solver_niter; why now = MJX step + Playground checkpoints + 2610.17221 consumer; race flag on engine teams and the Ostrich authors; window (about one GPU-sim fidelity paper a month in this register) exceeds twice the 5-day probe |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-15 | Convergence law of the capped contact solve along policy-visited states | Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of contact steps ever… | survived-kill | survived-kill ([record](../../../data/reports/2026-W43-kill-C-W43-15.md)) |
| C-W43-17 | The solver's own stopping statistic as a free per-step fidelity flag | Record the Newton gradient norm at the cap on the 200k visited states in CPU MuJoCo and correlate with d_t; 6 GPU-hours (5 shared with the convergence-law candidate) plus CPU, about $20, 3 days; dead if raw Spearman < 0.3 and stiffness-sca… | proposed | — |
| C-W43-14 | Does the real winner survive the engine's speed knobs? | Pilot: 2 tasks x 3 policies x 5 iteration settings x 3 batch seeds x 100 episodes with d_t against the finest setting; ~15 GPU-hours, $0 on public assets, 5 days; dead if absolute rates move < 5 points everywhere and no resolvable pair fli… | proposed | — |
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K=1 in R_conv and rho… | proposed | — |

Also under this claim (no scorecard yet): import:2026-W43-S4xF4 and X-2026-W42-S4F4 (instrument variants of the audit; no scorecard)

## Kill search

### C-W43-15 — survived-kill (2026-10-20)
No fetched paper sweeps a GPU contact solver's iteration cap along policy-visited states or reports a per-state convergence rate; the closest work (2304.06372 fixed scenes, GPUSimBench fixed settings, Ostrich time-step axis, MFPG-PPO bundled cap) each stops one step short; survival is 'first to measure' with a race flag on engine teams and the Ostrich authors.
Full record: [`data/reports/2026-W43-kill-C-W43-15.md`](../../../data/reports/2026-W43-kill-C-W43-15.md).
Per position — **solo**: survived-kill: public checkpoints, free engine, 10 GPU-hours; nothing missing in the solo position; **lab**: survived-kill: an engine team adds the Warp residual at the cap (one field beside solver_niter) and the production task set; same measurement
**Why not done before:** an enabling piece landed: MJX's functional step (2023) and Playground's shipped per-task caps with public checkpoints (Feb 2025) make re-stepping 200k visited states at eight caps a batch job; GPUSimBench (Jul 2026) made GPU-simulator fidelity a measured object and stopped at the distribution level; 2610.17221 (Oct 2026) supplied a consumer that needs the law and declined to assume it. The question sits between communities: solver authors measure convergence on fixed scenes, RL users take the cap as a performance setting, simulator benchmarks compare engines at fixed settings.
Closest neighbors (one-sentence trick; one-line difference):
- `2607.13059` GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI — Run five GPU simulators on the same inclined-plane and ball-drop scenes at one time step, compare simulated outcome distributions to real ones, and measure how much identical worlds diverge across batch slots and repeated runs. *Difference:* Holds solver settings fixed (dt = 0.01 s) and reports distribution-level fidelity and non-determinism; names solver early termination as a noise source but never sweeps the cap; the candidate sweeps the cap per visited state and ties it to return.
- `2502.08844` MuJoCo Playground — A pip-installable MJX stack with environments and caps that trains locomotion and manipulation policies in minutes and transfers zero-shot. *Difference:* Ships iterations=1 (Go1) and 5 (Leap) and says DM-Control XMLs were 'modified for performance'; no sweep of iterations against return or transfer anywhere; the candidate measures what those caps cost.
- `2609.08800` Ostrich: Taking Large Strides Through Stiff Contact in Differentiable Dynamics — Solve hard contact with non-smooth Newton at 0.1 s time steps and differentiate the converged residual implicitly so gradients cost constant memory per step. *Difference:* Sweeps the time step against real trajectories for one wheeled scene and notes that a fixed Newton budget returns a worse iterate than an earlier one on a third of mesh-terrain steps; no iteration-cap sweep, no policy, no visited-state measurement.
- `2502.19611` PRDP: Progressively Refined Differentiable Physics — Train through an under-converged iterative linear solver and raise the iteration count only when the training loss plateaus. *Difference:* Linear solvers, PDE emulators, regressor consumer; its outlook lists the iteration-versus-accuracy relation as future work; no contact, no policy.
- `2610.02505` Multi-Fidelity Policy Gradients Stabilize Data-Scarce Reinforcement Learning — Use cheap low-fidelity rollouts only as a control variate that cancels variance in the gradient from a few high-fidelity rollouts. *Difference:* Its low-fidelity Isaac Lab simulator 'reduces the number of physics solver iterations' bundled with a coarser time step, a simplified collision model and disabled self-collisions; the cap is never isolated and no per-step error is measured.
**Probe as pre-registered (checked):** 200k visited states from public Playground checkpoints re-stepped in MJX at caps {1,2,3,5,10,20,50,100+tol 1e-8} and substeps h0/{1,2,4,8}; per-state geometric fit, rho spread, knee vs active contacts, rho_L5 for cap-1 vs cap-100 Go1; 10 GPU-hours, ~$30, 5 days; under one GPU-week. Corrections: carry the rollout's warm-start vector (qacc_warmstart) and report the cold-start arm separately; report the GPU-batch repeat-step spread as the resolution floor before reading any R^2.
*Search degraded:* s2 skipped (no key); no conference-export index built; complaint stream not searched (GitHub API unreachable from this session)

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Red team **C-W43-15** (`/redteam C-W43-15`): three personas with fetched evidence; it survives only with no unanswered objection.
2. If it survives: run the probe exactly as pre-registered — 200k visited states from public Playground checkpoints re-stepped in MJX at caps {1,2,3,5,10,20,50,100+tol 1e-8} and substeps h0/{1,2,4,8}; per-state geometric fit, rho spread, knee vs active contacts, rho_L5 for cap-1 vs cap-100 Go1; 10 GPU-hours, ~$30, 5 days; under one GPU-week. Corrections: carry the rollout's warm-start vector (qacc_warmstart) and report the cold-start arm separately; report the GPU-batch repeat-step spread as the resolution floor before reading any R^2.
3. Write the result into the probe's record and this Log; the claim's status moves only on evidence.
4. Then `/report C-W43-15` (eight sections, three decisions), and the next probe under this claim by cost.

## Decisions for Jacob

- Spend a session on the red team of C-W43-15 now, or wait for the next automatic run? (write `promote` or leave it)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded against gates 2-6: no failing gate; C-W43-15 survived its kill search (occupied_by none); claim stays open — premise half documented by shipped artifacts, exploit half untested in every fetched source; probes re-ranked by cost
- 2026-10-20 — C-W43-15 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — No fetched paper sweeps a GPU contact solver's iteration cap along policy-visited states or reports a per-state convergence rate; the closest work (2304.06372 fixed scenes, GPUSimBench fixed settings, Ostrich time-step axis, MFPG-PPO bundled cap) each stops one step short; survival is 'first to measure' with a race flag on engine tea…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-01`, version 2)
- probe `C-W43-15`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W43-kill-C-W43-15.md`
- probe `C-W43-17`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-14`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
