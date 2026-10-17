# Product red team — Shape C: simulator-fidelity instrument for user-simulator benchmarks

Date: 2026-10-10. Brief: `data/pressure/2026-W41/product-shapes.md` (Shape C). Inputs read: `prompts/checklist.md`,
pressure point #12 and Section 4 of `2026-W41-pressure-points.md`, the P7 section of `2026-W41-redteam-top3.md`
(P7(ii) is the parked λ measurement this shape productizes), the P8 section of `2026-W41-problem-shortlist.md`
and its 27 member records. Fetched today and read in full text (not abstracts): τ-bench, τ²-bench, ττ-bench,
τ-Voice, τ-Knowledge, τ-Multilingual, SABER / τ-Bench Verified, and eleven P8 or variance-decomposition papers;
plus taubench.com, the tau2-bench leaderboard submission guide, three Sierra blog posts, the τ³ task-fixes post,
the Thinking Machines determinism post, and one backgammon article. Raw PDFs, text and arXiv API XML are in the
session scratchpad under `shapeC/` (treated as untrusted data; Python run with `-I`). Nothing below is from memory.

**Verdict in one line: parked.** The product as written is not computable: a fixed simulator seed does not fix
the simulator's replies once the agent's messages differ, so the "simulator-induced share" of the nested seed
design is structurally near zero whatever the simulator does. The decomposition the shape wants is already
written down as Eq. 6 of a published paper (One Frozen Simulator, Aug 2026) and declared there as the cleaner
diagnostic left unmeasured. The identifiable replacement (a per-turn attribution) costs 3–7× the brief's budget
and measures a quantity the benchmark owners define as the agent's job. Re-open condition and cost at the end.

Terms used throughout. **Simulated user / simulator**: a language model prompted to play the customer the agent
talks to. **pass^k**: the chance a task is solved in all k of k repeated trials, averaged over tasks (τ-bench's
reliability metric). **Seed**: the number that fixes a sampler's random draws, so the same prompt with the same
seed gives the same text. **Nested design**: repeat each task under several simulator seeds, and under each of
those several agent seeds, so that the two sources of randomness can be told apart statistically. **Law of total
variance**: the identity that splits the spread of an outcome into the spread caused by one factor plus the
average spread left over once that factor is fixed. **Critical simulator error**: a simulator turn that makes the
task impossible for a correct agent (τ²-bench's annotation category). **Temperature**: the sampling knob; 0 means
always take the most likely token. **Batch invariance**: a serving property under which a request's output does
not depend on which other requests share the GPU batch; without it, temperature 0 is not deterministic.

---

## 1. Incumbent table

| Artifact | What it ships (verbatim where it matters) | What it does not ship | Source, date |
|---|---|---|---|
| τ-bench paper | Defines pass^k. Protocol: "The LM temperature is 0.0 for agent and 1.0 for user." Design intent: "for the same task, the user prompt and database transitions are the same, with just the LM sampling of the user and agent messages generating sufficient stochasticity. Thus, pass^k can capture the reliability of the agent at handling variations in conversations with the same underlying semantics". Failure audit of 40 gpt-4o retail failures: "4 of them are caused by user instruction typo or ambiguity (and then fixed), and the remaining 36 failure cases are agent issues". Per-task rates from "at least 40 gpt-4-turbo trials". | No variance split by source. Simulator variation is treated as the test stimulus: "the onus is on the agents to handle diverse users." | arXiv:2406.12045, 2024-06-17 |
| τ²-bench paper | "Each task is run four times, maintaining a consistent LLM temperature of 0 to promote deterministic outputs." Names "Three primary sources of uncertainty [...]: implementation errors, task specification errors, and user simulator errors." Annotates simulator errors (Table 2): airline 100 conversations, 13 (13%) critical, 34 (34%) benign; retail 50, 6 (12%) critical, 14 (28%) benign; telecom 50, 3 (6%) critical, 5 (10%) benign. pass^k still decays at temperature 0 (gpt-4.1 retail 0.74 at k=1 to about 0.53 at k=4, Figure 3 plot labels). | No seed experiments; no share of pass^k decay attributed to agent, simulator or reward. Conclusion: "Works remains to be done to improve the user simulator." | arXiv:2506.07982, 2025-06-09 |
| τ³ (= τ-Knowledge + τ-Voice + task audit; taubench.com) | Task audit, Feb 2026: 27 airline and 26 retail tasks fixed; "Many tasks had user simulation instructions that left key information underspecified, causing the simulated user to behave unpredictably across trials"; the fixes "primarily reduced variance across trials rather than uniformly boosting scores"; "pass^4 improvements were often even larger than pass^1 improvements" (GPT-5.2 (high) airline pass^4 50.0% → 72.0%); fixes removed "evaluation noise that turned some correct completions into false negatives". Chart: "4 trials per task." | The leaderboard "describes [...] the passk reliability metric" but every table has one Pass^1 column; no variance, confidence intervals or error bars anywhere on the page. | taubench.com and taubench.com/blog/tau3-task-fixes.html, fetched 2026-10-10 (post dated February 2026) |
| tau2-bench leaderboard submission guide | "We recommend using `gpt-5.2` as the user simulator for the most accurate results." "we strongly prefer results with at least 4 trials per domain for statistical reliability". "Voice submissions typically only report Pass^1 scores since multi-trial evaluation with audio-native models is expensive". | No simulator temperature, no seeds, no definition of how pass^k is computed. | github.com/sierra-research/tau2-bench/docs/leaderboard-submission.md, fetched 2026-10-10 |
| τ-Knowledge (τ³-Banking) | "the user is simulated by an LLM, which could introduce stochasticity and/or instruction-following errors that we must verify do not unfairly penalize or reward agents." Verification is annotation: "Across 194 annotated trajectories, only 4 contained task-critical user errors". Simulator "standardized to GPT-5.2 with low reasoning effort, which we found to exhibit few task-critical errors." Graded arm exists: "Because passˆk scores are based on a binary pass/fail measure on tasks, we introduce Action Recall as a proxy for measuring how close the agent got to task success". | No variance split; the graded metric is not connected to pass^k decay. | arXiv:2603.04370, 2026-03-04 |
| τ-Voice | Seeds the non-LLM parts: "Given a seed, all stochastic elements are deterministic for controlled comparison across agents; full reproducibility is limited only by LLM output variance." "stochasticity arises from agent and simulator LLMs." Reliability: "2 independent runs per condition on the Retail domain", paired permutation tests. | No agent-versus-simulator split; LLM randomness explicitly left unseeded. | arXiv:2603.13686, 2026-03-14 |
| τ-Multilingual | One or two trials per cell; "cost limited additional languages, models, and trials." | No variance analysis. | arXiv:2609.35820, 2026-09-21 |
| ττ-bench (hyper-τ-bench) | Client and user are LLM simulators; tool faults replay deterministically ("seeded delays where timing is involved, so repeated trials replay identically"). Limitation (2): "Compute costs limit each configuration to one construction trial per task; scores average over 53 tasks, but per-task variance across repeated builds is not characterized and would be an interesting addition to study." | No repeated trials at all. | arXiv:2609.04611, 2026-09-04 |
| Sierra blog posts | 2025-03-18: pass^k "exposed how even strong models degrade over multiple attempts"; "This unsolved gap in reliability represents one of 𝜏-bench's key values"; remedy named is "improved user simulation during training or specialized fine-tuning on multi-turn tasks". 2025-06-10 (τ²): "user simulators are error-prone or unpredictable"; telecom "tightly couples the user simulator to the environment". | Neither post mentions variance, repeated-run analysis, or attributing the decay to the simulator. | sierra.ai/blog, fetched 2026-10-10 |
| SABER / τ-Bench Verified | "31 out of 50 and 53 out of 115 instructions, respectively, lacked sufficient detail [...] Such ambiguities increase benchmark variance and weaken its reliability as a diagnostic tool." "To reduce the variance present in τ-Bench, we report the average score over three runs." Simulator: claude-sonnet-4. | Names variance from underspecification; does not measure or split it. | arXiv:2512.07850, 2025-11-26 |
| One Frozen Simulator Is Not Enough (Yu … Levine, Manning, Shi) | Writes the exact decomposition as Eq. 6: "Let ξπ be agent-side randomness, ξU simulator-side randomness, and Rx = R(x, ξπ, ξU). The law of total variance gives Var[Rx \| x] = Eξπ[VarξU(Rx \| x, ξπ)] + Varξπ[EξU(Rx \| x, ξπ)]", labelled "simulator-side contrast" and "agent-side contrast". Then: "A cleaner diagnostic would separate simulator-side from agent-side variance via Eq. 6; only the simulator-side term tracks ϵϕ." Measures a proxy instead: the "zero-variance batch fraction, which climbs from 60% to over 85% during single-simulator training" (τ²-bench retail, rollout temperature 0.7, GPT-5-mini simulator). | The decomposition is defined and motivated, not measured. This is the paper that occupies the definition. | arXiv:2608.12253, 2026-08-12 |
| UserProxyBench | Varies the simulator *model* (7 proxies, temperature 1.0, one rollout per task) with a frozen GPT-5.5 agent on 375 τ²-bench tasks: "changes mean task reward by 15.2 points". Limitation: "Repeated rollouts on Telecom, a second frozen agent, and a small RL experiment [...] would separately test stochasticity, interaction-partner dependence, and downstream training effects." | Between-simulator effect only; no within-simulator variance. | arXiv:2609.38043, 2026-09-29 |
| Lost in Simulation (Seshadri … Goldfarb-Tarrant) | Difficulty labels from "running the benchmark 5 times using GPT-4o as both the agent and user LLMs". Table 5, "Error Attribution (%) for simulated vs. human user conversations with reward = 0, manually annotated by the authors (n = 45 per condition)": simulated — Agent 48.9, User 40.0, Both 2.2, Other 8.9; human — Agent 24.5, User 62.2. Abstract: success "varying up to 9 percentage points across different user LLMs". Design: "we focus on a single, fixed agent (GPT-4o). Holding the agent constant enables us to isolate the effects of user simulation". | Attribution is by annotation, not variance; no seeds. | arXiv:2601.17087, 2026-01-23 |
| Mind the Sim2Real Gap (Zhou … Sap; COLM 2026) | 31 simulators vs 451 people on 165 τ-bench tasks. Reward arm: "70.6% of reward=0 interactions are actually judged as successful by human users, while 33% of reward=1 interactions are judged as unsuccessful or only partially successful." Human study "includes three conversations per task". | No within-simulator variance; binary-reward critique is about bias against human judgment, not trial-to-trial flips. | arXiv:2603.11245, v1 2026-03-11 |
| Agent Evaluation Reliability (… Koyejo) | Bayesian variance decomposition over task × model × scaffold facets on HAL data incl. τ-bench Airline. "Because repeated observations of the same (i, m, a) cell are rare, the task–model–scaffold interaction is not separately identifiable from latent response variation". | No simulator facet; no repeated trials. | arXiv:2610.00651, 2026-09-30 |
| Deployment Decision Reliability (Srinivasan) | Four-facet G-theory (agent, task, step, error category) on τ²-bench traces ("three frontier agents [...] running 4 trials per task across 50 tasks per domain"), TheAgentCompany, AppWorld: "the agent main effect accounts for less than 3% of total variance [...] while the agent-by-task interaction accounts for 7-23%." Frames pass^k: "In G-theory terms passk is a single-facet (trial) design". | Trials fold into the residual; the simulator is not a facet. | arXiv:2608.11323, 2026-08-11 |
| Stochasticity in Agentic Evaluations (McCann) | "ICC decomposes observed variance into between-query variance (task difficulty) and within-query variance (agent inconsistency)" on GAIA and FRAMES. | No simulated user. | arXiv:2512.06710, 2025-12-07 |
| Luck Is Not Skill (Sakib) | "paired rollouts, which share an event-keyed noise schedule within each group while preserving each rollout's marginal distribution"; the luck-share estimator λ (one-way random effects) on a tool-fault environment. | Not a simulated user; the schedule must be keyed by *event*, not by call index — the fact that breaks the seed design below. | arXiv:2609.24144, 2026-09-21 |

**Kill conditions from the brief.** (a) "A τ-family paper already reports the decomposition": not met — none reports
agent-versus-simulator variance shares; the closest are τ²-bench's annotated critical-error rates (6–13%) and
the τ³ audit's "primarily reduced variance across trials". (b) "The expected result ('mostly the agent') is
already published for a comparable benchmark": met on the annotation route, with a contradiction — τ-bench's
own audit gives 36 of 40 failures (90%) to the agent; Lost in Simulation's Table 5 gives 48.9% agent / 40.0%
user on the same benchmark, same agent family (GPT-4o), different simulator and protocol; τ²-bench's critical
rates give 6–13% of conversations to the simulator. Not published on any benchmark on the variance route.
(c) "One user, no second benchmark": not met (Section 4, persona 2 lists twelve benchmarks with an LLM user).
The shape is not killed by (a)–(c); it is parked on the definition check (Section 3).

## 2. Data-availability check (systems reviewer)

| Public log source | Fields present | Fields the tool needs and does not find |
|---|---|---|
| tau2-bench leaderboard submissions (trajectory files; guide fetched 2026-10-10) | Per-trial outcomes (≥4 trials per domain preferred), agent model, user model ("this choice will be reported on the leaderboard"), identical `--user-llm` args across runs | Simulator seed (none; API simulators gpt-5.2 / gpt-4.1 cannot be seeded or made deterministic), simulator temperature (not stated), graded reward (binary only) |
| τ²-bench paper traces used by DDR (arXiv:2608.11323) | 3 agents × 4 trials × 50 tasks per domain, five check types (db_check, action_checks, env_assertions, communicate_checks, nl_assertions) | Same as above; trials are exchangeable, so the simulator is unidentifiable as a facet |
| HAL reliability tracker (pressure records B25/B55, fetched 2026-10-09) | Multi-run outcomes on a "Curated 26-task subset of the airline domain" | No simulator seeds; simulator is an API model |
| UserProxyBench (arXiv:2609.38043) | 2,618 graded trajectories, 7 proxies, rubric scores (a graded arm) | "one rollout per task": no within-simulator repeats |

Consequence: on the logs as they exist, nothing in the tool's three shares can be computed. Every arm requires
re-running the benchmark with a self-hosted simulator, which is a different simulator than the leaderboard's
(UserProxyBench: proxy choice moves reward 15.2 points), so the tool's output describes a configuration no
leaderboard row uses. Maintenance: the τ family shipped τ² (Jun 2025), the task audit (Feb 2026), τ-Knowledge
and τ-Voice (Mar 2026), ττ and τ-Multilingual (Sep 2026) and a grader change (tau2-bench 1.0.1, banking); about
four releases a year, each a full re-run of the tool (Section 7 cost each time).

## 3. Definition check (RL reviewer)

**The nested design.** Task i. Agent seed a (fixes the agent's sampling draws). Simulator seed u (fixes the
simulator's draws). Binary outcome R_iau ∈ {0, 1}. Within one task, write R_au for short.

Per-task mean and total variance (p is the task's success probability):

  p = E_{a,u}[R_au],   Var[R] = p(1 − p).

Law of total variance, conditioning on the simulator seed first:

  Var[R] = Var_u( E_a[R | u] ) + E_u( Var_a[R | u] ).

Conditioning on the agent seed first:

  Var[R] = Var_a( E_u[R | a] ) + E_a( Var_u[R | a] ).

The two-way random-effects model that the 8 × 8 seed table estimates:

  R_au = p + α_a + β_u + γ_au,

with σ²_A = Var(α_a) the agent main effect, σ²_U = Var(β_u) the simulator main effect, σ²_AU = Var(γ_au) the
interaction, and Var[R] = σ²_A + σ²_U + σ²_AU. The brief's "simulator-induced share" is σ²_U / Var[R]; the
"agent-induced share" is σ²_A / Var[R]. Because R is a deterministic function of (i, a, u) once both seeds are
fixed, there is no separate residual: the interaction *is* the residual. pass^k and these quantities are linked
per task by

  pass^k_i = E[ R_{a1 u1} ⋯ R_{ak uk} ] = p_i^k  (independent trials),

so pass^k decay, p_i − p_i^k, is a function of p_i alone; the decomposition says *why* p_i is not 0 or 1, not
anything extra about k.

**Why "fix the simulator's responses, resample the agent" is not what a fixed seed does.** A simulator reply at
turn t is a function of the whole conversation so far and of the seed:

  u_t = S(h_t, u),   h_t = (m_1, u_1, …, m_t),

where m_t is the agent's t-th message and S is the simulator with its sampler. Two agent seeds a ≠ a′ produce
different messages at the first turn where their draws differ; from that turn on h_t ≠ h′_t, and S(h_t, u) and
S(h′_t, u) are draws from different distributions with the same random numbers. For a token sampler seeded by a
pseudo-random stream, the same uniforms applied to different next-token distributions give essentially unrelated
tokens after a few steps. So the simulator seed's *main effect* β_u — "how much the outcome moves when only the
simulator seed changes, averaged over agent seeds" — is near zero by construction, however much the simulator
actually drives outcomes: all of the simulator's influence lands in the interaction γ_au, which is attributable to
neither party. The estimator does not fail; it answers a question nobody asked. Luck Is Not Skill needed its
schedule "event-keyed" rather than call-indexed for exactly this reason, and an event key for a conversation is a
semantic coarsening of agent messages (which question was asked), a modeling choice, not a measurement.

The brief's phrase "fix the simulator's *responses*" names the other implementation: replay a reference
conversation's user turns to a fresh agent. That is defined only up to the first turn where the new agent says
something different; afterwards the replayed user is answering questions the agent did not ask, and the outcome
is meaningless. This is the P7 red team's objection RL-3 restated.

**What is identifiable, and what it means.**
1. *Temperature-0 simulator.* If the simulator is a deterministic function of the history (temperature 0 on a
   batch-invariant stack), then u is a constant: Var[R] = Var_a[R], the "simulator share" is 0 by definition, and
   every simulator error becomes a deterministic consequence of the agent's path — bias conditional on the
   prefix, not variance. τ²-bench already runs both sides at temperature 0 and still sees pass^k fall (0.74 → about
   0.53); that residual is serving nondeterminism, which Thinking Machines measured at "80 unique completions"
   in 1,000 temperature-0 samples of one prompt (2025-09-10) and which cannot be attributed to either side
   without a batch-invariant server (their vLLM test: 26 s default versus 42–55 s deterministic).
2. *The temperature contrast.* The difference in pass^k between (agent sampled, simulator deterministic) and
   (agent sampled, simulator at temperature T) is identifiable: it is the marginal effect of simulator sampling at
   T. It is a knob reading, not a property of the benchmark — the P7 red team's RL-1 point, which stands.
3. *Per-turn attribution.* Define the win probability after any prefix, V(h) = E[R | h]. Each move changes it; the
   changes are uncorrelated across turns (a martingale), so

     Var[R] = Σ_t E[ (V(h_t, m_t) − V(h_t))² ] + Σ_t E[ (V(h_t, m_t, u_t) − V(h_t, m_t))² ],

   the first sum over agent moves, the second over user replies. This splits outcome variance by *who moved*,
   needs no replay and no deterministic simulator, and is the standard decomposition in game analysis: Zare
   (2000) on backgammon, "luck is the equity you gain through the roll of the dice" and "The outcome of a match
   or money game equals the net luck plus the net skill difference." The simulator is the dice. Estimating V at
   every prefix needs branching continuations from every turn of every base conversation (a rollout tree); cost in
   Section 7. Its interpretation problem is the professor's (Section 4): a large user-move share is, by τ-bench's
   definition, what pass^k is *supposed* to test, unless the moves are annotated critical errors.

**Reward-threshold arm.** Let g_iau ∈ [0, 1] be a graded score (τ-Knowledge's Action Recall, or a rubric score as
in UserProxyBench) and θ the pass threshold, so

  R = 1[g ≥ θ].

"Threshold-induced decay" means, operationally: among pairs of trials of one task where R flips (one 0, one 1), the
fraction whose graded scores both lie within a band δ of θ — flips that are the threshold reading noise in g rather
than a qualitatively different outcome. The graded analogue of pass^k is the expected worst of k graded trials,
E[min(g_1, …, g_k)]; the arm compares its decay with pass^k's. Identifiable from the same rollouts, requires a
graded scorer the τ family lacks for airline/retail/telecom (τ-Knowledge is the exception), and inherits the
scorer's own noise: Benchmarking the Benchmarks (arXiv:2607.02577, 2026-06-30), which audits τ²-bench among four
families, reports for the LLM-judged LiveMCPBench that "23 repeated evaluations of the same setup produce scores
ranging from 57.9% to 76.8%". The published
binary-reward facts are about bias against humans, not flips: "70.6% of reward=0 interactions are actually
judged as successful by human users" (2603.11245); "24.4% of agent-successful episodes fail UFS" (2609.38043).

**Plain statement.** The three-share decomposition in the brief is not identifiable from a seed design, because a
seed is not a state of the world; the simulator's contribution can be measured only turn by turn, with branching
rollouts, and even then its reading is "how much the user's moves move the win probability", which the
benchmark's authors define as the thing the agent is being tested on. That is a park.

## 4. Five personas

**1. The incumbent (Sierra / the τ-bench authors).** *Objection:* "pass^k was designed around simulator variation
as the stimulus, and we measure the part that is a defect by annotation and fix it at the source." Evidence:
τ-bench: "pass^k can capture the reliability of the agent at handling variations in conversations with the same
underlying semantics" and "the onus is on the agents to handle diverse users"; τ²-bench: critical-error table
(13%/12%/6%) and the telecom remedy ("tightly couples the user simulator to the environment"); τ-Knowledge:
simulator "standardized to GPT-5.2 with low reasoning effort, which we found to exhibit few task-critical
errors"; τ³ audit: fixes "primarily reduced variance across trials". *Answer:* conceded. The incumbent's two
remedies (constrain the simulator with tools; audit the tasks) remove the defect without decomposing it, and the
τ³ post already published the only decomposition-adjacent number a benchmark owner wants: pass^4 rose more than
pass^1 after the audit. What they have *not* done is report any repeated-run variance on the public leaderboard
(one Pass^1 column; "higher Pass^k values may be `null`").

**2. The would-be user (a benchmark owner).** *Objection:* "On how many benchmarks could this run, and would
Sierra or Narasimhan's group run it or have they already?" Benchmarks with an LLM user in the loop, all with public
code (fetched ids): τ-bench (2406.12045), τ²-bench (2506.07982), τ³-Banking / τ-Knowledge (2603.04370), τ-Voice
(2603.13686), τ-Multilingual (2609.35820), ττ-bench (2609.04611, LLM client), UserProxyBench (2609.38043, on
tau2-bench v1.0.0), SimulatorArena and τ²-bench via GAUGE (2609.12191), SEATauBench (2606.28715), AgentWorld
(2608.24076, "pass^k consistency metric"), Persuasion for Good as used by 2608.12253, ConvApparel (2602.16938),
RealWorldShop (2609.38974), PAUSE (2607.27354), ICAE-Bench (2607.21217), CustomerSim (2605.08334). Twelve or
more: the "no second benchmark" kill condition does not fire. Would Sierra run it: their papers' own text says
they verify the simulator by annotation (τ², τ-Knowledge), seed only the non-LLM parts (τ-Voice: "stochasticity
arises from agent and simulator LLMs"), run one or two trials where compute binds (ττ, τ-Multilingual), and
treat remaining variation as the agent's problem. The one variance sentence they wrote is a future-work line in
ττ-bench ("per-task variance across repeated builds is not characterized and would be an interesting addition to
study"), about *agent* builds. Nothing fetched suggests they have run or want an agent-versus-simulator split.
The group most likely to run Eq. 6 is the one that wrote it (Yu, Tomlin, Abdulhai … Levine, Manning, Shi): they
have the τ²-bench RL stack, a self-hosted agent at temperature 0.7, and the proxy they used (zero-variance batch
fraction) is the thing Eq. 6 would replace. *Answer:* the user exists, but the two most natural users either do
not want the number (Sierra) or will produce it themselves (Shi's group). What a benchmark owner would cite is
narrower: a per-turn report that says *which user turns* move outcomes and whether those turns are annotated
simulator errors — the audit-targeting use, which the τ³ post did by hand ("left key information underspecified,
causing the simulated user to behave unpredictably across trials").

**3. The systems reviewer.** *Objection:* "None of the three shares can be computed from any public log, and the
tool's precondition — a seedable, deterministic simulator — does not exist for the simulators the leaderboards
use." Evidence: Section 2; the submission guide names gpt-5.2 as the recommended simulator; Thinking Machines:
"LLM APIs are still not deterministic in practice", and batch-invariant serving costs 1.6–2.1× (26 s → 42–55 s).
Per the brief's throughput assumption (30–60 rollouts per H100-hour for a 32B agent), the parked P7(ii) design of
6,400 episodes costs 107–213 agent H100-hours before the simulator is served, not the brief's "~40" (that figure
holds only at the 7B rate). *Answer:* conceded on computability from logs. The tool is a re-run protocol, not a
re-scorer, and every τ-family release (about four a year) re-triggers it.

**4. The RL reviewer.** *Objection:* "Define the conditioning set. A fixed simulator seed conditions on nothing
once the agent's message differs; the main effect you call the simulator share is the share of a random-number
stream, not of the simulator." Evidence and equations: Section 3; Luck Is Not Skill's event-keyed schedule; P7 red
team RL-1 to RL-3 (checklist item 2026-10-08, "zero mean given what, exactly?"). Second objection: "Which paper
falls out, with what mechanism and method consequence?" The brief's #12 question ("agent, simulator or binary
reward?") has no method consequence either way: if the simulator share is large, the remedy is the incumbent's
(constrain or audit the simulator); if small, pass^k is already the right metric. *Answer:* conceded on the seed
design. Partially answered on the per-turn version: it has a mechanism (which turns carry the variance) and one
consequence (where to point an audit), but no training-time consequence that is not P8's (22 groups).

**5. The professor who dismisses it in ten minutes.** "pass^k was defined as robustness to simulator variation.
Asking what share of the decay is the simulator is asking how much of the stimulus is stimulus. The part that is
a defect — turns that make the task impossible — Narasimhan's group counts by hand at 6–13% and fixes, and the
audit that did so already reported that pass^4 moved more than pass^1. The decomposition you want is Eq. 6 of a
Levine–Manning–Shi paper that calls it the cleaner diagnostic and has the stack to run it. What is left is a
rollout tree on one open model telling us that user turns move the win probability on airline more than on
telecom, which the critical-error table already says." *The sentence that answers it:* no τ-family paper and no
P8 paper reports any within-simulator variance on any benchmark; the three annotation-based attributions
disagree with each other (90% agent; 49% agent / 40% user; 6–13% simulator-critical), and the only paper that
wrote the variance definition did not measure it. *Is it true:* yes on every fetched text. *Is it enough:* no — a
measurement whose two natural owners either reject its framing or are positioned to publish it first, costing
130–280 H100-hours per domain per release, is not a product for one first-year student without lab compute.

## 5. Density (window 2025-10-09 → 2026-10-10; arXiv API, `all`/`abs` fields, max 50, newest first, 3 s pause)

| key | query | total | on the exact question (within-simulator variance share) | adjacent |
|---|---|---|---|---|
| T1 | ti: τ-bench family names | 4 | 0 | τ-bench, ττ-bench |
| T3 | au:Barres AND au:Narasimhan | 5 | 0 | τ², τ-Knowledge, τ-Voice, τ-Multilingual, ττ |
| D1 | "user simulator" AND (fidelity OR consisten* OR variance OR seed) | 58 | 0 | MIMESIS, CUEing, AgentPersonaBench, CustomerSim, RealUserSim, GAUGE, Disclosure-Gated, Back in Style |
| D2 | τ-bench ids AND (pass^k OR variance OR reliability) | 30 | 0 | SABER (variance from underspecification), Lost in Simulation, Benchmarking the Benchmarks (2607.02577), SEATauBench |
| D3 | "simulated user" AND (noise OR stochastic OR luck OR variance OR seed) | 3 | 0 | — |
| D4 | LLM-as-user / user LM AND reliab*/consisten*/variance/fidelity | 13 | 0 | Simulated Customers Never Walk Away, RealUserSim |
| D5 | pass^k AND (simulator OR simulated user) | 15 | 0 | AgentWorld (pass^k + partial credit + personas) |
| D6 | variance decomposition / law of total variance / ICC / G-theory AND agent AND evaluation | 24 | 0 | 2610.00651 (Koyejo), 2608.11323 (DDR), 2512.06710 (ICC), 2609.29709 (CTT for judges) |
| from `pressure-points.md` §4 | F1a/F1b/F1c; P7x4 | 0/3/0; 0 | 0 | — |

Groups counted (by last author / affiliation): on the exact measurement, **0 measured, 1 defined** (Shi / Levine /
Manning, 2608.12253); variance decompositions of agent benchmarks without a simulator facet, **3** (Koyejo;
Srinivasan; McCann); between-simulator main effects, **3** (Goldfarb-Tarrant; Jain/Sarvam; Wei/GAUGE);
annotation-based attribution of failures to the user, **3** (Narasimhan τ/τ²; Barres τ-Knowledge;
Goldfarb-Tarrant). Pre-window precedents the in-window papers cite: τ-bench itself (2024-06, pass^k as a
single-trial-facet design), Miller, *Adding Error Bars to Evals* (arXiv:2411.00640, 2024-11), Madaan et al.,
*Quantifying Variance in Evaluation Benchmarks* (arXiv:2406.10229, 2024-06, "seed variance across
initialisations"), Shi et al., *How to Build User Simulators to Train RL-based Dialog Systems* (arXiv:1909.01388,
2019: "The performance of the simulator directly impacts the RL policy"), Sekulić et al., DAUS (arXiv:2402.13374,
2024-02: hallucinations "a major source of inconsistencies in simulator responses"), and Zare (2000) for the
per-move luck/skill split.

"Why has nobody measured Eq. 6": the enabling piece is a self-hosted, seedable *and* batch-invariant simulator;
batch-invariant kernels for vLLM landed in Sept 2025, and the one group with both the stack and the stated need
wrote the equation eleven months later. That is "an enabling piece landed recently" — a good answer for them, a
timing risk for anyone else.

## 6. Narrowest surviving version

A per-turn attribution report for one user-simulator benchmark: for each conversation, the win-probability change
at every agent move and every user reply (estimated from branching continuations), summed into an agent-move share
and a user-reply share of outcome variance, with the highest-variance user replies passed through τ²-bench's
critical/benign annotation rubric so the user share is split into "legitimate variation" and "simulator error".
It needs no replay and no deterministic simulator, is not published anywhere fetched, and its one use is to tell
a benchmark owner which tasks and turns to audit — the thing the τ³ audit did by hand.

## 7. First measurement and its cost

τ²-bench telecom (50 tasks; critical-error rate 6%, the hardest case for finding a user share), self-hosted
Qwen3-32B agent at temperature 1 and a self-hosted 32B simulator (the benchmark's own user prompt) on a
batch-invariant server. Rollouts: 4 base conversations per task; at each of about 20 move boundaries per
conversation, 2 branched continuations of average half length. Episode-equivalents: 50 × 4 × 20 × 2 × 0.5 = 4,000
plus 200 base = 4,200. Agent side at the brief's 30–60 rollouts per H100-hour: 70–140 H100-hours. Simulator side,
shorter turns but deterministic kernels at 1.6–2.1× (Thinking Machines' numbers): about +60–100%. Total ≈
**130–280 H100-hours, $330–1,100 at $2.5–4 per H100-hour (price is an assumption; the P7 report used ≈ $3.75), no
API cost**, two to three weeks of one student. Annotation of the top-variance user turns with τ²-bench's rubric:
a few hundred LLM calls, under $50. Kill result: user-reply share under 15% of outcome variance with fewer than
half of it on annotated critical errors — expected, given the 6% critical rate and the τ³ audit having already
removed the underspecified instructions on airline and retail. Continue result: user-reply share above 30%
concentrated on annotated errors, which would make the report an audit tool; even then its first customer is a
blog post, not a paper. The brief's nested-seed design (6,400 episodes) is not costed because it is not
identifiable (Section 3); for the record it would be 160–320 H100-hours at the 32B rate, not 40.

## 8. The two closest papers' limitation text, verbatim

- One Frozen Simulator Is Not Enough (arXiv:2608.12253, 2026-08-12), §3.1: "The empirical proxy in Figure 19
  (zero-variance batch fraction) is a one-sided diagnostic of training-signal degeneration, not a direct estimator
  of ϵϕ: small ϵϕ implies small reward variance via Lemma 3.3, but the converse can fail because sparse binary
  rewards or all-failure batches give zero variance too. A cleaner diagnostic would separate simulator-side from
  agent-side variance via Eq. 6; only the simulator-side term tracks ϵϕ."
- UserProxyBench (arXiv:2609.38043, 2026-09-29), Appendix F: "Repeated rollouts on Telecom, a second frozen
  agent, and a small RL experiment comparing policies trained against high- and low-UFS proxies would separately
  test stochasticity, interaction-partner dependence, and downstream training effects." Also §G: "All seven
  reported user proxies use temperature 1.0."
- Supporting (τ family): ττ-bench (arXiv:2609.04611): "per-task variance across repeated builds is not
  characterized and would be an interesting addition to study." τ-Knowledge (arXiv:2603.04370): "the user is
  simulated by an LLM, which could introduce stochasticity and/or instruction-following errors that we must verify
  do not unfairly penalize or reward agents."

## 9. Checklist items triggered

- Estimator — 2026-10-08 "Zero mean given what, exactly?": the conditioning set of a fixed simulator seed is the
  shared prefix only; after divergence nothing is fixed. Decisive here.
- Estimator — positivity/measurability: the simulator share is measurable only where the agent's messages agree
  across seeds (turn 1), i.e. nowhere useful.
- Known confounds — 2026-10-08 deterministic sandboxes / "name the real source of randomness": named (simulator
  sampling), and found to be a temperature knob plus serving nondeterminism.
- Positioning — 2026-10-09 "nobody has done X" must quote the two closest papers' own limitation text: done
  (Section 8); the sentence survives.
- Positioning — 2026-10-09 density queries with failure-mode and operations words: seed / luck / stochastic /
  noise / variance / ICC / G-theory included; counts above.
- Positioning — 2026-10-08 twelve-month window with mechanism words (seed, replay, branch, decomposition): run;
  2608.12253's Eq. 6 and 2608.11323's G-theory would have been missed by the problem's own vocabulary.
- Positioning — "why now": an enabling piece (batch-invariant serving, Sept 2025) exists and is already in the
  hands of the group that defined the quantity.
- 2026-10-09 — premise numbers carry the source's category and denominator: "13 (13%) critical errors of 100
  airline conversations", "4 of 194 annotated trajectories task-critical", "Agent 48.9% of n = 45 reward = 0
  simulated conversations", "80 unique completions of 1,000 at temperature 0".
- 2026-10-09 — first measurement names a runnable benchmark: tau2-bench is public; the deterministic-simulator
  stack is the item to budget.
- 2026-10-09 — judge and critic are different objects: the reward-threshold arm imports judge noise (run-to-run
  spread of LLM graders) into a reliability number; stated as a confound in Section 3.
- Readability — equations with every symbol defined; nested design, law of total variance, martingale, batch
  invariance each glossed in the paragraph that introduces them.

## 10. New checklist lessons (not written to `checklist.md`; for the operator to add)

- A "seed" is not a state of the world. For any design that fixes one party's seed and resamples the other in a
  sequential interaction (simulated user, LLM judge, LLM-backed tool), write down what the seed still fixes after
  the first divergence of the other party's output; if the answer is "nothing", the main-effect variance is
  structurally zero and the design measures a random-number stream. Ask for event-keyed noise or a per-move
  decomposition instead.
- Before proposing to decompose a benchmark's reliability metric, read the metric's definition sentence in the
  original paper: τ-bench defines simulator variation as the stimulus pass^k tests, so a "simulator share" has no
  defect reading without an error annotation.
- Temperature-0 evaluation through an API is not a deterministic arm; cite the serving-nondeterminism numbers
  (80 of 1,000 unique at temperature 0; 1.6–2.1× for batch-invariant kernels) whenever a design assumes it.
- When a competitor paper writes the target quantity as an equation and calls it future work, record the group,
  their stack and the date; the kill search's "why now" must then answer why that group has not done it.
- A product shape whose only computable version is a re-run protocol (not a re-scorer of public logs) must list
  the source benchmarks' release cadence and cost each re-run; "a tool a benchmark owner runs" is not a tool if
  the owner's configuration (an API simulator) cannot run it.
- Annotation-based attributions on the same benchmark can disagree by 4× (90% agent vs 49% agent); when a
  question's "expected result" is quoted from one of them, quote the others.

**VERDICT: parked.** Re-open condition: a published statement of need for the Eq. 6 measurement from a benchmark
owner or from 2608.12253's authors that has not been met by then (check arXiv for "simulator-side variance"
measured on any user-simulator benchmark), plus access to a batch-invariant serving stack. Cost on re-open:
130–280 H100-hours ($330–1,100) for the per-turn version on one τ²-bench domain, two to three weeks; the
nested-seed version is not to be re-opened at any price.
