# Red team — week 2026-W41, top three problems (P7, P6, P14)

Date: 2026-10-09. Inputs: `2026-W41-problem-shortlist.md`, `2026-W41-problem-shortlist-members.jsonl`,
`prompts/checklist.md`. Seven neighbor papers were downloaded from arXiv and read in full text (not from
the shortlist's summaries); ten extra arXiv API density queries were run with mechanism words the
shortlist did not use (window 2025-10-09 to 2026-10-10, max 50, newest first, 3 s pause). Raw XML,
parsed listings and the PDF texts are in the session scratchpad under `redteam/`.

Terms used throughout. **Rollout**: one recorded attempt at a task. **GRPO**: sample several rollouts of
the same task, grade each at the end, push the model toward the ones above the group average.
**Sibling**: another rollout of the same task in the same group. **Prefix**: the first t steps of a
rollout. **Luck share** (defined in §P7): the fraction of reward variance explained by the environment's
own randomness rather than by the policy's sampling. **CRN** (common random numbers): make several
rollouts share one environment random draw so that differences between them are decisions, not luck.
**Snapshot / restore**: save a sandbox's state mid-episode and later resume from it. **Simulated
user**: a language model prompted to play the customer the agent talks to.

Summary of verdicts: **P7 killed** as a direction (class (i) killed, class (ii) parked behind one
40-GPU-hour measurement, class (iii) killed); **P6 killed**; **P14 killed**.

---

## P7 — Environment-side failures charged to the agent

### Neighbors fetched (full text)

**2609.24144 — Luck Is Not Skill (Sakib, BRAC University; single author; 21 Sep 2026).**
Trick: give all eight rollouts in a GRPO group the same environment random draw (which tool calls
fault, which grades flip), keyed by event rather than by call index, so that siblings differ only by
their own decisions; then measure whether this lowers the gradient's variance and speeds learning.
What it occupies: (1) the definition and estimator of the luck share λ (an intraclass correlation from
an 8 schedules × 8 policy-samples table per task, one-way random effects); (2) the proof that pairing
removes the between-schedule part of reward-contrast variance exactly (factor 1−λ) and the
counterexample where pairing *raises* gradient variance (a scalar bandit, Appendix A.1); (3) the
spurious-variance-group analysis for grader flips (at flip rate q = 0.10 and G = 8, 57% of all-correct
groups get a non-zero advantage from noise alone; pairing makes it 0); (4) a pre-registered 2B
training study. Facts that matter for the kill: the fault rate was p = 0.25 *per tool call* ("about
three quarters of the episodes meet at least one fault"), and "the fault mixture was calibrated to
produce appreciable reward luck share"; the first environment version measured λ = 0.03 and was
redesigned twice to reach λ = 0.33–0.38. Even then both pre-registered learning criteria were missed
(H2a: AUC +0.037 with seed 1 negative; H2b under grader flips: +0.003, interval [−0.029, +0.033]); the
final noisy-test gain is +5.1 points. The gradient-probe reductions are 21–30% (grader flips) and
40–63% (tool faults) of the covariance trace: a constant factor below 3× in variance.

**2608.11977 — Retry, Switch, or Abstain? / Bench2Robust (Chen … Jin Lai, Amazon; 12 Aug 2026).**
Trick: wrap τ²-bench and BFCL in an injection layer that corrupts 40% of tool replies with nine
failure types, and give every training episode a known recoverability class (retry works / must switch
tool / impossible), so that "lucky recovery" and "good recovery policy" are separated by construction
rather than by after-the-fact attribution; train Qwen3-4B with DAPO, a curriculum over the classes,
partial credit, and groups of 8 clean + 8 injected rollouts. What it occupies: in-loop separation of
environment fault from agent fault on the τ-bench family; mixed clean/injected groups; the finding that
vanilla GRPO under random injection learns nothing (23.0% vs 23.2% base, Table 16) while their recipe
reaches 45.9%; the finding that correct abstention cannot be rewarded by the task evaluator at all
("impossible tasks cannot satisfy the benchmark evaluator"). Their own caveat: P(clean) = 0.60 "is a
severe stress-test setting, not an estimate of real API failure rates", and the per-episode budget
(B ≤ 5 injections, ≤ 2 consecutive) guarantees solvability outside the impossible class. The user
simulator is Qwen3-235B via Bedrock.

**2603.21972 — STAR (Wu … ; 2026).** Trick: a post-training pipeline on TravelPlanner that sweeps one
design axis at a time; the environmental-stability axis injects a single error string ("Current tool
{name} is not available") at a per-call rate of 0–10% during RL on a 3B model and tests on a clean
environment. What it occupies: the 10%-failure degradation number quoted by the shortlist. Facts that
matter: average 9.2 tool calls per episode (Table 8), so the per-episode probability of meeting at
least one fault is 38% at p = 0.05 and 62% at p = 0.10; the test success is unchanged for p ≤ 0.05 and
drops only at p = 0.10; the error is transient (a retry draws a fresh fate), so every faulted episode
is recoverable by a retry; the authors attribute the drop to exploration starvation ("hinders the agent
from completing successful trajectories during exploration, thereby starving the model of reliable
reward signals"), which is P4, not misattribution.

Also fetched by id for the density count: **2605.27209 NoisyAgent** (Chen … Chua, NUS, 26 May 2026):
trains agents with user-noise and tool-noise injected into rollouts under a curriculum. **2605.11928
When Simulation Lies** (Zhou … Xiyang Hu, 12 May 2026): a 22-perturbation sim-to-real benchmark for
tool use (timeouts, duplicate tool names, hallucinated tools) plus a domain-randomized RL recipe.
**2603.11084** (Buffalo, Pearson, Klein, Mar 2026): the event-keyed CRN construction Luck builds on.

### Extra density searches (window 2025-10-09 → 2026-10-10)

| label | query (mechanism words) | n | on-topic titles |
|---|---|---|---|
| P7x1 | (retry OR retries OR flaky OR "rate limit(s)" OR timeout(s)) AND reward AND agent AND ("reinforcement learning" OR GRPO) | 9 | 2605.11928 When Simulation Lies (Hu); 2608.00335 RMSWeb (salvages failed web-agent rollouts; adjacent) |
| P7x2 | (exogenous OR "stochastic environment(s)" OR "environment stochasticity" OR "stochastic transitions" OR "transition noise") AND (GRPO OR "group relative" OR "policy optimization") AND (LLM OR "language model" OR agent) | 0 | — |
| P7x3 | ("common random numbers" OR "paired rollouts" OR "shared seed" OR "noise schedule" OR luck OR lucky) AND (rollouts OR GRPO OR "reinforcement learning") AND (LLM OR "language model" OR agent) | 16 | 2609.24144 Luck Is Not Skill; 2606.05885 Evidence-Calibrated PO ("lucky actions" = sampling luck, not environment luck; adjacent) |
| P7x4 | ("simulator error(s)" OR "user simulator" OR "simulated user") AND (reward OR "training signal" OR credit) AND (error(s) OR noise OR unreliable OR mistake(s)) AND agent AND "reinforcement learning" | 0 | — |
| (from P6x1) | — | — | 2609.25960 CausalLoss-Fin (Sharma, Sep 2026): attributes a financial agent's losses to decisions versus *infrastructure faults*, exactly P7's attribution framing, on a payment-exception benchmark |

Revised density: the shortlist's "6 groups, 4 training-side" becomes **at least 9 groups, 6
training-side**: Sakib (Luck), Amazon (Bench2Robust), NUS/Chua (NoisyAgent + AgentNoiseBench), Hu
(When Simulation Lies), STAR, Belayer, plus PALADIN and ToolCritic cited by Bench2Robust as training
on failure-injected recovery data, plus CausalLoss-Fin on attribution. The shortlist's sentence
"nobody separates agent error from environment error inside the training loop" is false: Bench2Robust
does it by construction (scenario classes), Luck does it statistically (CRN pairing), and τ²-bench's
own authors did it at evaluation time (the 16%/6% and 40%/12% error / critical-error rates come from a
checker that knows the ground-truth user state).

### Objections by persona

**Systems reviewer.**
1. *Explicit faults are visible, so "indistinguishable from an agent mistake" is false for them.* A
   tool timeout, HTTP 429, "tool not available" (STAR's injected string), a schema error or a sandbox
   exception is printed into the observation the trainer already stores. Bench2Robust reads these
   labels to split groups into 8 clean + 8 injected. The only faults that are indistinguishable are
   silent ones (stale reads, a simulator stating a wrong fact), and those are the P2/P8 judge problem.
2. *On deterministic local sandboxes the default failure mode is a crash, not a zero reward.* Record
   2606.04484: "a single environment failure can crash the entire pipeline, discard all progress since
   the last checkpoint." Belayer exists because the default is restart; it measures 1% of environment
   actions failing and recovers them with warm spares and container snapshots. The damage is wall-clock
   (+48.7% rollout duration), not gradient corruption.
3. *Flaky tests are filtered before training.* CRR record: "a three-rerun consistency filter discards
   ∼7% of the upstream SWE-GYM candidate pool to enforce determinism"; the same record names package
   mirrors and HTTP replay layers as standard practice. So on SWE-Gym-style stacks the environment is
   made deterministic on purpose and the residual is what the filter missed.
4. *Live tools: the field removes the randomness or trains through it; nobody attributes it away.*
   Tongyi DeepResearch (2510.24701) moved to offline/simulated environments because live noise made
   diagnosis impossible; LiteResearcher replaced the web with a local corpus (P11, ≥20 groups). Those who
   stay live train robustness *to* faults (Bench2Robust, NoisyAgent, When Simulation Lies, PALADIN).
   Attributing a fault away would delete the training signal for retry/switch/abstain, which is the
   behavior deployment needs.
5. *Simulated users on the stacks people use are served through APIs* (Qwen3-235B via Bedrock in
   Bench2Robust; GPT-4o in Ambig-SWE; GPT-4-class in τ-bench). Their random seed is not controllable,
   so the CRN fix and the luck-share estimator are unavailable unless the lab self-hosts the simulator.

**RL-theory reviewer.**
1. *The identifiable quantity is already defined, and it is zero in two of the three classes.* Let ω be
   the environment's random draw given the agent's actions (which calls fault, what the sampled
   simulator says), ξ the policy's own sampling, R the reward. Luck defines

   σ²_env = Var_ω E_ξ[R | ω],  σ²_pol = E_ω Var_ξ[R | ω],

   λ = σ²_env / (σ²_env + σ²_pol).

   In a deterministic sandbox ω is a constant, so σ²_env = 0 and λ = 0 (checklist item 2026-10-08:
   nothing is random after the action). With a simulated user run at temperature 0, ω is again a
   constant: every simulator error is then a deterministic function of the agent's prefix, i.e. bias,
   not luck. λ > 0 only when the simulator is sampled or the tool is live. So λ on τ-bench is a
   *knob* (the simulator temperature), not a property of the problem.
2. *"Attribution" is not well-posed when the error is systematic.* If the simulator errs whenever the
   agent phrases a question a certain way, a different agent action avoids the error; the policy
   gradient already credits that. Deciding that the simulator, not the agent, is "to blame" is a
   fidelity judgment about the simulator (P8, 22 groups), not a statistical quantity.
3. *The shortlist's proposed measurement reduces to Luck's diagnostic.* "Re-run the identical action
   prefix and log disagreement" is defined only up to the first fault; after it, the agent's next action
   depends on what it observed, so the re-run is a fresh policy sample — a GRPO sibling. Shared versus
   independent schedules across siblings is precisely the 8 × 8 table in Luck §5.2.
4. *The ceiling is a constant factor and small at realistic rates.* With λ = 0.35 (at 75% of episodes
   faulted), the best case for reward contrasts is 1/(1−λ) ≈ 1.5× fewer rollouts; the measured gradient
   covariance fell by 40–63% (≈ 1.7–2.7×), and learning gains were +5 points with one of three seeds
   negative. At the τ²-bench critical-error rates (6% telecom, 12% retail) the effect is a fraction of
   that. Lesson (c) applies: constant-factor variance reduction, low ceiling.
5. *Dose.* Any fix that drops or masks faulted episodes changes the effective sample size; a comparison
   against flat GRPO then measures dose, not attribution (checklist: dose-matched).
6. *Privileged information.* A fault label produced by a checker that sees the ground-truth user state
   is privileged; if it enters a weight rather than a pure mask, the expected update changes.

**Professor (ten minutes).** "Your motivating number is a 10% per-call injection on a 3B model where
the same paper shows nothing happens at 5% per call, which already faults 38% of episodes. The one
paper that built an environment to make luck matter needed three redesigns to get λ above 0.03 and then
missed its own pre-registered criteria. Amazon has a 12-author team with 8×H100 and the τ²-bench
simulator on Bedrock training exactly this; NUS and Hu's group train under injected noise; Narasimhan's
own τ²-bench already measured simulator critical errors with a checker. Who will have done it by the
time you finish: all of them, plus whoever integrates Luck's pairing into verl, which is a seeding
change. The question that collapses it: *show me one training log from a standard environment where
the environment caused more than 2% of the zero rewards and the fault was not printed in the
observation.* Workshop paper at best; on the numbers in hand, a negative result."

### Checklist items triggered

- Estimator — "Zero mean given what, exactly?" (2026-10-08): the conditioning set for any luck
  baseline is (task, action prefix); in classes (i) and temperature-0 (ii) nothing is random after it.
- Estimator — positivity/measurability: the fraction of episodes with a decisive environment fault is
  unmeasured on every standard training environment; the estimator (λ) needs a seedable environment.
- Estimator — privileged information: checker-derived fault labels entering a loss weight.
- Comparisons — dose-matched: masking faulted episodes changes dose.
- Positioning — 12-month mechanism-word kill search: run (above); four more groups found.
- Positioning — "why now": the enabling piece is event-keyed CRN (Mar 2026) and it is already used
  (Sep 2026); nothing is left to be first at.
- Known confounds — deterministic sandboxes (2026-10-08): class (i) has no luck; the claim must name a
  real source, and the only real sources (flaky tests, crashes) are filtered or recovered.

### Kill fact (shortlist: "under about 2% of episodes after trivial retries → nuisance")

Checkable cheaply, and the evidence already in hand decides two of three classes.
- Class (i) SWE-Gym-style sandboxes: Belayer's 1% action-failure rate (recovered, not charged) and
  CRR's 7% flaky-task filter put the post-filter, post-retry environment-attributable zero rate well
  under 2%. **Met: killed.**
- Class (ii) simulated users: τ²-bench's critical-error rates (6% telecom, 12% retail at evaluation,
  GPT-4-class simulator) are above 2%, so the kill fact does not fire by itself. But the number is
  bias-dominated and temperature-dependent (objection RL-1/2), and the fix for bias is the simulator
  (P8). **Not met; the problem folds into P8.**
- Class (iii) live tools: the rate is high and real, and the field's two answers (remove the live
  environment: P11; train through faults: Bench2Robust/NoisyAgent/Hu) are both occupied. **Moot.**

### Verdict: killed as a direction; one parked measurement

- **(i) Deterministic local sandboxes — killed.** No randomness given the action; flaky tests are
  filtered at 7%; crashes restart rather than score zero; explicit errors are in the observation. Any
  residual is an engineering patch to the rollout loop (mask or re-sample on a logged sandbox
  exception), which Belayer-class systems already ship.
- **(ii) LLM-simulated users — parked behind one measurement, expected negative.** The randomness is
  real only at temperature > 0, the τ²-bench group already measures simulator errors with a checker,
  and the published remedy for genuine luck (CRN pairing) is a seeding change with a constant-factor
  ceiling. If the student is in the τ-bench group anyway, the measurement below is a one-week side
  project; it is not a thesis direction.
- **(iii) Live tools and web — killed.** Attribution is the wrong objective in deployment-like
  environments (the agent must learn recovery); robustness training is occupied by three funded groups;
  environment replacement is P11 with ≥ 20 groups.

**First measurement for class (ii).** On τ²-bench telecom and retail with a self-hosted open-weight
simulator (Qwen3-32B or 235B) at the benchmark's default temperature and a frozen agent (Qwen3-32B):
50 tasks × 8 simulator seeds × 8 agent samples per seed per domain = 6,400 episodes; compute λ with
Luck's one-way random-effects estimator; run the τ²-bench simulator-error annotation on every
zero-reward episode and record the fraction whose fault is a simulator critical error *and* whose agent
prefix succeeded under another seed. Cost: about 40 H100-hours (≈ $150 at cloud rates), zero API cost,
one week. Kill: λ < 0.10 or environment-attributable zero rewards < 2% of episodes. Continue: λ > 0.30
with faults that recur across siblings taking different actions — and even then the follow-up is to
apply Luck's pairing to τ²-bench, a workshop note, because the fix is published.

---

## P6 — Sandboxes cannot be rewound mid-episode

### Neighbors fetched (full text)

**2607.14171 — Branching Policy Optimization, BPO (He … Xue Liu, MBZUAI/McGill; 15 Jul 2026).**
Trick: instead of eight independent rollouts per task, run one backbone rollout, snapshot the sandbox
at the highest-entropy steps, fork alternative actions from each snapshot, and compute each step's
advantage against its siblings' returns, which removes the prefix-explained part of the return variance
(Theorem 2: the reduction is Var(V(s_t) | s_0)). What it occupies: fork-based sibling advantages on
WebShop, ALFWorld and SWE-bench Verified; the entropy placement rule; the matched-compute comparison.
Assumption 1 is asserted, not measured: "rest(snap(s)) produces a state with identical transition
distribution to s", justified by naming "Docker overlayfs, CRIU, Python interpreter pickling, browser
session export". **Table 4** is the cost measurement the shortlist asks for, and it is already done:
snapshot 42 ms on WebShop (rollout 11.4 s, 0.6% overhead), 138 ms on ALFWorld via pickling (9.1 s,
2.4%), **1,920 ms on SWE-bench Verified via Docker overlayfs (rollout 182 s, 4.2%)**; wall-clock to match
GRPO 47.6 h vs 74.1 h on SWE-bench. Caveats on the RL claim: all baselines reimplemented by the authors,
Qwen2.5-7B, three seeds.

**2605.22781 — DeltaBox (Dong … Haibo Chen, SJTU + Huawei; v2 8 Jun 2026).** Trick: save only the
difference between consecutive checkpoints — the filesystem through an overlayfs whose layer stack can
be swapped at runtime (checkpoint = insert a fresh writable layer; rollback = switch layers), and
process memory through a frozen forked copy of the agent process kept as a template (restore = fork the
template in 1.86 ms) with an asynchronous CRIU dump as fallback, both hidden inside the LLM's inference
wait. What it occupies: coupled (filesystem, memory) checkpoint/rollback at 10.83 ms / 1.86 ms on
SWE-bench Verified MCTS traces (Django, SymPy, Astropy, Matplotlib, scikit-learn, Xarray, pylint,
requests, pytest) versus E2B's self-hosted incremental path at 524 ms / 900 ms and Firecracker diff at
622 ms / 3.4 s; RL fan-out of N = 64 children at 5.5 ms p50; GPU occupation 95–97% vs E2B 29–36% in a
synchronous loop. Fidelity statements: "the (filesystem, memory) pair at each checkpoint is consistent";
"DeltaBox does not currently support network I/O rollback, which may incur external side effects".
Runs on Firecracker with a *custom guest kernel module* (modified overlayfs on Linux 6.8); no public
code URL in the text.

### Extra density searches

| label | query (mechanism words) | n | on-topic titles |
|---|---|---|---|
| P6x1 | (nondeterminism OR "non-deterministic" OR reproducibility OR determinism OR deterministic) AND (sandbox(es) OR container(s)) AND agent AND (LLM OR "language model") AND ("reinforcement learning" OR rollout(s) OR restore OR replay) | 33 | 2607.14171 BPO; the rest off-topic (verification harnesses, security) |
| P6x2 | ("tree search" OR MCTS OR backtrack(ing) OR "best-of-n" OR speculative) AND (sandbox OR container OR filesystem OR "virtual machine" OR microVM) AND agent(s) AND (snapshot OR checkpoint OR restore OR fork OR clone) | 4 | 2605.22781 DeltaBox; 2605.17320 TClone (UCSD); 2608.00881 AOSpec (Fan; speculative action/observation execution for serving, needs forkable state) |
| P6x3 | ("side effects" OR idempotent OR idempotency OR transactional OR transaction OR undo OR "external state") AND agent AND (tool(s) OR environment OR sandbox) AND (LLM OR "language model") AND (rollback OR restore OR revert OR recovery OR "roll back") | 23 | 2609.35366 Planarian (Imperial; statepoints spanning local and remote-service state); 2606.17573 Cordon (Tsinghua, Zhai; semantic transactions for tool calls); 2602.14849 Atomix (MPI-SWS, Bindschaedler; transactional tool use with settlement); 2603.20625 ACRFence (Quinn; retried calls after restore are re-synthesized differently — "semantic rollback attacks"); 2608.14635 Belayer; 2604.28138 Crab; 2512.12806 Fault-Tolerant Sandboxing (Yan) |

Revised density: the shortlist's 8 mechanism-builders become **at least 12** (adding Cordon, Atomix,
ACRFence, AOSpec), i.e. ≥ 16 groups in all. The fidelity half the shortlist calls unmeasured — state that
leaves the sandbox — is the stated subject of Planarian, Cordon, Atomix and ACRFence, all in the last
eight months.

### Objections by persona

**Systems reviewer.**
1. *The cost half is already engineered away on the standard SWE training environment, twice.* BPO's
   Table 4: plain Docker overlayfs snapshots cost 4.2% of rollout time on SWE-bench Verified. DeltaBox:
   10.83 ms checkpoint, 1.86 ms restore, including process memory, on SWE-bench Verified traces. The
   remaining slow path is a product (E2B: "approximately 4 seconds per 1 GiB of RAM" to pause,
   "approximately 1 second" to resume, no fork, per its own docs fetched today), not a research gap.
2. *Which state is outside the sandbox on the standard environments is already known without a
   measurement.* SWE-Gym containers run without network during RL by construction (package mirrors and
   HTTP replay layers, CRR record), so no step's effect leaves the container. AppWorld is a local Python
   simulation with on-disk databases: a file copy is a faithful snapshot. WebArena's world state lives in
   separate self-hosted web-app containers: a browser-sandbox snapshot is not a world snapshot, and the
   benchmark's own reset is a container restart — which is precisely the coordinated local-plus-remote
   statepoint Planarian builds and the GUI fork TClone builds. The shortlist's "fraction of steps whose
   effects leave the sandbox" census has a known answer per environment (≈ 0%, ≈ 0%, most state-changing
   steps) and is a paragraph, not a paper.
3. *Fidelity of filesystem-plus-process restore is a test, not a question.* A deterministic sandbox
   either reproduces the same observations after replaying the same commands from the restored state or
   it does not; DeltaBox reports the coupled pair consistent and names the one exclusion (network I/O);
   Belayer names its exclusions (external services, bind mounts, host daemons, live connections).
4. *Integration is the gap, and it is a pull request.* verl, SkyRL and the OpenHands runtime start one
   container per rollout from an image; adding `snap`/`rest` calls (BPO did it with overlayfs in their own
   code) is engineering. DeltaBox needs a custom guest kernel, which is why it is not in verl; that is a
   deployment choice, not an open problem.

**RL-theory reviewer.**
1. *"Enabling" rests on the value of what restore enables, and that value is the student's own
   filled-in territory.* Fork-based credit (BPO, CRR, EPIG-Tree, HDL) delivers Var(V(s_t) | s_0) of
   variance reduction — a constant factor (lesson c). The one dose-matched audit in the harvest
   (2608.19760) finds no credit rule beats the untrained policy at matched dose. If fork-based methods do
   not reliably beat flat GRPO at matched dose, faster forking is not enabling.
2. *Free prefix sharing already exists without restore.* GRPO siblings of one task share s_0; RTMC
   (2604.11037) hashes step signatures to find shared states across siblings for free early in the
   trajectory (checklist: "free branching from GRPO-group overlap"). Restore adds branching deeper in the
   episode, where BPO's own Figure 3 shows the reduction shrinking as the policy improves (0.42 → 0.58).
3. *Reset curricula (SCOUT) and crash recovery are the only genuinely enabling uses, and both are taken*
   (SCOUT on text environments; Belayer for recovery on SWE containers).

**Professor.** "SJTU/Huawei, HKUST, UCSD, Imperial, Tsinghua, MPI-SWS and a Berkeley-adjacent group
have each shipped a checkpoint/rollback system for agents in the last ten months; BPO measured that
plain overlayfs already costs 4%. What is left is wiring one of them into verl. The question that
collapses it: *name one training result that needs mid-episode restore and that you cannot get from the
GRPO group's shared prefix or from a two-second overlayfs snapshot.* If the answer is 'tree search over
coding agents', DeltaBox already ran MCTS on SWE-bench with 1–2% state-management overhead."

### Checklist items triggered

- Positioning — systems contribution separated from the algorithmic claim: the systems part is done
  by ≥ 12 groups; the algorithmic part (fork-based credit) is constant-factor and contested at matched
  dose.
- Positioning — "why now": overlayfs and CRIU are a decade old; the new primitive (runtime layer
  switching) is DeltaBox's and is published; a newcomer has no enabling piece.
- Positioning — does the idea survive if placement is second-order to the advantage form: the
  infrastructure's value is conditional on fork placement mattering, which the student's month found
  second-order.
- Comparisons — compute-matched: BPO Table 4 and DeltaBox Fig. 6 already are the compute comparison.
- Known confounds — free branching from GRPO-group overlap (RTMC).
- Positioning — 12-month mechanism-word kill search: run; four more systems groups found.

### Kill fact (shortlist: "if DeltaBox, Crab and TClone restore faithfully at millisecond cost on the standard RL training environments, what remains is the scheduler")

Met on the evidence fetched: DeltaBox's measurements *are* on SWE-bench Verified traces (the standard
SWE RL environment family) at 10.83 ms / 1.86 ms with the (filesystem, memory) pair stated consistent;
BPO's plain-overlayfs cost is 4.2% on the same environment; TClone covers live GUI environments;
Planarian covers remote-service state. The scheduler for tree-shaped rollouts is BPO's named future work
("asynchronous tree-distributed training") and a systems-group item.

### Verdict: killed

The infrastructure fact is true only of the default runtimes (E2B, OpenHands, one-container-per-rollout
in verl/SkyRL) and false as a research frontier: at least twelve groups have built the mechanism, two of
them measured on SWE-bench itself at millisecond-to-2-second cost, and the fidelity exclusions (network,
remote services) are the declared subject of four more. The RL-side payoff is a constant-factor variance
reduction whose value at matched dose is disputed. Nothing here is a first-year thesis; the cheapest
confirmation (one day, $0) is to snapshot a SWE-Gym container with overlayfs after 20 agent steps,
restore, replay the next 10 commands from the log on both copies, and diff: identical filesystems and a
lost shell cwd/environment that the scaffold re-establishes anyway, which is the expected result.

---

## P14 — Pass/fail rewards cannot see communication

### Neighbors fetched (full text)

**2502.13069 — Ambig-SWE (Vijayvargiya, Zhou, Yerukola, Sap, Neubig, CMU; ICLR 2026).** Trick: rewrite
each SWE-bench Verified issue with GPT-4o to strip details, hand the full issue to a GPT-4o user proxy
that answers only from it, and measure resolve rate in three settings (Hidden 22%-class, Interaction,
Full) plus whether the agent asks only when the issue is actually underspecified. What it occupies: the
measurement protocol for "did asking help" with a paired complete specification; detection accuracy
(Table 2: Claude Sonnet 4 with strong encouragement 0.89 accuracy, 0.03 false-positive, 0.18
false-negative; Claude Sonnet 3.5 with moderate encouragement 0.84 / 0.24 / 0.09; Qwen3-Coder never asks);
the finding that interaction recovers up to 89% of full-information performance; and the explicit
statement that real underspecified issues cannot be used "because they lack the paired ground truth
(complete specifications) necessary for causal measurement".

**2604.14624 — CLARITI (Vijayvargiya, Viswanathan, Neubig, CMU; 16 Apr 2026).** Trick: train a separate
8B question-asking module with GRPO on four rubric rewards graded by a 32B judge — questions not already
answered in the issue, not generic, answerable from the full issue, and weighted by a Shapley estimate
of which information category predicts task success — instead of rewarding by running the coding agent,
which the authors call "computationally intractable" at their budget. What it occupies: reward design for
clarification without downstream execution; the six-category taxonomy of missing information (error
information 65%, implementation details 37%, …); the result that CLARITI matches GPT-5's resolve rate
(36.8% vs 35.6%, full-issue 41.6%) with 3.0 questions instead of 5.1; the finding that more questions
plateau while answerability falls. Single-turn; synthetic removals; GPT-5 user proxy.

### Extra density searches

| label | query (mechanism words) | n | on-topic titles |
|---|---|---|---|
| P14x1 | ("when to ask" OR "ask questions" OR "asking questions" OR "question-asking" OR "information gathering" OR "information seeking" OR proactive) AND agent(s) AND ("reinforcement learning" OR GRPO OR PPO OR "policy optimization") AND (user OR human) AND (clarification OR clarify OR clarifying OR ambiguous OR underspecified) | 5 | 2602.03468 IntentRL (Ying Shen; RL-trained proactive clarification for deep-research agents); 2512.13159 SpeakRL (adjacent) |
| P14x2 | ("contradictory requirements" OR "conflicting requirements" OR "specification holes" OR "missing requirements" OR "requirements elicitation" OR "incomplete specification(s)" OR "inconsistent requirements") AND (agent(s) OR LLM OR "language model") | 57 (50 shown) | 2604.09408 HiL-Bench (Bing Liu, 12 authors: "benchmarks … solely reward execution correctness, so an agent that makes a lucky guess …" — P14's sentence, April 2026); 2607.00711 ClarifyCodeBench (Ge Li); 2603.00187 ClarEval (Yi Chang); 2609.36789 GitHarness (requirement completion/shift during long tasks); 2601.13295 CooperBench (Diyi Yang); 2608.16618 The Specification Paradox (position) |
| P14x3 | ("developer-agent" OR "real conversations" OR "interaction logs" OR "session logs" OR "chat logs" OR "in the wild" …) AND (coding OR "software engineering" OR programming OR code) AND (agent OR assistant) AND (dataset OR corpus OR benchmark) AND (user OR developer(s)) | 50 shown | **2604.20779 SWE-chat (Baumann … Koyejo, Stanford): "almost 18,000 sessions, more than 229,000 user prompts and 2 million agent tool calls" of real coding-agent use by open-source developers**; 2608.29204 AgentLogs (Wessel; full step logs of GitHub's Copilot cloud agent); 2604.01527 REAP (Satish Chandra; curates benchmarks from interactive production usage); 2605.26440 Conv-to-Bench (turns real user–assistant code dialogues into requirement checklists); 2606.03889 RealClawBench; 2603.09701 interaction smells in multi-turn collaborative coding; 2510.09801 Neubig, how to assess human-agent interactions; 2609.04611 τᵗ-bench |

Revised density: the shortlist's 20 groups become **at least 27**, and the "one entrant" on real
conversations becomes at least five (SWE-chat, AgentLogs, REAP, Conv-to-Bench, RealClawBench).

### Objections by persona

**Systems reviewer.**
1. *"Rewarding a clarifying question by running the downstream task is intractable" is a budget
   statement, not a fact about the recipe.* CLARITI's reason is 30 steps × thousands of tokens per
   candidate question set. With G = 8 question sets per issue that is eight agent runs per issue per
   step — the ordinary cost of agentic GRPO, which every lab in the harvest pays. Training against a
   simulated user in the loop is what 2601.22607 and Bench2Robust already do on τ-bench.
2. *The blocking artifact exists.* The shortlist and 2608.12355 say real developer–agent conversations
   are unavailable; SWE-chat (April 2026) released ~18,000 real sessions, AgentLogs released Copilot
   cloud-agent step logs, REAP curates benchmarks from production usage. Whoever measures natural
   specification holes on them first has a six-month head start, and the data owners are the natural
   authors.

**RL-theory reviewer.**
1. *The premise is false once a user is in the loop.* "Rewards record only whether the final task
   passed, so they cannot see whether the agent asked" holds for SWE-bench, which has no user by design.
   In Ambig-SWE's Interaction setting the pass bit is a function of asking (Hidden 22.4% → Interaction
   36.8% → Full 41.6% in CLARITI's numbers; up to 74% relative gain in Ambig-SWE), because the needed
   information exists only in the simulated user. What pass/fail cannot see is *unnecessary* asking, and
   that is a question-count cost term (CLARITI reports it; "Pareto-Dominant Clarification" in the
   shortlist's own list budgets it with PPO-Lagrangian).
2. *The proposed artifact is not identifiable on real data.* A "paired complete specification" for a
   real ticket does not exist because the reporter does not hold it either (Ambig-SWE §2.1 says this is
   why they used synthetic removals). On real conversations the measurable quantity is "did the user's
   later message change the agent's output" — behavior-changing questions — which is CONTRA's (2610.01769)
   stated object.
3. *Contradictory requirements are a labeling problem before they are a reward problem.* Whether a
   spec "has a hole" is a judgment; τᵗ-bench (the target group's own paper) names it and supplies the
   benchmark. A reward for noticing holes is an LLM-judge reward (P2's proxy-grader problem, 17 groups).
4. *The production default already does most of it.* Ambig-SWE Table 2: a 2025 model prompted to ask
   detects 82% of synthetic holes at a 3% false-positive rate; another detects 91% at 24% false positives.
   Any training claim must beat "add one sentence to the system prompt" at matched false-positive rate.

**Professor.** "Twenty-seven groups, two of them the lab you want to join (τ²-bench, τᵗ-bench) and one
at CMU that has already published both the measurement (ICLR 2026) and the trained module (April 2026)
on exactly this benchmark family. The real-conversation corpus you call missing was released by Stanford
in April with 18,000 sessions. The question that collapses it: *what does your reward see that
Ambig-SWE's Interaction setting plus a question-count penalty does not?* If the answer is 'real holes
instead of synthetic ones', you are proposing a labeling study on someone else's dataset."

### Checklist items triggered

- Estimator — privileged information: the full issue enters the user proxy and CLARITI's answerability
  reward; on real tickets no such object exists, so the measurement is not identifiable there.
- Comparisons — production default in the table: prompted asking (Sonnet 4, 0.89 accuracy) is the
  incumbent; false-positive rate must be matched.
- Positioning — neighbors from conference exports: Ambig-SWE is an ICLR 2026 paper; HiL-Bench, ClarEval,
  ClarifyCodeBench are 2026 benchmarks with the same statement.
- Positioning — "why now": the enabling piece for a real-data study is SWE-chat (Apr 2026), public, and
  its owners are positioned to use it first; no enabling piece is the student's.
- Positioning — 12-month mechanism-word kill search: run; seven more groups found.

### Kill fact (shortlist: "if frontier agents, simply prompted, detect and raise about 90% of real-ticket holes, the gap is a default setting")

Checkable for about $200 of API calls and two days of labeling: take 200 SWE-chat sessions in which the
user's second message supplies information absent from the first, label whether the first message had a
hole, run Claude Sonnet 4 with Ambig-SWE's strong-encouragement prompt on the first message, and count
detections. On synthetic holes the published number is 82–91%. Natural holes are subtler (Ambig-SWE's
own distributional analysis: natural underspecified issues carry more concrete details), so the expected
detection is lower than 90% and the kill fact as written does not fire. The problem dies on density and
on the false premise instead, not on this fact.

### Verdict: killed

The recipe failure the records name is false as soon as a simulated user holds the missing information
(the pass bit then sees asking); the remaining blind spot, unnecessary asking, is a cost term already in
two published rewards; the "missing" real-conversation corpus has at least five entrants since April; the
specific gap (contradictory requirements, real holes) is the target lab's own τᵗ-bench and CMU's
Ambig-SWE/CLARITI line; and the detection incumbent is a system-prompt sentence at 82–91% recall. For a
student entering Narasimhan's group this is a problem to *join* through τᵗ-bench, not a candidate to
propose. No first artifact is assigned; the $200 measurement above is a two-day exercise whose result
does not change the verdict.

---

## Cross-cutting notes for the pipeline

1. The shortlist's density counts were low by 50% (P7: 6 → ≥ 9), 33% (P6: 12 → ≥ 16) and 35% (P14:
   20 → ≥ 27) because its queries used the problem's own vocabulary. Mechanism words that found the
   misses: *retry/timeout/rate limit*, *luck/paired*, *idempotent/transactional/undo*, *in the wild /
   session logs*. Add these to the density-query template.
2. The shortlist's "nobody has done X" sentences (P7: in-loop separation of agent and environment error;
   P6: nobody measured snapshot cost; P14: no real conversation corpus) were each contradicted by a paper
   already cited in the same section (Bench2Robust; BPO Table 4) or by a public dataset six months old
   (SWE-chat). Rule for next week: a "nobody has" claim must cite the two closest papers' limitation
   sections saying so, not the absence of a hit.
3. For this student's stated attraction to P7 ("luck is real"): the luck share λ is a property of the
   *sampling temperature of the simulator and the liveness of the tool*, not of the problem; in the
   deterministic sandboxes he trained on for a month it is identically zero, and in the one controlled
   study that made it large (0.33–0.38) the pre-registered learning gains were missed.
