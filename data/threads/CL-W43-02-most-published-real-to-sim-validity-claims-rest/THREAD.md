# Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.

`CL-W43-02` · lane **L1** · status **open** · rank 2 · position solo · refreshed 2026-10-19

## Status

Open claim. Probe C-W43-13 survived the kill search; red team owed before anything is called proper. Failing gate: none on paper; survival is by scope and statistic, not by the observation (which Kaedim and SIMPLER state); red team owed. Grade on paper: proper-shaped (small community) pending probe result and red team. Next action: see First steps.

## The claim

- **Headline:** Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve.
- **Current belief (the field's):** Real-to-sim papers report rank agreement as point estimates over a handful of pairs (YUBI 2610.17521: 9 pairs, no interval; PhAIL 2605.29710 on cohort sizes); YUBI IV: its Wilson intervals 'are not confidence intervals for ranking accuracy or tests of the difference between policies'; 2606.10366 4.1: '5 real-world rollouts for each policy, task, and perturbation dimension'; Kaedim 2610.00731 App. B: 'We do not report MMRV on this basis'
- **If true:** Real-to-sim validation papers report resolvable fraction and chance-corrected agreement; benchmark owners publish the sample-size table
- **If false:** Rank agreement is robust even on unresolvable pairs — then the field's practice is fine and the note says so

## Scorecard (from the cheapest probe's record)

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
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-13 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: resolvable fraction, split sign agreement, chance-corrected kappa and the attenuation ceiling are identifiable from published tables; pre-registered surprise — expected near-perfect agreement on resolvable pairs and near-chance on unresolvable (SIMPLER 52/53 vs 24/31), field assumes pooled r and MMRV grade the simulator, the ruler dies if >= 85% of pairs are resolvable everywhere; route A also present (PhAIL N <= 25 without intervals; YUBI and Kaedim statements) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass: real-to-sim validity authors (report split agreement and kappa), benchmark owners (trials-per-arm table, resolution column), real-side statistics tools (AnyRank, SureSim: grade the sim prior); community-wide inside robot-learning evaluation (every real-to-sim validity paper), a small community |
| G4 | mechanism and consequence | pass: mechanism — binomial noise at 5-25 real trials leaves most pairs' real ordering unknowable, so pooled agreement averages a coin flip into a near-perfect number; consequence — report the split and size real trials by the gap to resolve |
| G5 | durability; lab-adjacent | pass: a ruler on any simulator and policy generation; lab-adjacent |
| G6 | ownership, density, race window; position clause | pass with a weak-survival flag after the kill search of C-W43-13 (8 queries, 13 neighbors, 5 precedents, 8 quotes): no paper grades published agreement by resolvability or chance; Kaedim App. B applies the check at single-study scale to withhold MMRV; SIMPLER III-B weights violations by the real gap, not its standard error (the incumbent weighting); why now = 2026 same-family cohorts at n = 5-25; 2-day probe against about one real-to-sim paper a fortnight |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-13 | Resolvable pairs: the noise ceiling on real-to-sim rank agreement | Re-analyse 5-7 published real-vs-sim tables (binomial resolvability, agreement split, kappa, attenuation ceiling) and build the sample-size table; 0 GPU-hours, $0, 2 days; dead if resolvable fraction >= 85% everywhere or unresolvable-pair… | survived-kill | survived-kill ([record](../../../data/reports/2026-W43-kill-C-W43-13.md)) |

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

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Red team **C-W43-13** (`/redteam C-W43-13`): three personas with fetched evidence; it survives only with no unanswered objection.
2. If it survives: run the probe exactly as pre-registered — Re-score SIMPLER (87 pairs, done today: 52/53 resolvable vs 24/31 unresolvable, 3 ties), SimFoundry Table G.1 (n=25), PolaRiS (n=20), 2606.10366 (n=5 per cell), YUBI (n=20), R2S-Eval Table II (n=20), Kaedim per-trial (n=20), plus PhAIL and RoboArena for the sample-size half; resolvable fraction, split agreement, kappa, attenuation ceiling, trials-per-arm table. $0, 0 GPU-hours, 2 days; under one GPU-week. Dead if resolvable fraction >= 85% everywhere or unresolvable-pair agreement >= 0.9.
3. Write the result into the probe's record and this Log; the claim's status moves only on evidence.
4. Then `/report C-W43-13` (eight sections, three decisions), and the next probe under this claim by cost.

## Decisions for Jacob

- Spend a session on the red team of C-W43-13 now, or wait for the next automatic run? (write `promote` or leave it)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:



## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded: no failing gate; C-W43-13 survived its kill search with a weak-survival flag; premise strengthened (n = 5 per cell in 2606.10366, n = 20 in four 2026 papers); not supported until the probe reports the split on at least four 2026 tables
- 2026-10-20 — C-W43-13 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — no fetched paper grades published real-to-sim agreement against real-trial resolvability or chance; the closest, Kaedim 2610.00731 App. B, applies the check to its own five tasks to withhold MMRV, so the mechanism exists at single-study scale and the field-wide ruler with kappa, the attenuation ceiling and the sample-size table does…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-02`, version 2)
- probe `C-W43-13`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W43-kill-C-W43-13.md`
