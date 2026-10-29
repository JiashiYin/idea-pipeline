# The run-to-run variance that agent benchmarks report at temperature 0 is the serving stack's batch-dependent arithmetic, not the agent, and over multi-turn trajectories it is large enough to reorder leaderboards.

`CL-W43-J01` · lane **L1** · status **thought** · rank — · position solo · refreshed 2026-10-29

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** The run-to-run variance that agent benchmarks report at temperature 0 is the serving stack's batch-dependent arithmetic, not the agent, and over multi-turn trajectories it is large enough to reorder leaderboards.
- **Current belief (the field's):** Fetched 2026-10-20 from thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference (Horace He and Thinking Machines Lab, 2025-09-10): the forward pass is run-to-run deterministic, but kernels whose reduction order changes with batch size make a request's numerics depend on the other requests in the batch, so 'from each user's perspective the output is nondeterministic'; Qwen3-235B-A22B at temperature 0, 1000 completions of 1000 tokens: 80 unique completions, identical for the first 102 tokens; with batch-invariant kernels all 1000 identical; cost on Qwen3-8B, 1000 sequences: 26 s default vs 55 s unoptimised vs 42 s with the improved attention kernel (about 2.1x and 1.6x). The post frames this as reproducibility and on-policy RL (sampler-trainer KL flat at 0) and does not discuss benchmark evaluation. The field's working belief to test at the kill search: temperature-0 agent evaluations are reported as single runs or with a 'noise' of a point or two, as if deterministic.
- **If true:** Every temperature-0 benchmark report states its serving stack and whether decoding was batch-invariant; leaderboards add a stack-noise column or run batch-invariant; and the per-turn luck-skill decomposition (W41 product red team C, parked) becomes exactly identifiable on the agent side: a batch-invariant agent at temperature 0 has zero decision variance by construction, so Var[R] decomposes onto the user simulator and environment alone - the control arm that instrument lacked.
- **If false:** At trajectory scale the token-level divergences rarely change an action's outcome (flip rate under 2 percent, rank order stable) - a reassuring measurement benchmark owners would still cite when they report temperature-0 numbers; the luck-skill thread stays parked on its consumer verdict.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: the TML post (fetched) calls reproducibility 'a bedrock of scientific progress' and shows 80 unique completions in 1000 at temperature 0, but stops before evaluation - that is the gap. Who pays: benchmark owners who report temperature-0 numbers, and anyone ranking agents a few points apart. Missing: a benchmark owner's own statement about temperature-0 variance - kill search.
- **Impact ceiling:** **floor**: A measured flip-rate and first-divergence-turn table for one benchmark and one model; a note people cite when they report temperature-0 numbers. Requires the probe. p = 0.7 (judgment).; **middle**: The number is large enough that benchmark owners add a serving-stack column or adopt batch-invariant decoding for official runs. Requires flips over 5 percent or a rank swap. p = 0.25 (judgment).; **ceiling**: The exact zero-variance agent arm re-opens the parked per-turn luck-skill instrument with a clean identification, and the pair becomes a standards paper on deterministic evaluation of agents. Requires the middle result plus the parked item's consumer objection answered. p = 0.1 (judgment).
- **Relevance:** L1 (reliability, variance attribution): direct. L3 and the systems route (Lloyd, Netravali, Dao): batch-invariant kernels are their vocabulary; direct. Narasimhan route via tau-bench as the natural testbed. Industry: every eval team. Jacob's edge: GPU numerics and kernels (computer engineering) load-bearing. Zero for L5 and for any robotics consumer.
- **Kill probe:** P-W43-J01-a above: 15-25 GPU-h, $50-80, 4 days; dead if flips under 2 percent and ranks identical across ten repeats.
- **Density and ownership:** Unknown until the kill search (12-month arXiv API count with mechanism words - batch invariance, reduction order, nondeterminism - AND role words - benchmark, evaluation, agent, pass^k; two pre-window precedents; the two closest papers' limitation text). Incumbents to check: TML's kernels, vLLM/SGLang deterministic modes, any 'temperature 0 is not deterministic' measurement.
- **Why now:** Batch-invariant kernels (2025-09-10) make a truly zero-variance agent arm available for the first time; before them, stack noise and agent decision variance at temperature 0 could not be separated, so nobody could measure the first in isolation.
- **Register, and what it is not:** Measurement (a ruler for serving-stack noise at benchmark scale) with a standards consequence (what a temperature-0 report must state). It is not a new kernel, not a benchmark, not a method, and not a claim about sampling at temperature above 0.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-J01-a (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J01-a | Outcome-flip rate at temperature 0: default serving stack (batch composition varied by concurrency) versus batch-invari… | Dead if the default arm's outcome-flip rate is under 2 percent of tasks AND the rank order of the three agent variants is identical across all ten repeats. Expected (judgment): 5-15 percent flips on 30-turn tasks and at least one adjacent-… | thought | not run (no candidate record yet) |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-J01-a** (Sunday run), or run `/kill P-W43-J01-a` in a session.
2. If it survives: `/redteam P-W43-J01-a`, then the probe as pre-registered — Dead if the default arm's outcome-flip rate is under 2 percent of tasks AND the rank order of the three agent variants is identical across all ten repeats. Expected (judgment): 5-15 percent flips on 30-turn tasks and at least one adjacent-rank swap. Field's assumption: temperature 0 is deterministic or noise of a point. Belief-changing: over 15 percent or a non-adjacent rank reversal. 15-25 GPU-h…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Is this worth its kill search slot this week (it would take one of the three), given it serves L1 and the systems route rather than the top-ranked L5 thread?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim thought: captured from chat (Jacob raised the TML nondeterminism post as adjacent to the luck-subtraction thread); scorecard skeleton filled where the fetched post supports it; kill search owed before it is a proposal

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J01`, version 1)
- `P-W43-J01-a`: seed or import record (no candidate yet)
