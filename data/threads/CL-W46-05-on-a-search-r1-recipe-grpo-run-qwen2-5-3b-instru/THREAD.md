# On a Search-R1-recipe GRPO run (Qwen2.5-3B-Instruct, HotpotQA, four turns), at least half of the problems the greedy union-versus-best gap calls 'forgotten' are coin-flip cells — success probability between 0.2 and 0.8 at the best checkpoint under eight draws at the RL temperature — and at most a fifth are strict probability drops (above 0.8 at some earlier checkpoint, below 0.2 at the best).

`CL-W46-05` · lane **L2** · status **open** · rank 5 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed); Gate 2B flagged (the direction is plausible from pass@k folklore; the magnitude and the three-way split are the content). Next action: see First steps.

## The claim

- **Headline:** On a Search-R1-recipe GRPO run (Qwen2.5-3B-Instruct, HotpotQA, four turns), at least half of the problems the greedy union-versus-best gap calls 'forgotten' are coin-flip cells — success probability between 0.2 and 0.8 at the best checkpoint under eight draws at the RL temperature — and at most a fifth are strict probability drops (above 0.8 at some earlier checkpoint, below 0.2 at the best).
- **Current belief (the field's):** Agentic-OPD 2611.12799 (card, full text): 'We use greedy decoding for all checkpoint evaluations' (sec. 2); 'the final checkpoint solves 2,808 tasks, while 4,553 tasks are solved by at least three checkpoints, a difference of 62%' (sec. 2), read as 'forgotten agent capabilities' and made a training target by selecting teachers on greedy failure sets (eqs. 4-9); 'measuring how much of the historical task coverage can be reliably recovered' is conceded only as a 'useful next step' (sec. 5). Temporal Sampling 2505.20196 (abstract fetched 2026-11-16; sec. 2.2 quoted by the import from the full text): 'models often forget how to solve problems they previously answered correctly during training. We term this phenomenon temporal forgetting'; 'To minimize variability arising from different sampling methods during evaluation, we employ greedy sampling'; the resulting table is read as 'the model oscillates between correct and incorrect answers across checkpoints' (Figure 3). Neither paper decodes a checkpoint twice on the forgetting set or reports a noise floor.
- **If true:** 'Temporal forgetting' and the union-versus-best gap are protocol numbers until a draw floor is reported: checkpoint-consolidation and temporal-ensembling papers (Agentic-OPD, Temporal Sampling, GTR-Turbo) report $\rho_1$ and $m$ beside the score; HCN-style teacher selection moves from greedy set cover to $\hat p$ differences with a replicate rule; the recoverable target of a consolidation stage becomes the strict-drop count, about a fifth of the headline; RL frameworks' per-checkpoint validation adopts a two-stage draw rule (one draw on settled cells, more where draws disagree); L1's pass^k-across-versions reading extends to checkpoints as versions.
- **If false:** If strict drops are at least half of the gap: forgetting within one RL run is a large, problem-specific property of the policy, the greedy ruler over-counts by under 2x, and the record is a footnote licensing it with the first variance-component card for an RL run. If the draw facet is empty (90% of cells settled at $T = 1$): the policy is near-deterministic at its own training temperature (the Sharpening Tax reading, 2610.01509), the greedy gap is argmax churn under parameter updates, the persistence statistics become the forgetting measurement, and Temporal Sampling at $T > 0$ recovers nothing one checkpoint's sampling would not.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** The same consumers as C-W46-13, reached a week earlier for $20: the Agentic-OPD recovery accounting (sec. 4.3) and the Temporal Sampling greedy choice (sec. 2.2) are the sentences the floor is set against. Who pays: whoever is about to buy a consolidation stage on the strength of the 62% headline.
- **Impact ceiling:** **floor**: A three-number note ($\delta_0$, $f$, $\rho_1$) for one public RL'd agent, cited by the G-study and by the next forgetting paper. Judgment 0.6.; **middle**: The stationary reference brackets the published 62% gap from below with no training, so the headline is read with a floor before C-W46-13 runs. Judgment 0.3.; **ceiling**: None beyond C-W46-13's: this is its step 0.
- **Relevance:** As C-W46-13; Jacob's edge: the stationary-reference arithmetic and the Bernoulli floor are napkin identities; a first result in a weekend.
- **Kill probe:** About 8 GPU-h, $20, 3 days; kills CL-W46-05 if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$.
- **Density and ownership:** Same searches as C-W46-13: no fetched source reports a same-checkpoint floor on a forgetting set. Occupied: the paper's greedy table and recovery count; 2602.07150 (pipeline precedent) owns temperature-0 variance as serving arithmetic in general, not on an agent checkpoint table. The Search-R1 authors hold the checkpoint; the Agentic-OPD authors hold 100.
- **Why now:** As C-W46-13; the public checkpoint makes it free of training.
- **Register, and what it is not:** A noise-floor measurement and a bracket; the cheapest first move under CL-W46-05. It is not the G-study (no checkpoint facet), not a verdict on forgetting, and not a claim about Qwen3-4B (the paper's recovery backbone): it transfers the floor by the arithmetic above.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper. Every premise number is fetched and dated (2,808 vs 4,553 at step 500, HotpotQA, Qwen2.5-3B-Instruct, 100 checkpoints, sec. 2; 60/45/15 of 2,000 on Qwen3-4B, sec. 4.3; TFS 6.4-56.1%, 2505.20196 sec. 2.2 per the import; Pass@k gain 4-19 points, abstract). Conditioning set written: fixed task set, retriever index and prompt, so the environment is deterministic given the action sequence and there is no luck term; whose temperature: at $T = 0$ the draw facet is zero up to serving arithmetic (measured by C-W46-14's $\delta_0$) and the greedy gap is a property of the (policy argmax,… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W46-14 at about 8 GPU-h kills the claim before any training if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$; C-W46-13 at about 150 GPU-h (under one GPU-week) kills it if strict drops are at least 0.5 of the gap (lower bound above 0.35) or 90% of cells are settled. Both outcomes informative: the kill result is the first noise floor for a forgetting score either way. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B, the ruler route: the forgetting score is a widely used fuzzy notion made measurable by a per-cell success probability under the stated protocol (identifiable at $T > 0$ with $m$ draws; computable from data the Temporal Sampling authors already hold, $r_{i,j}$ at 64 samples on 8 checkpoints). Pre-registered surprise written three ways: expected (coin-flip share at least 0.5, strict drops at most 0.2; judgment 0.55), field assumes (the gap is lost capability; greedy removes variability), belief-changing (a draw floor beside every forgetting score; the recoverable target a fifth of the… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Pass at one community with a second adjacent: (1) checkpoint-consolidation and temporal-ensembling recipe authors — build the gain matrix from $\hat p$ differences with a replicate rule, report the strict-drop count; (2) L2 training-dynamics measurers (2509.12235, 2602.03073, Temporal Sampling) — report $\rho_1$ and $m$ beside a forgetting score; (3) RL-framework validation and checkpoint-selection tooling (L1) — two-stage draws, publish the probability table rather than the greedy set; (4) training teams deciding whether to buy a consolidation stage — price it against the strict-drop count.… |
| G4 | mechanism and consequence | Mechanism written: GRPO at 3B over four-turn retrieval leaves a wide band of problems at intermediate success probability; a few RL steps move near-tied argmaxes without moving probabilities; the first greedy success puts such a problem into $U_{\geq 1}$ within a few checkpoints and the final greedy decode fails with probability about $1 - p$, so the union-versus-final gap is large with no probability change. Consequence per outcome: coin flips dominate — report the floor, select teachers on $\hat p$, target the strict drops; strict drops dominate — the greedy ruler stands within 2x and conso… |
| G5 | durability; lab-adjacent | Pass with a flag: the ruler (a per-cell probability with a draw floor) applies to any run that saves checkpoints and survives the next model generation; the 3B HotpotQA numbers expire with the next recipe. Lab-adjacent: a measurement of a published ruler, not a recipe fight. Race flag: the Temporal Sampling authors hold the data to compute the split in a day. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17). Role words for the search, in the neighbours' vocabulary: temporal forgetting, forgetting score, forgotten problems, checkpoint ensemble, temporal sampling, historical checkpoints, best-validation checkpoint, greedy decoding, pass@k across checkpoints, sampling variance, test-retest, intraclass correlation, variance components, generalizability, noise floor, repeated sampling, success probability per problem, always/never solved, sharpening, oscillate, flicker, churn. W46 counts (2026-11-16): forgetting x checkpoints x RL x LLM 6 hits (on… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-14 | One public checkpoint decoded twice: the noise floor under Agentic-OPD's recovery count and the coin-flip share a 3B se… | About 8 GPU-h, $20, 3 days; kills CL-W46-05 if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$. | proposed | — |
| C-W46-13 | The checkpoint x problem x draw table of one GRPO run: what the greedy 'forgetting' gap is made of | C-W46-14 first (about 8 GPU-h, $20, 3 days), then steps 1-3 (about 150 GPU-h, $350, 12 days); dead if the strict-drop share of $G$ is at least 0.5 (lower bound above 0.35), or 90% of cells settled at $m = 8$, or temperature-0 disagreement… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-14** (Sunday run), or run `/kill C-W46-14` in a session.
2. If it survives: `/redteam C-W46-14`, then the probe as pre-registered — About 8 GPU-h, $20, 3 days; kills CL-W46-05 if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L2 lane sentence plus the card's protocol quotes); probes C-W46-14 (cheapest, 8 GPU-h) and C-W46-13 (import S12xF1, 150 GPU-h); concept-level kill search owed (rule 17); Gate 2B flagged at filing
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 5: born W46: $20 step-0 probe on a public checkpoint kills before any training; reverses the two occupants' stated reading; direction is pass@k folklore (2B flag); concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-05`, version 1)
- probe `C-W46-14`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-13`: `data/candidates/2026-W46.jsonl`
