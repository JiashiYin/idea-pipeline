# Product red team — Shape B: annotated trace corpus plus an open annotator (2026-W41)

Date: 2026-10-10. Brief: `data/pressure/2026-W41/product-shapes.md` (Shape B). Inputs read: `prompts/checklist.md`,
pressure points #3, #7, #10 and the Section 4 query log of `2026-W41-pressure-points.md`, the cross-cutting lessons
of `2026-W41-pressure-redteam.md`, and the W41 pressure jsonl records on HAL, Terminal-Bench, OSWorld, SWE-rebench.
Everything below was fetched today; raw downloads are in `scratchpad/shapeB/` (arXiv XML under `arx/`, pages and
dataset metadata under `pages/`, one decrypted HAL zip under `haldl/`) and were treated as data. The WebFetch tool
caps quotes at 125 characters, so verbatim abstracts come from the arXiv API XML (`arx/incumbents_ids.xml`).

Terms. **Trace / trajectory / rollout**: one recorded attempt at a task, as a sequence of model calls, tool calls
and tool outputs. **Step type**: the role of one step (think / act / verify / communicate). **Token destination**:
which step type a model's generated tokens went into. **Failure attribution**: naming the step (and agent) where a
run went wrong. **κ (kappa)**: chance-corrected agreement between two labelers; 1 is perfect, 0 is chance.
**Effort**: a vendor knob for how many thinking tokens a model spends. **Normalizer**: code that turns each agent's
own log format into one common schema.

## Verdict

**VERDICT: killed.** Every component of the shape is occupied by a released artifact (table below), the sources it
would live on are frozen or closed (HAL paused, last upload 2026-02-01; Terminal-Bench 2.0 submissions closed
2026-05-14), and the three papers that would fall out are headlines from labels alone — none gains a mechanism or a
method consequence without an intervention that belongs to another shape (#3's replay, #7's training run). The
strict kill condition in the brief (one 2026 corpus with ≥5k natural cross-benchmark traces and a released
annotator) is not met by any single artifact; the shape dies on the third condition ("the taxonomy is the only
novelty") and on density (185–270 arXiv hits in 12 months on the shape's own words).

What survives is not a product: a one-week, ~$100 measurement on HAL's effort pairs that feeds pressure point #3
(Section "Narrowest surviving version"). It should be run under #3, not as Shape B.

## 1. Incumbent table

| Artifact | What it ships | What it does not | Source, date |
|---|---|---|---|
| **MAST** — "Why Do Multi-Agent LLM Systems Fail?" (Cemri … Stoica) | "MAST-Data, a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks"; "14 unique modes, clustered into 3 categories"; "validated by high inter-annotator agreement (kappa = 0.88)"; "We publicly release our comprehensive dataset (MAST-Data), the MAST, and our LLM annotator". | Multi-agent frameworks only; no named single-agent benchmark; no step types, no token destinations. | arXiv:2503.13657, v1 2025-03-17, v3 2025-10-26 |
| **TRAIL** (Patronus AI) | "a formal taxonomy of error types encountered in agentic systems"; "a set of 148 large human-annotated traces (TRAIL) … grounded in established agentic benchmarks"; "software engineering and open-world information retrieval"; "the best Gemini-2.5-pro model scoring a mere 11% on TRAIL". | 148 traces; it is a benchmark *for* trace judges, not an annotator; no step types or tokens. | arXiv:2505.08638, 2025-05-13 (v3 2025-06-23) |
| **Who&When** (Zhang … Wu) | "extensive failure logs from 127 LLM multi-agent systems with fine-grained annotations linking failures to specific agents and decisive error steps"; "The best method achieves 53.5% accuracy in identifying failure-responsible agents but only 14.2% in pinpointing failure steps". | Multi-agent; small; shows LLM step-level attribution is unreliable (14.2%). | arXiv:2505.00212, 2025-04-30 |
| **Who&When Pro** (… Huazheng Wang) | "12,326 failed trajectories with golden labels across 3 modalities and 26 benchmarks"; built "by injecting a failure only after exactly replaying a successful prefix". | Failures are injected, not natural; labels are the injection point, not a failure-mode taxonomy of real runs. | arXiv:2607.09996, 2026-07-10 |
| **AgentErrorTaxonomy / AgentErrorBench / AgentDebug** (Zhu … You) | "AgentErrorTaxonomy, a modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations"; "AgentErrorBench, the first dataset of systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop". | Count not in abstract; three small benchmarks; "code and data will be available". | arXiv:2509.25370, 2025-09-29 |
| **HORIZON** — "The Long-Horizon Task Mirage?" (Wang … Nowak) | "3100+ trajectories across four representative agentic domains"; "a trajectory-grounded LLM-as-a-Judge pipeline for scalable and reproducible failure attribution … (inter-annotator κ=0.61; human-judge κ=0.84)"; leaderboard page: 3,357 trajectories, 7 failure categories, judge reports a "failure_step". | Page shows the judge prompt but no code link; trajectories not stated downloadable; models GPT-5-mini and Claude-4-Sonnet; self-described "an initial diagnostic benchmark", "a pilot empirical study". | arXiv:2604.11978, 2026-04-13; xwang2775.github.io/horizon-leaderboard |
| **AgentLens** (… Yu Hu) | "2,614 OpenHands trajectories from eight model backends on 60 SWE-bench Verified tasks"; "AgentLens-Bench, a dataset of 1,815 trajectories annotated with quality scores, waste signals, divergence points"; "a context-sensitive intent labeler to assign actions to Exploration, Implementation, Verification, or Orchestration". | One benchmark, one scaffold; no token destinations. This is the step-type labeling the shape proposes, already done on SWE-bench Verified. | arXiv:2605.12925, 2026-05-13 |
| **TraceProbe** — "What Resolve Rate Hides" (… Yuan Wang) | "normalizes each raw run into a canonical nine-type action taxonomy with deterministic effect labels"; anti-patterns "search loops, verification skips"; "2,500 trajectories from five production settings on SWE-Bench Verified". | One benchmark; rule-based, no LLM annotator. Ships the normalizer the shape would need. | arXiv:2607.06184, 2026-07-07 |
| **SearchAuditBench / SearchAuditor** (… Qiong Cao) | "1,243 failed trajectories, averaging 73.1 messages and 65.1K tokens, collected from eight open-weight models on five deep-search benchmarks, each expert-annotated with the critical error step, a search-specific root cause, and a reference repair". | Search agents only; best auditor "26.6% end-to-end pass rate". | arXiv:2608.05212, 2026-08-05 |
| **AgentRx** (… Chetan Bansal, Microsoft) | "170 trajectories across 11 diverse task settings … annotated with a critical failure step and a category from a grounded-theory derived, cross-domain failure taxonomy". | 170 traces. | arXiv:2602.02475, 2026-02-02 |
| **CheatBench** (Phan … Hendrycks) | "a benchmark of cheating in AI agents across mathematical research, knowledge work, coding, visual tasks, and other domains"; "We publicly release CheatBench at https://cheatbench.ai". | Environments, not an annotated corpus of benchmark traces. | arXiv:2609.36308, 2026-09-28 |
| **Every Model Cheats** (Kouremetis … Greunke) | "All 1,518 task traces were individually audited through a four-stage pipeline combining LLM-as-a-judge classification, programmatic verification, judge-verifier reconciliation, and human review"; "37.1% of passes involved cheating, 21 of 22 models cheated". | Cybench CTF only (23 challenges). The audited cheating-label pipeline for #10 exists. | arXiv:2607.21763, 2026-07-23 |
| **"When Do Agent Loops Mistake Stagnation for Progress?"** (Park, Choi) | A testbed, not a corpus: "Across 54 cycles a frontier agent claimed improvement every time, yet 56 percent had a measured delta of zero or below". | 54 cycles; no released traces. | arXiv:2607.25152, 2026-07-27 (v2 2026-09-29) |
| **Agent-as-a-Judge** (Zhuge … Schmidhuber) | "DevAI, a new benchmark of 55 realistic automated AI development tasks … a total of 365 hierarchical user requirements"; judges requirement satisfaction "for the entire task-solving process". | Judges requirement satisfaction, not failure modes or step types. | arXiv:2410.10934, 2024-10-14 |
| **HAL** (Kapoor … Narayanan) | "we use LLM-aided log inspection to uncover previously unreported behaviors, such as searching for the benchmark on HuggingFace"; "We share all agent logs, comprising 2.5B tokens of language model calls". | Inspection findings, no released labels or annotator; site: "We have paused updating HAL leaderboard with new models". | arXiv:2510.11977, 2025-10-13; hal.cs.princeton.edu fetched 2026-10-10 |
| **Beyond pass@1** (Khanal … Zhou) | "10 models across 23,392 episodes on a 396-task benchmark"; meltdown rates "up to 19%". | No step labels; its own benchmark. | arXiv:2603.29231, 2026-03-31 |

Kill-condition reading. No single 2026 artifact has ≥5k *natural* cross-benchmark traces plus a released annotator:
Who&When Pro has 12,326 across 26 benchmarks but injected failures; HORIZON has 3,357 natural traces, a validated
judge (κ=0.84) and no confirmed code release; MAST has 1,600+ and a released annotator but multi-agent frameworks
only. The components are nonetheless each occupied: step-type labels on SWE-bench (AgentLens, TraceProbe),
cross-domain natural-failure taxonomy with a validated judge (HORIZON), audited cheating labels (Every Model Cheats),
failure-step attribution at scale (Who&When Pro, SearchAuditBench). The unoccupied cell is "token destination",
and Section 2 shows it is only partly observable.

## 2. Data-availability check

| Source | Inspected | Per-step content | Per-step tokens | Outcome per task | State |
|---|---|---|---|---|---|
| **HAL** `agent-evals/hal_traces` (HuggingFace) | Dataset tree via HF API: 380 encrypted zips, 113.07 GB, prefixes corebench 66, taubench 47, swebench 45, scicode 38, gaia 37, colbench 36, assistantbench 34, scienceagentbench 25, browser-use 19, seeact 18, usaco 15; last modified 2026-02-01. One zip decrypted (`swebench_verified_mini_my_agenttogether_aideepseekaideepseekr1_1745262492_UPLOAD.zip`, 6.7 MB; the harness's fixed password is in `hal/utils/upload.py`). | Yes. Top-level keys `config, results, raw_eval_results, raw_logging_results, total_usage, total_cost, git_info`. `raw_logging_results` is a list of every model call (294 in the sample, 49 tasks, 6 calls/task) with `inputs.messages` (full conversation as sent, tool outputs included), `inputs.tools`, `output.choices[0].message` (`content`, `tool_calls`, `finish_reason`), `started_at`, `ended_at`, `attributes.weave_task_id`. Reasoning text present only where the provider returns it (`reasoning_content`/`thinking` markers in 79 of 294 calls, DeepSeek-R1); for OpenAI reasoning models only counts exist. | Yes: `output.usage` = `prompt_tokens, completion_tokens, total_tokens`, plus `completion_tokens_details` / `prompt_tokens_details` on 147 of 294 calls (reasoning and cached tokens). | Yes: `results.successful_tasks`, `results.failed_tasks`, `raw_eval_results` (`resolved_instances`, `empty_patch_instances`, id lists). Note the sample run is broken: 49 of 50 patches empty, `finish_reason: length` at 2048 completion tokens — the corpus contains harness-failure runs that must be filtered. | Paused. No Terminal-Bench or OSWorld inside. The current `weave_utils.get_weave_calls` compacts to "one message array + metadata per task" (`messages, call_metadata{usage,started_at,ended_at}, model, call_count`), so newer uploads keep per-call usage but only the longest call's messages. |
| **Terminal-Bench 2.0** `harborframework/terminal-bench-2-leaderboard` (HuggingFace) | HF API tree (capped at 100,000 files; 15 submissions seen, 445 trials each = 89 tasks × 5); README; one `result.json` fetched. | Agent-specific, no common schema: `agent/episode-N/prompt.txt` + `response.txt` (16,593 each, Terminus-style agents), `agent/trajectory.json` (2,115), Claude Code `claude-code.txt` + `agent/sessions/.../*.jsonl`, `codelia-output.log`, `dirac_output.txt`, `ante.txt`; `command.txt`/`stdout.txt`/`return-code.txt` for some. | Trial totals only in `result.json`: `agent_result.n_input_tokens, n_cache_tokens, n_output_tokens, cost_usd` (14,247,478 / null / 68,945 / null in the sample). Per-step tokens only inside an agent's own `trajectory.json` where present. | Yes: `verifier_result.rewards.reward`, `exception_info` (`AgentTimeoutError`, "Agent execution timed out after 12000.0 seconds"), phase timestamps (`agent_execution`, `verifier`). Rule: "Each task must be evaluated with a minimum of five trials." | README: "SUBMISSIONS CLOSED … We are working on a new submission process … Check back by end of June". `tbench.ai/leaderboard/terminal-bench/2.0` now serves the 4.0 board (empty, columns RANK, MODEL, AGENT, RESOLUTION RATE, COST, TOKENS). |
| **SWE-rebench** `ibragim-bad/swe_rebench_07_2026_trajectories` (HuggingFace, Nebius author) | Dataset card. | "9,435 normalized software-engineering agent trajectories: 111 tasks, 17 participants, and five runs per participant … 13 standalone models in a common scaffold and four agentic systems: Claude Code, Codex, Cursor, and Junie"; "Each JSONL row contains the participant and run, rendered or exposed prompts, ordered agent/tool events, available time and token usage, and evaluation and exit statuses. Submitted patches are not included." Schema in `schema.json` (not opened). | "available time and token usage" — granularity not confirmed. | Yes ("evaluation and exit statuses"). | One monthly window (07/2026); the leaderboard dataset `nebius/SWE-rebench-leaderboard` holds tasks (features `repo, instance_id, patch, test_patch, FAIL_TO_PASS, …`), not traces. |
| **OSWorld 2.0** | osworld-v1.xlang.ai (osworld.xlang.ai redirects there). | v1/Verified page: "All verified trajectories are hosted on Hugging Face for community analysis." For 2.0 only "2026-06-26: OSWorld 2.0 is now available!" — no trajectory statement found. HF search returned only third-party v1 sets (`mlfoundations-cua-dev/osworld-trajectories`, 2025-11). | Unknown. | Unknown. | **Not confirmed in this pass** — a kill-grade gap for the computer-use slice. |
| **τ-bench** | HAL taubench zips (47, full `raw_logging_results` format above); `AgentSuite/tau-bench-trajectories` card. | AgentSuite: "Models: 30 … Tasks per model: 165 … Fields: `model_path, user_model_path, benchmark_name, task_name, sampling_params, user_sampling_params, messages, eval_result, meta`". | HAL: per call. AgentSuite: not stated. | Yes (`eval_result`). | HAL airline runs include low/high effort pairs (o4-mini, Claude 3.7, Opus 4.1 "no_reasoning"/"high_reasoning", GPT-5 "minimal"/"high"). |

Reading. Per-step content exists for coding, terminal (heterogeneous), customer service and web; computer use is
unconfirmed. Per-step token counts exist in HAL, not in Terminal-Bench's `result.json`. Hidden reasoning of closed
models is visible only as a count (`reasoning_tokens`), never as text, so "token destination" is observable as
*tokens per step type* and never as *what the reasoning was about*. The 26k figure in the brief is HAL's site count
(26,597 rollouts, 9 benchmarks); HAL's paper counts 21,730 rollouts across 9 models and 9 benchmarks for $40,000.

## 3. Personas

**1. The incumbent.** "We already ship this." MAST: a released LLM annotator with κ=0.88 on 1,600+ traces. HORIZON:
a cross-domain judge with human-judge κ=0.84 on 3,357 natural trajectories in four domains. AgentLens: intent labels
(Exploration / Implementation / Verification / Orchestration) on 1,815 SWE-bench Verified trajectories — the shape's
"step type" axis. Every Model Cheats: a four-stage audited cheating label on 1,518 traces — the shape's #10 axis.
*Answer:* none covers HAL/Terminal-Bench/τ-bench logs or token destinations, and no single one is ≥5k natural
cross-benchmark traces with code. *Concession:* the union covers every axis but "token destination", and that axis is
a per-step count the corpus could add to AgentLens-style labels in a week — a feature, not a product.

**2. The would-be user** (an eval lead, a benchmark owner, an author comparing agents). They already run log
inspection: HAL "use[s] LLM-aided log inspection", Terminal-Bench's paper did "an error analysis", Anthropic's cards
use judge protocols on RL episodes. What they would need is an annotator that runs on *their private logs in their
format*; the public corpus is irrelevant to them, the normalizer is the value. *Answer:* a normalizer across
Terminal-Bench's six-plus agent formats plus HAL's Weave format plus SWE-rebench's schema is real engineering.
*Concession:* TraceProbe already ships "a canonical nine-type action taxonomy with deterministic effect labels" and
Nebius ships a normalized schema; the user would cite those, and nobody cites a corpus of other people's runs over
re-running their own.

**3. The systems reviewer.** Can the labels be computed from the logs as they exist? Content yes (Section 2);
per-step tokens only for HAL; reasoning text only for open models; OSWorld 2.0 unknown. The 113 GB HAL corpus
contains harness-failure runs (the sampled run: 49 of 50 empty patches at a 2048-token cap) that a labeler must
detect first. Maintenance per month: HAL paused since 2026-02-01, Terminal-Bench 2.0 closed since 2026-05-14 with
a new process pending, SWE-rebench monthly — the corpus is a snapshot of early-2026 models, and "updates when a
source releases new logs" has one live source. *Concession in full.*

**4. The RL reviewer.** Is the metric well-defined, and do the three papers get a mechanism and a method
consequence? *#3 mechanism* ("where the extra tokens go when more effort lowers the score"): from labels alone the
result is "high-effort failed runs put X% more tokens into verify/loop steps on tasks the low-effort run solved" —
correlational; the decomposition into {timeout, grader-scope penalty, wrong answer or spiral} needs the replay in
pressure point #3's first measurement, which is not this shape. Headline. *#7* ("does post-training move coin-flip
tasks to always/never-solved"): needs per-task success probability across checkpoints under one scaffold; public
logs give 5 runs per task (Terminal-Bench rule, SWE-rebench "five runs per participant"), so SE at p=0.5 is 0.22 and
"coin-flip" is not a class (the pressure report already required 32 rollouts); and "post-training" is unobservable
on released pairs — the Sharpening Tax's own "observational rather than interventional" objection. Headline, and
underpowered. *#10* ("persistence past blockers versus grader gaming on the same tasks"): the label "circumvented a
blocker" is observable, but "capability or failure" needs a per-task statement of which blockers were legitimate,
which no public log carries; Every Model Cheats' audited pipeline already gives the cheating rate on a benchmark
where the answer key exists. Headline. *Also:* the step-level part of the annotator is exactly where LLM judges are
known to fail — Who&When "only 14.2% in pinpointing failure steps", TRAIL "a mere 11%", SearchAuditor "26.6%
end-to-end" — while category-level agreement is where they succeed (κ 0.84–0.88); the 200-trajectory validation
would validate the easy axis and leave the step axis where the incumbents left it. *Concession in full.*

**5. The professor who dismisses it in ten minutes.** "This is a labeling exercise with a new taxonomy; MAST, TRAIL,
HORIZON and AgentLens did it; a taxonomy is not a result." The sentence that would answer it is "the corpus makes
a mechanism finding possible that no incumbent could make" — and Section 3.4 shows no such finding falls out
without an intervention. *Concession.*

## 4. Density (arXiv API, window 2025-10-09 → 2026-10-11, max 50, newest first, 3 s pause; raw XML in `arx/`)

| key | query (all: fields) | total |
|---|---|---|
| T1 | agent AND taxonomy AND (trajectory OR trajectories OR trace OR traces OR rollout OR rollouts) | 185 |
| T2 | agent AND (annotated OR annotation OR annotate) AND (trajectory… OR trace…) AND (failure OR error) | 126 |
| T3 | agent AND "failure mode" AND (trajectory… OR trace… OR rollout…) | 270 |
| T4 | agent AND "error attribution" AND (trajectory… OR trace…) | 6 |
| T5 | agent AND "failure attribution" | 58 |
| T6 | agent AND "step-level" AND (label OR labels OR annotation) AND (trajectory… OR trace OR logs) | 37 |
| T7 | agent AND "failure taxonomy" | 35 |
| T8 | agent AND trajectories AND dataset AND failures AND release | 14 |
| K1 | token AND (destination OR allocation OR where) AND agent AND reasoning AND (trajectory OR trace OR steps) | 113 |
| K2 | agent AND "token allocation" AND reasoning | 2 |
| K3 | agent AND tokens AND "spent on" AND (verification OR exploration OR retry) | 4 |
| B1 | (bimodal OR bimodality OR "coin flip" OR "always solved" OR "never solved") AND agent AND ("post-training" OR RL OR "reinforcement learning") | 5 |
| B2 | "per-task" AND "success probability" AND agent AND ("post-training" OR "reinforcement learning") | 0 |
| B3 | agent AND sharpening AND ("pass@k" OR coverage) AND "reinforcement learning" | 2 |
| R1 | "reward hacking" AND agent AND benchmark | 53 |
| R2 | grader AND agent AND benchmark AND (exploit OR gaming OR cheat OR cheating) | 4 |
| R3 | ("test-sensing" OR "evaluation awareness" OR "test awareness") AND agent AND benchmark | 7 |
| R4 | agent AND persistence AND (blocker OR blockers OR circumvent OR circumvention OR guardrail) | 32 |
| C1 | "SWE-bench" AND trajectories AND (taxonomy OR annotated OR "failure analysis" OR "error analysis") | 11 |
| C2 | "Terminal-Bench" AND trajectories | 57 |
| C3 | OSWorld AND trajectories AND (failure OR error OR analysis) | 21 |
| C4 | HAL AND agent AND leaderboard AND rollouts | 1 |
| C5 | agent AND trajectories AND "LLM-as-a-judge" AND (failure OR error) AND (agreement OR kappa OR "inter-annotator") | 2 |
| C6 | agent AND traces AND observability AND (failure OR error OR debugging) | 180 |

517 distinct papers returned; 16 in-window papers report a trace count together with annotation or taxonomy
words (listed in Section 1 where they matter: HORIZON, AgentLens, TraceProbe, Who&When Pro, SearchAuditBench,
AgentRx, plus 2609.29508 with "13,780 deliberation traces … LLM-assisted labeling paired with human audit (κ=0.83)"
in a toy setting). The failure-taxonomy words alone (T1, T3, C6) return 185–270 hits; the token-destination words
(K2, K3) and the bimodality words (B1–B3) return 0–5, which says the unoccupied cells are unoccupied because they
are not reachable from labels, not because nobody looked.

Pre-window precedents (named per checklist 2026-10-09): MAST (2025-03), Who&When (2025-04), TRAIL (2025-05),
AgentErrorBench (2025-09), HAL's LLM-aided log inspection (2025-10), Agent-as-a-Judge (2024-10). The SWE-bench
Verified failure analyses the brief names were not fetched separately in this pass; AgentLens and TraceProbe (both
2026, both on SWE-bench Verified) are their in-window successors and are cited instead.

## 5. The two closest papers' limitation text, verbatim

- HORIZON (arXiv:2604.11978, abstract): "these long-horizon failures remain poorly characterized, hindering
  principled diagnosis and comparison across domains" … "Our findings offer an initial methodological step toward
  systematic, cross-domain analysis of long-horizon agent failures". Leaderboard page: "an initial diagnostic
  benchmark"; "a pilot empirical study"; "Help grow the benchmark by contributing new long-horizon tasks."
- MAST (arXiv:2503.13657, abstract): "We develop MAST through rigorous analysis of 150 traces, guided closely by
  expert human annotators" … "Our analysis provides insights revealing that identified failures require more
  sophisticated solutions". TRAIL (arXiv:2505.08638): "Current evaluation methods depend on manual, domain-specific
  human analysis of lengthy workflow traces - an approach that does not scale".
- Who&When (arXiv:2505.00212): "The best method achieves 53.5% accuracy in identifying failure-responsible agents
  but only 14.2% in pinpointing failure steps, with some methods performing below random."

Note per checklist 2026-10-09: these are abstract- and page-level quotes; the introductions, limitation sections
and appendix titles of HORIZON and AgentLens were not read in full in this 25-minute pass. The verdict does not rest
on an "unposed" claim, so the rule's failure mode (a false "unposed") does not arise here.

## 6. Narrowest surviving version (not a product; hand to #3)

Take HAL's released effort pairs on one benchmark (τ-bench airline: o4-mini low/high, Claude 3.7 default/high,
Opus 4.1 no_reasoning/high_reasoning, GPT-5 minimal/high; roughly 8 runs × 50 tasks ≈ 400–600 trajectories with
per-call `usage`), label each step think / act / verify / communicate with one prompted model, and for the tasks
solved at low effort and failed at high effort report the token share by step type at each effort level against
the tasks solved at both. This is the correlational half of pressure point #3's question and is only worth doing
as the week before #3's replay experiment; alone it is a headline.

## 7. First measurement and its cost

Measurement: the Section 6 run. GPU-hours: 0 (public logs, API labeling). Dollars (assumptions labeled): 600
trajectories × ~50k input tokens of unique content per trajectory (assumption; HAL averages ~115k billed tokens per
rollout, 2.5B / 21,730, most of it re-read prefix) = 30M input tokens; at $0.25 per million input (assumed price
of a small labeling model) plus ~2k output tokens per trajectory at $2 per million → **about $12; with a frontier
labeler at $3 per million input, about $95**. Human validation: 200 trajectories at ~20 minutes each (SearchAuditBench
averages 73.1 messages and 65.1K tokens per trajectory) ≈ 67 hours of Jacob's time — the dominant cost. Full-shape
cost for the record: 26,597 rollouts × 50k = 1.3B input tokens → $330 (small model) to $4,000 (frontier) of API,
plus the same 67 human hours, plus the normalizer (Terminal-Bench alone has six-plus log formats).

Result that kills the residue: token share by step type does not differ between flipped and non-flipped tasks beyond
the 5-run noise, or the extra tokens sit in hidden reasoning (count only), where step type is unobservable.

## 8. Checklist items triggered

- "Nobody has done X" rule (2026-10-09): applied — two incumbents' own text quoted (Section 5); no "nobody" sentence
  survives.
- Density words include failure-mode and operations words (2026-10-09): applied (T3, T6, R2, R4, C6).
- 12-month window + ≥2 pre-window precedents (2026-10-08 / 2026-10-09): applied (Section 4).
- Premise numbers with category and denominator: "21 of 36 model-agent-benchmark combinations" (HAL), "37.1% of
  passes involved cheating" (Every Model Cheats, denominator passes), "14.2% in pinpointing failure steps" (Who&When).
- Artifact runnable / available (2026-10-09): triggered — HAL paused, Terminal-Bench 2.0 closed, OSWorld 2.0
  trajectories unconfirmed.
- Judge vs critic (2026-10-09): the annotator is a judge; its documented failure is step localization (11–26.6%),
  not category agreement — stated in persona 4.
- "Why now": the enabling pieces (HAL's 2.5B-token release 2025-10, Terminal-Bench's HF submission repo 2025-12,
  Nebius's normalized trajectories 2026-07) landed, and the first users of each (HORIZON, AgentLens, TraceProbe,
  Who&When Pro) already published — the window opened and closed inside the last 12 months.

## 9. New checklist lessons (not yet added to `prompts/checklist.md`)

1. For any corpus or tracker shape, record each source's release state and last-modified date before design (HAL:
   paused, last upload 2026-02-01; Terminal-Bench 2.0: "SUBMISSIONS CLOSED" 2026-05-14). A living product over
   frozen sources is a snapshot.
2. "Token destination" splits into two fields: tokens per step (a count, present in HAL `usage`, absent in
   Terminal-Bench `result.json`) and reasoning text (present only for open models; closed models give
   `reasoning_tokens` counts). State which one a measurement needs.
3. Agent logs have no common schema (Terminal-Bench 2.0: `prompt.txt/response.txt`, `trajectory.json`, Claude Code
   session jsonl, `codelia-output.log`, `dirac_output.txt`, `ante.txt`). Budget the normalizer, and check whether
   one exists (TraceProbe's canonical taxonomy; Nebius's `schema.json`) before the taxonomy.
4. The HuggingFace API (`huggingface.co/api/datasets?search=…`, `…/api/datasets/<id>?full=true`) is reachable from
   the shell and finds trajectory releases arXiv misses (the Terminal-Bench 2.0 leaderboard repo, SWE-rebench
   trajectories, AgentSuite τ-bench trajectories). Add it to the data-availability step.
5. WebFetch caps quotes at 125 characters; pull verbatim abstracts from the arXiv API XML (`id_list=` accepts many
   ids in one call).
6. A kill condition about "a corpus that labels traces" must say natural versus injected failures: Who&When Pro's
   12,326 labeled trajectories are injected after "exactly replaying a successful prefix" and do not label
   real failure modes.
7. LLM judges succeed at category labels (κ 0.84–0.88) and fail at step localization (11–26.6%); a plan that
   validates an annotator on 200 trajectories must say which axis the agreement number covers.

VERDICT: killed
