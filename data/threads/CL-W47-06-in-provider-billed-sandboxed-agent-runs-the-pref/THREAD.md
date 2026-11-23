# In provider-billed sandboxed agent runs the prefix cache expires while the tools run: the realized cache-miss rate from tool-wait expiry is at least 0.2, which puts the effective cache price $c_{\mathrm{eff}} = c + m(1 - c)$ above the warm-cache crossover for 2611.22238's models, so keep-ten observation masking saves money under real billing at the list price where the warm-cache replay says it costs 87-116% more.

`CL-W47-06` · lane **L3** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G0 (premise: tool-wait gaps are seconds, not minutes), G2B (expiry is the field's stated and measured knowledge; no paper asserts a warm cache), G6 (occupied by 2608.00101, 2026-07-30; 2610.34817; SWE-agent #1482); the probe's pre-registered kill fired at step 0 inside the search. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** In provider-billed sandboxed agent runs the prefix cache expires while the tools run: the realized cache-miss rate from tool-wait expiry is at least 0.2, which puts the effective cache price $c_{\mathrm{eff}} = c + m(1 - c)$ above the warm-cache crossover for 2611.22238's models, so keep-ten observation masking saves money under real billing at the list price where the warm-cache replay says it costs 87-116% more.
- **Current belief (the field's):** 2611.22238 (card, full text) prices 20,000 coding-agent runs under an own-cache model that 'counts reuse of the previous prompt only' and 'does not model expiration or eviction' (sec. 2), with the limitation 'The cache accounting approximates within-run reuse and does not reproduce provider-specific expiration, write charges, breakpoints or load-dependent eviction'; its headline is that observation masking saving 19-25% undiscounted costs 87-116% more at a tenth-price cache; its evidence for warm caches is interactive production sessions ('cache reads are 94-98% of input tokens, against 95.6% in 8,058 Claude Code and Codex sessions', sec. 2), where gaps between requests are short. The C-W43-22 kill record (2026-10-25): CADOC 2609.37012, TokenPilot 2606.17016 and TurnCost 2610.15093 price context management under an assumed cache, none under measured expiry.
- **If true:** The sign of a context-management decision under API billing is set by how long the agent's tools take (the cache time-to-live against the test-suite wall clock), not by the price list; cost papers on agent context report the realized miss curve by inter-request gap beside the token count; harness builders choose masking versus keeping per benchmark by its tool latency distribution.
- **If false:** If the token-weighted miss rate $m < 0.10$ on every HAL benchmark's cache-active runs with no step at the time-to-live and the billed masked-to-unmasked ratio stays above 1 in both sleep conditions: the realized cache is the warm cache even in sandboxed harnesses, $c_{\mathrm{eff}} = c$, the card's flip holds under billing, and the record is a footnote confirming it with provider fields.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card's own limitation (quoted above) and its App. O checklist; TraceLab's 95.6% as the production number the card validates against; the serving-side eviction-during-tool-wait literature (Continuum, MORI, 2610.22863, per the CL-W43-12 record). Who pays: teams choosing masking, summarization or digests under API billing; authors of context-management methods (every one of the card's six re-ranks with the price); providers setting time-to-live defaults.
- **Impact ceiling:** **floor**: The miss curve by gap and the $c^*_m$ table, cited by the card's v2 and by the next context-management paper. Requires steps 0-1. Judgment 0.5.; **middle**: The break-even rule with $c_{\mathrm{eff}}$ adopted by one context-management method, and realized hit share reported beside the price vector in one benchmark's cost table. Requires step 2. Judgment 0.25.; **ceiling**: Realized cache state becomes a reported axis of every agent cost result (price vector and miss rate), and the two published signs for masking are read as two cache states. Requires a second provider and a second scaffold. Judgment 0.1.
- **Relevance:** Systems route (Lloyd / Netravali / Tri Dao): direct, cache residency across tool waits is the true cost structure of agentic workloads. L4: direct, a lossy message priced under the realized cache. Narasimhan route: zero. HAL route: indirect (the archive). Industry: direct. Jacob's edge: the crossover algebra is a two-line identity he can check; GPU numerics zero.
- **Kill probe:** Steps 0-1: $0, 0 GPU-h, 3 days; dead if $m < 0.10$ everywhere with no time-to-live step; step 2 about $300 and 3 days as the manipulation check.
- **Density and ownership:** Not searched this session (brief: no fetching). From this repo's records: C-W43-22 (re-price context management under cache billing) was killed 2026-10-25 by CADOC 2609.37012 (the general trim-versus-keep break-even for an edit inside a cached prefix, replayed over 50 SWE-bench Verified histories at five cache-read weights, batched commit as the fix), TokenPilot 2606.17016 (provider-counted Keep-Last-N cheaper than full history in 4 of 4 cells at a cache ratio of 0.1) and TurnCost 2610.15093 (a re-scoring tool under alternative caching and pricing); per those records none carries a realized-miss or time-to-live term, and CADOC's break-even is the warm-cache one. Serving-side occupants of the mechanism: Continuum (time-to-live pinning for tool-calling requests), MORI (idle-window tiering on Claude Code traces), 2610.22863 (63% of calls recompute under LRU at a tenth of peak). The card's…
- **Why now:** 2611.22238 (2026-11-17) states the missing term in its own limitations; 2611.21515 (2026-11-16) shows the provider-reported cache fields exist per call in a public archive; the eviction-during-tool-wait mechanism is in print on the serving side (2025-11 to 2026-10) without a billing consequence.
- **Register, and what it is not:** Measurement with a recipe consequence (the break-even takes $c_{\mathrm{eff}}$) and a reconciliation of two published signs. It is not a new masking policy, not the card's replay on another benchmark, and not a serving-system design.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched (87-116% more at a tenth-price cache; 19-25% undiscounted saving; 94-98% cache reads; $c \in [0.025, 0.1]$, $p \in [4, 6]$ price lists accessed 2026-10-22 — card secs. 2, 5, Table 7). Conditioning set: the miss rate is a property of the (provider time-to-live, tool wall clock, harness concurrency) triple — a protocol quantity, named in the headline as 'provider-billed sandboxed runs'; the agent's draw enters only through tool durations. The identity is checked against every number in the record (checklist 2026-11-08): at $c = 0.1$ the restoring miss rate… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: steps 0-1 are $0 and three days on the HAL archive; step 2 about $300 of API, no GPU. Kill written; both outcomes informative (the first measured expiry curve for agent runs either way). Unverified premise marked 'inference' in the probe: per-call timestamps in HAL's logs; provider time-to-live values. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route A pressure (two source types quoted in the card: the paper's own limitation on expiration; provider pricing pages with cache time-to-live) and Route B (the effective cache price as a ruler). Surprise three ways: expected $m \geq 0.2$, sign flips at the list price (judgment 0.4); field assumes a warm cache (card sec. 2; production-session statistics); belief-changing $m < 0.10$ everywhere (0.35) or $m$ large with no sign flip because $x$ is small (0.25). Flag for the kill search: the serving community's words (TTL, eviction, prefix cache hit rate under idle, session gap, cache warming, k… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: cost-accounting papers (report the realized miss curve), harness builders (masking by tool latency), serving-system designers (TTL as a cost lever for agents), the L3 cost-structure thread. Proper-shaped; systems register. |
| G4 | mechanism and consequence | Mechanism: a tool call that outlasts the cache time-to-live forces a full re-prefill at the uncached price; the input bill per prompt token is $1 - (1 - c)h$ with $h = 1 - m$, so the masking crossover $c^*$ moves with $m$ and crosses the list price once $m$ exceeds the warm-cache crossover; keep-ten masking shortens the re-prefilled prefix on every miss. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the expiry term exists for every provider with a time-to-live; flag — time-to-live values and prices change by release; the probe's step 2 re-runs per price sheet. |
| G6 | ownership, density, race window; position clause | Density owed at the kill search in the serving community's words (time-to-live, TTL, idle, eviction, hit rate, session gap, cache warming, as-billed, invoice, prompt caching) and the cost-accounting words (TokenPilot, TurnCost, CADOC vocabulary: commit, batch, as served). Why now: HAL per-call cache fields and 2611.22238's cost model (November 2026); provider TTLs of 5 minutes documented on pricing pages (to be fetched). Race: L3 cost papers about one a week; 2611.08902 was a four-day concurrent twin last time — the concurrent-twin query runs first. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-02 | The effective cache price: realized provider misses during tool waits and the sign of observation masking | Steps 0-1: $0, 0 GPU-h, 3 days; dead if $m < 0.10$ everywhere with no time-to-live step; step 2 about $300 and 3 days as the manipulation check. | killed | — |

## Kill search

### Concept level (CL-W47-06) — killed (2026-11-22)
On HAL's cache-active archives the realized expiry miss rate is 0.000 (SWE-agent/Opus 4.1, 2,333 requests, gaps p99 6.8 s) and 0.0085 (Generalist/o3-mini, p99 69 s), the probe's own kill; 2608.00101 measured the miss curve by gap, the 5-minute step, the 0.1 bill and a keep-alive fix on 5.7 billion production calls in July 2026, with intra-turn KV idle at P95 38 s.
Full record: [`/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-06.md`](../../..//home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-06.md).
**Occupied by:** 2608.00101 (the realized hit rate versus inter-request gap, the 5-minute step 'consistent with time-based KV-cache eviction', the cache-read bill at 0.1 and the harness keep-alive saving 14.9% at turn boundaries; intra-turn gaps P50 1.2 s / P95 38 s); 2610.34817 (the misconfiguration channel: 108 of 120 prompt-caching defects silent, extra spend the only trace); SWE-agent issue #1482 (2026-07-28:…
**Why not done before:** It was done where it is non-trivial: at human turn boundaries by the group holding production traces (2608.00101). Inside autonomous tool loops the miss curve is a line at zero because sandbox tool calls return in seconds (SWE-bench Verified Mini p99 6.8 s; CORE-bench 1.5% of requests past 300 s). The one live channel (a harness that never requests caching: HAL Core Agent, 0 cached tokens on 1,553 calls) is a published bug class with a detector, not a cost law. The enabling pieces (HAL per-call timestamps and usage fields) have existed since April 2025.
Closest neighbors (one-sentence trick; one-line difference):
- `2608.00101` Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale (202… — Sample 5.7 billion production coding-agent calls, show the prefix-cache hit rate falls with the gap between calls at the provider's five-minute TTL, and send a dummy refresh when the predicted gap exceeds the TTL to cut token cost 14.9% at turn boundaries. *Difference:* none for the ruler and the consequence - occupied; it adds that the gaps crossing the TTL are the human's (cross-turn median 160 s) while intra-turn KV idle is P50 1.2 s / P95 38 s and within-turn hit rate is 90%
- `2610.34817` Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Age… — Mine 120 prompt-caching pull requests from 10 agent systems, classify request-side misconfiguration and read-side miscount, show 108 fail silently as extra spend, and ship a static checker with a dated provider-capability oracle. *Difference:* owns the channel by which a harness's realized cache differs from the price list (the HAL Core Agent archive with zero cache_control is its Table II in the wild); no TTL curve, no masking sign
- `2611.22238` Context Has a Price (the seed, 2026-11-17) — Bill 20,000 vLLM runs as U + cC + pO with own-cache hits and show keep-ten masking flips from -19-25% at c = 1 to +87-116% at c = 0.1. *Difference:* names expiration as unmodelled in its own limitations; the claim's 'field assumes a warm cache' is the seed's stated limitation
- `2610.15093` TurnCost (2026-10-10) — Re-score 600 released trajectories under an exact append-only cache: 98.6% of input tokens hit. *Difference:* states the TTL eviction as known and unmodelled ('evict them after a time-to-live ... none of which we model')
- `2511.02230` Continuum (2025-11-04) — Pin a tool-calling request's KV for a time-to-live set from reload cost and queueing delay. *Difference:* the TTL as a serving lever with the premise that tool calls are short; no billing
*Search degraded:* ['s2', "arXiv API Q6 (claim's own words): Rate exceeded x2", 'arXiv API Q7 (prompt caching x expiry, all time): Rate exceeded x4 over 25 min; arxiv.org HTML search also Rate exceeded', 'WebFetch of docs.anthropic.com and platform.openai.com blocked by fetch permission (platform.claude.com and devel…

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

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): one probe from card 2611.22238; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-06.md): killed — gate G0 (premise: tool-wait gaps are seconds, not minutes), G2B (expiry is the field's stated and measured knowledge; no paper asserts a warm cache), G6 (occupied by 2608.00101, 2026-07-30; 2610.34817; SWE-agent #1482); the probe's pre-registered kill fired at step 0 inside the search; On HAL'…
- 2026-11-22 — C-W47-02 killed: W47 concept-level kill search of CL-W47-06: probe verdict killed. Step 0 ran at $0: m = 0.000 and 0.0085 on the two cache-active HAL archives with no request near the TTL (pre-registered kill met); step 1 moot (c*_m = 0.546 vs 0.55); step 2 already run by SWE-agent #1482 for the mechanism. Do not run.

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-06`, version 2)
- probe `C-W47-02`: `data/candidates/2026-W47.jsonl`
