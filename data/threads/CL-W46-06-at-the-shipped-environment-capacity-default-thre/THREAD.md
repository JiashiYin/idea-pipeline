# At the shipped environment-capacity default (three tool slots on MCP-Atlas), the batch-makespan tail of agent rollouts is work, not a scheduling loss: in trace replay the makespan bound no dispatch order can beat — total slot work over slots, or the longest chain — sits within 10% of first-come-first-served, so reordering tool jobs cannot remove more than a tenth of the makespan.

`CL-W46-06` · lane **L3** · status **open** · rank 6 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed); Gate 2B flagged (the expected reading is plausible from the card paper's own small CAAS gain; the bound, the curve and the shed-versus-reorder price are the content). Next action: see First steps.

## The claim

- **Headline:** At the shipped environment-capacity default (three tool slots on MCP-Atlas), the batch-makespan tail of agent rollouts is work, not a scheduling loss: in trace replay the makespan bound no dispatch order can beat — total slot work over slots, or the longest chain — sits within 10% of first-come-first-served, so reordering tool jobs cannot remove more than a tenth of the makespan.
- **Current belief (the field's):** 2611.16661 (card, full text), sec. 4.2: 'With future trajectory lengths unknown, CAAS uses completed inference turns as a proxy for potentially long trajectories'; sec. 5.3: 'Although CAAS reaches 95% completion later, it finishes the batch earlier'; sec. 5.4: 'The final 25 tasks under Opt-CAAS average 27.9 and 15.6 turns ... compared with 10.1 and 7.9 under the baseline' — the tail is a scheduling target, compared with FCFS only, never with a bound, although the replay harness holds 'recorded environment responses and durations' (sec. 5.1); derived from its Table 3 (not stated by the paper): the last 5% of tasks occupy 40% and 27% of the makespan after capacity separation. 2609.10964 (abstract fetched 2026-11-16): under contention 'once submitted, those turns can no longer be reordered by the workflow-level policy, increasing tail latency'. Seer 2511.14617 (abstract fetched): rollout 'suffers from substantial long-tail latency and poor resource utilization due to inherent workload imbalance'. The tail is read as a loss that scheduling recovers.
- **If true:** The last-5% tail share is a work-distribution statistic, not a scheduling KPI: scheduling papers report $T_{\mathrm{LB}}$ and the headroom $H$ beside every makespan gain (as the GPU-side tail literature already reports oracle-normalized throughput, TIDE 2611.17924); harness owners size $C_E$ against the batch ($N$, $\bar g / \bar\tau$) instead of adding dispatch rules; RL rollout engines treat long chains by shedding or carrying them over (what the labs already do under length censoring, pressure #10) and get a number for what reordering would have bought instead; the next environment-side scheduler is pitched at the $C_E / N$ regime where the headroom exists.
- **If false:** If $H \geq 0.25$ at three slots: the environment-side tail is the under-exploited scheduling lever and the field gets its first oracle bound for it; the pre-registered alternative is that CAAS captures under 0.3 of the achievable gain, which puts a longest-chain-first prior from the per-task recurrence (card sec. 5.4) on the recipe table; the residue is the shed-versus-reorder price on one trace either way.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.16661's own replay design ('recorded environment responses and durations', sec. 5.1) that holds the data for the bound and does not compute it; its derived tail share; its statement that MCP-Atlas and tau-bench harnesses use one gate; 2609.10964's P95 reduction with no bound; pressure #10 (2026-11-02): DeepSeek 'discarding early-returned short samples', prime-rl 'Timed-out rollouts ... kept out of training batches', Mistral 16 of 33 billion tokens trainable — the labs shed the tail and the lane has no number for what reordering would have bought instead. Who pays: harness owners choosing $C_E$ defaults (MCP-Atlas, tau-bench, Terminal-Bench runners), RL rollout engines with sandbox fleets (ARL-Tangram's action-level scheduling), benchmark operators paying for batch runs, and the authors of the next tail-scheduling rule.
- **Impact ceiling:** **floor**: The first $H$-versus-$C_E$ curve for agent batches on public traces with the CAAS and LRCP capture ratios, cited by the card paper's v2 and the next scheduling paper. Requires steps 0-1. Judgment 0.6.; **middle**: A reporting rule (bound and headroom beside every makespan gain) adopted by one harness or rollout-engine paper, and a recommended $C_E$ sizing rule ($C_E$ against $N$ and $\bar g / \bar\tau$) in one harness's docs. Requires step 2 on MCP-Atlas-shaped traces. Judgment 0.3.; **ceiling**: The shed-versus-reorder price settles how RL rollout engines treat long trajectories (truncate, carry over as partial rollouts, or reorder) with the environment-side bound as the unit; adopted as a pre-deployment check in a framework. Requires two more workloads and a live confirmation. Judgment 0.1.
- **Relevance:** Systems route (Lloyd, Netravali, Tri Dao): direct — a definitive comparison with an oracle bound on a rollout-engine design decision. Narasimhan route: indirect (rollout cost of agent RL). Industry: direct for anyone running agent batches against capacity-limited services. L1: indirect (benchmark run cost set by harness defaults). L2, L4, L5: zero. Jacob's edge: parallel-machine makespan bounds, list scheduling and the critical-path identity are operations research he can check by hand; the discrete-event replay is computer engineering; physics zero.
- **Kill probe:** Steps 0-1: $0, 0 GPU-h, 5 days on public traces; step 2 about 30-50 GPU-h, 4 days; dead if $H \geq 0.25$ at $C_E = 3$ on MCP-Atlas-shaped traces (lower bound above 0.15), uninformative if the hindsight list schedule exceeds the bound by more than 15%.
- **Density and ownership:** Environment-side scheduling of agent batches against a bound: 11 API hits for (makespan OR critical path OR lower bound OR oracle OR hindsight) x (tool execution OR sandbox OR environment) x agent x scheduling (2026-11-16, by date); none computes a bound — 2611.16661 (FCFS only), PASTE 2603.18897 (speculative tool execution for one task's latency; 'tool latency exposed on the task critical path'), AgentPerfBench 2609.34683 (a benchmark suite), MO-SAIC 2611.13740 (multi-objective workflow scheduling with HEFT, cloud cost). Tail-of-rollout literature: 194 hits for (makespan OR long-tail OR straggler) x (rollout OR agentic OR tool calls) x LLM, of which the on-target ones are GPU-side generation-length tails — Seer 2511.14617, APRIL 2509.18521, RhymeRL 2508.18588, TailSieve 2608.22788, RollVerify 2610.09914, ASP 2611.08864, TIDE 2611.17924 ('97% of optimal throughput' is an oracle-normaliz…
- **Why now:** 2611.16661 2026-11-12 (the data for the bound, uncomputed); 2609.10964 2026-09-10 (a second rule without a bound); TIDE 2026-11-13 (the oracle-normalized register in the neighbouring GPU tail); pressure #10 2026-11-02 (the labs shed the tail; nobody prices reordering against shedding).
- **Register, and what it is not:** Measurement with a definitive comparison (five arms against a bound on one trace) and a sizing consequence ($C_E$ against $N$; shed or reorder). It is not a new scheduler, not CAAS on a new benchmark, not a verdict on the card paper's 65% (which is capacity separation, not CAAS), and not a GPU-side tail paper: the resource is the environment slot.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper. Premise numbers fetched and dated with their verbs: live MCP-Atlas makespan 163.0 and 128.5 min with $L_5$ 66.0 and 35.3 min (measured, Table 3, three-run means with no spread); CAAS 1.9-3.5% makespan and 19-21% $L_5$ in replay (simulated with real inference, sec. 5.3); the 27-40% tail share is derived by the card from Table 3, not stated by the paper. Conditioning set: recorded $\tau$ and $g$ held fixed under every order and slot count (the paper's own replay protocol, sec. 5.1: 'Stage dependencies and environment durations remain fixed'), so $H$ is a property of the (trace, $… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: steps 0-1 cost $0 and no GPU on public traces; the shipped-default number needs MCP-Atlas-shaped traces (the authors' records, or step 2 at about 30-50 GPU-h); kill written: $H \geq 0.25$ at $C_E = 3$ with the bootstrap lower bound above 0.15. Both outcomes informative: the first environment-side oracle bound either way. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route A, a stated pressure point in two source types: (i) papers — 2611.16661 ships a dispatch rule for the tail and compares it with FCFS only while holding the data for the bound; 2609.10964 ships a second tail rule with no bound (HTML read); (ii) lab disclosures — pressure #10 (2026-11-02): DeepSeek 'discarding early-returned short samples', prime-rl 'Timed-out rollouts ... kept out of training batches', Mistral 16 of 33 billion tokens trainable — the labs shed the tail without a number for the alternative. Route B flag: the expected reading (ordering is a dead lever at three saturated slo… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Pass at one community with adjacent consumers: harness owners choosing $C_E$ defaults (MCP-Atlas runner: five; tau-bench and MCP-Atlas: one gate — size the slots, do not add a rule); rollout-engine and RL-infra teams (shed or carry over long chains; report the bound); scheduling-paper authors (report $H$ beside gains); benchmark operators paying for batch runs (cost set by $W / C_E$ and $\max_k \mathrm{CP}_k$). Register test: a systems measurement that changes a reported quantity and a default. Proper-shaped. |
| G4 | mechanism and consequence | Mechanism written: with $N \gg C_E$ chains admitted, the slots are busy whenever at least $C_E$ chains hold a ready tool job; idle slot-time appears only when fewer chains remain than about $C_E (1 + \bar\tau / \bar g)$, a few chains' alternation at the end, small against a 163-minute batch; the 27-40% tail is then the long chains' remaining tool jobs passing through three slots at full utilization. As $C_E$ grows toward $N$, $W / C_E$ falls below $\max_k \mathrm{CP}_k$ and the bound becomes the longest chain, which only an order that starts long chains early can approach — the regime where L… |
| G5 | durability; lab-adjacent | Pass with a flag: the bound and the $H$-versus-$C_E / N$ curve apply to any batch of chains on any slot pool and survive model and benchmark refreshes; the MCP-Atlas number expires with the harness default. Lab-adjacent: systems labs publish measurements and designs of this kind; frontier infra teams do not publish the bound. Race flag: the card paper's authors can compute the bound on their replay traces in a day. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17). Role words in the neighbours' vocabulary: batch makespan, job completion time, flow time, tail latency, P95, long-tail rollout, straggler, environment capacity, tool concurrency, sandbox pool, slot, action completion time, critical path, list scheduling, LPT, HEFT, lower bound, hindsight optimal, oracle, capture ratio, release scheduling, eager release, committed work, length censoring, partial rollout, over-provisioning; queueing words from the CL-W45-05 lesson (busy period, renewal, FIFO orbit). W46 counts (2026-11-16, by date): environm… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-15 | The bound no dispatch order can beat: how much of the environment-capacity tail of an agent batch is work, at the shipp… | Steps 0-1: $0, 0 GPU-h, 5 days on public traces; step 2 about 30-50 GPU-h, 4 days; dead if $H \geq 0.25$ at $C_E = 3$ on MCP-Atlas-shaped traces (lower bound above 0.15), uninformative if the hindsight list schedule exceeds the bound by mo… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-15** (Sunday run), or run `/kill C-W46-15` in a session.
2. If it survives: `/redteam C-W46-15`, then the probe as pre-registered — Steps 0-1: $0, 0 GPU-h, 5 days on public traces; step 2 about 30-50 GPU-h, 4 days; dead if $H \geq 0.25$ at $C_E = 3$ on MCP-Atlas-shaped traces (lower bound above 0.15), uninformative if the hindsight list schedule exceeds the bound by more than 15%.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L3 lane sentence plus card 2611.16661's replay-harness sentence); probe C-W46-15 (cheapest, $0 for the curve, about 40 GPU-h for the shipped-default number); filed as a new claim beside CL-W43-08, not under it (different resource, decision and objective; C-W45-11 precedent); concept-level kill search owed (rule 17); Gate 2B flagged at filing
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 6: born W46: $0 replay probe on public traces; consumers are every rollout-harness builder; headline hinges on a bound no scheduling paper reports; concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-06`, version 1)
- probe `C-W46-15`: `data/candidates/2026-W46.jsonl`
