# Whether prefill-decode disaggregation pays for an agent workload is set by the measured temporal overlap of prefill with decode, not by turn count.

`CL-W43-07` · lane **L3** · status **open** · rank 7 · position both · refreshed 2026-10-23

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established. Grade on paper: open. Next action: see First steps.

## The claim

- **Headline:** Whether prefill-decode disaggregation pays for an agent workload is set by the measured temporal overlap of prefill with decode, not by turn count.
- **Current belief (the field's):** Prorsa 2610.x reports WAPE without the throughput that forecast error costs and no oracle; PEARL answers by profiling, not by a statistic
- **If true:** Serving and RL-infra teams compute the overlap statistic from traces before choosing a topology; rollout-engine docs carry it as the pre-deployment check
- **If false:** Turn count or workload type predicts the sign as well as the overlap does, and the ruler is a service; the 8-GPU reproduction of Prorsa's reversal stays a footnote

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Prorsa Section 5.2 (math slower than colocation in most settings, no rule given; card complaint #1); PEARL abstract: 'the choice between colocation and disaggregation and the optimal PD ratio vary with the workload'; 2605.28302 poses 'when does each level actually pay off' for attention-FFN disaggregation. Who pays: every team provisioning rollout engines for RLVR or agentic RL, and SGLang/verl maintainers writing deployment guidance.
- **Impact ceiling:** **floor**: An 8-GPU reproduction of Prorsa's sign reversal with the overlap mechanism isolated from turn count on four workloads, plus the Omega script over SWE-agent logs. Requires the node and the fake-tool replayer. p = 0.6 (judgment).; **middle**: Omega adopted as the pre-deployment check in one framework's docs and used to show that asynchronous single-turn RLVR gains from disaggregation. Requires the async single-turn cell to come out positive and a maintainer to pick it up. p = 0.25 (judgment).; **ceiling**: Omega becomes the standard workload descriptor that rollout-engine papers report alongside turn count and context length, and PD-switching papers evaluate against it. Requires confirmation at cluster scale by a lab. p = 0.08 (judgment).
- **Relevance:** L3 routes (Lloyd / Netravali / Tri Dao): direct, a ruler for a rollout-engine decision with a systems experiment. Industry: RL infra and serving teams. Jacob's edge: computer engineering (DP-attention barrier, interconnect cost model) and the Little's-law style time-integral statistic. Zero relevance to L1, L2, L4, L5.
- **Kill probe:** Four workloads x two topologies x 3 repeats on one 8-GPU node, ~80 GPU-hours, ~$250, 7 days; dead if either off-diagonal cell breaks the predicted sign or Omega is not monotone with the speedup.
- **Density and ownership:** arXiv API 2026-10-19: prefill+decode+(interference|colocat)+(agent|multi-turn|rollout) = 12 hits (Prorsa, AInfer-PD 2609.00993, PPD 2603.13358 'not all prefills are equal', P-PAS 2608.15171 prefill-decode interference crossover in vLLM, PackServe 2609.33224 white-box interference latency models, 2609.34663 tool re-arrival prefill interference on NPUs); prefill+(disaggregation|disaggregated)+(when|whether|break-even|cost model|analytical) = 35 hits, closest 2605.28302 (AFD design space, 'when does each level pay off', by simulation) and 2601.21351 (one trace statistic theta governs AFD provisioning, nonparametric estimator from traces: the same ruler shape for a different decision); (data parallel attention|DP attention)+(prefill|MoE)+(idle|straggler|imbalance) = 0 hits, so the DP-attention idle mechanism is Prorsa's alone in abstracts. Occupied: Prorsa owns the idle-ratio characterizati…
- **Why now:** Prorsa 2026-10-12 (the reversal with numbers and the named mechanism); PEARL 2026-09-28 (the question posed and answered by profiling, not by a statistic); SGLang PD disaggregation single-node since 2025; SWE-agent .traj execution_time public.
- **Register, and what it is not:** Ruler (a workload statistic with a sign prediction) plus a small systems experiment. It is not a scheduler, not a switching policy, not a simulator paper, and not a reproduction of Prorsa at scale.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-05 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass: route A — Prorsa (paper: sign reversal math versus coding with the idle-ratio mechanism), PEARL (runtime selection by profiling), FluidPD and ConServe (serving-side observation rules); route B — the overlap statistic Omega with a pre-registered surprise (expected: Omega orders all four cells; field assumes workload type) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass at one community: RL-infra teams, agentic-serving teams, rollout-engine maintainers |
| G4 | mechanism and consequence | pass: mechanism — colocation hurts decode only during the fraction of decode time that overlaps a prefill; consequence — a threshold on Omega decides the topology before the second set of GPUs is bought |
| G5 | durability; lab-adjacent | pass with a flag: the statistic is durable as a definition, its threshold is hardware- and engine-specific; lab-adjacent (systems labs publish measurements) |
| G6 | ownership, density, race window; position clause | open: kill search owed; closest ruler shape is 2601.21351 (one trace statistic theta for AFD provisioning); limitation sections of PEARL and 2605.28302 unread |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-05 | A prefill-decode overlap statistic predicts when disaggregation pays | Four workloads x two topologies x 3 repeats on one 8-GPU node, ~80 GPU-hours, ~$250, 7 days; dead if either off-diagonal cell breaks the predicted sign or Omega is not monotone with the speedup. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-05** (Sunday run), or run `/kill C-W43-05` in a session.
2. If it survives: `/redteam C-W43-05`, then the probe as pre-registered — Four workloads x two topologies x 3 repeats on one 8-GPU node, ~80 GPU-hours, ~$250, 7 days; dead if either off-diagonal cell breaks the predicted sign or Omega is not monotone with the speedup.
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
- 2026-10-20 — claim open: headline split into one sentence per claim: the switching half moved to CL-W43-08; this record keeps the overlap statistic with C-W43-05

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-07`, version 2)
- probe `C-W43-05`: `data/candidates/2026-W43.jsonl`
