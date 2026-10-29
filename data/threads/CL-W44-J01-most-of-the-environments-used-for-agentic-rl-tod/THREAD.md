# Most of the environments used for agentic RL today are luck-dominated at the group sizes people train with: at G = 8, more than half of the within-group reward variance in user-simulator and flaky-tool environments is environment randomness, not the agent's choices.

`CL-W44-J01` · lane **L2** · status **thought** · rank — · position solo · refreshed 2026-10-29

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

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

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W44-J01-a** (Sunday run), or run `/kill P-W44-J01-a` in a session.
2. If it survives: `/redteam P-W44-J01-a`, then the probe as pre-registered — Pre-registered: dead if lambda < 0.25 in every stochastic environment at G = 8 (luck is a corner case and the headline is false); dead as a headline if a published table already exists (kill search). Expected (judgment): user-simulator environments 0.4-0.7, flaky-tool sandboxes 0.2-0.5, ALFWorld 0, MuJoCo with DR 0.1-0.3. Cost: 20-40 GPU-h, $60-120, two weeks.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Spend the two weeks on the luck table, knowing the recipe half is taken and the result is a proper idea at best?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-10-29 — claim thought: captured from the 2026-10-29 dependence discussion; recipe half found occupied (2609.24144, 2609.33543, 2610.31544); the cross-environment measurement kept as the thought

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-J01`, version 1)
- `P-W44-J01-a`: seed or import record (no candidate yet)
