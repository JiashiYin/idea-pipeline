# Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.

`CL-W43-05` · lane **L4** · status **open** · rank 3 · position both · refreshed 2026-10-29

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 0 (premise number corrected; headline quantifier unwritten); Gate 6 race window; Gate 5 weak. Grade on paper: open, re-probe owed; headline quantifier to be pre-registered or removed at the next claims run; proper-shaped at best. Next action: see First steps.

## The claim

- **Headline:** Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.
- **Current belief (the field's):** Compaction quality is tuned by compression ratio and length; SJC 2610.20927 reports that 29 of 35 analyzed Prompting-arm failures follow a summary entry and 25 of 35 (71%) follow an entry no environment output supports or that contradicts one (Table 11, after a 9-run exclusion), and deletes unsourced entries; TRACE 2610.08722's human causal audit finds 0 of 14 pure compression-caused failures
- **If true:** Compactors label or delete unsourced entries by default; compaction evaluations add a provenance axis
- **If false:** Length and section controls match the judge — the provenance story is a correlation

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2607.13071 names the mechanism as 'a conflation of observation and persistence' in Claude Code compaction summaries and calls for re-verification; SJC's card states the agent 'cannot distinguish the two' after compaction and the paper never passes the bit forward; transparent-compact argues for maximal transparency of the agent's view of its compacted context. Who pays: harness and product teams writing structured-summary prompts; memory-system authors who rely on provenance tags being read.
- **Impact ceiling:** **floor**: A negative: agents ignore provenance labels in their own summaries; a footnote cited by memory-schema papers; requires the two arms; probability 0.35 (judgment).; **middle**: Tag matches delete on one model and benchmark; a typed-summary default proposed to harness builders; requires replication on M3; probability 0.45 (judgment).; **ceiling**: Tag-plus-delete beats SJC and the typed schema is adopted by two public harnesses; requires OfficeBench and one coding harness (another ~$1,500); probability 0.2 (judgment).
- **Relevance:** L4 routes: product teams directly (a template change); all compaction and memory groups (whether the reader uses provenance); Narasimhan's self-evolving interest moderately (what a self-written memory should mark). Industry: direct. Jacob's edge: zero.
- **Kill probe:** Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared.
- **Density and ownership:** Occupied: SJC delete-only gate; transparent-compact (deterministic verbatim retention plus flags of stripped information, Pi agent, lightweight models); MemTrace 2610.04838 (provenance-aware memory traces with validity checks before restoring evidence, coding agents); Memory Echo 2610.17763 (Family-Provenance-Authority gating in long-term memory); REMORY 2610.11287 (soft residual tokens improving source attribution on SummHay); When History Lies 2608.06057 (polluted history hijacks tool-use policy; Oracle State view). arXiv API: compactor/condenser/compaction-summary x agent x provenance/fabricated/unsupported = 24 total, 19 in window, closest Slipstream 2605.08580 (judge validates the summary against the agent's asynchronous continuation) and 2607.13071; broad provenance x compaction x agent query hit the 100-result cap (198 total) and is uninformative. No in-window hit renders a per-e…
- **Why now:** SJC 2026-10-14 (the bit exists and is discarded); 2607.13071 (2026-07-11) names the failure in a production tool; transparent-compact 2026-10-14 shows flags are consumed by lightweight models.
- **Register, and what it is not:** Controlled comparison of a mechanism's two uses (label vs delete) in the measurement register, with a template consequence. Not a new compressor, not a judge, not a training method, not a memory system.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | flagged 2026-10-25: the claim's premise number was misquoted ('83% follow one unsourced bullet'); SJC 2610.20927 reports 29 of 35 analyzed failures following a summary entry (83%) and 25 of 35 (71%) following an unsupported or contradicted one, after a 9-run exclusion; corrected in current_belief |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass on paper: cheapest proposed probe is again C-W43-09 (~$450); no probe has survived a kill search and red team |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a paper census (2610.20927: 83% of failures follow one unsourced bullet; 67.7% of Open TODOs unsourced), a product-log study (2607.13071 on Claude Code summaries), a second recipe paper (transparent-compact 2610.20116 flags stripped information) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: compactor builders (label or delete unsourced entries by default), compaction evaluators (provenance axis), product teams (Claude Code, Codex, OpenHands) |
| G4 | mechanism and consequence | pass: mechanism — after compaction the agent reads its own earlier plan as an observed fact and executes it; consequence — label or delete by provenance, or, if matched-count deletion matches the judge, provenance is a correlate of length and the gate is a length control; the two new probes split the mechanism into commission (kept unsourced bullets) and omission (dropped irrecoverable values) so each way the result comes out names a different compaction gate; 2026-10-25: 'not by length' is touched by none of the probes — a matched-length control (C-W43-08's arm) is the only one that tests th… |
| G5 | durability; lab-adjacent | flagged: tied to the current generation of compactors and to one benchmark (AppWorld); a model that reads provenance labels changes the result; lane is lab-contested on the recipe side, and the claim is kept in measurement register |
| G6 | ownership, density, race window; position clause | open and at risk: kill search owed; density is the highest of any lane (SJC, PAIR, TRACE, RECAP within one month); race window about one compaction paper a week against a 10-day probe plus a one-week harness build is under the 2x rule for golden; 2026-10-25: SJC already publishes the unsourced share by LLM annotation and TRACE's human causal audit (14 trajectories, 46 compactions) finds 0 pure compression-caused failures and 11 of 12 POLICY — the claim's quantifier is contested in print both ways |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-09 | Label the unsourced bullet instead of deleting it | Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared. | proposed | — |
| C-W43-10 | Per-entry counterfactual value of compaction bullets on TRACE's paired-replay corpus | 60 boundaries, leave-one-entry-out, 4 paired continuations each; ~$600 API, 0 GPU-hours; kills if >= 70% of annotated entries flip or provenance AUROC >= 0.7, or if prefix re-execution reproduces < 90% of boundary states; 14 days. | proposed | — |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |
| C-W43-21 | Omission of irrecoverable state versus commission of unsourced bullets: which predicts the compaction penalty on the sa… | Steps 1-3 on the TRACE corpus: ~$60 API, 0 GPU-hours, 5 days (10 with the optional cross-benchmark step at ~$300 more); kills if the unsourced count explains at least twice the penalty variance of the omission count or the omission coeffic… | proposed | — |
| C-W43-23 | Omitted, never fetched, or overridden: a judge-free stage split of post-compaction failures | Parse the public corpus, build $P$ and $S$, label needed and emitted values, 50-label audit; 0 GPU-hours, about $50 (about $300 if the Prompting arm must be re-run, shared with C-W43-08), 6 days; kills if $\pi_{\mathrm{exp}} \geq 0.5$ (omi… | killed | survived-kill |

## Kill search

### C-W43-23 — survived-kill (2026-10-25)
No fetched paper computes the never-fetched / dropped / overridden split with executable labels on natural post-compaction failures, so no neighbour's difference is 'none'; survival is 'first to measure with a judge-free label', weak, and the probe's Gate 1 premise (a public corpus with summaries and full trajectories) is false, raising cost to about $300 and two weeks via the SJC/ACON harness re-run.
Per position — **solo**: killed (red team 2026-10-25); redesigned census owed as a new candidate; **lab**: killed: an owned production log carries no reference solution, so the typed oracle does not transfer; only reference-free labels do
**Why not done before:** it is hard because the field reaches for a judge on naturalistic corpora (2606.25449: 'a naturalistic corpus would reintroduce the judge model we deliberately avoid'; SJC used LLM annotators and lists it as a limitation), and an enabling piece landed: 2610.26836 (2026-10-19) showed literal-value matching over produced and seen corpora is exact when the tool is deterministic, and SJC's harness (ACON patch + OpenClaw compressor, github.com/GuanghuiMin/sjc, 2026-10-14) makes the Prompting arm re-runnable. The group that holds the logs and the limitation sentence (SJC's authors) is the natural first mover.
**Occupied by:** none (partial occupation: 2610.20927 holds the unsourced share on natural AppWorld failures by LLM annotation; TRACE's causal_annotation holds a human mechanism split at n = 14)
Closest neighbors (one-sentence trick; one-line difference):
- `2610.20927` Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents (SJC) — After the compressor writes a summary, ask a non-generative decision model whether each entry has a source in the environment outputs or the previous summary, and delete the entries that do not. *Difference:* Its failure analysis already does two of the candidate's three cells on natural AppWorld failures (OpenClaw compressor, GPT-5.6 Luna, 90 training tasks x 3 runs): 29 of 35 analyzed failed runs carry out a summary entry, 22 of those entries are supported by no…
- `2608.06503 (+ repository nokia-applied-research/Trace, read 2026-10-25) and 2610.08722` Towards Reliable Context Compression for Long-Horizon Agents (TRACE), its frozen 590-boun… — Rebuild the AppWorld state at each real compaction boundary twice, continue once with raw history and once with the summary, and score the summary by how many of the next actions error or repeat an earlier call; a side annotation treats a summary defect as ca… *Difference:* The corpus does not carry what the probe needs: the repository's own words are 'data/ ships the derived boundaries and rollouts, not these source trajectories' (docs/COLLECTION.md) and 2610.08722 App. A lists what is released: 'Sorted sets of prior calls and…
- `2606.25449` Reclaim Evaluation: A Lossy Memory Is Worse Than an Empty One — Plant a known wrong conclusion, compress at a fixed budget keeping either the answer or the work behind it, deliver a correction, and score exact recovery without a judge; a memory that kept the stale value and dropped its source makes the model re-emit the s… *Difference:* Judge-free exact-match scoring of a compaction's unsourced-persistence failure, replicated on tau-bench by database-state hash, but on induced drift with the source present by construction; it names the naturalistic agent-log case as untested and says a judge…
- `2608.11392` AI Guardrail Survival under Single-Cycle Agentic Self-Summarization — Compact once with a planted safety rule in context, then check whether the rule is dropped, degraded to a residue, or intact, and replay behaviour to see whether each state still prevents the prohibited action; textual presence is not a safety check because r… *Difference:* A dropped / degraded / present-but-not-acted-on split (the exposure and closure cells) measured by behavioural replay for one planted fact type on synthetic sessions; the candidate labels natural failures and adds the never-fetched cell.
- `2606.22528` Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horiz… — Place a governance constraint in context, compact, grade tool calls deterministically, and split episodes by whether the constraint survived the summary: violation is 0% when it survives and 38% when it is dropped. *Difference:* A judge-free exposure split (fact kept vs dropped) with deterministic tool-call grading, for an injected constraint on 1,323 synthetic episodes; no natural failures, no never-fetched or unsourced cell.
**Probe as pre-registered (checked):** Restated: label every failed AppWorld task with at least one compaction boundary by whether the needed value v* (argument of a state-changing reference-solution call) was never in any environment output (build), in an output but absent from the summary plus post-boundary tool results (exposure), or present and overridden (closure); label the emitted wrong value as unsourced if no output ever contained it; exact normalized matching, no judge; 50-label two-annotator audit. Gate 1 correction: the $50 arm is void because the TRACE release carries no summary text and no source trajectories (repository docs/COLLECTION.md; 2610.08722 App. A) and has no licence; the probe runs on the $300 fallback,…
*Search degraded:* ['s2 skipped (no key)', 'exports: not built', 'complaints: skipped (no GitHub access)', 'TRACE source trajectories and SJC run logs are not public; corpus facts taken from repository docs and 2610.08722, not from opening a trajectory file']

## Red team

**C-W43-23** — {"date": "2026-10-25", "rounds": 1, "protocol": "three attacker personas (systems, theory, professor + checklist) as parallel agents; a separate defender agent answered every objection in writing before conceding; the operator graded", "objections": [{"persona": "systems; theory; theory; professor", "class": "killing", "objection": "No matched uncompressed control: the claim concludes 'compaction fails by X' from a census of post-compaction failures, but in the same harness the No-compression arm fails 15.9% of runs (acc 84.1%) against Prompting's 23.2% (acc 76.8%), so under nesting about two thirds of the Prompting arm's failures are failures the agent has with no summary at all, and TRACE's annotators found none of 14 compression-caused. The three cells must be differenced against the No-compression arm's failures (where exposure is zero by construction and the cells reduce to build versus closure); without that arm the census measures the agent's baseline failure anatomy, and the 'build dominates' outcome the record half-expects says nothing about compaction. The control costs a second arm of 441 runs at roughly the same token count.", "evidence": "", "answer": "conceded: the a…

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-09** (Sunday run), or run `/kill C-W43-09` in a session.
2. If it survives: `/redteam C-W43-09`, then the probe as pre-registered — Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared.
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
- 2026-10-20 — claim open: graded: probes re-ranked by cost (09 < 10 < 08); race window under the golden rule; kill search owed next on C-W43-09
- 2026-10-25 — claim open: claims (closing W43): C-W43-21 and C-W43-23 attached from cards 2610.26632 and 2610.26836; cheapest probe moves from C-W43-09 ($450) to C-W43-23 ($50); rank 2; second automatic kill search this run
- 2026-10-25 — claim open: kill + red-team run (closing W43): C-W43-23 survived-kill (weak) then killed by the red team (19 merged objections: 10 answered, 9 conceded, 5 killing conceded); premise number corrected; rank 2 -> 3
- 2026-10-25 — C-W43-23 survived-kill: kill search (stage 4, automatic, claim-ranked): survived-kill — No fetched paper computes the never-fetched / dropped / overridden split with executable labels on natural post-compaction failures, so no neighbour's difference is 'none'; survival is 'first to measure with a judge-free label', weak, and the probe's Gate 1 premise (a public corpus with summaries and full trajectories) is false, rais…
- 2026-10-25 — C-W43-23 killed: red team (stage 5, automatic, three personas + separate defender; 30 objections merged to 19: 10 answered, 9 conceded, 5 killing conceded): killed — killed as a probe of CL-W43-05 as written: four killing objections conceded with evidence — (1) no uncompressed control, so 'compaction fails by X' does not follow from a census of post-compaction failures (SJC Table 3: 116.9 vs 80.1 failures of 504…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-05`, version 4)
- probe `C-W43-09`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-10`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-08`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-21`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-23`: `data/candidates/2026-W43.jsonl`
