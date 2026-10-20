# Published step-credit critics for long-horizon agents do not beat their own shuffled control early in training.

`CL-W43-06` · lane **L2** · status **open** · position both · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Published step-credit critics for long-horizon agents do not beat their own shuffled control early in training.
- **Current belief (the field's):** LVRL 2610.15840 reports its step credit is unreliable early (44% vs 88%) and leaves the separation to future work; critics are evaluated against end-task success, not against executed replay
- **If true:** Critic papers must report the shuffled-control and placebo arms against executed ground truth; dollar-matched Monte Carlo becomes the baseline
- **If false:** The critic beats its shuffle from the start — then the audit is a confirmation the critic's authors cite

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** Asked in print: LVRL (2610.15840) states its step credit is unreliable early (44% vs 88%), leaves separating anchors from in-context siblings to future work, and calls the frontier bill prohibitive under budget limits (card complaints 2 and 3); 2610.17633 sec. 7 says value estimators controllers need 'can be built and ranked' against its curves; CWGT's abstract: existing evaluations grade step correctness, it audits contribution, and they come apart. Who pays: training teams spending order $10k per AppWorld run on a frontier critic plus summarizer; restart or controller builders (2608.03222, 2609.38147) who need a forward prefix value.
- **Impact ceiling:** **floor**: A footnote: the anchored frontier critic's localization on SWE failures sits inside its own shuffle in all thirds, or beats it only late, with a measured ranking of three estimators against a noise ceiling; requires the release to contain trajectory text and per-continuation outcomes; p = 0.5 (judgment).; **middle**: A measurement paper: value-captured share and Spearman by trajectory third for the critic, k = 0, placebo, shuffle, MC and log-ratio arms, with the mechanism (outcome-reading vs step-reading) separated and the recipe consequence that anchors plus uniform split equal the critic for the first two thirds at $0; requires step 0 to show resolution and the 60 second-agent curves to replicate; p = 0.35 (judgment).; **ceiling**: The critic survives placebo, beats shuffle early and matches MC: first replay-graded evidence that frontier models carry forward value on long-horizon agent runs, which makes a distilled local critic a sound target and changes what restart controllers use; or the reverse, 'Spearman with executable V' becomes the reported validation for step-credit claims adopted by one training group; requires curves from a second scaffold (~100 GPU-hours); p = 0.15 (judgment).
- **Relevance:** Narasimhan route (Odysseus, EasyPPO) and any RL group: a ground-truth grade of the lane's most expensive credit signal, usable as a baseline table; the uniform/shuffle/placebo/MC arms become required controls. Industry: anyone paying frontier API for critics. Jacob's edge: the instrument's statistics (binomial noise at 331 continuations, bootstrap over curves, placebo design, attenuation by noisy ground truth) is a physics-trained fit; computer engineering: zero (no systems component); L5: zero.
- **Kill probe:** Step 0: oracle-vs-random VC_2 gap on the released curves, $0, 1 day, dead if intervals overlap. Step 1: critic plus controls and the dollar-matched MC arm, about $550 API and 10 GPU-hours, 5 days; claim dead if the critic beats its shuffle in the first third, holds under placebo and matches MC within 0.05 Spearman.
- **Density and ownership:** —
- **Why now:** 2610.17633's released V-curves (2026-10-13) make the ground truth free; LVRL's prompt (2026-10-11) is the first published anchored in-context critic with its own early/late number; CWGT (Aug 2026) supplies the pre-registered audit template; Fail-Fast 2608.03222 (Aug 2026) trained a forward monitor on the same Qwen3.6-27B policy, a further estimator to grade.
- **Register, and what it is not:** measurement / ruler with a dollar-matched comparison. It is not a new critic, not a training run, and not a reproduction of LVRL's AppWorld or BabyAI numbers.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-01 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-01 | Placebo and dollar-matched audit of LVRL's anchored frontier critic on released V-curves | Step 0: oracle-vs-random VC_2 gap on the released curves, $0, 1 day, dead if intervals overlap. Step 1: critic plus controls and the dollar-matched MC arm, about $550 API and 10 GPU-hours, 5 days; claim dead if the criti | proposed | — |
| C-W43-02 | Budget loss versus state loss: the two controls executable restart skipped | ~6,100 continuations (full-budget anchors on 40 failed runs; screening curves on 30 successful runs); ~80 H100-hours, ~$250; dead if beta < 0.15 on capped runs and false-kill rate < 5%; 7 days. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-01** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Step 0: oracle-vs-random VC_2 gap on the released curves, $0, 1 day, dead if intervals overlap. Step 1: critic plus controls and the dollar-matched MC arm, about $550 API and 10 GPU-hours, 5 days; claim dead if the critic beats its shuffle in the first third, holds under placebo and matches MC withi
3. Write the result into the probe's record and this thread's Log; the claim's status moves only on evidence.
4. Only then: red team (`/redteam <probe>`), then the next probe under this claim by cost.

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-10-19 — open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run

## Records

- claim record: `data/claims/claims.jsonl` (id CL-W43-06)
- probe `C-W43-01`: `data/candidates/*.jsonl`
- probe `C-W43-02`: `data/candidates/*.jsonl`
