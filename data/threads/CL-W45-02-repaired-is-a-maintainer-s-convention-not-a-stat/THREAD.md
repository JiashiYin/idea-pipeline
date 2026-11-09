# 'Repaired' is a maintainer's convention, not a state of the task: on the Terminal-Bench 2.0 tasks whose instruction-test mismatch was fixed twice — Z.ai's Verified tightened the instruction, Terminal-Bench 2.1 loosened the test — the two repairs lift different agents, with the top-band minus mid-band gain (the two strongest probed models' gain minus the two middle ones') positive under the loosened test and negative under the tightened instruction, each outside the five-trial replicate interval.

`CL-W45-02` · lane **L1** · status **open** · rank 13 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; Gate 2B flagged (direction stated in print). Next action: see First steps.

## The claim

- **Headline:** 'Repaired' is a maintainer's convention, not a state of the task: on the Terminal-Bench 2.0 tasks whose instruction-test mismatch was fixed twice — Z.ai's Verified tightened the instruction, Terminal-Bench 2.1 loosened the test — the two repairs lift different agents, with the top-band minus mid-band gain (the two strongest probed models' gain minus the two middle ones') positive under the loosened test and negative under the tightened instruction, each outside the five-trial replicate interval.
- **Current belief (the field's):** 2611.08417 App. A.3 (card quote): 'when an instruction and its test disagree, Verified edits the instruction to state what the test checks, whereas Terminal-Bench 2.1 more often edits the test to accept any correct solution; stating the grader's expectation tells the agent part of the solution, while relaxing the grader leaves the task as hard as its contributor intended' — read by the paper as restoring the intended task; its abstract (fetched 2026-11-09) reads the 2.1 repairs as removed defects: 'accuracy increased by over 10 percentage points and leaderboard positions move by up to three ranks'. ABA 2605.26079 takes the maintainers' fix PR as the unique ground truth for 'broken'.
- **If true:** Continuous benchmarks publish the repair convention per task (tighten / loosen / environment) and the inter-repair delta beside the version delta; audit tools that propose repairs (ABA, the 2611.08417 workflow) report the convention they chose; CL-W44-11's content-repaired set is split by convention before any repair share is read; a lab's launch table citing a version is read with its repairs' band signature.
- **If false:** Two independent repairs of an instruction-test mismatch are interchangeable to within replicate noise: 'repaired' is a well-defined state of the task, the version delta is a property of the defect, audit workflows may pick the cheaper fix — which strengthens 2611.08417's paired re-score and the difference-in-differences design on 3.0 to 4.0.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.08417 App. A.3 (the two-convention sentence quoted above) and sec. 4 ('Agreement measures consistency rather than correctness'); the Z.ai Verified card (52.4% to 57.9% from environment fixes alone; 11 instruction fixes); the Terminal-Bench position post 'Reuse, regrade, and rerun trials as necessary' (B05, quoted on CL-W44-02); SWE-Bench Pro V2's 480 of 731 tasks 'repaired or retired' with 69 contradicting instructions (B07). Who pays: benchmark maintainers choosing how to fix a mismatch (Terminal-Bench, Harbor-Index, SWE-bench Pro), audit tools that propose repairs (ABA, the 2611.08417 workflow), and labs whose launch tables cite a version whose repairs favoured their band.
- **Impact ceiling:** **floor**: A table of per-model gains under the two repairs on the shared tasks with the band contrast, cited by the Terminal-Bench team's next changelog and by 2611.08417's v2. Requires step 1. Judgment p 0.5.; **middle**: A repair-convention column in continuous benchmarks (tighten / loosen / environment per repaired task) with the inter-repair delta as a reported uncertainty, adopted by Terminal-Bench or Harbor-Index, and CL-W44-11's design amended to split by convention. Requires step 1 plus the 3.0 to 4.0 changelog classified the same way. Judgment p 0.3.; **ceiling**: Repair as a measurement operation with its own reproducibility: inter-repairer agreement on outcomes measured across three benchmarks and used as the validity criterion for audit-and-repair tools (replacing agreement on flags), changing how 'benchmark repaired' is certified. Requires two more benchmarks with independent repairs. Judgment p 0.1.
- **Relevance:** HAL and the Terminal-Bench / Harbor route: direct — the maintainers' repair policy. Evaluators: direct. Narasimhan (tau-family): indirect (tau2-bench's criteria changes are repairs of the same kind, per the sibling card 2611.04399). Industry: moderate (every lab reporting a version). Jacob's edge: the gain identity under a difficulty shift is napkin-checkable ($\sigma(\theta - b_{\mathrm{new}}) - \sigma(\theta - b_{\mathrm{old}})$ with $\sigma$ the logistic function, $\theta$ the agent's ability and $b$ the item's difficulty, peaked at $\theta = (b_{\mathrm{old}} + b_{\mathrm{new}})/2$); GPU numerics and physics zero.
- **Kill probe:** Step 1: about $600, 0 GPU-h (or about 80 GPU-h local), 8 days including step 0; dead if the two repairs' gain vectors agree within the replicate interval on at least five tasks and the band contrast has one sign under both arms.
- **Density and ownership:** Occupied by the card: the 2.1 artifact, the paired re-score, the convention sentence, and the agreement statistics between auditors. Neighbours from the CL-W44-02 kill report and the card: 2601.08778 (text-to-SQL; per-item flips by correction type on one correction per item — the closest design), 2605.26079 ABA (filter; PR #53 as ground truth), 2506.09289 UTBoost (test additions as a tightening repair; 11 ranking changes), 2610.22760 Between Spoilers and Guesswork (hints over-specify tasks — the 'tells the agent part of the solution' mechanism measured on its own), 2609.00482 (matched-random subtests), 2604.12843 Growing Pains (anchor-item equating), 2607.15190 (few-model regimes make item-level IRT unreliable — why the probe uses band contrasts, not fitted item parameters), hf:zai-org/terminal-bench-2-verified (the other repair). Kill-search words must be the neighbours': underspecifie…
- **Why now:** Terminal-Bench 2.1 (2026-05-08) and Verified (card updated 2026-08-18) are both public with files; 2611.08417 (2026-11-05) states the convention split and adopts four of Verified's fixes, which fixes the comparison set; the project page that would hold the per-cell matrix returns 404 as of 2026-11-09, so the arms must be run. Flag: the IRT gain identity is textbook; the enabling piece is the existence of two independent repairs of the same tasks.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | 'repaired' is defined by the file diff, not the change log (checklist 2026-11-01); the three arms differ in one field on a common 2.1 image, confirmed by diff, so environment fixes cancel by construction; ability bands are the models' published 2.0 accuracies, not fitted item parameters (2607.15190: few-model regimes make item-level IRT unreliable); the harness's access to hidden tests is checked at step 0; five-trial cells carry the exact binomial interval |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: about $600 and 0 GPU-h (or about 80 GPU-h local), 8 days; kill written: the two repairs' per-model gain vectors agree within the five-trial interval on at least five kept tasks and the pooled top-minus-mid contrast has one sign under both arms |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route A: the convention split is stated in print by the repairers themselves (2611.08417 App. A.3; Z.ai's Verified card) and the maintainers' position post asks to 'Reuse, regrade, and rerun trials as necessary' — two source types; route B: the ruler (inter-repair delta and its band sign) carries a pre-registered surprise against 'a repair restores the intended task'. Flag: the paper states the mechanism's direction in prose, so the surprise is the magnitude above the replicate floor and the band signature — Gate 2B is the red team's first objection |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: benchmark maintainers (publish the convention per task), audit-tool authors (report the convention chosen), labs citing a version (read the band signature), CL-W44-11 (split its set). Population: every continuous executable benchmark — community-wide in shape |
| G4 | mechanism and consequence | mechanism: under a logistic item model the gain from a difficulty shift is $\sigma(\theta - b_{\mathrm{new}}) - \sigma(\theta - b_{\mathrm{old}})$, with $\sigma$ the logistic function, $\theta$ the agent's ability and $b$ the item's difficulty, peaked at $\theta = (b_{\mathrm{old}} + b_{\mathrm{new}})/2$: tightening the instruction lowers $b$ for agents who could nearly solve the task, loosening the test rewards agents already producing alternate correct solutions; consequence: a convention column and an inter-repair delta, or none |
| G5 | durability; lab-adjacent | durable as a measurement operation (repairs recur in every maintained benchmark); the TB 2.0 numbers expire with 2.1's successor; lab-adjacent (maintainers publish their repairs) |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: underspecified, instruction-test mismatch, spoiler, hint, over-specification, test relaxation, weak tests, re-annotation, inter-annotator agreement, correction type, verifier fix). Nearest: 2601.08778 (per-item flips by correction type, one correction per item), 2506.09289 UTBoost (test additions as tightening), 2610.22760 (hint over-specification), 2605.26079 ABA. The two repairs exist as public files since 2026-05-08 and 2026-08-18. Race: the Terminal-Bench team holds the per-trial logs. The theme lost twice at claim level in W44 (CL-W44-02 refuted… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-03 | Same defect, two repairs: tightening the instruction and loosening the test lift different agents on the Terminal-Bench… | Step 1: about $600, 0 GPU-h (or about 80 GPU-h local), 8 days including step 0; dead if the two repairs' gain vectors agree within the replicate interval on at least five tasks and the band contrast has one sign under both arms. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W45-03** (Sunday run), or run `/kill C-W45-03` in a session.
2. If it survives: `/redteam C-W45-03`, then the probe as pre-registered — Step 1: about $600, 0 GPU-h (or about 80 GPU-h local), 8 days including step 0; dead if the two repairs' gain vectors agree within the replicate interval on at least five tasks and the band contrast has one sign under both arms.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-03; chosen over C-W45-02 for L1's second slot on consumer breadth (every continuous benchmark) and durability; headline quantifier set at the band-contrast sign the probe's kill names, with the per-task count secondary; concept-level kill search owed (rule 17), reading the CL-W44-02 and CL-W44-11 reports first; ranked 13

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-02`, version 1)
- probe `C-W45-03`: `data/candidates/2026-W45.jsonl`
