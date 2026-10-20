# At the concurrency of asynchronous agentic RL, a backlog-threshold rule captures as much of the hindsight-optimal prefill-decode role-switching headroom as a demand forecaster does.

`CL-W43-08` · lane **L3** · status **open** · rank 8 · position both · refreshed 2026-10-20

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established. Grade on paper: open. Next action: see First steps.

## The claim

- **Headline:** At the concurrency of asynchronous agentic RL, a backlog-threshold rule captures as much of the hindsight-optimal prefill-decode role-switching headroom as a demand forecaster does.
- **Current belief (the field's):** Prorsa 2610.16592 reports forecast error (WAPE 5.4-14.4%) for role switching without the throughput it costs and no oracle; FluidPD's abstract motivates observation-only reassignment against forecasting-free autoscaling, never against an oracle
- **If true:** Switching papers report capture ratio against the hindsight oracle; training-infra teams drop the forecaster from the recipe when the rule matches it, and stop building forecasters where the oracle headroom is under 10%
- **If false:** The forecaster captures most of a large headroom: the field gets its first oracle-normalized number for 10-second forecasting and the next question is which ignored term closes the rest

## Scorecard (from the cheapest probe's record)

- **Target value:** Prorsa itself: Section 5.5 and Appendix C report WAPE but never the throughput that forecast error costs, and no oracle is reported (card, weakest_component); FluidPD's abstract motivates observation-only role reassignment against forecasting-free autoscaling but never against an oracle. Who pays: every team running asynchronous agentic RL on verl, ROLL, AReaL or slime that must decide whether PD disaggregation with role switching is worth 6.4K lines of scheduler code.
- **Impact ceiling:** **floor**: A released replay harness and the first oracle-normalized capture ratio for forecast-guided switching on one public coding trace. Requires only the simulator and the .traj parser. p = 0.7 (judgment).; **middle**: The scaling result: switching headroom versus concurrency and staleness across three workloads, with the hysteresis-equals-forecaster finding; cited by rollout-engine papers as the reason to switch (or not) at a given scale. Requires the three traces and Frontier-level calibration. p = 0.35 (judgment).; **ceiling**: The rule is adopted as a pre-deployment check in a framework's docs (verl or SGLang router) and the hysteresis rule ships as the default role-switching policy; Prorsa/PEARL follow-ups report capture ratio against the oracle. Requires one framework maintainer to care and a real-trace confirmation. p = 0.1 (judgment).
- **Relevance:** L3 routes (Lloyd / Netravali / Tri Dao, systems): direct, a measurement of a rollout-engine design decision. Industry: RL infra teams choosing topology; serving teams get the RL analogue of ConServe/FluidPD. Jacob's edge: stochastic processes (superposition of renewal processes, Palm-Khintchine) supply the mechanism; computer engineering supplies the scheduling model. Zero relevance to L1, L2 (no training signal is touched), L4, L5.
- **Kill probe:** Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at >= 1024 async.
- **Density and ownership:** arXiv API 2026-10-19: prefill+decode+(oracle|hindsight|offline optimal)+(trace|replay|simulat) = 1 hit (NetKV 2606.03910, unrelated: decode-instance selection); prefill+(disaggregation|disaggregated)+(RL|rollout|post-training) = 7 hits, closest Prorsa and PEARL 2609.35158 (runtime PD mode/ratio selection with cost-aware switching, no oracle); (polling|switching cost|setup time|hysteresis|threshold policy)+(prefill|LLM serving) = 3 hits, none relevant. Occupied: Prorsa owns the forecaster and Eq. 1; FluidPD 2610.06917 owns observation-only in-place role reassignment in serving (pressure indices); ConServe 2606.01839 owns 'observation, not prediction' at conversation level in serving; Frontier 2605.21312 owns the simulator. No one owns the oracle bound or the capture ratio. Pre-window precedents to name in the kill search: Hofri & Ross 1987 (two queues, setup times, threshold optimality);…
- **Why now:** Prorsa 2026-10-12 (first WAPE without cost, no oracle); Frontier 2026-05-20 (validated simulator with RL rollout support, released); FluidPD 2026-10-02 (observation-only rule exists in serving); SWE-agent .traj with execution_time public since 2025.
- **Register, and what it is not:** Measurement with a definitive comparison (four arms, one trace, oracle-normalized). It is not a new scheduler, not a new forecaster, and not Prorsa on a new benchmark; the hysteresis arm is a control, not the contribution.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-04 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: Prorsa (no oracle, no throughput cost of forecast error), FluidPD (observation-only rule in serving), ConServe (observation, not prediction); all papers — the issue-tracker check in verl/SGLang is owed |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass at one community: RL-infra teams choosing topology, rollout-engine maintainers (default switching policy), serving teams |
| G4 | mechanism and consequence | pass: mechanism — many independent trajectory renewal processes superpose into a smooth prefill-to-decode demand ratio, so headroom over a static split shrinks with concurrency and asynchrony; consequence — delete the forecaster, or report its oracle-normalized capture |
| G5 | durability; lab-adjacent | pass with a flag: system constants enter through the switch cost and the prefill/decode speeds, which are reported as the two calibration numbers |
| G6 | ownership, density, race window; position clause | open: kill search owed; 1 hit on prefill+decode+oracle/hindsight; pre-window precedents Hofri and Ross 1987 (two queues with setup times, threshold optimality), DistServe and Splitwise 2024 |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-04 | Hindsight-optimal switching bounds forecast-guided prefill-decode role switching | Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-04** (Sunday run), or run `/kill C-W43-04` in a session.
2. If it survives: `/redteam C-W43-04`, then the probe as pre-registered — Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at >= 1024 async.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim open: new claim, split from CL-W43-07 (one sentence per headline); probe C-W43-04

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-08`, version 1)
- probe `C-W43-04`: `data/candidates/2026-W43.jsonl`
