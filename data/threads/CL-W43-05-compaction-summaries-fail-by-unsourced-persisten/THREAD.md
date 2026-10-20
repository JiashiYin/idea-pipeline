# Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.

`CL-W43-05` · lane **L4** · status **open** · rank 5 · position both · refreshed 2026-10-19

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 race window (golden); Gate 5 durability graded weak; proper-shaped at best. Grade on paper: proper-shaped at best pending kill search. Next action: see First steps.

## The claim

- **Headline:** Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.
- **Current belief (the field's):** Compaction quality is tuned by compression ratio and length; 2610.20927 reports 83% of failures follow one unsourced bullet; SJC deletes them
- **If true:** Compactors label or delete unsourced entries by default; compaction evaluations add a provenance axis
- **If false:** Length and section controls match the judge — the provenance story is a correlation

## Scorecard (from the cheapest probe's record)

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-09 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a paper census (2610.20927: 83% of failures follow one unsourced bullet; 67.7% of Open TODOs unsourced), a product-log study (2607.13071 on Claude Code summaries), a second recipe paper (transparent-compact 2610.20116 flags stripped information) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: compactor builders (label or delete unsourced entries by default), compaction evaluators (provenance axis), product teams (Claude Code, Codex, OpenHands) |
| G4 | mechanism and consequence | pass: mechanism — after compaction the agent reads its own earlier plan as an observed fact and executes it; consequence — label or delete by provenance, or, if matched-count deletion matches the judge, provenance is a correlate of length and the gate is a length control |
| G5 | durability; lab-adjacent | flagged: tied to the current generation of compactors and to one benchmark (AppWorld); a model that reads provenance labels changes the result; lane is lab-contested on the recipe side, and the claim is kept in measurement register |
| G6 | ownership, density, race window; position clause | open and at risk: kill search owed; density is the highest of any lane (SJC, PAIR, TRACE, RECAP within one month); race window about one compaction paper a week against a 10-day probe plus a one-week harness build is under the 2x rule for golden |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-09 | Label the unsourced bullet instead of deleting it | Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared. | proposed | — |
| C-W43-10 | Per-entry counterfactual value of compaction bullets on TRACE's paired-replay corpus | 60 boundaries, leave-one-entry-out, 4 paired continuations each; ~$600 API, 0 GPU-hours; kills if >= 70% of annotated entries flip or provenance AUROC >= 0.7, or if prefix re-execution reproduces < 90% of boundary states; 14 days. | proposed | — |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

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

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-05`, version 2)
- probe `C-W43-09`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-10`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-08`: `data/candidates/2026-W43.jsonl`
