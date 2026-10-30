# Published step-credit critics for long-horizon agents do not beat their own shuffled control in the first two thirds of a trajectory.

`CL-W43-06` · lane **L2** · status **parked** · rank 4 · position both · refreshed 2026-10-30

## Status

Parked — re-open trigger: the forward (prefix-only) frontier re-grade on 2610.17633's K=32 L0+L1 curves (~$300-900, 0 GPU-h, 2 d; vs linear decay and the owners' restart gain; equivalence bound; task-cluster bootstrap) reverses 2610.21088's early-chance null — or a named consumer (a distillation or restart-controller paper) states in print that it needs the hindsight-vs-forward separation Failing gate: G2B, G4 (degenerate null); G1 as written. Grade on paper: parked; re-open on the forward re-grade reversing a published null. Next action: see First steps.

## The claim

- **Headline:** Published step-credit critics for long-horizon agents do not beat their own shuffled control in the first two thirds of a trajectory.
- **Current belief (the field's):** LVRL 2610.15840 reports its step credit is unreliable early (44% vs 88%) and leaves the separation to future work; critics are evaluated against end-task success, not against executed replay; LVRL 4.5: 'separating the effect of the endpoint anchors from that of the context rollouts, and varying the number of context rollouts, is left to future work'; 2610.17633 discussion: 'the curve is the reference against which localizers and the value estimators controllers need can be built and ranked'
- **If true:** Critic papers must report the shuffled-control and placebo arms against executed ground truth; dollar-matched Monte Carlo becomes the baseline
- **If false:** The critic beats its shuffle from the start — then the audit is a confirmation the critic's authors cite

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: LVRL (2610.15840) states its step credit is unreliable early (44% vs 88%), leaves separating anchors from in-context siblings to future work, and calls the frontier bill prohibitive under budget limits (card complaints 2 and 3); 2610.17633 sec. 7 says value estimators controllers need 'can be built and ranked' against its curves; CWGT's abstract: existing evaluations grade step correctness, it audits contribution, and they come apart. Who pays: training teams spending order $10k per AppWorld run on a frontier critic plus summarizer; restart or controller builders (2608.03222, 2609.38147) who need a forward prefix value.
- **Impact ceiling:** **floor**: A footnote: the anchored frontier critic's localization on SWE failures sits inside its own shuffle in all thirds, or beats it only late, with a measured ranking of three estimators against a noise ceiling; requires the release to contain trajectory text and per-continuation outcomes; p = 0.5 (judgment).; **middle**: A measurement paper: value-captured share and Spearman by trajectory third for the critic, k = 0, placebo, shuffle, MC and log-ratio arms, with the mechanism (outcome-reading vs step-reading) separated and the recipe consequence that anchors plus uniform split equal the critic for the first two thirds at $0; requires step 0 to show resolution and the 60 second-agent curves to replicate; p = 0.35…; **ceiling**: The critic survives placebo, beats shuffle early and matches MC: first replay-graded evidence that frontier models carry forward value on long-horizon agent runs, which makes a distilled local critic a sound target and changes what restart controllers use; or the reverse, 'Spearman with executable V' becomes the reported validation for step-credit claims adopted by one training group; requires cu…
- **Relevance:** Narasimhan route (Odysseus, EasyPPO) and any RL group: a ground-truth grade of the lane's most expensive credit signal, usable as a baseline table; the uniform/shuffle/placebo/MC arms become required controls. Industry: anyone paying frontier API for critics. Jacob's edge: the instrument's statistics (binomial noise at 331 continuations, bootstrap over curves, placebo design, attenuation by noisy ground truth) is a physics-trained fit; computer engineering: zero (no systems component); L5: zero.
- **Kill probe:** Step 0: oracle-vs-random VC_2 gap on the released curves, $0, 1 day, dead if intervals overlap. Step 1: critic plus controls and the dollar-matched MC arm, about $550 API and 10 GPU-hours, 5 days; claim dead if the critic beats its shuffle in the first third, holds under placebo and matches MC within 0.05 Spearman.
- **Density and ownership:** Occupied: CWGT 2608.19760 (ALFWorld audit of judge scores, log-ratios and confidence against executed replay with marginal-matched shuffle); 2610.17633 (SWE V-curves, judge-label grading, value-based restart); LVRL's own AppWorld sign-agreement probe (114 hand-thresholded events, no placebo, no shuffle, no correlation); CAR 2606.08275 (intervention-based attribution tooling); RTMC 2604.11037 (rollout-tree MC credit on SWE-bench Verified); VinePPO 2410.01679 and GiGPO 2505.10978 as pre-window precedents. arXiv API 12-month counts run 2026-10-19: 'credit assignment' AND 'Monte Carlo' AND critic/value/PRM AND agent = 7; placebo/shuffled AND critic/PRM/judge AND LLM AND step/trajectory = 5 (CWGT the only audit); ground truth AND step-level AND value/credit AND rollout/replay AND agent = 5; in-context/frozen LLM value or critic AND credit AND agent = 26 recipes, none graded against replay ex…
- **Why now:** 2610.17633's released V-curves (2026-10-13) make the ground truth free; LVRL's prompt (2026-10-11) is the first published anchored in-context critic with its own early/late number; CWGT (Aug 2026) supplies the pre-registered audit template; Fail-Fast 2608.03222 (Aug 2026) trained a forward monitor on the same Qwen3.6-27B policy, a further estimator to grade.
- **Register, and what it is not:** measurement / ruler with a dollar-matched comparison. It is not a new critic, not a training run, and not a reproduction of LVRL's AppWorld or BabyAI numbers.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | fails as written: the kill is a one-sided conjunction whose placebo clause cannot fire; the equivalence-bound forward re-grade is the live probe if re-opened |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | fails route B: the expected result (critics at chance early against executed value) is published for forward critics (2610.21088, 2026-10-15) and the hindsight class has no consequence; route A's quotes describe the critic's own appendix, not a strain |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community; the 'validation column' exists in LVRL App. F and 2610.21088 Table 8 |
| G4 | mechanism and consequence | fails: the headline's null (shuffle) is the random-step row; the mechanism sentence (outcome-reading vs step-reading) needs the linear-decay / outcome-blind null, which the headline does not name |
| G5 | durability; lab-adjacent | unchanged |
| G6 | ownership, density, race window; position clause | kill-search miss: 2610.21088 (five days before the search) inside the audit register; ownership adds the Probe-and-Resume group (Columbia; forkable terminal environments); lane vocabulary must add test-time search, MCTS, critic access, intermediate states, continuation pass rate |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-01 | Placebo and dollar-matched audit of LVRL's anchored frontier critic on released V-curves | Step 0: oracle-vs-random VC_2 gap on the released curves, $0, 1 day, dead if intervals overlap. Step 1: critic plus controls and the dollar-matched MC arm, about $550 API and 10 GPU-hours, 5 days; claim dead if the critic beats its shuffle… | killed | survived-kill ([record](../../../data/reports/2026-W43-kill-C-W43-01.md)) |
| C-W43-03 | Dollar-matched cold-start BabyAI: LVRL's critic bill as GRPO rollouts | GRPO G = 8 floor reproduction plus GRPO G = 32 on LVRL's BabyAI config, about 400 GPU-hours (about $1k cloud), 7 days; void if the floor is not reproduced; claim dead if G = 32 stays at or below 20% ID at 150 updates. | parked | — |

## Kill search

### C-W43-01 — survived-kill (2026-10-20)
No fetched paper grades an anchored sibling-conditioned frontier value critic against executed prefix values with a wrong-outcome placebo and a dollar-matched MC arm; CWGT audits a different signal class on ALFWorld and the curve owners grade no estimator; occupied_by none; probe stays under one GPU-week after adding ~25 GPU-h of sibling regeneration.
Full record: [`data/reports/2026-W43-kill-C-W43-01.md`](../../../data/reports/2026-W43-kill-C-W43-01.md).
Per position — **solo**: survived-kill: all arms but k = 3 run from public data; ~$550 and ~35 GPU-h; weak points: the curve owners name this measurement as the next use of their data (re-open test: ask them), and the self-estimate arm is a rep…; **lab**: survived-kill: adds the AppWorld replication (LVRL's 114 MC events unreleased) and a second critic vendor; races LVRL's authors on their own data
**Why not done before:** an enabling piece landed: 2610.17633's V-curve release (2026-10-13; transcripts of the 107 selected runs, every continuation's outcome, 8 base-run outcomes per task), after LVRL's prompt (2026-10-11) and CWGT's audit template (2026-08-20); hard parts: sibling transcripts are not released (k = 3 arm needs ~700 regenerated base runs) and the ground truth's own resolution (SE ~0.08 per point at K = 32) caps attainable Spearman
Closest neighbors (one-sentence trick; one-line difference):
- `2608.19760` Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against… — Re-execute the policy's own alternative action at each step and roll forward; the outcome shift is the step's contribution, and every credit signal is graded against it beside its own shuffled copy. *Difference:* Audits an outcome-aware per-step correctness judge, a hindsight log-ratio and policy confidence on ALFWorld (Qwen2.5-7B); no anchored sibling-conditioned frontier value critic, no wrong-outcome placebo, no dollar-matched MC arm, no SWE.
- `2610.17633` Executable Prefix Values for Locating Agent Failures — Restart the agent from reconstructed states of its own failed run and count how often it still succeeds; where that number falls is where the run was lost. *Difference:* Supplies the ground truth; grades judges, a human and fixed rules by value captured (Table 32 already holds the random-step, step-1, first-edit rows: cite, do not re-run); grades no value estimator.
- `2610.15840` LLM Value Functions for Credit Assignment in Agentic RL (LVRL) — Ask a frozen frontier model for the value of every step, pin the first to the group pass rate and the last to the observed outcome, and train on the differences. *Difference:* The critic under audit; its own MC check is 114 hand-thresholded AppWorld events with sign agreement, no shuffle, no placebo, no correlation; anchors and siblings ablated jointly; no code or labels released.
- `2608.29685` Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents — Score verbal confidence and perplexity at each stage of a run against the final outcome; they separate failures at the end (AUROC 0.85) and not at mid-run (under 0.60 at 50% progress). *Difference:* Forward uncertainty on deep-research tasks, no executed value and no critic; makes the candidate's self-estimate arm a replication row.
- `2610.18614` Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in… — Train per-step verbalized confidence against the episode's realized outcome using the GRPO group as labels; AUROC rises from chance to 0.68-0.85. *Difference:* Trained self-estimate graded on group outcomes (ALFWorld/TextWorld/WebShop), not on executed V-curves; its depth/difficulty/foresight protocol is the one to copy.
**Probe as pre-registered (checked):** Step 0 ($0, 1 day): oracle-vs-random VC_2 bootstrap on the released curves (Table 32 already shows random step VC1 0.04 / VC3 0.10 vs judges 0.16 / 0.26, so resolution is near-certain). Step 1: k = 0 critic, wrong-outcome placebo, marginal-matched shuffle, linear decay, K = 4 MC subsampled from released continuation outcomes, self-estimate and Qwen log-ratio from the release (~10 GPU-h); k = 3 sibling arm needs ~700 base runs (~25 GPU-h); ~$550 API, ~35 GPU-h, 8 days. Under one GPU-week. Kill result unchanged.
*Search degraded:* s2 skipped (no key); no conference-export index built; complaint stream not searched (GitHub API unreachable from this session)

## Red team

**C-W43-01** — {"date": "2026-10-20", "rounds": 2, "personas": ["systems", "theory", "professor", "checklist"], "counts": {"raised": 20, "conceded": 18, "answered": 0, "open": 2}, "objections": [{"persona": "professor", "objection": "The forward critic-vs-executed-continuations audit by trajectory depth is in print: Probe-and-Resume 2610.21088 (2026-10-15) grades a frontier critic at 25/50/75% depth against executed continuations on 1,111 intermediate states of 89 Terminal-Bench 2.1 tasks \u2014 pairwise accuracy 49-56% at 25% depth (chance 50%), 56-62% at 50%, 64-69% at 75%, no significant selection gain over random at 25%, decided-pairs split, best-constant row, bootstrap intervals over tasks; the record's pre-registered 'expected' result is a published finding (Gate 2B service); the kill search's 11 queries missed a 5-day-old paper because its vocabulary ('credit assignment', 'process reward', 'placebo', 'Monte Carlo') does not contain 'test-time search', 'critic', 'intermediate states', 'continuation pass rate'.", "evidence": "2610.21088 S3.2, S4, S5, App. F, Table 8 [full]: 'At intermediate states, the critics rank states better than chance late in the trajectory (64%-69% at 75% depth), but…

## First steps if pursued

1. If re-opened: day 1 ($0) — from the release's derived.json and continuation outcomes, list the L0+L1 curves of both policies (~46), their probed anchors and achieved K; drop doomed curves (V-hat(h_0) <= 1/8); compute the split-half ceiling on increments and the random-row and linear-decay baselines on the probed grid; pre-register the equivalence bound (delta = 0.05 on VC_2 and on increment correlation) and the task-cluster bootstrap.
2. Day 2 (~$300-900): run the prefix-only frontier critic at every probed anchor (no outcome, no anchors, LVRL's 4,000-character truncation), three repeats with prefix caching; score increments, VC_2 and the restart gain; report decided pairs; write the note against 2610.21088 App. F and Table 8.
3. Before any write-up: fetch 2610.21088's limitations section verbatim and email the three owning groups.

## Decisions for Jacob

- Fund the forward re-grade (~$300-900 API, 0 GPU-h, 2 days: prefix-only frontier critic on the K=32 uncapped curves vs linear decay and restart gain) as a replication note that is news only if it reverses 2610.21088's early-chance null — or leave CL-W43-06 parked.
- Add test-time-search / critic-access vocabulary ("test-time search", MCTS, critic, "intermediate states", "continuation pass rate", fork, branch) to the L2 queries in config/sources.yaml so the lane's density and kill searches can see the audit register.
- Whether to email the three owning groups (2610.17633's authors, LVRL's authors, the Probe-and-Resume group) before any write-up; 'they have the stack' is a guess and the re-open test is asking them.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-19 — C-W43-03 parked: mutate (stage 3) from card 2610.15840: parked at filing, Access to an 8-GPU node for one week (lab position), or a BabyAI configuration that reproduces LVRL's floor in under 168 GPU-hours total; cost on re-open: ~400 GPU-hours, 7 days.
- 2026-10-20 — claim open: headline rewritten (the 10-19 sentence said early in training; every fetched number is early in the trajectory); C-W43-01 survived its kill search with a revised cost (~35 GPU-h for sibling regeneration) and narrowed arms; C-W43-02 detached (orphan); C-W43-03 attached as the lab-position dose probe
- 2026-10-20 — claim parked: red team of C-W43-01 (2026-10-20): probe killed as designed (degenerate shuffle null; unfirable placebo; mis-costed MC arm; hindsight critic without forward consequence; budget confound; one-sided underpowered kill) and the claim's substance found in print five days before the kill search (Probe-and-Resume 2610.21088: forward frontier critic at chance at 25% depth against executed continuations);…
- 2026-10-20 — C-W43-01 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — No fetched paper grades an anchored sibling-conditioned frontier value critic against executed prefix values with a wrong-outcome placebo and a dollar-matched MC arm; CWGT audits a different signal class on ALFWorld and the curve owners grade no estimator; occupied_by none; probe stays under one GPU-week after adding ~25 GPU-h of sib…
- 2026-10-20 — C-W43-01 killed: red team (stage 5, automatic, three personas, 20 objections: 18 conceded, 0 answered, 2 open after two rounds): killed as designed — the claim's shuffle null is degenerate (for a localizer the marginal-matched shuffle of an anchored curve has the random-step row's expected VC_k; any monotone curve beats it on rank correlation), the placebo clause cannot fire on an all-failed set, the dollar-match…
- 2026-10-20 — C-W43-03 parked: claims (stage 11): attached to CL-W43-06 — secondary probe, lab position only (parked solo): tests the dollar-matched consequence (what the critic buys is rollout budget)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-06`, version 3)
- probe `C-W43-01`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W43-kill-C-W43-01.md`
- probe `C-W43-03`: `data/candidates/2026-W43.jsonl`
