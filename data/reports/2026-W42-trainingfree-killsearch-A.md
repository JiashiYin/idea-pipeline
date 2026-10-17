# Kill search A — training-free scoping of C-W42-02: signal and headroom at the memory-consolidation step

Date: 2026-10-16 (written 2026-10-17 01:20 UTC). Candidate: `C-W42-02` in `data/candidates/2026-W42.jsonl`, scoped to
agents that improve across a task stream by rewriting a text memory (playbook, cheatsheet, lessons, experience bank)
instead of their weights. Checklist: `prompts/checklist.md` (all items run; triggered items in Section 7). Nothing below
is from memory: every paper was fetched today as a PDF from `arxiv.org/pdf/<id>` into
`/tmp/claude-0/-home-claude/684a602a-8772-59ed-8c60-74c4245ab4ea/scratchpad/ks/dl/` (untrusted data), converted with
`pdftotext -layout` into `.../scratchpad/ks/txt/`, and read there; abstracts and the density queries came from
`export.arxiv.org/api/query` (three 429 and two 503 responses between 00:40 and 00:55 UTC; retried after 40 s, 120 s and
60 s waits; density query Q1 failed and was not repeated). Depth marks: [full] = whole text read; [sections] = abstract,
method, results, limitations read with grep-guided reading; [abstract-only] = arXiv API abstract.

**Terms used below (one gloss each).** *Task stream*: the agent meets tasks one after another and carries text between
them. *Consolidation*: the step that rewrites the memory after a task (ACE's Reflector/Curator, Dynamic Cheatsheet's
curator, ReasoningBank's extractor, SkillOS's curator). *Growth run*: one pass of consolidations over a training set
that produces one memory; two growth runs on the same tasks differ in task order and sampling. *SIGNAL C*: variance of
downstream success across independently resampled consolidations of the same history; what an outcome-reward policy
gradient can see at that step. *HEADROOM H*: downstream success with the full raw history, or with an oracle-curated
memory, minus mean success after the self-written consolidation. *Outcome reward*: a scalar from task success only, no
judge of the memory text. *Process reward*: a scalar that scores the memory operation itself (a judge, a verifier, a
rule). *Group-relative RL (GRPO)*: sample a group of outputs for one prompt, reward each, update toward the ones above
the group mean; a group with equal rewards gives a zero update. *Write-time vs read-time curation*: distilling memory
when a task ends (before the next task is known) vs distilling retrieved raw traces when the next task arrives.
*Held-out gate*: accept a rewritten memory only if success on tasks not used to write it does not fall.

## 0. Verdict in one paragraph

**The pair (C, H) is not reported anywhere at the per-consolidation step, but both halves exist in print at coarser
grain and the field has already moved past the question the candidate wants to ask.** (i) RBC (2610.18427, 2026-10-13)
measures the growth-run spread of self-written playbooks (three runs per setting; "82.5, 58.9 and 30.0 against 78.4 with
no playbook") and separates it from evaluation noise ("at most 5.0 points"); its Table 5 lets a reader compute a
run-level C and a curation-oracle H for 11 ACE settings. Its Reflector and Curator run at temperature 0, so under its
own protocol resampling one consolidation of a fixed history would give zero variance by construction: C as defined is a
protocol constant, not a property of the memory step (checklist 2026-10-14). (ii) The learnability question is posed in
the authors' own words by JitMem (2609.27334, 2026-09-23: "the value of a storage decision may only become apparent when
a relevant query arrives, potentially many tasks later, creating a long-horizon credit-assignment problem"), by MetaExp
(2610.21492, 2026-10-15: "Reinforcement learning would therefore require attributing future performance changes back to
earlier execution and reflection decisions") and answered by construction rather than measurement: SkillOS (2605.06614,
Google, 2026-05-07) trains the write-time curator with GRPO using grouped task streams plus three auxiliary rewards; EASE
(2609.36746, 2026-09-29) gates out curation actions with no retrieval incidence and notes "Identical total rewards within
a group yield zero advantages"; Mem-α reports that dropping its judge reward "leads to catastrophic performance
degradation"; TRUSTMEM that "coarse scalar rewards alone are insufficient". No paper reports the fraction of
zero-variance groups or the variance of downstream success across resampled consolidations. (iii) Luck in single-outcome
lessons is named and replication proposed by reSolve (2608.28638: "an evolution-time pass records one lucky trajectory
that a fresh stochastic agent often fails to reproduce"; solve-and-reproduce in a fresh container) and by the held-out
gates of RSEA, PACE, Recuris and Trace Evolution Bench. (iv) The "full raw history" ceiling is below the self-written
memory in the two published arms that have it (Dynamic Cheatsheet FH on AIME: 26.7 vs 50.0 for Sonnet; Mem-α's 32k
long-context baseline 0.588 vs 0.642), so H needs an oracle-curation definition, which RBC's S* already supplies.
**Status recommendation: killed as a measurement-novelty claim; the narrowest survivor in Section 6 is a one-figure
appendix to RBC's released code, not a paper.**

## 1. Paper records (closest first)

Each record: trick; setting; what is measured at the memory step; resampling + downstream variance (signal) yes/no with
quote; full-history or oracle arm (headroom) yes/no with quote; learnability / sparse-signal statement; noise or luck in
single-outcome lessons; verbatim limitation or future-work text; code and data; models and task families; depth.

### 1.1 arXiv 2610.18427 — Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments (Pham, Nguyen, Le, Srey, Luu; NTU and VinUniversity; 2026-10-13) [full]

- **Trick.** Serve each block of self-written lessons at random (in or out, probability one half) on practice tasks, regress
  success on the inclusions to get each block's effect, keep the positive blocks within a token budget, and let fresh
  practice episodes choose among the curated sets, the whole playbooks and no playbook.
- **Setting.** Task stream: training tasks grow a playbook (ACE lesson-by-lesson; Dynamic Cheatsheet whole rewrite), practice
  tasks measure it, evaluation tasks score it. Memory form: a list of lessons served in the prompt.
- **Measured at the memory step.** The effect of each block on success (Banzhaf value: "how much the block raises success,
  averaged over what else is served with it"), the whole-playbook score per growth run, the agent's own helpful/harmful
  tags against the measured effects ("over 81 blocks, ACE's tags and the measured effects have a rank correlation of only
  0.21").
- **Resamples the consolidation and measures downstream variance: YES at growth-run grain, NO at step grain.** "We ran
  three growth runs in each of the eleven ACE settings"; "the same procedure on the same tasks, in another order, can write
  a helpful or a harmful playbook. On 27B AppWorld with per-test feedback, the three runs score 82.5, 58.9 and 30.0
  against 78.4 with no playbook (Figure 2, mixed): one helps, two harm. Such swings occur in 3 of the 6 settings with a
  harmful run, all on Qwen, whose runs differ only in task order and sampling." (§4, Finding 2). Appendix B.2: "the runs
  of one setting lie up to 37.3 points apart (Gemma ALFWorld), and on 9B WebShop one run helps while another harms."
  Evaluation noise is separated: "re-evaluating a playbook moved its score by at most 5.0 points, so such a gap is not
  noise" (§4). Protocol (Table 3 caption): "Actors sample at temperature 0.7, all other roles at 0." Appendix A.1: "Growth
  runs differ in the order of the training tasks and the actor's sampling." So the spread is variance of the *history*
  (trajectories and their order), not of the consolidation of a fixed history; the Reflector and Curator are deterministic
  given their input.
- **Full-history or oracle arm (headroom): PARTIAL.** No arm serves raw trajectories. Two oracle-like arms: Best-Full
  ("serves the best whole playbook or no playbook on practice tasks") and RBC, whose curated set "estimates the best set
  S* of Eq. (1)". Per setting, Table 5 gives the three whole-run scores and the chosen candidate, so a curation-oracle
  headroom is computable: 27B AppWorld per-test, whole runs 82.5/58.9/30.0 (mean 57.1) against RBC 84.3; 27B AppWorld
  pass/fail, whole runs 31.2/17.7/8.7 (mean 19.2) against RBC 77.6, which equals no playbook (78.4) within noise. Pooling
  all runs' lessons is tested and loses (Appendix E.3, Table 11: "Pooled, uncapped" 43.3 against Best-Full 45.2 on four
  development settings; "a playbook's value can lie in its lessons together, which choosing among runs keeps and pooling
  breaks").
- **Learnability / sparse signal.** Not posed as RL. Two measurements bear on it: the self-judge is uninformative (rank
  correlation 0.21 above); the per-lesson signal is below the noise floor at the budgets used ("We measure groups of
  related lessons, as a single lesson rarely moves success beyond the noise of a few hundred episodes", §5.1; Related
  Work: coalition-aware valuation "reports that single-skill knockouts resolve only small effects at a few hundred
  queries"). Appendix E.8: "Task success cannot be replaced by an LLM judge ... the set curated on the judge's estimates
  failed on 27B and 9B AppWorld pass/fail".
- **Noise or luck in single-outcome lessons.** Only through feedback granularity: with pass/fail feedback the Reflector
  "writes rules for an imagined validator; under per-test feedback it sees the failed tests and writes none" (Appendix
  B.1). Environments are deterministic; luck is not discussed.
- **Limitations (verbatim, section "Limitations").** "Our evidence covers two memory systems, three benchmarks and three
  open-weight models, with playbooks we grew; other memory systems, domains and larger or proprietary models remain to be
  tested. Within this scope, RBC values a block by its average gain over the other blocks served with it, which makes
  curation exact when block effects add; when lessons are hard to separate, as in a memory rewritten as a whole, it falls
  back on the best whole playbook, which still lifts success but saves no context. RBC also trades extra episodes for
  reliability: it grows several playbooks, runs practice rounds and needs practice tasks with an observable outcome. Since
  its guarantee holds on these practice tasks, it works best when they resemble the tasks the agent will face. We fixed
  its constants on four ACE settings and kept them unchanged elsewhere. Finally, we study playbooks fixed once grown;
  extending RBC to memory that grows while it is served is a natural next step."
- **Code and data.** `https://anonymous.4open.science/r/rbc` (footnote 1). Cost table: practice round 600–684 episodes per
  run; RBC with K=3 is 3.3–4.1 times the episodes of one curated run.
- **Models and tasks.** Qwen3.8-27B, Qwen3.5-9B, Gemma-4-31B (FP8), thinking off; AppWorld (168 test tasks × 3 seeds),
  WebShop (500 × 3), ALFWorld (134 × 3).

### 1.2 arXiv 2609.27334 — Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents (Zhou, Li, Liu, Yavuz, Joty; Salesforce AI Research; 2026-09-23) [sections]  — found by density query Q4, not on the input list

- **Trick.** Keep every raw trajectory, and when a new task arrives let a curator (trained with GRPO on that task's own
  success) rewrite the retrieved raw traces into a short payload for the frozen executor.
- **Setting.** Task stream (ALFWorld, WebShop, τ²-bench); memory form: raw trajectories in a bank, retrieved by BM25,
  curated at read time.
- **Measured at the memory step.** Downstream success of read-time curation against write-time artifacts (ReasoningBank,
  MemP, SkillOS) with the same curator model, untrained and RL-trained.
- **Resampling / signal: NO.** GRPO groups of 8 payloads per task are the training signal; no variance is reported.
- **Headroom arm: YES, in the target's task families.** Raw history retained plus read-time curation against self-written
  write-time memory: with Qwen3-8B as curator and executor, ALFWorld 77.4 against SkillOS 61.2 and ReasoningBank 55.7;
  WebShop success 32.8 against 16.5; "even an untrained curator is already competitive with or surpasses these baselines"
  (JitMem-base 60.5 on ALFWorld). This is the "full raw history" side of H measured by a stronger reader, not by
  appending.
- **Learnability statement (verbatim, abstract and §1).** "Learning such a write-time curator is also difficult because
  the value of a storage decision may only become apparent when a relevant query arrives, potentially many tasks later,
  creating a long-horizon credit-assignment problem." "This avoids the need to group related tasks to manufacture a
  learning signal, as required by learned write-time curators such as Ouyang et al. (2026a), whose ablations identify
  grouping as a major contributor to performance." §3: "the temporal gap between the curator's action and its reward is
  zero ... In write-time memory, by contrast, a storage decision at step s is graded only when a future task t > s
  retrieves the artifact, possibly many tasks later."
- **Luck.** Not discussed; storage is gated by a success judge ("UPDATE appends ξt only if the judge deems the task
  successfully solved").
- **Limitations (verbatim, §5 Conclusion).** "JitMem has several limitations. The retriever (BM25) is simple and may
  become a bottleneck as the memory bank grows large and diverse. The curator adds an extra LLM call per task. The payload
  format is fixed and hand-designed per benchmark. Future work could jointly optimize the payload format, explore stronger
  retrievers, and extend curation from once per task to turn- or step-level adaptation as new observations arrive."
- **Code.** No link found in the text. **Models and tasks.** Curator Qwen3-8B (GRPO, 100 steps, group size 8); executors
  Qwen3-8B, Gemini-2.5-Pro, GPT-5.4; ALFWorld 140, WebShop 500, τ²-bench.

### 1.3 arXiv 2605.06614 — SkillOS: Learning Skill Curation for Self-Evolving Agents (Ouyang, Yan, Chen, Han, Wang, Dalvi Mishra et al.; Google; 2026-05-07) [sections] — found through JitMem's related work

- **Trick.** Train the curator that edits a skill repository with GRPO, where each training instance is a group of related
  tasks solved in order so that later tasks score the edits made after earlier ones, and the reward adds a judge score of
  the edit, a function-call validity term and a compression term to the downstream success.
- **Setting.** Task stream of grouped tasks; memory form: Markdown skill files in a repo, retrieved by BM25.
- **Reward (verbatim, Eq. 1).** r = r_task + λ_f r_fc + λ_u r_cnt + λ_c r_comp; "we define the task outcome reward as the
  average success over the remaining tasks ... r_task = 1/(|G|−1) Σ_{i=2}^{|G|} 1(ξ_i)"; "Let Judge(c_i) denote the scalar
  score assigned by an external judge (Qwen3-32B)". The success indicator is itself a judge: "outcome signal 1ξt is
  obtained via LLM-as-a-judge with the frozen agent executor".
- **Resampling / signal: training only.** "For each task group G, we sample N independent rollouts of the entire curation
  sequence"; no variance or zero-advantage fraction reported.
- **Headroom arm: NO.**
- **Learnability.** The abstract poses it ("they still struggle to learn complex long-term curation policies from
  indirect and delayed feedback") and the ablation (Table 3, ALFWorld, Qwen3-8B curator and executor) is the only published
  dose-response: full 61.2 success; without the judge reward 58.6; without the compression reward 60.0; without grouping
  57.3. No arm removes all auxiliary rewards.
- **Limitations (verbatim, Appendix D).** "Our current implementation relies on a relatively simple keyword-based
  retrieval mechanism, such as BM25 ... We leave the joint optimization of skill curation and skill retrieval to future
  work." No code link found. Models: Qwen3-8B curator; executors Qwen3-8B and Gemini-2.5-Pro; ALFWorld, WebShop,
  single-turn reasoning tasks; 16 H100.

### 1.4 arXiv 2609.36746 — EASE: Behavior-Adaptive Skill Curation for Self-Evolving Agents (Xiong, Tan; 2026-09-29) [sections] — found by density query Q6

- **Trick.** Train one skill curator with GRPO across several frozen executors, condition it on a running profile of the
  executor's recent behaviour, and update only the curation actions whose edited skill was later retrieved and changed the
  executor's actions.
- **Measured at the memory step.** Which curation actions have any downstream signal. "Gate 1 admits an edit only if Zt >
  0, excluding curation actions with no observed opportunity to influence later execution"; "Removing both gates costs
  4.8 ∼ 6.5 pp ... A random mask with the same admission rate performs on par with ungated training, so the gain comes
  from which curation steps are updated." Appendix: "Executors near a benchmark's floor or ceiling may offer little
  variation in task outcomes ... Identical total rewards within a group yield zero advantages."
- **Resampling / signal: training only;** the admission rate of the gates (the share of curation actions with any
  downstream signal) is logged but not reported as a number in the text I read. **Headroom: NO.**
- **Code.** `https://github.com/Eric2i/EASE`. Models: curator Qwen3-8B; executors Qwen3-8B/32B, GPT-OSS-120B, unseen Kimi
  K2.6, DeepSeek V4 Flash, Gemini 3.5 Flash; ALFWorld, ScienceWorld, WebShop.

### 1.5 arXiv 2610.21492 — MetaExp: Learning to Self-Improve through Experience via Verifiable Cross-Task Environment Scaling (Li, Shen, Su, Tu, Wong, Liu, Yang; UMacau, Alibaba Token Hub, SIAT; 2026-10-15) [sections]

- **Trick.** Build 1,000 families of verifiable tasks that share a tool or a workflow, collect sequential trajectories in
  which the agent solves a task and then rewrites a skill bank, keep the verified ones, and fine-tune Qwen3.5-122B-A10B on
  4,956 of them so that the model writes better experience at deployment with frozen weights.
- **Learnability (verbatim, Appendix C Discussion).** "Why supervised fine-tuning? The environments, tasks, and executable
  verifiers constructed by MetaExp readily support reinforcement learning. However, experience learning introduces a
  delayed cross-episode objective that is more difficult to optimize than task-level reward. An update to the skill bank
  may appear reasonable on the task that produced it, yet its true utility is only revealed when that experience is reused
  on subsequent tasks. Reinforcement learning would therefore require attributing future performance changes back to
  earlier execution and reflection decisions, creating a nontrivial credit-assignment problem. It would also require
  rolling out multiple downstream tasks to evaluate earlier updates, substantially increasing the cost of optimization
  over long sequential task streams. For this reason, we use rejection sampling followed by supervised fine-tuning as a
  practical first step." They write the per-update downstream utility as an equation: Δ_i^exp = S_val(B_i) − S_val(B_{i−1})
  (Eq. 9; S_val is success on held-out family members, B_i the skill bank after update i) and close: "We leave
  downstream-utility-based filtering and reinforcement learning with cross-episode reward signals as promising directions."
- **Resampling / signal: NO. Headroom: NO.** Luck: not discussed. No limitations section beyond Appendix C; no code link
  found. Tasks: SpreadsheetBench (+8.5), APEX-Agents (+2.3), AutomationBench (+14.8).

### 1.6 arXiv 2605.21768 — Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents (Yan, Bahloul, Nie, Schwarzmann, Trivisonno, Tresp, Ma; 2026-05-20) [sections]

- **Trick.** Train a fact extractor and a memory manager with GRPO over multi-session dialogues, and add "local rerollouts":
  re-run one session's memory operations several times from the same cached memory state and compare their downstream QA
  rewards, so that siblings are compared on equal footing.
- **Setting.** Multi-session dialogue → memory bank → QA (LoCoMo), not a task-stream playbook. Reward: token-level F1 of
  answers whose evidence sits in the session, minus a compression penalty (Eqs. 8–10).
- **Resampling the consolidation: YES, as a training signal, variance not reported.** "we choose an anchor rollout i0,
  retrieve the cached memory state immediately before session t, and sample m local rerollouts of session t only. Since
  these rerollouts share the same starting memory state M_{t−1}^{(i0)}, their comparison is not confounded by divergence
  from earlier sessions." (§3.3; N_local = 4, p_local = 0.5.) Motivation: "GRPO still normalizes their rewards within a
  single comparison group, leading to unfair comparisons and biased credit assignment." Evidence that global outcome
  credit is worse at the memory step: Table 2, LoGo-GRPO 49.67 F1 against standard GRPO 46.62.
- **Headroom: NO.** Luck: environment is a fixed transcript; "a weaker answer model would yield noisy reward signals that
  conflate memory quality with answer-model limitations" (fixed GPT-OSS-120B answer agent).
- **Limitations (verbatim, Appendix D).** "Our study focuses on long-horizon text-only multi-session dialogue, where
  memory is constructed from conversational turns and evaluated through downstream QA. Extending the same training
  paradigm to multimodal settings, such as image-grounded dialogue, video memory, or embodied interaction, remains
  unexplored. While the proposed credit-assignment framework is in principle agnostic to the modality of memory content,
  its practical effectiveness in richer environments still requires further investigation."
- **Code.** "The code is available for access via this repository" (footnote; no URL in the text layer). Models
  Qwen2.5-7B-Instruct (also 3B); VERL; LoCoMo 2:1:7 split; OOD LongMemEval, MSC, MemBench.

### 1.7 arXiv 2610.21147 — All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents (Wang, Lin, Qiao, Li, Xu; 2026-10-15) [sections]

- **Trick.** Compile a long history into source-linked events, let one policy decide to search, write, skip or stop over
  that event bank, score every action with a trained process reward model (SFT on evidence coverage plus trajectory-level
  DPO), and optimize the policy with DAPO on the aggregated process scores.
- **Setting.** Long-context QA (LoCoMo, MemoryAgentBench, PersonaMem); single-episode memory construction, no task stream.
- **Why process rewards (verbatim, §1).** "existing supervision is largely outcome-centered: it assigns rewards to the final
  answer but provides little process-level credit for the intermediate memory operations that produced it. As a result,
  trajectories with the same final-answer score may still differ substantially in evidence relevance, memory
  faithfulness, redundancy control, and stopping sufficiency; answer correctness alone cannot reliably evaluate the
  semantic quality of memory operations." This is a motivation, not a measurement: Table 2 ablations remove components of
  the reward model (w/o Evid. SFT −3.1, w/o Traj. DPO −2.2), none replaces the process reward with an outcome-only reward.
- **Resampling / signal: NO. Headroom: NO.** Luck: not discussed. No limitations section ("Work in progress"); "we will
  release our code on GitHub". Models Qwen3-8B reward model, Qwen3-4B policy.

### 1.8 arXiv 2606.25161 — TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory (Yang, Paul, Srinivasan, Kulkarni, Chappidi; 2026-06-23) [sections]

- **Trick.** A frozen LLM verifier scores each memory transition (old memory, chunk, new memory) for coverage, corruption
  and hallucination; GRPO uses the score as part of the reward and also ranks the best against the worst transition in
  each group with a DPO-style loss.
- **Setting.** Chunk-stream memory construction for QA (Mem-α training pool; LoCoMo, LongMemEval, MemoryAgentBench, HaluMem).
- **Learnability (verbatim).** §1: "Most training paradigms rely on terminal scalar rewards ... These global signals are
  too coarse to pinpoint exactly when or where a faulty memory update occurred within a long sequence of updates." §4.6:
  "Both methods improve in the early stage, suggesting that task-level rewards can learn basic memory-editing behaviors.
  However, the variant without transition-ranked optimization later becomes unstable and shows a sharp drop in both task
  and total rewards ... This indicates that coarse scalar rewards alone are insufficient for reliable memory
  consolidation." Ablation: without the verifier reward 58.7 against 66.3 overall. No arm is outcome-only (Ract, Reff,
  Rtype stay).
- **Resampling / signal: NO** (variance across the 8 GRPO rollouts not reported). **Headroom: NO.** Luck: no.
- **Limitations (verbatim).** "A key limitation of TRUSTMEM is that our current experiments mainly focus on text-based
  long-term memory benchmarks. However, in real-world agent applications, user inputs and memory evidence are often
  multimodal ... We plan to extend our framework to multimodal memory agents and vision-language models". No code link
  found. Qwen3-4B, 32 H100 for two days.

### 1.9 arXiv 2610.19910 — When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents (Yu et al.; JD Future Academy, CASIA, UCAS, Exeter, Tsinghua; 2026-10-14) [sections]

- **Trick.** Run three skill-evolution methods (ACE, SkillOpt, RethinkSkill) on six benchmarks with one of four
  perturbations injected at one point of the learning loop (instruction, evidence, execution record, outcome–record
  pairing), freeze the skill store, and score it on clean held-out tasks.
- **Noise and luck (verbatim).** Abstract: "noisy learning retains only 25.5%–42.1% of the aggregate gain achieved by
  clean self-evolution, depending on the noise type" (six-benchmark macro-average, three runs). N-Bind pairs "an outcome
  ... with another attempt's record"; Appendix G.5: "The interface gives it no way to question the pairing itself, so it
  instead constructs an explanation for a failure that never happened and writes that explanation down as a rule ... If
  that round happens to pass validation, the invented rule is deployed and retrieved repeatedly thereafter, and a one-off
  perturbation of the binding has been converted into a persistent false prior." §5.4: "Validation assesses each candidate
  update as a whole, providing limited evidence about the contribution of individual clauses." Noise is injected, not
  natural luck; environments are deterministic ("the same action sequence yields the same verdict").
- **Resampling / signal: pipeline-level only.** Table 13 gives mean±SD over "three independent runs of the complete
  evolution and evaluation pipeline" (ACE, SpreadsheetBench, DeepSeek-V4.1-Flash, clean: 90.00±0.00; RethinkSkill,
  GPT-5.2, N-Bind: 39.17±4.02). Protocol (Table 5): DeepSeek-V4.1-Flash actor and optimizer at temperature 0; GPT models at
  provider default. The DeepSeek SDs are therefore serving noise, not consolidation variance. Trace Evolution Bench
  (2610.15055, abstract) gives the matching noise floor: a frozen policy "moves 7.5, 5.0, and 12.5 percentage points
  across three seeds" on 40 held-out tasks.
- **Headroom: NO.** Replication proposed: NO. No limitations section; conclusion only. Code
  `https://github.com/yutao1024/RSEClaw`, data `https://huggingface.co/datasets/Kirito-Lab/RSE-Bench`. Models GPT-5.2,
  GPT-5.5, DeepSeek-V4.1-Flash; SpreadsheetBench, SP/MP-DocVQA, ALFWorld, SkillFlow, ContinualSkillBench.

### 1.10 arXiv 2510.04618v3 — Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (Zhang et al.; ICLR 2026; v1 2025-10-06, v3 2026-03-29) [sections]

- **Trick.** Instead of letting one model rewrite the whole context, a Reflector writes short lessons from each trajectory
  and a Curator appends them as tagged bullets with helpful/harmful counters, deduplicating by embedding, so the context
  grows without being rewritten.
- **Context collapse (verbatim, §2.2).** "In a case study on the AppWorld benchmark, we observe a phenomenon we call
  context collapse, which arises when an LLM is tasked with fully rewriting the accumulated context at each adaptation
  step. As the context grows large, the model tends to compress it into much shorter, less informative summaries, causing
  a dramatic loss of information. For instance, at step 60 the context contained 18,282 tokens and achieved an accuracy of
  66.7, but at the very next step it collapsed to just 122 tokens, with accuracy dropping to 57.1—worse than the baseline
  accuracy of 63.7 without adaptation." One run, one benchmark, Dynamic Cheatsheet as the rewriter. §3.2: incremental
  updates "avoid the potential variance introduced by monolithic context rewriting" (asserted, not measured).
- **Resampling / signal: NO. Headroom: NO** (no raw-history arm; GT-label vs no-GT arms only). Noise: Appendix A.4 injects
  a harmful reflector every X steps (FiNER; stays above base except when injected every step).
- **Limitations (verbatim, §5).** "A limitation of ACE is its reliance on a reasonably strong Reflector: if the Reflector
  fails to extract meaningful insights from generated traces or outcomes, the constructed context may become noisy or even
  harmful. In domain-specific tasks where no model can extract useful insights, the resulting context will naturally lack
  them. This dependency is similar to Dynamic Cheatsheet, where the quality of adaptation hinges on the underlying model's
  ability to curate memory." §4.4: "when ground-truth supervision or reliable execution signals are absent, both ACE and DC
  may degrade in performance. In such cases, the constructed context can be polluted by spurious or misleading signals".
- **Code.** `github.com/ace-agent/ace`. Models DeepSeek-V3.1-671B, GPT-OSS-120B, GPT-5.1, Llama-3.3-70B; AppWorld, FiNER,
  Formula, medical reasoning, text-to-SQL.

### 1.11 arXiv 2504.07952 — Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory (Suzgun, Yuksekgonul, Bianchi, Jurafsky, Zou; 2025-04-10) [sections]

- **Trick.** After each query the model rewrites one cheatsheet of strategies and code snippets, judging success itself,
  and reads it on the next query; a retrieval variant also pastes the three most similar past input–output pairs.
- **Headroom arm: YES (full-history appending), and it is below the self-written memory.** "Full-History Appending (FH).
  This is a naive approach that appends the entire conversation history to the model input without any curation or
  truncation" (tested only on AIME 2024/2025, 30 questions each). Table 2: Claude 3.5 Sonnet AIME 2024, BL 23.3, FH 26.7,
  DC-Cu 50.0; GPT-4o AIME 2024, BL 20.0, FH 13.3, DC-RS 40.0. The §4.3 text reads "GPT-4o managed a baseline of 20.0% but
  fell to 6.7% using FH, in direct contrast to 40.0% with DC-RS", while its Table 2 lists FH at 13.3 (2024) and 3.3 (2025);
  the direction is the same in both.
- **Resampling / signal: NO.** Single runs; no seeds. Collapse mechanism named: "the model merely references or
  abbreviates the existing memory (e.g., 'Previous content [...] preserved') instead of explicitly rewriting it. Such
  truncated memory updates can reduce the quality of stored heuristics over time." Luck: "faulty heuristics that slip into
  memory can be equally amplified."
- **Limitations.** No section; §5 "Additional Analyses and Discussions" plays the role (smaller models "show limited gains";
  "memory curation cannot yield substantial gains" without "sufficiently accurate and efficient base solutions"). Code
  `github.com/suzgunmirac/dynamic-cheatsheet`. Models Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Claude 3.5 Haiku; AIME, GPQA
  Diamond, Game of 24, equation balancing, MMLU-Pro.

### 1.12 arXiv 2509.25140v2 — ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (Ouyang et al.; Google; 2025-09-29) [sections]

- **Trick.** After each task an extractor (same model, temperature 1.0) writes up to three short memory items from the
  trajectory, labelled success or failure by an LLM judge, and later tasks retrieve items by embedding similarity; MaTTS
  samples k trajectories per task and asks the model to contrast them before writing memory.
- **Replication before consolidation: YES in a weak form (MaTTS parallel scaling).** "By comparing and contrasting
  (self-contrast) across different trajectories, the agent can identify consistent reasoning patterns while filtering out
  spurious solutions. This process enables more reliable memory curation from multiple trials of a single query" (§3.3).
  WebArena overall, Gemini-2.5-flash: no memory 40.5, ReasoningBank 48.8, +MaTTS (k=5) 51.8.
- **Outcome label's share of the memory's value (judge-noise study, §5).** Judge accuracy against ground truth 72.7%;
  simulated judge from 100% to 50% accuracy moves WebArena-Shopping success from 50.6 to about 47.6–48.7 against 39.0 with
  no memory: "the judge's accuracy does not significantly impact the performance". So in this setting under three of
  roughly ten points of the memory's gain depend on the outcome label being right.
- **Resampling / signal: NO. Headroom: NO** (baselines Synapse and AWM are trajectory or workflow memories, not full
  history). **Future work (verbatim, Appendix D).** "Learning-based routers and consolidation policies could also automate
  this process." **Limitations (verbatim, Appendix E).** "Dependence on LLM-as-a-judge for correctness signals. In our
  implementation, success and failure signals for trajectories are determined by an LLM-as-a-judge. While this automatic
  labeling enables scalable evaluation without ground-truth feedback, it may introduce noise when tasks are ambiguous or
  when the judge model itself errs." Code `https://github.com/google-research/reasoning-bank`. Models Gemini-2.5-flash/pro,
  Claude-3.7-sonnet; WebArena, Mind2Web, SWE-Bench-Verified.

### 1.13 arXiv 2508.19828v5 — Memory-R1 (Yan et al.; 2025-08-27) and arXiv 2509.25911 — Mem-α (Wang, Takanobu, Liang, Mao et al.; 2025-09-30) [sections]

- **Memory-R1 trick.** A memory manager picks ADD/UPDATE/DELETE/NOOP for each extracted fact and an answer agent filters
  retrieved memories; both are trained with PPO or GRPO on exact-match answer correctness. Reward (verbatim): "We use an
  outcome-driven reward: the Memory Manager's operations are judged by their effect on downstream QA ... R_answer =
  EM(y_pred, y_gold)". Sparsity statement (Limitations, verbatim): "we train the Memory Manager and Answer Agent separately
  to ensure stability under sparse rewards. This separation is necessary but makes the process less straightforward." 152
  training QA pairs; LLaMA-3.1-8B-Instruct, Qwen-2.5 3B/7B/14B; LoCoMo, MSC, LongMemEval. No variance, no headroom.
- **Mem-α trick.** A 4B model learns with GRPO which of core/episodic/semantic memory tools to call on each chunk; reward r
  = r1 + r2 + βr3 + γr4 (QA correctness, tool-call format, compression, judge-scored memory content). Sparsity evidence
  (verbatim, §4.4): "the memory content reward (γ) proves critical for effective learning: setting γ = 0 leads to
  catastrophic performance degradation, as the model fails to acquire meaningful memory construction strategies". Headroom
  arm: "Long-Context" (Qwen3-32B with 32k window) scores 0.588 against Mem-α 0.642 on validation (Table 3 and §4.3), so the
  full history is below the learned memory here too (different reader model, so not a clean comparison). Code uses verl;
  Qwen3-4B on 32 H100. Future work: integration with MIRIX; real databases.

### 1.14 arXiv 2609.34649 — Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses (Li, Xu, Chen, Wang, Liang, Liang, Yang; Fudan; 2026-09-28) [sections]

- **Trick.** Evolve the harness's context-management code and prompts (what enters the prompt, how history is kept, how
  sub-contexts are shared) from failed trajectories, using cross-case evidence and counterfactual replay at single decision
  points to decide whether context management caused a failure.
- **Relation to the target.** One level up: it edits the compaction *policy*, not a memory. Its replay is the mechanism of
  C at one decision: "hold the execution prefix τ<t fixed and modify only the model-visible context at decision t ... We
  then compare samples from the original and modified contexts" (Eq. 4; at most five samples per condition).
- **Limitation (verbatim, §7).** "Cross-case evidence supports an attribution hypothesis, bootstrap evidence can justify a
  bounded update, and decision-point replay measures only local next-action sensitivity. These forms of evidence do not by
  themselves establish a task-level causal reward contribution for an individual policy mechanism." No variance of task
  success across resampled contexts; no headroom. Models DeepSeek-V4-Flash, GPT-5.6-Luna; LHTB (46), DeepSWE (113),
  BrowseComp-Plus hard174. Code: Pi-agent harness named; no repo link seen.

### 1.15 Abstract-plus-limitations reads

- **2609.33717 SELFSUITE (Asgari, Kiciman, Nunes, Chandra; Microsoft; 2026-09-27) [sections].** The agent writes its own
  evaluation suite, freezes it, and uses it to gate a keep-best retry and an outcome-tagged memory; five repeats per cell.
  Relevant measurements: "a best-attempt oracle gap remains as headroom" (retry selection, 7.4 pp on average); "Fresh
  suites differ from repeat to repeat, so part of the reported variance is design variance"; "Five repeats bound effects
  of about ±4 pp on a 50-task cell"; the value of the outcome label to the memory writer: "experience that was graded by
  someone who knew the answer is worth more than the same experience self-graded" (+2.8 pp overall, +6.4 on tau2, "not
  significant with five repeats"); "a warm playbook that kept adapting label-free lost 3.2 pp on tau2 relative to the same
  playbook frozen". Limitations verbatim: "The judge, the brief grounder, the memory ranker and the agent are the same
  model; decomposition, grounding and state read-back reduce but do not remove self-evaluation circularity". GPT-5.5,
  Opus-4.8; tau2-bench, AppWorld.
- **2610.19581 XferAgent (2026-10-14) [abstract + Limitations].** Local and shared experience graphs for transfer between
  heterogeneous agents. Limitations: privacy of shared experience, text-only, "Separating source and evaluation tasks does
  not rule out semantic overlap or exposure during model pretraining." Nothing on variance, headroom or learnability.
- **2610.19386 STRATA (NJIT, CUHK-Shenzhen; 2026-10-14) [abstract + Conclusions].** Three-layer typed experience graph
  with forgetting and "contrast edges" that warn about direction-opposite memories. Future work verbatim: "Our results use
  a single model family (DeepSeek-V4) and should be replicated across backbones"; "a controlled study that fixes the
  evaluation set and varies only the number of accumulated experiences would separate scale from difficulty, which our
  benchmark-level comparisons cannot." Nothing on C or H.
- **2606.08656 MemoPilot (Cai et al.; Zhipu AI, Tsinghua; 2026-06-07) [sections].** Trains a memory copilot with multi-turn
  GRPO to update a frozen player's memory between games of Rock-Paper-Scissors and Limit Hold'em; reward is the next
  game's outcome. On signal: "Using long-horizon returns would couple the learning signal to future stochasticity (e.g.,
  different dealt hands), amplifying environment noise and making credit assignment unstable. The one-step proxy avoids
  this issue". Qwen2.5-14B-Instruct; toy games, not agentic tasks.
- **2608.28638 reSolve (Liu et al.; 2026-08-10) [sections].** Per-task skill evolution with a surrogate verifier and
  "solve-and-reproduce": the authored skill package is re-executed in a fresh container before a pass is credited. Luck,
  verbatim: "An evolution-time pass therefore records a single successful trajectory, and that success need not recur when
  a fresh agent later reads the skill and re-derives the answer. We call this shortfall the reproduction gap ... current
  self-evolution frameworks ... reward a candidate skill for producing a solution trace once, not for reproducing the
  solution when re-executed." SkillsBench (86 tasks), DeepSeek-V4-Pro, mean-of-3 deployment trials.
- **Abstract-only (API), one line each.** 2606.28374 RSEA (2026-06-17): a rewritten memory is committed "only if it does not
  regress on a disjoint held-out split"; "unguarded context evolution is high-variance and unsafe. Dynamic Cheatsheet ...
  collapses on WebShop, with a score of 0.14 compared with 0.43 for ReAct." 2606.08106 PACE (2026-06-06): "keep it if the
  score went up" against a noisy dev set "is uncontrolled adaptive multiple testing"; a paired anytime-valid commit test;
  greedy "commits 30–42% false and 10–33% harmful edits" (Qwen2.5 0.5B–3B, prompt-level). 2610.15055 Trace Evolution Bench
  (2026-10-10): no-evolve seed drift of 7.5–12.5 points on 40 tasks; held-out identifiers never enter the update.
  2609.24144 Luck Is Not Skill (2026-09-21): paired rollouts in group-relative RL "need not reduce gradient variance".
  2607.21106 AttriMem (2026-07-23): outcome rewards "cannot identify which intermediate memory contents support the final
  answer, creating a fine-grained credit-assignment bottleneck". 2605.00702 MemCoE (2026-05-01): "sparse outcome rewards
  provide weak supervision, resulting in unstable long-horizon optimization". 2608.22610 coalition-aware skill reliability
  (2026-08-23): "coalition-conditioned reliability modeling reduces sensitivity to noisy outcome-reward fluctuations during
  reinforcement learning". 2607.24300 (2026-07-27): "self-assigned scores can remain near perfect while real deployment
  performance degrades or stays low". 2610.22273 Librarian Agents (Kumar group; 2026-10-15): RL on a builder that curates a
  workspace "to directly maximize downstream answering accuracy" (single corpus, +33 points on BrowseComp-Plus).
  2608.24876 Recuris (2026-08-25): "validation-gated updates to Skill Memory". 2608.04562 SkillSV: "a rollout-budgeted
  estimator for noisy agent evaluations" for per-unit skill value.

## 2. Q1 — Is the signal/headroom pair at the consolidation step measured anywhere?

**No paper reports Var over resampled consolidations of a fixed history, and no paper names the pair.** What exists:

- *Signal at growth-run grain (history and order resampled, consolidator deterministic).* RBC Table 5, 11 ACE settings × 3
  runs, plus Figure 7 for 8 Dynamic Cheatsheet settings, with evaluation noise bounded at 5.0 points. The spread is large
  (range 52.5 points on 27B AppWorld per-test; "up to 37.3 points apart" on Gemma ALFWorld) and it is a property of the
  trajectories and task order because "Actors sample at temperature 0.7, all other roles at 0."
- *Signal at pipeline grain (everything resampled or nothing, depending on backbone).* RSE-Bench Table 13 (three runs,
  SD 0.00–4.02 on 80 tasks; DeepSeek rows at temperature 0 for both actor and optimizer). SELFSUITE (five repeats, "±4 pp
  on a 50-task cell"; evaluator "design variance" named). Trace Evolution Bench (no-evolve drift 5.0–12.5 points on 40 tasks).
- *Signal used as a gradient but not reported.* Memory-R2 local rerollouts (m=4 from a shared memory state); SkillOS and
  EASE GRPO groups of 8 curation rollouts; EASE's gates exist because many curation actions have no downstream signal
  ("Identical total rewards within a group yield zero advantages"); the admission rate is not printed.
- *Headroom.* Full-raw-history arms exist in Dynamic Cheatsheet (FH, AIME only, below the self-written memory) and Mem-α
  (32k long-context reader, below the learned memory). Raw-history-plus-reader is JitMem (+16.2 ALFWorld, +16.3 WebShop
  over the best write-time memory with the same 8B model). Curation-oracle headroom is RBC (curated or chosen set against
  the mean whole playbook; e.g., 84.3 against 57.1 on 27B AppWorld per-test). SELFSUITE's "best-attempt oracle" is the
  retry-level analogue.

So the candidate's sentence "nobody measures this pair at the memory step" is true only with "per-consolidation, same
history" inserted, and under the dominant protocol (consolidator at temperature 0) that quantity is zero by construction.

## 3. Q2 — Is the outcome-reward learnability question posed, and is there evidence either way?

**Posed, in print, by three groups; answered by fixes, not by a measurement of signal.**

- Posed: JitMem (Salesforce, 2026-09-23) and MetaExp (Alibaba/UMacau, 2026-10-15) in the words quoted in 1.2 and 1.5;
  SkillOS (Google, 2026-05-07): "they still struggle to learn complex long-term curation policies from indirect and
  delayed feedback"; EASE (2026-09-29): curation "introduces noisy supervision, especially when an edited skill is never
  retrieved again".
- Evidence that outcome-only is not enough, all indirect: SkillOS without its judge reward loses 2.6 points and without
  grouping 3.9 (ALFWorld, Qwen3-8B); EASE's gates are worth 4.8–6.5 pp and a random mask of the same size is worth nothing;
  Mem-α without the judge reward is "catastrophic"; TRUSTMEM's scalar-only variant "later becomes unstable and shows a
  sharp drop"; Memory-R2's global GRPO is 3.05 F1 below local rerollouts; Memory-R1 trains two agents separately "to ensure
  stability under sparse rewards". None of these arms is outcome-only in a task stream: each keeps a format or compression
  term, and in SkillOS and ReasoningBank the "outcome" is itself an LLM judge (72.7% accurate in ReasoningBank's
  calibration), so the judge/critic confound of the checklist applies.
- Evidence on the other side: Librarian Agents (Kumar group, 2026-10-15) trains a workspace builder on downstream answer
  accuracy alone and gains 33 points on BrowseComp-Plus, in a single-corpus setting where the reward is immediate; JitMem
  trains a read-time curator on immediate task success alone and gains 16 points. MemoPilot trains a memory writer on
  next-game outcome alone in toy games. So outcome reward trains the *writing* step wherever the reward is immediate; the
  open part is the delayed, cross-task case, which SkillOS and EASE make immediate by grouping and gating.
- Nobody reports zero-variance group fractions, all-equal-reward batches, or the share of consolidation steps whose
  downstream effect clears the Monte Carlo floor. RBC's "a single lesson rarely moves success beyond the noise of a few
  hundred episodes" is the closest sentence and it is about measurement, not training.

## 4. Q3 — Does any paper measure luck contamination of lessons and propose replication before consolidation?

**Replication before consolidation is proposed in three forms; luck contamination is named but not measured as a share
of lessons.** reSolve re-executes the frozen skill package in a fresh container before a pass is credited and names the
"reproduction gap" (per-task skills, hidden-test oracle). ReasoningBank's MaTTS samples k trajectories of the same task
and writes memory by self-contrast ("filtering out spurious solutions"). RSEA, PACE, Recuris and Trace Evolution Bench
gate each rewritten memory on held-out tasks (RSEA: "commits a candidate only if it does not regress on a disjoint
held-out split"; PACE: a paired sequential test because greedy acceptance "commits 30–42% false ... edits"). RSE-Bench
shows what one mis-paired outcome does to a lesson ("a one-off perturbation of the binding has been converted into a
persistent false prior") but injects the error rather than measuring natural luck. No paper counts how many lessons in a
playbook were written from a trajectory whose outcome would not replicate, and in ALFWorld, AppWorld and WebShop the only
randomness is the actor's own sampling (RSE-Bench: "the same action sequence yields the same verdict"; checklist
2026-10-08 on deterministic sandboxes), so "luck" there means "the policy's sampling", not the environment.

## 5. Q4 — The two closest papers' limitation text, verbatim

- **RBC, 2610.18427, section "Limitations" (2026-10-13):** quoted in full in 1.1. The sentence that leaves the question open:
  "Finally, we study playbooks fixed once grown; extending RBC to memory that grows while it is served is a natural next
  step." Nothing in the section mentions resampling the consolidation, outcome-reward training, or a raw-history arm.
- **MetaExp, 2610.21492, Appendix C "Discussion" (2026-10-15):** quoted in full in 1.5. The sentence that leaves it open: "We
  leave downstream-utility-based filtering and reinforcement learning with cross-episode reward signals as promising
  directions for further improving meta-experience learning." They write Δ_i^exp = S_val(B_i) − S_val(B_{i−1}) as Eq. 9:
  the group (Alibaba Token Hub, UMacau, SIAT) has 1,000 verifiable task families, held-out family members, and a 122B
  MoE fine-tuning stack; the checklist's re-open test (ask them) applies.
- Third, because it is the closest in task family: **JitMem, 2609.27334, §5 (2026-09-23):** quoted in 1.2; the open sentence
  is "extend curation from once per task to turn- or step-level adaptation". JitMem's abstract already states the
  write-time credit-assignment problem the candidate wants to measure, and sidesteps it.

## 6. Q5 — Narrowest surviving version, and the one result that kills it

**Survivor (two sentences).** Using RBC's released code, models and three benchmarks, hold the trajectory history fixed at
each consolidation step of one ACE growth run, resample the Reflector+Curator output 8 times at temperature 0.7 (the
protocol choice that makes C non-zero), continue 4 episodes per sample, and report per step (a) between-consolidation
variance of downstream success net of the within-consolidation floor and (b) the gap to RBC's measured-curation oracle
S*; the deliverable is the fraction of consolidation steps whose signal clears the Monte Carlo floor at GRPO group size 8,
which is the quantity SkillOS, EASE and MetaExp assume without printing. It is an appendix figure to RBC, not a paper, and
its "why now" is RBC's code release on 2026-10-13 and EASE's on 2026-09-29.

**The result that kills it.** EASE's gate statistics: its code logs, per curation action, whether the edited skill was
ever retrieved (Gate 1) and whether it changed executor behaviour (Gate 2); if the admission rates in its runs (ALFWorld,
WebShop, Qwen3-8B curator) are already the zero-signal fraction, the survivor is a re-plot of an existing log, cost
about one GPU-hour to confirm. Second kill: if the between-consolidation variance at every step is within RBC's 5.0-point
re-evaluation noise with m=8 and n=4 (about 32 episodes per step, far below RBC's 600-episode practice rounds), the map has
no resolved cells and the candidate's own kill condition "C below Monte Carlo noise floor at affordable m,n everywhere"
fires.

## 7. Checklist items triggered, and new lessons

**Triggered.**
- *2026-10-09 "nobody has done X" must cite the two closest papers' own limitation text.* Done (RBC, MetaExp, JitMem). The
  candidate record's note "no public benchmark reports variance of downstream success across independently resampled
  summaries" came from a research-tool report; RBC's Table 5 and RSE-Bench's Table 13 are run-level versions of it.
- *2026-10-16 landscape report is a harvest, not a kill search.* The input list of 15 papers missed the four closest
  neighbors (SkillOS, JitMem, EASE, MemoPilot) and the replication papers (reSolve, PACE, RSEA, Trace Evolution Bench); the
  API density queries with mechanism words found them: Q2 (memory construction + outcome/process reward + credit) 13
  in-window hits; Q4 (full history / oracle / raw trajectories + memory agent) 46; Q5 (self-evolving + held-out/validation
  gate) 200 fetched of 395; Q6 (reflector/curator/memory manager + RL) 175 in-window. The field's words for the candidate's
  "learning the consolidation step" are "learned write-time curator", "skill curator", "memory manager", "read-time curation".
- *2026-10-14 protocol check for any variance claim.* RBC: Reflector and Curator at temperature 0, actors at 0.7, so
  growth-run spread is history variance; RSE-Bench: DeepSeek actor and optimizer at 0, so its SDs are serving noise;
  ReasoningBank: extractor at 1.0; SkillOS/EASE/JitMem: curator sampled in GRPO groups of 8. C as defined is set by the
  consolidator's temperature.
- *2026-10-08 deterministic sandboxes.* ALFWorld, AppWorld, WebShop, SpreadsheetBench are deterministic; any "luck" claim
  about lessons must say "actor sampling" (RSE-Bench Appendix D quote).
- *Premise numbers carry the source's category and denominator.* Used throughout ("noisy learning retains only
  25.5%–42.1% of the aggregate gain achieved by clean self-evolution", six-benchmark macro-average, three runs; "falls up to
  69.6 points below no playbook", one growth run of eleven ACE settings).
- *Judge and critic are different objects.* The "outcome reward" in SkillOS and ReasoningBank is an LLM judge; in Memory-R1
  and JitMem it is exact match or the benchmark metric. Any learnability claim must say which.
- *Competitor writes the target quantity as an equation and calls it future work.* MetaExp Eq. 9 (Alibaba Token Hub,
  UMacau, SIAT; Qwen3.5-122B-A10B; 2026-10-15). Also Memory-R2's local rerollout advantages (Eq. 15) are the C mechanism as
  a gradient (Yan, Bahloul, Nie, Schwarzmann, Trivisonno, Tresp, Ma; Qwen2.5-7B; 2026-05-20).
- *First measurement names a benchmark: confirm runnable.* RBC code (anonymous.4open.science/r/rbc), EASE
  (github.com/Eric2i/EASE), ACE (github.com/ace-agent/ace), Dynamic Cheatsheet, ReasoningBank
  (github.com/google-research/reasoning-bank), RSE-Bench code and data are public; SkillOS, JitMem, AiO-Mem ("we will
  release"), TRUSTMEM, MetaExp show no link in the text read.
- *Abstract-only reading gives false "unposed" verdicts.* MetaExp's RL discussion is in Appendix C only; EASE's
  zero-advantage sentence is in an appendix; JitMem's is in the abstract. Two of the three would have been missed at
  abstract depth.
- *Why now.* The enabling pieces are RBC's randomized-inclusion code (2026-10-13) and EASE's gated curator-RL stack
  (2026-09-29); Google (SkillOS, ReasoningBank) and Salesforce (JitMem) have the stacks and have not printed the variance;
  per the checklist, "they have the stack" is a guess about priorities, not evidence.

**New lessons (proposed additions to `prompts/checklist.md`, dated 2026-10-16).**
1. For any claim about variance *of a consolidation, summary or rewrite*, record each cited system's temperature for the
   writer role separately from the actor role before quoting its run-to-run spread; a deterministic writer makes the
   spread a property of the inputs, and the candidate's quantity zero.
2. "Full raw history" is not an upper bound for memory agents: two published arms (Dynamic Cheatsheet FH on AIME; Mem-α
   long-context) put it below the self-written memory. Define headroom against a measured-curation oracle (RBC's S*) or a
   stronger reader of the raw history (JitMem), and say which.
3. When a candidate's "nobody measures" came from a tool's landscape report, run the API with the field's role words
   (curator, reflector, memory manager, write-time, read-time, held-out gate, reproduce) before the vocabulary of the
   candidate; here four of the six closest neighbors carried none of the candidate's words.
4. For task-stream memory papers, record whether the "outcome" reward is a benchmark verifier or an LLM judge, with the
   judge's measured accuracy when given (ReasoningBank: 72.7%); a learnability claim about outcome reward does not transfer
   between the two.

## 8. Decisions only Jacob can make

1. Accept the kill of the measurement-novelty claim for the training-free scoping, or keep the Section 6 survivor as a
   one-week appendix experiment on RBC's code (cost: about 11 settings × 10 consolidation steps × 32 episodes ≈ 3,500
   AppWorld/ALFWorld episodes on a 9B–27B model; under one GPU-week) whose main value is a number the field assumes.
2. Whether to ask the MetaExp authors (Eq. 9 is the target's H as an equation) and the EASE authors (gate admission rates
   are the target's zero-signal fraction) before spending any compute; both answers could close the question by email.
3. Whether the compaction-summary scoping of C-W42-02 (the original record) should be re-run through this same kill
   search with the four new neighbors (JitMem's read-time argument transfers directly to handoff briefs).
