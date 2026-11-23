# On RoboTwin 2.0's defect tasks, a policy optimised against the released success checker earns at least a quarter of its reported gain over its imitation initialisation on phantom states that SimAudit's Verified checker rejects, so an RL fine-tuning gain scored by a released checker is not a result until a verified checker has seen the same rollouts.

`CL-W47-08` · lane **L5** · status **killed** · rank — · position both · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G6 (occupied in mechanism within the window: 2611.08318 ran the train-against / score-under 2x2 with a verdict-only arm on RoboDojo, 2026-11-05; 2608.17423 Prism-GRPO measured the exploit cell of checker-trained RL policies on RoboTwin 2.0, 2026-08-18; 2607.09492 named the estimator NRFR), with G2B (the 'RL community assumes reward = task' sentence is contradicted in Prism-GRPO's own text; expected equals stated) and G4 (if_true equals 2611.08318's recommendation and the seed's own release) failing on the same evidence; G0 flag: SimAudit's Verified checkers are announced with no URL and not findable on GitHub or Hugging Face on 2026-11-22. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** On RoboTwin 2.0's defect tasks, a policy optimised against the released success checker earns at least a quarter of its reported gain over its imitation initialisation on phantom states that SimAudit's Verified checker rejects, so an RL fine-tuning gain scored by a released checker is not a result until a verified checker has seen the same rollouts.
- **Current belief (the field's):** Two communities assume opposite things and neither has the number (card 2611.25179, full text): the audit lineage treats the checker as ground truth — LIBERO-PRO and LIBERO-Plus score perturbed tasks with 'the benchmarks' own checkers', which 'assumes that the checker verdicts accurately reflect whether the task was completed' (sec. 2) — and the card paper frames its defects as reachability, asking 'how often released policies reach them' (sec. 4.4), finding 'the rankings stayed the same on all three benchmarks' on imitation-trained checkpoints; the words 'exploit' and 'hack' do not occur in it. The RL-fine-tuning community assumes the reward is the task (the lane's reward-hacking literature says otherwise for solvers: SimuGuard, 2610.32277 Table 2 — CL-W44-08 record — but no fetched source prices a checker's share of an RL gain).
- **If true:** RL-on-manipulation-benchmark papers report their gain under the released and a verified checker on the same rollouts; benchmark owners ship verified checkers before accepting RL submissions; the L5 lane's exploit headline is established on the scorer, where the lane's solver version died (CL-W44-08).
- **If false:** If $\phi < 0.10$ for a released checker-trained checkpoint with the phantom-share difference inside the paired interval: RL policies do not find the checker's phantom states at the gains reported, the imitation-time re-scoring stands for RL too, and the record is a footnote certifying the released checkers for RL use.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's own identifiability sentence (App. C: 'The recorded episode is the same in both cases') and its reachability frame (sec. 4.4) that stops short of training; its finding that rankings are unchanged for 15 imitation-trained checkpoints; the survey it cites ('No Free Checker', 2609.09250: verifiers' 'error rate is reported far less often than the success rate they produce', sec. 2); 2609.37771's rankings reversed by checker fixes. Who pays: RL-fine-tuning-of-VLA teams (their reported gains), the RoboTwin 2.0 / RoboCasa365 / RoboDojo owners (which checker to ship as reward), leaderboard readers, and the lane (the first exploit instance on a shipped artifact).
- **Impact ceiling:** **floor**: A 2x2 table on 8 RoboTwin tasks with $\mathrm{Phan}$, $\phi$ and $X$ for one checker-trained policy pair, with the phantom states named; cited by the card paper's v2 and by the next RL-VLA paper evaluated on RoboTwin. Requires steps 0-2. Judgment p 0.55.; **middle**: A verified-rescoring rule (phantom share beside every RL-fine-tuning gain) adopted by one benchmark owner or one RL-VLA codebase, and the Verified checker shipped as the default reward on one benchmark. Requires a released on-policy RL pair (step 2a) or the lab arm. Judgment p 0.25.; **ceiling**: The train-against / score-under 2x2 becomes the standard exploitation test for any learned-or-hand-written reward in simulated robot learning, with the checker and the solver budget as two instances of one estimator (the program note's $X$). Requires two benchmarks and an RL-VLA group's adoption. Judgment p 0.08.
- **Relevance:** Robotics and learning faculty: direct (what an RL gain on a simulated benchmark means). Engine builders: indirect (the air-gap contact report is an engine-side quantity the checker inherits). Industry (RL-VLA teams, benchmark owners): direct. HAL / evaluators (L1): indirect, the judge-validity shape. Narasimhan route: zero. Systems route: zero. Jacob's edge: the interaction identity and paired-seed statistics are his; no mechanical engineering, no new simulator; the RFT branch is standard fine-tuning code.
- **Kill probe:** Steps 0-2a: about 20 GPU-h, $40, 6 days if a checker-trained pair is released; steps 0-2b: 60-90 GPU-h, $120-200, 10 days otherwise; dead if $\phi < 0.10$ and the phantom-share difference is inside the paired interval of zero (on-policy pair), or $X$ inside the seed interval after three RFT rounds (weaker kill).
- **Density and ownership:** Occupant of the instrument: the card paper (differential re-scoring of 15 imitation-trained checkpoints, 'rankings stayed the same'); it owns $c'$ and the phantom vocabulary and did not train anything. Nearest lane precedent: CL-W44-08 (killed 2026-11-08, Gate 2B: the solver-budget 2x2's expected result equalled the field's assumption); the difference here is that two communities assume opposite signs and the quantity $\phi$ is a fraction of a published gain, so the expected result is a magnitude, not a folklore sign. Nearest cross-field precedent: UTBoost (card neighbour, 2506.09289) changed 24-41% of SWE-bench leaderboard entries by augmenting the scorer, without a training arm. Density (inference, not fetched this week): the RL-fine-tuning-of-VLA conjunction is dense (several papers a month in 2026) and none re-scores under a second checker; the reward-hacking-on-robot-benchmarks con…
- **Why now:** 2611.25179 posted 2026-11-18 with the released Verified checkers; 2609.37771 (2026-09) for the ranking-reversal precedent; the RL-VLA fine-tuning wave of 2025-26 supplying checker-trained checkpoints (to be named by the kill search). Flag: artifact-enabled, not technique-enabled.
- **Register, and what it is not:** Measurement with a mechanism (a terminal reward at the first accepting state) and a recipe consequence (which checker to train against; a phantom-share column). It is not a new RL recipe, not SimAudit on a new benchmark, not a claim about checker repair quality, and not a sim-to-real claim.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched (61 defects; 3.1-5.6% flipped; X-VLA 95% to 20% on 'click bell'; rankings unchanged; card secs. 4.3-4.4, Table 4). Conditioning set: $\phi$ is defined on the released checker $c$ and the Verified checker $c'$ evaluated on the same rollouts of the same policy, so the only randomness is the policy's draw and the seeds (paired); the exploit cell is $\mathrm{Phan}(\pi_c) - \mathrm{Phan}(\pi_0)$, written before saying which is unmeasured (checklist 2026-11-08). Flag: the premise 'a released checker-trained RL checkpoint exists on an audited benchmark' is a st… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass with a flag: step 2a is 20 GPU-h if the checkpoint exists; step 2b (RFT arms) is 60-90 GPU-h, at the one-GPU-week edge, with a weaker kill stated. Parked rule written. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler) with a Route A element (two communities' quoted assumptions). Surprise three ways: expected $\phi \geq 0.25$ (judgment 0.35); audit community assumes checker = ground truth, RL community assumes reward = task; belief-changing $\phi < 0.10$ (0.4, certifies the checkers) or $\phi$ large but the Verified checker also exploited (0.25). The expected result is a magnitude neither community has stated — not the CL-W44-08 case — but the kill search must grep the RL-on-manipulation papers for 'checker', 'success detector', 'reward bug', 'false positive' before grading 2B. |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: RL-fine-tuning authors on manipulation benchmarks (two-checker reporting), benchmark owners (verified checkers as a submission gate), checker-audit authors (the exploit cell beside reachability), the L5 exploit headline. Proper-shaped; lab position for the RFT arms. |
| G4 | mechanism and consequence | Mechanism: an optimiser against a checker with phantom states finds the cheapest rewarded states; phantom states (a contact across an air gap, early stop credited) are often cheaper than the task, so gradient mass moves toward them; the Verified checker removes the reward there, so the gap between $c$ and $c'$ grows with optimisation and is a fraction of the reported gain. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the two-checker report applies to any benchmark with a repaired checker; flag — needs released RL checkpoints, which the lane has few of. |
| G6 | ownership, density, race window; position clause | Density owed at the kill search in the reward-hacking role words (hackable, unearned pass, integrity gap, verifier hardening — checklist 2026-11-01) and the robotics words (success detector, reward bug, false positive success, checker exploit, termination exploit), plus the RL-on-VLA papers' method sections. Why now: SimAudit's Verified checkers (2026-11-20) make the two-checker comparison free of annotation. Race: RL fine-tuning of VLAs is a lab-contested recipe area; the measurement is lab-adjacent. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-12 | The checker as the engine: the train-against / score-under 2x2 on RoboTwin 2.0's released and Verified success checkers | Steps 0-2a: about 20 GPU-h, $40, 6 days if a checker-trained pair is released; steps 0-2b: 60-90 GPU-h, $120-200, 10 days otherwise; dead if $\phi < 0.10$ and the phantom-share difference is inside the paired interval of zero (on-policy pa… | killed | — |

## Kill search

### Concept level (CL-W47-08) — killed (2026-11-22)
The checker 2x2 is published (2611.08318, verdict-only learner keeps 87 of 89 successes under faithful criteria), the RL exploit cell on RoboTwin 2.0 is published (Prism-GRPO: binary-GRPO shove share 0.7-7.0% of successes), and the $0 arithmetic puts phi at 0.01-0.13 against a 0.25 line; the Verified checkers have no public URL.
Full record: [`/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-08.md`](../../..//home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-08.md).
**Occupied by:** 2611.08318 (mechanism: the 2x2 under original and instruction-faithful criteria, RoboDojo, 2026-11-05) and 2608.17423 (exploit cell on RoboTwin 2.0 with GRPO, 2026-08-18); estimator by 2607.09492 (NRFR)
**Why not done before:** It is done in the parts that mattered to the groups with the checkpoints: Prism-GRPO measured the hack on RoboTwin because it reordered methods; 2611.08318 ran the 2x2 because criteria exposure is how self-improving agents are built; the remaining conjunction (SimAudit's c' x SimpleVLA-RL's released RL/SFT pairs) waits on a release that has no URL yet and is one group's stated next step ('rewritten criteria for a second benchmark').
Closest neighbors (one-sentence trick; one-line difference):
- `2611.08318` Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self… — Run one self-improvement loop with and without the learner reading the benchmark's success-criteria code, rewrite RoboDojo's criteria to verify only what the instruction says, and judge every episode by both. *Difference:* Occupies the 2x2 in mechanism (libraries optimised against C^orig and C^faith, each judged by both; verdict-only learner keeps 87 of 89 successes; exposed learner 51.6% -> 45.0%); differs in actor (LLM skill library, not RL on a VLA), benchmark (RoboDojo) and…
- `2608.17423` Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups — Add a trajectory-level execution-quality score to the binary success reward so same-outcome GRPO groups are not discarded, on four RoboTwin 2.0 tasks from SimpleVLA-RL's released SFT checkpoints. *Difference:* Occupies the exploit cell on the claim's benchmark with RL: 'many successful rollouts hacked the binary checker'; shove-cheat share 0.7-7.0% (binary GRPO), 0.6-20.0% (RL-ZVP) of successes over five seeds; raw vs calibrated success; reproduced on hardware. Sec…
- `2509.09674` SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning — Train OpenVLA-OFT with GRPO on a 0/1 task-completion reward on LIBERO and RoboTwin 1.0/2.0 and release SFT and RL checkpoints. *Difference:* Source of the released checker-trained RL/SFT pairs on RoboTwin 2.0 (Haozhan72 on Hugging Face, incl. click bell and move can pot) and of the 'pushcut' emergence reading of the behaviour Prism-GRPO calls a hack; no second scorer; real-robot click bell 30% ->…
- `2611.25179` Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation… — Read instruction and checker code separately, stage disagreement states under physics, repair the checker, re-score released imitation policies under both. *Difference:* The seed: owns c' and the phantom numbers on imitation policies; trains nothing; 'exploit' and 'hack' absent (grep); Verified checkers announced with no URL and not findable on 2026-11-22.
- `2607.09492` Multimodal Reward Hacking in Reinforcement Learning — Define the Newly Rewarded Failure Rate (failures among samples whose proxy reward improved over the SFT baseline) and show outcome-only rewards reach a 48.1% hacking rate in MLLM RL. *Difference:* Owns the claim's estimator (phi is NRFR with a checker as proxy and c' as oracle); VQA domain.
*Search degraded:* ['s2']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): the lane's 2x2 moved from the solver to the checker; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-08.md): killed — gate G6 (occupied in mechanism within the window: 2611.08318 ran the train-against / score-under 2x2 with a verdict-only arm on RoboDojo, 2026-11-05; 2608.17423 Prism-GRPO measured the exploit cell of checker-trained RL policies on RoboTwin 2.0, 2026-08-18; 2607.09492 named the estimator NRFR)…
- 2026-11-22 — C-W47-12 killed: W47 concept-level kill search of CL-W47-08: probe verdict killed. Its 2x2 is 2611.08318's design (verdict-only arm included), its exploit cell is Prism-GRPO's measurement on RoboTwin 2.0, its phi is NRFR, its if_true is the neighbours' recommendation; step 0's artefact (c') is announced without a URL; step 2a's premise (a released RL/SFT pair on RoboTwin 2.0) is true and recorded for the residue.

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-08`, version 2)
- probe `C-W47-12`: `data/candidates/2026-W47.jsonl`
