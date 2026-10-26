# Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.

`CL-W43-03` · lane **L1** · status **open** · rank 2 · position both · refreshed 2026-10-26

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed; budget spent on ranks 1-2 and the L3 cost claim this run). Grade on paper: open, ungraded past Gate 5 until the kill search. Next action: see First steps.

## The claim

- **Headline:** Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.
- **Current belief (the field's):** Scaffold papers attribute gains to their design; 2610.22289 §9.3: 'Further analysis is needed to determine their relative contributions'; HAL: higher effort can reduce scores
- **If true:** Scaffold papers must run the effort-notch and fresh-restart control arms; leaderboards separate scaffold from effort
- **If false:** Scaffold design carries independent value beyond effort — a measured answer to an open question

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's abstract recommends 'combining configurations for broader coverage' and reports 14.3% single-model findings while its sec. 7 says a yield 'can shift by a third between runs'; CyberGym and BountyBench report per-agent recall and never a run-accumulation curve (card neighbors). Who pays: security teams deciding whether a scan budget buys models or runs; benchmark owners (CyberGym, BountyBench, ZeroDayBench) who report coverage per agent; harness builders (DeepSec, AgentFlow) whose multi-model designs rest on complementarity.
- **Impact ceiling:** **floor**: A re-analysis note on one matrix: run-versus-model marginal coverage at matched $k = 2$ and the Chao bound on the 265; cited by the next multi-model scanning paper. Requires step 0 only. Judgment p 0.45.; **middle**: A replicated result with accumulation curves on open models and a reporting rule (run-accumulation curve before any complementarity claim) adopted by one security-agent benchmark. Requires step 1. Judgment p 0.35.; **ceiling**: A general ruler, the run-equivalent of model diversity, measured on two more agent domains (coding-agent union coverage on SWE-bench-style tasks, where pass@k across models is reported the same way), changing how ensembles are justified across agent evaluation. Requires two more domains, about 200 GPU-hours. Judgment p 0.15.
- **Relevance:** HAL (Narayanan): direct, cost-controlled comparison and multi-run reliability. Narasimhan (tau-family): moderate, the union over runs is the complement of pass^k and the same run-variance question. Evaluators (CyberGym, BountyBench owners): direct. Industry: direct for security scanning spend. Jacob's edge: the capture-recapture statistics and the matched comparison are evaluable from his background; theoretical physics zero; computer engineering small (serving three open models).
- **Kill probe:** Step 0 on the matrix (zero dollars, 2 days) then three open models times four runs at A1 (about 80 GPU-hours, about $100, 7 days); dead if the model-accumulation union beats the best model's run-accumulation union beyond the run-to-run band at $k = 2, 3$ in both arms.
- **Density and ownership:** From the card's fetched neighbors: CyberGym (2506.02548) scores per-agent proof-of-concept success over 1,507 vulnerabilities and gives no run-accumulation statistic in its abstract; ZeroDayBench (2603.02297) three frontier models, fixed harness, no runs-per-cell statement; BountyBench (2505.15216) 10 agents in dollars of finding; IRIS (2405.17238) and AgentFlow (2604.20801) are methods, not coverage measurements. Occupied by the card: the 60.4% and 14.3% marginals and the per-model Jaccard. The kill search must use the neighbors' words (ensemble, union coverage, complementary, pass@k across models, repeated runs, capture-recapture, species accumulation, unseen species) and quote the card paper's and CyberGym's limitation text; density is counted on the day of writing, not here.
- **Why now:** Card paper 2026-10-20 (open harness, two runs per cell, per-finding cell record); CyberGym 2025-06 (public oracle instances). The estimator is old; the flag is recorded.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W43-19's step 0 is a zero-dollar re-analysis of a released response matrix; C-W43-18 reprices from released per-game dollar ledgers before any run |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: scaffold paper (2610.22289 sec. 9.3: further analysis needed on relative contributions), leaderboard (HAL: higher effort can reduce scores on 21 of 36 benchmarks), meta-paper (2607.12227: matched feedback and inference budgets) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: scaffold papers (run effort-notch and restart arms), leaderboards (separate scaffold from effort columns), harness builders (default effort setting) |
| G4 | mechanism and consequence | pass: mechanism — scaffolds inject tokens and fresh contexts, both of which the effort knob and a restart also inject; consequence — matched-spend reporting, or the scaffold keeps its organisational credit |
| G5 | durability; lab-adjacent | pass as a protocol, flagged as a number: the effort knob persists across generations; ARC-AGI-3 is a static set consumed in months |
| G6 | ownership, density, race window; position clause | open: kill search owed on C-W43-12 and C-W43-11 (limitation text of 2607.12227 and 2609.15309 unread); ownership risk — the same author owns the stack and names the question in sec. 9.3; re-open test is asking him |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-19 | Second run or second model: matched-run accumulation curves for multi-model coverage | Step 0 on the matrix (zero dollars, 2 days) then three open models times four runs at A1 (about 80 GPU-hours, about $100, 7 days); dead if the model-accumulation union beats the best model's run-accumulation union beyond the run-to-run ban… | proposed | — |
| C-W43-18 | Cross the builder's effort with the player's effort on the released self-written harnesses | Two off-diagonal cells on Opus 5 (3 harnesses x 20 games each, effort parameter swapped), about $1,700, 0 GPU-hours, 5 days including the $0 ledger regression; dead if the builder main effect is at least half the player main effect with xh… | proposed | — |
| C-W43-12 | Timed returns as the shuffled control for Stop-and-report | Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched. | proposed | — |
| C-W43-11 | Effort notch and fresh restart as control arms for scaffold gains | Restart-controller arm at GPT-5.5 xhigh capped at 45.5 M normalized tokens, 3 reps x 25 games, about $1,600 of the $2,200, 0 GPU-hours, 6 days; dead if RHAE < 53.2 in all reps and truncation curves separate on B <= 9 M. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-19** (Sunday run), or run `/kill C-W43-19` in a session.
2. If it survives: `/redteam C-W43-19`, then the probe as pre-registered — Step 0 on the matrix (zero dollars, 2 days) then three open models times four runs at A1 (about 80 GPU-hours, about $100, 7 days); dead if the model-accumulation union beats the best model's run-accumulation union beyond the run-to-run band at $k = 2, 3$ in both arms.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded: C-W43-06 and C-W43-07 detached (they test sibling claims, now orphans); cheapest attached probe is C-W43-12; kill search owed; dollar-equivalent of a GPU-week raised as a decision
- 2026-10-25 — claim open: claims (closing W43): C-W43-18 (card 2610.30499) and C-W43-19 (card 2610.28802) attached; C-W43-19's attachment reads 'adding a model' as a restart (fresh run) effect — detach to orphan if Jacob reads 'which models to run' as outside scaffold design; rank 4
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 4 -> 2 after the kill run: two fresh scorecarded probes with a zero-dollar step 0 (C-W43-19), no probe killed

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-03`, version 4)
- probe `C-W43-19`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-18`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-12`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-11`: `data/candidates/2026-W43.jsonl`
