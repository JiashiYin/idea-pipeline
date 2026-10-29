# Pasted context and scaffold layers steer agents by presence, not content: a same-length block from the wrong source moves a model's yield as much as the right one does.

`CL-W43-10` · lane **L1** · status **open** · rank 4 · position solo · refreshed 2026-10-29

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established. Grade on paper: open pending kill search. Next action: see First steps.

## The claim

- **Headline:** Pasted context and scaffold layers steer agents by presence, not content: a same-length block from the wrong source moves a model's yield as much as the right one does.
- **Current belief (the field's):** Harness papers read a per-model context effect as the information in the block: 2610.28802's abstract recommends 'combining configurations for broader coverage' and reports a targeted call-graph block raising weaker models' yield; investigator-agent papers attribute a semantic layer's harm to its content (C-W43-07's card).
- **If true:** Every scaffold or context-engineering comparison needs a same-length placebo arm, the way drug trials do; leaderboard 'harness' columns are re-read as prompt-form effects; harness builders spend on form (an authoritative-looking block) before retrieval quality.
- **If false:** Content wins: the placebo moves nothing, the information in the block is what helps, and the open question is which models can use it (C-W43-06's habit ruler).

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: the card paper's Limitations (each scaffold tested in one representative design; other designs are future work) and its finding that the layer lowers investigators' tool use; 2604.25149's interpretation that the layer changes 'what the model is being asked to do'. Who pays: teams building semantic layers and data catalogs for agents (the data-platform industry), data-agent benchmark owners (KramaBench, DataClaw) deciding whether to ship descriptions, and anyone evaluating a context-engineering claim without a placebo arm.
- **Impact ceiling:** **floor**: A control-arm result on two benchmarks and three open models saying how much of the layer's behavioral effect is content; cited by the next layer paper. Requires the four arms. Judgment p=0.5.; **middle**: A measurement with a mechanism: form explains most of the drop in investigation, content explains the accuracy change, and the layer-as-tool arm recovers investigation; a placebo-context arm becomes a standard control in context-engineering evaluations. Requires the fifth arm and one closed investigator model (about $400). Judgment p=0.3.; **ceiling**: A recipe default changes: data-agent harnesses serve the layer as a queryable tool rather than prompt text, with the paper's sign rule rewritten by form; adopted by one public harness. Requires the middle result replicated on the card paper's own harness. Judgment p=0.1.
- **Relevance:** HAL and evaluators: the placebo-context control as a standard arm for scaffold claims. Narasimhan (tau-family): low, no simulated user. Industry: direct for data-platform teams. Jacob's edge: zero for theoretical physics; small for computer engineering (serving models, building the placebo generator).
- **Kill probe:** Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead.
- **Density and ownership:** arXiv API 2026-10-19: 'semantic layer' + agent 52 total (45 in window); placebo/distractor + description + tool use 48; text-to-SQL schema robustness 82. Closest, abstracts read: 2604.25149 (layer document helps three frontier models equally, single-shot, no loop), 2609.37153 ToxicBench (blind compliance with poisoned tool outputs; the trusted object is evidence, not a description), 2605.07769 (action bias: agents act when inaction is right), 2601.07226 (contextual distractors degrade reasoning models), 2608.16045 (data exploration as a first-class step), 2605.25838 (schema variants change text-to-SQL answers), 2609.15779 EvoOntology (layer as a tool). No returned paper runs a placebo or content-free description arm against agent tool use; bounded by the search, limitation sections unread, kill search owed. Occupied by the card: the true-layer effect per group. Not re-proposed: any comp…
- **Why now:** Card paper 2026-10-14; 2604.25149 2026-04-28; EvoOntology code 2026-09-14.
- **Register, and what it is not:** Measurement with a mechanism and a control arm, with a small recipe consequence (layer as prompt versus layer as tool). It is not a new semantic-layer design, not a prompt-injection or robustness study, and not a compaction or memory recipe.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-07 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: the ruler is the placebo increment relative to the true-content increment, identifiable with same-length blocks and matched run counts; pre-registered surprise in C-W43-20 (placebo >= half the true increment, judgment 0.5) against the field's content reading |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every harness and context-engineering paper adds a placebo arm; benchmark owners re-read harness columns; product teams change what they paste |
| G4 | mechanism and consequence | pass: mechanism — an authoritative block changes the agent's search policy (fewer or more tool calls, 2610.28802's inverted dose: 144 graph-query calls with increment -6.5 vs 9 calls with +4.5), not its knowledge; consequence — spend on form or on retrieval |
| G5 | durability; lab-adjacent | pass as a ruler (applies to any agent and any block); the specific effect sizes are generation-bound |
| G6 | ownership, density, race window; position clause | open: density not measured (kill search owed); the placebo design is standard in medicine and the two cards' own papers skipped it, so 'why has nobody' needs the kill search's answer; race window unknown |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-07 | Placebo semantic layer: does form or content stop investigators looking | Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead. | proposed | — |
| C-W43-20 | Wrong repository's call graph as the placebo for pasted static-analysis context | Three arms times three open models times four runs (about 60 GPU-hours, about $100, 7 days); dead if nothing clears two SE at $k = 4$ or if the placebo moves yield by under a third of the true block while the true block clears two SE. | proposed | — |
| C-W43-06 | No-scaffold habit as a ruler for the sign of scaffold effects | Arm 1 alone (5,810 MedicalHarness runs, ~80 H100-hours, 6 days): if habit-based sign accuracy is within one sign of accuracy-based on the effects clearing 2 SE, or ICC < 0.5, dead. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-07** (Sunday run), or run `/kill C-W43-07` in a session.
2. If it survives: `/redteam C-W43-07`, then the probe as pre-registered — Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run from three orphans on one theme (prompts/11_claims.md rule: three orphans = a missing claim)
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 5 -> 4 after the kill run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-10`, version 2)
- probe `C-W43-07`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-20`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-06`: `data/candidates/2026-W43.jsonl`
