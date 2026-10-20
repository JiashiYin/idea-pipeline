# GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference.

`CL-W43-01` · lane **L5** · status **open** · rank 1 · position both · refreshed 2026-10-20

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: G1 (no live probe of the exploit clause) and headline defects (actor; exploit clause as news; 'silent'). Grade on paper: open, re-probe owed; headline rewrite owed in the next /claims run; not proper. Next action: see First steps.

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | fails as written for the exploit half: rho_L5 was a protocol artifact (kappa asymmetric by warm-start protocol; mean-action rollouts off the training protocol; number format unstated) |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | UNSATISFIED for the claim after the red team: the cheapest probe is killed and no remaining probe tests the exploit clause; the 2x2 return-matrix probe (~2-6 GPU-h, pre-registered kill: interaction inside the seed interval of zero) must be written with a scorecard |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | weakened, route A: the engine's own performance page states the trade and justifies it by DR noise (MJX docs), so the strain is asserted away rather than asserted; GPUSimBench and 2610.17221 App. G still stand as the other two source types; route B fails for the law half (expected result = the manual's description) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | unchanged if the exploit clause holds; the 'engine builders expose a per-step fidelity flag' consequence is already shipped on CPU (mjData.solver, fwdinv) and partly on Warp (solver_niter, per-world tolerance) — strike it |
| G4 | mechanism and consequence | mechanism rewritten: the Newton solve at iterations=1 is one exact step from the previous step's warm start, exact when the active set is unchanged and short when it changes; the consequence for the exploit clause is the 2x2 interaction term, not a per-state law |
| G5 | durability; lab-adjacent | unchanged (a ruler on any engine), but the hardware prior at the shipped caps is against the exploit clause (Playground: cap-1 Go1 policies transfer robustly) |
| G6 | ownership, density, race window; position clause | kill-search correction: the exploit clause is 2017 folklore (Peng et al. 1710.06537) and its cross-engine version is measured in-window by PolySim 2510.01708 (a bound; sim2sim success +52.8) — a hit inside the kill search's own Q4 set that was not opened; the cap-isolated share remains unmeasured; caps are universal (legged_gym num_position_iterations=4 since 2021), so 'GPU' is not the novelty |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-15 | Convergence law of the capped contact solve along policy-visited states | Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of contact steps ever… | killed | survived-kill ([record](../../../data/reports/2026-W43-kill-C-W43-15.md)) |
| C-W43-17 | The solver's own stopping statistic as a free per-step fidelity flag | Record the Newton gradient norm at the cap on the 200k visited states in CPU MuJoCo and correlate with d_t; 6 GPU-hours (5 shared with the convergence-law candidate) plus CPU, about $20, 3 days; dead if raw Spearman < 0.3 and stiffness-sca… | proposed | — |
| C-W43-14 | Does the real winner survive the engine's speed knobs? | Pilot: 2 tasks x 3 policies x 5 iteration settings x 3 batch seeds x 100 episodes with d_t against the finest setting; ~15 GPU-hours, $0 on public assets, 5 days; dead if absolute rates move < 5 points everywhere and no resolvable pair fli… | proposed | — |
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K=1 in R_conv and rho… | proposed | — |

Also under this claim (no scorecard yet): owed: 2x2 return matrix on Go1 rough terrain (pi_1 vs pi_100 under the training protocol, wall-clock matched, each evaluated in both engines, paired DR draws;…; import:2026-W43-S4xF4 and X-2026-W42-S4F4 (instrument variants; no scorecard)

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

**C-W43-15** — {"date": "2026-10-20", "rounds": 2, "personas": ["systems", "theory", "professor", "checklist"], "counts": {"raised": 20, "conceded": 15, "answered": 3, "open": 2}, "objections": [{"persona": "theory", "objection": "rho_L5 (share of return on steps with e_t > kappa) does not estimate exploitation: for deterministic engines J_1(pi) - J_inf(pi) = sum_t E[grad V^{pi,inf}_{t+1} . delta_t] (signed, value-weighted one-step errors), so rho_L5 can be 1 with zero exploitation and 0 with full exploitation (a sub-kappa systematic bias over 5,000 physics steps per Go1 episode).", "evidence": "argument (telescoping identity over hybrid rollouts); 2605.29032 abstract (global policy-value gap bounded by the local one-step error; Error-MDP duality)", "answer": "rho_L5 was a screening statistic; the estimator the claim needs is the 2x2 train-in/evaluate-in return matrix, which is a different experiment and kill criterion \u2014 a new candidate, not an edit allowed mid-red-team", "status": "open"}, {"persona": "theory", "objection": "The headline's cheapest probe is the 2x2 return matrix (trade = J_inf(pi_inf) - J_inf(pi_1) with a wall-clock-matched pi_1; exploit = interaction term), which the desi…

## First steps if pursued

1. Wait for the automatic kill search on **none live — 2x2 return-matrix probe owed (see decisions)** (Sunday run), or run `/kill none live — 2x2 return-matrix probe owed (see decisions)` in a session.
2. If it survives: `/redteam none live — 2x2 return-matrix probe owed (see decisions)`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Fund the 2x2 return-matrix probe on Go1 (~2-6 GPU-h; pi_1 vs pi_100 under the training protocol, cross-evaluated, paired DR draws) as the claim's cheapest honest probe, or mark the claim jacob-dropped: the exploit clause is folklore at the engine level and the hardware prior at the shipped caps is against it.
- Accept the headline rewrite in the next /claims run: 'Shipped solver-iteration caps (Playground iterations=1, legged_gym 4) carry a cap-isolated share of the sim-to-sim gap that policies trained under them exploit' — or retire CL-W43-01 and keep the CPU note.
- Whether the zero-GPU CPU note (mjData.solver residual distribution along the shipped Go1 rollout) is worth a day as a Playground README contribution; it has no paper register.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded against gates 2-6: no failing gate; C-W43-15 survived its kill search (occupied_by none); claim stays open — premise half documented by shipped artifacts, exploit half untested in every fetched source; probes re-ranked by cost
- 2026-10-20 — claim open: red team of C-W43-15 (2026-10-20): probe killed — rho_L5 is not an estimator of the return gap (the 2x2 matrix is) and the law half is the manual's own convergence statement read from a trace CPU MuJoCo logs; claim stays open with Gate 1 unsatisfied (2x2 probe owed), headline defects recorded (actor; exploit clause is Peng-2017 folklore with PolySim's in-window cross-engine measurement; 'silent')…
- 2026-10-20 — C-W43-15 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — No fetched paper sweeps a GPU contact solver's iteration cap along policy-visited states or reports a per-state convergence rate; the closest work (2304.06372 fixed scenes, GPUSimBench fixed settings, Ostrich time-step axis, MFPG-PPO bundled cap) each stops one step short; survival is 'first to measure' with a race flag on engine tea…
- 2026-10-20 — C-W43-15 killed: red team (stage 5, automatic, three personas, 20 objections: 15 conceded, 3 answered, 2 open after two rounds): killed as a probe of CL-W43-01 — rho_L5 is not an estimator of the capped-vs-converged return gap (telescoping identity: the gap is a signed, value-weighted sum of one-step errors; the 2x2 train-in/evaluate-in matrix is the estimator and is cheaper), and the 'law' half re-derives the Mu…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-01`, version 3)
- probe `C-W43-15`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W43-kill-C-W43-15.md`
- probe `C-W43-17`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-14`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-16`: `data/candidates/2026-W43.jsonl`
