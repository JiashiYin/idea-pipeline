# In asynchronous agentic RL the binding resource of a training iteration is KV-cache residency, not decode compute, and the waste terms systems papers list do not add.

`CL-W43-12` · lane **L3** · status **open** · rank 5 · position both · refreshed 2026-10-30

## Status

Open claim. Every probe under it has been killed; the claim needs a new probe or dies. Failing gate: Gate 1 blocked on paperwork (the only live probe, import S6xF7, has no scorecard); Gate 6 open for the training half. Grade on paper: open, narrowed to the training half; scorecard for import S6xF7's pass A ($0) owed, then kill search. Next action: see First steps.

## The claim

- **Headline:** In asynchronous agentic RL the binding resource of a training iteration is KV-cache residency, not decode compute, and the waste terms systems papers list do not add.
- **Current belief (the field's):** Systems papers quote throughput in output tokens per second per GPU and list waste terms as if they add (FlashNext-RL 2610.28998: 26% zero-advantage rollouts discarded, a third of sessions idle on sandbox commands, trainer waiting 25%); context-management papers report savings as token counts (observation masking, sliding windows), while 2610.26632 found dropping turns cost 2.9-4.0x the dollars at 0.84-0.90x the tokens because it broke prefix caching.
- **If true:** Every agentic-RL systems paper reports a per-station demand table and names the binding station; KV release during tool waits becomes a predicted 25-35% iteration-time lever; trainer kernel work past the balance point is shown futile
- **If false:** Decode compute binds (utilization >= 0.85 with KV below cap) and KV release moves iteration time under 5%: token accounting is adequate and the lane's cost instrument is Little's law applied once

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: AKV (per its card) states KV-cache reads are 82.4% of API cost and that a text trim costs 1.85x, against the Complexity Trap's 'halves cost' and 2609.20804's efficiency ranking: a contradiction between three papers on one operation. Who pays: every harness team choosing a context-management default on a cache-priced API, every paper reporting an agent cost column, and the systems groups (AKV, TokenPilot, SmoothAgent) whose motivation this quantifies.
- **Impact ceiling:** **floor**: The identity plus a table showing the reversal is confined to windows under ~50k tokens; a footnote the systems papers cite for their motivation; requires steps 1-3; probability 0.35 (judgment).; **middle**: Published masking savings flip sign at $r \le 0.25$ on SWE-bench lengths and boundary-batched masking recovers them; a re-pricing note adopted as the cost-reporting standard in L4 evaluations and a default change in two harnesses; requires steps 1-3; probability 0.45 (judgment).; **ceiling**: The break-even curve $s = r + \delta$ becomes the standard cost ruler across providers and policies, with a measured accuracy-versus-computed-prefill frontier replacing token-count frontiers in the lane; requires a second benchmark (BrowseComp-Plus) and accuracy arms (another ~60 GPU-hours); probability 0.2 (judgment).
- **Relevance:** **routes**: L3 route (Lloyd / Netravali / Tri Dao: cost structure of agentic serving, prefix-cache reuse); L4 (every compaction evaluation's cost column); L1 (cost-per-task accounting on leaderboards).; **industry**: Direct: harness defaults, provider pricing pages, and the cost claims in agent-framework READMEs.; **jacobs_edge**: High for this lane: a conservation-style identity, GPU prefill arithmetic, and cache-hit measurement on a serving stack.; **zero_where**: L5 and L2; nothing about what trimming does to accuracy, which is deliberately held out of this probe.
- **Kill probe:** Step 1 analytic re-pricing on released trajectories ($0, 2 days); step 2 replay of 50 SWE-bench trajectories x 5 policies on SGLang with prefix caching, 30 GPU-hours, ~$100, 4 days; kills if per-turn masking computes fewer prefill tokens than full history on most turns at $r \le 0.25$ and the published savings keep their sign; 7 days in all.
- **Density and ownership:** From the cards: AKV 2610.28577 (server-side drop/reposition, the 1.85x motivation number, 82.4% KV-read share), TokenPilot 2606.17016 (batched eviction to keep prefixes stable: the text-level fix our fifth arm is), SmoothAgent 2607.00151 (precompute the trimmed prefix in the background), Context Language Models 2609.37725 (suffix-cache reuse after text edits), the Complexity Trap 2508.21433 (the 'halves cost' claim), 2609.20804 (176 settings, efficiency ranking), card 2610.26632 (the measured 2.9-4.0x reversal). The systems papers know the mechanism and build around it; none re-prices the measurement lane's published results or states the break-even identity. The kill search counts 12 months with the neighbours' words (prefix cache, cache hit, invalidation, re-prefill, context management, observation masking, cost) and reads how the Complexity Trap and 2609.20804 computed cost before an…
- **Why now:** Card 2610.26632 (October 2026) and AKV (October 2026) each report the reversal independently in the same month against the Complexity Trap's August 2025 halving; provider cache pricing with large discounts is the enabling piece, and open servers with radix prefix caching (SGLang, per AKV's regime) make the computed-prefill count measurable without provider logs.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe import:2026-W43-S6xF7 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a systems paper's own non-additive waste list (2610.28998), a harness paper's own dollars-vs-tokens inversion (2610.26632), and the serving literature's cached-input price tiers (three independent source types); route B: the import supplies the ruler (demand per station, utilization law) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: systems authors (demand table), context-management authors (dollar sign of savings), billing comparisons on leaderboards (cached-input column), RL infra teams (KV release during tool waits) |
| G4 | mechanism and consequence | pass: mechanism — sessions holding KV while waiting on tools consume the binding resource; trimming forces re-prefill at the uncached price; consequence — park KV during tool waits, keep history until the break-even ratio |
| G5 | durability; lab-adjacent | pass: operational laws hold for any stack; the specific break-even depends on provider prices, which change |
| G6 | ownership, density, race window; position clause | serving half refuted as news (CADOC 2609.37012 eq. 2 states the trim-vs-keep break-even and measures the token-vs-dollar reversal; TokenPilot 2606.17016 Tables 1-2 and Fig. 6; TurnCost 2610.15093 re-scores public trajectories under cache pricing; 2607.12161 'Token Reduction Is Not Cost Reduction'; 2610.22863 M365 traces with 80% of context tokens cached); the training-iteration half is unmade across 3 queries (14, 89, 12 hits) per import S6xF7; four papers on cache-aware context cost in six weeks — race window short on the serving side, open on the training side |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-22 | Re-price context management under prefix-cache billing: when does trimming cost more than keeping everything | Step 1 analytic re-pricing on released trajectories ($0, 2 days); step 2 replay of 50 SWE-bench trajectories x 5 policies on SGLang with prefix caching, 30 GPU-hours, ~$100, 4 days; kills if per-turn masking computes fewer prefill tokens t… | killed | killed |

Also under this claim (no scorecard yet): import:2026-W43-S6xF7 (pass A: $0, one day, operational analysis of FlashNext-RL's published numbers; pass B: instrumented 8-GPU stack with KV release during t…

## Kill search

### C-W43-22 — killed (2026-10-25)
CADOC (2609.37012) states the general trim-versus-keep break-even for an edit inside a cached prefix, measures the token-versus-dollar reversal on real agent histories, replays 50 SWE-bench Verified histories under ten commit policies at five cache-read weights and ships batched commit as the fix; TurnCost (2610.15093) released the re-scoring tool for public coding-agent trajectories under alternative caching and pricing; and the headline that published sliding-window savings carry the wrong sign is contradicted by TokenPilot's provider-counted tables (Keep-Last-N cheaper than full history, 4 of 4 cells, $r = 0.1$) and by the Complexity Trap's own appendix (API-returned, cache-priced cost). The candidate's identity is also mis-specified for rolling windows (the trimmed history is a stable prefix; only the window is recomputed).
Per position — **solo**: killed — occupied by CADOC and TurnCost; the headline is a published negative (TokenPilot, Complexity Trap App. A); density about two papers per week against a one-week probe.; **lab**: killed — a lab position adds provider-side cache logs, which 2610.22863 (M365, 121M calls) and 2607.12161 (2,848 provider-billed runs) already publish; nothing in the probe needs an owned artifact, and the identity is i…
**Why not done before:** It has been done, in three pieces inside the window: CADOC (2026-09-29) wrote the condition and replayed SWE-bench histories under it; TurnCost (2026-10-10) released the re-scoring tool for public coding-agent corpora under alternative caching and pricing; TokenPilot (2026-06-15) and 2607.12161 (2026-07-13) published provider-billed dollar comparisons of trimming against full history with cache-hit counts, one with each sign. The enabling piece was provider cached-input pricing with large discounts (OpenAI/Anthropic/Google, 2024-2025) plus released trajectory corpora (Complexity Trap 2025-08; Open-SWE-Traces 2606.16038, 2026-06), and the field used it within months.
**Occupied by:** 2609.37012 (CADOC): the per-edit break-even identity, the measured token-versus-dollar reversal on real agent histories, the replay of 50 SWE-bench Verified histories under ten trim-commit policies at five cache-read weights, and the batched-commit fix. The headline 'published sliding-window saving…
Closest neighbors (one-sentence trick; one-line difference):
- `2609.37012` CADOC: Cache-Aware Dynamic Object Context for Long-Horizon Agents — Replace old structured objects in the history with short retrievable cards, but commit the replacements in batches timed by an economic-order-quantity rule so that the cached suffix is rebuilt once per batch instead of once per edit. *Difference:* none — occupied: its eq. 2 is the general per-edit break-even, $\Delta\mathcal{C}_{\text{first}} = (1-w_r)(I-G) + F - w_r G$ with $I$ the cached tokens from the first edit to the cache frontier, $G$ the tokens removed and $w_r$ the cached-to-uncached price ra…
- `2610.15093` TurnCost: Turns, Not Observations: Cache-Aware Loop Engineering for Coding Agents — Re-score 600 released coding-agent trajectories under an exact prefix-cache simulation and show that 98.6% of input tokens are cache hits, so flat input pricing overstates loop cost about 7x and the break-even for delegating an observation to a cheap model is… *Difference:* The candidate's step 1 (re-price released coding-agent trajectories under cached-input pricing, report the sign of published savings per price ratio, release a re-scoring tool) is this paper's contribution and released tool, with the pricing normalised to rat…
- `2606.17016` TokenPilot: Cache-Efficient Context Management for LLM Agents — Stabilise the prompt prefix at ingestion (static placeholders for paths, timestamps and tool schemas; rule-based trimming of tool results before they enter the history) and evict expired segments only every B turns, so text shrinks without moving the cache ed… *Difference:* Published negative for the candidate's headline: with provider-reported cache-hit and cache-miss token counts and GPT-5.4-mini prices ($p_{\text{hit}} = 0.075$, $p_{\text{miss}} = 0.75$ per million, $r = 0.1$), the fixed-window Keep-Last-N baseline is cheaper…
- `2607.12161` Token Reduction Is Not Cost Reduction — Run three tool-output compressors against unmodified Claude Code on 2,848 paired provider-billed runs and show that removing 38.4% of delivered tool tokens raised the bill 6.8%, because cache creation and cache reads are about 87% of cost and compression chan… *Difference:* The claim's headline sentence is this paper's title, measured on provider bills; its mechanism is trajectory change plus cache-write pricing at ingestion-time compression, not the moving edit point of per-turn trimming, and it states a per-token marginal mode…
- `2508.21433` The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for… — Replace environment observations older than the last M = 10 turns with a placeholder and compare against LLM summarisation on SWE-bench Verified; masking halves cost against the raw agent at equal solve rate. *Difference:* The candidate's premise that this paper's cost column is a token count is false: Appendix A says the Gemini cost is 'the cost returned by the API' (Vertex AI, cache-priced) and the Qwen3-Coder cost uses Alibaba pricing that distinguishes cache hit and miss (o…
**Probe as pre-registered (checked):** Restated: step 1 re-prices released trajectories under $D^{\text{trim}}_t / D^{\text{full}}_t = s_t / (r + \delta_t)$ at $r \in \{0.1, 0.25, 0.5\}$ ($0, public data: Complexity Trap HF tarballs, 500 SWE-agent tasks per arm; TurnCost's Zenodo tool); step 2 replays 50 SWE-bench Verified trajectories x 5 policies on SGLang logging computed prefill (30 GPU-h, ~$100); step 3 the break-even table. Cost 30 GPU-h is under one GPU-week. Two defects. (a) Gate 0: the identity assumes the trimmed prefix is never cached; for a rolling window the masked history is itself a stable prefix and only the window is recomputed, so the recomputed interval is $I$ = (edit point to cache frontier), exactly CADOC's…
*Search degraded:* ['s2 skipped (no key)', 'exports: not built', 'complaints: skipped (no GitHub access)']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **import:2026-W43-S6xF7** (Sunday run), or run `/kill import:2026-W43-S6xF7` in a session.
2. If it survives: `/redteam import:2026-W43-S6xF7`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written top-down by the closing-W43 claims run (L3's cost sentence; the field's own accounting quoted); import S6xF7 and C-W43-22 attached
- 2026-10-25 — claim open: kill run (closing W43): C-W43-22 killed; headline narrowed to the training half (one claim per sentence); previous headline kept in previous_headline; rank 3 -> 5
- 2026-10-25 — C-W43-22 killed: kill search (stage 4, automatic, claim-ranked): killed — CADOC (2609.37012) states the general trim-versus-keep break-even for an edit inside a cached prefix, measures the token-versus-dollar reversal on real agent histories, replays 50 SWE-bench Verified histories under ten commit policies at five cache-read weights and ships batched commit as the fix; TurnCost (2610.15093) released the re-scori…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-12`, version 2)
- probe `C-W43-22`: `data/candidates/2026-W43.jsonl`
