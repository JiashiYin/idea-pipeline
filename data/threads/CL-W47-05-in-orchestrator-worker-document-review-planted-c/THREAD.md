# In orchestrator-worker document review, planted conflicts vanish at the lead's partition, not in the workers' return summaries: a random split of the same documents among the same workers co-locates a planted conflict within 10 points of the observed rate, and on contexts that hold both numbers a report written through a return-style summary flags the conflict at least 15 points more often per surviving pair than one written from the raw context.

`CL-W47-05` · lane **L4** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G2B (first clause's surprise is 2605.26174's pre-registered thesis and the seed's own sec. 5 reading); G4 (if_true equals the seed's recommended fix: overlapping assignment); G1 for the $0 arms (seed released no traces, profiler or planted edits). Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** In orchestrator-worker document review, planted conflicts vanish at the lead's partition, not in the workers' return summaries: a random split of the same documents among the same workers co-locates a planted conflict within 10 points of the observed rate, and on contexts that hold both numbers a report written through a return-style summary flags the conflict at least 15 points more often per surviving pair than one written from the raw context.
- **Current belief (the field's):** 2611.22245 (card, full text) locates the loss at 'the largest drop in evidence preservation at the worker-to-lead handoff' (sec. 1) under the noun 'memory inconsistency', with the mechanism stated as a summariser's deficit: 'workers summarizing isolated partitions lack the cross-document context needed to recognize figures that appear unproblematic in isolation as conflicting across documents' (sec. 5); it reads 72.2% vs 33.3% Judge Pass as 'conflict resolution depends heavily on provenance' (sec. 5). The card's own count: of 301 retrieved pairs, 190 were Split (no worker ever saw both numbers) and 56 of 111 Same pairs were dropped by summaries; under no delegation 220 pairs sat in one context and only 71 were flagged. Yan 2025 'recommends sharing full agent traces' and design guides 'return condensed summaries to the lead' (sec. 2.2).
- **If true:** 'Lost in delegation' numbers are read as partition design times worker count, not as memory or summary failures; multi-agent benchmarks that plant distributed evidence report the permutation null for their lead's partition; return-summary research stops treating the summary as a pure loss channel and measures the flag rate per surviving pair; the fix moves from 'share full traces' to how documents are assigned.
- **If false:** If the lead places documents with information (observed completeness differs from the null by over 0.10 for two of three models): the partition is a lead property and the claim is false; a lead-placement measurement is the residue. If $s_S - s_R < 0.05$: the summary is a pure loss channel for this cargo and the 72.2% is a provenance effect of the Required lead.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's Limitations ('separate the effect of distribution from retrieval difficulty') and its own Same / Split split (sec. 4.4); the W46 sibling card 2611.16526 measured the downward brief and inferred the upward loss; HiddenBench (Li et al. 2026, card neighbour) distributes facts by design and never asks how a lead distributes them. Who pays: orchestration-harness teams choosing how a lead assigns documents (Claude Code SDK, Codex SDK workflows), benchmark owners of planted-conflict suites, and the multi-agent-versus-single-agent comparison community (57 controlled comparisons in twelve months per the CL-W46-03 record), whose delegation penalties carry an unreported pair completeness.
- **Impact ceiling:** **floor**: A note with $PC_{\mathrm{obs}}$ against the null per model and the planting-design arithmetic, cited by the card paper's v3 and the next planted-conflict benchmark. Requires steps 0-2. Judgment 0.5.; **middle**: Pair completeness reported beside every delegation result in one benchmark and an entity-keyed overlapping assignment shipped as a lead instruction in one harness, with the Split cell measured before and after. Requires one intervention run (about 40 GPU-hours more). Judgment 0.2.; **ceiling**: Blocking metrics (pair completeness, reduction ratio) become the standard decomposition of delegation loss into placement and handoff for multi-agent evaluations. Requires adoption by two benchmark owners. Judgment 0.07.
- **Relevance:** Narasimhan route: indirect (multi-agent credit in L2 needs the placement term separated from the handoff term). HAL route: zero. Evaluators: direct. Industry: direct (lead assignment instructions). Jacob's edge: a permutation null and a combinatorial expectation are things he checks by hand; physics zero; GPUs zero.
- **Kill probe:** Steps 0-2: $0, 0 GPU-hours, 4 days on the traces; 40 GPU-hours and 5 days on the fallback; dead if $|PC_{\mathrm{obs}} - \mathbb{E}_{\pi'}[PC]| > 0.10$ with the interval excluding zero for two of three models.
- **Density and ownership:** From the card and the repo's records, not re-counted this week: the return-format sweep is occupied (PACT 2606.05304; 2610.06069; 2607.16133, per the CL-W46-03 record) and this probe does not touch the return; the distributed-information setting is HiddenBench's (facts distributed by design) and 2607.16133's SAS-Plan arm (same sub-instructions in one context); no card neighbour or kill-record occupant tests the lead's placement against a null. Pre-window precedents: blocking and pair completeness in record linkage (Christen 2012 survey; Fellegi and Sunter 1969 for the comparison step the split pairs never reach) and the hidden-profile paradigm (Stasser and Titus 1985: groups fail to pool unshared information). Owner: the card paper's authors hold the profiler traces; Harvey holds the tasks. Role words for the kill search: task allocation, document assignment, work partitioning, subtask…
- **Why now:** 2611.22245 v2 2026-11-18 (per-worker read sets and planted locations in one profiler); 2611.16526 2026-11-12 (the downward brief measured, the placement never). Flag: release status unknown.
- **Register, and what it is not:** Measurement with a reporting consequence (pair completeness beside delegation results) and a small recipe (overlapping, entity-keyed assignment). It is not a return-format study (occupied), not a new orchestration policy, and not the card paper's benchmark on another domain.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched with denominators (438 pooled observations; 301 retrieved pairs, 190 Split, 111 Same, 56 dropped; 106/301 survive the summary; 220 pairs under None with 71 flagged; Judge Pass 72.2% vs 17.1%/33.3% — card Table 1, secs. 4.3-4.4; denominators 72 and 35 inferred and marked). Conditioning set: the permutation null re-assigns the same documents to the same number of workers, so the only randomness is the assignment; the summary arm holds the context fixed and the writer's temperature is the harness's (to be read from the release). Two quantified clauses in on… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W47-10 is $0 and four days on released traces (fallback 40 GPU-h, under a week); C-W47-11 under 50 GPU-h. Kills written. Flag: the card says release status of profiler, traces and tasks is unknown — step 0 is the release check. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'lost in delegation' decomposed into partition, summary and synthesis terms with a null for the first. Surprise three ways: expected — completeness within 10 points of the permutation null, summary raises the flag rate per surviving pair by $\geq 15$ points (judgment 0.4); field assumes — the summary is where conflicts disappear (card sec. 1, sec. 5); belief-changing — leads place with information (0.3) or $s_S - s_R < 0.05$ (0.3). Flag for the kill search: the hidden-profile literature (group decision making) and record-linkage blocking own the null's shape; grep 2611.22245… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: multi-agent benchmark owners (report the partition null), orchestration-recipe authors (assignment before summary format), delegation-loss measurers (2611.16526's authors; the W46 import), the L4 handoff thread. Proper-shaped. |
| G4 | mechanism and consequence | Mechanism: a lead that assigns documents without reading them splits a planted pair with probability $1 - 1/w$ for $w$ equiprobable workers (hypergeometric for unequal shares), so the Split share is a design constant; a summary written for a lead foregrounds anomalies the raw context buries in 220 pairs of noise, raising the flag rate on what survives. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the partition null applies to any delegated review benchmark; flag — one benchmark (Harvey LAB-style document review) and three models. |
| G6 | ownership, density, race window; position clause | Density owed at the kill search in the lane's role words (delegation, partition, hidden profile, distributed information, handoff note, relay sufficiency, return summary, conflict detection, evidence preservation) and the record-linkage words (blocking, pair completeness). Known neighbours from the card and records: PACT 2606.05304, 2610.06069, 2607.16133 (SAS-Plan arm), HiddenBench, 2611.16526. Why now: 2611.22245 (2026-11-18) is the first stage-wise trace of a planted conflict. Race: dense lane. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-10 | Split by lot: whether a lead's document partition co-locates a planted conflict any better than a random split of the s… | Steps 0-2: $0, 0 GPU-hours, 4 days on the traces; 40 GPU-hours and 5 days on the fallback; dead if $|PC_{\mathrm{obs}} - \mathbb{E}_{\pi'}[PC]| > 0.10$ with the interval excluding zero for two of three models. | killed | — |
| C-W47-11 | Louder after the summary: whether routing an agent's own reads through a return-style summary raises the conflict flag… | Steps 0-2: at most $150 or 50 GPU-hours, 5 days; dead if $s_S - s_R < 0.05$ with the interval covering zero; uninformative if $\kappa_S < 0.3$. | parked | — |

## Kill search

### Concept level (CL-W47-05) — killed (2026-11-22)
The partition-not-summary clause is 2605.26174's mechanism ('the cliff is a property of partitioning structure'), confirmed by a pre-registered re-run and released; the seed itself blames 'isolated partitions' and recommends overlapping assignment. The null needs a worker count the paper omits (implied 2.4-3.8 vs 'up to ten'). Residue: a probe on summary salience, redesign-owed.
Full record: [`/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-05.md`](../../..//home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-05.md).
**Occupied by:** 2605.26174 (first clause: mechanism, consequence, trace-does-not-repair; fixed partition, no lead choice, no null); 2611.22245 sec. 5 (Gate 2B and Gate 4 occupant for the first clause); second clause unoccupied as a measurement, with 2610.37624 (B3 summary at or below all-facts) and 2505.11556 (passive summarisation 0.241/0.713) as data against it
**Why not done before:** The partition mechanism was done, pre-registered and released (2605.26174, 2026-05-25); distribution-vs-content separation exists as a benchmark (CrossProfile 2610.37624, 2026-10-27) and a paradigm (HiddenBench 2505.11556). A permutation null on a lead's realised assignment is uncomputed because the only paper with a lead that chooses the assignment (2611.22245) printed neither worker counts nor assignments and released no traces, and the only released assignment schemes (2605.26174) fix the partition by hand so the null is degenerate. Enabling piece for the residue: Harvey LAB public (MIT, 2026-05-06).
Closest neighbors (one-sentence trick; one-line difference):
- `2605.26174` A Universal Cliff and a Design Fingerprint: Cross-Section Defect Detection Under LLM Orch… — Plant four contradictions between distant sections in each of four long documents, review under one agent and under five workers with fixed non-overlapping slices across ten models, and show every model that finds the defects alone loses two-thirds or more un… *Difference:* none for the first clause's mechanism and consequence ('the cliff is a property of partitioning structure'; the full trace 'does not repair this'); object differs: partition fixed by the harness, no lead choice, PC = 0 by design, no return-summary stage; ever…
- `2611.22245` Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents — Plant 73 numerical conflicts in 11 Harvey LAB tasks and trace both values through source reads, worker reports, lead evidence and the report under None, Optional and Required. *Difference:* the seed: splits the loss by Same/Split itself, blames 'isolated partitions', recommends overlapping assignment (Gate 2B and Gate 4 occupant); releases no traces, profiler or edits
- `2610.37624` Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions (CrossProfile) — Cross who holds supporting, decoy and irrelevant facts while holding their text fixed, compress the discussion into a budgeted memory by five policies, and read a separate decision from the memory alone. *Difference:* owns the 'vary who holds which evidence' design the seed's Limitations ask for; written evidence summary B3 at or below all-facts (72.0 vs 73.1; 58.7 vs 72.6) is a datum against the second clause; short contexts, decisions not flags, no lead partition
- `2505.11556` Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent… — 65 hidden-profile tasks; groups reach 30.1% under distributed facts against 80.7% for one agent with everything; forced disclosure lifts to 92.6-98.2%. *Difference:* facts distributed by design, no lead and no null; 'the failure lies in surfacing information, not reasoning over it'; 'Passive summarization yields more limited and model-dependent gains' (0.241/0.713) is a second datum against the second clause
- `2609.33485` DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation — Partition a long context across worker LLMs that ground locally while an RL-trained driver reasons over their returns. *Difference:* a method built on the partition as the lever; no null, no conflict cargo
*Search degraded:* ['s2', 'Q8 own-words query returned 1 (API phrase handling; no budget to re-run loose)', 'Q9 summarise-then-answer query returned 2 (too tight; community unsearched at density level)', 'arXiv HTML search has no phrase matching (two own-words searches defective)', 'complaint stream not searched (no…

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- C-W47-11 is parked — Steps 0-2: at most $150 or 50 GPU-hours, 5 days; dead if $s_S - s_R < 0.05$ with the interval covering zero; uninformative if $\kappa_S < 0.3$.: fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): two probes on the lead's partition and the summary's salience; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-05.md): killed — gate G2B (first clause's surprise is 2605.26174's pre-registered thesis and the seed's own sec. 5 reading); G4 (if_true equals the seed's recommended fix: overlapping assignment); G1 for the $0 arms (seed released no traces, profiler or planted edits); The partition-not-summary clause is 2605.…
- 2026-11-22 — C-W47-10 killed: W47 concept-level kill search of CL-W47-05: probe verdict killed. step 0 dead (no traces); the null's value needs the realised worker count, absent from the paper; its headline is 2605.26174's pre-registered conclusion and the seed's own sec. 5 reading; the $0 arithmetic (w_eff 2.4-3.8) is the one-sentence footnote
- 2026-11-22 — C-W47-11 parked: W47 concept-level kill search of CL-W47-05: probe verdict redesign-owed. step 0 dead (None captures unreleased); survives as a probe-sized residue on public Harvey LAB tasks (~$150, 5 days) with five design requirements: distance-band pre-registration against CrossProfile B3 and HiddenBench, net rate kappa_S s_S beside the conditional, salience separated from provenance, compaction state named, w…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-05`, version 2)
- probe `C-W47-10`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-11`: `data/candidates/2026-W47.jsonl`
