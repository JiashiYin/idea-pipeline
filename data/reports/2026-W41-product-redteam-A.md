# Product red team — Shape A, Observatory (week 2026-W41)

Date: 2026-10-10. Brief: `data/pressure/2026-W41/product-shapes.md` (Shape A). Inputs: pressure points #1, #2,
#3, #6, #7 and the Section 4 query log of `2026-W41-pressure-points.md`; cross-cutting lessons of
`2026-W41-pressure-redteam.md`; `prompts/checklist.md`. Everything below was fetched today unless a date says
otherwise; records B##/L##/Q## refer to `data/pressure/2026-W41/*.jsonl` (fetched 2026-10-09). Downloads sit in
`scratchpad/shapeA/dl/` (HAL sample traces, METR YAML, dataset cards, README files, 45 arXiv API responses) and
were treated as data; decryption and remote-zip listing used my own scripts in `scratchpad/shapeA/scripts/`,
run with `python3 -I`. Fetch failures: `arxiv.org/abs/2610.04433` (HTTP 429, read through the arXiv API
instead); `artificialanalysis.ai/evaluations/terminal-bench-hard` (client error; the `terminalbench-4-0` page
was read instead); the Harbor Hub leaderboard and the Galileo Hugging Face Space (JavaScript-rendered, no
rows in the text).

Terms. **pass^k**: the share of tasks solved in all k runs (τ-bench's reliability metric). **pass@k**: solved in
at least one of k runs. **Outcome consistency** (HAL's tracker): (2p̂ − 1)² where p̂ is a task's observed success
rate over K runs, averaged over tasks; 1 means every task is always or never solved. **Per-task bimodality**:
the share of tasks a model solves either always or never, as opposed to sometimes. **Effort**: a vendor knob
(low/medium/high/xhigh/max) setting how many thinking tokens a model spends. **Effort curve**: score plotted
against that knob. **Prefix re-read**: an agent re-sends its whole conversation on every step, so each step's
input tokens are mostly text the model has already read; **cached tokens** is the provider's count of such
re-read input served from its cache at a discount. **Rollout**: one recorded attempt at a task. **Harness**:
the fixed code around the model (prompts, tools, retries). **Step cap**: the maximum number of actions a
harness allows per task.

## Verdict: killed

Two of the three metrics are shipped by incumbents as maintained artifacts (kill condition 1), and the public
logs cannot supply the third at the horizon where it would say something new (kill condition 2). In one
sentence each:

1. **pass^k across generations is shipped.** HAL's reliability tracker (hal.cs.princeton.edu/reliability,
   fetched today) is a maintained leaderboard of 15 agents spanning o1 to Claude Opus 4.7, GPT-5.5 and Gemini
   3.5 Flash, with outcome consistency and the pass@k–pass^k gap, and it already states the longitudinal
   claim Shape A would publish: "overall reliability shows only small improvements over time while accuracy
   steadily climbs." METR's released per-task file (`task_results_1_1.yaml`, `n_successes`/`n_runs` for 23
   model generations, 2023-03 → 2026-04) yields the per-task always/never/coin-flip trend in a 30-line
   script (computed below).
2. **Effort curves are shipped.** Artificial Analysis evaluates each model's effort variants as separate
   entries on Terminal-Bench 4.0 and its other agentic evals ("pass@1 averaged over three repeats per task";
   entries "Claude Opus 5.5 (Max…)", "Claude Opus 5.5 (Xhigh…)") with cache-aware cost; SWE-rebench lists
   `[minimal]`/`[medium]`/`[high]`/`[xhigh]` variants with Pass@5 and cost; HAL's own paper already drew
   the effort finding from the very logs Shape A would re-score ("in 21 of 36 model-agent-benchmark
   combinations, increased reasoning effort produces equal or lower accuracy").
3. **Prefix-aware cost: the headline is published and the long-horizon data lack tokens.** arXiv:2610.04433
   (2026-10-03) measured the mechanism on SWE-bench Verified ("The gap is set at the first call, by the
   preamble of system prompt and tool schemas each harness sends with every step, and scaled by the number
   of steps […] The provider's price for cached input scales the bill and does not reorder it");
   arXiv:2601.06007 (2026-01-09) measured caching savings of 41–80% over 500 agent sessions; SWE-rebench
   displays the re-read share as a column ("Cached 94.9%"). The one regime left open by the pressure-point
   report, 300–500 steps, is OSWorld 2.0, whose released trajectories carry no token fields (inspected
   below), and Terminal-Bench's team-verified run logs could not be located as a download.

The maintenance condition also fails: of the four log sources named in the definition, HAL "paused updating"
(leaderboard) with its dataset last modified 2026-02-01, METR's page says "This page is no longer actively
updated", SWE-rebench releases no per-run trajectories, and OSWorld's trajectories are 99 zips totalling 495 GB
with screenshots and no usage fields. A tracker "that updates when a source leaderboard releases new logs"
would be tracking two paused sources and two that do not release what the metrics need.

## Incumbent table

Each row: what the incumbent ships of (1) pass^k / per-task bimodality across generations, (2) effort curves,
(3) prefix-aware cost; what it does not; whether it has announced the rest; source; date; verbatim quote.

| Incumbent | (1) reliability across generations | (2) effort curves | (3) prefix-aware cost | Does not ship / announced | Source, date, quote |
|---|---|---|---|---|---|
| HAL leaderboard | No: single runs. | Effort labels per entry ("o3 Medium", "o4-mini Low", "Claude Sonnet 4.5 High"); the paper's 21-of-36 finding. | Dollar cost per entry at list price; caching ignored. | pass^k, tokens, multi-run: not on the board. Announced: paused. | hal.cs.princeton.edu, 2026-10-10: "We have paused updating HAL leaderboard with new models and are currently focusing on measuring reliability in AI agents." Latest entries "September 2025". arXiv:2510.11977 (2025-10-13): "For HAL, we were forced to rely on single runs without statistical validation for most evaluations." B14: "our cost calculations don't yet account for cache hits, reporting full token prices instead." |
| HAL reliability tracker | **Yes.** 15 agents, 2 headline benchmarks (GAIA; τ-bench airline clean/original), twelve metrics incl. outcome consistency (2p̂ − 1)² and the pass@k–pass^k gap; models from o1 to Opus 4.7 / GPT-5.5 / Gemini 3.5 Flash; longitudinal claim stated. | No. | No ("Cost and caching: not mentioned"). | Opus 4.8 missing; no roadmap beyond a recommendation. | hal.cs.princeton.edu/reliability, 2026-10-10: "We evaluate 15 agents across 2 benchmarks on twelve metrics spanning four reliability dimensions"; "overall reliability shows only small improvements over time while accuracy steadily climbs"; "all new models make a noticeable jump in accuracy, but their reliability is not improving at nearly the same rate"; "we did not yet have a chance to evaluate Claude Opus 4.8"; "Current benchmarks are too static". Earlier results "covered frontier models released up until January 2026." |
| METR time horizons | **Raw material shipped.** `task_results_1_1.yaml`: per (agent, task) `n_successes`, `n_runs` (4–8), `human_minutes`, `task_weight`; 23 agents with `release_date` from 2023-03-14 to 2026-04-07. Page states the thirds for GPT-5 (Q81). | No; effort not varied. | No; "We don't report the exact time it takes an AI agent". | pass^k not displayed; page retired. | metr.org/time-horizons, 2026-10-10: "We launch 6 independent runs for each task."; "This page is no longer actively updated."; "Measurements above 16 hrs are unreliable with our current task suite." |
| Epoch AI Benchmarking Hub | Repeated runs with ±1 SE on QA-style benchmarks ("16 times on GPQA Diamond […] 8 times on MATH Level 5"); no pass^k. | No ("each model's API-default temperature"). | No cost text. | Only agentic benchmark: SWE-bench Verified; logs behind a CAPTCHA viewer; data as CSV/Airtable. | epoch.ai/benchmarks, "Updated Oct. 10, 2026": "a confidence interval of plus and minus one standard error around the 'true' mean evaluation score". |
| Artificial Analysis | No pass^k; three repeats per task averaged into pass@1. | **Yes as entries**: every effort variant evaluated and plotted ("Claude Haiku 5.5 (High)", "(Low)", "(Medium)", "(Max)", "(Xhigh)"); TB 4.0 rows "Claude Opus 5.5 (Max, Default Fallback) 59.6%", "Claude Opus 5.5 (Xhigh, Default Fallback) 59.6%". | **Cache-aware pricing**: "Each evaluation's cost is calculated from input, cache hit, cache write, reasoning, and answer token prices". | Per-run data not public; no re-read split by step. | artificialanalysis.ai and /evaluations/terminalbench-4-0, 2026-10-10: "We run all 66 Terminal-Bench 4.0 tasks with the mini-swe-agent harness and report pass@1 averaged over three repeats per task." Changelog latest "8 Oct". |
| Vals AI | 3-run averages with range; pass@1 only. | Effort fixed ("compute effort set to 'max'"). | Cost per test ("$15.68 per test"); caching not discussed. | No pass^k, no CIs ("within noise"). | vals.ai, 2026-10-10: "Terminal-Bench 2.1 was averaged over 3 runs (71.9%–78.7%)."; "We hold one harness fixed and report pass@1." |
| Scale SEAL | Score ± CI per entry; runs unstated. | Effort labels in names ("Opus 5 (Claude Code) xhigh 99.40±0.40"). | No cost or tokens. | No methodology text on runs or CI. | labs.scale.com/leaderboard, 2026-10-10 (no page date). B07: capped runs "turn limit of 50. All others […] turn limit of 250." |
| LMArena (now arena.ai) | Human votes; no runs. | Effort labels in names ("Claude Opus 5.5 (High)"). | Cost per task in the Pareto view only ("$1.64/task"). | No pass^k, tokens, consistency. | arena.ai/leaderboard, 2026-10-10: "live leaderboards for text, code, image, video, and vision, powered by millions of human votes." |
| Inspect Evals (UK AISI / Generality Labs) | Not a leaderboard. | — | — | No results, no public logs (`.eval` logs only via an issue uploader). | github.com/UKGovernmentBEIS/inspect_evals README, 2026-10-10: "A library of evaluations built using Inspect AI." |
| SWE-rebench (Nebius) | Pass@5 per row (5 runs exist internally); no pass^k; per-run outcomes not released. | Effort variants as rows ("[high]", "[medium]", "[xhigh]"; "Added gpt-5 (medium, high, minimal)" 2025-08-12). | **Re-read share as a column**: "Tokens/Problem 2,518,308, Cached 94.9%" (B11); "Introduced Cached Tokens column" 2025-12-05. | Trajectories not released (the HF leaderboard dataset is problems only); cost convention unexplained. | swe-rebench.com, 2026-10-10: window "From 15/05/2026 to 01/07/2026"; B13: "It does not report pass^k." |
| Galileo Agent Leaderboard v2 | LLM-judged Action Completion and Tool Selection Quality; no pass^k. | No ("Reasoning models generally lag behind"). | Cost per session ("$0.014 per session"), convention unstated. | Last results 2025-07-17. | github.com/rungalileo/agent-leaderboard README, 2026-10-10: "Key Results (July 17, 2025)". |
| Toolathlon | **Pass^3 per row** beside Pass@1 ± and Pass@3; rows span generations but no trend is drawn. | Effort in names ("GLM 5.3 Flash (max)"). | None ("Cost or token figures: None"). | Missing values shown as "--". | toolathlon.xyz, B57/B58 (2026-10-09): "Kimi K3 (max) 76.5 ± 1.9, Pass@3 83.3, Pass^3 68.5". |
| arXiv:2610.04433 (Liu, Han) | Rerun calibration: "swapping the harness flips as many tasks as rerunning the same harness, 13% in both cases". | No. | **Mechanism measured**: "cost per task differs by up to 3x across harnesses. The gap is set at the first call, by the preamble […] and scaled by the number of steps […] The provider's price for cached input scales the bill and does not reorder it." | Horizon: SWE-bench Verified, 447 tasks, 3 harnesses, 5 models (tens of steps). | arXiv API, v1 2026-10-03. |

Neighbors found by the density search (abstracts via the arXiv API, all in-window): arXiv:2601.06007 "Don't
Break the Cache" (2026-01-09): "prompt caching reduces API costs by 41-80% and improves time to first token by
13-31% across providers" on "over 500 agent sessions"; arXiv:2609.33812 "Identical Runs, Different Results"
(2026-09-27): 584 runs, "cost differed more than twentyfold between two agents on the same model, mostly
through the prompt cache"; arXiv:2608.14711 "Beyond Pass@k" (2026-08-11): reliability@k "with n = independent
rollouts"; arXiv:2604.24579 (2026-04-27): pass@k, pass^k and the reliability decay curve "are projections of
one success-time distribution"; arXiv:2601.06112 ReliabilityBench (2026-01-03): pass^k under perturbation and
fault injection; arXiv:2610.00651 (2026-09-30): Bayesian variance decomposition over "22 benchmarks from the
Holistic Agent Leaderboard and Harbor Index"; arXiv:2607.18462 (2026-07-20): patch quality "across model
generations" on SWE-bench Lite; arXiv:2608.14903 (2026-08-14): audit of the METR record, "52 of 71
substantive quantitative events, or 73.2 percent, come from one measurement programme".

One-sentence tricks (checklist rule 2): HAL = one harness that runs many agents on many benchmarks and logs
every model call with its cost. HAL reliability tracker = run each agent several times and score how often the
same task comes out the same way. METR time horizon = fit the human-minutes length at which a model's success
rate crosses 50% (or 80%). Artificial Analysis = run public benchmarks itself on every public model variant
and price the tokens. SWE-rebench = freshly mined GitHub issues each month so models cannot have memorised
them, five runs each. 2610.04433 = hold the model fixed, swap the harness, rerun, and see that cost moves 3×
while score moves within rerun noise. 2601.06007 = switch provider caching on and off on the same agent
sessions and bill the difference. Sharpening Tax (2610.01509) = compare base and post-trained pairs by how
many tasks go from sometimes-solved to always- or never-solved.

## Data-availability check

Question per source: do the public logs contain per-step input/output token counts, per-task multi-run
outcomes (k ≥ 2), reasoning-effort settings and step caps? Field names are from files I opened.

| Source (file inspected) | Per-step tokens | Multi-run per task | Effort setting | Step cap | Verdict for (1)/(2)/(3) |
|---|---|---|---|---|---|
| **HAL traces**, Hugging Face `agent-evals/hal_traces` (380 zips, 113 GB, last modified 2026-02-01; each zip holds one `*.json.encrypted`, PBKDF2-SHA256 → Fernet with the fixed password published in `hal-harness/hal/utils/upload.py`; decrypted three files, 2.6 KB / 11.9 MB / 30 MB / 56 MB) | **Yes.** `raw_logging_results[i].output.usage.{prompt_tokens, completion_tokens, total_tokens}`, `completion_tokens_details.reasoning_tokens`, `prompt_tokens_details.cached_tokens` (present on 778 of 1,414 and 1,396 of 2,028 calls in the two τ-bench files — the OpenAI-served calls); `total_usage.<model>.{cache_creation_input_tokens, cache_read_input_tokens}` (both 0 for the Anthropic-served agent: caching was off); full `inputs.messages` per call, `started_at`/`ended_at`, `summary.weave.latency_ms`, `weave_task_id`. | **Mostly no.** One run of the task set per file (50 tasks in `swebench_verified_mini` and `taubench_airline`); outcomes in `results.successful_tasks` / `results.failed_tasks` and `raw_eval_results[<task>].reward`. Of 380 files, 19 agent–model combinations have 2–3 uploads (e.g., `swebench_verified_mini_sweagentclaudeopus4120250805` ×3, uploaded 2025-08-07, 2025-08-07, 2025-10-06); the rest are single. | **Yes** where used: `config.agent_args.reasoning_effort` ("high"); 94 of 380 file names carry an effort label (low/medium/high/minimal/xhigh/thinking); pairs exist for o3-mini, o4-mini, Claude 3.7, Opus 4.1 (none/high), GPT-5 (minimal/medium/high on browser-use). | Not a field; harness-specific. | (3) computable (tens of steps: 8–10 calls per SWE-bench Mini task, 28–41 per τ-bench task, simulator calls logged in the same list). (2) computable but already published by HAL from these logs. (1) across generations: not computable (k = 1 for 361 of 380 files). Quality caveat: the o3-mini-high SWE-bench Mini file scores 0 of 50 — broken runs are in the set unflagged. |
| **METR** `metr.org/assets/task_results_1_1.yaml` (686 KB) | No. | **Yes.** `n_successes`, `n_runs` (4–8; one run has 13) per `task_id` for 23 agents (213–228 tasks each) with `release_date`; also `human_minutes`, `task_weight`. | No (one setting per agent). | Token and time limits exist ("up to a token and time limit") but are not in the file. | (1) computable for one suite, trivially; (2), (3) not. |
| **OSWorld-Verified trajectories**, `xlangai/ubuntu_osworld_verified_trajs` (99 zips, 495 GB; listed one 3.4 GB zip's central directory by HTTP range request and read one `traj.jsonl`) | **No.** `traj.jsonl` fields: `step_num`, `action_timestamp`, `action{name, input, id, action_type, command, raw_response}`, `response`, `reward`, `done`, `info`, `screenshot_file`; per task also `result.txt`, `runtime.log`, `recording.mp4`, `step_*.png`. `args.json`: `max_steps`, `max_tokens: 1000`, `temperature: 0.0`, `history_n: 3`. | **Barely.** Card: "And multiple runs."; 3 of 99 zips carry a `-1` duplicate suffix. | No (one model configuration per zip). | **Yes, by file**: 75 of 99 zip names carry 15/50/100/300-step caps (`claude-sonnet-4-5-20250929_15steps.zip`, `_50steps`, `_100steps`). | (3) not computable (no usage; screenshots dominate input anyway). (2) by step cap is already the leaderboard's own display. (1) not computable. These are OSWorld-Verified (v1) runs; OSWorld 2.0 (arXiv:2606.29537, 500-step) trajectories were not found on the Hub. |
| **SWE-rebench** (`nebius/SWE-rebench-leaderboard` card and tree; `nebius/SWE-rebench-openhands-trajectories` card) | **No.** Leaderboard dataset = problems only (`repo, instance_id, patch, test_patch, FAIL_TO_PASS, docker_image, harbor_verifier_timeout_sec`, 860 test rows plus monthly splits). The trajectories dataset (67,074 trajectories, one model) has `trajectory`, `model_patch`, `exit_status`, `resolved`, `gen_tests_correct` — no usage fields. | Pass@5 on the site implies 5 runs internally; per-run outcomes are not released. | Labels on the site only. | Not released. | None of (1)–(3) computable from released data; the site already displays the cached share. |
| **Terminal-Bench 2.0 team-verified runs** | Not located. The 2.0 leaderboard URL now serves the 4.0 landing page (headers RANK, MODEL, AGENT, RESOLUTION RATE, COST, TOKENS; empty rows); the Harbor Hub leaderboard renders "Loading leaderboard…" in text; the GitHub README says "tagged releases published on the Harbor Hub" and describes running (`harbor run … -k 5`), not downloading, runs. | Not located. | Not located. | Harness flag `--ak reasoning_effort=max` exists. | Cannot be assumed; B15 (2026-10-09): the 2.0 table "has no cost or token fields". |

Consequence. (1) at the breadth the definition claims (9 benchmarks, across generations) cannot be computed
from free data; METR's single suite can, and HAL's tracker already does it for two. (3) is computable only on
HAL's tens-of-steps logs, where 2610.04433 has already measured the mechanism on a larger set (447 tasks × 5
models × 3 harnesses) and found no reordering. The "modest API re-runs" clause does not rescue (1): 2609.33812
reports that at observed run-to-run spread "resolving the agent differences we observed would take tens to
more than a hundred runs of each", so five runs per effort level ranks nothing.

Computation from METR's file (my script, unweighted shares of tasks per agent; `always` = `n_successes ==
n_runs`, `never` = `n_successes == 0`, `mixed` = the rest; the 66 short SWAA tasks are included and runs per
task vary 4–8, so the numbers are illustrative, not a result):

| release date | agent | tasks | always | never | mixed |
|---|---|---|---|---|---|
| 2023-03-14 | GPT-4 0314 | 213 | 0.34 | 0.46 | 0.20 |
| 2024-10-22 | Claude 3.5 Sonnet (New) | 226 | 0.47 | 0.34 | 0.19 |
| 2025-08-07 | GPT-5 | 228 | 0.71 | 0.17 | 0.12 |
| 2026-02-05 | Claude Opus 4.6 | 228 | 0.77 | 0.10 | 0.13 |
| 2026-04-07 | Claude Mythos Preview (early) | 228 | 0.83 | 0.07 | 0.10 |

On this suite the coin-flip share halves (0.20 → 0.10) while the always-solved share more than doubles, i.e.
unanimity rises with accuracy; on HAL's two benchmarks the tracker says reliability is nearly flat. Any
"is reliability improving?" paper is therefore a fixed-suite, fixed-harness question whose answer depends on
the suite, and the two public suites already give two answers.

## Personas

### 1. The incumbent — "we already ship this"

Objection (HAL): the reliability tracker is the artifact — 15 agents across generations, outcome consistency,
pass@k vs pass^k, longitudinal statement, maintained ("Since then, every frontier provider has released
updated models", Opus 4.7 / GPT-5.5 / Gemini 3.5 Flash present, Opus 4.8 pending). The effort finding was
drawn from the same 26,597 rollouts Shape A would re-score. Objection (Artificial Analysis): every effort
variant is a row with cache-aware cost and three repeats; the effort curve is read off the rows. Objection
(SWE-rebench): the re-read share is a column ("Cached 94.9%"), introduced 2025-12-05.

Answer: conceded for (1) and (2). For (3) the step-level split and the 300–500-step extrapolation are not
shipped by anyone (SWE-rebench's own text shows only a cached share; HAL's own text says caching is ignored),
but the result that would justify shipping them — a reordering — is already published as negative at tens of
steps (2610.04433: "does not reorder it") and the long-horizon logs have no token fields. "Nobody ships the
step split" is true and does not matter.

### 2. The would-be user

Eval lead at a lab: has internal multi-run data on current models; the tracker would offer k = 2–3 on 19
combinations of 2025 models (Claude 3.7, o3, o4-mini, Opus 4.1, Sonnet 4.5, Haiku 4.5) because that is what
HAL uploaded; HAL's board stops at "September 2025" and METR skipped models ("some models were measured long
after release and others were skipped entirely"). Benchmark owner (Nebius, Sierra): SWE-rebench already runs
five attempts per problem and chooses to display Pass@5; τ-bench's board displays "one Pass^1 column" (B23).
A tracker cannot display outcomes the owner does not release. Paper author comparing agents: needs the models
in their own table at k ≥ 8; 2609.33812's resolution arithmetic says 2–5 runs do not rank. What would make
them cite it: a number for a current model they cannot compute themselves. The shape has none.

Answer: conceded. The user who exists (a reader of launch tables) is served by Artificial Analysis and
Toolathlon's Pass^3 column today.

### 3. The systems reviewer

Can the metrics be computed from the logs as they exist? From the table above: (3) yes on HAL (per-call
`prompt_tokens`, `cached_tokens` where the provider reports it, full `messages` for an exact message-level
diff; 113 GB encrypted with a published key — decryption of a 56 MB file took seconds); (1) no beyond METR; (2)
yes on HAL for 2–3 effort points per model, single run each. Maintenance per month: HAL dataset unchanged
since 2026-02-01 and the board paused; METR retired; SWE-rebench a new window roughly monthly with no logs;
OSWorld zips of 1–13 GB each with screenshots; Terminal-Bench moved to Harbor Hub with a JavaScript
leaderboard and no located run download. Also from HAL's own paper: endpoint drift makes "k runs of the same
model" ill-defined across months ("Together AI changed their DeepSeek R1 endpoint to serve DeepSeek R1 0528
on release day, keeping the same API endpoint name"; "OpenRouter could serve a model with FP4 for one call
and FP8 for another", B54), and HAL's 19 duplicate uploads are months apart (2025-08 and 2025-10 for one
SWE-agent Opus 4.1 trio) with no field stating whether the scaffold changed between them.

Answer: conceded. Ingest is feasible for one source (HAL) at one horizon; the product's refresh depends on
sources that have stopped or do not release.

### 4. The RL reviewer

Is the metric well-defined? pass^k needs a conditioning set — same tasks, harness, effort, provider endpoint,
sampling settings, time window — and the estimator is unsettled even at HAL ("The old estimator overcounted
spread by a factor of K/(K−1). This caused every non-unanimous task to collapse to 0", B56). The quantity
varies by suite (METR's thirds move; HAL's two benchmarks do not), so "reliability across generations" is a
property of (suite, harness, k), not of the generations. Do the papers that fall out have a mechanism and a
method consequence? #6 ("is reliability improving?") has a headline and no mechanism; #7's cross-version
bimodality question is answered in direction by Sharpening Tax ("post-training pushes tasks toward two
extremes, always solved or never solved", 14 pairs, 42 cases); #3's decomposition (grader / timeout / policy)
is the one mechanistic question in the list and it needs re-runs with doubled timeouts and scope-neutral
grading — new rollouts, not re-scoring — so an observatory of existing logs cannot answer it; #2's long-horizon
reordering has no token data to test it.

Answer: conceded. The shape's re-scoring produces headlines whose mechanisms sit in experiments the shape does
not run.

### 5. The professor who dismisses it in ten minutes

"This is a leaderboard, not research." The sentence that would answer: "the research question is whether
these three metrics reorder the frontier, and nobody has checked." It is not true: 2610.04433 checked cost
("does not reorder"), HAL checked effort (21 of 36 reversals) and the tracker checked reliability versus
accuracy ("rank different models", B56), and 2610.00651 decomposed leaderboard variance over 22 HAL and Harbor
benchmarks. What is left is maintenance of a derived chart.

Answer: conceded.

## Density (12-month window, arXiv API, 3 s pauses; raw XML and JSON in `scratchpad/shapeA/arx/`)

All queries ran as `(<query>) AND submittedDate:[202510090000 TO 202610110000]`, newest first, max 50.
"total" is the API's `opensearch:totalResults`.

| key | query | total | note |
|---|---|---|---|
| P1 | "pass^k" AND reliability AND agent | 21 | 2608.14711, 2604.24579, 2601.06112, 2602.07150, 2604.14877 on the metric; none longitudinal |
| P2 | "pass@k" AND reliability AND agent AND consistency | 8 | subset of P1 |
| P3 | "pass^k" AND agent AND (generation OR longitudinal OR "over time" OR trend) | 22 | no hit tracks pass^k across model generations |
| P4 | agent AND reliability AND bimodal | 4 | none on agent benchmarks |
| E1 | agent AND ("reasoning effort" OR "reasoning budget" OR "thinking budget") AND (non-monotonic OR degrades OR hurts OR lower) | 19 | 2603.07915 Ares, 2606.01667 ATLAS, 2609.40284 cua-speedrun; none decomposes the decline |
| E2 | agent AND "reasoning effort" AND accuracy | 11 | includes HAL 2510.11977 |
| E3 | agent AND ("step cap" OR "step limit" OR "turn limit" OR "step budget") AND (timeout OR truncat OR degrad) | 5 | none on leaderboard caps |
| C1 | agent AND prefix AND ("re-read" OR reread OR "input tokens") AND cost | 1 | serving-side only |
| C2 | agent AND "prompt caching" AND cost AND (benchmark OR leaderboard) | 4 | **2601.06007**, **2609.33812**, 2609.23790 |
| C3 | agent AND "cached tokens" AND cost | 4 | StepKV (2609.22158), 2601.06007 |
| L1 | leaderboard AND agent AND (cost OR reliability) AND (tracker OR longitudinal OR "over time") | 2 | neither relevant |
| L2 | leaderboard AND agent AND cost AND reliability | 9 | 2610.00651, 2603.23749, 2607.26191, HAL |
| L3 | agent AND benchmark AND ("model generations" OR "successive models" OR "release date") AND (reliability OR variance OR consistency) | 58 | one relevant: 2607.18462 (patch quality across generations) |
| T1 | agent AND (trajectories OR logs OR rollouts) AND ("re-score" OR rescore OR "re-analysis" OR …) AND benchmark | 7 | 2610.11678 TRACE (verifier brittleness) is the only re-scoring of public logs |
| T2 | "time horizon" AND agent AND (reliability OR "80%" OR "per-task") | 9 | 2608.14903 audit |

Pre-window precedents (named, abstracts fetched): τ-bench, arXiv:2406.12045 (2024-06-17) — "We also propose a
new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials […] pass^8 <25% in
retail"; METR, arXiv:2503.14499 (2025-03-18) — "50%-task-completion time horizon"; AI Agents That Matter,
arXiv:2407.01502 (2024-07-01) — "a narrow focus on accuracy without attention to other metrics […] jointly
optimizing the two metrics" (cost-controlled evaluation, the HAL lineage); HAL, arXiv:2510.11977 (2025-10-13,
four days inside the window edge) — "We share all agent logs, comprising 2.5B tokens of language model calls".
Density reading: the window is dense on reliability metrics (21 groups touching pass^k) and on caching cost
(three groups measuring it on agents), and empty on exactly the two things the shape would add — a
longitudinal pass^k across suites (0 hits; occupied by the HAL tracker and METR's file rather than by
papers) and a step-level re-read split at 300+ steps (0 hits; no data).

## Narrowest surviving version

None as a product. The one fragment that is free and unoccupied is a one-week note, not a tracker: compute
the always/never/mixed shares per agent from METR's file with the published `task_weight` and the SWAA tasks
removed, put HAL's 19 duplicated runs beside it as k = 2–3 unanimity on τ-bench airline and SWE-bench Mini, and
state that the sign of "reliability versus accuracy across generations" depends on the suite. It is a
footnote because METR's page already states the thirds for GPT-5, HAL's tracker already states the flat case,
and Sharpening Tax already states the direction on 14 base/post-trained pairs.

Re-open condition (recorded, not recommended): Harbor publishes per-trial token usage for Terminal-Bench 4.0
team-verified entries (the empty 4.0 board already has COST and TOKENS headers) and SWE-rebench releases its
five per-problem runs. Then (1) at k = 5 and (3) at tens of steps become a zero-compute two-week computation,
and the only question worth asking is whether 2610.04433's "does not reorder" holds under Terminal-Bench's
2-hour, 100-million-token tails (B17). Cost of checking the condition: one fetch a month.

## First measurement and its cost

For the surviving note: zero GPU-hours; downloads of 686 KB (METR) plus about 6 GB (HAL's 19 duplicated
combinations, decrypted with the published key); API dollars $0; one week of one student. For the brief's
"modest API re-run" clause (one open model at four effort levels × five runs) on τ-bench airline: 50 tasks ×
4 × 5 = 1,000 rollouts; at 30–60 rollouts per H100-hour for a 32B agent that is 17–33 H100-hours (about
$50–100 at $2–3 per H100-hour), plus the simulated user at roughly 0.7M prompt tokens per run (HAL's
`total_usage` for gpt-4o on one τ-bench run: 685,428 prompt tokens) → about 14M tokens, about $35 at $2.50
per million. Total: about 25 H100-hours and about $150. It is not worth running: it reproduces HAL's 21-of-36
observation on one benchmark at k = 5, which 2609.33812's resolution arithmetic says cannot rank effort levels.

## The two closest incumbents' own text (verbatim)

Read as abstracts and page text; the limitation sections of the two papers were not reached because
`arxiv.org` refused the fetch (HTTP 429) — mark this report abstract-only for those two papers.

- HAL (arXiv:2510.11977, abstract, 2025-10-13): "We validate the harness by conducting 21,730 agent rollouts
  across 9 models and 9 benchmarks […] Our analysis reveals surprising insights, such as higher reasoning
  effort reducing accuracy in the majority of runs. […] We share all agent logs, comprising 2.5B tokens of
  language model calls, to incentivize further research into agent behavior." B50 (paper text, fetched
  2026-10-09): "High evaluation costs prevent uncertainty estimation. […] For HAL, we were forced to rely on
  single runs without statistical validation for most evaluations." Tracker page (2026-10-10): "we did not
  yet have a chance to evaluate Claude Opus 4.8"; "Current benchmarks are too static".
- 2610.04433 (abstract, 2026-10-03): "The gap is set at the first call, by the preamble of system prompt and
  tool schemas each harness sends with every step, and scaled by the number of steps; per-step growth and
  per-call tool output differ far less. The provider's price for cached input scales the bill and does not
  reorder it. The rerun data also give the resolution a harness comparison needs: at the discordance we
  observe, 45 tasks catch a 13-point gap only half the time and no gap with 80% power, and 447 tasks resolve 5
  points".
- 2601.06007 (abstract, 2026-01-09), the closest caching paper: "To our knowledge, no prior work quantifies
  these cost savings or compares caching strategies for multi-turn agentic tasks. […] prompt caching reduces
  API costs by 41-80%".

## Checklist items triggered

- "Nobody has done X" cites the two closest incumbents' own text (2026-10-09 item): applied to "nobody ships
  the re-read split" — SWE-rebench's "Cached 94.9%" column and HAL's "don't yet account for cache hits" quoted;
  the sentence is true and immaterial.
- Density queries include failure-mode and operations words (2026-10-09 item): timeout / truncat / degrad /
  non-monotonic / "cached tokens" / rescore used; counts above.
- 12-month window plus at least two pre-window precedents (2026-10-08 item): τ-bench 2024-06, METR 2025-03,
  AI Agents That Matter 2024-07 named with fetched abstracts.
- "Why now": the enabling pieces (HAL's log release 2025-10, METR's per-task file) landed a year ago and
  were consumed by HAL's own paper and tracker — a red flag the shape did not clear.
- Premise numbers carry the source's category and denominator: "21 of 36 model-agent-benchmark
  combinations"; "15 agents across 2 benchmarks"; "Cached 94.9%" of Tokens/Problem for one row; METR shares
  are unweighted over 213–228 tasks including SWAA.
- A first measurement names a runnable benchmark: τ-bench airline is runnable (HAL harness, public tasks);
  OSWorld 2.0's released trajectories were not found, so no measurement is placed on them.
- "Unposed" verdicts read beyond the abstract: not met for the two papers (429); flagged above rather than
  claimed.
- Regime stated: HAL logs are tens of steps; the shape's open regime (300–500 steps) has no public token
  data.

## New checklist lessons (for Jacob to add; checklist.md not edited)

1. **Public-log claims must name the field.** A shape that says "re-score public trajectories" lists, per
   source, the exact per-step token field, the per-task outcome field and the run count before it is written
   up; "26,597 rollouts" was 380 single-run files with 19 duplicates, and 495 GB of OSWorld zips had no usage
   field. Rule: open one file from each source and paste the field names into the shape.
2. **A maintained leaderboard row is an artifact.** Artificial Analysis's effort variants and SWE-rebench's
   cached column are "effort curves" and "prefix-aware cost" without using those words; search incumbents'
   column headers and entry labels, not only their methodology prose.
3. **"Tracker" shapes inherit their sources' cadence.** Before proposing a living artifact, record each
   source's last update date and release policy (HAL dataset 2026-02-01, board paused; METR retired; SWE-rebench
   monthly, no logs). Two of four paused sources is a kill.
4. **Encrypted-but-published data counts as free data.** HAL's traces are encrypted with a password printed
   in the harness source; treat such data as available, and decrypt with your own code rather than running the
   repository's.
5. **A derived chart from one YAML is not a product.** If the headline computation takes 30 lines on one
   released file (METR's per-task counts), the value is the file, and its owner has already said the headline.
6. **Fetch budget for arXiv.** `arxiv.org/abs` fetches rate-limit at 429 after other pages in the same
   session; route id lookups through `export.arxiv.org/api/query` from the start and reserve page fetches for
   full-text limitation sections.

VERDICT: killed
Narrowest surviving version: a one-week, zero-compute note that computes always/never/coin-flip task shares
across METR's 23 released model generations (weighted, SWAA removed) beside HAL's 19 duplicated runs, and
states that whether "reliability improves with accuracy" depends on the suite. It is a footnote to METR's
own thirds, HAL's tracker and Sharpening Tax, not a paper or a product.
First measurement cost: 0 GPU-hours and $0 for the note (about 6 GB of downloads); the brief's optional
re-run (one open 32B model, four effort levels × five runs on τ-bench airline) is about 25 H100-hours and
about $150, and reproduces a published observation.
