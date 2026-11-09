# The run-to-run variance that agent benchmarks report at temperature 0 is the serving stack's batch-dependent arithmetic, not the agent, and over multi-turn trajectories it is large enough to reorder leaderboards.

`CL-W43-J01` · lane **L1** · status **killed** · rank None · position solo · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search owed). Grade on paper: open as of 2026-11-02 (graded; first scorecarded probe attached); kill search owed before it is proper. Next action: see First steps.

## The claim

- **Headline:** The run-to-run variance that agent benchmarks report at temperature 0 is the serving stack's batch-dependent arithmetic, not the agent, and over multi-turn trajectories it is large enough to reorder leaderboards.
- **Current belief (the field's):** Fetched 2026-10-20 from thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference (Horace He and Thinking Machines Lab, 2025-09-10): the forward pass is run-to-run deterministic, but kernels whose reduction order changes with batch size make a request's numerics depend on the other requests in the batch, so 'from each user's perspective the output is nondeterministic'; Qwen3-235B-A22B at temperature 0, 1000 completions of 1000 tokens: 80 unique completions, identical for the first 102 tokens; with batch-invariant kernels all 1000 identical; cost on Qwen3-8B, 1000 sequences: 26 s default vs 55 s unoptimised vs 42 s with the improved attention kernel (about 2.1x and 1.6x). The post frames this as reproducibility and on-policy RL (sampler-trainer KL flat at 0) and does not discuss benchmark evaluation. The field's working belief to test at the kill search: temperature-0 agent evaluations are reported as single runs or with a 'noise' of a point or two, as if deterministic.
- **If true:** Every temperature-0 benchmark report states its serving stack and whether decoding was batch-invariant; leaderboards add a stack-noise column or run batch-invariant; and the per-turn luck-skill decomposition (W41 product red team C, parked) becomes exactly identifiable on the agent side: a batch-invariant agent at temperature 0 has zero decision variance by construction, so Var[R] decomposes onto the user simulator and environment alone - the control arm that instrument lacked.
- **If false:** At trajectory scale the token-level divergences rarely change an action's outcome (flip rate under 2 percent, rank order stable) - a reassuring measurement benchmark owners would still cite when they report temperature-0 numbers; the luck-skill thread stays parked on its consumer verdict.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: EnvOS states its intervals omit 'repeated-model-sampling variation' (sec. 7.3) and that server-side changes 'would not be detectable'; the log-analysis position paper (2605.08545, card neighbour) asks for input-level evidence of what the agent saw; HAL 2510.11977 relies on single runs. Who pays: benchmark owners reporting temperature-0 numbers as reproducible, evaluators certifying agents before deployment, the systems route (serving nondeterminism as a measured quantity on an agent workload) and CL-W43-J01's own program.
- **Impact ceiling:** **floor**: A measured first-divergence distribution and flip count at temperature 0 on one certified testbed and one provider stack, cited as the API-side boundary of J01. Requires step 1. Judgment p 0.5.; **middle**: The serving share $S$ of within-cell variance on the same cells as the temperature-1.0 matrix, giving the first instance / sampling / serving split for an agent benchmark with environment and grader at certified zero; adopted as a reporting line by one benchmark. Requires step 1 plus the sibling matrix. Judgment p 0.3.; **ceiling**: The same split on an open-weight model served with and without batch-invariant kernels on the same testbed (J01's probe moved onto EnvOS), turning 'temperature-0 variance is the serving stack' into a controlled result with a systems fix. Requires about 40 GPU-hours and the batch-invariant serving path. Judgment p 0.15.
- **Relevance:** Systems route (Lloyd / Netravali / Dao): direct, serving nondeterminism measured on an agent workload. HAL and tau-bench owners: direct for the replicate rule at temperature 0. Narasimhan: moderate. Industry: direct for certification of deployed agents. Jacob's edge: GPU numerics and batch-dependent arithmetic are his background and load-bearing for the mechanism; theoretical physics zero; the measurement itself is API calls.
- **Kill probe:** 100 rollouts of Gemini 3.1 Pro Preview at temperature 0 on the released claims block plus 20 single-step re-sends, about $300, 0 GPU-hours, 5 days including the rebuild shared with the sibling; dead if 90 of 100 pairs are action-identical through the commit and no cell flips.
- **Density and ownership:** Occupied by the card: the certification protocol and the temperature-1.0 single-rollout results. The serving-nondeterminism mechanism is in print as a systems blog and as single-call measurements (the batch-invariant decoding line, to be fetched by the kill search; a 2024 arXiv measurement of nondeterminism under 'deterministic' settings exists and must be fetched, not cited from memory). No fetched source measures first-divergence steps or outcome flips inside a certified-static agent loop. The kill search must use the neighbours' words (nondeterminism, batch invariance, greedy decoding, reproducibility, floating-point, divergence, agent trajectory, repeated runs) and quote the limitation text of the batch-invariant line and of 2605.08545; density is counted on the day of writing.
- **Why now:** EnvOS supplement (2026-10-29 / 2026-11-02) with journaled request digests and a certified-static environment; Gemini's REST path exposes temperature; CL-W43-J01 is a thought awaiting a testbed. The mechanism (batch-dependent kernels) is a 2025 systems result; the enabling piece is the hashed-observation harness.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass: the premise number is fetched and dated (TML 2025-09-10: 80 unique completions in 1,000 at temperature 0; Qwen3-235B-A22B); the quantity is conditioned — random given byte-identical inputs (journaled digests), certified-static environment, pinned sampling parameters, one launch window — so whatever varies is the server; the plain trick exists (batch composition changes reduction order, so a request's numerics depend on its neighbours in the batch) |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass as of 2026-11-02: C-W44-07 is scorecarded at ~$300 with a pre-registered kill; P-W43-J01-a (15-25 GPU-h) carries the leaderboard clause and is still a thought |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a lab blog (TML), a system card (L08 attributes the error bar to tasks 'rather than run-to-run variance' at single-run protocols), a benchmark paper (EnvOS sec. 7.3 omits 'repeated-model-sampling variation' from every interval and states server-side changes 'would not be detectable'), a meta-paper (2607.17136: run-to-run nondeterminism a named variance component); route B: the serving share S of within-cell variance is identifiable on a certified-static testbed with a pre-registered surprise (expected S between 0.3 and 0.7 of the T = 1 within-cell variance; field assumes temper… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every temperature-0 benchmark report states its stack and whether decoding was batch-invariant; leaderboards add a stack-noise column; benchmark owners certifying reproducibility; the luck/skill split gains its zero-variance agent arm |
| G4 | mechanism and consequence | pass: mechanism — kernels whose reduction order changes with batch size make a request's numerics depend on the other requests in the batch; over a 40-action episode one flipped token changes an action and the outcome; consequence — batch-invariant official runs or a declared stack-noise column, or (if flips are under 2%) temperature-0 reports keep their single-run convention |
| G5 | durability; lab-adjacent | pass: a ruler on any serving stack and any agent; the specific flip rates are model- and provider-bound; lab-adjacent (the kernels exist; the measurement at benchmark scale does not) |
| G6 | ownership, density, race window; position clause | open: kill search owed (12-month count with batch invariance, reduction order, nondeterminism AND benchmark, evaluation, agent, pass^k); incumbents TML's kernels, vLLM and SGLang deterministic modes, 2602.07150's power analysis, HAL's reliability paper (attributes temperature-0 variance to 'non-sampling sources' and does not separate the user simulator — C-W44-OWN-2's question); density P7b (agent AND benchmark AND bimodal AND seed) = 0 |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-07 | Temperature zero in a certified-static world: the serving stack's share of agent outcome flips | 100 rollouts of Gemini 3.1 Pro Preview at temperature 0 on the released claims block plus 20 single-step re-sends, about $300, 0 GPU-hours, 5 days including the rebuild shared with the sibling; dead if 90 of 100 pairs are action-identical… | proposed | — |
| C-W44-OWN-2 | Where HAL's five temperature-zero runs first diverge on tau-bench airline: the agent, the simulated user, or the stack | The diff over the owner's traces (zero dollars, two days) plus the three-model pinned re-run ($200, one day); dead if $U \le 0.2$ and pinning moves no consistency column by more than 0.05. | parked | — |
| P-W43-J01-a | Outcome-flip rate at temperature 0: default serving stack (batch composition varied by concurrency) versus batch-invari… | Dead if the default arm's outcome-flip rate is under 2 percent of tasks AND the rank order of the three agent variants is identical across all ten repeats. Expected (judgment): 5-15 percent flips on 30-turn tasks and at least one adjacent-… | thought | not run (no candidate record yet) |

## Kill search

### Concept level (CL-W43-J01) — killed (2026-11-01)
Gate 2B on clause 1 (HAL 2602.16666 §4 states the serving-stack attribution as its protocol assumption, citing the same TML post) and occupation of clause 2 by 2602.07150 (temperature-0 agent variance, first-divergence distributions, compounding over the trajectory, 2–3 point improvements inside noise); the premise that temperature 0 is a low-variance arm is contradicted by 2602.07150 Table 1 (variance 'never decreases and sometimes increases with temperature zero').
Full record: [`data/reports/2026-W44-kill-CL-W43-J01.md`](../../../data/reports/2026-W44-kill-CL-W43-J01.md).
**Occupied by:** 2602.07150 (clause 2, measurement level); 2602.16666 (clause 1, stated protocol assumption — Gate 2B)
**Why not done before:** no reason found (flag): the batch-invariant arm has existed since 2025-09-10 and was used in print at single-call level by 2026-05-26 (2605.27763) and 2026-06-14 (2606.15621); the replicate agent studies (2602.07150, 2602.16666) ran without it and 2602.07150's future work names compaction and horizon, not the stack arm; the two-arm share is a 15–25 GPU-hour appendix to any of them, and the inverted reading (the stack is not all of it) is already written as prose by 2603.09127 and 2609.04198.
Closest neighbors (one-sentence trick; one-line difference):
- `2602.07150` On Randomness in Agentic Evals — Run six agent configurations ten times each on SWE-bench Verified, half at temperature 0, and read single-run pass@1 spread, pass@k vs pass^k, and the token position of first divergence between run pairs. *Difference:* none — occupied for clause 2: SD > 1.5 points at temperature 0, first divergence delayed (median token 5 to 56) but not removed, 'longer trajectories exhibit amplified variance', 2–3 point improvements inside noise; for clause 1 it names 'inference engines an…
- `2602.16666` Towards a Science of AI Agent Reliability (HAL) — Run fifteen agents K=5 times at temperature 0 on GAIA and tau-bench airline and report twelve reliability metrics. *Difference:* none — the attribution is their stated protocol assumption (Gate 2B): temperature 0 'so that any observed variance is attributable to non-sampling sources of stochasticity' with floating-point non-associativity, batch-size variation and kernel scheduling list…
- `2605.27763` A Paired Testing Protocol for Batch-Conditioned Refusal Robustness in LLM Serving — Re-run the same prompts alone, in synchronized batches and under continuous batching, adjudicate label flips, and ablate with vLLM's batch-invariant kernels. *Difference:* The probe's two-arm design exists (22/55 flips under standard vLLM, 0/55 with VLLM_BATCH_INVARIANT=1) at single-call level on 1B–3B models and one stack; no agent loop.
- `2609.31796` Same Probe, Different Numbers — Train activation probes under one batch size and precision, evaluate under every other, and compare verdicts example by example. *Difference:* Within-generation compounding of a batch-size change measured: first-token flips 2.1% of rows, 25% on different tokens by token 20; no agent loop or outcome.
- `2606.15621` Re-feeding Is Not Replaying — Compare continuations from the live KV state, an exact replica pass and a re-fed prefix, and confirm with batch-invariant kernels. *Difference:* The replica floor and the batch-invariant causal check ('both disagreement rates exactly zero') for token credit; same control arm, different quantity; no multi-turn agent.
**Narrowest surviving headline:** On tool-using, multi-turn agent benchmarks, a certified-deterministic serving arm removes under half of the temperature-0 run-to-run outcome variance; the remainder is the environment's tool and timing nondeterminism and the second sampling party, so benchmark owners' attribution of temperature-0 spread to the serving stack is wrong in the majority of cells. (An inverted claim; file as new. Survival weak: 2603.09127 and 2609.04198 state the reading in prose; a benchmark owner with replicate traces measures it in a day.)
*Search degraded:* ['s2', 'exports (no local conference-export index exists in the repository)']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Is this worth its kill search slot this week (it would take one of the three), given it serves L1 and the systems route rather than the top-ranked L5 thread?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim thought: captured from chat (Jacob raised the TML nondeterminism post as adjacent to the luck-subtraction thread); scorecard skeleton filled where the fetched post supports it; kill search owed before it is a proposal
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-J01.md): killed (weak) — Gate 2B on clause 1 (HAL 2602.16666 §4 states the serving-stack attribution as its protocol assumption, citing the same TML post) and occupation of clause 2 by 2602.07150 (temperature-0 agent variance, first-divergence distributions, compounding over the trajectory, 2–3 point improvements inside noise); the prem…
- 2026-11-01 — C-W44-OWN-2 parked: stage 8 owned-artifact prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-OWN-2 parked: claim CL-W43-J01 concept-level kill search (killed): probe effect 'unchanged' — lab-parked; its U (first divergence at a user turn) is the inverted claim's natural surprise on the one public temperature-0 replicate set with a second sampling party; re-home under the inverted claim.
- 2026-11-01 — C-W44-OWN-2 parked: claim_id CL-W43-J01 -> CL-W44-07 (re-homed after the kill searches)
- 2026-11-02 — claim open: pressure #7 (2026-11-02): L08 'most of the uncertainty comes from tasks rather than run-to-run variance' bounds the serving term from above on bimodal suites; B01 Terminal-Bench 4.0 pass_at_5 ties across ranks 1-5; banter 2607.17136 names run-to-run nondeterminism as a variance component beside the data draw; records R01, L08, L16 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): C-W44-07 (card 2610.40246, certified-static testbed, scorecarded) and C-W44-OWN-2 (lab, HAL traces) attached; graded against gates 0-6; status thought -> open on the strength of a scorecarded probe under one GPU-week (the kill search, owed, decides proper); rank 8

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J01`, version 3)
- probe `C-W44-07`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-OWN-2`: `data/candidates/2026-W44.jsonl`
- `P-W43-J01-a`: seed or import record (no candidate yet)
