# On a Search-R1-recipe GRPO run (Qwen2.5-3B-Instruct, HotpotQA, four turns), at least half of the problems the greedy union-versus-best gap calls 'forgotten' are coin-flip cells — success probability between 0.2 and 0.8 at the best checkpoint under eight draws at the RL temperature — and at most a fifth are strict probability drops (above 0.8 at some earlier checkpoint, below 0.2 at the best).

`CL-W46-05` · lane **L2** · status **open** · rank 5 · position both · refreshed 2026-11-16

## Status

Open claim. Probe C-W46-14 survived the kill search; red team owed before anything is called proper. Failing gate: Gate 6 not yet established (kill search owed); Gate 2B flagged (the direction is plausible from pass@k folklore; the magnitude and the three-way split are the content). Next action: see First steps.

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
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W46-05.md): survived-kill; gate failed none; occupied_by none; why not done: Enabling pieces: Agentic-OPD (2026-11-09) made the greedy gap a training target; the split-generation placebo statistic (2609.22547, 2026-09-18) is a ready estimator; the public Search-R1 3B GRPO checkpoint (Hub listing fetched 2026-11-16) removes training from step 0; the data owners built methods on the gap and the replicate-aware papers asked other questions.. Previous: Unmeasured: concept-level kill search owed (rule 17). Role words for the searc… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-14 | One public checkpoint decoded twice: the noise floor under Agentic-OPD's recovery count and the coin-flip share a 3B se… | About 8 GPU-h, $20, 3 days; kills CL-W46-05 if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$. | survived-kill | survived-kill ([record](../../../data/reports/2026-W46-kill-CL-W46-05.md)) |
| C-W46-13 | The checkpoint x problem x draw table of one GRPO run: what the greedy 'forgetting' gap is made of | C-W46-14 first (about 8 GPU-h, $20, 3 days), then steps 1-3 (about 150 GPU-h, $350, 12 days); dead if the strict-drop share of $G$ is at least 0.5 (lower bound above 0.35), or 90% of cells settled at $m = 8$, or temperature-0 disagreement… | redesign-owed | redesign-owed ([record](../../../data/reports/2026-W46-kill-CL-W46-05.md)) |

## Kill search

### Concept level (CL-W46-05) — survived-kill (2026-11-15)
Weak survival: no fetched source splits a greedy checkpoint gap by a draw floor or states most of it is single-decode noise, but the direction (finite-sample solved status is stochastic; flips are partly sampling noise, partly drift) is written in the same search-agent GRPO setting by 2606.10709 and the same-checkpoint placebo statistic is published (2609.22547 sec. 4.3); what survives is the magnitude (half coin flips, a fifth strict drops) and the three-way split, with a race flag (Temporal Sampling authors hold the data).
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
**Why not done before:** Enabling pieces: Agentic-OPD (2026-11-09) made the greedy gap a training target; the split-generation placebo statistic (2609.22547, 2026-09-18) is a ready estimator; the public Search-R1 3B GRPO checkpoint (Hub listing fetched 2026-11-16) removes training from step 0; the data owners built methods on the gap and the replicate-aware papers asked other questions.
Closest neighbors (one-sentence trick; one-line difference):
- `2606.10709` Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries Du… — On GRPO for an LLM search agent, keep prompts whose rollout group was all-correct or all-wrong in a pool and resample them later, because their status flips as the policy moves. *Difference:* States the direction in the claim's own setting (finite-rollout status is 'a stochastic observation'; about 20% of queries flip; flips partly 'sampling noise', partly drift) on training queries with K=4/8 groups; no greedy table, no validation gap set, no spl…
- `2609.22547` When Pass@k Crossovers Are Real - and Why: Paired Inference and the Markov Kernel of RLVR — Test RL-versus-base pass@k crossovers by a paired prompt-level bootstrap and show per-prompt success probabilities disperse after RL via a split-generation covariance test whose placebo is two halves of the same model. *Difference:* Owns the same-checkpoint placebo as noise floor and the replicated per-prompt dispersion finding, base-versus-RL on math and code; no intermediate checkpoints, no greedy table, no forgetting set; 'multi-turn agentic or tool-use settings remains open'.
- `2505.20196` Temporal Sampling for Forgotten Reasoning in LLMs — Count final-checkpoint errors some earlier checkpoint got right (6.4-56.1%) and spread the k samples over several checkpoints to raise pass@k by 4-19 points. *Difference:* The occupant of the greedy forgetting score and the oscillation reading; chose greedy 'to minimize variability'; holds 64 samples on 8 checkpoints for its method and never applies them to the score; no draw floor, no split.
- `2611.12799` Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agent… — Keep every GRPO checkpoint, mark greedy-solved validation problems, and distill the best checkpoint toward the earlier one covering most of its current failures. *Difference:* The seed; greedy gap as training target; 60 recovered / 45 lost of 2,000 read as consolidation; no repeated decode of any checkpoint.
- `2610.01509` Sharpening Tax in Post-Training — Measure with 128 rollouts per task how post-training pushes per-task success probabilities to always or never solved, and tax the lost retry value. *Difference:* The competing reading (few coin-flip cells after RL), base-versus-post-trained on 14 pairs with a Lost/Gained/Both/Neither split at 128 rollouts; its own RL runs select the best-validation checkpoint without a checkpoint table; smaller backbones keep more int…
*Search degraded:* ['s2', 'conference-exports-not-built', 'Q11 arXiv 503 twice', 'gh issue bodies 403 (titles only)']

### C-W46-14 — survived-kill (2026-11-15)
A claim, weak: the three-way split (strict drop / coin flip / argmax flip) of a greedy checkpoint gap with a same-checkpoint draw floor, pre-registered at half and a fifth; the direction alone is a footnote already written by 2606.10709 and 2609.22547.
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched

### C-W46-13 — redesign-owed (2026-11-15)
A claim, weak: the three-way split (strict drop / coin flip / argmax flip) of a greedy checkpoint gap with a same-checkpoint draw floor, pre-registered at half and a fifth; the direction alone is a footnote already written by 2606.10709 and 2609.22547.
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Red team **C-W46-14** (`/redteam C-W46-14`): three personas with fetched evidence; it survives only with no unanswered objection.
2. If it survives: run the probe exactly as pre-registered — About 8 GPU-h, $20, 3 days; kills CL-W46-05 if $f < 0.12$ (upper bound below 0.17) with $\delta_0 < 1\%$.
3. Write the result into the probe's record and this Log; the claim's status moves only on evidence.
4. Then `/report C-W46-14` (eight sections, three decisions), and the next probe under this claim by cost.

## Decisions for Jacob

- Spend a session on the red team of C-W46-14 now, or wait for the next automatic run? (write `promote` or leave it)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L2 lane sentence plus the card's protocol quotes); probes C-W46-14 (cheapest, 8 GPU-h) and C-W46-13 (import S12xF1, 150 GPU-h); concept-level kill search owed (rule 17); Gate 2B flagged at filing
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 5: born W46: $20 step-0 probe on a public checkpoint kills before any training; reverses the two occupants' stated reading; direction is pass@k folklore (2B flag); concept-level kill search runs this week (rule 17)
- 2026-11-15 — claim open: concept-level kill search (data/reports/2026-W46-kill-CL-W46-05.md): survived-kill — gate none; Weak survival: no fetched source splits a greedy checkpoint gap by a draw floor or states most of it is single-decode noise, but the direction (finite-sample solved status is stochastic; flips are partly sampling noise, partly drift) is written in the same search-agent GRPO setting by 2606.10709 and th…
- 2026-11-15 — C-W46-14 survived-kill: claim-level kill search of CL-W46-05 (data/reports/2026-W46-kill-CL-W46-05.md): survived-kill — Run as written plus a split-half placebo and an m=16 sensitivity row on the 0.2/0.8 band edges; state the transfer assumption from the public final checkpoint.

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-05`, version 2)
- probe `C-W46-14`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-05.md`
- probe `C-W46-13`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-05.md`
