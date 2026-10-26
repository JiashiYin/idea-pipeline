# Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.

`CL-W43-05` · lane **L4** · status **open** · rank 2 · position both · refreshed 2026-10-26

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 race window (golden); Gate 5 durability graded weak; kill search on C-W43-23 this run. Grade on paper: proper-shaped at best; automatic kill search this run on C-W43-23. Next action: see First steps.

## The claim

- **Headline:** Compaction summaries fail by unsourced persistence — claims no observation supports — not by length.
- **Current belief (the field's):** Compaction quality is tuned by compression ratio and length; 2610.20927 reports 83% of failures follow one unsourced bullet; SJC deletes them
- **If true:** Compactors label or delete unsourced entries by default; compaction evaluations add a provenance axis
- **If false:** Length and section controls match the judge — the provenance story is a correlation

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card's paper (sec. 9 and its design section) says the exposure/closure question for compaction summaries, memory files and sub-agent briefs has no oracle and spells out what one must deliver (a produced corpus, a seen corpus, a matcher, fixed computation); 2607.13071 (via C-W43-09's record) names 'a conflation of observation and persistence' in production compaction summaries and calls for re-verification; ACON derives its guidelines from LLM analyses of failures with no executable label. Who pays: every compaction and memory paper that reports a failure taxonomy; harness teams choosing between keeping more observations and gating what the summary asserts.
- **Impact ceiling:** **floor**: The three-cell table on one corpus, one model, one compressor; a footnote on CL-W43-05 that fixes which cell the claim's noun lives in. Requires only the corpus and the matcher. Probability 0.3 (judgment).; **middle**: The split names the lever (omission vs persistence vs never-fetched) for one harness and model, CL-W43-05 is re-worded with a pre-registered number, and compaction papers in the lane adopt the three-cell report in place of LLM-annotated taxonomies. Requires the 50-label audit to agree at 85% or better and the Prompting arm on a second model (another ~$300). Probability 0.45 (judgment).; **ceiling**: The same dominant cell appears on a second deterministic environment (OfficeBench, or a coding sandbox where needed values are file hashes and paths), and 'compaction fails by X, not Y' becomes a headline with a judge-free standard behind it that any harness can compute on its own logs. Requires a second environment with re-executable logs (~$600-1,000). Probability 0.25 (judgment).
- **Relevance:** **routes**: L4 all routes: product teams (which lever to pull); Narasimhan's self-evolving interest (what a self-written memory loses versus invents, measured without a judge); L1 evaluators (attribution of a failure to the summary, the agent, or the fetch by executable labels instead of a judge, the card's L1 contribution carried to compaction).; **industry**: Direct: the three cells are computable on any deterministic-environment log a harness team already stores.; **jacobs_edge**: Small: the probe is exact set algebra over logs and a matcher, no numerics or GPU content; the edge is in writing the identity cleanly and refusing the judge.; **zero_where**: L5 and L3: nothing about physics, scheduling or serving; L2: no training.
- **Kill probe:** Parse the public corpus, build $P$ and $S$, label needed and emitted values, 50-label audit; 0 GPU-hours, about $50 (about $300 if the Prompting arm must be re-run, shared with C-W43-08), 6 days; kills if $\pi_{\mathrm{exp}} \geq 0.5$ (omission dominates) or if more than 25% of needed values are unclassifiable (the oracle does not transfer).
- **Density and ownership:** Occupied by the card's paper: the build / exposure / closure decomposition for a deterministic scientific simulator, its Shapley attribution, and the explicit statement that compaction lacks the oracle. CL-W43-05's probes: C-W43-08 (matched random deletion arm), C-W43-09 (label vs delete arm), C-W43-10 (per-bullet counterfactual replay on the same TRACE corpus) are interventions or replays; none labels existing failures by the three cells, and C-W43-10's $V(b)$ would be the natural check on our closure labels if both run. ACON and The Complexity Trap analyze failures by LLM reading or not at all. 2610.03769 supplies the externalization / absorption / closure vocabulary in theory with no empirical oracle. From the card's neighbors nothing computes exposure versus closure on compaction logs; the kill search must count in the neighbors' words (compaction failure analysis, summary omission,…
- **Why now:** 2610.26836 (2026-W43) shows the judge-free oracle works and names compaction as the case without one; TRACE's re-executable boundary corpus (per C-W43-10's record) and SJC (2026-10-14) put the data and the claim on the table in the same month; CL-W43-05 opened 2026-10-20 with no observational probe.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: cheapest probe now C-W43-23 ($50, zero GPU, reads existing TRACE boundary failures with a scalar-matching oracle); kill pre-registered (exposure cell >= 50% of classified failures refutes 'not by length'); parked if >25% of needed values are unclassifiable |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a paper census (2610.20927: 83% of failures follow one unsourced bullet; 67.7% of Open TODOs unsourced), a product-log study (2607.13071 on Claude Code summaries), a second recipe paper (transparent-compact 2610.20116 flags stripped information) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: compactor builders (label or delete unsourced entries by default), compaction evaluators (provenance axis), product teams (Claude Code, Codex, OpenHands) |
| G4 | mechanism and consequence | pass: mechanism — after compaction the agent reads its own earlier plan as an observed fact and executes it; consequence — label or delete by provenance, or, if matched-count deletion matches the judge, provenance is a correlate of length and the gate is a length control; the two new probes split the mechanism into commission (kept unsourced bullets) and omission (dropped irrecoverable values) so each way the result comes out names a different compaction gate |
| G5 | durability; lab-adjacent | flagged: tied to the current generation of compactors and to one benchmark (AppWorld); a model that reads provenance labels changes the result; lane is lab-contested on the recipe side, and the claim is kept in measurement register |
| G6 | ownership, density, race window; position clause | open and at risk: kill search owed; density is the highest of any lane (SJC, PAIR, TRACE, RECAP within one month); race window about one compaction paper a week against a 10-day probe plus a one-week harness build is under the 2x rule for golden |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-23 | Omitted, never fetched, or overridden: a judge-free stage split of post-compaction failures | Parse the public corpus, build $P$ and $S$, label needed and emitted values, 50-label audit; 0 GPU-hours, about $50 (about $300 if the Prompting arm must be re-run, shared with C-W43-08), 6 days; kills if $\pi_{\mathrm{exp}} \geq 0.5$ (omi… | proposed | — |
| C-W43-21 | Omission of irrecoverable state versus commission of unsourced bullets: which predicts the compaction penalty on the sa… | Steps 1-3 on the TRACE corpus: ~$60 API, 0 GPU-hours, 5 days (10 with the optional cross-benchmark step at ~$300 more); kills if the unsourced count explains at least twice the penalty variance of the omission count or the omission coeffic… | proposed | — |
| C-W43-09 | Label the unsourced bullet instead of deleting it | Two arms x 168 x 3 runs on GPT; ~$450 marginal on the sibling candidate's harness; kills if tag-only is within 1 Pass3 point of Prompting and pattern counts do not fall by a third; 10 days shared. | proposed | — |
| C-W43-10 | Per-entry counterfactual value of compaction bullets on TRACE's paired-replay corpus | 60 boundaries, leave-one-entry-out, 4 paired continuations each; ~$600 API, 0 GPU-hours; kills if >= 70% of annotated entries flip or provenance AUROC >= 0.7, or if prefix re-execution reproduces < 90% of boundary states; 14 days. | proposed | — |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-23** (Sunday run), or run `/kill C-W43-23` in a session.
2. If it survives: `/redteam C-W43-23`, then the probe as pre-registered — Parse the public corpus, build $P$ and $S$, label needed and emitted values, 50-label audit; 0 GPU-hours, about $50 (about $300 if the Prompting arm must be re-run, shared with C-W43-08), 6 days; kills if $\pi_{\mathrm{exp}} \geq 0.5$ (omission dominates) or if more than 25% of needed values are unclassifiable (the oracle does not transfer).
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

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-05`, version 3)
- probe `C-W43-23`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-21`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-09`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-10`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-08`: `data/candidates/2026-W43.jsonl`
