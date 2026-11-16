# In the human-labelled corpora of naturally failed multi-agent runs that failure-attribution methods are trained and scored on (Who&When, MAST's annotated traces, LongRCA Bench), at least one in ten runs carrying a responsible-agent label ended on a message written by the harness or the provider's error path, not by any agent.

`CL-W46-01` · lane **L1** · status **open** · rank 3 · position solo · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none hard yet; Gate 6 not established; Gate 2B risk flagged (the mechanism is in print on one corpus). Next action: see First steps.

## The claim

- **Headline:** In the human-labelled corpora of naturally failed multi-agent runs that failure-attribution methods are trained and scored on (Who&When, MAST's annotated traces, LongRCA Bench), at least one in ten runs carrying a responsible-agent label ended on a message written by the harness or the provider's error path, not by any agent.
- **Current belief (the field's):** LongRCA Bench 2608.15242 (abstract, fetched 2026-11-15): '1,140 complete failed trajectories from five sources, all human-annotated for responsible roles and earliest decisive root-cause steps'. 2610.17747 (abstract, fetched 2026-11-15) names the validity threat to attribution benchmarks as 'spurious signals (surface cues) that predict the annotation' and proposes four tests, none of which asks whether an agent produced the terminal message. The card (2611.13254, full text): on the one scanned corpus 'the corpus attributes those 25 runs to the orchestrator in 4 and to another agent (mostly the web surfer) in 21' — measured 26/58 on the hand-crafted split and 0/126 on the generated split; the other corpora are 'unscanned'.
- **If true:** Corpus owners add an exclusion rule and a terminal-message provenance field; method papers report accuracy on agent-finished runs; the MAST-style taxonomies gain a 'no agent acted' category; verifiers trained on these labels (AFANet 2608.18575 and kin) are re-trained on clean splits — for the attribution community, one community, so proper-shaped.
- **If false:** The Who&When hand-crafted split is a one-framework, one-provider 2025 artefact; the published accuracies on LongRCA and MAST stand; the footnote is the re-scored Who&When table (C-W46-02) and the clean certificate for the larger corpora.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.13254 sec. 4.6 and its open-items list ('the same harness-fault scan on MAST-Data, LongRCA or TRAVERSE; and the effect of the 45% contaminated split on published attribution accuracies'); 2610.17747's call to 'report these tests when developing failure-attribution benchmarks'. Who pays: the attribution-method community (54 arXiv papers in the 12-month window on the conjunction 'failure attribution' AND multi-agent AND LLM, fetched 2026-11-15), the corpus owners, and anyone training a verifier on these labels.
- **Impact ceiling:** **floor**: A note with $h_c$ per corpus and the label-vs-last-speaker table, cited by the next corpus release and by 2611.13254 v2. Requires steps 0-2. Judgment p 0.6.; **middle**: An exclusion rule and a terminal-message provenance field adopted by one corpus (LongRCA or the Who&When maintainers) and a re-scored accuracy table for the methods evaluated on it. Requires C-W46-02 as well. Judgment p 0.25.; **ceiling**: 'Who wrote the last message' becomes a standard validity test for trajectory corpora (attribution, TRAVERSE-style mistake annotation, MAST-style taxonomies), with a 'no agent acted' category in the taxonomies. Requires the single-agent extension to TRAVERSE and a taxonomy owner's adoption. Judgment p 0.1.
- **Relevance:** Narasimhan route (tau-family): zero. HAL route: indirect (HAL's archives are not attribution corpora; the provenance rule applies to any trajectory release). Evaluators and benchmark-validity work: direct. Industry: moderate (teams training failure-locating verifiers on public corpora). Jacob's edge (numerics, GPUs, identities): zero; this is a deterministic text audit.
- **Kill probe:** Step 1: $0, 0 GPU-h, 5 days; dead if pooled $h < 0.05$ (Wilson upper bound under 0.08) and both LongRCA and MAST under 0.05.
- **Density and ownership:** Occupant of the mechanism on one corpus: 2611.13254 ('26 of 58 hand-crafted Magentic-One runs end in a provider content-filter HTTP 400 ... 0 of 126 algorithm-generated runs'); its authors are the natural owners of the extension. Nearest validity audit: 2610.17747 ('on three benchmarks, simple predictors match or beat GPT-4.1') — cue predictability, not label-object validity. Corpora: Who&When 2505.00212, MAST 2503.13657, LongRCA 2608.15242; injected corpora excluded by construction (Who&When Pro 2607.09996: 'injects a failure only after exactly replaying a successful prefix'; Aegis 2509.14295: 'adaptively inject context-aware errors into successful execution trajectories'). Density on the harness-fault conjunction (provider/harness error words AND agent AND trajectories AND failure/attribution): 11 total, 1 direct (the card), fetched 2026-11-15; the attribution-method conjunction: 54 i…
- **Why now:** 2611.13254 posted 2026-11-09 with the scan on one corpus and the open list; LongRCA v4 2026-08-15. Flag: the method is a string scan; the enabling piece is the released corpora, not a technique.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass. Premise numbers fetched and dated with denominators: 26/58 and 0/126 (2611.13254 sec. 4.6, 2026-11-09); 1,140 trajectories from five sources (2608.15242, v4 2026-08-15); 54 attribution papers in the window (arXiv API, 2026-11-15). The quantity $z_i$ (terminal message authored by a non-LLM code path or a provider error with no agent message after it) is deterministic given the released trace text; its conditioning set is the corpus's own record format, and it is a property of the corpus, not of a protocol or a temperature. Judge and grader are not involved. Plain trick: read who authored… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass. C-W46-01 costs $0 and five days; the kill is written (pooled $h < 0.05$, upper bound under 0.08, with LongRCA and MAST each under 0.05). Both outcomes are informative: the negative certifies the two largest corpora clean and re-scores Who&When as a footnote. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B, with a stated 2B risk. The ruler (harness-terminated share of a labelled corpus) is identifiable from released text and computable from data the owners published. Pre-registered three readings: expected (judgment 0.4) pooled $h \geq 0.10$ with orchestrator-style sources at 10-30% and single-agent sources near 0; the field assumes 0 (every labelled run has a responsible agent; 2610.17747's threat model has no such category); belief-changing if $h \geq 0.10$. Risk: the finding exists in print on one corpus with the number attached (45% of one split); the claim is the generalisation to… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Three consumer classes with actions: corpus owners (exclusion rule, provenance field, 'no agent acted' label), method authors (clean-split accuracy), verifier trainers (re-train on clean labels). Must-change population: the attribution community — one community, so proper, not golden, unless the single-agent extension (TRAVERSE) carries it to mistake-annotation corpora generally. |
| G4 | mechanism and consequence | Mechanism written: orchestrator frameworks catch provider exceptions and emit a fallback final answer or stop; an annotator reading the transcript assigns the agent who spoke last before the termination (the card: 21 of 25 labels on the web surfer in runs the orchestrator's ledger call crashed). Consequence each way: $h \geq 0.10$ — exclusion rule and provenance field, re-scored tables; $h < 0.05$ — one-off, footnote. The two actions differ from each other and from the seed paper's recommendation (which asks for a human check of its annotations, not a corpus rule). |
| G5 | durability; lab-adjacent | Partly. The per-corpus numbers are consumed as soon as the corpora are cleaned; the rule (authorship of the terminal message as a validity field) applies to any trajectory release and survives model generations. Lab-adjacent: nobody at a frontier lab owns these corpora. Not head-to-head. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17). Density on the day of writing: 11 total / 1 direct on the harness-fault conjunction; 54 on attribution methods (about one a week — the community is dense on methods, sparse on corpus validity). Occupants: 2611.13254 (the one-corpus scan; natural owners; race risk if they extend in v2), 2610.17747 (cue audits). Why now: the open list posted 2026-11-09. Role words for the kill search, in the neighbours' vocabulary: label noise, annotation noise, trace quality, spurious cue, surface cue, benchmark contamination, infrastructure error, fallback… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-01 | Who wrote the last message: a harness-termination census of the human-labelled failure-attribution corpora | Step 1: $0, 0 GPU-h, 5 days; dead if pooled $h < 0.05$ (Wilson upper bound under 0.08) and both LongRCA and MAST under 0.05. | proposed | — |
| C-W46-02 | Re-scoring attribution on the runs an agent finished: Who&When accuracies with the 26 harness-terminated runs held out | Steps 0-1: $0, 3 days; dead if no released method moves by more than 2 points and the last-speaker baseline is flat across splits. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-01** (Sunday run), or run `/kill C-W46-01` in a session.
2. If it survives: `/redteam C-W46-01`, then the probe as pre-registered — Step 1: $0, 0 GPU-h, 5 days; dead if pooled $h < 0.05$ (Wilson upper bound under 0.08) and both LongRCA and MAST under 0.05.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin bottom-up (lifted from C-W46-01, C-W46-02 on card 2611.13254); first L1 claim since CL-W45-02; concept-level kill search owed before any probe is elaborated (rule 17)
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 3: born W46: $0 probe in 5 days, community-wide consumer (every failure-attribution corpus and method), durable procedure; Gate 2B risk (2611.13254 has the mechanism on one corpus) goes to the kill search; concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-01`, version 1)
- probe `C-W46-01`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-02`: `data/candidates/2026-W46.jsonl`
