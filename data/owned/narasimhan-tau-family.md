# Owned-artifact portfolio — Karthik Narasimhan (τ-family simulated-user environments; Odysseus / EasyPPO critics)

Entry-ticket questions for the advisor conversation. Each question is owner-only because of a named data field or
configuration; "not published" is the strongest statement made about the owner. Stage 8, monthly.

## 2026-W44

**Artifact state (fetched 2026-11-02).** tau2-bench 2.0.0 released 2026-10-19 (0.1.0 2025-06-12 then 0.2.0 2025-10-06 then 
1.0.1 2026-07-15 then 2.0.0; about one minor release a quarter; an Unreleased section already adds `benchmark-quality.json`).
Released frames `text-v1` and `voice-v2`: 6 languages x3 domains x50 frozen tasks = 900 calls at one trial; `voice-v1`
278 calls; `banking_knowledge` 97 tasks; `intake` 200. Defaults for released runs: user simulator `openai/gpt-5.5` at
`reasoning_effort: low` (1.x: `gpt-4.1` at temperature 0), trials 1, seed 300, communication judge `gpt-5.5` low,
NL-assertion judge `gpt-5.4-mini` low. Submission rule: "The 2.0 benchmarks and voice-v1 are scored at one trial (pass@1).
For 1.x text, at least 4 trials per domain are strongly preferred." Log record (`SimulationRun`): `id, task_id, trial,
seed, duration, termination_reason, agent_cost, user_cost, agent_usage, reward_info{reward, db_check, env_assertions,
action_checks, nl_assertions, communicate_checks, reward_basis, reward_breakdown}, messages, ticks (voice),
review{agent_error, user_error, critical_user_error, errors[].source in{user, agent, unknown}, errors[].turn_idx},
user_only_review, hallucination_check, auth_classification, effect_timeline`. Public bucket `s3://sierra-tau-bench-public`:
29 submission folders, ~40,000 objects; Sierra-run 1.x cells carry 4 trials with a `gpt-5.2` low user and per-call seeds;
every `review` field opened is null. Limitation text, verbatim: τ²-bench §4.3 "Three primary sources of uncertainty can
impact benchmark reliability: implementation errors, task specification errors, and user simulator errors"; Table 2
critical user errors airline 13%, retail 12%, telecom 6% (gpt-4.1 user, 200 annotated conversations); §5 "Works remains
to be done to improve the user simulator." τ-Voice §6.1 "Our simulator is more patient than real users, with perfect
memory and instantaneous tool calls"; §5 "79–90% of failures stem from agent behavior". τ-Multilingual §5 "cost limited
additional languages, models, and trials. Simulated callers may not reproduce human timing or repair." EasyPPO §4 "we use
the same rollout group to estimate weights and train the critic, which can introduce bias but works well in practice
... we leave these alternatives to future work."

**Q1 (strongest; candidate C-W44-OWN-1; claim CL-W43-14, training consumer CL-W44-J01).** *Who moved in τ-bench 2.0: the
user-simulator share of pass@1 variance at the one-trial protocol.* Owner-only: the 2.0 matrix at $K$ trials, the
`review.errors[].source` labels (schema fields, null in public data), the Sierra-internal voice IDs. First measurement:
agent `gpt-4.1` at temperature 0, 150 English tasks x4 trials x3 user arms (2.0 default; `gpt-4.1` at 0 as floor;
`gpt-4.1` at 1 as calibration); $S_U = \overline{(V_A - V_B)}/\overline{V_A}$ with $V = \hat p(1-\hat p)$ per task; the
first-divergence turn and its party; about $750, two days, no GPU. Surprise — ours: $S_U \ge 0.3$ in airline and retail and
the per-task spread larger than the top-5 gaps; theirs: "a reliable user simulator" and one trial; belief-changing: an
interval column and pass^k re-read as user-draw consistency, or the 4-trial rule retired. Adoption: taubench.com, the gym's
RL users, τ-derived benchmarks, HAL's dashboard. Density (arXiv API, role words): 0 strict; nearest 2601.17087 (user-LLM
swap moves scores up to 9 points — a mean shift), 2604.21480 DIVERT, 2605.08545. Not published by the owner.

**Q2 (orphan).** *Does the 2.0 semantic communication judge reorder the 1.x leaderboard?* Partly solo-doable (1.x
trajectories are public; `tau2 evaluate-trajs`); 2.0 cells are the owner's. about $150, one day. Surprise: at least 3 top-10 rank
swaps from the judge alone. Adoption: a judge-version column.

**Q3 (CL-W44-J01).** *Reward noise per domain in the gym at $G = 8$:* the within-group variance share that is the user's
draw, user seed varied versus pinned (2.0 seeds simulations with 300; 1.x was unseeded). about 20 GPU-hours with a local user
model. Surprise: > 50% user share in airline and retail, < 20% in telecom (whose tools constrain the user). Adoption:
every RL paper on τ-bench (2610.24294, EAU 2610.16523).

**Q4 (CL-W43-06).** *Does the Odysseus turn-level critic beat its shuffled control in the first two thirds of a 100+ turn
episode?* Owner-only: checkpoints, trained critics, savestate hooks (the emulator is deterministic given savestate and
actions, so Monte-Carlo values are exact). 200 episodes x3 checkpoints x16 re-rolls about 20 GPU-hours. Surprise: explained
variance < 0.2 early, > 0.5 late; if informative early, CL-W43-06 is refuted on its best case.

**Q5 (orphan; lab-contested).** *EasyPPO's same-group weights:* noise normalization versus a larger group at matched
rollouts versus held-out weights, on Search-R1; about 600 GPU-hours. Surprise: the stabilizer is a group-size effect.

**Entry ticket (Q1).** Your 2.0 matrix can answer how much of a pass@1 score on the frozen 900-call frame is the simulated
user's draw now that the user is gpt-5.5 at low reasoning effort and every cell is scored once. The obvious design, swap
the user model and compare means, fails because it measures a bias between users (2601.17087 already shows up to 9 points)
and not the noise a single user adds to one score. The identifiable design holds a non-reasoning agent at temperature 0 and
runs four trials in three user arms — the 2.0 default, gpt-4.1 at temperature 0 as the floor, gpt-4.1 at temperature 1 as
the calibration — so the user share is the variance above the floor, with the first-divergence turn and your own
`review.errors[].source` labels saying which party moved: 1,800 calls, about $750, two days. Pre-registered: we expect the
user share above 0.3 in airline and retail and the per-task spread larger than your top-5 gaps; your papers assume the
simulator is reliable and that 79–90% of failures are the agent's. Do you want it, and is anyone doing it?

Solo entry point before asking: the first-divergence party on the public 4-trial Sierra cells (seeds and messages are
public), zero dollars. Records: `C-W44-OWN-1` (data/candidates/2026-W44.jsonl, once merged).
