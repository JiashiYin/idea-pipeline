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

## Readability (added when a report confused Jacob)
- [ ] 2026-10-01 — A method explained in prose without equations is unreadable; write the equations with
      every symbol defined.
- [ ] 2026-10-01 — Per-action quantities (Q/V, "which action is better") and per-state quantities
      (Var[Q], "does the choice matter here") must be named as such wherever both appear.
- [ ] 2026-10-01 — Introduce no term (CARL, belief shift, nested sampling, variance decomposition) without
      its one-sentence trick in the same paragraph.
