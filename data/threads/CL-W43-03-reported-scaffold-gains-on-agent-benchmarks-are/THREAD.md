# Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.

`CL-W43-03` · lane **L1** · status **open** · position both · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.
- **Current belief (the field's):** Scaffold papers attribute gains to their design; 2610.22289 §9.3: 'Further analysis is needed to determine their relative contributions'; HAL: higher effort can reduce scores
- **If true:** Scaffold papers must run the effort-notch and fresh-restart control arms; leaderboards separate scaffold from effort
- **If false:** Scaffold design carries independent value beyond effort — a measured answer to an open question

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** Asked in print: the card paper's Limitations (each scaffold tested in one representative design; other designs are future work) and its finding that the layer lowers investigators' tool use; 2604.25149's interpretation that the layer changes 'what the model is being asked to do'. Who pays: teams building semantic layers and data catalogs for agents (the data-platform industry), data-agent benchmark owners (KramaBench, DataClaw) deciding whether to ship descriptions, and anyone evaluating a context-engineering claim without a placebo arm.
- **Impact ceiling:** **floor**: A control-arm result on two benchmarks and three open models saying how much of the layer's behavioral effect is content; cited by the next layer paper. Requires the four arms. Judgment p=0.5.; **middle**: A measurement with a mechanism: form explains most of the drop in investigation, content explains the accuracy change, and the layer-as-tool arm recovers investigation; a placebo-context arm becomes a standard control in context-engineering evaluations. Requires the fifth arm and one closed investigator model (about $400). Judgment p=0.3.; **ceiling**: A recipe default changes: data-agent harnesses serve the layer as a queryable tool rather than prompt text, with the paper's sign rule rewritten by form; adopted by one public harness. Requires the middle result replicated on the card paper's own harness. Judgment p=0.1.
- **Relevance:** HAL and evaluators: the placebo-context control as a standard arm for scaffold claims. Narasimhan (tau-family): low, no simulated user. Industry: direct for data-platform teams. Jacob's edge: zero for theoretical physics; small for computer engineering (serving models, building the placebo generator).
- **Kill probe:** Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead.
- **Density and ownership:** —
- **Why now:** Card paper 2026-10-14; 2604.25149 2026-04-28; EvoOntology code 2026-09-14.
- **Register, and what it is not:** Measurement with a mechanism and a control arm, with a small recipe consequence (layer as prompt versus layer as tool). It is not a new semantic-layer design, not a prompt-injection or robustness study, and not a compaction or memory recipe.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-07 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-11 | Effort notch and fresh restart as control arms for scaffold gains | Restart-controller arm at GPT-5.5 xhigh capped at 45.5 M normalized tokens, 3 reps x 25 games, about $1,600 of the $2,200, 0 GPU-hours, 6 days; dead if RHAE < 53.2 in all reps and truncation curves separate on B <= 9 M. | proposed | — |
| C-W43-12 | Timed returns as the shuffled control for Stop-and-report | Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched. | proposed | — |
| C-W43-06 | No-scaffold habit as a ruler for the sign of scaffold effects | Arm 1 alone (5,810 MedicalHarness runs, ~80 H100-hours, 6 days): if habit-based sign accuracy is within one sign of accuracy-based on the effects clearing 2 SE, or ICC < 0.5, dead. | proposed | — |
| C-W43-07 | Placebo semantic layer: does form or content stop investigators looking | Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, d | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-07** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead.
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

- claim record: `data/claims/claims.jsonl` (id CL-W43-03)
- probe `C-W43-11`: `data/candidates/*.jsonl`
- probe `C-W43-12`: `data/candidates/*.jsonl`
- probe `C-W43-06`: `data/candidates/*.jsonl`
- probe `C-W43-07`: `data/candidates/*.jsonl`
