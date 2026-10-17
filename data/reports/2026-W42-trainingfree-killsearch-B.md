# C-W42-02 — kill search B: density, precedents, pilot feasibility (training-free / context-level scoping)

Date: 2026-10-16. Agent: density/precedents/feasibility (sibling agent reads the closest papers in full; this
report does not). Target under kill search: at the memory-consolidation step of agents that improve by editing
their own text memory (playbooks, cheatsheets, reflections, experience banks), measure SIGNAL = variance of
downstream performance across resampled consolidations of the same history, and HEADROOM = performance with the
full raw history (or an oracle memory) minus performance with the self-written memory; question: can the
memory-writing step be learned from outcome reward alone?

Sources: arXiv API (`export.arxiv.org/api/query`, HTTPS, 3 s pause, `max_results=100`, sorted by submittedDate,
`submittedDate:[20251016 TO 20261017]` inside the query so `opensearch:totalResults` is the in-window count);
GitHub repository pages (WebFetch; `gh api` refused every repo as "not enabled for this session"); Hugging Face
`api/models?search=` and `api/datasets?search=`; three arXiv HTML pages (2508.19828v5, 2610.18427v1,
2609.34649v1, 2510.04618v3) read by WebFetch for feasibility fields only. Raw XML and parsed JSON are in
`/tmp/claude-0/-home-claude/684a602a-8772-59ed-8c60-74c4245ab4ea/scratchpad/densityB/` (untrusted data).
Titles and ids below are verbatim from the API. Papers marked "title only" had no abstract read; every paper
with a one-sentence trick had its abstract read.

Verdict in one line: the field is saturated at the level of "self-written memory is unstable and its lessons need
outcome-measured credit" (two papers in the last nine weeks report the run-to-run variance directly, one with
randomized lesson-block experiments on ACE and Dynamic Cheatsheet), and "learn the memory writer by GRPO from
outcome reward" is an ICML 2026 paper; what no fetched abstract reports is the per-consolidation-node pair
(variance across m resampled consolidations, headroom against the full raw history) as a regime map. A pilot on
a public open-weight setup costs under 20 H100-hours or under $200 of API; two weeks is realistic for the
measurement, not for a method.

## 1. Density table (window: published 2025-10-16 → 2026-10-16)

Counts are `totalResults` for the query; "cap" means more than 100 matched and the first 100 (most recent) were
returned; capped queries were narrowed or paged with `start=100` until fully covered. Queries use `abs:` fields;
the full query strings are in `scratchpad/densityB/batch*/results.json`.

| Sub-topic | Query (abbreviated) | Count | Cap hit? | Coverage |
| --- | --- | --- | --- | --- |
| (a) self-evolving agents with memory/context/experience/playbook/reflection | (self-evolving OR self-improving OR self-evolution OR self-improvement) AND agent AND (memory OR experience OR playbook OR reflection OR context) | **708** | yes | first 100 only |
| (a) + failure words | ... AND (noise OR noisy OR collapse OR drift OR forgetting OR variance OR brevity OR degradation OR stale OR erosion OR bloat) | **132** | yes → paged by date | full (100 + 32) |
| (a) training-free scoping | ... AND (memory OR playbook OR experience bank OR skill library OR cheatsheet) AND (training-free OR test-time OR without fine-tuning OR frozen OR in-context OR ...) | **160** | yes → start=100 | full |
| (b) context collapse / evolving contexts / cheatsheet / playbook / experience bank (broad, incl. "context engineering", "context optimization") | ... AND (agent OR LLM OR language model) | **267** | yes | first 100 only |
| (b) core terms only (drop "context engineering/optimization") | context collapse OR evolving context(s) OR cheatsheet OR cheat sheet OR playbook(s) OR experience bank OR brevity bias OR context evolution | **142** | yes → start=100 | full |
| (b) + failure words | broad (b) AND (collapse OR drift OR noise OR degradation OR brevity OR bloat OR verbosity OR over-editing OR stale OR erosion OR forgetting) | **53** | no | full |
| (b) context engineering AND evolve/test-time/experience | (context engineering OR context optimization) AND agent(s) AND (self-evolving OR ... OR experience OR reflection) | **42** | no | full |
| (c) RL-trained memory managers | memory AND "reinforcement learning" AND (consolidation/consolidate/consolidating OR memory management OR memory construction OR memory operations OR memory manager OR memory agent OR memory controller) | **76** | no | full |
| (c) restricted to LLM | ... AND (LLM OR language model(s)) | **46** | no | full |
| (c) wildcard check `consolidat*` (API accepts it; same 46) | memory AND "reinforcement learning" AND (consolidat* OR memory management OR memory construction OR memory operations) | **46** | no | full |
| (d) credit assignment / counterfactual value of memory items (as specified) | (memory OR playbook OR experience) AND (counterfactual OR randomized OR ablation OR credit assignment) AND agent | **1,167** | yes | unusable (common words); not paged |
| (d) LLM-restricted | ... AND (LLM OR language model(s) OR language agent(s)) | **266** | yes | first 100 only |
| (d) item-level | (memory item(s) OR memory entry/entries OR memory unit(s) OR lesson(s) OR insights OR experience bank) AND (counterfactual OR credit assignment OR ablation OR randomized OR leave-one-out OR shapley OR attribution) AND agent AND LLM | **87** | no | full |
| (d) counterfactual-only (drop "ablation") | (memory OR playbook OR experience bank OR skill library OR cheatsheet OR lessons OR insights) AND (counterfactual OR credit assignment OR randomized/randomised OR leave-one-out OR shapley OR uplift OR causal effect) AND agent AND LLM | **149** | yes → start=100 | full |
| (e) noise / luck / replication in lessons (as specified) | (self-evolution OR self-improvement OR self-evolving OR self-improving OR reflection(s)) AND (noise OR noisy OR stochastic OR variance OR replication OR replicate OR reproducibility OR luck OR lucky) AND agent AND LLM | **224** | yes | first 100 only ("reflection" is the noise) |
| (e) narrowed (drop "reflection", add fragility/seeds) | (... OR experience-driven OR test-time learning) AND (noise ... OR multi-seed OR seeds OR fragility OR fragile OR unstable OR instability) AND agent AND LLM | **112** | yes → start=100 | full |
| (f) RSI title flood, last 14 days (2026-10-02 → 10-16) | ti:RSI OR ti:"Recursive Self-Improvement" OR ti:"recursively self-improving" OR ti:"recursive self-improving" | **30** | no | full; 30/30 genuine |
| (f) RSI titles, 12 months | same | **89** | no | full; 87 genuine (2 false positives: satellite "RSI", "Rule-State Inference") |
| (g) multi-session / cross-session agent RL or benchmark | (multi-session OR cross-session OR multi-episode OR cross-episode OR multiple sessions OR across sessions OR across episodes) AND agent AND ("reinforcement learning" OR benchmark) AND LLM | **111** | yes | first 100 only |
| (g) RL only | same terms AND agent AND "reinforcement learning" AND LLM | **12** | no | full |
| (g) benchmark + memory/experience + task stream | (... OR task stream(s) OR sequence of tasks) AND agent AND benchmark AND (memory OR experience OR self-evolving OR test-time learning) AND LLM | **97** | no | full |
| (g) lifelong/continual/test-time learning + memory + LLM agent + (RL OR benchmark) | | **73** | no | full |
| target: full history / oracle / without memory | (full history OR raw history OR raw trajectories OR oracle memory OR without memory OR memory ablation OR full trajectories) AND agent AND (memory OR experience OR playbook) AND LLM | **68** | no | full |
| target: memory writing learned from reward | (memory writing OR memory writer OR write memory OR memory update(s) OR what to remember OR what to store OR memory curation/curator) AND agent AND ("reinforcement learning" OR reward OR outcome) AND LLM | **15** | no | full |
| target: variance across runs of self-evolving memory | (memory OR playbook OR cheatsheet OR lessons OR insights OR reflection(s) OR experience) AND (variance OR resample(d/ing) OR repeated runs OR multiple seeds OR multi-seed OR random seeds OR run-to-run) AND agent AND (self-evolving OR self-improving OR test-time learning OR experiential OR ...) | **14** | no | full |
| target: value / harm of lessons | (lesson(s) OR insight(s) OR memory item(s) OR playbook OR skill library) AND (value OR utility OR usefulness OR harmful OR helpful OR hurt(s) OR net effect) AND agent AND (self-evolving ...) AND LLM | **51** | no | full |
| target: memory + outcome/sparse reward + RL | (memory OR playbook OR experience bank OR skill library OR cheatsheet OR reflection) AND (outcome reward(s) OR outcome-based reward OR sparse reward OR downstream reward OR downstream performance OR final/terminal reward) AND agent AND (RL OR GRPO OR policy gradient/optimization) AND LLM | **28** | no | full |

Reading of the counts. Sub-topic (a) is a 700-paper field in twelve months; the failure-word slice alone is
132. The exact target vocabulary (variance/resampling of self-evolving memory) returns 14, memory-writer-from-
reward returns 15, oracle/full-history arms return 68. The W41 checklist warning held: adding failure words
changed which papers surfaced (the two most dangerous titles, 2608.18066 and 2610.19910, appear only in the
failure-word slices), not only the count.

### Ten most relevant titles per sub-topic (verbatim; id, published date)

(a) self-evolving agents with memory (from the 708 / 132 / 160 slices):
1. 2610.18427 (2026-10-13) Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments
2. 2608.18066 (2026-08-18) On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification
3. 2610.19910 (2026-10-14) When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents
4. 2606.28374 (2026-06-17) Recursive Self-Evolving Agents via Held-Out Selection
5. 2605.12978 (2026-05-13) Useful Memories Become Faulty When Continuously Updated by LLMs
6. 2605.19576 (2026-05-19) Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries
7. 2608.00017 (2026-06-29) Memory Reward Inflation in Self-Improving LLM Agents
8. 2607.24300 (2026-07-27) Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents (title only)
9. 2609.36892 (2026-09-29) Harness Evolution as Learning: Approximation, Generalization, and Optimization Limits of Self-Improving Personal Agents (title only)
10. 2605.09315 (2026-05-10) Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation (title only)
Also: 2610.19386 STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents; 2609.02217 SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams; 2609.02074 CHIME: Credit-Aware Hierarchical Memory Evolution for Long-Horizon Agentic Planning; 2608.05810 When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents; 2608.01679 When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary; 2608.22533 CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories; 2602.01966 Self-Consolidation for Self-Evolving Agents (all title only).

(b) context collapse / evolving contexts / cheatsheet / playbook / experience bank:
1. 2610.18427 (2026-10-13) Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments
2. 2609.34649 (2026-09-28) Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses
3. 2608.09153 (2026-08-10) TRACE: TRajectory Attribution for Automated Context Engineering
4. 2608.05778 (2026-08-06) When Do Prompt-Side Agent Playbooks Transfer? Accuracy, Cost, and Runtime Shift in Agent Deployment (title only)
5. 2607.09175 (2026-07-10) Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift (title only)
6. 2606.02304 (2026-06-01) Unified Context Evolution for LLM Agents (title only)
7. 2604.03189 (2026-04-03) Reflective Context Learning: Studying the Optimization Primitives of Context Space (title only)
8. 2607.14159 (2026-07-14) MemoHarness: Agent Harnesses That Learn from Experience (title only)
9. 2607.12397 (2026-07-14) Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents (title only)
10. 2601.00923 (2026-01-01) Context Collapse: In-Context Learning and Model Collapse (title only)
Also: 2610.20959 Same Context, Different Agents: A Behavioral Study of Semantic Layers, Orchestration and Compaction in Data Agents; 2607.28022 Flux-OPD: On-Policy Distillation with Evolving Contexts; 2602.10218 ACE-RTL: When Agentic Context Evolution Meets RTL-Specialized LLMs; 2601.21557 Meta Context Engineering via Agentic Skill Evolution; 2604.07487 CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection; 2606.24402 Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents (all title only).

(c) RL-trained memory managers (76 / 46):
1. 2605.21768 (2026-05-20) Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents
2. 2601.05488 (2026-01-09) MemBuilder: Reinforcing LLMs for Long-Term Memory Construction via Attributed Dense Rewards
3. 2606.25161 (2026-06-23) TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory
4. 2610.21147 (2026-10-15) All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents
5. 2605.00702 (2026-05-01) Learning How and What to Memorize: Cognition-Inspired Two-Stage Optimization for Evolving Memory
6. 2601.08435 (2026-01-13) Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management (title only)
7. 2601.23014 (2026-01-30) Mem-T: Densifying Rewards for Long-Horizon Memory Agents (title only)
8. 2604.01560 (2026-04-02) DeltaMem: Towards Agentic Memory Management via Reinforcement Learning (title only)
9. 2607.20553 (2026-07-15) CMI-Mem: Toward Generalizable Long-Term Memory Management via CMI-Augmented Reinforcement Learning (title only)
10. 2606.03979 (2026-06-02) Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories
Also: 2605.22411 DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Agent Memory; 2601.01885 Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents; 2608.03137 Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents; 2601.08323 AtomMem: Learnable Dynamic Agentic Memory with Atomic Memory Operation; 2605.23067 What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA; 2609.34422 Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning (all title only).

(d) credit assignment / counterfactual value of memory items (87 / 149):
1. 2610.18427 (2026-10-13) Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments
2. 2605.17641 (2026-05-17) Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents
3. 2609.08279 (2026-09-08) What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory
4. 2607.21106 (2026-07-23) AttriMem: Attribution-Guided Process Feedback for Agent Memory Construction
5. 2609.36805 (2026-09-29) UpliftMem: Learning Set-Level Uplift for Agent Memory Retrieval (title only)
6. 2608.23268 (2026-08-24) Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner (title only)
7. 2609.09115 (2026-09-08) MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance for Long-Horizon LLM Agents (title only)
8. 2606.08151 (2026-06-06) Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents (title only)
9. 2605.04811 (2026-05-06) Tree-based Credit Assignment for Multi-Agent Memory System (title only)
10. 2609.24259 (2026-09-21) MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents (title only)
Also: 2608.00155 AgentStream; 2606.29279 Manufactured Confidence: How Memory Consolidation Turns Hearsay into Confident Facts; 2607.25992 MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents; 2609.33321 Separating Memory and Workflow Effects in Predicting Individual Answers; 2610.14790 Counterfactual Regret for Reflective Agents with Lean-Verified Guarantees; 2610.11188 What to Admit and How to Present: Governing Persistent Memory in LLM Agents (all title only).

(e) noise / luck / replication in lessons (224 / 112 / 14):
1. 2608.18066 (2026-08-18) On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification
2. 2610.19910 (2026-10-14) When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents
3. 2609.36043 (2026-09-28) SAGE: A Statistical Acceptance Gate for Self-Evolving Agents
4. 2610.12601 (2026-10-08) Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol for Measuring Transferable Gains and Prompt-Level Overfitting
5. 2608.00017 (2026-06-29) Memory Reward Inflation in Self-Improving LLM Agents
6. 2607.07436 (2026-07-08) The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents
7. 2606.28374 (2026-06-17) Recursive Self-Evolving Agents via Held-Out Selection
8. 2610.00651 (2026-09-30) Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard (title only)
9. 2608.00355 (2026-07-31) CurveShift: Is Agent Progress Scalar? Separating Level from Shape (title only)
10. 2610.08215 (2026-10-06) Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments? (title only)
Also: 2609.35596 SEABench: Benchmarking Endogenous Misalignment In Self-Evolving Agents; 2608.25776 EVOMAL: Self-Poisoning in Self-Evolving Coding Agents; 2608.22610 Coalition-Aware Skill Reliability for Self-Evolving Agents; 2610.11732 MemTrial: Learning When to Trust Memory in LLM Portfolio Agents; 2608.28011 Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents (all title only).

(f) RSI flood: see section 2.

(g) multi-session / cross-session agent RL and benchmarks (12 RL / 97 benchmark / 73 lifelong):
1. 2606.08656 (2026-06-07) From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory
2. 2605.21768 (2026-05-20) Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents
3. 2606.17591 (2026-06-16) Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning
4. 2606.27472 (2026-06-25) Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents
5. 2608.00155 (2026-07-31) AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?
6. 2604.08988 (2026-04-10) SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment
7. 2511.20857 (2025-11-25) Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory (title only)
8. 2605.18421 (2026-05-18) EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective (title only)
9. 2602.04089 (2026-02-03) Scaling In-Context Online Learning Capability of LLMs via Cross-Episode Meta-RL (title only)
10. 2603.17621 (2026-03-18) Complementary RL: Towards Efficient Experience-Driven Agent Learning (title only)
Also: 2512.17102 Reinforcement Learning for Self-Improving Agent with Skill Library; 2606.17546 SEAGym: An Evaluation Environment for Self-Evolving LLM Agents; 2606.06960 FinEvolveBench: A Benchmark for Self-Evolving Agents on Low-Repetition Tasks with Implicit Rewards; 2605.29225 BenchTrace: A Benchmark for Testing Reflection Ability and Controlled Evolution in LLM Agents; 2608.01759 Benign Alone, Harmful Together: Exploiting Experience Composition in Self-Evolving LLM Agents; 2606.17328 MemTrace: Probing What Final Accuracy Misses in Long-Term Memory (all title only).

### Papers whose abstract says they measure value-of-memory or signal at the memory step (for the sibling agent)

Each line: id, one-sentence plain trick from the fetched abstract, and what it reports about SIGNAL / HEADROOM.

- **2610.18427 Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments** (Pham, Nguyen, Le, Srey, Luu; 2026-10-13). Trick: group a playbook's lessons into blocks, include or leave out each block at random on practice tasks, and keep the blocks whose measured success gap is positive; grow several playbooks and serve whichever curated/whole/no playbook scores best on fresh practice episodes. Reports: "the same procedure can write a playbook that helps or one that falls up to 69.6 points below no playbook"; three growth runs per setting (e.g., 27B AppWorld per-test feedback: 82.5, 58.9, 30.0 vs 78.4 with no playbook); systems ACE and Dynamic Cheatsheet; models Qwen3.8-27B, Qwen3.5-9B, Gemma-4-31B; AppWorld 168 / WebShop 500 / ALFWorld 134 eval tasks; K = 3 playbooks, 2K+1 = 7 candidates. This is a 3-sample SIGNAL at the whole-run level and a no-playbook arm; **no full-history / oracle arm, no per-node decomposition**. Code: anonymous.4open.science/r/rbc (anonymous link, not a final repository).
- **2608.18066 On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification** (Ye, Li, Pruksachatkun, Zhang, Wu; Salesforce; 2026-08-18). Trick: re-run two memory-based self-improving methods (Agent Workflow Memory, ReasoningBank) many times and with shuffled task orders, and show the gain is within the run-to-run noise and depends on an implicit curriculum. Reports: multiple self-improving runs to quantify variance on WebArena, VisualWebArena, SCUBA; "stacking a self-improving loop on top can further amplify this noise". **Run-level SIGNAL, no HEADROOM arm.** Code github.com/SalesforceAIResearch/self-improve-fragility (4 commits, 1 star); data huggingface.co/datasets/Salesforce/self-improve-fragility (updated 2026-08-18, 3,661 downloads; "Agent trajectories are released").
- **2610.19910 When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents** (2026-10-14). Trick: inject ordinary noise into instructions, evidence, execution records and outcome–record pairings during skill learning, freeze the skill store, and test on held-out tasks; noisy learning keeps only 25.5–42.1% of the clean gain. Reports noise-sensitivity of the writer; **not variance across resampled writes**.
- **2609.36043 SAGE: A Statistical Acceptance Gate for Self-Evolving Agents** (2026-09-28). Trick: accept a skill-document edit only when a one-sided paired test on identical validation items says its wins beat its losses, which removes the optimizer's-curse bias of "keep any edit that raises the average". Reports that the gate's noise problem is the problem; **no C/H numbers**.
- **2608.00017 Memory Reward Inflation in Self-Improving LLM Agents** (2026-06-29). Trick: the score stored with each episode is a proxy reward for an implicit policy; when an LLM judge produces it, wrong episodes get inflated scores and the agent preferentially reuses its most confident mistakes; corrects only if the verifier's error is independent of the memory bias. Relevant to the "signal-starved" claim: it formalizes a case where the outcome signal itself is biased.
- **2606.08656 From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory** (ICML 2026). Trick: train a separate "memory copilot" that rewrites a frozen player's memory between rounds, end-to-end with multi-turn GRPO on the player's later outcomes, with a turn-wise reward and turn-level advantages. **This is the target's question answered "yes" on Rock-Paper-Scissors and Limit Texas Hold'em**; no agentic task stream.
- **2605.21768 Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents** (2026-05-20). Trick: once rollouts write different memories they no longer share a state, so GRPO's group comparison is unfair; fix the comparison so credit reaches the write. Names the mechanism by which outcome reward reaches the memory write.
- **2601.05488 MemBuilder** and **2607.21106 AttriMem** (2026-01, 2026-07). Trick (both): outcome-only reward is too coarse to say which memory contents helped, so attribute the answer back to memory contents and pay dense rewards per write. Both state the signal-starvation premise as motivation ("sparse trajectory-level rewards"; "coarse signals ... cannot identify which intermediate memory contents support the final answer").
- **2605.00702 Learning How and What to Memorize** (2026-05-01) states it in one sentence: "although reinforcement learning (RL)-based agents learn memory updates, sparse outcome rewards provide weak supervision, resulting in unstable long-horizon optimization."
- **2606.27472 Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents** (2026-06-25). Trick: on LongMemEval's knowledge-update subset, replace the full context with a bounded self-maintained memory and measure the drop (92% → 77% on gpt-5.4, paired McNemar p < 0.005). **This is a HEADROOM measurement (full context minus self-written memory) on one QA subset**; code, environment, model and dataset at github.com/Vrin-cloud/supersede.
- **2608.12888 When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory** (2026-08-13). Trick: leave the raw history unmodified and let the agent keyword-search it; structured memory's benefit mostly comes from retrieval, not structure. A raw-history arm beating consolidation, i.e., negative headroom for consolidation in conversational QA.
- **2605.12978 Useful Memories Become Faulty When Continuously Updated by LLMs** (2026-05-13). Trick: as an LLM keeps rewriting a memory bank, utility first rises then falls even when the source experiences were useful. The consolidation step as the failure site.
- **2609.08279 What Eviction Destroys: A Restore-Counterfactual Audit of Forgetting in Agent Memory** (2026-09-08). Trick: per question, put the gold evidence back into the read-time context, rerun the same reader, and classify each error as recoverable, irreversible or residual. An oracle-restoration arm at the item level.
- **2605.17641 Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents** (2026-05-17). Trick: estimate each candidate memory's effect on the answer by controlled interventions and keep the ones that help. Item-level counterfactual value at read time.
- **2606.28374 Recursive Self-Evolving Agents via Held-Out Selection** (2026-06-17). Trick: rewrite strategy, skills and playbook from the agent's own trajectories and commit a candidate only if it wins on held-out tasks; compares reflections, workflows, playbooks, cheatsheets, prompts apples-to-apples.
- **2610.12601 Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol...** (2026-10-08). Trick: three seeds, bootstrap CIs, topic-disjoint splits; the validation-minus-held-out gap is "small-sample selection under a noisy judge"; a scalar reward makes transfer negative while decomposed feedback transfers. The protocol the target needs, on prompt optimization.
- **2609.34649 Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses** (ContextEvo; 2026-09-28). Trick: reconstruct what the model saw at key decision points, find context-related failures, and patch the harness's context policy. Paper states "Each task is attempted once"; no variance, no full-raw-history baseline (per the fetched HTML). Not a C/H measurement.

## 2. The RSI title flood

Titles containing "RSI" or "Recursive Self-Improvement" (and the two spelling variants): **30 in the last 14
days (2026-10-02 → 10-16), all 30 genuine**; 89 in twelve months, of which 87 are genuine (false positives:
2609.35906 satellite "RSI" = remote sensing image; 2603.21610 "Rule-State Inference (RSI)"). Monthly: Jan 1,
Feb 1, Mar 2, Apr 0, May 0, Jun 2, Jul 11, Aug 8, Sep 34, Oct 1–15: 30. A third of the twelve-month total
landed in the last two weeks. The 30 (ids, dates, verbatim titles):

2610.22192 (10-15) Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine · 2610.20474 (10-14) AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents · 2610.20431 (10-14) SwarmRSI: Recursive Self-Improvement through Evolving Scientific Agent Swarm · 2610.20294 (10-14) MMLA-RSI: Recursive Self-Improvement through RTT and RTMA · 2610.19424 (10-14) VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness · 2610.18845 (10-13) The Last Remote Sensing Model Built by Humans? Casting Any Earth Observation Task as Recursive Self-Improvement · 2610.18842 (10-13) Who Improves the Robot? Toward Physical Recursive Self-Improvement · 2610.18083 (10-13) AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement · 2610.17718 (10-13) ECG-RSI: Recursive Self-Improvement through Targeted Electrocardiogram Waveform Evolution · 2610.17114 (10-12) D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control · 2610.16491 (10-12) Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems · 2610.15782 (10-11) Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping · 2610.15772 (10-11) RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution · 2610.15708 (10-11) SpecForge: Recursive Self-Improvement for Coding Agents via Behavioral Specifications · 2610.14843 (10-10) Pre-Registered Genesis Accounting for Recursive Self-Improvement: First Audited Operator-Genesis Events in a Physics-Discovery Runtime · 2610.14625 (10-10) From Existing Methods to New Research Ideas: Two Perspectives on Recursive Self-Improvement · 2610.14495 (10-10) Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos · 2610.13912 (10-09) RSI-Anything: Unlocking Recursive Self-Improvement with World Models · 2610.12369 (10-08) Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement · 2610.12176 (10-08) Recursive Self-Improvement through Multi-Agent Self-Supervision · 2610.11794 (10-08) Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks · 2610.11299 (10-08) DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration · 2610.10310 (10-07) RSIGym: A Flexible Environment for Recursive Self-Improvement · 2610.09426 (10-07) RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement · 2610.07969 (10-06) EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation · 2610.07105 (10-05) Beyond Successor Accuracy: State Retention for Recursive Self-Improvement in Recommendation · 2610.05701 (10-05) Second-Order Problem Solving for Recursive Self-Improvement in Formal Verification · 2610.05151 (10-04) Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision · 2610.04302 (10-03) From Valid to Useful: Post-Verification Acquisition for Recursive Self-Improving Recommendation · 2610.03002 (10-02) Recursive Self-Improvement in Unified Multimodal Models.

Of these, the ones that touch the target's object (a self-written text memory/rulebook) by title: Memento 3
(reflective rulebooks), Terminal-RSI (recursive self-rewrite), RSIPO (skill–policy co-evolution), SpecForge
(behavioral specifications). All title only. The flood is a register signal: "RSI" is the packaging this month,
and a measurement paper on memory-write signal will be read against it.

## 3. Pre-window precedents (ids verified by title search on the API; abstracts read)

| Paper | id (first version date) | One-sentence plain trick (from the abstract) | Narasimhan? |
| --- | --- | --- | --- |
| Reflexion: Language Agents with Verbal Reinforcement Learning | 2303.11366 (2023-03-20) | After a failed try the agent writes a sentence about what went wrong, keeps it in an episodic text buffer, and reads it on the next try; no weights change. | **Yes**: authors Shinn, Cassano, Berman, Gopinath, **Karthik Narasimhan**, Shunyu Yao |
| Voyager: An Open-Ended Embodied Agent with Large Language Models | 2305.16291 (2023-05-25) | A Minecraft agent stores every behavior it gets working as executable code in a growing skill library and retrieves it later, driven by an automatic curriculum and iterative prompting with environment feedback. | No |
| ExpeL: LLM Agents Are Experiential Learners | 2308.10144 (2023-08-20) | Run training tasks, extract natural-language insights from the successes and failures, and prepend the insights plus retrieved past experiences at test time, without parameter updates. | No |
| Generative Agents: Interactive Simulacra of Human Behavior | 2304.03442 (2023-04-07) | Keep a complete natural-language record of an agent's experiences, periodically synthesize them into higher-level "reflections", and retrieve both to plan behavior. | No |
| A-MEM: Agentic Memory for LLM Agents | 2502.12110 (2025-02-17) | Each new memory becomes a Zettelkasten-style note with generated attributes and links to existing notes, so organization is produced by the agent rather than fixed. | No |
| Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory | 2504.07952 (2025-04-10) | A black-box LM keeps a persistent cheatsheet of strategies, code snippets and insights that it rewrites after each query and reads before the next, with no labels. | No |
| ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory | 2509.25140 (2025-09-29) | Distill generalizable reasoning strategies from self-judged successes and failures into a memory bank, retrieve them per task, and scale the number of trajectories per task to get contrastive signal for better memory (MaTTS). | No |
| Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ACE) | 2510.04618 (2025-10-06) | Treat the context as a playbook edited by three roles (generator, reflector, curator) with structured incremental item updates instead of whole rewrites, to avoid brevity bias and context collapse. | No |
| Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | 2508.19828 (2025-08-27) | Fine-tune a memory manager that emits ADD/UPDATE/DELETE/NOOP and an answer agent with outcome-driven PPO/GRPO from 152 QA pairs. | No |
| Mem-α: Learning Memory Construction via Reinforcement Learning | 2509.25911 (2025-09-30) | Train an agent that reads sequential chunks and writes a structured memory, rewarded by downstream QA accuracy over the full interaction. | No |
| MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent | 2507.02259 (2025-07-03) | Read a long text in segments and overwrite a fixed-size text memory after each, trained end-to-end with a multi-conversation extension of DAPO. | No |
| MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents | 2506.15841 (2025-06-18) | At every turn the agent rewrites one compact internal state that is both its memory and its reasoning, trained by RL to keep memory constant across turns. | No |
| Training-Free Group Relative Policy Optimization | 2510.08191 (2025-10-09) | Run GRPO's group rollouts but, instead of a gradient step, have the model write the lesson from the group's relative outcomes into an experiential-knowledge prior in the prompt. | No |

Only Reflexion carries Karthik Narasimhan. None of the thirteen abstracts reports variance across resampled
memory writes or a full-history arm (abstract-level reading; the sibling agent reads the bodies).

## 4. Pilot feasibility: code and setups

`gh api repos/<owner>/<repo>` returned HTTP 403 "GitHub access to this repository is not enabled for this
session" for every repository (the session's GitHub proxy only serves attached repositories); repository pages
were read with WebFetch instead, which shows commit counts but not commit dates. Hugging Face via the API.

| Setup | Code | Last commit | Base models | Task streams | Episodes per stream | Tokens per episode |
| --- | --- | --- | --- | --- | --- | --- |
| ACE (2510.04618) | github.com/ace-agent/ace — public since 2025-11-19 (SambaNova blog); 12 commits; 1.3k stars; offline/online/eval_only modes | date not shown on page | DeepSeek-V3.1 for generator, reflector, curator; providers sambanova / together / openai / commonstack (API only; no vLLM path in README) | AppWorld; FiNER and XBRL Formula (`eval.finance.run`) | not stated in README or paper body ("All datasets follow the original train/validation/test splits"; offline: up to 5 epochs; online: one pass, batch size 1) | not stated; `playbook_token_budget` 80,000; `max_tokens` 4,096; the DC collapse case study quotes a context of 18,282 tokens at step 60 |
| Dynamic Cheatsheet (2504.07952) | github.com/suzgunmirac/dynamic-cheatsheet; 4 commits; 276 stars | not shown | OpenAI, Anthropic, Gemini, xAI, DeepSeek APIs; open-weight via Together (Llama 3.3 70B, DeepSeek-R1) and local Ollama (Llama 3 70B) | AIME 2020–2024, AIME 2025, Game of 24, GPQA Diamond, MMLU-Pro Physics/Engineering, MathEquationBalancer | AIME 2025 = 30 problems; others not stated in README (AIME 2020–2024 ≈ 150 problems, estimate) | not stated; single-call episodes (cheatsheet + question + answer) |
| ReasoningBank (2509.25140) | github.com/google-research/reasoning-bank; 6 commits; 605 stars | not shown | gpt-3.5-turbo / gpt-4 / gpt-4o (OpenAI key); gemini-2.5-flash / -pro and claude-3-7-sonnet via Vertex AI; **no open-weight models** | WebArena; SWE-Bench ("We release code for SWE-Bench ... and WebArena") | not stated | not stated |
| 2610.18427 Randomized Block Curation | anonymous.4open.science/r/rbc (anonymous link in the abstract footnote; no GitHub) | n/a | Qwen3.8-27B, Qwen3.5-9B, Gemma-4-31B (open-weight) | AppWorld 168, WebShop 500, ALFWorld 134 eval tasks; train and practice splits in Table 3 (not read) | 3 growth runs per setting; K = 3 playbooks; 7 candidates scored on fresh practice episodes; practice count not stated | not stated (tokens served reported as % of whole playbook; Appendix E.4 "Cost" not read) |
| 2609.34649 ContextEvo | none public ("supporting materials provide the complete source code") | n/a | DeepSeek-V4-Flash-0731 and GPT-5.6-Luna (API); Qwen3.8-27B as judge; Pi-agent harness v0.80.6 | Long-Horizon-Terminal-Bench 46 (20 in / 26 out), DeepSWE 113 (48 / 65), BrowseComp-Plus hard 174 (76 / 98) | one attempt per task (44 / 112 / 174 trajectories) | median trace tokens 80.7K / 124.2K / 70.9K; 8.57M mean tokens per LHTB run (Pi baseline) |
| Memory-R1 (2508.19828) | **no code URL in the paper HTML (first 100K chars) or on HF** | n/a | LLaMA-3.1-8B-Instruct, Qwen-2.5-7B-Instruct (3B–14B range claimed); PPO and GRPO | LoCoMo, MSC, LongMemEval (152 training QA pairs) | n/a (QA, not a task stream) | not stated |
| Mem-α (2509.25911) | github.com/wangyu-ustc/Mem-alpha; 9 commits; 227 stars; `verl` directory; GRPO scripts | not shown | Qwen3-4B / Qwen3-8B trained (Memalpha-4B released at huggingface.co/YuWangX/Memalpha-4B); Qwen3-32B as memory server | Memalpha dataset (HF YuWangX/Memalpha, Memalpha-full) and MemoryAgentBench (HF YuWangX/Memalpha-Memoryagentbench) | n/a (chunked documents, not a task stream) | "Trained on 30k tokens, generalizes to 400k+ tokens" |
| Bonus: 2608.18066 self-improve-fragility | github.com/SalesforceAIResearch/self-improve-fragility; 4 commits; 1 star; HF dataset Salesforce/self-improve-fragility (2026-08-18; 3,661 downloads; trajectories) | n/a | not stated on the page | WebArena, VisualWebArena, SCUBA; methods AWM and ReasoningBank | not stated on the page | not stated |
| Bonus: 2606.27472 Supersede | github.com/Vrin-cloud/supersede ("Code, environment, model, and dataset") | not checked | gpt-5.4 named | LongMemEval knowledge-update subset | n/a | not stated |

Hugging Face search summary: Memory-R1 none; Mem-α model + 3 datasets; ReasoningBank only third-party subsets;
Dynamic Cheatsheet only two third-party Qwen-7B checkpoints named after it; ACE none official; ContextEvo none;
MemoPilot none (one empty third-party repo); Salesforce/self-improve-fragility present.

Cheapest runnable public setups for a SIGNAL/HEADROOM pilot, in order: (1) Dynamic Cheatsheet on AIME /
MMLU-Pro with an open 7–14B model through Ollama or an OpenAI-compatible vLLM endpoint (single-call episodes,
local, free); (2) ACE's playbook loop re-pointed at an open model through an OpenAI-compatible endpoint
(`api_provider` list has no vLLM entry, so one adapter is needed) on ALFWorld or WebShop as 2610.18427 did
(local simulators, 134 / 500 tasks; RBC code is anonymous so the harness around ACE/DC must be re-written,
≈ 2–3 student-days); (3) ACE on AppWorld with DeepSeek-V3.1 as shipped (API dollars; AppWorld install is the
schedule risk). ReasoningBank's code needs closed models through Vertex/OpenAI and WebArena hosting.

## 5. Pilot cost estimate (estimates; assumptions stated)

Design as specified: a stream of 30 tasks; 10 consolidation points; at each point resample the consolidation
m = 8 times, run k = 5 downstream tasks per resample with n = 2 repeats; plus a full-history arm (k × n per
point); plus a no-memory arm (recommended; cheap).

Episode counts. Base stream: 30 episodes (also provides the histories). Downstream: 10 × 8 × 5 × 2 = **800**.
Full-history arm: 10 × 5 × 2 = **100** (long context). No-memory arm: 100. Consolidation writes: 10 × 8 = 80
LLM calls (one call each, input = raw history to that point). **Total ≈ 1,030 episodes + 80 writes.**

Monte-Carlo floor (why m = 8, n = 2 is the minimum): with k = 5 tasks and n = 2 repeats, each resample's
success estimate V̂ has sampling variance V(1−V)/(k·n) ≈ 0.025 at V = 0.5; the between-resample variance C
must clear that after subtracting the binomial term, so C is detectable at a node only if C ≳ 0.01–0.02
(standard deviation of success across consolidations ≳ 0.1–0.15). 2610.18427's three runs (82.5 / 58.9 /
30.0) imply a run-level standard deviation of ~0.26, well above the floor; per-node C will be smaller, so
expect to double m or k at the nodes that matter (budget ×2 below).

(A) Dynamic Cheatsheet on AIME-style math, open 7–14B model (Qwen3-8B/14B class) on vLLM. Assumptions: 3K
prompt tokens (cheatsheet ≤ 2K + question), 6K output tokens per episode; 1,030 episodes → ~3M prompt + ~6M
output tokens; aggregate decode 1.5–3K tokens/s on one H100 at batch 64–256. **≈ 1–2 H100-hours; ×2 safety →
2–4 H100-hours. API alternative** (if the pilot must match DC's published closed-model setting): GPT-4o-class at
$2.50/M input, $10/M output → ≈ $70; Claude Sonnet-class at $3/$15 → ≈ $100 (price assumptions as of the
author's last known list prices; verify before spending).

(B) ACE- or DC-style playbook on ALFWorld (134 tasks, local text simulator), Qwen3-8B/14B on vLLM. Assumptions:
30 steps per episode; 4K context per step (playbook ~2K); 3K output tokens per episode; prefix caching makes
incremental prefill ~10K per episode (≈ 125K without caching). 1,030 episodes → ~3M output + 10–130M prefill
tokens; decode 2.5K tok/s, prefill 30K tok/s → 0.3 h + 0.1–1.2 h. Full-history arm: raw history of ≤ 30
ALFWorld episodes ≈ 100–150K tokens of context per step, 100 episodes × 30 steps; with prefix caching the
incremental cost is small, without it 450M prefill tokens ≈ 4 h. Needs a model with a ≥ 128K window (Qwen3-14B
with YaRN, or Qwen3-Coder-30B-A3B at 256K as in the C-W42-02 record). **≈ 3–8 H100-hours; ×2 safety → 6–16
H100-hours.** No API dollars.

(C) ACE on AppWorld as shipped (DeepSeek-V3.1 via API). Assumptions: 20 steps per episode; 30K context per step
with a 20–80K playbook; 5K output per episode; DeepSeek list prices ~$0.56/M input (cache miss), ~$0.07/M (cache
hit), ~$1.68/M output (assumption; verify): ≈ $0.05–0.10 per episode with caching, $0.3–0.5 without → **$50–
150 (cached) to $300–500 (uncached) for 1,030 episodes.** The full-raw-history arm is **not runnable** here:
30 AppWorld episodes ≈ 1–1.5M tokens exceed a 128K window; HEADROOM must use a substitute oracle (union of all
m playbooks; a reflector given ground-truth test feedback; or the last-3-episodes raw history), which changes
what H means and must be declared.

Two-week verdict (one student). **Realistic for (A) and (B)**: compute is under 20 H100-hours in every variant,
the engineering is a resampling wrapper around a public consolidation step plus logging, and the public ACE and
DC code already expose the consolidation call. The schedule risks are not compute: (i) AppWorld installation and
flaky execution (choose ALFWorld/WebShop first, as 2610.18427 did); (ii) the full-history arm needs a long-window
open model or a declared oracle substitute; (iii) the protocol check — the resampled party (the writer) must run
at temperature > 0 and the n repeats of the downstream policy also at temperature > 0, while ALFWorld/WebShop/
AppWorld environments are deterministic, so the n-repeat variance is policy sampling noise by construction and
no "environment noise" claim is available (checklist 2026-10-08). Not realistic in two weeks: a trained
memory-writer comparison (the RL arm) on an agentic stream; no MemoPilot release was found on Hugging Face
(GitHub not searched for it), and no Memory-R1 code URL was found in the paper's HTML or on Hugging Face.

## 6. Checklist items triggered

- **2026-10-16 "A landscape report from a research tool is a harvest, not a kill search."** The record's note
  "no public benchmark reports variance of downstream success across independently resampled summaries of the
  same prefix" is contradicted for the memory-consolidation site: 2608.18066 runs "multiple self-improving runs
  to quantify variance" and releases trajectories; 2610.18427 runs "three growth runs" per setting and quotes
  the spread. Both are run-level, not per-node; the sentence must be rewritten at node level with those two
  cited.
- **2026-10-09 "nobody has done X" must quote the two closest papers' own limitation sections.** The sibling
  agent should quote 2610.18427's limitations ("trades extra episodes for reliability"; no full-history arm) and
  2609.34649's protocol sentence ("Each task is attempted once").
- **2026-10-09 density queries must include failure-mode words.** Done; the two most dangerous titles surfaced
  only in the failure-word slices.
- **"The 12-month window measures density, not prior art."** Thirteen pre-window precedents listed and verified;
  Reflexion (Narasimhan) is the campus link.
- **"A first measurement that names a benchmark confirms it is runnable or budgets the re-implementation."**
  ACE and DC: public code, API-first; RBC: anonymous code, re-implementation ≈ 2–3 days; ContextEvo and
  Memory-R1: no public code; ReasoningBank: closed models only.
- **2026-10-14 protocol check for variance claims (who samples at T > 0).** Writer at T > 0 is the measured
  party; downstream policy at T > 0 for repeats; deterministic simulators → no environment-noise claim.
- **2026-10-08 "Deterministic sandboxes ... any 'environment noise' claim must name its source."** Applies to
  all three candidate task streams.
- **"Temperature-0 through an API is not a deterministic arm."** Applies if (C) is chosen; budget the open-model
  stack or drop the deterministic arm.
- **"When a competitor paper writes the target quantity and calls it future work, record the group, stack and
  date."** 2610.18427 (Pham, Nguyen, Le, Srey, Luu; open-weight Qwen3.8/3.5 and Gemma-4 on AppWorld/WebShop/
  ALFWorld; 2026-10-13) measures lesson-block effects by randomization and run spread; 2606.08656 (ICML 2026)
  trains the writer by GRPO. The "why now" must say why neither group has mapped C and H per node; "they have the
  stack" is a guess.
- **"Why now."** The enabling pieces are public: ACE code (2025-11-19), RBC's 3-run spread (2026-10-13),
  Salesforce trajectories (2026-08-18), open 128K–256K-window 8–30B models. No piece is newer than nine weeks;
  the window is weeks.
- **"One-sentence trick for the candidate itself."** Proposed: at each point where an agent rewrites its own
  notes, resample the rewrite several times and ask two questions — does the choice of rewrite change what
  happens next (signal), and would keeping everything have done better (headroom) — to tell where learning the
  rewrite from outcomes can work.
- **Scorecard (CLAUDE.md rule 9)** not present in the record for this scoping; required before any report.

## 7. What this report did not do

Read any paper body beyond the four HTML pages named above (the sibling agent's job); page the 708-, 267-,
1,167-, 266-, 224- and 111-count queries beyond their first 100 (their narrowed versions were paged in full);
verify GitHub commit dates (pages do not show them; `gh api` refused); verify current API list prices.
