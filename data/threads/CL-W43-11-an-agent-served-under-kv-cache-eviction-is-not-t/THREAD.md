# An agent served under KV-cache eviction is not the agent its transcript describes: it keeps using tool outputs it can no longer see, and a trainer recomputing log-probabilities from the text does not reproduce the policy it sampled from.

`CL-W43-11` · lane **L3** · status **open** · rank 6 · position both · refreshed 2026-10-29

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established. Grade on paper: open pending kill search. Next action: see First steps.

## The claim

- **Headline:** An agent served under KV-cache eviction is not the agent its transcript describes: it keeps using tool outputs it can no longer see, and a trainer recomputing log-probabilities from the text does not reproduce the policy it sampled from.
- **Current belief (the field's):** Agentic-RL stacks and the cache-engineering paper treat the visible token sequence as the policy's input: 2610.28577 names training under cache operations as future work and benchmarks drop/reposition only against threshold summarization, never against the same drop done as text (card 2610.28577, Table 1 and sec. 3.2).
- **If true:** Trainers log the operation sequence, not the token sequence, or forbid eviction during rollouts; the +1.7-point cache-operations margin is re-read as ghost information; off-policy corrections (the engine-trainer mismatch literature) gain a second, larger term.
- **If false:** KV drop equals text drop within 3 points and post-drop divergence is within 2x the numerical baseline: cache operations are a pure cost lever and trainers can keep recomputing from text.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2610.28577 writes down the history dependence and names training under it as future work; import S6xF7 names cache engineering as a training-throughput lever once KV residency is shown to bind. Who pays: agentic-RL systems teams that want eviction or compaction inside rollouts without training a different policy than the one that acted; serving teams who must know whether an operation log is a required part of the trajectory record.
- **Impact ceiling:** **floor**: A null: the divergence is within the numerical mismatch band and cache eviction is free for trainers; a citable footnote that unblocks the KV-residency lever inside RL; probability 0.15 (judgment).; **middle**: A ruler with numbers on two models: trainers must reproduce the operation sequence or carry it in importance weights; adopted as a check by one open agentic-RL stack; requires the two models and the trainer-side reproduction demo (one prefill per trajectory on AKV); probability 0.55 (judgment).; **ceiling**: The divergence is shown to change a training outcome: the same rollouts trained with text recompute versus operation-aware recompute diverge in pass rate on one task family (an added ~150 GPU-h training run, lab position preferred); the operation log becomes a standard field of agentic-RL trajectory records; probability 0.2 (judgment).
- **Relevance:** **routes**: L3 systems route: train-serve consistency for RL infrastructure, direct. L2 (Narasimhan, RL groups): the consumer of the result. L4: cache-level compaction as a training problem. L1: none.; **industry**: Direct for any team serving agents with cache editing and training on the trajectories; serving-engine teams (SGLang, vLLM) decide whether to expose the operation log.; **jacobs_edge**: Direct: this is a numerics and identity question (two states with identical tokens and positions, finite-precision re-rotation error, bf16 mismatch as the unit); GPU arithmetic is his ground.; **zero_where**: L5 (robot simulation): zero.
- **Kill probe:** 90 recorded trajectories, three teacher-forced replays each, two open models, ~30 GPU-h, ~$110, 5 days; kills if post-drop divergence stays under 2x the numerical mismatch and the over-threshold token fraction does not move.
- **Density and ownership:** From the card's neighbors only: SideQuest 2602.22603 trains a side branch to issue cache deletions (215 samples) and is the one neighbor where a trained component acts on a modified cache; whether its training reproduced the modified state is the first thing to read. Context Language Models 2609.37725 trains context editing with online RL, but its edits are to text, so text recompute is exact there, which is the contrast case. The other neighbors (TokenPilot, SmoothAgent, Complexity Trap) are text-level and do not face the mismatch. The engine-trainer numerical mismatch and its importance-ratio corrections are a known body of agentic-RL systems work that the kill search must name and quote; nothing is stated about it here from memory beyond its existence as a trainer practice. Queries in the field's words: 'training-inference mismatch', 'importance sampling', 'rollout engine', 'log-prob…
- **Why now:** 2610.28577 (October 2026): the formalization, the future-work sentence and the segment-batch attention that makes teacher-forcing any operation history one prefill; import S6xF7 (2026-10-25): KV residency as the predicted binding station in agentic RL.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-25 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a systems paper that names training under cache operations as future work (2610.28577) and the engine-trainer mismatch line that agentic-RL stacks already correct for (card neighbors); route B: the ruler is per-token divergence by turn offset, computable from recorded trajectories |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass: RL infrastructure teams (log operations or forbid eviction), serving teams (whether cache ops change the policy), compaction evaluators (ghost information as a confound); community-wide only if the divergence is large |
| G4 | mechanism and consequence | pass: mechanism — attention entries computed while the tool output was visible carry its information after eviction; consequence — a logging change or an eviction ban in rollouts |
| G5 | durability; lab-adjacent | pass: a property of any KV-cache serving stack; the AKV engine is one instance |
| G6 | ownership, density, race window; position clause | open: density not measured; why now — the released AKV engine and cache-operation API (2026-10); race window unknown; lab-adjacent (systems labs publish this; frontier labs do not) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-25 | Off-policy by cache: how far the served policy under KV eviction departs from its own text | 90 recorded trajectories, three teacher-forced replays each, two open models, ~30 GPU-h, ~$110, 5 days; kills if post-drop divergence stays under 2x the numerical mismatch and the over-threshold token fraction does not move. | proposed | — |
| C-W43-24 | Ghost information: KV drop versus the same drop done as text | Step 0 teacher-forced divergence (~10 GPU-h) then two arms x 300 SWE-bench Verified tasks x 2 runs on GPT-OSS-120B (~110 GPU-h, ~$420 at $3.50 per GPU-hour, 10 days); kills if the paired 90% interval for the pass-rate difference lies insid… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-25** (Sunday run), or run `/kill C-W43-25` in a session.
2. If it survives: `/redteam C-W43-25`, then the probe as pre-registered — 90 recorded trajectories, three teacher-forced replays each, two open models, ~30 GPU-h, ~$110, 5 days; kills if post-drop divergence stays under 2x the numerical mismatch and the over-threshold token fraction does not move.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run from card 2610.28577's probes; C-W43-22 (pricing) attached to CL-W43-12 instead
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 6 (unchanged) after the kill run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-11`, version 2)
- probe `C-W43-25`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-24`: `data/candidates/2026-W43.jsonl`
