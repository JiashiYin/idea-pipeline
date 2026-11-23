# At a matched sample count and the same teachers, SFT on 2611.01927's depth-synthesized terminal tasks ($D \geq 10$) gives Qwen3-8B no more than SFT on the shallow tasks it audited ($D \leq 3$) on Terminal-Bench 2.1 and TBLite — within two points of pass@1, inside the five-run spread — so the reported training gain is a sample-count effect and depth is not a training-data property at this scale.

`CL-W47-09` · lane **L2** · status **open** · rank — · position both · refreshed 2026-11-22

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at concept level; Gate 5 flagged (one scale); Gate 6 open until the kill search. Next action: see First steps.

## The claim

- **Headline:** At a matched sample count and the same teachers, SFT on 2611.01927's depth-synthesized terminal tasks ($D \geq 10$) gives Qwen3-8B no more than SFT on the shallow tasks it audited ($D \leq 3$) on Terminal-Bench 2.1 and TBLite — within two points of pass@1, inside the five-run spread — so the reported training gain is a sample-count effect and depth is not a training-data property at this scale.
- **Current belief (the field's):** 2611.01927 (card, full text) presents the SFT gain as the recipe consequence of depth ('2.6% to 4.9% and 3.4% to 9.1%', sec. 4.6) and recommends that 'builders of benchmarks and training data report depth alongside work' (sec. 5); the card's weakest component: 'no comparison to SFT on an equal number of samples from the audited shallow datasets, so "depth helps training" is not isolated from "more and longer trajectories help"'. The synthesis papers' premise (card neighbours): longer or deeper trajectories teach more (RST grows median solution lines 67 to 374; TMax, SETA, FACET report mean turns as the horizon measure).
- **If true:** Terminal-task synthesis papers report a matched-count shallow control before claiming a depth effect; training-data curation by depth waits for a result at a larger scale or with RL; 'depth' is read as an evaluation statistic (CL-W47-03) until a matched control says otherwise.
- **If false:** If the deep arm beats the shallow arm by at least three points of pass@1 on TBLite with the five-run spreads not overlapping, and by two on Terminal-Bench 2.1: depth is a training-data property at matched count and the paper's recommendation gains its missing control — the pre-registered alternative, itself citable.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the paper's sec. 4.6 and sec. 5; the lane's rule (L2 is watched for definitive comparisons, not recipes). Who pays: training teams buying or building synthesized terminal tasks (TMax, SETA, RST, FACET all sell training sets), and anyone deciding whether to spend generation budget on depth ($1.08 per accepted deep task, sec. 4.4) or on count.
- **Impact ceiling:** **floor**: The matched-count comparison at 8B on two public benchmarks, cited by the next synthesis paper. Requires steps 0-2. Judgment 0.5.; **middle**: Synthesis papers adopt a matched-count shallow control as the standard ablation for a depth or length claim. Requires step 3 and a second base model. Judgment 0.25.; **ceiling**: Depth becomes a reported, decision-relevant training-data statistic, or is dropped from training claims, across the terminal-agent synthesis line. Requires a 30B-class base and an RL arm. Judgment 0.1.
- **Relevance:** L2 (training dynamics; definitive comparison): direct. L1: indirect (the sibling candidate calibrates the depth label the arms are split on). Narasimhan route (RL on agents): indirect, the SFT precursor. Industry: direct for training-data vendors. Jacob's edge: the training and evaluation runs are his GPU engineering; the design is a dose-matched comparison; physics zero.
- **Kill probe:** About 60 GPU-h, $300-600, 10 days; dead if the deep arm wins by three or more on TBLite outside the five-run spread and two or more on Terminal-Bench 2.1.
- **Density and ownership:** Lab-contested lane: every terminal-task synthesis paper is a training recipe (TMax 2606.23321, SETA 2607.10891, RST 2608.05466, FACET 2608.18580, the card paper); none, per the card, runs a deep-versus-shallow control at matched count. The definitive-comparison shape is the one L2 allows from a solo position. Search words at the kill search: 'long-horizon', 'trajectory length', 'SFT data', 'task difficulty', 'curriculum', 'data efficiency', 'terminal agent', 'matched', 'ablation', 'sample efficiency', 'data mixture'. Race flag: the paper's authors can add this ablation in a v2 within weeks; the window is the time to their revision. Ownership: the authors hold the 4,941 samples and the hyperparameters; the re-open test is the release.
- **Why now:** 2611.01927 v1, 1 Nov 2026, with the cut rule and the deep tasks; the shallow task files are public. Flag: the result is bounded by an 8B model at 2-9% pass@1 and the five-run spread is written into the design.
- **Register, and what it is not:** Definitive comparison (dose-matched on sample count, token-matched as a third arm). It is not a new recipe, not a verdict on the paper's dataset quality, and not an RL result; the trained checkpoints are the measurement, not a proposed method (02_mutate's rule on learned models noted).

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched (2.6% to 4.9%, 3.4% to 9.1% on two terminal benchmarks; 105 tasks; Qwen3-8B; card sec. 4.6). Conditioning set: both arms share teachers, sample count and the SFT recipe; the five-run spread is the base model's own noise floor (2-9% for an 8B on these benchmarks, the probe's uninformative clause). Depth labels for the shallow arm are the paper's own audit labels, so the arm's contents are defined by the paper's ruler. |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: about 60 GPU-h, under one GPU-week; kill written; both outcomes informative (a matched control the synthesis literature lacks either way). Race flag: the authors' own v2 ablation is the likely occupant. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route A pressure (the card's own missing control; the synthesis papers' shared premise quoted) — the definitive-comparison shape. Surprise three ways: expected — no difference within two points (judgment 0.45); field assumes — depth helps (sec. 4.6, sec. 5); belief-changing — deep wins by $\geq 3$ on TBLite (0.35) or the 8B noise floor swallows both (0.2). Flag: 'a null at 8B' is a weak result unless the spread is small; the uninformative clause is written. |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community: terminal-task synthesis and agent-SFT data authors (matched-count control; report depth as a facet). Proper-shaped; a definitive comparison rather than a recipe. |
| G4 | mechanism and consequence | Mechanism: at 8B and about 2,000 samples, SFT gains on terminal benchmarks come from format, tool-use habits and command vocabulary, which shallow trajectories carry as well as deep ones; depth would matter only if the model learned to carry state across forced observation rounds, which SFT on a few thousand trajectories does not teach. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Flag: a result at one scale (8B) and one recipe (SFT); durable only as the control's shape. |
| G6 | ownership, density, race window; position clause | Density owed at the kill search in the synthesis community's words (long-horizon SFT data, trajectory length, task difficulty curriculum, sample efficiency, matched, ablation, terminal agent) — every synthesis paper is a recipe and lab-contested; the control is the lab-adjacent part. Why now: the first depth-labelled task set (2026-11-01). Race: the authors' ablation; window short. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-07 | Depth or count: SFT on synthesized deep terminal tasks against the same number of samples from the shallow sets it audi… | About 60 GPU-h, $300-600, 10 days; dead if the deep arm wins by three or more on TBLite outside the five-run spread and two or more on Terminal-Bench 2.1. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W47-07** (Sunday run), or run `/kill C-W47-07` in a session.
2. If it survives: `/redteam C-W47-07`, then the probe as pre-registered — About 60 GPU-h, $300-600, 10 days; dead if the deep arm wins by three or more on TBLite outside the five-run spread and two or more on Terminal-Bench 2.1.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): the matched-count control the card paper did not run; concept-level kill search scheduled this run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-09`, version 1)
- probe `C-W47-07`: `data/candidates/2026-W47.jsonl`
