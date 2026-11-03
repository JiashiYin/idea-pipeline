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
- 2026-10-29 — Scoop watch: the W41 per-turn luck/skill instrument (parked 10-14) appeared as a training recipe in three papers within six weeks (2609.24144, 2609.33543, 2610.31544). Counted as a generator hit; the lesson (consumers across registers before parking) is in taste.md §3.

## Added 2026-11-01 from the W44 pressure red team (#1 killed, #2 candidate-worthy narrowed, #4 killed)
- [ ] 2026-11-01 — A pressure synthesis's "unposed" from two-word problem-vocabulary conjunctions is a query defect, third occurrence (P1a/P1b returned 1 and 2, P4a/P4b 2 and 0; with the field's role words the same questions return 6–109 hits and ≥ 12 direct occupants each). Role words for reward hacking: hackable, unearned pass, integrity gap, verifier hardening, hacker-fixer, hack-verifiable, loophole; for persistence and scope: scope, authorization alignment, impasse, blocker, escalation, overeager, dead-end, goal pressure, evasion, consent. Run the role-word density before any "unposed" verdict enters the ranked table. (W44 #1, #4.)
- [ ] 2026-11-01 — Before writing a product decomposition $a = s \cdot q$, write the event's necessary conditions: an attempt does not require a surface (Vals MiMo audit: a cache search on a Go task with no Git history), so an attempt rate is not bounded by the hack-surface fraction; only the rewarded rate is. A headline whose quantity is "attempts" cannot claim "tracks the surface". (W44 #1.)
- [ ] 2026-11-01 — "Not the checkpoint" needs a series that holds the environment fixed; a lab's own cross-generation band (Fable 5.1 card, 20–28%) does not, by the card's own sentence ("we do not compare them across models that trained on different environments"), and the only matched-task series in print moves 7× (2609.34262: 24% → 73% → 11% → 0%). Name the series that holds the other axis fixed before writing a "not X" clause. (W44 #1.)
- [ ] 2026-11-01 — "Free data: paired trials on both versions" is checked against the host's leaderboard registry and one payload row before costing: Harbor Hub registers one Terminal-Bench leaderboard (4-0-0), the tbench.ai 3.0 URL serves the 4.0 payload, and rows carry aggregates (accuracy, pass@2–5, successes, tokens) with no per-task vector; a retired version's board disappears while its dataset revision persists (Hub revision 1 tagged 3.0.0). Fourth occurrence of "code, curves and labels are not the transcripts"; the preserved asset is the package, not the board. (W44 #2.)
- [ ] 2026-11-01 — "Reordered six of eight" is a rank correlation, not a count (FrontierCode 1.1 → 2.0: $\rho = 0.83$, one owner-model drop 3 → 6 and a bottom-two swap), and a "re-version" can be a new task set ("55% more repositories") with no kept subset to pair. Compute $\rho$ and check task overlap before writing "reordered". (W44 #2.)
- [ ] 2026-11-01 — A lab card can already carry the decomposition in its section headings (GPT-6.1 Terra §7.1 Respecting Auto-Review = harness-origin barriers; §7.2 Respecting Warnings = environment-origin barriers; with the capability-entanglement caveat in its own words). Read the headings of the two closest cards before proposing a split they already report. (W44 #4.)
- [ ] 2026-11-01 — A variance-share headline ("X moves it more than a generation") is design-dependent: the share depends on which levels of X and which generations are in the crossed set. Name the shipped levels in the headline or the quantity fails Gate 0's protocol clause; and when every neighbour reports both axes large with interactions (Troy Moment 2609.15494; one tool 59% → 3% in 2603.01608), the field's assumption is "interaction", so "X dominates" is a pre-registered surprise only after the counter-evidence is answered in writing. (W44 #4.)
- 2026-11-01 — Defender calibration, second run under the separate-defender rule: 36 objections, 14 answered (39%), 21 conceded (58%), 1 open; every killing objection carried a fetched id or a page quote; the conceded set contained no taste objection. The trip-wire (conceded > 80%, answered < 10%) was not approached.

## Added 2026-11-01 from the W44 weekly run (12 concept-level kill searches: 11 killed, 1 survived then refuted by its design red team)
- [ ] 2026-11-01 — A host's registry keeps retired versions' boards: Harbor Hub serves the Terminal-Bench 3.0 leaderboard under revision 1 with per-trial records (reward, error_type, timestamps); "the old board is gone" is checked against the host's server actions, not the public page. (C-W44-19 red team; corrects the pressure red team's line above.)
- [ ] 2026-11-01 — A power simulation must simulate every arm the kill clause names; a hybrid arm absent from the simulation makes the reported kill rates the DiD's, not the probe's. (C-W44-19.)
- [ ] 2026-11-01 — A conjunction headline dies when either clause dies on free data; file the clauses as separate claims or accept the conjunction's risk in writing. (CL-W44-02: the ordering clause died on the shipped board at step 1.)
- [ ] 2026-11-01 — A version "repair" label from a change log is not a content diff: 5 of 19 "fixed" TB 4.0 tasks had no substantive change and 7 "untouched" tasks had file changes; define the repaired set by the file diff and report the change-log labelling as secondary. A hybrid arm that swaps one field does not isolate a channel when the new version also changed budget sentences, pinned images and verifier blocks; the arm carries the whole uniform bundle. (C-W44-19.)
- [ ] 2026-11-01 — The occupant is usually invisible to the claim's own words and visible to the neighbours' role words: "penetration" + policy found SimuGuard where "solver iterations" + exploit returned 0 (CL-W43-01); "false positive / leaky / static audit" found 2607.11022 where "hack rate / base model / onset" found only SimHack (CL-W43-13); "item response / Rasch / latent difficulty" found 2610.12466 where frailty / hazard / Weibull found nothing (CL-W43-04); "restart / re-prefill / suffix cache reuse / block masking" found Memento and MemoryWalker (CL-W43-11); scheduler feature names (pause/resume/TTL/headroom/admission) found MISA-T and TideRL where the import's queueing words returned 1 (CL-W43-12). Run every lane's density with the role words of the three nearest communities before the claim's own vocabulary.
- [ ] 2026-11-01 — Read the closest paper's bibliography for off-arXiv incumbents (two of CL-W43-04's three occupants were notes cited in 2610.12466). A within-unit hazard needs a within-unit clock: horizon data without durations cannot carry a "per-minute hazard" clause.
- [ ] 2026-11-01 — The benchmark owners' protocol section is an occupant of Gate 2B: HAL's temperature-zero attribution sentence (2602.16666 sec. 4) was the claim's own headline (CL-W43-J01); read the protocol and limitation sections of the benchmark's own paper before writing a claim about its variance.
- [ ] 2026-11-01 — Twelve claims from one lane map, kill-searched the same week, died for the same two reasons: the surprise equalled the field's stated knowledge (Gate 2B, 8 of 11) or an occupant published in the last 90 days (Gate 6, 3 of 11). The generators write claims from the lane sentences, and the lane sentences are the field's own open questions; the next generator run reads this week's eleven kill reports first and writes claims one level narrower than the occupants' limitation sentences.
- [ ] 2026-11-01 — Parallel kill-search agents keep helpers and logs under per-claim directories; a shared helper was overwritten mid-run in wave 1.

## Added 2026-11-03 from the real-to-sim investigation (live session; CL-W45-J01)
- [ ] 2026-11-03 — "Heavily adopted" is a count, not an impression: a maintained list (`YanjieZe/agent-real2sim2real`, 75 papers in 13 weeks) settled in one fetch that agent-driven physical calibration on a real robot is 1 of 27, assignment-by-prior is the norm (NVIDIA SimReady: friction "assumed 0.8 / 0.6 ... not calibrated"), and the vivid demos are replay. Count the list before arguing the premise (Gate 0).
- [ ] 2026-11-03 — Separate the use cases before judging a practice: calibration is the point for *evaluation* twins (the sim must predict this scene; X2Real 0.84, R2S-Eval, PolaRiS) and a cost for *training* data (breadth over the prior; digital cousins, co-training, MetaGenSim). A practice that looks prevalent may be prevalent in the other use case.
- [ ] 2026-11-03 — Density check in the import's own words as well as the field's: the arXiv conjunction (Sobol OR variance-based sensitivity OR value of information OR EVPI) AND sim-to-real AND robot returned 0 while the field's words (task-oriented exploration, task-driven adaptation, measurement budget) returned the occupants of the concept; both counts go in the report, the zero is the density datum and the occupants are the one-line differences.
- [ ] 2026-11-03 — A statistics finding the user raises (transfer scores on binary outcomes at n = 50 have a 10-point standard error) is answered with the number and the fixes in print (SureSim, sequential tests, paired conditions), filed as a finding in the program note, and not as a claim: the evaluation-statistics owners (Princeton IRoM) have stated it, and the W44 run killed the L1 noise-floor set for exactly that reason (Gate 2B).
