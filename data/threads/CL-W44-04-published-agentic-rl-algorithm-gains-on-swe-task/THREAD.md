# Published agentic-RL algorithm gains on SWE tasks do not survive a tuned asynchronous baseline with bitwise-consistent rollouts, and environment scale at matched compute moves the score more than any loss choice.

`CL-W44-04` · lane **L2** · status **thought** · rank None · position lab · refreshed 2026-11-03

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: Gate 1 (no probe under one GPU-week; lab position only); Gate 6 not yet established. Grade on paper: thought (top-down from pressure #11); lab position; the definitive-comparison shape for L2. Next action: see First steps.

## The claim

- **Headline:** Published agentic-RL algorithm gains on SWE tasks do not survive a tuned asynchronous baseline with bitwise-consistent rollouts, and environment scale at matched compute moves the score more than any loss choice.
- **Current belief (the field's):** DeepSeek-V4.1-Flash tech report (L20, arXiv:2609.19969, 2026-09-17): 'under a fixed and unremarkable optimization procedure, systematic improvements in the scale, diversity, and verifiability of synthesized data and environments account for essentially all of the observed gains. [...] the marginal return of engineering the data and environment pipeline substantially exceeds that of algorithmic novelty in post-training' — a finding at one lab's scale, with no 2 x 2 in the open; Arctic-SWE (Q10, arXiv:2610.24914, 2026-10-17): 'This makes gains from new algorithms or data hard to distinguish from improvements to an under-tuned baseline. [...] No single component is new, yet together they form the missing foundation'; vLLM train-inference consistency post (Q08, 2026-10-14): 'the high-performance baseline's train-inference KL rose from 2e-3 to 29.9 while reward fell back [...] the consistent run's SWE-bench Pro score holds while the baseline's drops from 0.56 to 0.22 [...] neither baseline was thoroughly tuned or explored: each ran a single configuration' — each source poses a third; academic L2 papers report estimator deltas against untuned, inconsistent baselines
- **If true:** Method papers report against a tuned asynchronous baseline with the consistency flag and a train-inference KL column; L2 recipe work is retired for solo positions in favour of environment measurement and systems; the lane's out-of-scope rule ('a new advantage estimator evaluated on one benchmark') becomes the field's own
- **If false:** The deltas survive: the loss still matters at small environment scale, which is where academic RL lives, and the audit's residue is the tuned consistent baseline as a public artifact

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: Arctic-SWE names the under-tuned-baseline confound (Q10); vLLM's post names the untuned baselines in its own comparison (Q08); DeepSeek states the environment-versus-algorithm attribution at its scale and runs no 2 x 2 in the open (L20). Who pays: academic RL groups publishing estimators, open labs (SkyRL, DeepSWE, verl), NVIDIA and vLLM, anyone budgeting rollouts.
- **Impact ceiling:** **floor**: A tuned asynchronous 4B baseline with the consistency flag and both run logs published as an artifact; one method delta re-run. Requires the consistency pair. p = 0.5 (judgment).; **middle**: Two published deltas vanish on the tuned consistent baseline and environment scale moves the score more than either: method papers in the lane adopt the baseline and the KL column. Requires all six arms (lab). p = 0.25 (judgment).; **ceiling**: The reporting standard (tuned consistent baseline, KL column, environment-scale arm) becomes the venue norm for agentic-RL method papers. Requires the middle result plus adoption by one venue or open lab. p = 0.05 (judgment).
- **Relevance:** L2 direct (the definitive-comparison shape). Narasimhan route: Odysseus and EasyPPO are recipes the audit would measure — relevant and delicate. Systems route (Lloyd, Netravali, Dao): bitwise consistency and asynchronous stacks are their vocabulary; direct. Industry: open labs. Jacob's edge: numerics (bitwise consistency, FP8 rollouts) load-bearing. zero_where: L4, L5; the robotics route; solo position (Gate 1 fails solo).
- **Kill probe:** P-W44-04-audit: ~1,800 GPU-h over six arms (~600 for the consistency pair), lab position, one month; dead if both published deltas survive on the tuned consistent baseline and the environment-scale contrast is smaller than either method contrast.
- **Density and ownership:** P11a = 2, P11b = 0 in the 12-month window; incumbents are recipes and one flag, none an audit; the combined re-run is unposed in every fetched source; owners of the stack (Snowflake Arctic-SWE, vLLM) are the obvious authors; the lane publishes about one estimator paper a week, so the race is on the methods, not on the audit.
- **Why now:** A released, tuned 4B recipe (Arctic-SWE, 2026-10-17) and a released consistency flag with both run logs (vLLM, 2026-10-14) make the tuned consistent baseline reproducible for the first time; DeepSeek's attribution statement (2026-09-17) gives the audit its hypothesis.
- **Register, and what it is not:** Measurement (a definitive comparison and a reporting standard with a baseline library). It is not a new estimator, not a new environment, not a systems paper on asynchrony.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass on the premise numbers (Q08 KL 2e-3 to 29.9, 0.56 to 0.22; L20 and Q10 statements; fetched and dated); the quantity is a delta at matched rollout tokens on one stack with the consistency flag as the controlled variable — conditioning stated; plain trick: fix the baseline and the numerics, then see what is left of the method |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | fails solo: no probe under one GPU-week (six arms at ~300 GPU-h each; the consistency pair alone ~600); a thought, lab position only |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A, narrowly: tech-report (L20, Q10) and blog (Q08) — two source types, three records; the pressure report ranks it eleventh on breadth |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every method paper on an asynchronous stack (report against the tuned consistent baseline with a KL column); open labs (SkyRL, DeepSWE, verl recipes); NVIDIA and vLLM (the flag as default); the pressure report's objection: a negative result about other people's methods is the paper shape reviewers reject, and labs already run consistent and tuned |
| G4 | mechanism and consequence | pass: mechanism — with verifiable, diverse tasks every unbiased policy-gradient estimator extracts about one bit per episode, so estimator choice matters only where reward is sparse or a critic adds information, while environment scale changes the number of episodes with any bit at all; gated reward, importance-weight control and engine alignment each remove a failure that early curves hide, so an under-tuned baseline leaves them in and any method that incidentally fixes one claims the gain; with MoE routing a small logit difference flips the expert combination on about 7% of tokens per updat… |
| G5 | durability; lab-adjacent | pass as a reporting standard; the definitive-comparison shape is the one L2's positioning default allows from a lab position; lab-adjacent for the audit, lab-contested for any fix |
| G6 | ownership, density, race window; position clause | open: density P11a = 2 (2609.22870 title only), P11b = 0; incumbents Arctic-SWE (baseline, no re-runs), vLLM's consistency skill (one recipe), SkyRL and DeepSWE (recipes), Thinking Machines (batch invariance, single-turn); C-W44-DEF-L2 (credit at matched compute, under CL-W43-06) is the sibling spec and shares the stack; why now: a released tuned 4B recipe (2026-10-17) and a released consistency flag with both run logs (2026-10-14); kill search owed |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |


Also under this claim (no scorecard yet): none yet — thought (first measurement sketched in pressure #11: the Arctic-SWE recipe at 4B as the tuned baseline; rerun with and without the vLLM consistency…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **none yet — thought** (Sunday run), or run `/kill none yet — thought` in a session.
2. If it survives: `/redteam none yet — thought`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-02 — claim thought: written top-down by the W44 claims run from pressure #11 (L20, Q10, Q08 quoted); no probe under one GPU-week — lab position, thought; second of two new L2 claims this week (cap respected); concept-level kill search owed

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-04`, version 1)
