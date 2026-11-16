# On tau-bench airline under the Tool-Calling scaffold HAL ships, the same non-OpenAI model scores differently when its conversation reaches the provider through litellm's translation than through the provider's native SDK, by more than the five-run replicate interval, for at least one of Anthropic and Google.

`CL-W46-02` · lane **L1** · status **open** · rank 9 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none hard yet; Gate 6 not established; flag: the score clause is a judgment-0.35 surprise and the claim as written stands or falls on it (the loss share alone is a footnote to isloss). Next action: see First steps.

## The claim

- **Headline:** On tau-bench airline under the Tool-Calling scaffold HAL ships, the same non-OpenAI model scores differently when its conversation reaches the provider through litellm's translation than through the provider's native SDK, by more than the five-run replicate interval, for at least one of Anthropic and Google.
- **Current belief (the field's):** HAL 2602.16666 sec. 7 (quoted in data/reports/2026-W45-kill-CL-W45-01.md, fetched 2026-11-08): 'We evaluate each benchmark with a single well-performing scaffold'; sec. 4: 'For tau-bench, we use a tool-calling scaffold' and temperature 0 'so that any observed variance is attributable to non-sampling sources of stochasticity' — the request path is not among the sources named. tau-bench source (sierra-research/tau-bench, fetched 2026-11-15): the agent loop calls completion(messages=messages, model=self.model, custom_llm_provider=self.provider, tools=self.tools_info, temperature=self.temperature) with OpenAI-format 'role: tool' messages and truncates next_message['tool_calls'] to one. 2611.15543 (abstract): 'a translated request can be accepted by the target API while silently losing information about instruction roles, tool interactions, error states, or generation controls'; 127/685 (18.5%) of completed translations in its synthetic suite 'pass static target checks while silently changing prompt, role, or tool information in ways the target API could have preserved'.
- **If true:** Cross-provider leaderboard rows are not comparable without the translator version; leaderboards run native-SDK arms or a translator certified request by request, and disclose the path per row; the tau-family owners add a translation audit to the protocol; 'same scaffold' stops meaning 'same conversation' in harness disclosures — a change for every multi-provider leaderboard, so community-wide in reach if the gap is real.
- **If false:** litellm's translation of this harness's request shape is clean, or lossy without moving the score: the most-used multi-provider harness gets a certificate for these providers, the loss table is a footnote to isloss, and the lane stops asking.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.15543 ('These results establish conversation preservation as a distinct correctness requirement for ... agent execution, and model evaluation'); 2605.23950's call to disclose the harness; UniACE 2605.27898 ('a reported score reflects a complete model--harness--environment configuration ... tool protocols'). Who pays: HAL, Vals, Artificial Analysis and every leaderboard that routes several providers through one translator; tau-bench and tau2-bench owners; litellm's maintainers.
- **Impact ceiling:** **floor**: A per-provider loss table for the shipped tau-bench harness, cited by isloss v2 and by HAL's protocol section. Judgment p 0.6.; **middle**: HAL or the tau-bench owners add a translation-audit step (or native-SDK arms) to the protocol; one leaderboard discloses the translator version per row. Requires C-W46-04 to show a score effect. Judgment p 0.25.; **ceiling**: Conversation-preservation certificates become a standard column of cross-provider leaderboards, and the translation path is treated as part of the scaffold in every harness disclosure. Judgment p 0.1.
- **Relevance:** Narasimhan route (tau-family): direct — the harness is tau-bench's own. HAL route: direct — the protocol column. Evaluators: direct. Industry: direct for anyone running cross-provider evaluations through a gateway. Jacob's edge: software systems moderate; numerics and physics zero.
- **Kill probe:** Step 1: $0, 0 GPU-h, 4 days; dead if $L_p < 0.03$ on tool-bearing requests for every provider.
- **Density and ownership:** Occupant of the oracle and the synthetic-suite number: 2611.15543 (18.5% avoidable loss; 'translation-induced changes can alter model behaviour when tasks depend on the affected information' across six models). Adjacent: LLM-Rosetta 2604.09360 (a hub-and-spoke IR for cross-provider API translation), FailureAtlas 2607.17525 (taxonomy of multi-provider gateway failure modes), the harness-vs-model line (HarnessTax, 2609.11987, 2605.23950) which treats the scaffold as design, not dialect. Density of the translation-layer conjunction (LiteLLM / API translation / compatibility layer / gateway AND agent AND benchmark/evaluation): 33 total, 0 on a shipped leaderboard harness (fetched 2026-11-15). Role words for the kill search: translation, compatibility layer, gateway, provider dialect, request normalisation, tool_result, role mapping, OpenAI-compatible, ConvIR, SDK parity, harness disclosure,…
- **Why now:** The oracle (2026-11-11) and the fetched harness source (litellm in both parties' calls).
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass with one condition. Premise numbers: 18.5% avoidable loss (2611.15543, measured on a synthetic suite, 2026-11-11 — not yet on tau-bench, which is what C-W46-03 measures); about 9% hosted temperature-0 flips (2607.09691, single-shot SWE-bench, quoted from the W45 kill report); HAL K = 5 at temperature 0 on the Tool-Calling scaffold (2602.16666). Quantity: the score difference between two request paths for one model alias, random given the hosted stack's temperature-0 arithmetic and the user simulator's draws; both arms share the model, the tasks, the launch window and a user simulator pin… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass. C-W46-03 at $0 and four days kills the mechanism clause (loss share under 0.03); C-W46-04 at about $300 kills the score clause (gap inside the replicate floor). Both outcomes informative: a clean certificate for the shipped harness is a result the owners would cite. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B: the ruler (avoidable-loss share and the translation score gap) is identifiable from the shipped code and computable offline; pre-registered readings: expected (judgment 0.6) loss share at or above 0.10 on tool-bearing requests for at least one provider, and (judgment 0.35) a score gap beyond the replicate floor; the field assumes zero on both (same scaffold, same conversation; HAL's variance sources omit the request path); belief-changing if the gap clears the floor. Route A: isloss (paper), FailureAtlas (gateway failures from issue trackers and post-mortems), 2605.23950 and UniACE (… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Consumer classes with actions: leaderboard operators (native-SDK arms or a certified translator; translator version per row), benchmark owners (translation audit in the protocol), harness builders (the oracle as a CI check), labs quoting third-party rows (ask for the path). Community-wide reach if the gap is real, since every multi-provider leaderboard translates somewhere; proper if only the loss share survives. |
| G4 | mechanism and consequence | Mechanism: OpenAI-dialect tool messages ('role: tool', tool_call_id, name, parallel tool_calls truncated by the harness) are rewritten into Anthropic tool_use/tool_result blocks and Gemini functionResponse parts; fields with no target slot are dropped or merged (the oracle's role, tool-interaction and error-state categories), so the provider's model reads a different conversation from the one the harness logged and the auditor re-grades. Consequence: gap beyond the floor — native-SDK arms and disclosure become the rule; gap inside the floor — certificate and a documentation note. The two acti… |
| G5 | durability; lab-adjacent | Pass as a protocol check for any multi-provider harness; the specific loss shares expire with each litellm release (the number is consumed, the check is durable). Lab-adjacent: measurement of a shipped evaluation harness; not a frontier lab's core problem. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17). Density on the day of writing: 33 on the translation-layer conjunction, 0 on a shipped leaderboard harness. Occupants: 2611.15543 (oracle, synthetic suite, behaviour change on targeted tasks — the natural owners, who could run tau-bench in a week), LLM-Rosetta, FailureAtlas; the harness-as-design line (HarnessTax, 2609.11987, 2605.23950) and the serving-path line (2608.08239, 2607.09691) are adjacent, not occupying. Off-arXiv incumbents to check: litellm's issue tracker, provider OpenAI-compatibility test suites, HAL's protocol notes. Why… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-03 | The conversation the model saw: an offline isloss audit of tau-bench's litellm request stream per provider | Step 1: $0, 0 GPU-h, 4 days; dead if $L_p < 0.03$ on tool-bearing requests for every provider. | proposed | — |
| C-W46-04 | Native SDK versus litellm: the same model, the same tasks, two request paths on tau-bench airline | Step 1: about $300, 0 GPU-h, 5 days; dead if $\Delta$ and the pass^5 difference sit inside the within-arm replicate floor with no excess on flagged tasks. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-03** (Sunday run), or run `/kill C-W46-03` in a session.
2. If it survives: `/redteam C-W46-03`, then the probe as pre-registered — Step 1: $0, 0 GPU-h, 4 days; dead if $L_p < 0.03$ on tool-bearing requests for every provider.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (lane sentence + HAL's single-scaffold assumption; probes from seed 2611.15543 and the tau-bench source fetched 2026-11-15); concept-level kill search owed before any probe is elaborated (rule 17); the score clause is the claim — if the kill search finds the request-path gap measured on any agent benchmark, kill
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 9: born W46: judgment-0.35 surprise; the loss-share clause alone is a footnote to isloss; ranked last of the new claims; concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-02`, version 1)
- probe `C-W46-03`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-04`: `data/candidates/2026-W46.jsonl`
