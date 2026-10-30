# Where reward hacking starts under GRPO is readable from the untrained model: the few prompts it occasionally hacks but cannot solve seed the hacking, and removing them delays onset more than removing matched-difficulty prompts.

`CL-W43-13` · lane **L2** · status **open** · rank 8 · position solo · refreshed 2026-10-30

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 (density unmeasured in a dense, lab-contested area); Gate 1 at the budget edge (166 GPU-h). Grade on paper: open, weak; single probe. Next action: see First steps.

## The claim

- **Headline:** Where reward hacking starts under GRPO is readable from the untrained model: the few prompts it occasionally hacks but cannot solve seed the hacking, and removing them delays onset more than removing matched-difficulty prompts.
- **Current belief (the field's):** SimHack 2610.28707 ranks hack-seeding prompts by a sender coefficient fitted from ten reference RL runs and states that 'the initial hacking rate alone does not determine onset' across recipes; RLVR data-selection pipelines filter prompts by pass rate (zero-variance groups), not by hack probability (card 2610.28707).
- **If true:** Prompt-pool curation adds a step-zero hack screen before any RL run; SimHack's fitted ranking is replaced by a free statistic; verifier hardening is targeted at the screened prompts
- **If false:** Hack rate carries nothing beyond difficulty (verifier hardening is the only lever) or hacking is diffuse (removal moves nothing) — both citable negatives

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: SimHack's abstract asks for ways to 'select lower-risk recipes in advance' and names environment hardening as 'increasingly difficult'; its Sec. 5.2 ranks hack-seeding prompts and its introduction claims 'subsequent RL runs' confirm the ranking, with no such experiment in the text (card, weakest_component). Who pays: every team training coding models with verifiers that have loopholes; the SimHack authors themselves (a cheaper ranking); curriculum designers for RLVR (reinforcement learning with verifiable rewards — the setting where the reward is a programmatic check).
- **Impact ceiling:** **floor**: A negative: the step-zero quantity carries nothing beyond difficulty, or 5% removal moves nothing; a control cited by SimHack follow-ups and by anyone proposing prompt-level hack screens; requires the 12 runs; probability 0.4 (judgment).; **middle**: The $w_i$ screen works at 0.6B on one suite: a zero-fit prompt-pool screen proposed as a data step, with the identity that justifies it; requires a 4B replication (about 50 GPU-hours per run, outside the solo week) to be believed; probability 0.4 (judgment).; **ceiling**: The screen replaces fitted simulators for finding seeding prompts, predicts the seed spread of onset as a first-passage time from the top-$w_i$ prompts, and becomes a default step in RLVR data pipelines; requires two suites, 4B, and the released SimHack dataset; probability 0.2 (judgment).
- **Relevance:** **routes**: Narasimhan (Odysseus, EasyPPO) and any RL group: moderate — a credit-signal fact about GRPO's advantage at step zero, validated against a ground-truth hack label; L1 evaluators: weak (a verifier-validity measurement); L3/L4/L5: none.; **industry**: Direct: a data step for verifier-based RL on code.; **jacobs_edge**: The identity is an elementary moment computation on the group-normalised advantage, the kind of napkin check he favours; the LLM-RL stack itself is not his edge.; **zero_where**: Physics, GPU numerics, scheduling, robotics (L5); the whole L5 register is absent here.
- **Kill probe:** Pre-RL rollouts (8-12 GPU-hours) plus 3 arms x 4 seeds of 0.6B GRPO (about 156 GPU-hours), about $500 at A100 rates, 10 days including environment setup; kills if the $w_i$ arm's median $t_{50}$ falls inside the matched-random arm's seed interquartile range, or both removal arms fall inside the full pool's.
- **Density and ownership:** From the card's neighbors only: Simfluence 2303.08114 (influence via simulated loss curves; the parent method, no RL, no hack label); CoT monitoring 2503.11926 (a training-time monitor that induces obfuscation; a different lever); Countdown-Code 2603.07084 (the separable-reward testbed; seeds located in SFT data, not in the prompt pool); 2511.18397 (hacking taught then generalising; no prompt-pool structure); Wong, Engels and Nanda (monitor-based interventions; unfetched, must be read to see whether prompt removal is among them). Not in the card and owed to the kill search: the RLVR data-selection literature that filters prompts by pass rate (zero-variance prompts give zero GRPO advantage, so difficulty filtering is common) — search in its words: 'zero-variance prompts', 'pass rate filtering', 'online difficulty filtering', 'exploitable prompts', 'test-case hacking', 'verifier loophole'…
- **Why now:** SimHack 2026-10-20 (the $S_0$ data exists and is bypassed for a fitted ranking; the removal experiment is claimed and not shown); Countdown-Code March 2026 (public separable-reward environment); 13-GPU-hour 0.6B runs make the matrix solo-affordable.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-26 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: the paper's own introduction claims a removal experiment it does not report; the RLVR filtering literature's zero-variance rule is the field's stated practice |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community (RLVR training teams and verifier builders); proper-shaped, not golden |
| G4 | mechanism and consequence | pass: mechanism — the step-zero GRPO advantage mass on hacking rollouts $w_i = h_{i,0}\sqrt{(1-s_{i,0})/s_{i,0}}$ (defined in C-W43-26) is the gradient push toward hacking before any update; consequence — screen or harden those prompts |
| G5 | durability; lab-adjacent | flagged: tied to GRPO's group structure and to detectable hacking; frontier labs own the topic (race risk stated in C-W43-26's positioning note) |
| G6 | ownership, density, race window; position clause | open and at risk: the RLVR data-selection literature is dense and not in the card's neighbors; kill search must use its words (zero-variance prompts, pass-rate filtering, exploitable prompts, test-case hacking); position solo in a lab-contested lane — survives only as a controlled comparison |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-26 | Hack-seeding prompts are readable from the base model's rollouts | Pre-RL rollouts (8-12 GPU-hours) plus 3 arms x 4 seeds of 0.6B GRPO (about 156 GPU-hours), about $500 at A100 rates, 10 days including environment setup; kills if the $w_i$ arm's median $t_{50}$ falls inside the matched-random arm's seed i… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-26** (Sunday run), or run `/kill C-W43-26` in a session.
2. If it survives: `/redteam C-W43-26`, then the probe as pre-registered — Pre-RL rollouts (8-12 GPU-hours) plus 3 arms x 4 seeds of 0.6B GRPO (about 156 GPU-hours), about $500 at A100 rates, 10 days including environment setup; kills if the $w_i$ arm's median $t_{50}$ falls inside the matched-random arm's seed interquartile range, or both removal arms fall inside the full pool's.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run so L2 has an open claim (portfolio rule); single-probe claim, flagged
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 8 (unchanged)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-13`, version 2)
- probe `C-W43-26`: `data/candidates/2026-W43.jsonl`
