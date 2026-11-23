# In orchestrator-worker document review, planted conflicts vanish at the lead's partition, not in the workers' return summaries: a random split of the same documents among the same workers co-locates a planted conflict within 10 points of the observed rate, and on contexts that hold both numbers a report written through a return-style summary flags the conflict at least 15 points more often per surviving pair than one written from the raw context.

`CL-W47-05` · lane **L4** · status **open** · rank — · position solo · refreshed 2026-11-22

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at concept level; Gate 6 open until the kill search (dense lane). Next action: see First steps.

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
| C-W47-10 | Split by lot: whether a lead's document partition co-locates a planted conflict any better than a random split of the s… | Steps 0-2: $0, 0 GPU-hours, 4 days on the traces; 40 GPU-hours and 5 days on the fallback; dead if $|PC_{\mathrm{obs}} - \mathbb{E}_{\pi'}[PC]| > 0.10$ with the interval excluding zero for two of three models. | proposed | — |
| C-W47-11 | Louder after the summary: whether routing an agent's own reads through a return-style summary raises the conflict flag… | Steps 0-2: at most $150 or 50 GPU-hours, 5 days; dead if $s_S - s_R < 0.05$ with the interval covering zero; uninformative if $\kappa_S < 0.3$. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W47-10** (Sunday run), or run `/kill C-W47-10` in a session.
2. If it survives: `/redteam C-W47-10`, then the probe as pre-registered — Steps 0-2: $0, 0 GPU-hours, 4 days on the traces; 40 GPU-hours and 5 days on the fallback; dead if $|PC_{\mathrm{obs}} - \mathbb{E}_{\pi'}[PC]| > 0.10$ with the interval excluding zero for two of three models.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): two probes on the lead's partition and the summary's salience; concept-level kill search scheduled this run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-05`, version 1)
- probe `C-W47-10`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-11`: `data/candidates/2026-W47.jsonl`
