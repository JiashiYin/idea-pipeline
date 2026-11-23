# On the HAL leaderboard the cost axis of the accuracy-cost frontier is as unresolved as its accuracy axis: once a run's dollar cost carries its uncertainty budget (the agent's draw, the serving cache state, the accounting rule, the price sheet in force), at least 12 of the 35 frontier steps are compatible on cost at $k = 2$, and the cache-state row alone, not the replicate row, sets the floor.

`CL-W47-01` · lane **L1** · status **killed** · rank — · position both · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G0 (premise: the cache-state row is a scaffold constant on HAL, not a draw; the accounting row is a factor-2 blunder, not a bias) with the claim's own if_false branch (Gate 2B) realized at $0 on the archive it names. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** On the HAL leaderboard the cost axis of the accuracy-cost frontier is as unresolved as its accuracy axis: once a run's dollar cost carries its uncertainty budget (the agent's draw, the serving cache state, the accounting rule, the price sheet in force), at least 12 of the 35 frontier steps are compatible on cost at $k = 2$, and the cache-state row alone, not the replicate row, sets the floor.
- **Current belief (the field's):** 2611.21515 (card, full text) treats cost as exact and accuracy as uncertain: 'Our reconstructed costs represent API token spend only; they exclude hosting, external tools, and human-review costs' (sec. III-B); the statistical machinery (paired tests, 27 of 35 steps unresolved) is applied to accuracy only, and sec. VIII asks that costs be 'reported separately, with task-level token usage, cache accounting, and model pricing preserved for reproducibility'. 2611.22238 (card, full text) measures the cache rows one at a time — 'cache reads are 94-98% of input tokens', warmed caches move bills '+8% to +36%', the accounting 'does not model expiration or eviction' — and sums none of them. The killed CL-W43-14 record (2026-11-02) priced the replicate row of cost at 4-9% and called it a service: that row is the one the field already knows.
- **If true:** The cost column of every agent leaderboard (HAL, SWE-rebench cached column, Artificial Analysis effort variants) carries an uncertainty budget beside the number, as the accuracy column carries an interval; 'cheaper at equal accuracy' claims in agent papers state the cache condition and price sheet they were priced under; HAL's selection rule (2611.21515's $Q$) gains a cost interval and stops crediting bargains inside the floor; the resolvable cost ratio (about 1.5x at a tenth-price cache, the geometric step of the SWE-bench Mini frontier) becomes the unit of a cost comparison.
- **If false:** If the Type A (replicate) row dominates $u_c^2$: replicates fix the cost column and the CL-W43-14 service verdict stands with a number. If $u_{c,r} < 0.10$ after the gross-error audit: cost is exact enough at the frontier's step size and 2611.21515's 11.7x double-counting audit is the whole story; the budget is a reporting template, a footnote.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: card 2611.21515 sec. VII, 'Reconstructed costs rely on standardized pricing, cache-allocation assumptions, and occasional imputation.' and sec. VIII's call for cache accounting preserved beside task-level token usage; card 2611.22238 sec. 7, 'Whether a prefix stays cached also depends on concurrent agents', and its App. O checklist item on server-reported hits; HarnessTax's 5x harness cost effect without a cache term. Who pays: HAL and every leaderboard with a cost column, scaffold authors, and anyone buying an agent off a cost-accuracy frontier.
- **Impact ceiling:** **floor**: A table of $g_i$ and $\rho_i$ by provider x scaffold and the list of flipped frontier steps, cited by the card's v2 and by HAL. Requires steps 0-1. Judgment 0.55.; **middle**: HAL adds a realized-hit-share column and a cost re-priced at a stated cache state; one widely used scaffold fixes its breakpoints and its cost drops on the board. Requires the middle outcome and a maintainer. Judgment 0.25.; **ceiling**: 'Cost at a stated cache state and price vector' becomes the reporting rule for agent leaderboards and cost ablations, and published harness cost effects are re-read as cache plumbing. Requires adoption by two boards. Judgment 0.1.
- **Relevance:** HAL route (Narayanan): direct, it is their archive and their column. Narasimhan route: indirect (the tau-bench cells sit in the archive). Systems route (L3): direct, realized versus ideal reuse is a serving measurement of the true cost structure. Industry: direct, it is the API bill. Jacob's edge: the accounting identity and the append-only bound are napkin-checkable; GPU numerics zero.
- **Kill probe:** Steps 0-1: $0, 0 GPU-h, 5 days; dead if fewer than three of 35 steps flip and $g_i < 0.10$ for 90% of cache-capable runs; dead at step 0 without cache-read fields.
- **Density and ownership:** Not searched this session (brief: no fetching). From the cards and this repo's kill records: TurnCost 2610.15093 re-scores public coding-agent trajectories under alternative caching and pricing assumptions (C-W43-22 kill, 2026-10-25), the nearest occupant; difference: it assumes a cache, this measures the provider's realized cache against the ideal on a cross-provider, cross-scaffold archive and reads the gap onto a leaderboard's frontier. 2609.11987 re-prices harness contrasts from per-turn usage and calls the cost ordering unresolved because 58 runs left no usage record (CL-W43-14 record). 2607.12161 (card neighbour): cache creation and reads dominate input-side cost in Claude Code; a 38.4% token cut raised billed cost 6.8%. TraceLab 2606.30560 (card neighbour): 95.6% of input tokens are cache reads in production. Owners: HAL's maintainers (the archive; whether 2510.11977 discusses it…
- **Why now:** 2611.21515 (2026-11-16) and 2611.22238 (2026-11-17) landed a day apart with the two halves (the quadruples priced as logged; the own-cache ideal defined) and neither joined them; HAL's logs released 2025-10.
- **Register, and what it is not:** Measurement, a ruler on a shipped artifact (the leaderboard's cost column) with a reporting consequence. It is not a new cost model, not the card's successive halving on another benchmark, and not a claim about which agent is cheapest.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: every premise number is fetched and dated (27 of 35 steps unresolved, 40.1% of SWE-bench pairs, 11.7x cache double count, 4.8x and 5.0x price-sheet moves — 2611.21515 secs. IV-V; 94-98% cache reads, +8% to +36% warmed-cache bills — 2611.22238 secs. 2, 6, Table 7). Conditioning set written in the import: the measurand is the complete-run token cost at a declared price vector and cache condition; the agent's draw is the only Type A row (temperature as the harness set it, recorded per run); cache state and price sheet are Type B rows, properties of the protocol, which is the claim… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W47-01 and C-W47-03 cost $0 and under a week on the public archive; the import's step 2 is API spend only. Kill results written: fewer than 3 steps flip; Type A share over 0.60; $u_{c,r} < 0.10$. Both outcomes informative (a cost budget template either way). |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'cost' made measurable with an uncertainty budget identifiable under the stated protocol and computable from data HAL already holds. Surprise three ways: expected — at least 12 of 35 steps compatible on cost, Type A share under 0.35 (judgment 0.45); field assumes — cost exact, uncertainty on accuracy (2611.21515 sec. VIII); belief-changing — Type A over 0.60 (replicates fix it, 0.25) or $u_{c,r} < 0.10$ (0.30). Not the CL-W43-14 case: the expected row (cache state, Type B) is one the field does not report, and the W43 verdict covered only the replicate row. |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: leaderboard owners (a budget beside the cost column), agent-paper authors (state the cache condition under a 'cheaper' claim), HAL's selection tooling (cost interval in $Q$), cost-accounting papers (2609.11987, 2608.07304: a summed budget instead of one row). Proper-shaped; golden only if every leaderboard adopts the column (lab position with HAL). |
| G4 | mechanism and consequence | Mechanism: the input bill per prompt token is $1 - (1 - c)h$ with $c$ the cached price and $h$ the hit rate; at $c = 0.1$ a hit rate between 0.90 and 0.98 moves the input bill by 1.6x, larger than any replicate CV on a 48-task total, so the cache row dominates and no number of replicates shrinks it. Consequence per outcome written above. |
| G5 | durability; lab-adjacent | Durable: a budget applies to any priced run; flag — provider price sheets and cache rules change, so the budget's rows are re-evaluated per release (that is its purpose). |
| G6 | ownership, density, race window; position clause | Density to be measured at the kill search in the cost-accounting community's role words (cache-aware, as-billed, invoice, breakpoint, time-to-live, hit rate, price sheet, token-exact) and the metrology words (uncertainty budget, Type A/B, compatibility). Known neighbours from the import's four queries: 2609.11987 (one Type B row, 'unresolved' orderings), 2611.22238 (every row measured, none summed), 2609.33812 lineage (replicates). Why now: HAL's per-call quadruples with cache fields (2611.21515's data source) and 2611.22238's cache model, both November 2026. Race window: cost-accounting pape… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-01 | Whose cache paid: the realized-versus-ideal prefix-cache term in the cost axis of the HAL leaderboard | Steps 0-1: $0, 0 GPU-h, 5 days; dead if fewer than three of 35 steps flip and $g_i < 0.10$ for 90% of cache-capable runs; dead at step 0 without cache-read fields. | killed | — |
| C-W47-03 | Cheap because it gives up: the failure premium inside the cost axis of agent leaderboards | Steps 0-1: $0, 0 GPU-h, 2 days; dead if $\phi < 1.3$ on both benchmarks or the failure-share term dominates fewer than 5 of 35 steps. | killed | — |

Also under this claim (no scorecard yet): import:2026-W47-S6xF9 ($0 on the public HAL archive plus about $300-600 of API spend, 0 GPU-h, 9 d: the GUM budget per run, compatibility of the 35 steps on co…

## Kill search

### Concept level (CL-W47-01) — killed (2026-11-22)
On four decrypted HAL SWE-bench Mini archives the realized hit share is 0.00 (Anthropic, no cache_control), 0.41 and 0.60 (OpenAI automatic); OpenAI/Together-path published costs are exactly 2.00x the deduplicated bill (litellm parent and provider child spans both summed), Anthropic 1.00x. After correction the budget is the replicate row (u_c,r about 0.07-0.09 < 0.10; Type A share > 0.6; resolvable ratio 1.22x): CL-W43-14's service answer.
Full record: [`/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-01.md`](../../..//home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-01.md).
**Occupied by:** none for the summed GUM budget; the survivor is stated knowledge: CL-W43-14 kill record (replicate row 4-9%, a service), 2609.28919 ('so it picks the rate on the price sheet'), 2611.21515 sec. VIII (cache accounting and standardized price sheets preserved for reproducibility); the audit residue belongs to HAL and 2611.21515's authors
**Why not done before:** It has been done in rows (replicate: 2608.25399, 2609.33812, 2611.22238; cache state: 2601.06007, 2607.19214, 2608.00101; accounting defect: 2610.34817, 2611.21515; price sheet: 2611.21515, HAL PRs #105/#109/#113/#114). Nobody summed them because on HAL the Type B rows are blunders and declared constants, and metrology's instrument for that is a correction, not a budget. The factor-2 span duplication went unreported because any reader who re-prices from the spans inherits it and the host's own code sums every span with usage (weave_utils.get_total_cost, trace_roots_only=False).
Closest neighbors (one-sentence trick; one-line difference):
- `2611.21515` Beyond Leaderboard Ranks: Selecting Software Engineering Agents Under Budget Constraints — Re-price every HAL run from its token log at one price sheet, paired-test neighbours on shared tasks, replay purchasing policies on the fixed matrix. *Difference:* Owns the gross-error audit (11.7x, 5.0x), Eq. 1 and the frontier; statistics on accuracy only, point costs; its reconstruction 'a consistent comparison basis rather than exact historical invoices'; did not find the factor-2 span duplication, which a reconstru…
- `2611.22238` Context Has a Price: Adding and Removing Context for LLM Coding Agents under Prefix Cachi… — Bill runs as U + cC + pO on 20,000 vLLM runs; deleting an old tool output re-bills the suffix once, so masking flips sign at a tenth-price cache. *Difference:* Measures the cache rows one at a time (sibling warming +8% to +36%, block granularity 9.8%, replicate SE 3-4%) and sums none; 'reference prices, not measurements of a provider's billing system'; the rows it models as intervals are scaffold constants on HAL.
- `2609.11987` Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Con… — Paired same-model harness contrasts on a private suite, re-priced from per-turn usage at frozen list prices. *Difference:* The one source calling a cost ordering 'unresolved', from one Type B row (58 runs without usage records); one run per cell; no budget, no leaderboard.
- `2610.34817` Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Age… — Mine 120 prompt-caching pull requests in 10 agent systems, classify mis-integrations as request-side misconfiguration or read-side usage miscount, lint invocation sites against a dated provider oracle. *Difference:* States that scaffolds mis-integrate caching silently and miscount reads (32 found in 571 projects); HAL's generalist scaffold (no cache_control on Anthropic; doubled spans) is two instances of its taxonomy.
- `2607.19214` Keeping the Cache Warm Pays: Keepalive Economics for Agentic Workloads — Replay the prefix on a timer during tool waits so the provider's cache does not evict; locate each provider's eviction point. *Difference:* The cache-state row's magnitude on four providers ('cutting the post-pause request cost by up to 12.5x'; eviction at about 5/10/30 minutes for Anthropic/DeepSeek/OpenAI); a protocol variability source, not an uncertainty on a reported cost; CL-W47-06's territ…
*Search degraded:* ['s2', 'Q4 (metrology broad) query defect: generic tokens, 10,376 hits', 'conference exports not built', '2607.19214 API abstract truncated; eviction values read from the HTML full text (LaTeX artefacts), quoted in own words']

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

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): three probes on the cost axis lifted into a claim; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-01.md): killed — gate G0 (premise: the cache-state row is a scaffold constant on HAL, not a draw; the accounting row is a factor-2 blunder, not a bias) with the claim's own if_false branch (Gate 2B) realized at $0 on the archive it names; On four decrypted HAL SWE-bench Mini archives the realized hit share is…
- 2026-11-22 — C-W47-01 killed: W47 concept-level kill search of CL-W47-01: probe verdict killed. Step 0 ran on four archives and confirmed its expected reading (Anthropic h = 0, h_bar = 0.86, rho = 2.55; OpenAI h = 0.41-0.60), but its headline is Harness Tokenomics' sentence (2609.28919) and CacheLint's taxonomy (2610.34817) with HAL's name attached (Gate 2B); the survivor is the audit (span duplication 2.00x; no breakpoints),…
- 2026-11-22 — C-W47-03 killed: W47 concept-level kill search of CL-W47-01: probe verdict killed. Gate 2B: 'Failed runs tend to be longer' (2608.03222) is the field's motivating sentence, Cost-of-Pass (2504.13359) and Token Load including failed attempts (2610.32483) are the unit and the column; within the one Claude run the premium is 1.34-1.38, under its 'at least twice' and at its 1.3 kill line; the two-way fit on the releas…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-01`, version 2)
- probe `C-W47-01`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-03`: `data/candidates/2026-W47.jsonl`
