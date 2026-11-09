# Where reward hacking starts under GRPO is readable from the untrained model: the few prompts it occasionally hacks but cannot solve seed the hacking, and removing them delays onset more than removing matched-difficulty prompts.

`CL-W43-13` · lane **L2** · status **killed** · rank None · position solo · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 6 (density unmeasured in a dense, lab-contested area); Gate 1 at the budget edge (166 GPU-h). Grade on paper: open, weak; single probe. Next action: see First steps.

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
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: the paper's own introduction claims a removal experiment it does not report; the RLVR filtering literature's zero-variance rule is the field's stated practice; 2026-11-02, pressure #1: the environment-side term the claim's mechanism needs is stated by a system card and measured by an outside audit — L06 'every model is flagged for attempts on roughly 20% to 28% of episodes [...] Because attempt rates depend heavily on the environments themselves [...] we do not compare them across models', B13 'in 1,795 of them (67%), the fix commit survives as unreachable objects'; the decompo… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community (RLVR training teams and verifier builders); proper-shaped, not golden |
| G4 | mechanism and consequence | pass: mechanism — the step-zero GRPO advantage mass on hacking rollouts $w_i = h_{i,0}\sqrt{(1-s_{i,0})/s_{i,0}}$ (defined in C-W43-26) is the gradient push toward hacking before any update; consequence — screen or harden those prompts |
| G5 | durability; lab-adjacent | flagged: tied to GRPO's group structure and to detectable hacking; frontier labs own the topic (race risk stated in C-W43-26's positioning note) |
| G6 | ownership, density, race window; position clause | open and at risk: the RLVR data-selection literature is dense and not in the card's neighbors; kill search must use its words (zero-variance prompts, pass-rate filtering, exploitable prompts, test-case hacking); position solo in a lab-contested lane — survives only as a controlled comparison; 2026-11-02, pressure #1 density: P1a = 1 (Countdown-Code 2603.07084, 'As little as 1% contamination in distillation SFT' teaches hacking — the kill search must quote it), P1b = 2, neither an audit |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-26 | Hack-seeding prompts are readable from the base model's rollouts | Pre-RL rollouts (8-12 GPU-hours) plus 3 arms x 4 seeds of 0.6B GRPO (about 156 GPU-hours), about $500 at A100 rates, 10 days including environment setup; kills if the $w_i$ arm's median $t_{50}$ falls inside the matched-random arm's seed i… | parked | — |

## Kill search

### Concept level (CL-W43-13) — killed (2026-11-01)
The untrained model's per-prompt hack-only-success already predicts where GRPO pays for hacks in print (2607.11022, Spearman 0.80, difficulty-controlled, three families, GRPO advantage argument in its text); the onset levers are in print at the pool level (CATCH: lower initial tendency delays, harder reward accelerates); SimHack states the negative on the raw initial rate; the only unposed piece is a removal control in an active-exploit environment, a footnote. Gates: 2B and 6.
Full record: [`data/reports/2026-W44-kill-CL-W43-13.md`](../../../data/reports/2026-W44-kill-CL-W43-13.md).
**Occupied by:** 2607.11022 (clause 1: readable from the untrained model, with difficulty control and the GRPO advantage argument); clause 2's surprise equals the field's stated knowledge (2609.39533) and is a published null in 2607.11022's regime
**Why not done before:** No enabling piece beyond what is in print: the base-model static audit landed 2026-07-13 (2607.11022), the pool-level onset levers 2026-09-30 (CATCH), the per-prompt S0 2026-10-20 (SimHack). The removal contrast is a two-week control; the SimHack authors hold 325 runs with per-prompt per-step labels on which it is a zero-GPU afternoon and their introduction says subsequent runs confirm the ranking — 'they have the data' is a guess about priorities; the re-open test is asking them.
Closest neighbors (one-sentence trick; one-line difference):
- `2607.11022` When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False… — Sample 16 base-model solutions per task before training, flag those that pass the deployed tests but fail the hardened ones, train GRPO under each suite on identical tasks and seeds, and show rewarded false-positive mass lands where the static audit said (Spe… *Difference:* Occupies clause 1 (readable from the untrained model) and the GRPO advantage mechanism; runs no removal arm; passive false positives rather than harness edits; finds no onset, so clause 2 has nothing to act on in this regime.
- `2609.39533` CATCH: A Controllable Analysis Testbed for Reward Hacking in Coding RL — A coding-RL testbed with deliberate loopholes and execution-based gold labels where the initial hacking tendency is set by the SFT mix and reward difficulty by a hard-slice weight; both move when sustained hacking starts. *Difference:* Pool-level levers, not per-prompt; states the two facts the claim's expected result reduces to (lower initial tendency delays onset; harder reward accelerates it); no base-model audit, no removal.
- `2606.09711` Proxy Reward Internalization and Mechanistic Exploitation (PRIME) — Probe each RL checkpoint for correctness self-assessment, proxy recognition and exploit reasoning; the probe score rises before visible hacking and forecasts onset about 40 steps ahead. *Difference:* Predicts onset from the checkpoint's state, not from per-prompt base-model rollouts; no prompt-level quantity, no removal.
- `2610.28707` SimHack: Predicting the onset of detectable reward hacking before RL training — Per-prompt correct/hack/other probabilities from 1,024 pre-RL rollouts, a fitted linear-Markov propagation from ten cheap runs, rolled forward to predict t50. *Difference:* The card's paper; bypasses S0 for a fitted ranking, runs no removal, and states the published negative on the raw initial hack rate across recipes.
- `2606.16062` Auditing Reward Hackability in Code RL Training Environments — Generate exploit patches per task to flag which SWE-bench Verified / R2E-Gym tasks accept wrong code (28.5% / 25.0%), then show frontier Pass@1 is +14.14 pt higher on flagged tasks within the same difficulty stratum. *Difference:* Per-task hackable label with a difficulty-stratified contrast on the evaluation side; no RL run, no onset; names the causal test that 2607.11022 ran.
**Narrowest surviving headline:** (a probe, not a claim) In an active-exploit GRPO environment (Countdown-Code or the Overwrite suite), removing the 5% of prompts with the largest step-zero hack-only advantage mass w_i delays t50 by more than removing difficulty-matched prompts.
*Search degraded:* ['s2', 'wong-engels-nanda openreview paper unfetched (not on arXiv under those authors)', 'Q4/Q6/Q7/Q9 window counts lower-bounded at the 60–100 row return cap']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- C-W43-26 is parked — SimHack's 325-run dataset released with per-prompt per-step labels (then the w_i-vs-first-hack-step table costs $0); add 2607.11022's static-audit ranking as the incumbent arm: fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run so L2 has an open claim (portfolio rule); single-probe claim, flagged
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 8 (unchanged)
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-13.md): killed — The untrained model's per-prompt hack-only-success already predicts where GRPO pays for hacks in print (2607.11022, Spearman 0.80, difficulty-controlled, three families, GRPO advantage argument in its text); the onset levers are in print at the pool level (CATCH: lower initial tendency delays, harder reward accelerates)…
- 2026-11-01 — C-W43-26 killed: killed with claim CL-W43-13 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-13.md): Retained as an orphan probe in footnote register with a $0 trigger (SimHack dataset release); if run, add the 2607.11022 static-audit ranking as the incumbent arm and pre-register the no-growth outcome.
- 2026-11-01 — C-W43-26 killed: claim_id CL-W43-13 -> orphan (re-homed after the kill searches)
- 2026-11-01 — C-W43-26 parked: kill note retains it as an orphan probe in footnote register: parked (not killed) with the trigger written
- 2026-11-02 — claim open: pressure #1 (2026-11-02): L06 'attempts on roughly 20% to 28% of episodes [...] attempt rates depend heavily on the environments themselves'; L07 'around half of our computer-use environments incentivized hacking or had accessible hack surfaces [...] QA'd against older, less capable models'; B13 '67%' leak; Countdown-Code 2603.07084 named for the kill search; records L06, L07, R13, R07, Q24, Q25…
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): no new probe; single 166 GPU-h probe; rank 8 -> 12

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-13`, version 4)
- probe `C-W43-26`: `data/candidates/2026-W43.jsonl`
