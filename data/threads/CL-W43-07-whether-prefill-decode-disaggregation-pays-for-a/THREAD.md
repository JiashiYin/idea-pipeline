# Whether prefill–decode disaggregation pays for agent workloads is predicted by a measurable overlap statistic, and forecast-guided role switching recovers little of the oracle's headroom.

`CL-W43-07` · lane **L3** · status **open** · position both · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Whether prefill–decode disaggregation pays for agent workloads is predicted by a measurable overlap statistic, and forecast-guided role switching recovers little of the oracle's headroom.
- **Current belief (the field's):** Prorsa 2610.x reports WAPE without the throughput that forecast error costs and no oracle; PEARL answers by profiling, not by a statistic
- **If true:** Serving teams compute the statistic from traces before choosing a topology; switching papers report oracle-normalized capture
- **If false:** Switching captures most of the oracle headroom — forecasting is the right investment

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** Prorsa itself: Section 5.5 and Appendix C report WAPE but never the throughput that forecast error costs, and no oracle is reported (card, weakest_component); FluidPD's abstract motivates observation-only role reassignment against forecasting-free autoscaling but never against an oracle. Who pays: every team running asynchronous agentic RL on verl, ROLL, AReaL or slime that must decide whether PD disaggregation with role switching is worth 6.4K lines of scheduler code.
- **Impact ceiling:** **floor**: A released replay harness and the first oracle-normalized capture ratio for forecast-guided switching on one public coding trace. Requires only the simulator and the .traj parser. p = 0.7 (judgment).; **middle**: The scaling result: switching headroom versus concurrency and staleness across three workloads, with the hysteresis-equals-forecaster finding; cited by rollout-engine papers as the reason to switch (or not) at a given scale. Requires the three traces and Frontier-level calibration. p = 0.35 (judgment).; **ceiling**: The rule is adopted as a pre-deployment check in a framework's docs (verl or SGLang router) and the hysteresis rule ships as the default role-switching policy; Prorsa/PEARL follow-ups report capture ratio against the oracle. Requires one framework maintainer to care and a real-trace confirmation. p = 0.1 (judgment).
- **Relevance:** L3 routes (Lloyd / Netravali / Tri Dao, systems): direct, a measurement of a rollout-engine design decision. Industry: RL infra teams choosing topology; serving teams get the RL analogue of ConServe/FluidPD. Jacob's edge: stochastic processes (superposition of renewal processes, Palm-Khintchine) supply the mechanism; computer engineering supplies the scheduling model. Zero relevance to L1, L2 (no training signal is touched), L4, L5.
- **Kill probe:** Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at >= 1024 async.
- **Density and ownership:** —
- **Why now:** Prorsa 2026-10-12 (first WAPE without cost, no oracle); Frontier 2026-05-20 (validated simulator with RL rollout support, released); FluidPD 2026-10-02 (observation-only rule exists in serving); SWE-agent .traj with execution_time public since 2025.
- **Register, and what it is not:** Measurement with a definitive comparison (four arms, one trace, oracle-normalized). It is not a new scheduler, not a new forecaster, and not Prorsa on a new benchmark; the hysteresis arm is a control, not the contribution.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-04 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-04 | Hindsight-optimal switching bounds forecast-guided prefill-decode role switching | Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of  | proposed | — |
| C-W43-05 | A prefill-decode overlap statistic predicts when disaggregation pays | Four workloads x two topologies x 3 repeats on one 8-GPU node, ~80 GPU-hours, ~$250, 7 days; dead if either off-diagonal cell breaks the predicted sign or Omega is not monotone with the speedup. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-04** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at >= 1024 async.
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

- claim record: `data/claims/claims.jsonl` (id CL-W43-07)
- probe `C-W43-04`: `data/candidates/*.jsonl`
- probe `C-W43-05`: `data/candidates/*.jsonl`
