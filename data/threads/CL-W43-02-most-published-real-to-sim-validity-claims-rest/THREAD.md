# Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.

`CL-W43-02` · lane **L1** · status **refuted** · rank 2 · position solo · refreshed 2026-10-25

## Status

A probe came out against the claim. Failing gate: G1, G2B, G4; headline refuted on three tables (resolvable fraction 63/71/68%). Grade on paper: refuted as worded; residue is a service (methods note + PR); not re-seeded. Next action: see First steps.

## The claim

- **Headline:** Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.
- **Current belief (the field's):** Real-to-sim papers report rank agreement as point estimates over a handful of pairs (YUBI 2610.17521: 9 pairs, no interval; PhAIL 2605.29710 on cohort sizes); YUBI IV: its Wilson intervals 'are not confidence intervals for ranking accuracy or tests of the difference between policies'; 2606.10366 4.1: '5 real-world rollouts for each policy, task, and perturbation dimension'; Kaedim 2610.00731 App. B: 'We do not report MMRV on this basis'
- **If true:** Real-to-sim validation papers report resolvable fraction and chance-corrected agreement; benchmark owners publish the sample-size table
- **If false:** Rank agreement is robust even on unresolvable pairs — then the field's practice is fine and the note says so

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked for in print: YUBI 2610.17521 ('These results do not yet establish a generally reliable scene-acceptance rule'; point estimates over 9 pairs, no interval); PhAIL 2605.29710 ('these cohort sizes struggle to resolve close comparisons reliably'); Robot Learning as an Empirical Science 2409.09491 (success rate reported 'with little to no information regarding the number of runs'). Who pays: every group selecting VLA checkpoints in a reconstructed simulator (Physical Intelligence, Google DeepMind robotics, NVIDIA GEAR, the SIMPLER/ManiSkill maintainers) and every reviewer reading a real-to-sim correlation table.
- **Impact ceiling:** **floor**: A two-page re-analysis note: resolvable fraction and agreement split for 5-7 published tables plus the sample-size table; requires only the tables; p ~0.85 (judgment) that the SIMPLER-style split reproduces in at least two more papers.; **middle**: A measurement paper: 'resolvable pairs' and chance-corrected agreement become the reported columns for real-to-sim validity, adopted by the SIMPLER metrics file and one 2026 follow-up; requires the 2026 same-family papers to show < 40% resolvable; p ~0.35 (judgment).; **ceiling**: A standard: real-to-sim papers report (n_real, resolvable fraction, kappa) and hardware budgets are set from the sample-size rule; requires one lab to run the new-trials check and one benchmark (PhAIL or RoboArena) to adopt the column; p ~0.10 (judgment).
- **Relevance:** Narasimhan (tau-family) and HAL: the same attenuation argument applies when a cheap proxy (simulated user, LLM judge) is validated against a small human-rated criterion; the ruler transfers as a template, the data do not. Evaluators and benchmark owners: direct (a column). Industry: checkpoint-selection teams in robotics, direct. Jacob's edge: error propagation and reliability bounds are physics habits; the computer-engineering edge is zero here, and so is the systems route.
- **Kill probe:** Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or unresolvable-pair agreement >= 0.9.
- **Density and ownership:** arXiv API 2026-10-19, 12-month window: 'real-to-sim' AND (correlation OR rank) AND policy evaluation = 7 hits, all pipelines reporting a correlation, none grading its ceiling; (simulat*) AND 'policy evaluation' AND ('confidence interval' OR 'statistical power' OR 'sample size' OR reliability) AND robot AND real = 0; sim-to-real AND (kappa OR inter-rater OR attenuation OR test-retest OR psychometric) = 0; robot policy evaluation AND (CI OR power OR 'number of trials' OR 'sequential test') = 4 in window (AnyRank 2610.14603: sequential multi-policy ranking from hardware trials with an optional sim prior, prior is not graded; PhAIL 2605.29710: real-only leaderboard with KS test and bootstrap CIs; two off-topic). Pre-window precedents: Snyder et al. 2503.10966 (sequential two-policy comparison, near-optimal stopping, real-only), 2409.09491 (best-practice statistics), SureSim 2510.04354 (pred…
- **Why now:** PhAIL (2026-05-28) and AnyRank (2026-10-10) made real-side statistics a live topic; YUBI (2026-10-13) stated the interval gap in its own text; seven real-to-sim validity claims in 12 months form the sample; SIMPLER's public REAL_PERF table (fetched 2026-10-19) makes the first computation free.
- **Register, and what it is not:** Ruler / measurement with a recipe consequence (how many real trials to buy). It is not a new estimator (AnyRank, SureSim own that), not a benchmark, and not a simulator-fidelity method.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | fails: neither pre-registered outcome is informative about the simulator (a perfect simulator produces both thresholds); the kill that fired on two 2026 tables was mis-specified as 'the binomial model is wrong' |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | fails route B: the expected result equals the field's stated assumption (2409.09491, SIMPLER III-B, Kaedim App. B, PhAIL, Snyder) — service, not a paper; route A's quotes still describe the practice, not a strain anyone disputes |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community at best (note + PR to simpler_env metrics.py); adoption evidence negative (the 2024 best-practice ask is ignored by the 2026 cohort) |
| G4 | mechanism and consequence | fails: the stated consequence of each outcome is wrong (high unresolvable-pair agreement is the perfect-sim prediction, not 'the sims are better than the real tests') |
| G5 | durability; lab-adjacent | n/a after refutation |
| G6 | ownership, density, race window; position clause | kill-search misses recorded: Snyder 2503.10966 Supp. Table II (the sample-size table), RoboArena Fig. 6-7 / AutoEval / VLA-REPLICA (real-real repeatability; Q7 reported one hit), 2604.24018 (precursor of the betting certificate) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-13 | Resolvable pairs: the noise ceiling on real-to-sim rank agreement | Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or unresolvable-pair… | killed | survived-kill ([record](../../../data/reports/2026-W43-kill-C-W43-13.md)) |

## Kill search

### C-W43-13 — survived-kill (2026-10-20)
no fetched paper grades published real-to-sim agreement against real-trial resolvability or chance; the closest, Kaedim 2610.00731 App. B, applies the check to its own five tasks to withhold MMRV, so the mechanism exists at single-study scale and the field-wide ruler with kappa, the attenuation ceiling and the sample-size table does not
Full record: [`data/reports/2026-W43-kill-C-W43-13.md`](../../../data/reports/2026-W43-kill-C-W43-13.md).
Per position — **solo**: survived-kill: public tables, $0, 2 days; the whole probe is solo-feasible; **lab**: survived-kill: a lab with a robot adds new real trials on the unresolvable pairs to test the sample-size rule and the binomial model against repeated real batches
**Why not done before:** an enabling piece landed: Kaedim 2610.00731 App. B (2026-09-30) applied the per-pair resolvability check to withhold MMRV, and the 2026 same-family cohorts shrank real trials to 5-25 per cell (2606.10366: 5); the residual reason is incentive (validity papers are written by simulator builders; statistics papers treat the sim as a prior) plus the tedium of recovering denominators the repos do not ship
Closest neighbors (one-sentence trick; one-line difference):
- `2610.00731` Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation (Kaedim) — Build the same robot cell twice (authored vs default recipe), run two policies on five tasks twenty times each, and score both against the same real trials with bootstrap intervals. *Difference:* Applies the per-pair resolvability check to its own five tasks as a reason to omit MMRV (2 of 5 real orderings confident); no field-wide re-scoring, no split agreement, no chance correction, no sample-size rule.
- `2606.10366` A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation — Run the same five VLAs on three simulators and the real robot under four perturbation types and score each simulator by whether it keeps the real ranking and the real order of perturbation damage. *Difference:* A consumer: 5 real rollouts per cell, rho from 0.000 to 1.000 with no real-side interval; the regime the candidate predicts to be under 40% resolvable.
- `2405.05941` SIMPLER: Evaluating Real-World Robot Manipulation Policies in Simulation — Match the simulator's controller and camera image to the real setup and show policy success rates in sim line up with the real ones across RT-1/RT-2/Octo checkpoints. *Difference:* The incumbent weighting: MMRV weights a violation by the real gap |Ri-Rj|, not by the gap's standard error; the paper names real-evaluation noise as the motivation. Pre-window.
- `2610.17521` YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation — Rebuild a scene with Gaussian splatting for a wrist-fisheye gripper, inject artifacts, and count how many of nine real policy orderings the sim reproduces. *Difference:* States its Wilson intervals 'are not confidence intervals for ranking accuracy or tests of the difference between policies'; runs Fisher tests on the 80-trial sim side only.
- `2610.14603` AnyRank: Reliable Anytime Policy Ranking via Sequential Testing — Rank many policies from hardware trials with a sequential test that spends trials on hard-to-separate pairs and uses a sim ranking only to order the hypotheses. *Difference:* Real-side incumbent for producing a resolvable ranking; grades the sim prior by Pearson r with real progress (r = 0.05), never by real-pair resolvability; proxy evaluations 'left to future work'.
**Probe as pre-registered (checked):** Re-score SIMPLER (87 pairs, done today: 52/53 resolvable vs 24/31 unresolvable, 3 ties), SimFoundry Table G.1 (n=25), PolaRiS (n=20), 2606.10366 (n=5 per cell), YUBI (n=20), R2S-Eval Table II (n=20), Kaedim per-trial (n=20), plus PhAIL and RoboArena for the sample-size half; resolvable fraction, split agreement, kappa, attenuation ceiling, trials-per-arm table. $0, 0 GPU-hours, 2 days; under one GPU-week. Dead if resolvable fraction >= 85% everywhere or unresolvable-pair agreement >= 0.9.
*Search degraded:* s2 skipped (no key); no conference-export index built; complaint stream not searched (GitHub API unreachable from this session)

## Red team

**C-W43-13** — {"date": "2026-10-20", "rounds": 2, "personas": ["systems", "theory", "professor", "checklist"], "counts": {"raised": 18, "conceded": 16, "answered": 0, "open": 2}, "objections": [{"persona": "theory", "objection": "The split's unresolvable half is uninformative about the simulator by construction: sign agreement A = P(R=S) = 1/2 + 2(q_r-1/2)(q_s-1/2) with q_r = P(real sign = true sign), q_s = P(sim sign = true sign) is symmetric; on pairs selected as unresolvable q_r is small by selection. Simulation under the record's own model: a perfect simulator (q_s=1) scored against SIMPLER's rates gets A_unres = 0.895 (the record's 0.9 kill line), and 0.69 / 0.57 on same-family cohorts at n=20 / 5 (the record's 'expected' band); on resolvable pairs a perfect sim with m=25 sim trials scores 0.79 and with n=5, m=20 scores 0.65 (winner's curse), so '<0.8 means the simulator is broken' is false.", "evidence": "argument; rt13/theory_sim_out.txt sections 1-2 (2000 cohort replicates)", "answer": "the split was meant as a reporting convention, not an estimator of q_s; round 2: a convention whose two pre-registered outcomes are both the model's own prediction has no kill result and no consequence (…

## First steps if pursued

1. Nothing on this claim unless Jacob keeps the residue: one CPU day — recompute the Newcombe resolvable fraction and the task-clustered split on SIMPLER, R2S-Eval Table II, SimFoundry G.1/G.2 and YUBI from rt13/sys_tables.py, open a PR to simpler_env/utils/metrics.py, and write the two-page note citing 2409.09491 and Snyder Table II.
2. If the real-reliability claim is captured: read RoboArena Fig. 7 (r vs episode count), AutoEval's manual-vs-automatic agreement and VLA-REPLICA's cross-rig consistency before writing its scorecard; the estimand is q_r = P(real sign = true sign) from repeats, which these three measure and no table-only re-analysis can.

## Decisions for Jacob

- Retire CL-W43-02 (the headline is refuted on three tables and its narrow true version is the field's stated assumption), or keep the one-day residue: a methods note and a ~30-line PR adding a named-test resolvable fraction and the task-clustered split to simpler_env/utils/metrics.py.
- Whether the three real-real repeatability sources the kill search missed (RoboArena Fig. 6-7 at r=0.69 for conventional real evaluation vs a 4,284-rollout oracle; AutoEval; VLA-REPLICA) are worth a /capture as an L1 claim about real-evaluation reliability — with its own scorecard, not this one's.
- Checklist rule to adopt: a red team of a zero-cost probe runs the probe's first step (it decided this verdict in an hour).

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded: no failing gate; C-W43-13 survived its kill search with a weak-survival flag; premise strengthened (n = 5 per cell in 2606.10366, n = 20 in four 2026 papers); not supported until the probe reports the split on at least four 2026 tables
- 2026-10-20 — claim refuted: red team of C-W43-13 (2026-10-20): probe killed; claim refuted as worded — the probe's zero-cost step run on three 0/1 tables gives resolvable fractions 63% (SIMPLER), 71% (R2S-Eval), 68% (SimFoundry G.1), unresolvable-pair agreement 0.92 on both 2026 tables (the pre-registered kill line), and a perfect simulator produces those thresholds under the record's own model; kappa/Pbar unidentified, att…
- 2026-10-20 — C-W43-13 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — no fetched paper grades published real-to-sim agreement against real-trial resolvability or chance; the closest, Kaedim 2610.00731 App. B, applies the check to its own five tasks to withhold MMRV, so the mechanism exists at single-study scale and the field-wide ruler with kappa, the attenuation ceiling and the sample-size table does…
- 2026-10-20 — C-W43-13 killed: red team (stage 5, automatic, three personas, 18 objections: 16 conceded, 0 answered, 2 open after two rounds): killed — the red team ran the probe's zero-cost step on three published 0/1 tables (SIMPLER reproduced: 52/53 vs 24/31; R2S-Eval Table II n=20: 64/64 vs 24/26; SimFoundry G.1 n=25: 27/27 vs 12/13): the pre-registered kill fired (unresolvable-pair agreement 0.92 >= 0.9 on both 2026 table…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-02`, version 3)
- probe `C-W43-13`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W43-kill-C-W43-13.md`
