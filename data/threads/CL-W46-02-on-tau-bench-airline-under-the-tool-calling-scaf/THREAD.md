# On tau-bench airline under the Tool-Calling scaffold HAL ships, the same non-OpenAI model scores differently when its conversation reaches the provider through litellm's translation than through the provider's native SDK, by more than the five-run replicate interval, for at least one of Anthropic and Google.

`CL-W46-02` · lane **L1** · status **killed** · rank None · position both · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: Gate 2B (isloss 2611.15543 sec. 7.1 states the thesis and announces the measurement); Gate 6 (race against the owners); Gate 0 defect (Gemini reaches Google through litellm's OpenAI path). Next action: see First steps.

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
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W46-02.md): killed; gate failed G2B; occupied_by 2611.15543; why not done: The owners said they are doing it: isloss (2026-11-11) names tau-bench, LiteLLM and 'changes in published benchmark scores or leaderboard rankings' as its future work; 2609.03966 already runs the interface-only contrast on tau-bench retail; the one hosted native-SDK vs third-party same-model contrast in print (HarnessTax 2609.11987, n=80) is null on average.. Previous: Unmeasured: concept-level kill search owed (rule 17). Density on the day of writing:… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-03 | The conversation the model saw: an offline isloss audit of tau-bench's litellm request stream per provider | Step 1: $0, 0 GPU-h, 4 days; dead if $L_p < 0.03$ on tool-bearing requests for every provider. | killed | killed ([record](../../../data/reports/2026-W46-kill-CL-W46-02.md)) |
| C-W46-04 | Native SDK versus litellm: the same model, the same tasks, two request paths on tau-bench airline | Step 1: about $300, 0 GPU-h, 5 days; dead if $\Delta$ and the pass^5 difference sit inside the within-arm replicate floor with no excess on flagged tasks. | killed | killed ([record](../../../data/reports/2026-W46-kill-CL-W46-02.md)) |

## Kill search

### Concept level (CL-W46-02) — killed (2026-11-15)
The surprise (the request path moves a leaderboard score) is the seed paper's stated thesis and announced future work with tau-bench and LiteLLM named (isloss 2611.15543 sec. 7.1), the interface-moves-the-score result is in print (2609.03966, 2609.08861, 2605.27898, 2611.06116), the oracle's owners hold the measurement (Gate 6), and the Google clause names litellm as the translator when HAL's shipped path is Google's server-side OpenAI-compatible endpoint (Gate 0).
Full record: [`data/reports/2026-W46-kill-CL-W46-02.md`](../../../data/reports/2026-W46-kill-CL-W46-02.md).
**Occupied by:** 2611.15543
**Why not done before:** The owners said they are doing it: isloss (2026-11-11) names tau-bench, LiteLLM and 'changes in published benchmark scores or leaderboard rankings' as its future work; 2609.03966 already runs the interface-only contrast on tau-bench retail; the one hosted native-SDK vs third-party same-model contrast in print (HarnessTax 2609.11987, n=80) is null on average.
Closest neighbors (one-sentence trick; one-line difference):
- `2611.15543` Testing Conversation Preservation Across LLM APIs: A Rule-Based Oracle for Detecting Sile… — Map a request and its translation to one shared representation and apply written rules to flag information the target format could have kept but the translation dropped, with no model calls and no reference translation. *Difference:* none — occupied: the thesis (translation confounds evaluation; tau-bench and LiteLLM named) and the mechanism are its own; the score measurement is its announced future work
- `2609.03966` Interface-Induced Trajectory Censoring: When Tool-Call Interfaces Distort Evaluation and… — Hold the weights fixed and change only the serving stack's chat template and tool-call parser; count emitted, parsed and executed calls and the score at each layer. *Difference:* Same-model interface-only contrast on BFCL (0.00 to 0.96) with a 115-task tau-bench retail extension, on self-hosted vLLM and open-weight models; the claim's hosted-provider request translation is a different layer, and the remedy (versioned model–interface m…
- `2609.08861` API Benchmark Scores Do Not Reliably Transfer to Chatbot Interfaces — Run nine benchmarks through the API and through the chat interface of the same deployed model and difference the two. *Difference:* Access surface (UI vs API) on hosted ChatGPT, Claude and Gemini: 3.4 points on average, rivalling a model generation; no translator arm and no tool-calling loop
- `2609.11987` Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Con… — Run the same model through the vendor's native agent SDK and through a neutral third-party harness, paired by task on a private suite. *Difference:* The only hosted native-SDK vs third-party same-model contrast in print (claude-agent-sdk vs deepagents on claude-opus-4-8: -1.25 pp, CI [-10.0, +7.5]); varies the whole harness, not the request path alone; null on average
- `2604.21083` Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways — Send fixed probes to a commercial gateway and to the vendor's official API and compare response signatures, multi-turn retention, billing and latency. *Difference:* Native-API vs intermediary two-arm audit on ten commercial gateways (model substitution, silent truncation); not translation of tool-bearing requests, no benchmark score
*Search degraded:* ['s2', 'arxiv-api (2 queries answered, Q1 and Q2; about 15 further requests over 40 minutes returned 429/503 under ten parallel agents; HTML advanced search used for the rest)', 'conference exports not built', 'api.github.com and github.com tree page blocked (raw.githubusercontent.com and a blobles…

### C-W46-03 — killed (2026-11-15)
A footnote-sized service: an offline isloss run over HAL's Anthropic request stream at HAL's litellm version with drop_params=True, reported to litellm and HAL as a note (and, from the HAL position, a translator-version column in the run manifest). Not a claim; the end-to-end score measurement belongs to the isloss authors, who announced it.
Full record: [`data/reports/2026-W46-kill-CL-W46-02.md`](../../../data/reports/2026-W46-kill-CL-W46-02.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2611.15543

### C-W46-04 — killed (2026-11-15)
A footnote-sized service: an offline isloss run over HAL's Anthropic request stream at HAL's litellm version with drop_params=True, reported to litellm and HAL as a note (and, from the HAL position, a translator-version column in the run manifest). Not a claim; the end-to-end score measurement belongs to the isloss authors, who announced it.
Full record: [`data/reports/2026-W46-kill-CL-W46-02.md`](../../../data/reports/2026-W46-kill-CL-W46-02.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2611.15543

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

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (lane sentence + HAL's single-scaffold assumption; probes from seed 2611.15543 and the tau-bench source fetched 2026-11-15); concept-level kill search owed before any probe is elaborated (rule 17); the score clause is the claim — if the kill search finds the request-path gap measured on any agent benchmark, kill
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 9: born W46: judgment-0.35 surprise; the loss-share clause alone is a footnote to isloss; ranked last of the new claims; concept-level kill search runs this week (rule 17)
- 2026-11-15 — claim killed: concept-level kill search (data/reports/2026-W46-kill-CL-W46-02.md): killed — gate G2B; The surprise (the request path moves a leaderboard score) is the seed paper's stated thesis and announced future work with tau-bench and LiteLLM named (isloss 2611.15543 sec. 7.1), the interface-moves-the-score result is in print (2609.03966, 2609.08861, 2605.27898, 2611.06116), the oracle's owners hold the me…
- 2026-11-15 — claim killed: failing gate recorded after the W46 kill search: Gate 2B (isloss 2611.15543 sec. 7.1 states the thesis and announces the measurement); Gate 6 (race against the owners); Gate 0 defect (Gemini reaches Google through litellm's OpenAI path)
- 2026-11-15 — C-W46-03 killed: claim-level kill search of CL-W46-02 (data/reports/2026-W46-kill-CL-W46-02.md): killed — The Google arm cannot be audited offline (server-side translation at Google's OpenAI-compatible endpoint); the Anthropic arm is a service to isloss and HAL (a loss table for one translator version), a footnote, not a probe of a live claim.
- 2026-11-15 — C-W46-04 killed: claim-level kill search of CL-W46-02 (data/reports/2026-W46-kill-CL-W46-02.md): killed — Gated on C-W46-03; its shipped arm is not shipped once the user simulator is pinned and the litellm version chosen; the one hosted native-SDK vs third-party same-model contrast in print (HarnessTax, n=80) is null on average, so the pre-registered kill is the expected outcome.

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-02`, version 3)
- probe `C-W46-03`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-02.md`
- probe `C-W46-04`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-02.md`
