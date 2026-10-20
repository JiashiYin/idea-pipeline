# Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.

`CL-W43-05` · lane **L4** · status **open** · position both · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.
- **Current belief (the field's):** Compaction quality is tuned by compression ratio and length; 2610.20927 reports 83% of failures follow one unsourced bullet; SJC deletes them
- **If true:** Compactors label or delete unsourced entries by default; compaction evaluations add a provenance axis
- **If false:** Length and section controls match the judge — the provenance story is a correlation

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** In print: 2607.13071 names the mechanism as 'a conflation of observation and persistence' in Claude Code compaction summaries and calls for re-verification; SJC's card states the agent 'cannot distinguish the two' after compaction and the paper never passes the bit forward; transparent-compact argues for maximal transparency of the agent's view of its compacted context. Who pays: harness and product teams writing structured-summary prompts; memory-system authors who rely on provenance tags being read.
- **Impact ceiling:** **floor**: A negative: agents ignore provenance labels in their own summaries; a footnote cited by memory-schema papers; requires the two arms; probability 0.35 (judgment).; **middle**: Tag matches delete on one model and benchmark; a typed-summary default proposed to harness builders; requires replication on M3; probability 0.45 (judgment).; **ceiling**: Tag-plus-delete beats SJC and the typed schema is adopted by two public harnesses; requires OfficeBench and one coding harness (another ~$1,500); probability 0.2 (judgment).
- **Relevance:** L4 routes: product teams directly (a template change); all compaction and memory groups (whether the reader uses provenance); Narasimhan's self-evolving interest moderately (what a self-written memory should mark). Industry: direct. Jacob's edge: zero.
- **Kill probe:** Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared.
- **Density and ownership:** —
- **Why now:** SJC 2026-10-14 (the bit exists and is discarded); 2607.13071 (2026-07-11) names the failure in a production tool; transparent-compact 2026-10-14 shows flags are consumed by lightweight models.
- **Register, and what it is not:** Controlled comparison of a mechanism's two uses (label vs delete) in the measurement register, with a template consequence. Not a new compressor, not a judge, not a training method, not a memory system.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-09 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |
| C-W43-09 | Label the unsourced bullet instead of deleting it | Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared. | proposed | — |
| C-W43-10 | Per-entry counterfactual value of compaction bullets on TRACE's paired-replay corpus | 60 boundaries, leave-one-entry-out, 4 paired continuations each; ~$600 API, 0 GPU-hours; kills if >= 70% of annotated entries flip or provenance AUROC >= 0.7, or if prefix re-execution reproduces < 90% of boundary states | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-09** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared.
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

- claim record: `data/claims/claims.jsonl` (id CL-W43-05)
- probe `C-W43-08`: `data/candidates/*.jsonl`
- probe `C-W43-09`: `data/candidates/*.jsonl`
- probe `C-W43-10`: `data/candidates/*.jsonl`
