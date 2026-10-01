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
- [ ] "Why now": name the enabling piece and when it landed. "No reason" is a flag.
- [ ] Is the entropy-only version of the idea in the ablation? Many ideas collapse to it.
- [ ] Does the idea survive if placement turns out second-order to the advantage form?
- [ ] One-sentence trick for the candidate itself, presentable in a talk?
- [ ] What result kills it, and how cheaply?

## Known confounds in this area
- [ ] Score-weighted majority voting can account for gains attributed to search (Gambit review).
- [ ] Hindsight log-ratios echo policy fluency (Credit Without Ground Truth): is fluency conditioned out?
- [ ] Re-fed prefixes are not the decode-time KV: does the method resume from the original state or
      re-prefill, and does it matter for the estimate?
- [ ] Siblings can be near-clones at low-entropy states: is contrast reported per useful fork?
- [ ] Free branching from GRPO-group overlap (RTMC) already yields step credit early in trajectories: does
      the method add to it or merely replace it?

## Readability (added when a report confused Jacob)
- [ ] 2026-10-01 — A method explained in prose without equations is unreadable; write the equations with
      every symbol defined.
- [ ] 2026-10-01 — Per-action quantities (Q/V, "which action is better") and per-state quantities
      (Var[Q], "does the choice matter here") must be named as such wherever both appear.
- [ ] 2026-10-01 — Introduce no term (CARL, belief shift, nested sampling, variance decomposition) without
      its one-sentence trick in the same paragraph.
