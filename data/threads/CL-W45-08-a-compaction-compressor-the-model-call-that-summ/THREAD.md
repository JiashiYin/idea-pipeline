# A compaction compressor (the model call that summarises an agent's own history to fit its context) at its deployed sampling setting is a gauge, not a function of the history: re-compacting the same pre-compaction history accounts for at least one tenth of the variance of post-compaction harm (TRACE's burden: errored or repeated calls among the next actions), so the one-summary-per-boundary labels the lane builds on — TRACE's paired replay, SJC's 83% entry attribution, the corpus study's history-based triggers — are single readings of an instrument whose repeatability has never been measured.

`CL-W45-08` · lane **L4** · status **open** · rank 7 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established. Next action: see First steps.

## The claim

- **Headline:** A compaction compressor (the model call that summarises an agent's own history to fit its context) at its deployed sampling setting is a gauge, not a function of the history: re-compacting the same pre-compaction history accounts for at least one tenth of the variance of post-compaction harm (TRACE's burden: errored or repeated calls among the next actions), so the one-summary-per-boundary labels the lane builds on — TRACE's paired replay, SJC's 83% entry attribution, the corpus study's history-based triggers — are single readings of an instrument whose repeatability has never been measured.
- **Current belief (the field's):** 2610.08722 abstract (fetched 2026-11-09): the best trigger 'reaches held-out AUROC 0.66 (0.64 on the replicate's own label) against a same-boundary replicate of 0.72' — a replicate that, per its App. F (read in full by the import), splits 'each boundary's PRE and POST rollouts into disjoint halves' with the summary held fixed, so it measures the successor stage only; its authors write that 'the same numbers also support an attenuation reading' without a stage split. 2605.23296 abstract (fetched): 'the information it retains fluctuate[s] substantially from run to run, making the agent's retained knowledge unpredictable across runs' — a serving observation with no harm measurement. TRACE, SJC, HSC-Bench and 2611.06545 each use one summary per boundary.
- **If true:** Compaction evaluations add a writer-replicate arm ($m \geq 3$ re-compactions per boundary) beside the successor replicate and report the nested variance components; per-boundary harm labels and SJC's per-entry attribution are read as one draw; history-based triggers are read against the reliability ceiling $\rho_1 = \sigma^2_B / (\sigma^2_B + \sigma^2_W + \sigma^2_E / n)$ ($n$ continuations per summary; symbols defined in gate0); CL-W44-06's census and deletion arms average over writer draws; harness teams run the compressor at temperature 0 or ensemble $m$ draws if the share is high.
- **If false:** The compressor is effectively deterministic at the deployed setting (writer share under 0.10), single-summary labels are licensed, TRACE's successor-only replicate is the right yardstick, and the result is a protocol footnote; if the per-writer unsupported-policy rate is stable across re-compactions it is a calibratable writer bias (a column per writer model), not dice.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2610.08722's own sentence that 'the same numbers also support an attenuation reading' and its request for what corpora should ship; 2605.23296's observation that retained information fluctuates run to run; 2611.05650's call for replay certificates matched to the estimand. Who pays: compaction evaluators and corpus builders (TRACE, the corpus study, HSC-Bench, 2611.06545), gate and trigger builders (SJC, ACON), harness teams setting the compressor's sampling (Claude Code, Codex, OpenHands condenser, Pi), and CL-W44-06's own probes.
- **Impact ceiling:** **floor**: The first nested gauge study of a compaction compressor on one released harness, with the three variance shares and the reliability ceiling; cited by the corpus study's and TRACE's follow-ups. Judgment p 0.5.; **middle**: A writer-replicate arm becomes standard in compaction evaluations and corpora ship summary text; one gate (SJC) re-reports its attribution averaged over draws; CL-W44-06's census is redesigned. Judgment p 0.3.; **ceiling**: Compaction evaluation adopts the metrology frame (repeatability, reproducibility, bias) as its reporting standard, with the compressor's temperature a declared protocol parameter and a per-writer bias column. Judgment p 0.1.
- **Relevance:** Narasimhan (self-evolving agents, memory): direct — a written memory as an instrument reading. HAL and evaluators: moderate. Systems route: moderate (parallel compaction serving, 2605.23296). Industry (compaction and orchestrator teams): direct. L5: zero. Jacob's edge: variance components and nested designs are measurement statistics he knows from gauge studies; GPU numerics zero; physics zero.
- **Kill probe:** S3xF9 steps 1-3: about 30 GPU-h, about $100, 10 days; dead if the writer share is under 0.10 (interval's upper end under 0.20) on both writers; dead as a ruler if fewer than 100 of 150 snapshots re-execute identically.
- **Density and ownership:** arXiv API 2026-11-08 (import): (gauge OR repeatab* OR reproducib* OR 'measurement system' OR 'variance components' OR 'nested design' OR intraclass) AND compaction/handoff words AND agent AND LLM = 1, off point; ('run-to-run' OR stochastic* OR variance OR nondetermin* OR 'multiple runs' OR 'repeated runs' OR resampl* OR 're-summar*' OR 'multiple summaries') AND compaction words AND agent AND LLM = 13, on point only 2605.23296 (writer fluctuation as a serving issue) and 2606.03463 (a deterministic memory framework motivated by summarisation's nondeterminism). Occupied: the successor-stage replicate (2610.08722 App. F: half-half correlation 0.40, replicate AUROC 0.72), writer reproducibility in pieces (2611.06545's 1.2% vs 2.4% by writer; HSC-Bench's receiver dependence). The writer-stage repeatability is measured nowhere found. Pre-window precedent: the NIST/SEMATECH e-Handbook gauge-stu…
- **Why now:** 2611.06545 (2026-11) released a harness with re-executable state, two writers at stated temperatures and a ledger-checked outcome; 2610.08722 (2026-10-06) published the successor-only replicate and asked what corpora should ship; 2611.05650 (2026-11) made the replay certificate a norm; the metrology import was written 2026-11-08.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | nested model written first: $y_{bjk} = \mu + \alpha_b + \beta_{j(b)} + \epsilon_{k(bj)}$ for boundary $b$, re-compaction $j$ and continuation $k$, with variance components $\sigma^2_B$ (between histories), $\sigma^2_W$ (writer: between summaries of one history) and $\sigma^2_E$ (successor: between continuations of one summary); the headline quantity is the writer share $\sigma^2_W / (\sigma^2_B + \sigma^2_W + \sigma^2_E)$. Whose temperature: the writer's is stated (Qwen3-8B at 0.6, gpt-oss-20b at 1.0, the developers' settings) and a temperature-0 control arm separates sampling variance from s… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: about 30 GPU-h and $100, 10 days; kill written: writer share under 0.10 with the bootstrap interval's upper end under 0.20 on both writers |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: a ruler (the nested components and the reliability ceiling) with a pre-registered surprise — expected (judgment 0.45) a writer share of at least 0.25, 0.3 that it lies between 0.10 and 0.25, 0.25 that it is under 0.10 — against the field's one-summary-per-boundary practice; the corpus study's own authors name the attenuation reading and do not split the stages |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: compaction evaluators and corpus builders (TRACE 2608.06503, the corpus study 2610.08722, HSC-Bench, 2611.06545 — add the writer-replicate arm; ship summary text), gate and trigger builders (SJC 2610.20927, ACON, CL-W44-06's deletion arms — average over draws), harness and product teams (set the compressor's temperature or ensemble draws), failure-attribution standard authors (2611.05650 — a second certificate). Every compaction evaluation must change its protocol if true — community-wide within the lane |
| G4 | mechanism and consequence | mechanism: at the deployed temperature the writer's choice of which operations, values and next steps to keep varies across draws (the W44 import's fast entries most), and the successor acts on whichever draw it received, so harm inherits the writer's dice; consequence: at least three re-compactions per label and a ceiling on history-based triggers, or single-summary labels licensed |
| G5 | durability; lab-adjacent | durable: a gauge study applies to any compressor, harness and model generation; lab-adjacent (measurement of a shipped practice, not a lab's core recipe); L4 is very dense, so the race window is checked weekly |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: run-to-run, stochasticity, nondeterminism, repeated runs, re-summarisation, variance components, reliability, test-retest, intraclass). The import's density (2026-11-08): metrology words AND compaction words AND agent AND LLM = 1 off-point hit; lane role words AND compaction words = 13 hits, on point only 2605.23296 and 2606.03463 (motivation, no measurement); id_list 2610.08722 (full text), 2608.06503, 2610.20927, 2605.23296, 2606.03463, 2607.13071. Nobody re-compacts the same history or partitions harm by stage |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |


Also under this claim (no scorecard yet): import:2026-W45-S3xF9 (steps 1-3 about 30 GPU-h, about $100, 10 d on 2611.06545's released handoff-audit harness: 150 compaction boundaries x 4 re-compactions…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **import:2026-W45-S3xF9** (Sunday run), or run `/kill import:2026-W45-S3xF9` in a session.
2. If it survives: `/redteam import:2026-W45-S3xF9`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting import S3xF9; headline quantifier ('at least one tenth') set at the import's pre-registered kill, with the expected reading (a quarter) in the scorecard; took L4's second new-claim slot; concept-level kill search owed (rule 17); ranked 7

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-08`, version 1)
