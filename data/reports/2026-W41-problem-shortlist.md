# Problem shortlist — week 2026-W41

Synthesis of 419 complaint records (groupA 146, groupB 156, groupC 117; 72 papers) harvested from
frontier agentic-RL papers' limitation sections. Clustered into 14 problems; 286 records clustered, 133
left out (limitations-only statements and clusters of three papers or fewer; listed in Section 3).
Density was measured on the arXiv API over 2025-10-09 to 2026-10-10 (Section 4 lists every query).
Full membership with verbatim quotes: `2026-W41-problem-shortlist-members.jsonl` (same folder; one line
per record, field `problem` = P1..P14 or `unclustered`).

Terms used below. **Rollout**: one recorded attempt by the agent at a task. **GRPO** (Group Relative
Policy Optimization): today's standard recipe; sample several rollouts for the same task, grade each at
the end, push the model toward the rollouts that scored above the group's average. **Critic** (value
model): a second learned model that predicts how well a partial attempt will end; PPO uses one, GRPO
does not. **Sandbox**: the isolated container or virtual machine in which an agent's commands run.
**Simulated user**: a language model prompted to play the customer or developer the agent talks to.
**Staleness**: training on rollouts produced by an older version of the model. **τ-bench family**: the
customer-service benchmarks (τ-bench, τ²-bench and their extensions) tied to Karthik Narasimhan's group;
flagged "τ" below. **Systems paper**: a group C paper (infrastructure for agent RL); flagged "sys".

Ranking rule, applied in order: enabling ceiling first, then recipe failure, then industry cost, then
LOW lab density (fewer groups is better), then alignment (τ before sys, because the reader is seeking
to join that group).

## Section 1 — Ranked table

Density = distinct groups found in the 12-month window whose title/abstract is clearly about the
problem (counted by last author / known affiliation; first author when unsure). "Papers" = complaint
papers in this harvest that raise the problem.

| # | id | Problem (one sentence) | Papers | T1 recipe fails | T2 industry pays | T3 ceiling | Density (groups, 12 mo) | Alignment |
|---|----|------------------------|--------|-----------------|------------------|------------|-------------------------|-----------|
| 1 | P7 | When a tool, simulated user or sandbox fails during a rollout, the failure is indistinguishable from an agent mistake and is charged to the agent as zero reward; a 10% tool-failure rate alone degrades the learned policy. | 9 | yes | yes (teams training against real APIs, flaky tests, simulated users) | enabling in high-failure environments; constant-factor when failures are rare | **6** (4 training-side, 2 evaluation-only) | τ: 2506.07982; sys: 2603.21972, 2606.04484, 2608.14635 |
| 2 | P6 | No mainstream agent sandbox can be saved and restored mid-episode fast enough or faithfully enough, so anything that forks, rewinds or resets a rollout (step counterfactuals, reset curricula, tree search, crash recovery) is confined to toy text environments. | 11 | yes | yes (sandbox providers such as E2B; hosted agent platforms; labs training SWE agents) | enabling | **12** (8 build the mechanism, 4 use it in RL) | sys: 2602.03419, 2602.11767, 2604.28138, 2605.22781, 2608.14635 |
| 3 | P5 | RL on multi-turn agents collapses (reward suddenly drops, outputs degenerate, solved tasks regress) as episodes or training runs get longer, and the usual knobs only delay it with no diagnosis of the cause. | 8 | yes | yes (Meta FAIR self-play SWE; labs shipping RL-trained coding agents) | enabling | **15** | τ: 2605.00347 |
| 4 | P4 | On hard agent tasks most groups of rollouts all pass or all fail so the expensive rollouts teach nothing; finding tasks at the right difficulty costs extra rollouts and the supply runs out; when the policy almost never succeeds every success-based method stalls. | 13 | yes | yes (labs training coding agents: ~30% of rollout compute; dataset curation per model generation) | enabling at the zero-success end; constant-factor for the waste | **17** | sys: 2506.11425 |
| 5 | P14 | Benchmarks and rewards record only whether the final task passed, so they cannot see or reward whether the agent noticed a missing or contradictory requirement and asked about it. | 6 | yes | yes (companies deploying coding agents on vague tickets) | enabling | **20** | τ: 2603.04370, 2603.13686, 2608.12355, 2609.04611 |
| 6 | P11 | Training against real environments (the live web, real APIs, real repositories) is too costly, slow or non-stationary, or impossible when the project will not build, and the offline or learned substitutes have a measurable fidelity gap. | 8 | yes | yes (labs training web agents: $59K–$243K API fees per run; labs discarding unbuildable PRs) | enabling | **≥20** | sys: 2506.11425, 2602.03419, 2602.11210, 2603.21972 |
| 7 | P8 | Language models playing the user are systematically unlike people (too cooperative, too patient, single-habit), so agents learn exploits and scores inflate, and there is no way to measure a simulator's fidelity or confirm transfer to real humans. | 12 | yes | yes (teams shipping agents trained against one simulator; anyone reading simulator-based scores) | enabling | **22** | τ: 2506.07982, 2603.04370, 2603.13686, 2608.12355, 2609.04611 |
| 8 | P1 | When a long agent episode gets one grade at the end, nothing in today's recipe says which of the many steps helped or hurt, and getting that answer exactly costs rollouts that multiply with episode length. | 17 | yes | yes (every lab training multi-turn agents with GRPO) | enabling at horizons above ~100 turns; a small critic already crosses that threshold (2605.00347) | **≥28** | sys: 2603.21972 |
| 9 | P2 | Every grader cheaper than a trustworthy final check (a model judging steps, hindsight probability scores, hand-shaped step rewards, a learned verifier) turns out to be no better than noise or gets gamed by the policy it grades. | 19 | yes | yes (teams adopting cheap step signals; labs shipping agents that subvert tests) | unknown (records document only failures of proxies) | 17 | τ: 2606.10156, 2607.21856; sys: 2602.03419, 2602.11767, 2606.04484, 2608.08020 |
| 10 | P12 | Every parallel rollout needs its own live environment that holds host memory and takes seconds to start, so environment count, not GPU count, caps how much experience a cluster can collect. | 6 | yes | yes (micro-VM sandbox fleet operators; labs paying for CPU/RAM per environment) | constant-factor | 14 (industry-dominated: DeepSeek, Kimi, NVIDIA, Microsoft) | sys: all 6 |
| 11 | P13 | Learner GPUs idle 50–81% of each synchronous step waiting for the slowest rollouts, and the asynchronous fix trades idle time for stale data whose heavy-tailed correction weights collapse training. | 9 | yes | yes (every lab training agents synchronously) | constant-factor (≤2x) | ≥35 | sys: 7 of 9 |
| 12 | P9 | One pass of an agent over a benchmark, or one training epoch against a simulated user, costs hundreds to thousands of dollars, so each task gets one to four trials, variance is uncharacterized and models with overlapping error bars cannot be told apart. | 12 | partly | yes ($700–$3,000 per pass; OpenHands Index) | constant-factor | 10 | τ: 2506.06698, 2506.07982, 2606.10156, 2609.04611, 2609.31076 |
| 13 | P10 | Human judgments (preference labels, graded trajectories, expert-written domains, live conversations) cost dollars each and do not scale, and the known ways to stretch few human labels with cheap model labels hit a noise floor set by the human count. | 10 | partly | yes (healthcare, legal, finance annotation at dollars per trajectory) | constant-factor | 11 on agent/LLM evaluation (97 papers in the wider prediction-powered-inference + LLM space) | τ: 2506.07982, 2608.12355 |
| 14 | P3 | A learned value model (critic) as big as the policy doubles the hardware, trains unstably, gets no better with size, and nobody has run the compute-matched test that says whether it is worth having. | 12 | partly | yes (labs choosing between critic and critic-free stacks; 2x GPUs for a critic) | constant-factor (variance reduction), with one documented threshold at 100+ turns | 18 | τ: 2605.00347, 2609.36802 |

Reading the table: the top of the list is not the most-complained-about problem (that is P1/P2) but the
one where the records say the recipe fails, someone pays, fixing it changes feasibility, and fewest
groups are working: environment-side failures charged to the agent (P7, 6 groups), followed by sandbox
save/restore (P6, 12 groups). The τ-bench-aligned problems (P8, P14, P9) are all crowded (20–22
groups for P8 and P14); P7 is the only low-density problem with a τ-bench-family paper in it
(τ²-bench's own simulator error-rate measurement).

## Section 2 — Top 8 problems

### 1. P7 — Environment-side failures are charged to the agent

**Statement.** When a tool, simulated user or sandbox fails during a rollout, the failure is
indistinguishable from an agent mistake and is charged to the agent as zero reward; a 10% tool-failure
rate alone degrades the learned policy. 16 records, 9 papers (2506.07982, 2509.13305, 2510.24701,
2601.22607, 2603.21972, 2606.04484, 2608.14635, 2609.33875, 2610.09484); kinds: reliability 9, infra 3,
signal 3, data 1.

**Quotes.**
- 2603.21972 (STAR, a controlled sweep of RL design choices on TravelPlanner with injected tool
  failures): "when the failure rate reaches 10%, the environmental instability introduces noticeable
  challenges. As illustrated in Figure 6a, this setting causes a clear drop in training stability and
  convergence speed. Consequently, the final test success rate drops significantly, accompanied by
  declines across all metrics."
- 2601.22607 (synthetic tool-use dialogues with program checkers as rewards, GRPO against a fine-tuned
  open-weight user simulator): "As illustrated in Fig. 2, an inadequate user model may ignore its
  instructions and execute erroneous tools, introducing corrupted training signals that incorrectly
  attribute user errors to the agent."
- 2510.24701 (Tongyi DeepResearch, a staged offline-to-live curriculum of environments): "This data
  contamination makes it nearly impossible to diagnose performance issues, obscuring whether a poor
  outcome is caused by a weakness in the agent’s policy or by the instability of the environment itself."
- 2506.07982 (τ²-bench, dual-control telecom domain with a checkable user simulator): "the telecom
  domain’s user simulator shows a 16% error rate with 6% critical errors, compared to 40% error rate with
  12% critical errors in the retail domain from τ -bench"
- 2608.14635 (Belayer, fault tolerance for agentic RL via warm spare workers and selective container
  snapshots): "Naively replaying environment actions from an ambiguous state is unsafe because many
  actions are non-idempotent: re-executing them may duplicate persistent effects or interact with a
  partially updated runtime, while dropping them may lose effects that were already observed"

**Tests.**
1. Recipe failure: yes. GRPO grades the whole rollout from the final state, so a simulator error ("an
   inadequate user model may ignore its instructions and execute erroneous tools", 2601.22607) or a
   tool failure produces a zero that the optimizer treats as the agent's fault; 2603.21972's record
   states that standard GRPO training "cannot separate the agent's mistakes from environment failures".
2. Industry cost: yes. The records name "teams training agents against real APIs or flaky
   infrastructure, whose environment error rate silently caps policy quality" (2603.21972), "teams
   training agents against real tools, APIs and sandboxes, who lose hours of GPU time to a single rate
   limit or crash" (2606.04484), and 2608.14635 measures that "1% of environment action failures can
   extend the rollout duration by 48.7%".
3. Ceiling: enabling where the environment's error rate is at the level of real services, constant-factor
   where failures are rare. The one record with a sign flip is 2601.22607: "training with the base user
   model degrades performance to 75.6%, while training with the finetuned user model improves performance
   to 95.6%" from an 85.4% start, so the same RL recipe is harmful or helpful depending on the
   environment side alone. 2603.21972's 10%-failure result is a degradation, not an infeasibility. The
   uncertainty is that only one record documents the sign flip and it conflates simulator error with
   simulator bias (P8).
4. Density: **6 groups**, low. Four work on the training-side problem, two publish evaluation
   benchmarks only. Queries P7q1–P7q6 (Section 4); P7q5 (noisy/corrupted rewards + agent + LLM) returned
   zero papers in the window.

**Density evidence.**
- 2609.24144 (2026-09-21) Luck Is Not Skill: When Do Paired Rollouts Help Group-Relative RL of LLM
  Agents? — Sakib. Shares one environment-noise schedule across the rollouts of a group so the
  comparison is between agent choices, not luck.
- 2608.11977 (2026-08-12) Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via
  Controlled Error Injection — Chen … Lai. Injects transient, persistent and silent tool failures into
  failure-free tool-use data and trains recovery policies.
- 2608.14635 (2026-07-28) Belayer — Zhou … Zhang (in the harvest).
- 2604.28138 (2026-04-30) Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes — Wu …
  Wang (in the harvest; recovery, not attribution).
- 2602.11348 (2026-02-11) AgentNoiseBench — Wang … Chua. Evaluation of tool-using agents under noisy
  conditions; no training.
- 2609.05587 (2026-09-04) Agents' Overreliance on Unreliable Tools — Yang … Jo. Evaluation of agents
  given plausible-but-wrong tool returns; no training.
Nobody in the window publishes a measurement of how much of an agentic-RL reward signal is
environment-attributable, and nobody separates agent error from environment error inside the training
loop.

**Build or measure first.** A measurement, on the three standard training environments (τ²-bench with
a simulated user, a SWE-Gym-style sandbox with real tests, a live-web search agent), of what fraction
of zero-reward episodes are environment-caused: re-run the identical action prefix against the
environment and log disagreement, and have humans label a few hundred failed episodes as agent-fault
or environment-fault. The artifact is a labeled corpus of failed agent episodes with the fault side
tagged, plus the per-environment failure rate as a function of concurrency and run length. The records
give the ingredients (τ²-bench's 16–40% simulator error rate, STAR's 10% injection, Belayer's 1% action
failures) but no one has put them on one axis or measured the effect on the learned policy at realistic
rates.

**Kill fact.** If the measurement shows that, after trivial retries, environment-attributable zero
rewards are under about 2% of episodes on the standard training environments, the problem is the
constant-factor nuisance Belayer already handles (1% failures, +48.7% wall-clock), not a direction.

### 2. P6 — Sandboxes cannot be rewound mid-episode

**Statement.** No mainstream agent sandbox can be saved and restored mid-episode fast enough or
faithfully enough, so anything that forks, rewinds or resets a rollout (step counterfactuals, reset
curricula, tree search, crash recovery) is confined to toy text environments. 27 records, 11 papers
(2410.01679, 2602.03419, 2602.11767, 2604.28138, 2605.05112, 2605.22781, 2607.14171, 2607.26417,
2608.14635, 2609.11061, 2609.33875); kinds: infra 14, cost 8, reliability 3, generalization 2.

**Quotes.**
- 2605.22781 (DeltaBox, millisecond checkpoint/rollback by saving only diffs and forking a warm process
  template): "both BoN and MCTS need fast intermediate C/R, which no mainstream agent system provides
  today (§ 2.3): systems avoid deep search precisely because the infrastructure does not yet exist."
- 2604.28138 (Crab, eBPF-watched per-turn selective checkpointing): "Even modern sandbox substrates expose
  this cost: E2B [16] (based on Firecracker [19]) requires pausing the microVM before snapshot creation
  and introduces more than 4 s overhead [17, 19]."
- 2607.14171 (BPO, snapshot the sandbox at high-entropy steps and fork alternatives): "We assume
  rest(snap(s)) = s in distribution (Assumption 1), which captures the resumability of typical sandboxes
  (Docker overlayfs, CRIU, Python interpreter pickling, browser session export)."
- 2607.26417 (SCOUT, per-task reset curricula that move the start state toward the goal): "SCOUT needs
  informative bottleneck states, an ordered assistance axis, and the ability to restore selected states.
  ... The method does not apply without reset access, as on physical robots without instrumented resets."
- 2602.11767 (TSR, per-turn search during rollout generation): "TSR also assumes that the environment can
  be branched, restored, or re-queried at intermediate states, which holds naturally for the digital and
  simulator-based environments common in LLM-agent research (e.g., web sandboxes, text games, and code
  interpreters), but may require learned environment models in non-resettable settings."

**Tests.**
1. Recipe failure: yes. The standard rollout engine samples independent straight-line trajectories and
   has no branch-at-step primitive (2602.11767, 2605.22781); the three credit-assignment papers that
   fork (2607.14171, 2609.33875, 2609.11061) each list restore cost or fidelity as their binding
   constraint, and 2609.33875 reports "Fork/materialisation and counterfactual rollout remain the
   dominant training-time overheads".
2. Industry cost: yes. Named payers: "sandbox providers such as E2B whose snapshot latency sits on the
   critical path" and "teams running tree search or RL over coding agents" (2605.22781); "hosted agent
   platforms whose default recovery mode is chat-history-only" (2604.28138); 2609.33875 reports 321 vs
   188 H100-hours per seed with forking.
3. Ceiling: enabling. Five records are tagged enabling (C010, C018, C022, C052, C053); the mechanism
   that would use it (deep search over coding agents, reset curricula on stateful environments) is
   currently not run at all: "systems avoid deep search precisely because the infrastructure does not
   yet exist" (2605.22781).
4. Density: **12 groups** (8 building the mechanism, 4 using it in RL), moderate. Queries P6q1–P6q4 plus
   two hits surfaced by P12q2. The RL-side user count (4) is the relevant one for a researcher who is
   not a systems builder.

**Density evidence.**
- 2605.22781 (2026-05-21) DeltaBox — Dong … Haibo Chen (SJTU). Diff-only checkpoints, overlay hot-swap,
  warm process fork.
- 2604.28138 (2026-04-30) Crab — Wu … Wei Wang (HKUST). Per-turn skip/file/full checkpoint decided from
  observed OS effects.
- 2609.35366 (2026-09-28) Planarian: Managing Agent State with Statepoints — Guo … Pietzuch (Imperial).
  Statepoints that coordinate reverting local and remote-service state.
- 2605.17320 (2026-05-17) TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents —
  Huang … Yiying Zhang (UCSD). Fast branching of live desktop workspaces for speculative execution.
- 2602.08199 (2026-02-09) Fork, Explore, Commit: OS Primitives for Agentic Exploration — Cong Wang,
  Yusheng Zheng. A "branch context" OS abstraction with copy-on-write file and process state and atomic
  commit/rollback.
- 2604.12129 (2026-04-13) Aethon: A Reference-Based Replication Primitive for Constant-Time Instantiation
  of Stateful AI Agents — Rao … Krishnan.
- 2512.12806 (2025-12-14) Fault-Tolerant Sandboxing for AI Coding Agents: A Transactional Approach —
  Boyang Yan.
- 2608.14635 (2026-07-28) Belayer (in the harvest).
RL-side users of fork/restore in the window: 2607.14171 (BPO), 2609.33875 (CRR), 2609.32750
(CUA-Sandbox, copy-on-write slices per rollout), 2609.18304 (Rollback the World, Keep the Reflection —
Yu … Libing Wu; rolls the environment back after an erroneous action and keeps the reflection).

**Build or measure first.** A benchmark of restore fidelity and cost on real agent traces: for each
sandbox backend (Docker + CRIU, Firecracker micro-VM, Linux namespaces, the new diff-based systems),
measure the divergence between a restored branch and its parent (files, processes, network and
external-service state), the per-step snapshot cost against the per-step rollout cost (2607.14171's
Table 4 does this for a few environments only), and the fraction of agent steps on SWE-Gym, WebArena
and AppWorld whose effects leave the sandbox, which is how often 2607.14171's Assumption 1 holds. The
records state the assumption; nobody has measured how often it is true.

**Kill fact.** If DeltaBox, Crab and TClone are shown to restore faithfully at millisecond cost on the
standard RL training environments, the infrastructure problem is solved by existing systems and what
remains is the scheduler for tree-shaped rollouts (A018, A022), a smaller problem.

### 3. P5 — Multi-turn agent RL collapses as horizon or run length grows

**Statement.** RL on multi-turn agents collapses (reward suddenly drops, outputs degenerate, solved
tasks regress) as episodes or training runs get longer, and the usual knobs only delay it with no
diagnosis of the cause. 10 records, 8 papers (2509.13305, 2510.24701, 2512.17008, 2512.18552,
2604.11037, 2605.00347, 2605.11556, 2607.16257); kinds: reliability 8, signal 2.

**Quotes.**
- 2512.17008 (Turn-PPO, each turn is the RL action with a per-turn critic): "Our analysis shows that
  these failures are systematic and cannot be resolved by variants within the GRPO framework."
- 2605.00347 (Odysseus, PPO for a VLM game agent with a small CNN critic): "both outcome-reward and
  process-reward variants of these methods fail to learn effective policies that can make consistent
  multi-step progress (see results in Section 4.2)."
- 2512.18552 (self-play SWE-RL, one model injects bugs and fixes them): "Stable training at scale:
  Despite following (Devvrit et al., 2026; Zheng et al., 2025), we still observed training instability
  that prevents SSR from further scaling, manifesting as gibberish outputs. This instability may stem
  from a combination of suboptimal hyperparameter settings, intrinsic challenges of long-horizon
  rollouts, model pretraining dynamics, and fundamental properties of self-play learning."
- 2607.16257 (hindsight intent distributions in embedding space): "GRPO (Shao et al., 2024) can maintain
  stable training under shorter interaction horizons, but becomes unstable as the horizon length
  increases, often exhibiting sudden reward collapse (Jin et al., 2025; Xue et al., 2025; Sun et al.,
  2025)."
- 2604.11037 (RTMC, rollout trees from hashed step signatures): "We observe that RL training does not
  uniformly improve performance: the trained model solves new problems that the base checkpoint fails
  on, but also regresses on a subset of previously solved instances. Understanding and mitigating this
  regression—whether through better credit assignment, curriculum design, or checkpoint selection—remains
  an open question."

**Tests.**
1. Recipe failure: yes. 2512.17008 states the failure "cannot be resolved by variants within the GRPO
   framework"; 2512.18552 followed two published stabilization recipes and still collapsed;
   2605.00347's critic-free baselines fail "regardless of reward design or the use of advantage
   filtering".
2. Industry cost: yes. "Meta FAIR and any lab trying to scale self-play SWE training beyond the reported
   run length" (2512.18552); "Labs shipping RL-trained coding agents that regress on previously working
   cases" (2604.11037); "Teams training multi-turn web or embodied agents with GRPO who lose runs to
   collapse" (2512.17008).
3. Ceiling: enabling. The instability "prevents SSR from further scaling" (2512.18552), and at 100+
   turns critic-free methods make no progress at all (2605.00347). The uncertainty: 2605.00347 shows a
   small critic restores learning in its game setting, so part of this problem is already solved by
   switching recipe; what is not solved is the undiagnosed collapse under the recipe people actually
   use (GRPO at scale, self-play).
4. Density: **15 groups**, high. Queries P5q1–P5q3. One group offers a mechanistic diagnosis (lazy
   likelihood displacement, 2512.04220); the rest propose stabilizers.

**Density evidence.**
- 2512.04220 (2025-12-03) On Group Relative Policy Optimization Collapse in Agent Search: The Lazy
  Likelihood-Displacement — Deng … Xiaoxiao Li (UBC). A named mechanism for collapse in search agents.
- 2608.18682 (2026-08-19) RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training —
  Li … Siyi Hu.
- 2605.02178 (2026-05-04) T²PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL
  — Wang … Yizhou Sun (UCLA).
- 2602.21534 (2026-02-25) ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning — Wang
  … Wei Wang (UCLA).
- 2511.20718 (2025-11-25) Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level
  Importance Sampling and Clipping-Triggered Normalization — Li … Mingyi Hong.
- 2510.14545 (2025-10-16) Agentic Entropy-Balanced Policy Optimization — Dong … Zhicheng Dou.
- 2604.18235 (2026-04-20) Negative Advantages Is a Double-Edged Sword: Calibrating advantages in GRPO
  for Search Agents — Wu … Xiang Li.
- 2602.07078 (2026-02-06) The Optimal Token Baseline: Variance Reduction for Long-Horizon LLM-RL — Li …
  Baoxiang Wang.
Also in the window: Dr. MAS (Bo An), SeeUPO (Bolin Ding), Proximity-Based Multi-Turn Optimization
(Peilin Zhao), STARE (Yansong Tang), GTR-Turbo (Deheng Ye), FoldAct (Bing Luo), Improving Search Agent
with One Line of Code (Yabiao Wang).

**Build or measure first.** A reproducible collapse testbed: one fixed multi-turn environment, model
and recipe on which the collapses of 2512.17008, 2605.00347 and 2512.18552 reproduce on demand, with
the training-time signals logged per turn (policy entropy, advantage distribution, importance ratios,
truncation rate, the turn-count imbalance of A128, the regression set of 2604.11037) so that the four
candidate causes 2512.18552 lists can be separated by ablation rather than guessed. No record contains
such a testbed; every collapse report is a single run inside a method paper.

**Kill fact.** If the reproduced collapse traces to one already-named cause with a published fix
(lazy likelihood displacement per 2512.04220; truncation filtering per 2609.36802; routing mismatch per
the MoE stabilization papers), the direction is engineering adoption, not research.

### 4. P4 — The supply of learnable-difficulty tasks

**Statement.** On hard agent tasks most groups of rollouts all pass or all fail so the expensive rollouts
teach nothing; finding tasks at the right difficulty costs extra rollouts and the supply runs out; when
the policy almost never succeeds every success-based method stalls. 24 records, 13 papers (2402.19446,
2502.12272, 2506.11425, 2512.18552, 2605.05112, 2605.07579, 2605.11556, 2607.04713, 2607.14171,
2607.16257, 2607.26417, 2609.20004, 2610.00388); kinds: signal 13, data 7, cost 3, eval 1.

**Quotes.**
- 2605.05112 (Rollout Pass-Rate Control, replay a saved prefix to push group pass rate toward 50%):
  "However, when the reward contrast collapses, no optimizer can extract a strong binary-reward update
  from that group; balancing the pass rate maximizes the part of the signal controlled by the rollout
  outcomes."
- 2607.14171 (BPO): "whereas in GRPO an all-success or all-failure prompt batch contributes near-zero
  advantage. We measure that the fraction of training steps with non-degenerate advantage (defined as
  max(|A|) > 0.1) rises from 71% for GRPO to 94% for BPO on SWE-bench."
- 2506.11425 (Agent-RLVR, re-run failed tasks with hints and train offline on pass/fail pairs): "These
  settings, characterized by multi-step, complex problem solving, lead to high failure rates even for
  frontier LLMs, as the reward landscape is too sparse for effective model training via conventional
  RLVR."
- 2502.12272 (train only on questions solved about half the time): "On GSM8K we find that finding
  learning questions via rejection sampling (Algorithm 2) with |D| = 4 × |B| cannot consistently
  learnable questions during training, as train performance is closing in on 95%."
- 2512.18552: "While this seems to encourage the challenger to target an arbitrarily small solve rate,
  “arbitrarily small” cannot be distinguished from 0 by a small group of G = 8 samples so some margin is
  needed to achieve the optimum expected reward."

**Tests.**
1. Recipe failure: yes. GRPO's advantage is zero on uniform groups by construction and "no optimizer can
   extract" an update (2605.05112); at near-zero pass rate "conventional RLVR" does not train
   (2506.11425); static banks exhaust (2502.12272).
2. Industry cost: yes. "Labs training coding agents, who burn about 30% of rollout compute on
   zero-gradient groups" (2607.14171); "Labs curating RL datasets per model generation; the curation
   effort is repeated each time the model changes" (2502.12272); "labs trying to apply verifiable-reward
   RL to agent tasks where the base model's success rate is near zero" (2506.11425).
3. Ceiling: enabling only at the zero-success end (C000, A053, A134: training does not start or stops),
   constant-factor for the waste (71% to 94% non-degenerate steps is a 1.3x effect). The uncertainty is
   how much of real agent-RL compute sits at pass rate 0 versus near 0.5; the records give one number
   (29% of SWE-bench steps degenerate) and no distribution over training.
4. Density: **17 groups**, high. Queries P4q1–P4q4. The zero-variance-group waste is directly addressed
   by at least four groups (Xiong at CMU, Huan, Gao, Lei Zhang) and the rollout-budget question by at
   least four more.

**Density evidence.**
- 2606.10709 (2026-06-09) Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance
  Queries During Training — Coelho … Chenyan Xiong (CMU).
- 2608.17423 (2026-08-18) Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups
  — Deng … Jun Huan.
- 2608.27982 (2026-08-28) Learning from Hard Prompts: Difficulty-aware Advantage Amplification in
  Dynamic Sampling — Gan … Yang Gao.
- 2607.26253 (2026-07-28) Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for
  Compute-Efficient RLVR — Nomand … Reyes (same group as 2609.38018, Gaussian curricula).
- 2606.11119 (2026-06-09) TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic
  Reinforcement Learning — Zou … Xiangyang Ji.
- 2607.07674 (2026-07-08) Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning
  Problems — Beliaev.
- 2609.35303 (2026-09-28) PIVOT: Pivot-Aware On Policy Self Distillation for Multi-Turn VLM Agents —
  Zhou … Lei Zhang (names "zero-gradient silence on uniform failures").
- 2605.05262 (2026-05-06) Maximizing Rollout Informativeness under a Fixed Budget: A Submodular View of
  Tree Search for Tool-Use Agentic RL — Hu … Li Song.
Also: Groupwise Agentic Grading and Advantage Redistribution (Fuli Luo), Weak-Model Guidance in RLVR
(Dongyan Zhao), Selective Rollout (Xin Wang), WS-GRPO (Junda Wu), Progressive Reward Shaping with
Value-based Sampling (Zhuoran Zhuang), Process Reward Informed Tree Rollout (Jingbo Shang), The Filter
Metric is Safety-Critical (Juntao Yu), HDL (in the harvest).

**Build or measure first.** A measurement, on a real agentic-RL run (SWE or web), of the group
pass-rate distribution of the task bank at every training step: what fraction of rollout compute lands
in all-pass, all-fail and mixed groups as a function of group size and step; how fast the mixed region
empties (A134's exhaustion); and how many tasks sit at exactly zero over the whole run. The records
give single snapshots (29% degenerate steps; 7% of tasks discarded) and no trajectory over training,
so nobody knows whether the binding constraint is the bank, the sampler or the group size.

**Kill fact.** If prefix replay (2605.05112) and DAPO-style dynamic sampling already keep non-degenerate
steps above 90% at under 1.3x rollout cost on agent tasks, the remaining waste is a small constant and
the zero-success regime is a data-supply problem that belongs to P11.

### 5. P14 — Pass/fail rewards cannot see communication

**Statement.** Benchmarks and rewards record only whether the final task passed, so they cannot see or
reward whether the agent noticed a missing or contradictory requirement and asked about it. 10 records,
6 papers (2502.13069, 2603.04370, 2603.13686, 2604.14624, 2608.12355, 2609.04611); kinds: eval 3,
reliability 3, data 2, other 1, cost 1. Four of the six are τ-bench-family papers.

**Quotes.**
- 2608.12355 (position paper: coding-agent research optimizes autonomous pass rates and drops the human):
  "Today, benchmarks sidestep the study of such intricacies entirely: pass@k collapses all signal about
  communicative quality into a single bit, discarding everything about how mutual understanding was (or
  was not) achieved."
- 2609.04611 (τᵗ-Bench, a developer agent must build a customer-service agent from messy records and a
  simulated client): "Real engagements offer no such guarantees: requirements go undocumented or
  contradict each other, and noticing that the specification has holes is part of the job we do not
  measure."
- 2608.12355: "Without open coding conversation data or widely adopted open-source tooling, systematic
  and quantitative evaluation of grounding quality remains prohibitively out of reach (Vijayvargiya et
  al., 2025)."
- 2502.13069 (Ambig-SWE, strip details from SWE-bench issues and let the agent ask a simulated user who
  holds them): "We did not evaluate on naturally underspecified SWE-Bench examples because they lack the
  paired ground truth (complete specifications) necessary for causal measurement of interaction impact."
- 2502.13069: "LLMs rarely initiate clarification unprompted, and their sensitivity to prompt framing
  makes them brittle in noisy, real-world contexts."

**Tests.**
1. Recipe failure: yes. Verifiable-reward setups need a consistent planted ground truth and so "cannot
   reward the skill of spotting holes in a specification" (2609.04611); rewarding a clarifying question
   by running the downstream task is "computationally intractable" (2604.14624, record B082).
2. Industry cost: yes. "Companies deploying coding agents end up with tools optimized for leaderboards
   rather than for the developers who use them" (2608.12355); "Companies deploying coding agents pay for
   wasted runs on underspecified tickets" (2604.14624); "The model compensates for the lack of
   information with increased exploration and solution attempts leading to substantially higher
   evaluation costs" (2502.13069).
3. Ceiling: enabling. A skill no reward can observe cannot be trained; three records (B002, B052, B053)
   are tagged enabling. The uncertainty: 2502.13069 shows that prompting alone flips asking behavior,
   so part of the gap is a default rather than a capability.
4. Density: **20 groups**, high. Queries P14q1–P14q3 (narrowed twice). Clarification in coding agents
   is crowded; the specific gap the records name, real conversations with paired complete
   specifications, has one entrant (RealClawBench, live developer-agent sessions).

**Density evidence.**
- 2606.05920 (2026-06-04) Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and
  Multi-Round Refinement — Wang … Zhendong Mao.
- 2607.02294 (2026-07-02) Coding Agents Are Guessing: Measuring Action-Boundary Violations in
  Underspecified DevOps Instructions — Ji … Shing-Chi Cheung.
- 2603.26233 (2026-03-27) Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents —
  Edwards, Schuster.
- 2610.01769 (2026-10-01) CONTRA: Discovering and Qualifying Behavior-Changing Questions for Selective
  Clarification in LLM Code Generation — Fang … Ge Li.
- 2512.04111 (2025-11-30) CentaurEval: Benchmarking Human-in-the-Loop Value in Agentic Coding — Luo …
  Salam.
- 2606.09833 (2026-04-20) CollabSkill: Evaluating Human-Agent Collaboration On Real-World Tasks — Shao
  … Diyi Yang.
- 2603.26942 (2026-03-27) The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding
  Agents — Wang … Wang.
- 2606.03889 (2026-06-02) RealClawBench: Live OpenClaw Benchmarks from Real Developer-Agent Sessions —
  Lv … Zhao.
Also: Pareto-Dominant Clarification (PPO-Lagrangian budgets), Tri-Agent clarification framework,
DiscoBench (deep search), Uncertainty-Aware Clarification with Information Gain, Turning Intent into
Specifications (IBM), Ambig-DS, Learning Steerable Clarification Policies (Berant/Eisenstein), No More
No Less (terminal agents), TOM-SWE, CodeScout (Amazon), Beyond expert users (Guestrin),
ClarifyMT-Bench, Beyond Oracle Communication (Wei Xu).

**Build or measure first.** A corpus of real developer–agent conversations with the paired complete
specification (the artifact 2502.13069 says does not exist and 2608.12355 says blocks the field), and
a measurement on it of how often real tickets contain missing or contradicting requirements, how often
frontier agents notice, and how far the synthetic-removal protocol of 2502.13069 agrees with the real
distribution of holes.

**Kill fact.** If frontier agents, simply prompted to ask, already detect and raise about 90% of the
real-ticket specification holes (2502.13069 reports asking is prompt-sensitive), the gap is a default
setting, not a training or measurement problem.

### 6. P11 — Real environments are unaffordable or unbuildable; substitutes have a fidelity gap

**Statement.** Training against real environments (the live web, real APIs, real repositories) is too
costly, slow or non-stationary, or impossible when the project will not build, and the offline or
learned substitutes have a measurable fidelity gap. 13 records, 8 papers (2402.19446, 2506.11425,
2509.13305, 2510.24701, 2602.03419, 2602.11210, 2603.21972, 2604.17931); kinds: data 4, cost 3, infra
2, reliability 1, signal 1, generalization 1, eval 1.

**Quotes.**
- 2604.17931 (LiteResearcher, replace the live web with a local corpus of tens of millions of pages plus
  a local search engine): "However, scaling agentic RL for deep research remains constrained by two
  coupled challenges: hand-crafted synthetic data fails to elicit genuine real-world search
  capabilities, and real-world search dependency during RL training introduces instability and
  prohibitive cost, which limits the scalability of Agentic RL."
- 2604.17931: "Beyond the cost saving, the 10–46× latency advantage directly translates to higher rollout
  throughput, making our local ecosystem a prerequisite—not merely an optimization—for scalable
  on-policy agentic RL."
- 2510.24701: "(1) Non-stationarity. The dynamic nature of environments causes continuous distribution
  shift in training data, undermining learning stability; (2) Interaction cost. The tangible expense of
  each API call makes large-scale exploration economically prohibitive."
- 2602.03419 (SWE-World, two fine-tuned LLMs stand in for the container: one predicts command output,
  one predicts test pass/fail): "many real-world repositories and pull requests cannot be readily
  leveraged, as complex or brittle dependency configurations often prevent projects from building or
  executing reliably within containerized environments [13]."
- 2602.11210 (SWE-MiniSandbox, namespaces plus chroot over cached virtual environments): "We filter out
  instances that already pass (approximately 20k) under the default installation commands. The remaining
  instances are dropped and not used in subsequent training. This filtering does not imply that the
  excluded instances are unsolvable; rather, they simply require additional setup or verification beyond
  the default commands."

**Tests.**
1. Recipe failure: yes. On-policy GRPO against live tools is throughput-bound by tool latency
   (2604.17931) and cost-bound ("$59K to $243K in API fees for 73 million tool calls"); execution-based
   rewards exclude every repository that does not build (2602.03419, 2602.11210).
2. Industry cost: yes. "Labs training search agents on the live web" (2604.17931); "labs building SWE
   training sets, who discard most crawled pull requests for lack of a buildable environment"
   (2602.03419); the training-set bias toward easy-to-install repositories (2602.11210).
3. Ceiling: enabling. Four records are tagged enabling (B086, B090, B116, C005): the local ecosystem is
   "a prerequisite—not merely an optimization" and unbuildable repositories are excluded entirely rather
   than slowed.
4. Density: **≥20 groups**, very high, and the SWE-environment side is industrialized (one paper in the
   window is titled "A 'Shovel of the Gold Rush' Benchmark on Automatic Environment Building"). Queries
   P11q1–P11q3 (two narrowed). The offline-web side was not surfaced by the queries (two results, both
   unrelated); the harvest itself holds the three Tongyi papers on it.

**Density evidence.**
- 2603.13023 (2026-03-13) daVinci-Env: Open SWE Environment Synthesis at Scale — Fu … Pengfei Liu.
- 2602.23866 (2026-02-27) SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale — Badertdinov
  … Golubev (Nebius).
- 2512.06915 (2025-12-07) Multi-Docker-Eval: A 'Shovel of the Gold Rush' Benchmark on Automatic
  Environment Building for Software Engineering — Fu … Kaigui Bian.
- 2609.33429 (2026-09-27) Graph-Guided Repository Environment Construction — Pan … Hongyu Zhang.
- 2605.26186 (2026-05-25) SetupX: Can LLM Agents Learn from Past Failures in Functionality-Correct Code
  Repository Setup? — Zhou … Fan Wu.
- 2603.06739 (2026-03-06) ResearchEnvBench: Benchmarking Agents on Environment Synthesis for Research
  Code Execution — Wang … Xipeng Qiu.
- 2609.28416 (2026-09-23) Agent-Editing World Model: Rethinking World Modeling for LLM Agents — Sun …
  Ji-Rong Wen (the SWE-World group; learned execution surrogate).
- 2602.07274 (2026-02-06) TermiGen: High-Fidelity Environment and Robust Trajectory Synthesis for
  Terminal Agents — Zhu … Wenbo Guo.
Also: Change2Task, Meta-Task, LiteCoder-Terminal, Terminal-World, D3-Gym (Huan Sun), SWE-Next (Wenhu
Chen), SWE-Hub, CVE-Factory (Che), Dockerized trajectory generation (Chenghua Lin), EvoConfig,
Deploy-Master, CyberForge (Manocha), EnvScaler (Dou), EnvCraft.

**Build or measure first.** A measurement of the substitute's fidelity gap: agents trained on the
offline corpus (2604.17931) or the learned executor (2602.03419) versus the same recipe on the live
web or real execution, scored on identical tasks; and a census of why crawled pull requests fail to
build (C005, C016) so the excluded set's bias is known rather than assumed.

**Kill fact.** If the environment-synthesis pipelines in the window already build above 80% of
crawled repositories and offline-trained search agents match live-web-trained ones (2604.17931 claims
this at 4B), the supply problem is solved by industry and only the fidelity measurement remains.

### 7. P8 — Simulated users are systematically unlike people and their fidelity is unmeasured

**Statement.** Language models playing the user are systematically unlike people (too cooperative, too
patient, single-habit), so agents learn exploits and scores inflate, and there is no way to measure a
simulator's fidelity or confirm transfer to real humans. 27 records, 12 papers (2502.13069,
2506.07982, 2509.19736, 2601.22607, 2603.04370, 2603.13686, 2604.02869, 2608.12253, 2608.12355,
2609.04611, 2609.38043, 2610.09484); kinds: eval 9, signal 8, reliability 5, generalization 4, cost 1.
Five are τ-bench-family papers.

**Quotes.**
- 2608.12253 (simulator collapse; fixes are several weighted replies per turn or co-training the
  simulator): "We show that this approach systematically fails to generalize, and trace the failure to
  simulator collapse: because the simulator LLM is mode-collapsed, an LLM policy trained against it
  overfits to narrow strategies that exploit the simulator’s dominant mode, and such a policy transfers
  poorly to unseen simulators and real users."
- 2610.09484 (MIMESIS, a dedicated simulator trained on human conversations with written-out thoughts;
  82% success against off-the-shelf simulators versus 64% with humans): "This result suggests that
  simulator quality cannot be assessed from surface naturalness alone; preserving the interaction
  difficulty induced by human users is also important when the simulator determines the trajectories
  used for agent training or evaluation."
- 2609.38043 (UserProxyBench, rubric-graded User Fidelity Score against dollar cost): "Across all 2,618
  scored trajectories (of 2,625: two runs hit an infrastructure error, and five were unscorable because
  no criterion applied—Appendix B), 24.4% of agent-successful episodes fail UFS; on Telecom, 39.7% of all
  trajectories are Rτ pass / UFS fail."
- 2608.12355: "We encourage researchers and industry to partner and share anonymized interaction data to
  enable scalable research. Ultimately, measuring and improving the fidelity of LM-based simulators
  remains an open challenge."
- 2609.38043: "Limitations include one rollout per task, time-dependent serving prices, a pinned Banking
  version, and no measurement of downstream trained-policy effects."

**Tests.**
1. Recipe failure: yes. GRPO against one frozen simulator "systematically fails to generalize"
   (2608.12253); task reward is blind to simulator misbehavior in 24.4% of successful episodes
   (2609.38043); the recipe contains no fidelity check.
2. Industry cost: yes. "Teams that ship agents trained against a single simulated user get policies that
   underperform on real customers" (2608.12253); "Anyone reading benchmark numbers produced with
   LLM-simulated users is misled about real-world performance" (2610.09484); 2601.22607's 20-point
   swing from simulator quality alone.
3. Ceiling: enabling. Held-out success "collapses back toward Base" (2608.12253), so RL against a frozen
   simulator yields zero transferable gain without a fix; eight records are tagged enabling.
4. Density: **22 groups**, very high; this is the most crowded problem in the shortlist after P1 and
   P13, and it is the τ-bench group's home turf. Queries P8q1–P8q3 (two narrowed).

**Density evidence.**
- 2603.11245 (2026-03-11) Mind the Sim2Real Gap in User Simulation for Agentic Tasks — Zhou … Maarten
  Sap (CMU).
- 2601.17087 (2026-01-23) Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users
  in Agentic Evaluations — Seshadri … Goldfarb-Tarrant.
- 2606.20708 (2026-06-16) Simulated Customers Never Walk Away: Decision Fidelity of LLM User Simulators
  Measured Against Real Purchase Outcomes — Liang Chen.
- 2606.19336 (2026-06-17) Learning User Simulators with Turing Rewards — Wang … Yoon Kim (MIT).
- 2602.16938 (2026-02-18) ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators
  in Conversational Recommenders — Meshi … Boutilier (Google).
- 2609.38043 (2026-09-29) UserProxyBench (in the harvest).
- 2608.12253 (2026-08-12) One Frozen Simulator Is Not Enough (in the harvest; Weiyan Shi).
- 2610.09484 (2026-10-07) MIMESIS (in the harvest).
Also: Back in Style (persona fidelity), AgentPersonaBench, CUEing User Simulators (Mueller), Assistant
Bias in User Simulators (Juho Kim), Faithful Simulation of Shopping Behavior (Bo Zheng), Verifiable User
Simulation (Chan), VISTA (Zhou Yu), RealUserSim (Salesforce), CustomerSim (Salesforce), UserLM-R1,
Disclosure-Gated User Simulation, Person-Aligned User Simulation, Beyond Oracle Communication (Wei Xu),
PB-GRPO.

**Build or measure first.** The downstream test 2609.38043 says is missing: train the same agent against
simulators of graded fidelity and evaluate every resulting policy against real humans on the same tasks
(2610.09484 has one such data point, 82% versus 64%), so that fidelity scores are validated against
the quantity that matters, trained-policy transfer, rather than against rubric compliance.

**Kill fact.** If a fine-tuned simulator (MIMESIS, UserLM-R1) closes the human gap to within the
benchmark's confidence interval on τ²-bench, fidelity is a solved data problem and the 22 groups have
finished it.

### 8. P1 — One end-of-episode grade cannot say which step mattered

**Statement.** When a long agent episode gets one grade at the end, nothing in today's recipe says which
of the many steps helped or hurt, and getting that answer exactly costs rollouts that multiply with
episode length. 28 records, 17 papers; kinds: signal 21, cost 6, generalization 1.

**Quotes.**
- 2609.20004 (EPIG-Tree, fork where an extra branch most reduces gradient variance per compute):
  "Reward based GRPO assigns the whole trajectory a negative group-relative reward, so the correct
  actions are also punished. Conversely, if a trajectory succeeds despite multiple bad actions, the bad
  actions are reinforced."
- 2609.11061 (fork where a cheap probe of the model's answer belief shifts most): "LM judges are offline
  and costly [19], and learned rewards are exploitable during RL [11]; agent turns [30, 44] cost K T
  rollouts if branched exhaustively over T turns."
- 2608.01667 (TCPO, per-turn verifier scores turned into credit by best-so-far, hindsight and
  counterfactual references): "Trajectory-level methods broadcast final or best-turn success to all
  tokens, mixing failed attempts, useful repairs, and post-success regressions. Raw turn score rewards
  state quality rather than marginal contribution."
- 2604.11037 (RTMC): "With N =8 rollouts per problem, the majority of states are visited only once,
  limiting where true cross-rollout action comparison can occur. State isolation. Because most tree nodes
  receive only a single visit, the raw MC estimate yields zero advantage there"
- 2608.19760 (audit of step-credit signals against executed replay): "The ground truth is structured:
  30.5% of decision points where it is defined exhibit a nonzero replay contrast at the achieved
  sampling resolution, and measurability is model-dependent — the fraction of points with no
  policy-supported counterfactual differs twofold (13.1% vs. 26.8%) between two similar-scale policies."

**Tests.**
1. Recipe failure: yes. 23 of 28 records state a recipe failure; GRPO's uniform advantage is the stated
   mechanism in ten papers.
2. Industry cost: yes. "Teams training long-horizon or multi-turn agents with GRPO, who waste rollouts
   on wrong credit" (2609.20004); "Labs training long-horizon agents, where each rollout is many turns
   long and groups multiply that cost" (2605.07579).
3. Ceiling: enabling at horizons above about 100 turns, where critic-free methods make no progress
   (2605.00347) and successes are not found by chance (2402.19446). Two caveats from the records: the
   same 2605.00347 shows a small per-turn critic already crosses that threshold, and 2608.19760 finds
   that on its testbed "no arm reliably outperforms the untrained policy" once training dose is matched,
   so the enabling claim rests on the long-horizon regime that neither paper tests with dose matching.
4. Density: **≥28 groups**, the most crowded algorithmic problem in the list. Queries P1q1–P1q3; P1q1
   alone returned 37 papers, most of them turn-level advantage schemes.

**Density evidence.**
- 2610.08402 (2026-10-06) VETTA: Coordinating Turn- and Token-Level Credit Assignment for Multi-Turn
  LLM Agents — Chen … Yong Li.
- 2607.13988 (2026-07-15) TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon
  Agents — Tao … Sharon Li.
- 2609.28963 (2026-09-24) Back to the Definition: Estimating Step-Level Advantages via Trajectory Graphs
  for Agentic RL — Yao … Chongyang Zhang.
- 2606.29476 (2026-06-28) CRAFT: Counterfactual Credit Assignment from Free Sibling Rollouts for
  Self-Distilled Agentic RL — Meng, Kani Chen.
- 2605.04984 (2026-05-06) Self-Induced Outcome Potential: Turn-Level Credit Assignment for Agents
  without Verifiers — Hu … Fang.
- 2606.22995 (2026-06-22) Group-Graph Policy Optimization for Long-Horizon Agentic RL — Wang … Qi Zhang.
- 2608.01667 (2026-08-03) TCPO (in the harvest).
- 2512.17008 (2025-12-18) Turn-PPO (in the harvest).
Also, in the window: HiDiffTIR, SAPO and PlanPO, AgentOPSD, TurnSight and MatchTIR, Group-Reflective
Self-Distillation, Hybrid Advantage Estimation with Unified Critic (Elhoseiny), ECHO, CIGPO, GEAR,
Structured Action Credit for CLI agents, A²TGPO, TSPO, GTPO, IGPO, CRR, PGPO, IAPO, DiDPO, SLEA-RL.

**Build or measure first.** The yardstick 2608.19760 says does not exist in a second setting: a
replay-based ground-truth step-contrast dataset on a resettable multi-turn environment at 50–200
turns, with the dose-matched protocol its record demands ("Comparisons of credit rules must match
effective sample size, or they measure dose, not credit"), so that the 28 competing credit schemes can
be scored against something other than each other's benchmarks.

**Kill fact.** If 2608.19760's finding, that no credit rule beats the untrained policy at matched dose,
replicates in a second environment and model family, step-credit is not a direction: training dose is.

## Section 3 — Ranked but not detailed, and dropped

Ranks 9–14 (in the table, not detailed here) and why they sit below the top 8:
- P2 proxy graders (rank 9): ceiling unknown rather than enabling; the records document only failures of
  proxies (2608.19760's shuffled-control result; 2607.04713's shaped reward rising while success falls;
  2602.03419's learned judge hacked), and 17 groups are on it.
- P12 sandbox density (rank 10): constant-factor (5% storage, 25% setup time) and industry-dominated
  (DeepSeek DSec with 131 authors, Kimi K3, NVIDIA ProRL Agent, Microsoft Orchard in the window).
- P13 idle vs stale (rank 11): constant-factor (speedup at most 2x per 2610.05935's own analysis) and the
  densest area measured (≥35 groups).
- P9 trial cost (rank 12): recipe can afford it with money; constant-factor; τ-aligned but 10 groups
  already on cheaper evaluation.
- P10 human labels (rank 13): constant-factor for evaluation (prediction-powered inference is a variance
  game); the ~100-interaction learning regime of 2402.19446 is enabling but no record shows a path to it.
- P3 critics (rank 14): a variance-reduction device, constant-factor; the one documented feasibility
  threshold (2605.00347 at 100+ turns) is already crossed by a small CNN critic; 18 groups.

Dropped clusters (fewer than four papers, or not a thing a researcher can attack), one line each:
- Experiments stop at 7–14B, one or two benchmarks, single seeds, so scaling behavior is unknown (about
  25 records across 20 papers): a resource limit on the authors, not a problem with a mechanism.
- Cross-cluster weight synchronization takes minutes to 87.5 minutes at trillion scale (2610.08430,
  2605.06534, 2609.35158): three papers, owned by NVIDIA and Moonshot infrastructure teams.
- KV-cache pressure in multi-turn rollouts: suspended trajectories evicted and recomputed (2610.03286,
  2608.08020, 2608.14635): three papers, constant-factor.
- Agents cannot write their own missing skills or carry memory across episodes (2609.31076,
  2506.06698): two papers; a capability wish, not a broken recipe. τ-aligned; worth re-checking next
  harvest.
- Context length and context management limit long-horizon agents (2510.24701, 2604.17931,
  2603.04370): three papers, generic.
- Implemented multi-turn GRPO differs silently from the textbook formula (turn-expanded group statistics
  in 2610.00388; overlong filtering changing the objective in 2609.36802; token-count imbalance in
  2605.00347): three papers; an engineering audit, filed for the kill-search stage.
- RLVR spends the sampling diversity that majority voting needs (2610.00991): one paper, not agentic.
- Benchmark contamination from public domains (2609.04611, 2606.10156): two papers.
- Self-play task generators produce trivial or duplicate tasks and cannot write realistic issues
  (2512.18552, 2505.22954): two papers; folded partly into P4.
- Searched rollouts drift too far from the policy for clipped updates (2602.11767, B >= 20): one paper.
- Training several models of different sizes jointly (2606.04484), reward-edit restarts (2606.04484),
  prefix re-encoding across turns (2606.04484): one paper each.
- Agents trained to maximize task success can learn manipulation (2610.09484); voice-text gap
  (2603.13686); agents do not revise upstream decisions after downstream evidence (2603.21972): one
  paper each.

## Section 4 — Queries run (audit trail)

All queries hit `https://export.arxiv.org/api/query` with
`search_query=(<query>) AND submittedDate:[202510090000 TO 202610100000]`, `max_results=50`,
`sortBy=submittedDate`, `sortOrder=descending`, 3-second pause between calls, Atom XML parsed with
Python's `xml.etree` under `python3 -I`. "n" is the number of entries returned (50 = capped, too
broad, re-run narrower). Two calls (P3q2, P3q3) first returned HTTP 429 and were re-run after a pause.
Raw XML and parsed listings are in the session scratchpad (`raw/`, `parsed/`).

| label | query | n | used for count |
|---|---|---|---|
| P1q1 | `abs:"turn-level" AND abs:advantage AND (abs:agent OR abs:"multi-turn")` | 37 | yes |
| P1q2 | `abs:counterfactual AND abs:rollout AND (abs:advantage OR abs:credit) AND abs:agent AND abs:"reinforcement learning"` | 2 | yes |
| P1q3 | `abs:"step-level" AND abs:advantage AND abs:"multi-turn" AND abs:agent` | 9 | yes |
| P2q1 | `abs:"process reward" AND abs:agent AND (abs:hacking OR abs:exploit OR abs:noisy OR abs:unreliable)` | 19 | yes |
| P2q2 | `abs:"reward hacking" AND (abs:verifier OR abs:judge OR abs:"reward model") AND abs:agent` | 50 (total 57) | too broad |
| P2q2n | `abs:"reward hacking" AND (abs:verifier OR abs:"reward model") AND abs:agent AND abs:"reinforcement learning" AND (abs:code OR abs:coding OR abs:tool)` | 11 | yes |
| P2q3 | `abs:"LLM-as-a-judge" AND abs:reward AND abs:"reinforcement learning" AND (abs:bias OR abs:hacking OR abs:exploit)` | 9 | yes |
| P3q1 | `(abs:"value function" OR abs:"value network" OR abs:"value model") AND abs:critic AND abs:"language model" AND (abs:PPO OR abs:variance)` | 10 | yes |
| P3q2 | `abs:"control variate" AND abs:"policy gradient" AND (abs:"language model" OR abs:LLM)` | 1 | yes (after 429 retry) |
| P3q3 | `abs:"critic-free" AND (abs:critic OR abs:"value function") AND (abs:LLM OR abs:"language model") AND abs:"reinforcement learning"` | 49 | yes (after 429 retry) |
| P4q1 | `abs:"dynamic sampling" AND (abs:RLVR OR abs:GRPO OR abs:"verifiable reward")` | 19 | yes |
| P4q2 | `abs:curriculum AND (abs:GRPO OR abs:RLVR) AND (abs:difficulty OR abs:"pass rate" OR abs:learnability) AND abs:agent` | 3 | yes |
| P4q3 | `abs:"sparse reward" AND abs:agent AND (abs:GRPO OR abs:RLVR OR abs:"verifiable reward") AND (abs:hint OR abs:prefix OR abs:"task generation" OR abs:"self-play")` | 2 | yes |
| P4q4 | `(abs:"online filtering" OR abs:"rollout filtering" OR abs:"difficulty filtering" OR abs:"pre-filtering" OR abs:"rejection sampling" OR abs:"prefix") AND (abs:GRPO OR abs:RLVR) AND (abs:efficiency OR abs:wasted OR abs:learnable OR abs:"zero gradient")` | 36 | yes |
| P5q1 | `abs:"entropy collapse" AND (abs:agent OR abs:"multi-turn" OR abs:agentic)` | 6 | yes |
| P5q2 | `(abs:instability OR abs:collapse OR abs:unstable) AND abs:"multi-turn" AND (abs:GRPO OR abs:"policy optimization") AND abs:agent` | 27 | yes |
| P5q3 | `abs:"training collapse" AND abs:"reinforcement learning" AND (abs:LLM OR abs:"language model")` | 26 | yes |
| P6q1 | `abs:sandbox AND abs:agent AND (abs:snapshot OR abs:checkpoint) AND (abs:restore OR abs:rollback OR abs:fork)` | 7 | yes |
| P6q2 | `(abs:"copy-on-write" OR abs:CRIU OR abs:microVM OR abs:Firecracker) AND abs:agent AND (abs:LLM OR abs:"language model")` | 9 | yes |
| P6q3 | `(abs:branch OR abs:branching OR abs:fork) AND abs:environment AND abs:state AND (abs:restore OR abs:reset OR abs:snapshot) AND abs:agent AND abs:"reinforcement learning"` | 4 | yes |
| P6q4 | `(abs:rewind OR abs:"roll back" OR abs:rollback OR abs:undo) AND abs:agent AND (abs:environment OR abs:sandbox) AND (abs:LLM OR abs:"language model")` | 23 | yes |
| P7q1 | `(abs:"tool failure" OR abs:"tool failures" OR abs:flaky OR abs:"tool errors") AND abs:agent AND abs:"reinforcement learning"` | 2 | yes |
| P7q2 | `(abs:idempotent OR abs:"fault tolerance" OR abs:"fault-tolerant" OR abs:"fault tolerant") AND abs:rollout AND abs:agent` | 2 | yes |
| P7q3 | `abs:noisy AND abs:reward AND abs:simulator AND abs:error AND abs:agent AND abs:user` | 1 | yes |
| P7q4 | `(abs:"environment noise" OR abs:"noisy environment" OR abs:"unreliable tools" OR abs:"tool reliability" OR abs:"environment failures" OR abs:"environment errors" OR abs:"environment instability") AND abs:agent AND (abs:"reinforcement learning" OR abs:training)` | 16 | yes |
| P7q5 | `(abs:"noisy rewards" OR abs:"reward noise" OR abs:"corrupted rewards" OR abs:"noisy reward") AND abs:agent AND (abs:LLM OR abs:"language model") AND (abs:tool OR abs:environment OR abs:simulator)` | 0 | yes |
| P7q6 | `(abs:attribution OR abs:attribute OR abs:disentangle OR abs:separate) AND abs:failure AND abs:agent AND (abs:environment OR abs:tool) AND abs:"reinforcement learning" AND (abs:LLM OR abs:"language model")` | 10 (none on-topic) | yes |
| P8q1 | `abs:"user simulator" AND (abs:fidelity OR abs:realism OR abs:realistic OR abs:human) AND abs:agent` | 50 (total 62) | too broad |
| P8q1n | `abs:"user simulator" AND (abs:fidelity OR abs:realism) AND abs:agent` | 20 | yes |
| P8q2 | `abs:"user simulation" AND abs:agent AND (abs:"reinforcement learning" OR abs:training OR abs:evaluation) AND (abs:LLM OR abs:"language model")` | 50 (total 64) | too broad |
| P8q2n | `abs:"user simulation" AND abs:agent AND abs:"reinforcement learning" AND (abs:LLM OR abs:"language model")` | 12 | yes |
| P8q3 | `abs:"simulated users" AND abs:agent AND (abs:benchmark OR abs:"tau-bench" OR abs:"τ-bench" OR abs:"customer service")` | 34 | yes |
| P9q1 | `abs:benchmark AND abs:agent AND (abs:"early stopping" OR abs:"subset selection" OR abs:"efficient evaluation" OR abs:"evaluation cost") AND (abs:cost OR abs:expensive)` | 19 | yes |
| P9q2 | `(abs:"confidence interval" OR abs:"confidence intervals" OR abs:variance) AND (abs:agent OR abs:agentic) AND abs:benchmark AND (abs:trials OR abs:runs OR abs:repeated)` | 48 | yes |
| P9q3 | `abs:"efficient evaluation" AND (abs:agent OR abs:agentic OR abs:"tool use")` | 15 | yes |
| P10q1 | `abs:"prediction-powered" AND (abs:LLM OR abs:judge OR abs:evaluation OR abs:"language model")` | 50 (total 172) | too broad |
| P10q1n | `abs:"prediction-powered" AND (abs:LLM OR abs:"language model" OR abs:judge)` | 50 (total 97) | too broad; the total is reported as the wider-field count |
| P10q1nn | `abs:"prediction-powered" AND (abs:agent OR abs:agentic OR abs:trajectories OR abs:"LLM-as-a-judge")` | 31 | yes |
| P10q2 | `(abs:"pseudo-label" OR abs:"pseudo-labels" OR abs:"pseudo labels" OR abs:"synthetic labels") AND (abs:preference OR abs:RLHF OR abs:"reward model") AND abs:human` | 11 | yes |
| P10q3 | `abs:"active learning" AND (abs:preference OR abs:annotation) AND (abs:LLM OR abs:"language model") AND (abs:agent OR abs:RLHF OR abs:"reward model")` | 7 | yes |
| P11q1 | `(abs:offline OR abs:local) AND (abs:corpus OR abs:"search engine") AND abs:"search agent" AND abs:"reinforcement learning"` | 0 | re-run |
| P11q1n | `(abs:offline OR abs:local) AND (abs:corpus OR abs:"search engine" OR abs:wikipedia) AND (abs:"deep research" OR abs:"search agent" OR abs:"web agent" OR abs:"agentic search") AND abs:"reinforcement learning"` | 2 (neither on-topic) | yes |
| P11q2 | `(abs:executable OR abs:runnable OR abs:buildable) AND (abs:repository OR abs:repositories) AND abs:environment AND (abs:construction OR abs:synthesis OR abs:synthesize) AND abs:agent` | 48 | yes |
| P11q3 | `(abs:"world model" OR abs:surrogate OR abs:simulated) AND abs:execution AND (abs:"software engineering" OR abs:coding OR abs:SWE) AND abs:agent AND abs:training` | 50 (total 62) | too broad |
| P11q3n | `(abs:"world model" OR abs:surrogate) AND abs:execution AND (abs:"software engineering" OR abs:SWE OR abs:repository) AND abs:agent AND abs:training` | 2 | yes |
| P12q1 | `(abs:sandbox OR abs:container OR abs:containers) AND (abs:memory OR abs:density OR abs:startup) AND abs:rollout AND (abs:agent OR abs:agentic)` | 14 | yes |
| P12q2 | `(abs:"runtime sharing" OR abs:"copy-on-write" OR abs:"page sharing" OR abs:namespaces OR abs:namespace) AND (abs:environment OR abs:sandbox OR abs:environments) AND (abs:agent OR abs:"reinforcement learning")` | 12 | yes (also surfaced two P6 hits) |
| P12q3 | `(abs:isolation OR abs:sandboxing) AND abs:agent AND (abs:"reinforcement learning" OR abs:training) AND (abs:scalable OR abs:lightweight) AND (abs:environment OR abs:environments)` | 46 | yes |
| P13q1 | `abs:asynchronous AND (abs:staleness OR abs:stale OR abs:"off-policy") AND (abs:RLHF OR abs:RLVR OR abs:"reinforcement learning") AND (abs:LLM OR abs:"language model")` | 28 | yes |
| P13q2 | `(abs:"importance sampling" OR abs:"importance weight" OR abs:"importance weights" OR abs:"importance ratio") AND (abs:stale OR abs:asynchronous OR abs:"off-policy") AND (abs:GRPO OR abs:"policy gradient") AND (abs:LLM OR abs:"language model")` | 23 | yes |
| P13q3 | `abs:rollout AND (abs:"long tail" OR abs:straggler OR abs:stragglers OR abs:"long-tail") AND (abs:LLM OR abs:"language model") AND abs:"reinforcement learning"` | 20 | yes |
| P14q1 | `(abs:"clarifying questions" OR abs:"clarification questions" OR abs:"clarification question") AND abs:agent AND (abs:coding OR abs:"software engineering" OR abs:underspecified OR abs:code)` | 15 | yes |
| P14q2 | `(abs:underspecified OR abs:underspecification OR abs:ambiguous OR abs:ambiguity) AND (abs:agent OR abs:agentic) AND (abs:benchmark OR abs:evaluation) AND (abs:user OR abs:interactive) AND (abs:code OR abs:coding OR abs:"software")` | 50 (total 87) | too broad |
| P14q2n | `(abs:underspecified OR abs:underspecification) AND (abs:agent OR abs:agentic) AND (abs:benchmark OR abs:evaluation) AND (abs:code OR abs:coding OR abs:software)` | 44 | yes |
| P14q3 | `(abs:"human-AI collaboration" OR abs:"human-in-the-loop" OR abs:"human-agent collaboration") AND (abs:coding OR abs:programming OR abs:"software engineering") AND abs:agent AND (abs:evaluation OR abs:benchmark)` | 50 (total 105) | too broad |
| P14q3n | `(abs:"human-AI collaboration" OR abs:"human-agent collaboration" OR abs:"pair programming") AND (abs:coding OR abs:programming OR abs:"software engineering") AND abs:agent AND (abs:evaluation OR abs:benchmark OR abs:study)` | 50 (total 55) | too broad |
| P14q3nn | `(abs:"human-AI collaboration" OR abs:"human-agent collaboration") AND (abs:coding OR abs:"software engineering") AND abs:agent AND (abs:evaluation OR abs:benchmark)` | 33 | yes |

Counting method: for each problem, every returned entry's title and 420-character abstract prefix was
read; an entry counts if it is clearly about the problem as stated (not merely about agents or RL);
entries were grouped by last author where the same last author recurs, by known lab otherwise, and by
first author when neither was clear. Papers from the harvest that appeared in the results were counted
once. The counts are a lower bound on the field and an upper bound on direct competition, since a group
"clearly about" the problem is not necessarily attacking the same gap the records name.

## Section 5 — Membership index

Record ids per problem (A = groupA, B = groupB, C = groupC, zero-based line index in the JSONL). Full
quotes and fields for every record are in `2026-W41-problem-shortlist-members.jsonl`.

- P1 (28): A003 A005 A006 A012 A040 A042 A046 A047 A057 A060 A061 A063 A064 A067 A071 A082 A094 A095 A096 A098 A102 A107 A125 A129 B082 B121 B122 C034
- P2 (29): A000 A001 A002 A004 A024 A066 A072 A073 A079 A080 A099 A100 A101 A104 A105 A137 A143 B033 B042 B061 B072 B083 B091 B093 B141 C007 C021 C064 C067
- P3 (26): A013 A026 A027 A029 A030 A032 A033 A034 A037 A038 A039 A054 A058 A065 A074 A075 A076 A081 A085 A089 A090 A091 A092 A106 A109 A110
- P4 (24): A007 A009 A019 A043 A048 A053 A111 A112 A115 A117 A118 A119 A120 A123 A127 A130 A131 A132 A133 A134 A139 A140 A142 C000
- P5 (10): A045 A055 A056 A084 A086 A097 A124 A136 B118 B128
- P6 (27): A011 A016 A017 A018 A020 A022 A108 A113 A116 C010 C018 C022 C038 C039 C040 C041 C042 C043 C044 C052 C053 C054 C055 C057 C058 C070 C076
- P7 (16): A021 B019 B106 B108 B110 B117 B127 B129 B131 B132 C031 C059 C071 C074 C075 C077
- P8 (27): B000 B006 B007 B008 B009 B010 B011 B014 B015 B016 B026 B028 B029 B030 B031 B055 B056 B092 B096 B098 B100 B107 B109 B123 B125 B134 B150
- P9 (18): B001 B005 B012 B020 B021 B023 B024 B025 B038 B067 B070 B078 B124 B130 B135 B136 B140 B148
- P10 (18): A051 A078 A083 B013 B027 B040 B041 B043 B044 B054 B057 B075 B076 B077 B079 B080 B120 B133
- P11 (13): A052 B086 B087 B089 B090 B116 B126 C002 C005 C008 C009 C016 C032
- P12 (20): C001 C003 C006 C011 C012 C014 C015 C017 C078 C079 C080 C083 C084 C085 C087 C088 C098 C099 C100 C102
- P13 (20): A035 B114 C024 C025 C027 C029 C030 C045 C046 C047 C056 C082 C089 C090 C092 C093 C096 C101 C104 C105
- P14 (10): B002 B052 B053 B085 B097 B105 B152 B153 B154 B155
- unclustered (133): listed with `problem: unclustered` in the sidecar, each with its original problem
  sentence and quote.
