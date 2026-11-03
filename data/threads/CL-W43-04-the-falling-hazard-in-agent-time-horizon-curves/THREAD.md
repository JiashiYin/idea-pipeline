# The falling hazard in agent time-horizon curves is between-task frailty, not within-task degradation: hold the task fixed and the per-minute hazard is flat.

`CL-W43-04` · lane **L1** · status **killed** · rank None · position solo · refreshed 2026-11-03

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established; Gate 1 blocked on paperwork (no scorecard on X-2026-W42-S7F9); testbed frozen (METR stopped). Grade on paper: open; headline rewritten to the sentence its probe tests. Next action: see First steps.

## The claim

- **Headline:** The falling hazard in agent time-horizon curves is between-task frailty, not within-task degradation: hold the task fixed and the per-minute hazard is flat.
- **Current belief (the field's):** Hamilton (Jan 2026) fits a pooled Weibull with shape about 0.6 for frontier agents and reads it as the agents' hazard; Ord 2505.05115 reads a half-life; METR's own logistic-in-log-time curve is the sigma^2 = 1 gamma-frailty curve without being named as one (X-2026-W42-S7F9, derivation in the seed record)
- **If true:** Horizon producers publish the frailty variance or the within-task run agreement beside every 50% and 80% horizon and label the 80% horizon a share of tasks within reach; forecasters use k_cond for single-task tails and sigma^2 for reach; pass^k reporters replace one per-step reliability with a per-task distribution
- **If false:** The within-task hazard falls too (k_cond well below 1): agents do degrade along a task, which makes the horizon curve a property of agents after all and makes the step-clock hazard shape (S7xF9) the next question

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** —
- **Impact ceiling:** —
- **Relevance:** —
- **Kill probe:** —
- **Density and ownership:** —
- **Why now:** —
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe X-2026-W42-S7F9 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: sigma^2 and k_cond are identifiable from METR's released per-run file (27,119 runs, 4-8 runs per task); pre-registered surprise — expected k_cond in [0.8, 1.2] and sigma^2 above 0.3 for most agents, field assumes the pooled shape is an agent property, the ruler changes nothing if k_cond reproduces the pooled 0.6 within tasks |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: horizon producers and auditors, forecasters of high-reliability tails, pass^k and retry-model reporters |
| G4 | mechanism and consequence | pass: mechanism — a pooled hazard falls at the rate of the survivors' hazard variance (Vaupel, Manton, Stallard 1979), so unequal fixed task difficulty produces a falling curve from flat units; consequence — the 80% horizon is read as reach, not reliability, or the within-task shape is confirmed and horizon extrapolation keeps its form |
| G5 | durability; lab-adjacent | pass as a ruler; flag strengthened 2026-11-02: METR's tracker has stopped (B16: 'This page is no longer actively updated. LAST UPDATED September 8, 2026 [...] Measurements above 16 hrs are unreliable with our current task suite'; last model 2026-04-07), so the probe's dataset is frozen and the within-task test needs a second pool with repeated runs — Terminal-Bench 4.0's per-task expert-time annotations (median 4 hours, 35 entries x 330 trials) are the only public one |
| G6 | ownership, density, race window; position clause | open: kill search owed; Ord reports Hamilton found the frailty and Weibull fits similar on the pooled curve (seed record), which is the sentence to quote; density on Weibull and agents = 13 hits, frailty decomposition from repeated runs found in no fetched source |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| X-2026-W42-S7F9 | X-2026-W42-S7F9 (frailty refit of METR-Horizon-v1.1 runs; $0, 3 d; no scorecard) | — | — | not a candidate record (seed or import) |

Also under this claim (no scorecard yet): import:2026-W43-S7xF9 (step-clock hazard on tau-bench; ~$300-600 + 60 GPU-h; no scorecard)

## Kill search

### Concept level (CL-W43-04) — killed (2026-11-01)
Gate 6 occupied: the between-task frailty decomposition on METR's repeated runs is in print (Moss 2026-02-13; Nguyen & Fithian 2610.12466, 2026-10-08) including the claim's if_true consequence (typical vs marginal 80% horizon); the within-task half has no clock on horizon data (Gate 0) and on a step clock equals the field's stated knowledge (2609.01660, 2609.19113) against a published rising-hazard mechanism (2509.09677) (Gate 2B).
Full record: [`data/reports/2026-W44-kill-CL-W43-04.md`](../../../data/reports/2026-W44-kill-CL-W43-04.md).
**Occupied by:** 2610.12466 (Nguyen & Fithian, 2026-10-08) with Moss (LessWrong, 2026-02-13) on the consequence
**Why not done before:** no reason found for the hazard-vocabulary version — the statisticians (2610.12466, Moss) did the frailty decomposition in IRT words and the forecasters (Ord, Hamilton) read the pooled curve in survival words; the two literatures do not cite each other. The decomposition itself is done.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.12466` On the estimation and validity of AI time horizons — a statistical look at the METR plot… — Refit METR's 228 tasks x 26 AIs with an explanatory IRT model: per-task difficulty = monotone spline of log human time + task random effect + family random effect (variances are splines in log human time) + beta-binomial correlation between repeated runs, fit… *Difference:* none — occupied: the between-task frailty model on the same repeated runs; s(x)^2 = sigma(x)^2 + tau(x)^2 is the probe's sigma^2 by task length; '60% predicted vs 83% observed unanimous run vectors' is the probe's premise. Not done: hazard/Weibull translation…
- `web:lesswrong.com/posts/sBEzomgnYJmYHki9T (Moss, 2026-02-13)` (Updated) METR's data can't distinguish between trajectories (and 80% horizons are an ord… — 2PL IRT in Stan with per-task random difficulty around a log-human-time mean (1 SD ~ 4.7x in time); 'typical' vs 'marginal' 80% horizons differ by an order of magnitude (21.1 min vs 0.8 min, Claude 3.7 Sonnet). *Difference:* none on the consequence — the claim's if_true ('80% horizon is a share of tasks within reach') is Moss's marginal horizon. Not done: run-level overdispersion, hazard reading; human times treated as known.
- `web:metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results (Barry)` Impact of modelling assumptions on time horizon results — Thirteen refits of the horizon (shared-slope logistic, Weibull survival citing Hamilton, beta-binomial run correlation, Cauchy, LOESS, splines, isotonic) plus SIMEX for task-length noise; leave-one-family-out CV. *Difference:* Owner's sensitivity study; Weibull, logistic, LOESS 'all did similarly well'; the frailty term is named as unexplored ('Allowing task difficulty for LLMs to differ from baseliner time').
- `web:metr.org/notes/2026-01-22-time-horizon-limitations (Kwa)` Clarifying limitations of time horizon — States that 20%/80% horizons are not independent of the 50% estimate under the two-parameter logistic and that 99% horizons need ~300 tasks per time bucket. *Difference:* Owner limitation text; no heterogeneity, no hazard.
- `2608.00355` CurveShift: Is Agent Progress Scalar? — Rasch model with fixed per-task difficulty on METR data; rising ability reproduces the apparent shift toward hard tasks. *Difference:* Fixed task difficulty, no run-level term, no hazard reading.
**Narrowest surviving headline:** none as a claim; residue is a one-paragraph translation note — Hamilton's Weibull k≈0.6 is the pooled shape that 2610.12466's fitted spread s(x) produces from units with k=1, and the 99%-horizon disagreement Ord calls undecidable (Weibull vs log-logistic) is decided by rho and s(x), not by the link — a comment under Ord's 2026-02-04 post, recorded as a footnote
*Search degraded:* ['s2', "web: gushamilton.github.io blocked (provenance) — seed record's 2026-10-18 read used", 'arxiv: no HTML for 2505.05115 (abstract only)']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Promote? This is the cheapest headline in the portfolio ($0, 3 days) and the kill search decides it; part of the proposed L1 'noise floor' program (PROGRAM-L1-evaluation-floors.md).

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: headline rewritten: the 10-19 sentence (reliability unchanged across generations at fixed difficulty) was not what X-2026-W42-S7F9 tests; the probe tests frailty versus within-task hazard; import S7xF9 attached as the step-clock probe; scorecard owed on both seeds before any kill search
- 2026-10-25 — claim open: claims (closing W43): re-ranked to 9 — no new probe, Gate 6 still not established; scorecards still owed on import probes
- 2026-10-30 — claim open: nominated as a core-ML champion candidate (Jacob asked for a champion outside L5); kill search requested ahead of rank order; see PROGRAM-L1-evaluation-floors.md
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-04.md): killed — Gate 6 occupied: the between-task frailty decomposition on METR's repeated runs is in print (Moss 2026-02-13; Nguyen & Fithian 2610.12466, 2026-10-08) including the claim's if_true consequence (typical vs marginal 80% horizon); the within-task half has no clock on horizon data (Gate 0) and on a step clock equals the fie…
- 2026-11-02 — claim open: pressure #2 (2026-11-02): the horizon tracker is dead — B16 'This page is no longer actively updated [...] Measurements above 16 hrs are unreliable with our current task suite', last entry release_date 2026-04-07; the frailty test moves to the Terminal-Bench 4.0 pool (expert-time annotations, 330 trials per entry); records R16 and R04 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): no new probe; scorecard on X-2026-W42-S7F9 still owed before the requested kill search can run; rank 9 -> 10 (two new L1 claims with scorecarded probes enter above it)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-04`, version 6)
- `X-2026-W42-S7F9`: seed or import record (no candidate yet)
