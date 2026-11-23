# On CompAct-Bench's 200 instances, what a compaction must keep for the same executor to finish is under a fifth of what a forward reader of the history says it must keep: the literals the reference remainder actually consumes sit in under 20% of the forward inventory's 'required' units, their coverage by the compacted context predicts continuation success better than the inventory's omission count, and frontier compactors drop them regardless of whether the environment can give them back (kept-rate gap under 10 points).

`CL-W47-04` · lane **L4** · status **open** · rank — · position solo · refreshed 2026-11-22

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at concept level; Gate 6 open until the kill search (dense lane). Next action: see First steps.

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
| C-W47-08 | Live at the boundary: a hindsight liveness ruler for compaction, read off CompAct-Bench's own remainders against its fo… | Steps 0-2: $0, 0 GPU-hours, 4 days; dead if the dead-unit share is under 0.30 on both domains or the AUROC gain is under 0.03 on both; dead at step 0 without remainders and $M_b$ texts. | proposed | — |
| C-W47-09 | Dropped but re-fetchable: splitting compaction loss by whether the environment can give the literal back, with the pape… | Steps 0-2: $0, 0 GPU-hours, 4 days on the release; dead if $\Delta_\phi \geq 0.15$ for four of the top six compactors on Search or context-only literals are under 30% of Search's live literals; above $0 (about $400) if the environment-only… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W47-08** (Sunday run), or run `/kill C-W47-08` in a session.
2. If it survives: `/redteam C-W47-08`, then the probe as pre-registered — Steps 0-2: $0, 0 GPU-hours, 4 days; dead if the dead-unit share is under 0.30 on both domains or the AUROC gain is under 0.03 on both; dead at step 0 without remainders and $M_b$ texts.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): two $0 probes on CompAct-Bench's released traces; concept-level kill search scheduled this run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-04`, version 1)
- probe `C-W47-08`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-09`: `data/candidates/2026-W47.jsonl`
