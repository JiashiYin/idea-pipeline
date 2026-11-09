# On tool-using, multi-turn agent benchmarks, a certified-deterministic serving arm removes under half of the temperature-0 run-to-run outcome variance; the remainder is the environment's tool and timing nondeterminism and the second sampling party, so benchmark owners' attribution of temperature-0 spread to the serving stack is wrong in the majority of cells. (An inverted claim; file as new. Survival weak: 2603.09127 and 2609.04198 state the reading in prose; a benchmark owner with replicate traces measures it in a day.)

`CL-W44-07` · lane **L1** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 2B (pre-registered surprise equals or is contradicted by the field's stated and measured knowledge); Gate 0 also fails on the protocol clause (the environment channel's size is a dial the experimenter sets; a sampled user simulator is a policy, not an environment channel). Next action: see First steps.

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | the deterministic arm is not a zero arm under load (2609.38981); the record must certify replicas; added W45: coupling means the same draw sequence from the same stream position, not the same realised failure once action sequences differ (the common-random-numbers caveat); the hosted lane's coupled cell is the serving floor, not a zero cell (2611.05650 App. B.7: 0 of 4 re-sends reproduced) |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-07 ~$300 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler (serving share S of temperature-0 outcome variance) with a pre-registered surprise against the owners' stated assumption |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; 2602.07150 and 2605.27763 are the closest |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-07 | Temperature zero in a certified-static world: the serving stack's share of agent outcome flips | 100 rollouts of Gemini 3.1 Pro Preview at temperature 0 on the released claims block plus 20 single-step re-sends, about $300, 0 GPU-hours, 5 days including the rebuild shared with the sibling; dead if 90 of 100 pairs are action-identical… | killed | — |
| C-W45-04 | Common random numbers at temperature 0: the environment's draws versus the serving stack as the source of outcome flips… | Steps 0 to 2: about 12 GPU-hours, about $250, 7 days; dead if the serving share is at least two thirds at both tool-failure rates with lower bound above 0.5 and the hosted lane's independent-minus-coupled difference sits inside the serving… | killed | — |
| P-W43-J01-a | P-W43-J01-a (redesigned: deterministic arm must be replica-certified — Vosti 2609.38981, 2609.04198) | — | — | not a candidate record (seed or import) |
| C-W44-OWN-2 | Where HAL's five temperature-zero runs first diverge on tau-bench airline: the agent, the simulated user, or the stack | The diff over the owner's traces (zero dollars, two days) plus the three-model pinned re-run ($200, one day); dead if $U \le 0.2$ and pinning moves no consistency column by more than 0.05. | parked | — |

## Kill search

### Concept level (CL-W44-07) — killed (2026-11-08)
Gate 2B: the pre-registered surprise (serving share S < 0.5) is contradicted by the only two-arm measurement in print on a multi-turn tool-using benchmark (2608.08239: serving configuration alone moves diverging control forks from ~50% to 90-96% with the environment verified) and by the two channels' separately measured magnitudes (hosted temperature-0 serving flips ~9% of single-shot SWE-bench outcomes, 2607.09691; environment infra errors 0.5-2% of Terminal-Bench trials at leaderboard headroom, Anthropic 2026-02-05); the second-sampling-party clause is an unpinned-simulator protocol defect, not an environment channel; why-not-done is 'no reason found'.
**Occupied by:** 2608.08239 (near-occupant: the two-arm serving comparison inside a multi-turn tool-using loop with the environment rebuilt and verified; result in the field's direction) together with 2607.09691 and the Anthropic 2026-02-05 post (the two channels' magnitudes measured separately: ~9 of 100 instances vs 0.5-2 of 100 trials). No neighbour runs the certified decomposition; none is needed to settle th…
**Why not done before:** no reason found — the design is 2018 RL reproducibility practice (1809.05676) plus common random numbers plus a replica-stable serving arm available since 2025-09; the replicate papers skipped it because its expected answer is their stated assumption, and the one paper that ran the two-arm comparison did so as an audit of its own control floor and got the assumed direction
Closest neighbors (one-sentence trick; one-line difference):
- `2608.08239` The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World… — Fork live SWE-bench trajectories at 30% and 70% of their length, rebuild the container by re-executing the recorded commands, continue with another model or the same model, and read the swap's divergence over the same-model control floor. *Difference:* The claim's two-arm design at the action level, already run as an audit: under identical temperature-0 decoding, AWQ-served controls 'half never diverge at any action' while FP8-served controls 'diverge on 90-96% of forks', with environment reconstruction ver…
- `2607.09691` What Context Does a Coding Agent Actually Need to Act? (2026-06-19) — Hold localisation fixed with an oracle, vary only how the code is shown, build every patch with a deterministic SEARCH/REPLACE builder and grade with the official Docker harness, so the only sampled component is one temperature-0 API call. *Difference:* The serving channel measured alone with the environment and harness channel deterministic by construction: 6/70 (~9%) per-instance outcome flips between byte-identical temperature-0 runs on SWE-bench Verified, read as 'a noise floor under every small effect r…
- `web:anthropic.com/engineering/infrastructure-noise` Quantifying infrastructure noise in agentic coding evals (Anthropic Engineering, 2026-02-… — Run Terminal-Bench 2.0 on one model under six resource enforcement levels from strict per-task specs to uncapped and read the infra-error rate and pass rate at each. *Difference:* The environment channel measured alone, model fixed: infra errors 'from 5.8% at strict enforcement to 0.5% when uncapped' (2.1% at 3x headroom), +6 points over the range; SWE-bench 5x RAM sweep moves 1.54 points; the timing channel named and 'not formally qua…
- `2609.04748` Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Se… — Run an eighty-episode multi-turn tool-use workload at batch size one with prefix-cache reuse on and off across two engines and four weight formats and count episodes whose cache-hit and recompute paths diverge. *Difference:* The serving channel decomposed within itself on an agentic workload (reuse off reproduces every token in all ten configurations; reuse on diverges in up to 82.5% of episodes at four-bit); a cheap replica-stable serving arm exists; no environment channel, no o…
- `2610.10062` Loud Failures, Quiet Failures: Fault Detection and Recovery in Tool-Using Language Model… — Inject one typed tool fault at a chosen step and score recovery against the state the same model reaches fault-free, judged against the agreement of two fault-free runs. *Difference:* The read-against-the-run-to-run-floor design on a multi-turn tool benchmark (two fault-free runs agree in 63.3% of trials), but at temperature 1.0 with unseeded provider sampling; no channel split.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

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
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 3 -> 5; ranked 5 (was 3): ~$300 cheapest probe and a stated protocol assumption of three benchmark owners as the target; gained the two-channel testbed C-W45-04 this week; moved below CL-W44-06 and CL-W45-05 on consumer breadth; its W44 survival note ('2603.09127 and 2609.04198 state the reading in prose') still weighs on Gate 2B
- 2026-11-08 — claim killed: concept-level kill search (data/reports/2026-W45-kill-CL-W44-07.md): killed — Gate 2B: the pre-registered surprise (serving share S < 0.5) is contradicted by the only two-arm measurement in print on a multi-turn tool-using benchmark (2608.08239: serving configuration alone moves diverging control forks from ~50% to 90-96% with the environment verified) and by the two channels' separately measured…
- 2026-11-08 — C-W44-07 killed: W45 concept-level kill search of CL-W44-07 (data/reports/2026-W45-kill-CL-W44-07.md): killed-with-claim — its headline outcome is predictable on a hosted REST stack (2607.09691: 9% flips on a hosted Claude path, single-shot) and its surviving readout S reads near 1 on a certified-static world; keep the digest-matched first-divergence readout as a method note, no claim attached
- 2026-11-08 — C-W45-04 killed: W45 concept-level kill search of CL-W44-07 (data/reports/2026-W45-kill-CL-W44-07.md): killed-with-claim as a probe of CL-W44-07; its serving share sigma is a reading of the dial r it sets (Gate 0 protocol clause) and its coupling by stream position is the published-broken form of common random numbers (2603.11084, event-keyed fix); redesign owed only if re-homed: the certificate cell (model in th…
- 2026-11-08 — C-W44-OWN-2 parked: W45 concept-level kill search of CL-W44-07 (data/reports/2026-W45-kill-CL-W44-07.md): survives unchanged as lab-parked protocol service (its U is the only unmeasured cell with a named holder; a column, not a claim)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-07`, version 4)
- probe `C-W44-07`: `data/candidates/2026-W44.jsonl`
- probe `C-W45-04`: `data/candidates/2026-W45.jsonl`
- `P-W43-J01-a`: seed or import record (no candidate yet)
- probe `C-W44-OWN-2`: `data/candidates/2026-W44.jsonl`
