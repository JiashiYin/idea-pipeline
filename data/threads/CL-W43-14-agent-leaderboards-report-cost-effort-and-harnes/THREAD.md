# Agent leaderboards report cost, effort and harness effects from single runs whose run-to-run spread is larger than the differences they rank.

`CL-W43-14` · lane **L1** · status **killed** · rank None · position solo · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search requested ahead of rank order on 2026-10-30; the task-sampling rival from L08 must be in the pre-registration). Grade on paper: open pending kill search; six probes, two scorecarded with $0 first steps; community-wide consumers; champion candidate. Next action: see First steps.

## The claim

- **Headline:** Agent leaderboards report cost, effort and harness effects from single runs whose run-to-run spread is larger than the differences they rank.
- **Current belief (the field's):** HAL 2510.11977 states 'we were forced to rely on single runs without statistical validation for most evaluations' and reports higher effort giving equal or lower accuracy in 21 of 36 model-agent-benchmark combinations; the released 2610.00917 cost table holds exactly one run per (model, harness, task) cell in all 6,204 cells (import S6xF1's arithmetic, 2026-10-25).
- **If true:** Leaderboards add a replicate rule and a resolvable-ratio column for cost; effort non-monotonicity is re-read as an interaction component plus run noise; harness and model cost comparisons under the resolvable ratio are withdrawn
- **If false:** Run share of cost variance under 5% and the effort x task interaction identified from single runs: single-run tables are adequate and the lane's replicate rule is a service

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper states it does not estimate within-cell repeatability (sec. 4.1) and lists 'stability across repeated runs' as limited evidence (sec. 6.1) while ranking four harnesses; Harness-Bench (2605.27922) reports 5,194 trajectories per model-harness pairing with no replicate count in its abstract; 2607.17136 shows for one agent that a single-run improvement has the wrong sign about a third of the time. Who pays: harness benchmark owners (TraceTrial-Bench, Harness-Bench) who rank harnesses; harness vendors whose product comparisons at fixed model rest on one draw; HAL and every leaderboard with a harness or scaffold column; anyone citing 'harness X beats harness Y on model M'.
- **Impact ceiling:** **floor**: A re-analysis note: the replaced-cell counts and the paired first-vs-replacement flip rate from the release, plus the binomial ceiling on the reported swings; cited by the next harness benchmark. Requires step 0 only. Judgment p 0.45.; **middle**: The first within-cell repeatability and judge-variance numbers for a harness benchmark, with the ordering-stability fraction per model and a resolvable-difference column adopted by one harness benchmark. Requires step 1. Judgment p 0.35.; **ceiling**: A reporting rule across agent leaderboards: harness, cost and effort effects are reported with a replicate-based resolvable difference, and the judge component is a standard line in any LLM-judged benchmark; with the sibling probes on cost (S6xF1) and effort (S8xF1) this is the noise-floor program's headline. Requires replication on Harness-Bench and one HAL benchmark, about 150 GPU-hours or 1,50…
- **Relevance:** HAL (Narayanan): direct, multi-run reliability and the harness column. Narasimhan (tau-family): moderate, the same run-variance question with a simulated user in place of a harness. Evaluators and harness benchmark owners: direct. Industry: direct for harness vendors comparing products at fixed model. Jacob's edge: variance components, bootstrap bands and the binomial ceiling are identities he can check; computer engineering small (serving an open model, running the gateway); theoretical physics zero.
- **Kill probe:** Step 0 (zero dollars, 2 days) then 4 harnesses x 2 models x 30 tasks x 5 runs plus three re-judges per trace (about 60 GPU-hours for the open-weight arm, about 850 dollars in API and judge dollars, 7 days); dead if the within-cell flip rate is under 10%, every model's harness ordering is stable in at least 95% of run-bootstrap resamples and the judge component is under a tenth of the run component.
- **Density and ownership:** From the card's fetched neighbours and this run's API fetches: Harness-Bench 2605.27922 (per model-harness pairing, no replicate statement), Auditing Agent Harness Safety 2605.14271 (210 tasks x 10 harness configurations, stability named as an axis but no within-cell number in the abstract), 2607.17136 (variance components for one 35B computer-use agent across data draw, seed and run; the closest prior, not a harness instance). Under this claim already: import S6xF1 (cost variance components on the 2610.00917 table) and S8xF1 (effort x task interaction on HAL); the CL-W43-14 thread lists 2610.00651 and 2608.11323 as generalizability theory for scores, to be checked for a harness facet. Occupied by the card: the single-run grid, its two rankings and the 31.1% figure. The kill search must use the neighbours' words (repeatability, reproducibility, pass^k, run-to-run, replicate, seeds, nond…
- **Why now:** Card paper 2026-10-23 (released grid, traces, verdicts, gateway); 2607.17136 2026-07-19 (the prior and the k-seed library); Harness-Bench 2026-05-27 (a second single-draw harness leaderboard). The estimator is old; the flag is recorded.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass as of 2026-11-02: import S7xF3 is scorecarded with a $0 step 0 (the single-run band on Trial by Trace's 27 adjacent harness gaps) and C-W44-03's step 0 is $0 on the released replaced-cell archive; the two W43 imports still lack scorecards |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B with a stated strain: the ruler is the run-within-cell variance component for cost and for the effort effect; the field itself states the single-run limitation; 2026-11-02, pressure #3 and #7: B09 52.0 vs B12 58.08 vs official 57.88 for one model; B01 Terminal-Bench 4.0 stores pass_at_5 and shows pass@1, under which 'Row 1 Opus 5.5 [...] pass_at_5 0.7879' ties 'Row 5 Fable 5.1 [...] pass_at_5 0.7879'; L08 'two-thirds of the tasks are solved either >=80% or <=20% of the time by a given model, so most of the uncertainty comes from tasks rather than run-to-run variance' — the task-… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every leaderboard with a cost or effort column; harness papers; cost-per-success reporting |
| G4 | mechanism and consequence | pass: mechanism — heavy-tailed per-run cost (log-cost SD 1.4-1.6) and binomial single-run success make one-replicate cells noisy; with T tasks, m trials and per-task success p_t, $\mathrm{Var}(\bar p) = \frac{1}{T}\big(\mathrm{Var}_t(p_t) + \mathbb{E}_t[p_t(1-p_t)]/m\big)$, so sharpened models push the within-task term to zero and only T shrinks the bar (pressure #7); consequence — a replicate rule and a resolvable-ratio column where the within-task term dominates, a task-count rule where the between-task term does |
| G5 | durability; lab-adjacent | pass as a ruler; G-theory for scores is already imported (2610.00651, 2608.11323) so the new ground is cost and effort as measurands |
| G6 | ownership, density, race window; position clause | open: imports found no fetched source decomposing cost or the effort x task interaction; kill search owed; Gate 1 blocked on paperwork — neither probe carries a scorecard (checklist 2026-10-20: write it at import time or in the first /mutate); 2026-11-02: BB-EDGE 2609.32248 owns the anytime-valid leaderboard over complete-panel replicates and leaves 'item-level anytime-valid inference [...] for future work' (import S7xF3's nearest); 2602.11619 found single runs misrank 29.3% of the time on 50 tasks; HAL's reliability tracker is paused; Terminal-Bench 4.0's per-trial payload (11,550 trials) is… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-03 | Second draw for the harness grid: within-cell run and judge spread against the harness rankings TraceTrial-Bench reports | Step 0 (zero dollars, 2 days) then 4 harnesses x 2 models x 30 tasks x 5 runs plus three re-judges per trace (about 60 GPU-hours for the open-weight arm, about 850 dollars in API and judge dollars, 7 days); dead if the within-cell flip rat… | killed | — |
| C-W44-06 | Paired on nothing: instance share versus rollout share in EnvOS's generated-instance cells | Step 1: 160 rollouts of Gemini 3.1 Pro Preview and Claude Sonnet 5 on the released claims block, about $500, 0 GPU-hours, 7 days including the rebuild; dead if the ON-A cells are instance-deterministic (8 of 10 instances at 0 or 1, $\rho_I… | proposed | — |
| C-W44-OWN-1 | Who moved in tau-bench 2.0: the user-simulator share of pass@1 variance at the leaderboard's one-trial protocol | The 1,800-call three-arm run: $750, two days, zero GPU-hours; dead if $S_U < 0.1$ everywhere and agent-first divergence is at least 80%. | parked | — |

Also under this claim (no scorecard yet): import:2026-W43-S8xF1 (step 0: $0 re-analysis of HAL per-task logs for the 36 cells; step 1: 4 effort x 60 tasks x 5 runs crossed G-study, 60-100 GPU-h or $2-4…; import:2026-W43-S6xF1 (step 1: $0 variance decomposition of the released 2610.00917 cost table; step 2: 3 harnesses x 63 Terminal-Bench 4 tasks x 5 runs, $400-…; import:2026-W44-S7xF3 (confidence-sequence stopping rule on the pass^k difference with replicates raced to the disagreeing cells; step 0 $0, 3 d on Trial by Tr…

## Kill search

### Concept level (CL-W43-14) — killed (2026-11-02)
Gate 2B: the surprise ('run-to-run spread larger than the differences ranked') is the field's stated knowledge with measurements attached (2609.33812 run SD 0.0107 > pairing spread 0.0095 and 2.2-fold median cost swing; 2610.01618 54% run-to-run; 2602.07150 2.2–6.0 pt; 2602.11619 29.3% misrank), and the cost and effort clauses are contradicted at leaderboard scale by fetched numbers (effort moves cost x4.8 vs x1.34 run spread, 2608.25399; harness moves cost up to 5x with task-bootstrap CIs, HarnessTax; frontier effort-on-accuracy already read as flat, R03/L04); the unmeasured residual (cost run share on a public grid) computes at $0 to 4–9%, at or under the claim's own if_false line of 5%, siding with the task-sampling rival (L08).
Full record: [`data/reports/2026-W44-kill-CL-W43-14.md`](../../../data/reports/2026-W44-kill-CL-W43-14.md).
**Occupied by:** 2609.33812 (mechanism, harness + cost clauses, one task) with 2610.01618 (multi-task grid, 54% run-to-run) and 2602.07150 (SWE-bench, scaffold axis); effort-on-cost clause a published negative in 2608.25399
**Why not done before:** Not applicable: done in pieces that cover the headline (2609.33812, 2610.01618, 2602.07150, 2608.25399, HarnessTax, 2604.22750, 2512.06710). The leaderboard-scale cost/effort G-study is an appendix to released payloads (Terminal-Bench 4.0 per-trial payload 2026-10-23; 2610.01618's 18,000 trajectories; HarnessTax's promised traces; 2608.25399's 2,700 runs) whose owners are its natural authors; 'they have the stack' is a guess and the re-open test is asking them. 'It is a service' is the reason, not 'no reason found'.
Closest neighbors (one-sentence trick; one-line difference):
- `2609.33812` Identical Runs, Different Results: Benchmarking AI Coding Agents on Open-Weight Models (2… — Run six coding agents on six open-weight endpoints 52 times each on one ML-engineering task, score a hidden holdout, and compare the run-to-run SD with the spread between pairing means, pricing every run including the prompt cache. *Difference:* none — occupied for the harness and cost clauses at the mechanism level: run SD 0.0107 > between-pairing spread 0.0095; within-cell cost swing 2.2-fold median vs 1.2–2.1x between agents; tens to a hundred runs per arm to resolve. Own scope: one task.
- `2610.01618` Agents Are Systems, Not Models: Rethinking Agentic Evaluation (2026-10-01) — Cross five configuration axes (information, reasoning, verification, time budget, model) on four scientific tasks with five runs per cell and split score variance into between-cell and run-to-run parts by ANOVA/ICC, with cost beside the score. *Difference:* none — occupied for 'configuration effects from single runs sit inside run noise' on a multi-task grid with a budget axis: 54% of score variance is run-to-run; cost per cell reported as means only, run component of cost not decomposed.
- `2602.07150` On Randomness in Agentic Evals (2026-02-06) — 60,000 SWE-bench Verified trajectories over three models and two scaffolds: single-run pass@1 moves 2.2–6.0 points with the run chosen, SD > 1.5 points at temperature 0; recommends replicates, power analysis, pass@k/pass^k. *Difference:* The accuracy clause on a real agent benchmark with a scaffold axis; no cost, no effort axis, no task-vs-run split.
- `2608.25399` Can your AI agent be cheaper? Task specifications and token spend (2026-08-26) — Five SWE-bench Verified tasks x twelve specifications x three thinking efforts x fifteen repeats (2,700 runs, Kimi K3, mini-swe-agent): token spend, its run-to-run geometric SD (x1.34), and a one-probe predictor. *Difference:* Effort x run x task for cost exists: effort moves mean spend x4.8 against a x1.34 run spread; spread scales with mean cost (slope 1.08); no credible effort effect on solve rate at ceiling. The claim's effort-on-cost clause is a published negative here. Own li…
- `HarnessTax (harnesstax.github.io)` HarnessTax: How Much Does the Harness Matter for Coding Agents? (Pan, Yang, Arabzadeh, Ch… — Seven models x three harnesses (Claude Code, Codex CLI, Pi) on 30-task samples of SWE-bench Lite and Terminal-Bench 2.0, three attempts per task, cost vs success with 10,000-resample task bootstraps. *Difference:* The replicated harness x model x task grid with cost exists: 'Harness choice has little effect on task success rate, but can significantly affect the cost [...] up to 5x'. Attempts are averaged, so the within-cell term is in their data, not their text; traces…
**Narrowest surviving headline:** Not a measurement claim under CL-W43-14. Method fragment for a new claim: 'A per-cell confidence sequence on the pass^k difference, with replicates raced to the disagreeing cells, certifies a harness ordering with fewer runs than BB-EDGE's complete-panel rounds' (BB-EDGE's stated future work; weak — head-to-head with its authors, Gate 5; 2607.17409's 'uniform sometimes beats adaptive' is the pre-registered risk).
*Search degraded:* ['s2 (Semantic Scholar skipped, no key)', 'Q5 effort vocabulary returned 6 — query defect noted; the effort x run study surfaced via cost words', 'HarnessTax is a web post (no arXiv id); per-attempt data not yet released']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Promote? Princeton-local consumer (HAL); $0 first step; part of the proposed L1 'noise floor' program.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written top-down by the closing-W43 claims run; the two cost/effort imports attached as probes; scorecards owed before it is kill-applicable
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 7 (unchanged)
- 2026-10-30 — claim open: nominated as a core-ML champion candidate (Jacob asked for a champion outside L5); kill search requested ahead of rank order; see PROGRAM-L1-evaluation-floors.md
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-14.md): killed — Gate 2B: the surprise ('run-to-run spread larger than the differences ranked') is the field's stated knowledge with measurements attached (2609.33812 run SD 0.0107 > pairing spread 0.0095 and 2.2-fold median cost swing; 2610.01618 54% run-to-run; 2602.07150 2.2–6.0 pt; 2602.11619 29.3% misrank), and the cost and effort…
- 2026-11-01 — C-W44-03 killed: killed with claim CL-W43-14 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-14.md): Step 0 (replaced-cell count on Trial by Trace) is a footnote; step 1 (4 harnesses x 2 models x 30 tasks x 5 runs) is HarnessTax / 2609.11987 / 2609.33812 territory; the judge-component clause is 2609.33044's.
- 2026-11-01 — C-W44-OWN-1 parked: stage 8 owned-artifact prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-OWN-1 parked: claim CL-W43-14 concept-level kill search (killed): probe effect 'unchanged' — Lab-parked; its 'one-trial protocol' premise is stated knowledge; its measurand (user-simulator party) belongs to CL-W43-J01 / pressure #8.
- 2026-11-02 — claim open: pressure #3 and #7 (2026-11-02): B01 Terminal-Bench 4.0 computes pass_at_5 and shows pass@1 (rank 1 and rank 5 tie at 0.7879); L08 'most of the uncertainty comes from tasks rather than run-to-run variance' (the rival term); B09/B12 three numbers for one model; banter seed 2607.17136 'eval variance ~0, seed <=10%, data draw 48% on the hardest cell, bimodal runs'; records R01, R03, L08, L16, R09, R…
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): headline widened to 'cost, effort and harness effects' (C-W44-03's attachment; previous headline kept in previous_headline); import S7xF3 (scorecarded), C-W44-03, C-W44-06 and C-W44-OWN-1 (lab) attached; cheapest probe -> import S7xF3 ($0 step 0); Gate 1 unblocked; rank 7 -> 2 — every leaderboard with a cost, effort or harness column is a consumer, the ruler i…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-14`, version 5)
- probe `C-W44-03`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-06`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-OWN-1`: `data/candidates/2026-W44.jsonl`
