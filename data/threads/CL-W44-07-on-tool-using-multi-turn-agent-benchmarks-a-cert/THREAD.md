# On tool-using, multi-turn agent benchmarks, a certified-deterministic serving arm removes under half of the temperature-0 run-to-run outcome variance; the remainder is the environment's tool and timing nondeterminism and the second sampling party, so benchmark owners' attribution of temperature-0 spread to the serving stack is wrong in the majority of cells. (An inverted claim; file as new. Survival weak: 2603.09127 and 2609.04198 state the reading in prose; a benchmark owner with replicate traces measures it in a day.)

`CL-W44-07` · lane **L1** · status **open** · rank 3 · position both · refreshed 2026-11-02

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed next week). Next action: see First steps.

## The claim

- **Headline:** On tool-using, multi-turn agent benchmarks, a certified-deterministic serving arm removes under half of the temperature-0 run-to-run outcome variance; the remainder is the environment's tool and timing nondeterminism and the second sampling party, so benchmark owners' attribution of temperature-0 spread to the serving stack is wrong in the majority of cells. (An inverted claim; file as new. Survival weak: 2603.09127 and 2609.04198 state the reading in prose; a benchmark owner with replicate traces measures it in a day.)
- **Current belief (the field's):** HAL 2602.16666 sec. 4: 'We set the temperature to zero so that any observed variance is attributable to non-sampling sources of stochasticity [17] (e.g., floating-point non-associativity, batch-size variation from concurrent server load, non-deterministic kernel scheduling...)'
- **If true:** Benchmark owners stop attributing temperature-0 spread to the serving stack and report the environment's and the second party's share; a certified-deterministic arm becomes a required control
- **If false:** The serving stack is the majority source and HAL's attribution stands — a measured confirmation of a stated assumption (service)

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | the deterministic arm is not a zero arm under load (2609.38981); the record must certify replicas |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-07 ~$300 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler (serving share S of temperature-0 outcome variance) with a pre-registered surprise against the owners' stated assumption |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; 2602.07150 and 2605.27763 are the closest |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-07 | Temperature zero in a certified-static world: the serving stack's share of agent outcome flips | 100 rollouts of Gemini 3.1 Pro Preview at temperature 0 on the released claims block plus 20 single-step re-sends, about $300, 0 GPU-hours, 5 days including the rebuild shared with the sibling; dead if 90 of 100 pairs are action-identical… | proposed | — |
| P-W43-J01-a | P-W43-J01-a (redesigned: deterministic arm must be replica-certified — Vosti 2609.38981, 2609.04198) | — | — | not a candidate record (seed or import) |
| C-W44-OWN-2 | Where HAL's five temperature-zero runs first diverge on tau-bench airline: the agent, the simulated user, or the stack | The diff over the owner's traces (zero dollars, two days) plus the three-model pinned re-run ($200, one day); dead if $U \le 0.2$ and pinning moves no consistency column by more than 0.05. | parked | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W44-07** (Sunday run), or run `/kill C-W44-07` in a session.
2. If it survives: `/redteam C-W44-07`, then the probe as pre-registered — 100 rollouts of Gemini 3.1 Pro Preview at temperature 0 on the released claims block plus 20 single-step re-sends, about $300, 0 GPU-hours, 5 days including the rebuild shared with the sibling; dead if 90 of 100 pairs are action-identical through the commit and no cell flips.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- C-W44-OWN-2 is parked — access to HAL's K = 5 reliability traces (the Weave logs of the tau-bench airline runs) or a stated need from Narayanan: fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-01 — claim open: filed as the narrowest surviving headline of CL-W43-J01 (killed at concept level the same day); its own concept-level kill search is owed next week (W44 budget of 12 spent) before any probe is designed (rule 17)
- 2026-11-01 — claim open: ranked 3 after the W44 kill searches: ~$300; inverts a stated protocol assumption of three benchmark owners
- 2026-11-01 — C-W44-OWN-2 parked: stage 8 owned-artifact prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-OWN-2 parked: claim CL-W43-J01 concept-level kill search (killed): probe effect 'unchanged' — lab-parked; its U (first divergence at a user turn) is the inverted claim's natural surprise on the one public temperature-0 replicate set with a second sampling party; re-home under the inverted claim.
- 2026-11-01 — C-W44-OWN-2 parked: claim_id CL-W43-J01 -> CL-W44-07 (re-homed after the kill searches)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-07`, version 2)
- probe `C-W44-07`: `data/candidates/2026-W44.jsonl`
- `P-W43-J01-a`: seed or import record (no candidate yet)
- probe `C-W44-OWN-2`: `data/candidates/2026-W44.jsonl`
