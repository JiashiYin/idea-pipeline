# Most of the environments used for agentic RL today are luck-dominated at the group sizes people train with: at G = 8, more than half of the within-group reward variance in user-simulator and flaky-tool environments is environment randomness, not the agent's choices.

`CL-W44-J01` · lane **L2** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G0. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** Most of the environments used for agentic RL today are luck-dominated at the group sizes people train with: at G = 8, more than half of the within-group reward variance in user-simulator and flaky-tool environments is environment randomness, not the agent's choices.
- **Current belief (the field's):** Paired rollouts with event-keyed noise in group-relative RL are in print: 2609.24144 'Luck Is Not Skill' (2026-09-21, fetched: pairing removes the between-schedule component of reward-contrast variance but need not reduce gradient variance; 2B tool-use agent, pre-registered; +5.1 pp under tool faults, no learning-curve win; gradient covariance traces down 21-30% under grader flips and 40-63% under tool faults), OSCC 2609.33543 (2026-09-27, observation-safe coupling with a gradient-aware criterion), TWICE 2610.31544 (2026-10-22, twin worlds via Gumbel noise keyed by turn and line; variance scaled by 1 - rho), EPIG-Tree 2609.20004 (law-of-total-variance decomposition of the policy gradient into decision and continuation uncertainty), 'Drowning in Routine' 2606.22164 (decision density rho; SNR scales as rho^-1/2), event-keyed hashing for common random numbers 2603.11084, paired seeds 2512.24145. None of them reports the luck share across the environments the field actually trains in; 2609.24144 injects faults into one environment.
- **If true:** Training teams choose coupling (TWICE / paired rollouts) and group size per environment from a table rather than by default; benchmark owners report the luck share of their environment as a property; the per-turn split of Oct 2026 finds its consumer in training, not evaluation.
- **If false:** Real environments are skill-dominated and the Sept-Oct 2026 coupling methods address a corner case - a reassuring table training teams would still cite.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked in print: 2609.24144 reports that pairing helps under tool faults and not under grader flips - the kind of environment dependence that only a table across real environments settles; EPIG-Tree and TWICE both need the continuation-uncertainty share to allocate budget. Who pays: training teams choosing coupling and group size; benchmark owners.
- **Impact ceiling:** **floor**: A table of luck shares across six environments at three group sizes, cited when people choose G or coupling. p = 0.6 (judgment).; **middle**: Environment owners report the luck share as a property and training recipes condition on it. p = 0.2 (judgment).; **ceiling**: The luck share becomes the standard first measurement of any new agentic-RL environment. p = 0.05 (judgment).
- **Relevance:** L2 (training dynamics) direct; L1 (variance attribution) direct - the per-turn split of October 2026 with a training consumer; Narasimhan route (tau-bench user simulator) direct; systems route zero; Jacob's edge (identities, variance decompositions) load-bearing. Positioning: a ruler, lab-adjacent; the recipe side is occupied and lab-contested.
- **Kill probe:** P-W44-J01-a: 20-40 GPU-h, two weeks; dead if lambda < 0.25 everywhere stochastic or a table exists.
- **Density and ownership:** Dense on the recipe side (seven papers Sept 2025-Oct 2026 listed above); the cross-environment measurement unfound in this session's queries (134 hits on GRPO AND stochastic/noise AND agent, relevance-ranked, first 25 read); kill search owed with the Luck paper's related work as the seed.
- **Why now:** The coupling recipes landed in Sept-Oct 2026 and need the number; open-weights user simulators and batch-invariant inference make the nested sampling exact.
- **Register, and what it is not:** Measurement (a ruler across environments) with a recipe-selection consequence; not a new estimator.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W44-J01-a (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W44-J01-a | For each environment, sample G agent trajectories per task; for each trajectory re-run the environment's randomness K t… | Pre-registered: dead if lambda < 0.25 in every stochastic environment at G = 8 (luck is a corner case and the headline is false); dead as a headline if a published table already exists (kill search). Expected (judgment): user-simulator env… | thought | not run (no candidate record yet) |

## Kill search

### Concept level (CL-W44-J01) — killed (2026-11-22)
Gate 0: lambda (an ICC) has no G in it; in user-simulator environments it is the harness's unpinned simulator temperature (zero at T=0 by construction), in flaky-tool environments a fault-rate dial; the probe's fixed-action estimator is undefined past the first differing reply. 2B and 4 fail behind it; 2609.24144 occupies the instrument at G=8.
Full record: [`data/reports/2026-W47-kill-CL-W44-J01.md`](../../../data/reports/2026-W47-kill-CL-W44-J01.md).
**Occupied by:** 2609.24144 (the instrument: lambda = sigma_env^2/(sigma_env^2+sigma_pol^2) named 'the luck share, an intraclass correlation', estimated from 8x8 schedule-by-sample tables on a G=8 GRPO run; 0.33-0.38 at step 0, 0.44-0.53 at step 100 at p=0.25; 0.03 before calibration). The cross-environment table is the only difference and each of its cells is a protocol choice.
**Why not done before:** it is hard because the quantity is not a property of the environment: zero by construction in the deterministic environments the field trains in most (search over a fixed corpus, ALFWorld, WebShop, sandboxes), a designer's fault rate where injected, and an unpinned second-party temperature in user-simulator environments; the group that built the instrument registered an external-benchmark tier and did not run it, and wrote that the number 'is not a validated predictor of learning gains'
Closest neighbors (one-sentence trick; one-line difference):
- `2609.24144` Luck Is Not Skill: When Do Paired Rollouts Help Group-Relative RL of LLM Agents? — Give every sibling of a GRPO group the same event-keyed environment draws so reward differences inside the group are the policy's, and measure what that does to the gradient. *Difference:* none — occupied for the instrument: defines lambda as 'the luck share, an intraclass correlation', estimates it from 8x8 schedule-by-sample tables on a G=8 run, reports 0.33-0.53 at p=0.25 and 0.03 before calibration; lacks only a second environment (its 'ext…
- `2610.31544` Same Luck, Different Choice: Twin-World Credit Assignment for Agentic RL (TWICE) — Key every token's Gumbel noise by turn and line so a counterfactual decision can be rolled out in the same world and the paired difference becomes turn credit. *Difference:* Its environments are deterministic by its own observation ('the retriever, the corpus, and the grader are deterministic'); rho (0.57; 0.36 under injected retrieval noise) couples the policy's downstream noise, not environment luck — the record's 'rho estimate…
- `2606.05885` When Denser Credit Is Not Enough: Evidence-Calibrated Policy Optimization (ECPO) — At each anchor state shrink low-count action estimates and weight step credit by the between-action share of return variance B_s/(B_s+W_s). *Difference:* The complement 1-lambda at the action level computed inside GRPO groups and used as a gate ('anchors dominated by within-action randomness'), on deterministic ALFWorld and WebShop where the within-action noise is the policy's own; no environment channel, no t…
- `2609.33543` OSCC: Certified Observation-Safe Coupling Optimization — Certify a coupling of rollouts as safe and choose among independent, root-only, continuation-only and full coupling by a gradient-aware criterion. *Difference:* Tabular Leduc and Kuhn poker; the chance share is the game's, not an LLM environment's.
- `2609.20004` EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient RL — Split policy-gradient variance by the law of total variance into decision and continuation uncertainty and branch where a branch most reduces it. *Difference:* The decomposition used for allocation; continuation uncertainty mixes 'recovery attempts, and environment-randomness events' and is never split; control suites and Wordle.
*Search degraded:* ['s2', 'exports', 'verl issue tracker (422, not searchable)', 'task id 2609.02547 defective (astronomy); corrected to 2509.02547']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Spend the two weeks on the luck table, knowing the recipe half is taken and the result is a proper idea at best?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-29 — claim thought: captured from the 2026-10-29 dependence discussion; recipe half found occupied (2609.24144, 2609.33543, 2610.31544); the cross-environment measurement kept as the thought
- 2026-11-02 — claim thought: pressure #8 (2026-11-02): B23 StressSim 'tau-bench pass^4 scores decreasing by up to 69% on gemini-3.8-flash and 62% on gpt-5.6-sol [...] using an optimisation budget of 20 rollouts per task' — the adversarial-cooperative spread is the part of within-group reward variance that is the simulator's plan; L22 DeepSeek trains against 'mocked tools that reproduce the interfaces and behaviors of real-wo…
- 2026-11-22 — claim killed: concept-level kill search (data/reports/2026-W47-kill-CL-W44-J01.md): killed — gate G0; Gate 0: lambda (an ICC) has no G in it; in user-simulator environments it is the harness's unpinned simulator temperature (zero at T=0 by construction), in flaky-tool environments a fault-rate dial; the probe's fixed-action estimator is undefined past the first differing reply. 2B and 4 fail behind it; 2609.24…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-J01`, version 3)
- `P-W44-J01-a`: seed or import record (no candidate yet)
