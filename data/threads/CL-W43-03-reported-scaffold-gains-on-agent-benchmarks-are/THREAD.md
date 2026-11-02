# Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.

`CL-W43-03` · lane **L1** · status **killed** · rank None · position both · refreshed 2026-11-02

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search owed; race flag from pressure #3). Grade on paper: open; four scorecarded probes with two zero-dollar steps; kill search owed. Next action: see First steps.

## The claim

- **Headline:** Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.
- **Current belief (the field's):** Scaffold papers attribute gains to their design; 2610.22289 §9.3: 'Further analysis is needed to determine their relative contributions'; HAL: higher effort can reduce scores
- **If true:** Scaffold papers must run the effort-notch and fresh-restart control arms; leaderboards separate scaffold from effort
- **If false:** Scaffold design carries independent value beyond effort — a measured answer to an open question

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's sec. 6.1 and 4.2 name unmatched runtime settings and recovery runs as the limit on causal conclusions about harness design; HAL (2510.11977, per the CL-W43-14 thread) reports higher effort giving equal or lower accuracy in 21 of 36 combinations; 2610.22289 sec. 9.3 (per the CL-W43-03 thread) says 'Further analysis is needed to determine their relative contributions'. Who pays: harness benchmark owners, harness vendors comparing products at fixed model, leaderboards with a harness column, and teams choosing a harness for a model on the strength of a 20-point single-run swing.
- **Impact ceiling:** **floor**: A re-analysis note: the dose and reset shrinkage of the harness contrasts on the released grid, per model group, with the mediation caveat; cited by the next harness benchmark. Requires step 0 only. Judgment p 0.5.; **middle**: The first pinned-effort, matched-budget cross-vendor harness comparison, with the share of the harness gap that is effort and the per-dimension profile of the remainder; a harness benchmark adopts gateway-pinned effort. Requires step 1. Judgment p 0.3.; **ceiling**: Matched-effort reporting becomes the norm for scaffold and harness claims (CL-W43-03's consequence), with this grid and the ARC-AGI-3 probes as the two instances. Requires the ARC-AGI-3 arm (C-W43-11) to agree and one further benchmark, about 2,000 dollars. Judgment p 0.15.
- **Relevance:** HAL (Narayanan): direct, effort-controlled comparison. Narasimhan (tau-family): low to moderate, the effort knob exists there but no harness grid does. Evaluators and harness benchmark owners: direct. Industry: direct for harness vendors and buyers. Jacob's edge: the mixed-effects fit and the mediation-versus-intervention distinction are evaluable from his background; computer engineering small (a gateway request rewrite); theoretical physics zero.
- **Kill probe:** Step 0 (zero dollars, 3 days) then 2 harnesses x 95 tasks x 2 arms x 2 runs on Opus 5 through the gateway (0 GPU-hours, about 1,100 dollars, 7 days); dead if the dose and reset terms shrink the harness contrast by under 25% in at least 7 of 9 model groups and the pinned-effort, matched-cut gap stays above 11.6 points and outside the run band.
- **Density and ownership:** From the card's fetched neighbours and this run's API fetches: Harness-Bench 2605.27922 runs harnesses 'under shared task environments, budgets, and evaluation protocols' (abstract), a shared budget ceiling, not matched reasoning tokens; the card paper logs the dose and does not match it. Under CL-W43-03 already: C-W43-11 (effort notch and fresh restart as control arms on self-written ARC-AGI-3 scaffolds), C-W43-12, C-W43-18 (builder vs player effort), C-W43-19 (restart vs model coverage); none touches a cross-vendor harness grid. Occupied by the card: the single-run swings and the per-run token accounting. The kill search must use the neighbours' words (reasoning effort, thinking budget, test-time compute, matched budget, compute-matched, token budget, harness configuration, scaffold ablation, restarts, retries, compaction, mediation) and quote the limitation text of 2605.27922 and of…
- **Why now:** Card paper 2026-10-23 (per-run dose, resets and harness logged; gateway topology); HAL 2510.11977 (effort non-monotonicity in print); Harness-Bench 2026-05-27 (shared budgets without matched dose). The regression is old; the flag is recorded.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-04's step 0 and import S1xF12 are zero-dollar re-analyses of released grids with pre-registered kills; C-W44-02 keeps the effort clause under one GPU-week on an open model, which answers the dollar-equivalent note |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: scaffold paper (2610.22289 sec. 9.3: further analysis needed on relative contributions), leaderboard (HAL: higher effort can reduce scores on 21 of 36 benchmarks), meta-paper (2607.12227: matched feedback and inference budgets); 2026-11-02, pressure #3: the evaluator effect is in print across three boards (B09 Artificial Analysis 52.0 vs B12 Vals 58.08 vs the official 57.88 for one model at one effort), L04 'the effort knob moves Haiku 7.2 points between adjacent levels while Claude Sonnet 5.5, Claude Opus 5.5, and Claude Fable 5.1 each varied by less than 2 points across the f… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: scaffold papers (run effort-notch and restart arms), leaderboards (separate scaffold from effort columns), harness builders (default effort setting) |
| G4 | mechanism and consequence | pass: mechanism — scaffolds inject tokens and fresh contexts, both of which the effort knob and a restart also inject; consequence — matched-spend reporting, or the scaffold keeps its organisational credit |
| G5 | durability; lab-adjacent | pass as a protocol, flagged as a number: the effort knob persists across generations; ARC-AGI-3 is a static set consumed in months |
| G6 | ownership, density, race window; position clause | open: kill search owed on C-W43-12 and C-W43-11 (limitation text of 2607.12227 and 2609.15309 unread); ownership risk — the same author owns the stack and names the question in sec. 9.3; re-open test is asking him; 2026-11-02, pressure #3 density: harness reversals are dense (P3a = 5, led by 2605.23950's 'Binding Constraint Thesis'; 2610.37255 states return = ceiling - mismatch and does not measure it on released models; 2610.32483 released 52,168 trajectories) — the pressure report's objection is that the per-lab premium 'is a weekend on public boards and will be in someone's appendix before… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-19 | Second run or second model: matched-run accumulation curves for multi-model coverage | Step 0 on the matrix (zero dollars, 2 days) then three open models times four runs at A1 (about 80 GPU-hours, about $100, 7 days); dead if the model-accumulation union beats the best model's run-accumulation union beyond the run-to-run ban… | proposed | — |
| C-W43-18 | Cross the builder's effort with the player's effort on the released self-written harnesses | Two off-diagonal cells on Opus 5 (3 harnesses x 20 games each, effort parameter swapped), about $1,700, 0 GPU-hours, 5 days including the $0 ledger regression; dead if the builder main effect is at least half the player main effect with xh… | proposed | — |
| C-W43-12 | Timed returns as the shuffled control for Stop-and-report | Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched. | killed | — |
| C-W43-11 | Effort notch and fresh restart as control arms for scaffold gains | Restart-controller arm at GPT-5.5 xhigh capped at 45.5 M normalized tokens, 3 reps x 25 games, about $1,600 of the $2,200, 0 GPU-hours, 6 days; dead if RHAE < 53.2 in all reps and truncation curves separate on B <= 9 M. | killed | — |
| C-W44-04 | Is the harness effect at fixed model an effort and restart effect? Dose-matched re-analysis of the released grid, then… | Step 0 (zero dollars, 3 days) then 2 harnesses x 95 tasks x 2 arms x 2 runs on Opus 5 through the gateway (0 GPU-hours, about 1,100 dollars, 7 days); dead if the dose and reset terms shrink the harness contrast by under 25% in at least 7 o… | proposed | — |
| C-W44-02 | Five coding harnesses at matched thinking tokens: is the fixed-model harness ranking an effort ranking | Step 0 ($0, 1 day) then step 1 (about 80 GPU-hours, $0 API, 7 days); dead if the harness ordering and at least 75% of the default spread survive at matched realised tokens beyond two three-run standard errors. | killed | — |

Also under this claim (no scorecard yet): import:2026-W44-S1xF12 (Brinson ledger — placement, conversion, fit — on the released 6,204-run cross of 2610.00917; $0, 0 GPU-h, 4 d; scorecard present; reads…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- (none pending)

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
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-03.md): killed — Gate 2B: the surprise equals the field's stated knowledge - matched-budget and effort-matched controls on scaffold gains are a published protocol with a published, benchmark-dependent answer (test-time scaling 14% of evolved-harness gains; effort gains exceeding scaffold differences on ARC-AGI-3; effort a few points aga…
- 2026-11-01 — C-W43-12 killed: killed with claim CL-W43-03 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-03.md): 2610.24649 ran a placebo-at-the-same-moments controller arm on Terminal-Bench 2.1 with no pass-rate difference; the Stop-and-report timed-return instance is a footnote; cite 2610.24649 if kept as an orphan
- 2026-11-01 — C-W43-11 killed: killed with claim CL-W43-03 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-03.md): 2607.15439 (same author, same 25 games) already reports effort gains exceeding scaffold differences; HDA supplies the pass@k restart-control template; 2610.35971 refutes the restart arm's expected direction on coding agents; a matched-token phi on 2610.22289's arms is a footnote
- 2026-11-01 — C-W44-02 killed: killed with claim CL-W43-03 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-03.md): matched-compute harness comparisons at a fixed model are in print (HDA, 2609.40303, 2610.35962, 2608.23395); a thinking-token-cap instance on a 9B model is a footnote to 2610.37255's table
- 2026-11-02 — claim open: pressure #3 (2026-11-02): one model, three numbers — B09 52.0, official 57.88, B12 58.08 on Terminal-Bench 4.0; 'a vendor harness adds 9 points over a neutral one for one lab'; B21 'Reversing the order of the observation fields leaves every optimal decision unchanged yet lowers a trained model's success from 85.0% to 19.2%'; records R09, R12, R21, L04, L13 routed here as evidence, no new claim
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): C-W44-04 and C-W44-02 (card 2610.32285 and 2610.37255's five-harness table) and import S1xF12 attached; cheapest probe moves to C-W44-04 (step 0 at $0 on the released grid); rank 2 -> 3 (CL-W43-14 moves above it on consumer breadth and four new probes)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-03`, version 6)
- probe `C-W43-19`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-18`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-12`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-11`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-04`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-02`: `data/candidates/2026-W44.jsonl`
