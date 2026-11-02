# Owned-artifact portfolio — Arvind Narayanan (HAL: harness, leaderboard logs, Reliability Dashboard)

Entry-ticket questions for the advisor conversation. Each question is owner-only because of a named data field or
configuration; "not published" is the strongest statement made about the owner. Stage 8, monthly.

## 2026-W44

**Artifact state (fetched 2026-11-02).** `hal-harness` is archived: "HAL leaderboard results are no longer being updated
through this harness. We are focusing our current work on agent reliability"; "HAL is no longer accepting new result
submissions". The HAL paper (2510.11977, ICLR 2026): 21,730 rollouts, 9 models x9 benchmarks, about $40,000, "We share all
agent logs, comprising 2.5B tokens" (encrypted zips, `hal-decrypt`). Harness record per run: `config{agent_name,
benchmark_name, date, run_id, agent_args, run_command, prompt_sensitivity, agent_version}, results{…, total_cost,
latencies}, raw_eval_results, raw_logging_results (Weave: every API call), task_prompts, total_usage, total_cost,
git_info, agent_hash, wall_clock_times, task_step_counts, prompt_sensitivity_metrics{mean_variance, task_variances,
task_min_max_gaps, …}`. The live artifact is the AI Agent Reliability Dashboard (paper 2602.16666 v3, ICML 2026): 15
agents, GAIA (165 validation tasks) and τ-bench airline "clean" (26 tasks), 12 metrics in 4 dimensions, $K = 5$ runs per
task; outcome consistency corrected to $(2\hat p - 1)^2$; final results add GPT-5.5, Gemini 3.1 Pro / 3.5 Flash, Claude
Opus 4.7; "all new models make a noticeable jump in accuracy, but their reliability is not improving at nearly the same
rate." The τ-bench wrapper (`hal/benchmarks/taubench.py`) fixes `user_strategy: llm, user_model: gpt-4o`; upstream
tau-bench's user simulator calls `completion(model=…, messages=…)` with no temperature argument. Limitation text, verbatim:
HAL A3 "High evaluation costs prevent uncertainty estimation … For HAL, we were forced to rely on single runs without
statistical validation for most evaluations"; A4.1 "our cost calculations don't yet account for cache hits, reporting
full token prices instead"; A4.2 "Establishing true causal relationships between observed failures and task outcomes would
require checkpointing agent and environment states at each failure point, then replaying execution with the error
corrected, which is beyond our computational budget at the moment." Reliability §4.1 "We set the temperature to zero so
that any observed variance is attributable to non-sampling sources of stochasticity"; footnote "Reasoning models do not
expose a user-configurable temperature parameter"; §6 "Scaffold diversity … a single well-performing scaffold"; "Choice of
temperature … may overestimate the reliability achievable."

**Q1 (strongest; candidate C-W44-OWN-2; claim CL-W43-J01, also CL-W43-14).** *Where HAL's five temperature-zero runs first
diverge on τ-bench airline: the agent, the simulated user, or the stack.* Owner-only: the $K = 5$ x 15-model x 26-task
Weave traces (every user-simulator call logged; release not stated on the dashboard), the harness config, the budget.
First measurement: align the five transcripts per mixed-outcome cell, record the first differing turn $\tau^\ast$ and its
party; $U$ = share of cells diverging at a user turn; zero dollars, two days. Then three non-reasoning models x 26 x 5
with the user pinned (temperature 0, fixed seed), about $200, recomputing the consistency column. Surprise — ours: $U \ge 0.6$
and pinning lifts τ-bench consistency by at least 0.1; theirs: variance at temperature 0 is "non-sampling"; belief-changing: a
divergence-source column and user-pinned protocol, or the user cleared and the serving stack confirmed as the mechanism.
Adoption: the dashboard, METR-style consistency measurements, τ-bench 2.0's rules. Density: 0 strict; nearest 2609.33812
(identical runs vary more than agents differ; no party attribution), 2610.33012, 2602.07150. Not published by the owner.

**Q2 (CL-W43-14).** *Is the effort effect a single-run artifact?* "higher reasoning effort reducing accuracy in the
majority of runs" came from single runs. 4 effort levels x 5 runs x 2 benchmarks x 3 models about $1,500–3,000, one week.
Surprise: the sign flips in at least 40% of cells once intervals exist. Adoption: every leaderboard with an effort setting.

**Q3 (orphan; owner-cheap).** *Cache-aware re-pricing* of the SWE-agent runs from the Weave usage fields, if cached-token
counts are present; zero dollars, one day. Surprise: costs fall 40–60% (2601.06007 measured 41–80% from caching) and the
top of the SWE-bench Verified Mini frontier reorders. Adoption: the cost axis.

**Q4 (orphan).** *Replay with the error corrected* on τ-bench, the step A4.2 calls beyond budget: for each Docent-flagged
first failure (A7), replay from the step before with a corrected action; counterfactual yield per failure category. 200
replays about $100, three days (DIVERT 2604.21480 shows the state is snapshot-able). Surprise: under half of first failures
flip the outcome; the yield ranking differs from the frequency ranking. Adoption: the log-analysis principles (2605.08545).

**Entry ticket (Q1).** Your $K = 5$ temperature-zero traces can answer which party moves first when two runs of the same
τ-bench task come apart: your harness pins the agent at 0 but runs the gpt-4o user through tau-bench's simulator with no
temperature argument, so the user samples at the provider default. The obvious design, more runs and a wider interval,
fails because it never separates the user's draw from the serving stack's. The identifiable design is a diff: align the
five transcripts of every mixed-outcome cell, record the first differing turn and who wrote it, then re-run three
non-reasoning models with the user pinned and recompute your consistency column; zero dollars for the diff, about $200
for the re-run. Pre-registered: we expect the first divergence at a user turn in most mixed cells and a consistency gain
of 0.1 or more from pinning; your paper attributes the variance to non-sampling sources. Do you want it, and is anyone
doing it?

Solo entry point before asking: 26 tasks x 5 runs x 2 user settings on one cheap model (about $50) gives $U$ for one model.
Records: `C-W44-OWN-2`.
