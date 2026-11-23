# On CompAct-Bench's 200 instances, what a compaction must keep for the same executor to finish is under a fifth of what a forward reader of the history says it must keep: the literals the reference remainder actually consumes sit in under 20% of the forward inventory's 'required' units, their coverage by the compacted context predicts continuation success better than the inventory's omission count, and frontier compactors drop them regardless of whether the environment can give them back (kept-rate gap under 10 points).

`CL-W47-04` · lane **L4** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G1 (no public traces: project site carries no data or code, 'No reference summaries'); G6 (ruler occupied by Compact-Bench 2610.31710 Recurring-Detail Retention with released data and scorer; recoverability axis and offline hindsight oracle occupied by 2608.16370; dead-store rule by Contexture 2611.26980); G2B on clauses 2 and 3; G4 on clause 3; G0 on the 'no re-derivability axis' sentence. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** On CompAct-Bench's 200 instances, what a compaction must keep for the same executor to finish is under a fifth of what a forward reader of the history says it must keep: the literals the reference remainder actually consumes sit in under 20% of the forward inventory's 'required' units, their coverage by the compacted context predicts continuation success better than the inventory's omission count, and frontier compactors drop them regardless of whether the environment can give them back (kept-rate gap under 10 points).
- **Current belief (the field's):** 2611.25673 (card, full text): the information inventory is 'the information required to continue the task', written 'from the original task and the complete pre-boundary history $H_b$, without access to any compacted context or continuation' (App. G.1); 'critical omission' is the leading error label at '47.8% of early failures / 48.8% of budget exhaustions' and is scored against that inventory; the stage reversal is explained at the domain level ('nine of the twelve compactors show a monotonic decrease on Search, whereas ten show a monotonic increase on Coding', sec. 3.3) with an environment-only control (Table 14) and no re-derivability axis in the labels; 'compaction can distort as well as omit task state' (sec. 1). The lane's killed claims (CL-W43-05, CL-W44-06, CL-W45-08) all scored the summary against a forward or presence-based ruler.
- **If true:** Compaction benchmarks score omission against a hindsight liveness set (what the continuation used), not a forward inventory; the 10% retention budget is not the binding constraint and is replaced by a sufficiency-based one; compactor recipes gain a recoverability rule (keep what no single re-read restores) that the frontier models do not have.
- **If false:** If the inventory already is the need set (dead-unit share under 0.30 on both domains): the forward reader is a valid ruler and the liveness scan adds a regex to a list the paper has — a footnote. If compactors already keep by recoverability ($\Delta_\phi \geq 0.15$ for four of six on Search): the recipe is in the models and the reversal is about something else.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's own 'inherently prospective' sentence (sec. 4) and Case E's 'proportion of the history that was load-bearing' (Table 23 discussion), a quantity gestured at and not computed; Context Compaction Theory 2608.01326 (card neighbour) defines the minimum budget for a query set and scores a compaction endpoint on set-membership queries, leaving agent remainders as the uncovered case (inference from the card's neighbour note); Slipstream 2605.08580 (card neighbour) uses the agent's own next steps as the judge of a summary online. Who pays: compaction benchmark owners (CompAct-Bench, Compact-Bench, TRACE, ARCBench), harness teams choosing a compaction prompt and ratio, and anyone training a compactor (CompactionRL 2607.05378, ACON) who needs a target that is not a forward guess.
- **Impact ceiling:** **floor**: A note with the dead-unit share, the $\ell^\star_i / 0.10\,\ell(H_b)$ distribution and the AUROC table on CompAct-Bench's release, cited by its v2 and by the next compaction benchmark. Requires steps 0-2. Judgment 0.55.; **middle**: Hindsight-live coverage adopted as a reported column by one compaction benchmark and a sufficiency-normalised ratio in one harness's evaluation; the 'critical omission' label split into live-and-dropped versus dead-and-dropped. Requires the sibling recoverability probe and a second corpus (Compact-Bench). Judgment 0.25.; **ceiling**: Liveness coverage becomes the standard scoring axis for compaction (every compaction paper reports it; compactor training targets it as reward). Requires a trained compactor from a group with compute and a second domain beyond coding and search. Judgment 0.08.
- **Relevance:** Narasimhan route: indirect (compaction as a training problem is L2; a hindsight target is what CompactionRL-style training lacks). HAL route: zero. Evaluators and benchmark validity: direct. Industry: direct (harness compaction prompts and ratios). Jacob's edge: liveness is compiler dataflow analysis, computer engineering; the kept / recovered / guessed partition of live literals is an identity he can check by hand; physics zero.
- **Kill probe:** Steps 0-2: $0, 0 GPU-hours, 4 days; dead if the dead-unit share is under 0.30 on both domains or the AUROC gain is under 0.03 on both; dead at step 0 without remainders and $M_b$ texts.
- **Density and ownership:** From the card and this repo's L4 kill records, not re-counted this week (the kill search counts): the hindsight signal is used online by Slipstream 2605.08580 (a judge checks the candidate summary against the agent's independently generated next steps) and as a theory by 2608.01326 (minimum budget for a query set, toy queries); literal-value matching over produced and seen corpora is the method of 2610.26836 per the CL-W43-05 record; the outcome-side pairings (TRACE 2608.06503 paired burden, Compact-Bench 2610.31710 PRE/POST, ARCBench 2611.03223, handoff audit 2611.06545) measure harm, not the need set; CL-W43-05 and CL-W44-06 were killed on the harm side (unsourced persistence; lost binding), and neither computed a need set. Pre-window precedents: live-variable analysis (Kildall 1973: a value is live when read later before being overwritten) and task-based extrinsic summary evaluation…
- **Why now:** CompAct-Bench v1 2026-11-19 (inventory, $M_b$, continuations and remainder per instance in one corpus); App. F's environment-only arm (same date) for the sibling probe. Flag: release status unknown.
- **Register, and what it is not:** Measurement with a scoring consequence (a hindsight-live column and a sufficiency-normalised ratio). It is not a compactor, not CompAct-Bench run on another benchmark, not a judge-based audit, and not a full-history control (occupied, CL-W44-06).

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched (200 instances; 25/50/75% boundaries; 12 compactors at a fixed 10% character ratio; success 100% to 57% average; 47.8% / 48.8% critical omission; Table 14 environment-only control; card, full text). Conditioning set: the reference remainder and the three continuations exist in the traces (card: 'generated once' for $M_b$; 3 continuations per fixed $M_b$), so liveness is read in hindsight on a fixed summary and the executor's draw is the only random term; the compressor's temperature is unstated (card) and does not enter a hindsight scan. Flag: the card s… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: both probes $0 and four days if the traces ship; kills written; both outcomes informative (the first hindsight sufficiency measurement on a compaction benchmark either way). Dead at step 0 if no release carries remainders and summaries. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'what a compaction must keep' made measurable as the literal set the continuation consumed. Surprise three ways: expected — live literals in under a fifth of 'required' units, live coverage beats omission count by AUROC $\geq 0.03$, recoverability-blind compactors (judgment 0.4); field assumes — the forward inventory is the need set and omission is the failure (card App. G.1, sec. 3.2); belief-changing — the inventory is the need set (0.35) or compactors already select by recoverability (0.25). Flag for the kill search: Slipstream 2605.08580 uses a hindsight check online and… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: compaction-benchmark owners (replace the forward inventory), compactor-recipe authors (a recoverability rule), harness builders (budget by sufficiency, not ratio), the L4 measurement thread. Proper-shaped; the lane is dense and the race window is checked at the kill search. |
| G4 | mechanism and consequence | Mechanism: a forward reader lists everything plausibly needed; the continuation uses a small subset of literals (ids, paths, values) and re-derives the rest from the environment where the environment is a repository (Coding) but not where it is a search chain (Search), which is the stage reversal priced in actions. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the liveness ruler applies to any trajectory with a remainder; flag — the lane publishes about two papers a week and the ruler's name may already exist under other words (hindsight sufficiency, oracle summary, information need). |
| G6 | ownership, density, race window; position clause | Density owed at the kill search in the lane's role words (compaction, context folding, working context, summary sufficiency, oracle, hindsight, live variables, information need, recoverable, re-fetch, offloading, file-backed memory) plus the compiler import's words (liveness, dead store). Known neighbours from the card and records: Slipstream 2605.08580, 2608.01326, 2610.26836 (literal matching, CL-W43-05 record), TRACE 2608.06503, Compact-Bench 2610.31710. Why now: CompAct-Bench (2026-11-19) ships boundaries, summaries and continuations for 200 instances. Race: dense; window to be estimated… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-08 | Live at the boundary: a hindsight liveness ruler for compaction, read off CompAct-Bench's own remainders against its fo… | Steps 0-2: $0, 0 GPU-hours, 4 days; dead if the dead-unit share is under 0.30 on both domains or the AUROC gain is under 0.03 on both; dead at step 0 without remainders and $M_b$ texts. | killed | — |
| C-W47-09 | Dropped but re-fetchable: splitting compaction loss by whether the environment can give the literal back, with the pape… | Steps 0-2: $0, 0 GPU-hours, 4 days on the release; dead if $\Delta_\phi \geq 0.15$ for four of the top six compactors on Search or context-only literals are under 30% of Search's live literals; above $0 (about $400) if the environment-only… | killed | — |

## Kill search

### Concept level (CL-W47-04) — killed (2026-11-22)
The object is unreleased, so both $0 probes die at step 0; the live-literal ruler is Compact-Bench's released Recurring-Detail Retention (9,330 atoms, substring membership, LLM summaries keep at most 16%); the recoverability axis and hindsight oracle are 2608.16370's pre-registered arms (random matches hindsight); the seed's own protocol already discounts environment-recoverable information.
Full record: [`data/reports/2026-W47-kill-CL-W47-04.md`](../../../data/reports/2026-W47-kill-CL-W47-04.md).
**Occupied by:** 2610.31710 (ruler of clauses 1-2); 2608.16370 (recoverability axis and offline hindsight oracle of clause 3); 2611.26980 (dead-store import); 2611.25673 sec. 3.3 / App. G.1 / Table 15 (clause 3's premise and if_true recipe)
**Why not done before:** The ruler, the recoverability axis and the dead-store rule are done; the one undone comparison (hindsight literal set versus a forward 'required' inventory on one corpus) needs CompAct-Bench's traces, which are three days old and unreleased, so the owners hold the enabling piece. Not 'no reason'.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.31710` Compact-Bench: Measuring What Context Compaction Costs Long-Horizon Coding Agents — Pair full-history and summary-only continuations from one repository snapshot, and on 146 real coding sessions extract the paths, SHAs, PR ids, error types, URLs, key-value pairs and IPs that occur both before an artificial boundary and in the next 3-8 reques… *Difference:* none for the live-literal ruler - occupied with released data (e2/sessions.jsonl, 9,330 atoms) and scorer; lacks a forward inventory, a per-cell outcome beside retention, a use-before-re-supply condition and a recoverability split; its finding runs against cl…
- `2608.16370` What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Complet… — In a deterministic planning environment, drop or preserve state under compression, restore it by oracle interventions, and count retrieval tool calls as the reacquisition cost completion metrics miss. *Difference:* none for the recoverability axis (externally queryable D vs history-dependent R) and the offline hindsight oracle by future re-access counts - occupied as designs; recoverability-prioritized retention does not beat random, random matches the hindsight oracle;…
- `2611.26980` Contexture: Runtime Context Eviction for High-Throughput Agent Serving — Trace each history token to the tool operation that produced it and mark an earlier observation as a removal candidate when a later operation on the same target supersedes it, then commit removals under KV pressure. *Difference:* none for the dead-store import - occupied as a rule and a census (64% of final-history tokens superseded); forward-computable, serving register, no comparison with an LLM compactor's choices, no literal granularity
- `2611.25673` CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks — Cut a solved run at 25/50/75%, compact the history to 10% of its characters with twelve models, let the same executor finish under the reference remainder budget. *Difference:* the seed; its App. G.1 excludes environment-recoverable information from 'preserved', Table 15 discounts omitted code that persists in the environment, sec. 3.3 states the recoverability recipe; no release (project site: paper, leaderboard, demo; 'No referenc…
- `2610.31778` Benchmarks Are Surprisingly Compaction-Friendly — Fix one scaffold, run five compaction strategies and three frontier models on three long-horizon benchmarks, count dropped task constraints. *Difference:* states clause 3's premise as the field's position ('most of what compaction discards can be recovered, except constraints that don't exist anywhere else'); constraints not literals, no per-literal kept rate
*Search degraded:* ['s2 (skipped)', 'WebFetch of compaction-eval.github.io (permission request timed out; site fetched by curl instead)', 'conference exports not built', "Q5 defective breadth (1,690 total; 'summary' AND 'next action' match everything; 9 on target by hand)"]

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

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): two $0 probes on CompAct-Bench's released traces; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (data/reports/2026-W47-kill-CL-W47-04.md): killed — gate G1 (no public traces: project site carries no data or code, 'No reference summaries'); G6 (ruler occupied by Compact-Bench 2610.31710 Recurring-Detail Retention with released data and scorer; recoverability axis and offline hindsight oracle occupied by 2608.16370; dead-store rule by Contexture 2611.26980); G2B on c…
- 2026-11-22 — C-W47-08 killed: W47 concept-level kill search of CL-W47-04: probe verdict killed. dead at step 0 (no released remainders or M_b texts); its ruler is Compact-Bench's released Recurring-Detail Retention (substring membership of future-recurring literals, LLM summaries keep at most 16%); its AUROC clause contradicts Compact-Bench's retention-vs-preservation divergence and 2608.16370's hindsight-equals-random withou…
- 2026-11-22 — C-W47-09 killed: W47 concept-level kill search of CL-W47-04: probe verdict killed. dead at step 0 (no released environment-only traces or M_b texts); its recoverability axis is 2608.16370's pre-registered D/R split with a null on recoverability-prioritized retention; its if_true recipe is the seed's sec. 3.3 sentence and CWL/Contexture/Self-GC's shipped policies; its premise 'no re-derivability axis in the labels…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-04`, version 2)
- probe `C-W47-08`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-09`: `data/candidates/2026-W47.jsonl`
