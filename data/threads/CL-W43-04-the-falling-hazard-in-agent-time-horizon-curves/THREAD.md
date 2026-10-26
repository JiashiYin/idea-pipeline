# The falling hazard in agent time-horizon curves is between-task frailty, not within-task degradation: hold the task fixed and the per-minute hazard is flat.

`CL-W43-04` · lane **L1** · status **open** · rank 9 · position solo · refreshed 2026-10-26

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; Gate 1 blocked on paperwork (no scorecard on the probe). Grade on paper: open; headline rewritten to the sentence its probe tests. Next action: see First steps.

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
| G5 | durability; lab-adjacent | pass as a ruler; flagged: METR's suite is retired (checklist 2026-10-10), so the ruler needs a second suite with repeated runs to stay live |
| G6 | ownership, density, race window; position clause | open: kill search owed; Ord reports Hamilton found the frailty and Weibull fits similar on the pooled curve (seed record), which is the sentence to quote; density on Weibull and agents = 13 hits, frailty decomposition from repeated runs found in no fetched source |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| X-2026-W42-S7F9 | X-2026-W42-S7F9 (frailty refit of METR-Horizon-v1.1 runs; $0, 3 d; no scorecard) | — | — | not a candidate record (seed or import) |

Also under this claim (no scorecard yet): import:2026-W43-S7xF9 (step-clock hazard on tau-bench; ~$300-600 + 60 GPU-h; no scorecard)

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **X-2026-W42-S7F9** (Sunday run), or run `/kill X-2026-W42-S7F9` in a session.
2. If it survives: `/redteam X-2026-W42-S7F9`, then the probe as pre-registered — —
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
- 2026-10-20 — claim open: headline rewritten: the 10-19 sentence (reliability unchanged across generations at fixed difficulty) was not what X-2026-W42-S7F9 tests; the probe tests frailty versus within-task hazard; import S7xF9 attached as the step-clock probe; scorecard owed on both seeds before any kill search
- 2026-10-25 — claim open: claims (closing W43): re-ranked to 9 — no new probe, Gate 6 still not established; scorecards still owed on import probes

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-04`, version 3)
- `X-2026-W42-S7F9`: seed or import record (no candidate yet)
