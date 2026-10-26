# Token counts mis-state the cost of agentic workloads: KV-cache residency, not tokens generated, is the binding term in both the training iteration and the serving bill.

`CL-W43-12` · lane **L3** · status **open** · rank 3 · position both · refreshed 2026-10-26

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 pending this run's kill search; Gate 1 for the import half blocked on paperwork (no scorecard). Grade on paper: open; third automatic kill search this run on C-W43-22. Next action: see First steps.

## The claim

- **Headline:** Token counts mis-state the cost of agentic workloads: KV-cache residency, not tokens generated, is the binding term in both the training iteration and the serving bill.
- **Current belief (the field's):** Systems papers quote throughput in output tokens per second per GPU and list waste terms as if they add (FlashNext-RL 2610.28998: 26% zero-advantage rollouts discarded, a third of sessions idle on sandbox commands, trainer waiting 25%); context-management papers report savings as token counts (observation masking, sliding windows), while 2610.26632 found dropping turns cost 2.9-4.0x the dollars at 0.84-0.90x the tokens because it broke prefix caching.
- **If true:** Every agentic-RL systems paper reports a per-station demand table and names the binding station; cache-engineering is priced as a training-throughput lever; published token savings are re-signed under cached-prefix pricing; harness builders stop trimming by default
- **If false:** Decode compute binds (utilization >= 0.85 with KV below cap) and trimming saves money at the reported lengths: token accounting is adequate and the lane's cost instrument is Little's law applied once

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
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-22 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a systems paper's own non-additive waste list (2610.28998), a harness paper's own dollars-vs-tokens inversion (2610.26632), and the serving literature's cached-input price tiers (three independent source types); route B: the import supplies the ruler (demand per station, utilization law) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: systems authors (demand table), context-management authors (dollar sign of savings), billing comparisons on leaderboards (cached-input column), RL infra teams (KV release during tool waits) |
| G4 | mechanism and consequence | pass: mechanism — sessions holding KV while waiting on tools consume the binding resource; trimming forces re-prefill at the uncached price; consequence — park KV during tool waits, keep history until the break-even ratio |
| G5 | durability; lab-adjacent | pass: operational laws hold for any stack; the specific break-even depends on provider prices, which change |
| G6 | ownership, density, race window; position clause | open: the import found the operational-analysis half unmade in agentic RL across 3 queries (14, 89, 12 hits) and the straggler half made (Heddle, VenusRL, QwenGyre, PACE); C-W43-22's incumbents are AKV's 1.85x text-trim number and TokenPilot's table; kill search on C-W43-22 this run |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-22 | Re-price context management under prefix-cache billing: when does trimming cost more than keeping everything | Step 1 analytic re-pricing on released trajectories ($0, 2 days); step 2 replay of 50 SWE-bench trajectories x 5 policies on SGLang with prefix caching, 30 GPU-hours, ~$100, 4 days; kills if per-turn masking computes fewer prefill tokens t… | proposed | — |

Also under this claim (no scorecard yet): import:2026-W43-S6xF7 (pass A: $0, one day, operational analysis of FlashNext-RL's published numbers; pass B: instrumented 8-GPU stack with KV release during t…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-22** (Sunday run), or run `/kill C-W43-22` in a session.
2. If it survives: `/redteam C-W43-22`, then the probe as pre-registered — Step 1 analytic re-pricing on released trajectories ($0, 2 days); step 2 replay of 50 SWE-bench trajectories x 5 policies on SGLang with prefix caching, 30 GPU-hours, ~$100, 4 days; kills if per-turn masking computes fewer prefill tokens than full history on most turns at $r \le 0.25$ and the published savings keep their sign; 7 days in all.
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

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-12`, version 1)
- probe `C-W43-22`: `data/candidates/2026-W43.jsonl`
