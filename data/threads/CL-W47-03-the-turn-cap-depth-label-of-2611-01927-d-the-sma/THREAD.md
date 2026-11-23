# The turn-cap depth label of 2611.01927 ($D$, the smallest stated cap under which a task passes) is a property of the measuring panel above a cap of ten: its index of dependability $\Phi$ for the deep/shallow cut is under 0.5 above the three-turn floor, a four-model minimum lowers at least 30% of the released labels, and in passing runs on the median-depth-40 tasks fewer than one turn in three is newly informed by the previous output.

`CL-W47-03` · lane **L1** · status **open** · rank — · position solo · refreshed 2026-11-22

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at concept level; Gate 6 open until the kill search. Next action: see First steps.

## The claim

- **Headline:** The turn-cap depth label of 2611.01927 ($D$, the smallest stated cap under which a task passes) is a property of the measuring panel above a cap of ten: its index of dependability $\Phi$ for the deep/shallow cut is under 0.5 above the three-turn floor, a four-model minimum lowers at least 30% of the released labels, and in passing runs on the median-depth-40 tasks fewer than one turn in three is newly informed by the previous output.
- **Current belief (the field's):** 2611.01927 (card, full text) states the dependence qualitatively and bounds it from one side: 'Unlike the idealized $D^{*}$, $D$ depends on the models, the harness and the single state $e_0$, so it is an estimate rather than a bound' (sec. 2); 'a model that merges poorly overestimates the depth' (sec. 3.1); adding GLM-5.3-Flash lowers $D$ on 40 of 160 existing tasks, 32 by one cap (App. E.1); the recommendation is that 'builders of benchmarks and training data report depth alongside work' (sec. 5), with $D$ read from one or two runs per (model, cap) and the measuring models' temperature 'default of the provider' (App. I). The synthesis papers (TMax 2606.23321, SETA 2607.10891, RST 2608.05466, FACET 2608.18580, per the card) report mean turns or solution lines as the horizon measure.
- **If true:** A depth or horizon label on an agent task suite names its measuring panel as a fixed facet and carries $\Phi$; certifying a label to one grid level takes about 7 runs at the cap below it, not 2; 'long-horizon' claims in synthesis papers report the model-free forced-round count (the key steps the generator planted) beside $D$; the 2611.01927 audit's 94%-within-three-turns result stands (it is at the floor, where $\Phi$ is high).
- **If false:** If $\Phi \geq 0.8$ everywhere and labels move within one grid level: depth is the task's and the cheap one-model protocol is a valid reading — a citable certification the paper lacked. If the newly-informed share is at least one half: the turns beyond the designed key steps are rounds drawing on undesigned environment surprises, and synthesized depth is real but comes from the environment, not the key steps (the pre-registered alternative headline, itself recipe-changing).

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the paper's sec. 5 recommendation and its uncounted gap (sec. 4.2); its own one-sided robustness check (App. E.1). Who pays: the benchmark owners audited as shallow (TMax, SETA, RST, FACET), who need to know whether $D$ reads their tasks or the auditor's models; training-data builders choosing tasks by depth; Terminal-Bench and TerminalWorld maintainers, whose human-curated tasks were audited under a harness not their own.
- **Impact ceiling:** **floor**: The $F$ / $2K + 1$ / $D$ table on 54 tasks plus the TMax column, cited by the paper's v2 and the next synthesis paper. Requires steps 0-2. Judgment 0.55.; **middle**: A model-free depth column (the provenance count from trajectories) adopted beside $D$ by one benchmark or synthesis pipeline. Requires a second harness and the human-curated sets. Judgment 0.25.; **ceiling**: 'Depth' on terminal benchmarks reported as forced rounds read from trajectories, with the cap-depth retired above ten; the synthesis recipes redesigned around whichever source of depth the count finds. Requires two more datasets and an owner's adoption. Judgment 0.1.
- **Relevance:** L1 (benchmark validity: what 'long-horizon' measures): direct. L2: indirect (which tasks are worth training on; the sibling candidate). Narasimhan route: indirect. HAL: indirect (Terminal-Bench cells). Systems: zero. Jacob's edge: the work / depth decomposition is parallel computing (Blelloch), his computer-engineering ground; the provenance scan is deterministic text work; physics zero.
- **Kill probe:** $0-100, 0 GPU-h, 6 days; dead if the newly-informed share is at least one half or $F \geq 2(2K + 1)$ on half the tasks with retry share under 0.2, or kappa under 0.6.
- **Density and ownership:** Occupant of the ruler: the card paper ($D$ by stated cap). Nearest, from the card: RST 2608.05466 (solution lines as the horizon measure; median 67 to 374 lines), TMax 2606.23321 and SETA 2607.10891 (mean turns, 16.3 and difficulty labels), FACET 2608.18580 (11.86 mean turns), TerminalWorld 2605.22535 (tasks from real recordings). Inference, no fetch this week: no paper counts per-turn information use from trajectories as a depth measure; density is measured at the kill search in the neighbours' words — 'adaptive', 'rounds of interaction', 'interaction depth', 'sequential dependency', 'trajectory analysis', 'turn-level', 'retry', 'error recovery', 'long-horizon benchmark', 'horizon length', 'action dependency'. Ownership: the authors hold the tasks, the key-step record and the runs; the re-open test is the release.
- **Why now:** 2611.01927 v1, 1 Nov 2026: the first task set with both a designed forced-round record and a measured depth; TMax's released runs give the shallow comparator at $0. Flag: the probe is a sketch until the dataset link resolves.
- **Register, and what it is not:** Measurement calibrating a shipped ruler against a model-free count. It is not a new synthesis pipeline, not a re-audit of the six datasets with $D$, and not a verdict on whether synthetic sets are shallow.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched with denominators (734 tasks audited, 94% of solved synthetic tasks within three turns, 40 of 160 labels lowered, 11 of 40 'deep' existing labels pushed below 5, Spearman 0.91 part-whole over 361/401 shared readings with 241 pinned at $D = 1$, 333 of 734 never passed — card and import, full text). Conditioning set: $D$ is a reading of a (task x model x cap x run) design; the model's temperature is the provider default and unstated (flag: the card's regime field should carry this; added to the digest). Quantifiers pre-registered ($\Phi < 0.5$; 30%; one in… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W47-06 is $0-100 and six days; the import's G-study is about $1,000 of API and no GPU. Kills written; both outcomes informative. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'depth' and 'long-horizon' made measurable with a dependability index and a model-free forced-round count. Surprise three ways: expected $\Phi < 0.5$ above the floor, $\geq 0.8$ at it, a four-model min lowers $\geq 30\%$ of labels (judgment 0.45); field assumes $\Phi \geq 0.8$ everywhere, moves within one grid level (0.30); belief-changing: run residual dominant, same-model label agreement under 0.5 at $D \geq 40$ (0.25). Flag: the owners state the model dependence qualitatively (sec. 2, 3.1, 4.2), so the number and the two-way alternative headline carry the surprise; the kil… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: terminal-task synthesis authors (report $\Phi$ and the forced-round count), benchmark builders adopting 'depth' as a column (name the panel), training-data curators selecting by depth (CL-W47-09), L1's horizon-measurement thread. Proper-shaped. |
| G4 | mechanism and consequence | Mechanism: $D_\tau = \min_m \min\{T : \max_{r \leq 2} X_{\tau m T r} = 1\}$ is an extreme statistic over a panel, upward-biased in the panel size and in the model's retry habit; a model that fails to merge turns, waits on slow output or retries inflates $D$ with no task-forced round behind it; at the floor ($D \leq 3$) the min saturates and the label is stable. Consequence per outcome written above. |
| G5 | durability; lab-adjacent | Durable: $\Phi$ and the forced-round count apply to any horizon label; flag — the released tasks and the measuring panel are 2026 models. |
| G6 | ownership, density, race window; position clause | Import's density: F1 words x label words x agents 1 hit (2512.06710, ICC for scores); horizon-measurement role words 23 (only the card paper on point); difficulty-label / IRT words 14 (2604.00594, 2603.23749, 2608.00355, 2610.41089 — IRT papers assume difficulty is the item's). No fetched source computes a reliability coefficient for an agent-task difficulty or horizon label. Kill search owed in the synthesis community's words (turn budget, interaction depth, trajectory length, horizon, difficulty label, LLM-labelled difficulty). Why now: the first depth-synthesis pipeline and audit (2026-11-… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-06 | Where the forty turns go: a hindsight provenance count of forced rounds against the turn-cap depth of synthesized deep… | $0-100, 0 GPU-h, 6 days; dead if the newly-informed share is at least one half or $F \geq 2(2K + 1)$ on half the tasks with retry share under 0.2, or kappa under 0.6. | proposed | — |

Also under this claim (no scorecard yet): import:2026-W47-S5xF1 (about $1,000 API, 0 GPU-h, 7 d: 60 tasks x 4 models x 8 caps x 4 runs = 7,680 capped runs in terminus-2, variance components, $\Phi$, Ne…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W47-06** (Sunday run), or run `/kill C-W47-06` in a session.
2. If it survives: `/redteam C-W47-06`, then the probe as pre-registered — $0-100, 0 GPU-h, 6 days; dead if the newly-informed share is at least one half or $F \geq 2(2K + 1)$ on half the tasks with retry share under 0.2, or kappa under 0.6.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up, third L1 claim under the three-probes rule): banter card 2611.01927 plus import S5xF1; concept-level kill search scheduled this run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-03`, version 1)
- probe `C-W47-06`: `data/candidates/2026-W47.jsonl`
