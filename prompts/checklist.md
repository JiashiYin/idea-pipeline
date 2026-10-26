# Red-team checklist

Mined from the fork-placement project (Sept 20 – Oct 1, 2026). Every item is an objection unless the
candidate record already answers it. Add items with a date when a report confuses Jacob or a reviewer
raises something not here. Never remove items; mark them `retired` with a reason.

## Estimator and bias
- [ ] Is the gradient (or the estimator) unbiased for the stated objective? Under which exact conditions
      (frozen policy during rollout, unclipped update, which weighting of continuations)?
- [ ] Does any privileged information (answer, reference, outcome, hint) enter a loss, a weight, or a
      sampler that trains the plain policy? If it enters the sampler, is the trained view the plain one?
- [ ] If a signal decides where samples are taken, does it depend only on the state (not on the sampled
      action)? Otherwise the expected update is biased.
- [ ] Positivity / measurability: can the quantity be estimated where the method uses it? Where the policy
      has no alternatives, the method is blind; is that fraction reported?
- [ ] 2026-10-08 — Zero mean *given what, exactly?* For every baseline or control-variate claim, write the
      conditioning set and check it against what the sampler actually conditions on. If the prompt
      identifies the task and the environment is deterministic, nothing is random after the action:
      E[f(s,a,o) | s,a] = f. "Averaging over tasks that look alike" is the critic's blur, not the sampling
      distribution. (Luck control variate for SWE, retracted 2026-10-08 after an outside review.)

## Comparisons
- [ ] Compute-matched: same rollout tokens, same wall-clock on the same engine, update pass included?
- [ ] Dose-matched: same effective sample size (examples retained, optimizer steps)? A credit rule that
      drops examples changes the dose; is the comparison measuring dose or credit?
- [ ] Is the production default (flat GRPO, group of 8) and the strongest cheap incumbent (large flat
      groups; free branching from group overlap) in the table?
- [ ] Shuffled control for any targeting or placement claim: same number of interventions at random
      positions, and a marginal-matched shuffle of the signal.
- [ ] Placebo for any hindsight or privileged signal: the same wrapper with the wrong task's information.
- [ ] Is the regime stated (model size, horizon, pass-rate band) and are results reported by band?
- [ ] 2026-10-19 — A proxy's agreement with a noisy criterion (sim-vs-real rank agreement, judge-vs-human labels, simulated
      user vs real user) is bounded by the criterion's own test-retest reliability. Split pairs by whether the criterion's trials
      could resolve them, report agreement on resolvable pairs, and chance-correct; a pooled k-of-M hides a broken proxy behind
      near-ties (YUBI 8/9 over nine pairs with one near-tied cell deciding; SIMPLER's table: 52/53 resolvable vs 24/34 not).

## Positioning
- [ ] Placement rule stated? (Several published fork methods leave it unstated.)
- [ ] Systems contribution separated from the algorithmic claim? Is the "free" part free on the deployed
      engine (e.g., vLLM bypasses the prefix cache for `prompt_logprobs`)?
- [ ] Neighbors from conference exports (abstracts-only posters) checked, not only arXiv?
- [ ] 2026-10-09 — A "nobody has done X" sentence must cite the two closest papers' own limitation sections
      saying so; the absence of a search hit is not evidence. (W41 shortlist: three such sentences, each
      contradicted by a paper cited in the same section or by a public dataset six months old.)
- [ ] 2026-10-09 — Density queries must include failure-mode and operations words, not only the problem's
      vocabulary: retry / timeout / rate limit, luck / paired / seed, idempotent / transactional / undo,
      "in the wild" / session logs. (W41 counts were low by 33–50% without them.)
- [ ] 2026-10-08 — Kill-search window covers at least the last 12 months, and queries use mechanism words
      (snapshot, fork, branch, sibling, prefix, replay, checkpoint), not only the candidate's own vocabulary.
      Miss that prompted this: Branching Policy Optimization (2607.14171, July 2026) occupied the fork lead
      and was not found in September's weekly-window searches.
- [ ] "Why now": name the enabling piece and when it landed. "No reason" is a flag.
- [ ] Is the entropy-only version of the idea in the ablation? Many ideas collapse to it.
- [ ] Does the idea survive if placement turns out second-order to the advantage form?
- [ ] One-sentence trick for the candidate itself, presentable in a talk?
- [ ] What result kills it, and how cheaply?
- [ ] 2026-10-14 — Scorecard present and filled (CLAUDE.md rule 9): target value, three-scenario ceiling with
      probabilities, relevance including where it is zero, kill probe with cost and criterion, density and
      ownership, why now, register and what it is not. Probabilities are labelled as judgment.
- [ ] 2026-10-16 — A landscape report from a research tool is a harvest, not a kill search. Its "not found" and
      "wide open" sentences are bounded by its search budget and its vocabulary; run the arXiv API density with
      mechanism words before repeating any of them. Today: a report called message-level credit in multi-agent
      systems "wide-open" (quoting a May 2026 survey); the API returned 39 in-window hits including six
      counterfactual/contrastive credit papers, four of them after the survey.
- [ ] 2026-10-16 — For any "no public benchmark" sentence, run the density query on the day of writing: in this
      area three relevant papers landed in the previous seven days (GACC-Bench, 2610.20116, Mosaic).
- [ ] 2026-10-16 — Whose temperature? Any "decision variance" or "signal" quantity is a property of the sampling
      protocol of the party whose moves are resampled. A writer, compactor, reflector or curator run at
      temperature 0 has zero decision variance by construction (ACE's Reflector/Curator; RBC's and RSE-Bench's
      writers). State the protocol the quantity is measured under and why it is the training protocol.
      (Second occurrence of the lesson first learned on τ-bench's temperature-0 agent, 2026-10-14.)
- [ ] 2026-10-16 — "Full context" or "full raw history" is not an upper bound on performance: curated memory
      beats raw history in Dynamic Cheatsheet (FH 26.7 vs 50.0), Mem-α (0.588 vs 0.642) and JitMem (+16 for
      raw history only with a stronger reader); CliffCompaction at 32K beats full context. Define headroom
      against an oracle curation or a stronger reader, name it a signed cost, and expect both definitions to be
      published already.
- [ ] 2026-10-16 — Search with the field's role words, not the mechanism's: for learned memory steps the names
      are write-time curator, read-time curation, reflector, skill curator, memory manager, held-out gate,
      reproduction gap. Problem vocabulary ("signal", "headroom", "consolidation") found a fraction of them.
- [ ] 2026-10-16 — Record whether a paper's "outcome" is a verifier or an LLM judge (SkillOS and ReasoningBank
      reward a judge at ~72.7% accuracy); a learnability claim about outcome reward does not transfer between the
      two.
- [ ] 2026-10-16 — "Zero advantages within a group" is a one-paragraph observation anyone training with GRPO
      writes down (EASE 2609.36746 said it for memory curation). Any proposal whose core is that observation is
      occupied the day a lane has a GRPO paper; look for the sentence before proposing.
- [ ] 2026-10-14 — Protocol check for any variance or reliability claim: which parties sample at temperature
      above zero under the protocol actually used? A party at temperature 0 contributes no variance by
      construction (up to serving noise), so a "share" attributed to it or away from it is a protocol artifact.

## Known confounds in this area
- [ ] Score-weighted majority voting can account for gains attributed to search (Gambit review).
- [ ] Hindsight log-ratios echo policy fluency (Credit Without Ground Truth): is fluency conditioned out?
- [ ] Re-fed prefixes are not the decode-time KV: does the method resume from the original state or
      re-prefill, and does it matter for the estimate?
- [ ] Siblings can be near-clones at low-entropy states: is contrast reported per useful fork?
- [ ] Free branching from GRPO-group overlap (RTMC) already yields step credit early in trajectories: does
      the method add to it or merely replace it?
- [ ] 2026-10-08 — Deterministic sandboxes: GRPO siblings share one environment, so differences between
      siblings are decisions, never luck. Any "environment noise" claim must name its source of real
      randomness (simulated user, LLM judge, LLM-backed tool, flaky test) or it is wrong.

## Added 2026-10-09 from the first pressure-point review (W41)
- [ ] "Unposed" means: the introduction, limitations section and appendix titles of the two closest papers
      were read, and the sentence that leaves the question open is quoted. Abstract-only reading produced two
      false "unposed" verdicts out of four this week (PACE App. C; OverclaimBench §5).
- [ ] The 12-month window measures density, not prior art. Every question's kill search names at least two
      pre-window papers that the in-window neighbors cite (VC-PPO, DAPO, AReaL, Wen ICLR 2025 this week).
- [ ] Premise numbers carry the source's own category name and denominator, verbatim ("functionally
      discrepant from gold, 57%, of resolved patches" — not "62–66% behaviourally wrong").
- [ ] A base → RL pair used in a first measurement states base model id, algorithm and harness for both
      ends and confirms they match; "base" in agentic RL is itself a post-trained model.
- [ ] A first measurement that names a benchmark confirms it is runnable (public code and data) or budgets
      the re-implementation.
- [ ] Judge and critic are different objects with different failure modes (self-preference and length bias
      vs variance, lag and initialization bias); a question that imports one's failure into the other is
      ill-posed.
- [ ] Density-query words to include by default: over-editing / verbosity / minimal edit; selection bias /
      long-tail / abort / partial rollout / straggler; reward-seeking / grader / mislead / refusal;
      explained variance / value pretraining / initialization bias.

## Added 2026-10-10 from the product-shape red team (W41: A killed, B killed, C parked)
- [ ] "Re-score public logs" names, per source, the exact per-step token field, the per-task outcome field
      and the run count, after opening one file from each source. (HAL's "26,597 rollouts" were 380 single-run
      files with 19 duplicated agent–model pairs; OSWorld's 495 GB of trajectories carry no usage field;
      SWE-rebench releases no per-run logs.)
- [ ] A tracker, corpus or any living artifact records each source's release state and last-update date before
      design. Two of four sources paused is a kill (HAL paused 2026-02-01; METR retired; Terminal-Bench 2.0
      submissions closed 2026-05-14).
- [ ] A maintained leaderboard row or column is a shipped artifact: search incumbents' column headers and entry
      labels, not only their methodology prose (Artificial Analysis effort variants = effort curves; SWE-rebench
      cached column = prefix-aware cost).
- [ ] A seed is not a state of the world. For any design that fixes one party's seed and resamples the other in
      a sequential interaction (simulated user, LLM judge, LLM-backed tool), write what the seed still fixes
      after the first divergence of the other party's output. If nothing, the main-effect variance is
      structurally zero and the design measures a random-number stream; use a per-move (martingale)
      decomposition from branched continuations instead.
- [ ] Before decomposing a benchmark's reliability metric, read the metric's definition sentence in the original
      paper. τ-bench defines user-simulator variation as the stimulus pass^k tests, so a "simulator share" has
      no defect reading without an error annotation.
- [ ] Temperature-0 through an API is not a deterministic arm: 80 unique completions of 1,000 at temperature 0;
      batch-invariant kernels cost 1.6–2.1×. Budget the deterministic stack or drop the arm.
- [ ] When a competitor paper writes the target quantity as an equation and calls it future work, record the
      group, their stack and the date; the kill search's "why now" must answer why that group has not done it,
      and "they have the stack" is a guess about priorities, not evidence — the re-open test is asking them.
- [ ] Kill conditions about labeled corpora say natural versus injected failures (Who&When Pro's 12,326
      trajectories are injected after replaying a successful prefix). Annotator-agreement numbers say which
      axis they cover: category labels reach κ 0.84–0.88; step localization sits at 11–26.6%.
- [ ] Agent logs have no common schema (six or more formats in one Terminal-Bench leaderboard repo). Budget the
      normalizer and check for an existing one before the taxonomy.
- [ ] Annotation-based attributions on one benchmark can disagree by 4× (τ-bench 90% agent; Lost in Simulation
      49% agent); when an "expected result" is quoted from one, quote the others.
- [ ] A re-run protocol is not "a tool a benchmark owner runs" if the owner's configuration (an API simulator)
      cannot run it; cost each re-run and list the benchmark's release cadence.
- [ ] Tooling: route arXiv id lookups through `export.arxiv.org/api/query` over HTTPS with `id_list=` (many ids
      per call; verbatim abstracts in the XML) — `arxiv.org/abs` rate-limits at 429 mid-session and WebFetch caps
      quotes at 125 characters; the Hugging Face API (`huggingface.co/api/datasets?search=`) is reachable from the
      shell and finds trajectory releases arXiv misses.

## Added 2026-10-18 from the first cross-field run (W42: 2 filed, 2 already-made)
- [ ] A field's textbook answer has usually been imported into agents already: within 12 months, gauge R&R and
      variance components (2610.00651, 2608.11323), Weibull time-to-failure (Ord 2505.05115, Hamilton Jan 2026),
      rate-distortion for agent compaction (2608.01326, 2607.08032) and e-value acceptance gates (PACE 2606.08106).
      Search for the standard answer first; the unmade import is usually the field's *next* step (frailty versus
      within-unit hazard; decoupled residuals rather than raw innovations).
- [ ] An import's literal form can fail Gate 0. Innovation whiteness and NIS (normalized innovation squared, a
      chi-square consistency test) presuppose noise; a simulator-versus-reference residual is deterministic given
      the state, action and settings, so its only spreads are the domain-randomization range and float error, and
      its correlation over time reflects which states the policy visits. Write the conditioning set before importing a test.

## Readability (added when a report confused Jacob)
- [ ] 2026-10-01 — A method explained in prose without equations is unreadable; write the equations with
      every symbol defined.
- [ ] 2026-10-01 — Per-action quantities (Q/V, "which action is better") and per-state quantities
      (Var[Q], "does the choice matter here") must be named as such wherever both appear.
- [ ] 2026-10-01 — Introduce no term (CARL, belief shift, nested sampling, variance decomposition) without
      its one-sentence trick in the same paragraph.

## Added 2026-10-20 from the first automatic kill run (W43: C-W43-15, C-W43-13, C-W43-01 all survived-kill; red team owed)
- [ ] 2026-10-20 — Warm start is part of the state: a per-step re-simulation audit of an iterative contact solver must carry the rollout's warm-start vector (MuJoCo qacc_warmstart) or declare a cold start; the engine's documented accuracy claim for low iteration caps ('accurate results are obtained with fewer iterations') holds only under warm start, and MuJoCo's docs say warm start is meaningless on states that do not form a trajectory. The two protocols give different per-step errors; the record names which one each number uses. (C-W43-15 kill search.)
- [ ] 2026-10-20 — A paper that bundles several fidelity knobs into one 'simplified simulator' (MFPG-PPO 2610.02505: collision model, time step, solver iterations, self-collisions) occupies the mechanism without answering anything about any single knob; record it as a mechanism precedent and a non-answer for the knob, and add the bundled phrasings ('simplified simulator', 'low-fidelity simulator') to the density query beside the knob's name.
- [ ] 2026-10-20 — An incumbent metric can already answer the objection in weakened form (MMRV weights a rank violation by the real gap, not by the gap's standard error). Before calling a ruler new, write the incumbent's weighting and ours side by side and name the case where they diverge (0.08 at n = 5 vs 0.08 at n = 75).
- [ ] 2026-10-20 — A mechanism can be in print as a reason to omit a metric (Kaedim 2610.00731 App. B: 'We do not report MMRV on this basis') without being in print as a ruler. Search the appendices of the smallest papers in a thread, not only the metric sections of the large ones, before writing 'nobody has done this'.
- [ ] 2026-10-20 — Denominators inferred from decimal rates must pass two checks: the appendix protocol sentence and integer consistency across every cell. SIMPLER's eggplant task says 24 trials in Appendix B and its rates are consistent only with 20; the repo itself reconstructs trial vectors from rates.
- [ ] 2026-10-20 — A release's "code, curves and labels" is not the transcripts: open the README's data layout before costing an arm. 2610.17633 ships the selected runs' transcripts and every continuation's outcome, but no sibling or continuation transcripts, so any arm that reads peers (LVRL's k summaries) needs regeneration (~700 base runs here).
- [ ] 2026-10-20 — Before proposing a control row against a released ground truth, read the release paper's own baseline table: 2610.17633 Table 32 already prices random step, step 1, first edit and first verification by value captured; such rows are citations, not arms.
- [ ] 2026-10-20 — When a critic's endpoints are anchored to the outcome, exclude anchored transitions from any late-trajectory agreement statistic (LVRL App. F.3 does; an audit that does not overstates final-third skill by construction).
- [ ] 2026-10-20 — A claim's headline must be the sentence its cheapest probe tests. Two of seven seeded claims were not (CL-W43-04 named a cross-generation reliability result while its probe tests frailty versus within-task hazard; CL-W43-06 said "early in training" while every fetched number is early in the trajectory); one carried two claims in one sentence (CL-W43-07). Read the probe's kills_if against the headline before grading.
- [ ] 2026-10-20 — An import seed is not kill-applicable until it carries a scorecard (config/generation.yaml: status proposed, scorecard complete). CL-W43-04 and CL-W43-09 ranked 3rd and 9th with no applicable probe; the kill budget skipped to the next claim. Write the scorecard at import time or in the first /mutate.

## Added 2026-10-20 from the first automatic red-team run (W43: C-W43-15, C-W43-13, C-W43-01 all killed; two claims re-probe owed / parked, one refuted)
- [ ] 2026-10-20 — A red team of a zero-cost probe runs the probe's first step. The first two tables scored for C-W43-13 fired its pre-registered kill in an hour; the kill search had called it "survived" without computing anything beyond its seed table.
- [ ] 2026-10-20 — Before pre-registering a kill on an agreement, chance or shuffle statistic, compute what a perfect proxy scores under the record's own noise model. Split-by-resolvability sign agreement is symmetric in the proxy's and the criterion's reliabilities (A = 1/2 + 2(q_r − 1/2)(q_s − 1/2)); a perfect simulator landed exactly on C-W43-13's kill line. A marginal-matched shuffle of a monotone, endpoint-anchored value curve is the random-step row and any monotone curve beats it on rank correlation (C-W43-01); the null that tests step-reading is the straight line between the critic's own anchors or an outcome-blind copy of the prompt.
- [ ] 2026-10-20 — A plug-in ceiling built from observed gaps is observed power (bias +0.29 at a true null, n = 20); a chance-corrected agreement that divides by it is not identified without repeats of the criterion or a hierarchical model across pairs; a reliability estimate from one realization of k ≤ 6 cells is negative a third of the time. Do not promise kappa or an attenuation-corrected r at those cohort sizes.
- [ ] 2026-10-20 — Pairs share policies; curves share tasks. Any contrast over policy pairs or trajectory curves needs a task-cluster bootstrap or a within-task permutation, not a two-proportion interval (SIMPLER's split: [−0.01, +0.44]; VC_2 means: SE ≈ 0.04–0.05 over ~55 curves from ~30 tasks).
- [ ] 2026-10-20 — Each clause of a pre-registered kill conjunction must be satisfiable and each pre-registered outcome informative: a wrong-outcome placebo on an all-failed set forces a non-decreasing curve ("placebo leaves the largest drop unchanged" cannot fire); "unresolvable-pair agreement ≥ 0.9 means the binomial model is wrong" is the perfect-sim prediction. Write the kill as an equivalence bound where the claim is a null.
- [ ] 2026-10-20 — Before pre-registering a "law" for an iterative solver, read the solver's own convergence statement in its manual: exact Newton on a piecewise-quadratic cost converges by active-set identification (zero iterations when warm-started; iterations only on constraint-state changes), not by a contraction factor; a geometric fit is misspecified by construction (MuJoCo docs; C-W43-15). And read the engine's own per-iteration statistics (MuJoCo mjData.solver[], solver_niter, fwdinv) before designing a re-step sweep — when the trace is already logged, the sweep is a profiler read and "why now" is false.
- [ ] 2026-10-20 — A "share of return on high-error steps" is not an estimator of a return gap; for deterministic engines the gap is the signed, value-weighted sum of one-step errors (telescoping identity), and the operational test of "exploitation" is the 2x2 train-in / evaluate-in matrix's interaction term under the training protocol (DR, kicks, sampled actions), with a wall-clock-matched arm.
- [ ] 2026-10-20 — Number format is part of the conditioning set: JAX/Warp simulators run float32 by default and floor acceptance near 8 × 1.2e-7 relative, so a 1e-8 reference is unreachable there; state the dtype and the floor before reading any residual.
- [ ] 2026-10-20 — A critic that reads the whole transcript and the outcome is a hindsight smoother, not a value function (LVRL says so in its own §3.2); nothing measured on it licenses a forward consequence (restart controllers, distillation targets). The forward arm (prefix only, no outcome) is a separate, cheaper experiment; price it on its own.
- [ ] 2026-10-20 — Rank correlation against a monotone ground truth is shape-dominated: simulate the split-half ceiling and the trivial-baseline score (linear decay) under the release's own schedule before promising a Spearman gap (linear decay scored 0.86 on erosion curves against a 0.61 split-half ceiling); grade increments or value captured instead. "Dollar-matched" needs the unit (per call or per trajectory bill), the GPU price and the continuation cost from the release's stated collection cost; subsampling the truth's continuations contaminates the arm. Budget is part of the state in executed-prefix ground truth; run the primary analysis on the uncapped strata the owners use.
- [ ] 2026-10-20 — Before costing a "re-score published tables" probe, open each table: SimFoundry's design is paired on fixed grid positions (the two-sample binomial is wrong), PolaRiS and Kaedim grade progress rubrics (binomial resolvability does not apply), 2606.10366 publishes rankings, not rates. When a kill search lists a statistics paper as an incumbent for a neighbouring deliverable (Snyder: ranking), open its supplement before claiming the adjacent deliverable (its Table II is the sample-size table).
- [ ] 2026-10-20 — A hit counted and unopened is a miss (third occurrence: Branching Policy Optimization 2026-10-08; PolySim 2510.01708 inside C-W43-15's own Q4 hits; Probe-and-Resume 2610.21088 five days old, written in test-time-search words — "critic", "intermediate states", "continuation pass rate", MCTS, fork — invisible to L2's "credit assignment / process reward / placebo / Monte Carlo" queries). Open every hit whose title names the claim's mechanism at a coarser grain, and run each lane's density with both the method vocabulary and the audit/search vocabulary.
- [ ] 2026-10-20 — "Set for performance with no accuracy check" and "nobody has done X" must be checked against the owner's own tuning page or appendix, where the trade and its justification are often one sentence (MJX docs: solver accuracy subordinated to DR noise; Playground's hardware results at the shipped caps; Kaedim App. B; LVRL App. F's own MC validation; 2610.21088 Table 8's full validation table).
- 2026-10-21 — Red team calibration: three of three W43 survivors were killed by substantive objections (an estimator that did not estimate, a kill that fired on real tables, a prior publication), but the defender conceded 84% and answered 5%: the defender is now a separate agent, objections are classified killing/limiting, and a monthly control on a published claim measures whether the gate kills what it should keep.

## Added 2026-10-25 from the closing-W43 weekly run (kill: C-W43-17 killed, C-W43-22 killed, C-W43-23 survived-kill weak; red team: C-W43-23 killed)
- [ ] 2026-10-25 — Before importing a textbook bound into an engine as "our flag", grep the engine's source comments, docs and changelog for the bound's name: MuJoCo 3.11.0's strong-convexity certificate, its stiffness caveat ("force errors of order sqrt(2*gap*stiffness)") and the Newton-decrement termination were in engine_solver.c and the changelog, not in any paper; Warp ships a per-world cap-hit bit and Isaac Lab logs solver_niter every step. The owners' shipped text is an occupant. (C-W43-17.)
- [ ] 2026-10-25 — A zero-hit arXiv conjunction that known occupants should match is a query defect, not evidence: fetch the known occupants by `id_list` and read them before trusting a zero. (C-W43-17 Q4, Q5.)
- [ ] 2026-10-25 — A Spearman against a quantity the statistic provably upper-bounds is shape-dominated and its kill clause contradicts a theorem; pre-register a slack distribution (bound over error, as a ratio) instead. (C-W43-17.)
- [ ] 2026-10-25 — A trim-versus-keep break-even prices the recomputed interval, not the whole trimmed prompt: under a rolling window the masked history is itself a stable cached prefix (CADOC 2609.37012 eq. 2); "published savings are token counts" is checked in each paper's cost appendix first (Complexity Trap App. A, TokenPilot eq. 11 and TurnCost already priced the cache). Search cache-aware context management in operations words (commit, batch, schedule, "as served", loop engineering), not only "observation masking". (C-W43-22.)
- [ ] 2026-10-25 — A "public corpus" named in one candidate's record is not a public corpus for another candidate's cost until the release's data glossary is opened: TRACE ships derived boundaries and rollouts with a 4,000-character observation cap and hashes, not summaries or source trajectories (docs/COLLECTION.md). Third occurrence of "code, curves and labels is not the transcripts" (2026-10-20). LaTeXML-stripped HTML doubles every math-wrapped integer ("4444" = 44); verify counts against the alttext. (C-W43-23 kill search.)
- [ ] 2026-10-25 — A quotation in why_now, target_value or a limitation_quote is grep-verified in the paper's text before it enters a record; a card's information_asymmetry inference written as a quote fabricated a requester in print (2610.26836 has zero occurrences of "oracle" or "compaction"). (C-W43-23 red team.)
- [ ] 2026-10-25 — A judge-free oracle built on a benchmark's reference solutions names the split that ships them: AppWorld withholds solutions on test_normal and test_challenge (train+dev only carry ground_truth/api_calls.json), so a probe costed on 168 test-normal tasks had no oracle on the corpus it named. The first step of any value-matching probe is to run the matcher over the references and report coverage (25.7% of AppWorld needed values are composed or task-given; 34.6% are small integers) before costing. (C-W43-23.)
- [ ] 2026-10-25 — A census of failures after a boundary needs the uncompressed arm as its control before "fails by" is written: SJC Table 3 bounds compaction-attributable failures at 31.5% of the Prompting arm's post-compaction failures (116.9 vs 80.1 of 504 runs), and TRACE's re-audit retained 0 of 3 presence-based INFO-LOSS labels. A presence label is not a cause. (C-W43-23.)
- [ ] 2026-10-25 — When two attackers derive opposite numbers from one protocol (8.6% and 51% unsourced on SJC Table 11), the normalization rule is the unwritten part: pre-register the matcher (typed fields, atomic decomposition, summary membership) before any quantifier enters a headline; an unsourced-persistence estimator must test membership in the summary ($w \in M$) and exclude the never-fetched cell or it is near-entailed by the build share. (C-W43-23.)
- [ ] 2026-10-25 — The bootstrap cluster on AppWorld is the scenario (one template, three variants), not the task: 35 failures in 10 scenarios, one with 9; a lower-bound kill clause is power-checked at the scenario level (half-width about 0.3 at n = 35). On stateful-shell harnesses (ACON/SJC) the produced corpus is defined at the API-response layer, not printed stdout; a variable that survives a boundary is a channel the summary never carried. A lab-position verdict of "a day's audit on owned logs" is checked against what the oracle needs — production logs carry no reference solution. (C-W43-23.)
- [ ] 2026-10-25 — One quantified statement per claim sentence, with the kill set at that number: C-W43-23's sentence carried two quantifiers (one third; 40%) and a causal conclusion, its kill fired at 0.5, and the headline noun "not by length" was touched by no cell. (C-W43-23; second occurrence of the 2026-10-20 headline lesson.)
- [ ] 2026-10-25 — The weekly label and the digest file: a Sunday-evening run is labelled by New York time (the week that is ending); the 2026-10-18 run labelled itself W43 under UTC, so W43 carries two weekly runs (opening digest moved to data/digests/2026-W43-opening.md). Check `data/digests/<week>.md` for an existing file before writing the digest.
