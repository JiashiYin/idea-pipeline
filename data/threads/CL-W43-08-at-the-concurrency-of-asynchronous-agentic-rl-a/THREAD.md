# At the concurrency of asynchronous agentic RL, a backlog-threshold rule captures as much of the hindsight-optimal prefill-decode role-switching headroom as a demand forecaster does.

`CL-W43-08` · lane **L3** · status **open** · rank 10 · position both · refreshed 2026-11-16

## Status

Open claim. The claim survived its concept-level kill search (2026-11-15); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: Gate 6 not yet established. Grade on paper: open. Next action: see First steps.

## The claim

- **Headline:** At the concurrency of asynchronous agentic RL, a backlog-threshold rule captures as much of the hindsight-optimal prefill-decode role-switching headroom as a demand forecaster does.
- **Current belief (the field's):** Prorsa 2610.16592 reports forecast error (WAPE 5.4-14.4%) for role switching without the throughput it costs and no oracle; FluidPD's abstract motivates observation-only reassignment against forecasting-free autoscaling, never against an oracle
- **If true:** Switching papers report capture ratio against the hindsight oracle; training-infra teams drop the forecaster from the recipe when the rule matches it, and stop building forecasters where the oracle headroom is under 10%
- **If false:** The forecaster captures most of a large headroom: the field gets its first oracle-normalized number for 10-second forecasting and the next question is which ignored term closes the rest

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

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
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: Prorsa (no oracle, no throughput cost of forecast error), FluidPD (observation-only rule in serving), ConServe (observation, not prediction); all papers — the issue-tracker check in verl/SGLang is owed; 2026-11-02, pressure #10: the demand the switching rule schedules is length-censored at both ends in the labs' own words — L21 DeepSeek 'shorter sequences tend to complete first and thus dominate the initial training batches [...] we support discarding early-returned short samples', L24 prime-rl 'Timed-out rollouts are now their own outcome: scored in evals, and kept out of trai… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass at one community: RL-infra teams choosing topology, rollout-engine maintainers (default switching policy), serving teams |
| G4 | mechanism and consequence | pass: mechanism — many independent trajectory renewal processes superpose into a smooth prefill-to-decode demand ratio, so headroom over a static split shrinks with concurrency and asynchrony; consequence — delete the forecaster, or report its oracle-normalized capture |
| G5 | durability; lab-adjacent | pass with a flag: system constants enter through the switch cost and the prefill/decode speeds, which are reported as the two calibration numbers |
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W43-08.md): survived-kill; gate failed none; occupied_by none; why not done: Enabling pieces landed: SGLang runtime P<->D role switching shipped (PR 28403, roadmap Q2/Q4 2026) with the load-driven policy still open; Prorsa (2026-10-12) put the forecaster and its WAPE in print without the cost of error; FluidPD (2026-10-02) put the observation rule in print without a forecaster arm; Frontier PDD support since 2026-08; the oracle belongs to none of the three groups.. Previous: open: kill search owed; 1 hit on prefill+decode+ora… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-04 | Hindsight-optimal switching bounds forecast-guided prefill-decode role switching | Replay four arms on three traces at three concurrencies, sync and async; 16 GPU-hours calibration (or 0 with Frontier), ~$60, 7 days; dead if H >= 15% and forecaster captures >= 0.8 H while hysteresis <= 0.5 H in two of three workloads at… | redesign-owed | redesign-owed ([record](../../../data/reports/2026-W46-kill-CL-W43-08.md)) |

## Kill search

### Concept level (CL-W43-08) — survived-kill (2026-11-15)
No paper compares a threshold role-switching rule against a hindsight-optimal schedule or reports a capture ratio; Prorsa owns the forecaster (static-split baseline only, zero 'oracle'/'hindsight' occurrences), FluidPD the hysteresis rule in serving (its 'oracle' is a per-window static ratio), TokenScale a correlation-only hindsight check on single-turn serving; SGLang's Q4-2026 roadmap ships the switch mechanism (PR 28403) and lists the load-driven policy as open. Proper grade; two design flags (Prorsa's W_P already includes the backlog; Prorsa's stated lever is KV capacity that grows with concurrency).
Full record: [`data/reports/2026-W46-kill-CL-W43-08.md`](../../../data/reports/2026-W46-kill-CL-W43-08.md).
**Why not done before:** Enabling pieces landed: SGLang runtime P<->D role switching shipped (PR 28403, roadmap Q2/Q4 2026) with the load-driven policy still open; Prorsa (2026-10-12) put the forecaster and its WAPE in print without the cost of error; FluidPD (2026-10-02) put the observation rule in print without a forecaster arm; Frontier PDD support since 2026-08; the oracle belongs to none of the three groups.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.16592` Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcemen… — Watch every trajectory's lifecycle stage to forecast ten seconds of prefill tokens and decode KV admissions, then flip verl/SGLang rollout engines between prefill and decode roles by a sizing rule. *Difference:* Owns the forecaster and the RL-side role switch; compares only to a hindsight-chosen static split, no oracle, no observation-only arm, no throughput cost of forecast error; its W_P already counts the backlog; its stated lever (KV capacity) grows with concurre…
- `2610.06917` FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving — Steal bounded prefill onto decode workers for bursts and reassign a running worker's role in place when two pressure indices stay past thresholds for K intervals, with a cool-down. *Difference:* The hysteresis arm shipped in serving; compared against static engines and Dynamo autoscaling, never against a forecaster or a switching oracle; its 'oracle' is a per-window static ratio; open arrivals, no RL.
- `2512.03416` TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velo… — Scale prefillers and decoders by the tokens per second each stage can absorb, and convert a profiled share of decoders into temporary prefillers during bursts. *Difference:* Observation-derived leading indicator for role conversion; hindsight check is provisioned-vs-required instance counts by correlation only, utilization-derived; single-turn serving by its own statement.
- `2609.35158` PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learni… — Refit a closed-form makespan model from telemetry each rollout step, enumerate P/D configurations under the GPU budget, and switch only when the predicted makespan improves by more than a mode-dependent threshold. *Difference:* Step-granularity model-predicted switching with hysteresis on a prediction, triggered by elastic GPU events; no oracle, no observation-only arm.
- `2606.01839` Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serv… — Make the conversation the scheduling unit so first-turn prefill goes to a prefiller and the memory-bound tail stays on one decoder. *Difference:* Removes prediction by changing the unit, not by a threshold rule; no role switching, no oracle.
*Search degraded:* ['s2', 'arxiv-api: Q8 and second id_list (Rate exceeded x2)', 'conference exports not built', 'complaint stream: verl/AReaL 422 via search endpoint; issues endpoint 403']

### C-W43-04 — redesign-owed (2026-11-15)
The whole claim survives as a measurement claim: the first oracle-normalised capture ratio for prefill-decode role switching, with headroom reported against concurrency and staleness in two regimes; the forecaster-versus-threshold contrast is only a claim if the forecast increment is isolated inside Prorsa's own rule, otherwise it is a footnote true by construction.
Full record: [`data/reports/2026-W46-kill-CL-W43-08.md`](../../../data/reports/2026-W46-kill-CL-W43-08.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched

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
- 2026-10-25 — claim open: claims (closing W43): re-ranked to 11 — no new probe this week
- 2026-11-01 — claim open: ranked 6 after the W44 kill searches: unchanged; kill search owed
- 2026-11-02 — claim open: pressure #10 (2026-11-02): L21 'discarding early-returned short samples', L24 'kept out of training batches [...] the orchestrator backfills samples that were filtered out', L23 '33 billion tokens per day [...] around 16 billion are trainable'; density P10a = 0, P10b = 1; the length-fate question is unposed and bears on this claim's demand model; records L21, L23, L24, Q09 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): no new probe; rank 11 -> 14
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 6 -> 14; ranked 14 (was 6): unchanged probe; a second control loop (C-W45-11) filed as an orphan beside it rather than widening the headline before its kill search; kill search owed since W43
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 3: L3 open; kill search owed; orphan C-W45-11 attaches after it
- 2026-11-15 — claim open: claims (W46, 2026-11-15): rank 3 -> 10; kill search owed since W43; unchanged probe
- 2026-11-15 — claim open: concept-level kill search (data/reports/2026-W46-kill-CL-W43-08.md): survived-kill — gate none; No paper compares a threshold role-switching rule against a hindsight-optimal schedule or reports a capture ratio; Prorsa owns the forecaster (static-split baseline only, zero 'oracle'/'hindsight' occurrences), FluidPD the hysteresis rule in serving (its 'oracle' is a per-window static ratio), TokenSca…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-08`, version 8)
- probe `C-W43-04`: `data/candidates/2026-W43.jsonl`; kill record `data/reports/2026-W46-kill-CL-W43-08.md`
