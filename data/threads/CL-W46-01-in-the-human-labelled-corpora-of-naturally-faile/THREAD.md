# In the human-labelled corpora of naturally failed multi-agent runs that failure-attribution methods are trained and scored on (Who&When, MAST's annotated traces, LongRCA Bench), at least one in ten runs carrying a responsible-agent label ended on a message written by the harness or the provider's error path, not by any agent.

`CL-W46-01` · lane **L1** · status **killed** · rank None · position solo · refreshed 2026-11-16

## Status

Killed — see the kill section. Failing gate: Gate 0 (premise: pooled harness-termination share 0.020 on 1,324 released runs, under the 0.05 kill line; MAST carries no responsible-agent label); Gate 2B, Gate 4, Gate 6 behind it. Next action: see First steps.

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
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W46-01.md): killed; gate failed G0; occupied_by 2611.13254; why not done: No reason found for the positive claim; the generalisation was not published because it is negative and empty — LongRCA's construction excludes infrastructure runs and records the harness as a named speaker with a termination reason, and MAST's human split has no agent labels to contaminate.. Previous: Unmeasured: concept-level kill search owed (rule 17). Density on the day of writing: 11 total / 1 direct on the harness-fault conjunction; 54 on attribut… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-01 | Who wrote the last message: a harness-termination census of the human-labelled failure-attribution corpora | Step 1: $0, 0 GPU-h, 5 days; dead if pooled $h < 0.05$ (Wilson upper bound under 0.08) and both LongRCA and MAST under 0.05. | killed | killed ([record](../../../data/reports/2026-W46-kill-CL-W46-01.md)) |
| C-W46-02 | Re-scoring attribution on the runs an agent finished: Who&When accuracies with the 26 harness-terminated runs held out | Steps 0-1: $0, 3 days; dead if no released method moves by more than 2 points and the last-speaker baseline is flat across splits. | killed | killed ([record](../../../data/reports/2026-W46-kill-CL-W46-01.md)) |

## Kill search

### Concept level (CL-W46-01) — killed (2026-11-15)
The pre-registered kill fired on free data inside the kill search: LongRCA 0 of 1,140 provider-error terminations, Who&When 26 of 184 (the seed's number reproduced), MAST's human split carries no responsible-agent label; pooled h = 26/1,324 = 0.020, Wilson [0.013, 0.029], under the claim's own 0.05 line; the mechanism ('label on whoever spoke last') is false at step level (6 of 26) and the if_true action is the seed paper's own sec. 5 recommendation.
Full record: [`data/reports/2026-W46-kill-CL-W46-01.md`](../../../data/reports/2026-W46-kill-CL-W46-01.md).
**Occupied by:** 2611.13254
**Why not done before:** No reason found for the positive claim; the generalisation was not published because it is negative and empty — LongRCA's construction excludes infrastructure runs and records the harness as a named speaker with a termination reason, and MAST's human split has no agent labels to contaminate.
Closest neighbors (one-sentence trick; one-line difference):
- `2611.13254` Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors… — Read each failed run end to end and record where the wrong state entered and which control would have reached it; a deterministic string scan finds the provider content-filter crash in 26 of 58 hand-crafted Who&When runs with a harness-printed final answer. *Difference:* none — occupied: the mechanism, the 26/58 and 0/126, the 4/21 label split, the reading and the fix ('Attribution benchmarks should mark such runs') are in sec. 4.6 and 5; the quoted 'open-items list' is not in the paper
- `2608.15242` LongRCA Bench: Root-Cause Localization in Long-Horizon Agent Trajectories — Normalise 1,140 evaluator-confirmed failed runs from five sources into step-indexed records with recorded roles, have 22 annotators mark the responsible role and earliest decisive step, resolve disagreements by two experts. *Difference:* holds the corpus-side rule already: infrastructure runs excluded (sec. 3.2), harness a named speaker (Computer_terminal) with a termination reason in the last record; our scan: 0 of 1,140 provider-error terminations
- `2610.17747` Auditing Failure Attribution: Label Predictability and Judge Behavior — Four tests (input restriction, cue following, residual accuracy, aggregation) that ask whether an attribution score reflects a cross-step check or a surface cue; simple predictors match GPT-4.1 on three benchmarks. *Difference:* owns the validity-audit frame; no non-agent-termination category; scores 'only against the released annotations' — a harness row would be one line in its framework
- `2603.25001` Rethinking Failure Attribution in Multi-Agent Systems: A Multi-Perspective Benchmark and… — Three experts each mark every failure-inducing step on 289 runs; consensus rankings show prior 'LLMs struggle at attribution' conclusions are 'largely driven by limitations in existing benchmark designs'. *Difference:* owns 'Who&When's numbers are a benchmark-design artefact' with a different defect (deterministic single-step labels, 60% expert disagreement); no harness category
- `2505.00212` Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-… — Collect 184 failed runs from 127 systems, have humans mark the responsible agent and decisive step, score three attribution methods (53.5% agent, 14.2% step). *Difference:* the corpus; its release already carries a harness speaker label on the hand-crafted split ('Orchestrator (termination condition)', last message in 31 of 58 runs)
*Search degraded:* ['s2', 'exports', 'arxiv-api Q5 (HTTP 429 x3)', 'arxiv-api Q6 (HTTP 429 x3)', 'WebFetch longrca-bench.github.io (permission not answered; fetched with curl instead)']

### C-W46-01 — killed (2026-11-15)
A footnote, not a claim: the content-filter contamination is a Who&When hand-crafted artefact (one framework, one provider, 2025); LongRCA (0/1,140) and MAST's human split (no agent labels) are clean of it, and Who&When's own schema already names the harness speaker on 31 of 58 runs. Home: a comment to the authors of 2611.13254 and a note to the Who&When maintainers; the C-W46-02 remnant is agent-level accuracy on the 32 clean hand-crafted runs for any method with released predictions.
Full record: [`data/reports/2026-W46-kill-CL-W46-01.md`](../../../data/reports/2026-W46-kill-CL-W46-01.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2611.13254

### C-W46-02 — killed (2026-11-15)
A footnote, not a claim: the content-filter contamination is a Who&When hand-crafted artefact (one framework, one provider, 2025); LongRCA (0/1,140) and MAST's human split (no agent labels) are clean of it, and Who&When's own schema already names the harness speaker on 31 of 58 runs. Home: a comment to the authors of 2611.13254 and a note to the Who&When maintainers; the C-W46-02 remnant is agent-level accuracy on the 32 clean hand-crafted runs for any method with released predictions.
Full record: [`data/reports/2026-W46-kill-CL-W46-01.md`](../../../data/reports/2026-W46-kill-CL-W46-01.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2611.13254

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

- 2026-11-15 — claim open: born W46 claims stage, origin bottom-up (lifted from C-W46-01, C-W46-02 on card 2611.13254); first L1 claim since CL-W45-02; concept-level kill search owed before any probe is elaborated (rule 17)
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 3: born W46: $0 probe in 5 days, community-wide consumer (every failure-attribution corpus and method), durable procedure; Gate 2B risk (2611.13254 has the mechanism on one corpus) goes to the kill search; concept-level kill search runs this week (rule 17)
- 2026-11-15 — claim killed: concept-level kill search (data/reports/2026-W46-kill-CL-W46-01.md): killed — gate G0; The pre-registered kill fired on free data inside the kill search: LongRCA 0 of 1,140 provider-error terminations, Who&When 26 of 184 (the seed's number reproduced), MAST's human split carries no responsible-agent label; pooled h = 26/1,324 = 0.020, Wilson [0.013, 0.029], under the claim's own 0.05 line; the me…
- 2026-11-15 — claim killed: failing gate recorded after the W46 kill search: Gate 0 (premise: pooled harness-termination share 0.020 on 1,324 released runs, under the 0.05 kill line; MAST carries no responsible-agent label); Gate 2B, Gate 4, Gate 6 behind it
- 2026-11-15 — C-W46-01 killed: claim-level kill search of CL-W46-01 (data/reports/2026-W46-kill-CL-W46-01.md): killed — run inside the kill search on all 1,324 labelled runs; pooled h = 0.020, LongRCA 0/1,140; the pre-registered kill fired
- 2026-11-15 — C-W46-02 killed: claim-level kill search of CL-W46-01 (data/reports/2026-W46-kill-CL-W46-01.md): killed — premise false at step level (label = crash step in 6 of 26); the remnant (clean-split agent accuracy on 32 runs) is a footnote to the Who&When maintainers, not a probe of a live claim

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-01`, version 3)
- probe `C-W46-01`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-01.md`
- probe `C-W46-02`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-01.md`
