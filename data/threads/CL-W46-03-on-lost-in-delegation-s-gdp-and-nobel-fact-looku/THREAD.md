# On Lost in Delegation's GDP and Nobel fact lookups with gpt-oss-120b and GPT-5 as both orchestrator and executor, the post-cutoff delegation loss is a return-rate operating point, not a cost of separating contexts: at the single agent's tool budget and tool-use instruction, an at-most-80-token structured return (answer, source URL, quoted snippet, tool-failure list) appended to the executor's bare answer recovers at least half of the matched delegation loss.

`CL-W46-03` · lane **L4** · status **open** · rank 4 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 unmeasured (kill search owed); Gate 2B flagged (expected result at judgment 0.35; the two imports disagree on the channel and the probes decide the fork). Next action: see First steps.

## The claim

- **Headline:** On Lost in Delegation's GDP and Nobel fact lookups with gpt-oss-120b and GPT-5 as both orchestrator and executor, the post-cutoff delegation loss is a return-rate operating point, not a cost of separating contexts: at the single agent's tool budget and tool-use instruction, an at-most-80-token structured return (answer, source URL, quoted snippet, tool-failure list) appended to the executor's bare answer recovers at least half of the matched delegation loss.
- **Current belief (the field's):** 2611.16526 sec. 7 (card, full text): 'Passing complete executor traces to the orchestrator could mitigate the loss of information, but would undermine the context-saving benefits of delegation'; sec. 2: 'we isolate the effect of delegating tool access on performance'; sec. 5.1: 'Query rewriting can alter the task itself'. 2607.16133 sec. 3 (full text read by the S10xF5 import, 2026-11-15): 'The system-level aggregator then combines all terminal memories into the final output'; abstract (fetched 2026-11-15): 'the nontrivial advantage of MAS arises under bounded relays, where compression introduces a fundamental trade-off'. 2604.02460 abstract (fetched 2026-11-15): 'under a fixed reasoning-token budget and with perfect context utilization, single-agent systems are more information-efficient'. 2611.13254 sec. 4.2 (card): contradicting evidence 'was in an agent's input and was never mentioned' in 41 of 68 failed runs that held it, so the loss between agents is attention, not transmission.
- **If true:** Orchestrator harnesses replace 'final answer' returns with a structured evidence block at the knee and report the return rate in tokens; MAS-versus-SAS comparisons match the pooled tool budget and the executor instruction and report the return rate operated at, so 2611.16526's 9-11 point loss is re-read as a protocol and schema choice; delegation-training teams fix the return schema before writing the rubric; 2607.16133's relay complexity gets an estimator for the return channel; the attribution line gains an intervention-identified per-message credit beside its human labels.
- **If false:** If the return recovers under 0.4 of the matched loss while the brief carries at least 0.6, the paper's brief-distortion reading stands with an identified number and verbatim briefs are the recipe; if both channels carry under 2 points and the matched loss stands, context separation itself costs the points and the recipe is not to delegate adjudicated lookups; if the matched loss is under 2 points, the headline of 2611.16526 is a budget-and-instruction artifact and every same-model orchestration comparison owes a matched protocol; in every branch the field gets its first token-counted return curve and its first matched delegation loss.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.16526 sec. 7 (the trade-off sentence) and sec. 6 ('targeted mechanisms for communicating evidence'); 2607.16133 sec. 7 ('Future work should develop quantitative estimators for both'); 2611.17041 abstract (fetched): 'subagents must return reliable evidence', a rubric on 'the research utility of each subagent report'; 2606.09730 abstract (fetched): 'constraining subagents to return results'; 2611.13254 sec. 4.2. Who pays: every harness that returns final answers from subagents (Claude Code subagents, OpenAI Agents SDK handoffs, Magentic-One's ledger); delegation-training teams whose rubric grades the return; MAS-versus-SAS authors whose comparisons sit at an unreported rate.
- **Impact ceiling:** **floor**: gradual curve or $G < 2$ pp: a footnote that the return channel for fact lookups is high-complexity or that Lost in Delegation's loss did not pass through it; cited by 2607.16133's successors and the paper's authors. Requires steps 1-4. Judgment p 0.35.; **middle**: knee at or under 80 tokens on both headline models with the post-cutoff excess closing at $R_1$: a measurement with a schema consequence any orchestrator harness can adopt and a quantitative relay complexity for one channel; proper idea, one community (harness builders) changes a default. Requires steps 1-5 and both $R_1$ schemas. Judgment p 0.40.; **ceiling**: the same knee shape on a second task family with execution-based scoring (a SWE-style subagent return or ClawArena-Team), so 'return rate operated at' becomes a reported column in MAS-versus-SAS papers and the structured return a default in two public harnesses. Requires about 20 more GPU-hours. Judgment p 0.25.
- **Relevance:** L4 all routes (a handoff measured for what it costs in tokens and accuracy, with a schema consequence); Narasimhan route through the MAS-versus-SAS measurement register; HAL and evaluators through L1 (frozen traces remove the budget and prompt confounds); product teams directly. L2 at the margin (LEAD-RL's rubric is the training consumer); L3 only as tokens saved per return; L5 zero. Jacob's edge: direct, rate-distortion, sufficiency and the information bottleneck are his to check and say in a talk; the design has no learned component.
- **Kill probe:** Steps 1-5: frozen traces on rebuilt GDP and Nobel sets, five return rates, gpt-oss-120b and GPT-5 (Qwen as sign check); about 12 GPU-hours and $415; 8 days; dead if $\phi(R_1) < 0.4$ on both headline models under both schemas (interval upper end under 0.6) or $G < 2$ pp on both.
- **Density and ownership:** Occupied: the information-bottleneck objective for inter-agent relays (2607.16133; 2606.13733's min-cut bound; 2604.02460's data-processing argument; GoAgent 2603.19677 as a method; IMAC 1911.06992 and CGIBNet 2112.10374 in MARL); the single-point measurement of the answer-only return (2611.16526); the shown-rate design for a judge (2610.15938, fetched 2026-11-15: 'what the judge was shown mattered more than which judge it was'; 'About a tenth of the source did almost all'); harness pressure on 'return results properly' (SearchSwarm 2606.09730; MS-Eval 2610.22869's MAD-SAE benchmark with isolated contexts); return rubrics in training (LEAD-RL 2611.17041). Unoccupied in every fetched source: a rate sweep of the executor-to-orchestrator return on frozen traces, the orchestrator's decision as the relevant variable, the knee as an estimated relay complexity, the orchestrator's prior as deco…
- **Why now:** 2607.16133 (2026-07-17); 2611.16526 (2026-11-12) with public-API ground truth; 2611.17041 and 2606.09730 as training consumers with a rubric and no schema; 2610.15938 (2026-10-11) as the shown-rate design in another role; the two open models serve on one H100 under vLLM.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Premise numbers fetched with denominators from the card: Table 1 means over four models and four datasets, forced delegation $0.77 \to 0.66$ pre to post against the single agent's $0.77 \to 0.75$; forced below the single agent in 21 of 32 model x dataset x cutoff cells; GPT-5 post-cutoff GDP $0.89 \to 0.35$ (forced); GPT-OSS pre-cutoff GDP $0.92 \to 0.65 / 0.73$; Qwen gains under forced delegation in 6 of 8 cells, which is why the headline names gpt-oss-120b and GPT-5 and Qwen is a sign-check arm (a 'loss' headline cannot name a model whose cells gain). The quantity $\rho_{80} = [\bar p(D(1,0… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W46-07 at about 12 GPU-hours and $415 in 8 days kills the headline if the return channel carries under 2 pp on frozen traces or the 80-token block recovers under 0.4 of the full-trace gap; C-W46-08 step 1 at 25 GPU-hours kills the headline cell directly ($\rho_{80} < 0.4$, upper end under 0.6). Both outcomes are citable: the negative is the first token-counted statement that the return channel on fact lookups is high-complexity or that the loss is a protocol artifact. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route A, three papers that disagree in print on where the loss between agents sits: 2611.16526 (transmission: the orchestrator 'receives neither the executor's intermediate trajectory nor the contents returned by its web tools', and the fix needs 'targeted mechanisms'), 2607.16133 (the aggregator's input is lossless; the trade-off lives in worker-to-worker relays), 2611.13254 (attention: evidence delivered and unused in 88% of failed runs that held it); plus harness and training pressure (SearchSwarm, LEAD-RL) — two source types (papers; released harness and training recipes). Route B: a rule… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Consumers with actions: orchestration harness builders (return schema default; report return tokens), MAS-versus-SAS evaluators and theorists (match budget and instruction; report the return rate; estimate relay complexity instead of assigning it), delegation-training teams (schema before rubric), failure-attribution benchmark owners (an intervention-identified label beside the human one), product teams. One community (orchestration harnesses) must change a default if true; community-wide only at the ceiling. Proper-shaped. |
| G4 | mechanism and consequence | Mechanism: the orchestrator decides accept / re-delegate / override by weighing a bare answer against its own belief, which is wrong post-cutoff by construction; the trace content that would change that decision (did a page state the answer; did a tool fail) is a few bits, cheap to send and absent at the answer-only operating point; the same prior enters the brief as a folded-in guess (C-W46-10 measures both leaks). Consequence: at least half recovered at 80 tokens, ship the schema and report the rate; under 0.4 with the brief carrying the loss, pass items verbatim; neither, do not isolate co… |
| G5 | durability; lab-adjacent | Durable as a ruler: the return-rate curve and the matched factorial apply to any orchestrator harness and model generation; the specific 80-token knee and the 9-11 point loss expire with the models. Lab-adjacent: a measurement of a shipped practice and of a published comparison, not a frontier lab's core recipe; the lane positioning (measurement register only) is met. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17) before any probe is elaborated beyond design level. Density on 2026-11-15: the imports' queries returned 13 (field words) and 82 (lane words) hits for the return channel and 22 / 54 / 15 for the attribution and swap words; this run's return-format query 15 hits all time, 3 since 2026-10-16 (about one on-point orchestration-communication paper a month); the lane as a whole runs about 3.4 compaction-agent papers a week (CL-W45-08 kill), but the orchestrator-subagent sub-lane is the less dense one by the imports' own counts. Nearest: 2607.1613… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-07 | The return is an operating point: the orchestrator's error against the return rate (final answer / 80-token evidence bl… | Steps 1-5: frozen traces on rebuilt GDP and Nobel sets, five return rates, gpt-oss-120b and GPT-5 (Qwen as sign check); about 12 GPU-hours and $415; 8 days; dead if $\phi(R_1) < 0.4$ on both headline models under both schemas (interval upp… | proposed | — |
| C-W46-08 | Who lost the item: randomised replacement of the brief and the return at the single agent's tool budget and instruction… | Step 1: six arms x 80 prompts x 5 runs on gpt-oss-120b with a cached web, about 25 GPU-hours and $440, 7 days; dead for the headline if $\rho_{80} < 0.4$ on both models (upper end under 0.6); dead as an import if both swaps move accuracy u… | proposed | — |
| C-W46-10 | The orchestrator's closed-book answer as the leak: a judge-free count of lost items whose brief or final answer carries… | Step 1 on the parents' logs, $0, 1 day; dead if $\pi < 0.2$ post-cutoff on both models or the leak rate does not separate lost from non-lost items by 5 points. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-07** (Sunday run), or run `/kill C-W46-07` in a session.
2. If it survives: `/redteam C-W46-07`, then the probe as pre-registered — Steps 1-5: frozen traces on rebuilt GDP and Nobel sets, five return rates, gpt-oss-120b and GPT-5 (Qwen as sign check); about 12 GPU-hours and $415; 8 days; dead if $\phi(R_1) < 0.4$ on both headline models under both schemas (interval upper end under 0.6) or $G < 2$ pp on both.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down from the L4 lane sentence and 2611.16526 sec. 7's asserted trade-off; the two S10 imports attached as probes C-W46-07 and C-W46-08 with their pre-registered disagreement recorded as the fork; C-W46-10 attached as the mechanism probe; headline quantifier (at least half of the matched loss recovered at 80 tokens) set at the C-W46-08 kill; models named gpt-oss-…
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 4: born W46: lifts both S10 imports; proper-shaped, 12 GPU-h probe; two imports disagree on the channel so the probes decide a fork; concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-03`, version 1)
- probe `C-W46-07`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-08`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-10`: `data/candidates/2026-W46.jsonl`
