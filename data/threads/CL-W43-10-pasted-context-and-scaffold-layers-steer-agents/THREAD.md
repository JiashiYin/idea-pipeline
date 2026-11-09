# Pasted context and scaffold layers steer agents by presence, not content: a same-length block from the wrong source moves a model's yield as much as the right one does.

`CL-W43-10` · lane **L1** · status **killed** · rank None · position solo · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search owed; the HRP authors are the race). Grade on paper: open pending kill search; five probes, cheapest an exact 24 GPU-h readout. Next action: see First steps.

## The claim

- **Headline:** Pasted context and scaffold layers steer agents by presence, not content: a same-length block from the wrong source moves a model's yield as much as the right one does.
- **Current belief (the field's):** Harness papers read a per-model context effect as the information in the block: 2610.28802's abstract recommends 'combining configurations for broader coverage' and reports a targeted call-graph block raising weaker models' yield; investigator-agent papers attribute a semantic layer's harm to its content (C-W43-07's card).
- **If true:** Every scaffold or context-engineering comparison needs a same-length placebo arm, the way drug trials do; leaderboard 'harness' columns are re-read as prompt-form effects; harness builders spend on form (an authoritative-looking block) before retrieval quality.
- **If false:** Content wins: the placebo moves nothing, the information in the block is what helps, and the open question is which models can use it (C-W43-06's habit ruler).

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper reads the H5 ceiling gain as induced by the instructions' content (sec. 5.3, Table 4) and leads its abstract with harnesses being 'judged by how an already trained model performs under them'; CL-W43-10's current belief quotes harness papers attributing per-model context effects to the information in the block. Who pays: harness-search and prompt-optimisation builders (the card's intro cites four), every scaffold paper that adds a system-instruction block and reports the gain as design, and the two deployment placebo probes of CL-W43-10, which need to know what a content effect looks like where it can be certified.
- **Impact ceiling:** **floor**: A short note on the released sandbox: the placebo ceiling-gain ratio per family with its rewording spread, cited by the next harness-geometry or prompt-sensitivity paper. Requires steps 0 to 2. Judgment p 0.5.; **middle**: The mechanism of CL-W43-10 in one solvable setting (the reference's valid-action mass, not the procedure, carries a prompt-only ceiling gain), adopted as the placebo arm that harness-search papers run before claiming a prompt revision raised what the harness offers. Requires the presence outcome plus the same computation on the paper's H1 to H4 with a placebo instruction block appended. Judgment…; **ceiling**: A rule for prompt-only harness revisions, confirmed at deployment scale by C-W43-07 and C-W43-20: a same-length placebo recovers a stated fraction of every instruction block's gain, so harness leaderboards add a placebo column. Requires both deployment probes to agree with the exact result. Judgment p 0.1.
- **Relevance:** Narasimhan (tau-family, scaffold sensitivity): direct, the certified form-versus-content split is the lane's attribution question. HAL (Narayanan): moderate, harness columns re-read. Evaluators and harness-search builders: direct. Industry: moderate (what to spend on in a system prompt). Jacob's edge: dynamic programming on finite graphs, a KL-regularised Bellman solve and an exact identity are his register; theoretical physics zero beyond the identity; GPU engineering small (one 2B model, batched forward passes).
- **Kill probe:** Steps 0 to 2 (about 24 GPU-hours, about $30 cloud or $0 on a local GPU, 5 days); dead if the wrong-content and content-free blocks give $\rho < 0.25$ on all three families across all rewordings and the inverted block gives $\rho < 0$.
- **Density and ownership:** From the card's fetched neighbours: FormatSpread 2310.11324 measures accuracy spread over meaning-preserving formats on frozen models (up to 76 points) with no control problem and no ceiling; Harness-Zero 2609.24974 and the co-evolving-harness paper 2609.09134 train under harnesses and never vary instruction content against a placebo; WHALE 2609.00196 searches harnesses by a fixed model's return. Occupied by the card: the identity, the H5 ceiling gain of 0.081 and the sandbox. Not occupied: any placebo or content-free instruction arm, any decomposition of a prompt-only ceiling gain. The kill search must use the neighbours' words (prompt sensitivity, instruction ablation, irrelevant instructions, system prompt, format robustness, KL-regularised reference, harness revision, prompt optimisation) and quote the limitation text of 2310.11324 and 2609.00196; density is counted on the day of wr…
- **Why now:** Card paper v2 2026-10-28 with code; the sandbox makes the placebo's effect on the ceiling exact. The identity is old; the flag is recorded.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-01 is about 24 GPU-h with an exact readout and a pre-registered kill (dead if wrong-content and content-free blocks give rho < 0.25 on all three families and the inverted block gives rho < 0); C-W44-05 is $250 with a $0 step 0 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route B: the ruler is the placebo increment relative to the true-content increment, identifiable with same-length blocks and matched run counts; pre-registered surprise in C-W43-20 (placebo >= half the true increment, judgment 0.5) against the field's content reading; 2026-11-02, pressure #3 adds a stated strain: B21 'Reversing the order of the observation fields leaves every optimal decision unchanged yet lowers a trained model's success from 85.0% to 19.2%' — a form effect with content held fixed, in print; route A now has a meta-paper (B21), leaderboards (B09, B12) and a model card (… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: every harness and context-engineering paper adds a placebo arm; benchmark owners re-read harness columns; product teams change what they paste |
| G4 | mechanism and consequence | pass: mechanism — an authoritative block changes the agent's search policy (fewer or more tool calls, 2610.28802's inverted dose: 144 graph-query calls with increment -6.5 vs 9 calls with +4.5), not its knowledge; consequence — spend on form or on retrieval |
| G5 | durability; lab-adjacent | pass as a ruler (applies to any agent and any block); the specific effect sizes are generation-bound |
| G6 | ownership, density, race window; position clause | open: density not measured (kill search owed); the placebo design is standard in medicine and the two cards' own papers skipped it, so 'why has nobody' needs the kill search's answer; race window unknown; 2026-11-02: 2610.37255 (card paper of C-W44-01) owns the ceiling/mismatch decomposition and the field-order null; its authors are the obvious next authors of the content-varied arm — race flag; the claim's ground is the same-length placebo (content varied, form fixed), which 2610.37255 did not run |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-07 | Placebo semantic layer: does form or content stop investigators looking | Two investigator models x four arms x 104 KramaBench tasks x k=2 (1,664 runs, ~15 H100-hours, 3 days): if placebo arms move pre-answer tool calls by less than a third of the true layer's change and within 2 SE of zero, dead. | killed | — |
| C-W43-20 | Wrong repository's call graph as the placebo for pasted static-analysis context | Three arms times three open models times four runs (about 60 GPU-hours, about $100, 7 days); dead if nothing clears two SE at $k = 4$ or if the placebo moves yield by under a third of the true block while the true block clears two SE. | proposed | — |
| C-W43-06 | No-scaffold habit as a ruler for the sign of scaffold effects | Arm 1 alone (5,810 MedicalHarness runs, ~80 H100-hours, 6 days): if habit-based sign accuracy is within one sign of accuracy-based on the effects clearing 2 SE, or ICC < 0.5, dead. | proposed | — |
| C-W44-01 | Placebo instructions in an exactly solved harness: does the ceiling rise through what the block says or that it is there | Steps 0 to 2 (about 24 GPU-hours, about $30 cloud or $0 on a local GPU, 5 days); dead if the wrong-content and content-free blocks give $\rho < 0.25$ on all three families across all rewordings and the inverted block gives $\rho < 0$. | proposed | — |
| C-W44-05 | Wrong fact at the boundary: is a harness-delivered block trusted over a tool call? | Step 0 (zero dollars, 2 days) then 2 harnesses x 2 models x about 8 qualifying tasks x 3 arms x 4 runs through the gateway (0 GPU-hours, about 250 dollars, 4 days); dead if no task qualifies, or if the verification ratio is under 0.3 with… | proposed | — |

## Kill search

### Concept level (CL-W43-10) — killed (2026-11-01)
occupied (Gate 6): the same-length wrong-content control on scaffold, plan, memory, skill and evidence blocks is in print from eight groups with the claim's own ruler computed per model (2608.23067 Table 3: rho = 0.79, 1.5, 0.15, 0.30); and the universal sentence is a published mixed result (Gate 2B): presence leads for two of four models on skills, for driving memory and for data-science skills; content leads for plans (+7.17), RAG rewrites (28-64 F1), constraint dilution (62-100%) and static-analysis notes (false assurances -19); the consequence the claim would deliver ('length-matched controls ... a minimum standard') is already stated in 2608.23067's abstract
Full record: [`data/reports/2026-W44-kill-CL-W43-10.md`](../../../data/reports/2026-W44-kill-CL-W43-10.md).
**Occupied by:** 2608.23067 (scaffold layer, per-model Delta_len/Delta_con, both signs; length-matched control named a minimum standard); 2609.20474 (harness-plan layer, content +7.17); 2610.27714 (memory layer, filler unbeaten); 2607.07504 (data agents); 2610.32876 (static-analysis notes, direction-aware)
**Why not done before:** done - enabling piece: skills (SKILL.md) and repository context files made the pasted block a unit of defined length, so a byte-matched irrelevant block is a one-line substitution (2608.23067 sec. 3, 2026-08-24), on the 2022 random-label template (2202.12837); eight groups ran a length-, token- or word-matched placebo on a scaffold, plan, memory, skill or evidence block between 2026-04-22 and 2026-10-23; the claim's vocabulary (placebo, presence, form) is not the field's (length-matched irrelevant control, sham, token-matched filler, length-distracted, content-misled)
Closest neighbors (one-sentence trick; one-line difference):
- `2608.23067` Signal or Noise? A Benchmark Study of Agent Skills in Web Development — Four matched arms (no skill, target SKILL.md, a byte-matched irrelevant SKILL.md within 5%, leave-one-slice-out) on 31 public skills x 50 Web-Bench projects x 4 models, with only SKILL.md in the prompt so the length control is well defined; Delta_len = C2 - C… *Difference:* none - occupied: the claim's ruler per model (Sonnet 4 total -4.2 / length -3.3 / content -0.9; Qwen -2.3 / -3.5 / +1.2; GPT-5.1 -1.3 / -0.2 / -1.1; DeepSeek -2.0 / -0.6 / -1.4); names 'length-distracted' and 'content-misled' and makes the length-matched cont…
- `2609.20474` How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful… — Pair a prewritten task plan with domain-policy vocabulary shuffled and cut to the same whitespace-word count (Sham) in the same wrapper on tau^2-bench, five models, 265 matched cells, task-clustered bootstrap. *Difference:* none for the harness-plan layer - occupied, content reading: Fixed - Sham = +7.17 [1.15, 13.36]; Sham - Minimal = +1.89 [-3.45, +7.09], per model -4.5 to +7.3; Kimi's content effect near zero
- `2610.27714` When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation… — Treat the warm-up pool as a resampled random factor and add token-matched irrelevant-filler controls to five memory designs on HighwayEnv. *Difference:* none for the memory layer - occupied, presence reading: no retrieval design exceeds token-matched filler; a 15-token caution line reaches the ceiling
- `2607.07504` Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-… — One generated skill per data-science stage, 7,560 runs of component ablation plus a 1,512-run token-matched control. *Difference:* none for data agents - occupied: full skills perform similarly to task-irrelevant skill-formatted content; nothing beats the task prompt alone (p >= 0.396)
- `2606.06454` Scaffold, Not Vocabulary? A Controlled, Two-Tier, Pre-Registered Study of a Popperian Cod… — Pre-registered ablation of a prompt skill with a length-matched placebo, a labels-only scaffold and an execution oracle. *Difference:* form vs content on a prompt skill, pre-registered: gains track scaffold structure; placebo trails by 2.4 points on the small model; single-shot generation, not a tool loop
**Narrowest surviving headline:** none at claim level; the untested instance - 'in an exactly solved harness, a same-length wrong-content instruction block raises the certified ceiling by at least half of what the right block raises it' - is a footnote-grade orphan on 2610.37255 whose authors hold the solver
*Search degraded:* ['s2']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run from three orphans on one theme (prompts/11_claims.md rule: three orphans = a missing claim)
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 5 -> 4 after the kill run
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-10.md): killed — occupied (Gate 6): the same-length wrong-content control on scaffold, plan, memory, skill and evidence blocks is in print from eight groups with the claim's own ruler computed per model (2608.23067 Table 3: rho = 0.79, 1.5, 0.15, 0.30); and the universal sentence is a published mixed result (Gate 2B): presence leads for…
- 2026-11-01 — C-W43-07 killed: killed with claim CL-W43-10 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-10.md): 2607.07504 ran the token-matched task-irrelevant skill-formatted block on data-science agents (7,560 + 1,512 runs); 2608.23067's C2 is the design; a placebo semantic layer on KramaBench is a fifth instance, a footnote on 2610.20959 if kept as an orphan
- 2026-11-02 — claim open: pressure #3 (2026-11-02): B21 'Reversing the order of the observation fields leaves every optimal decision unchanged yet lowers a trained model's success from 85.0% to 19.2%' (2610.37255) — a form effect with content fixed, which is this claim's mechanism seen from the other side and a density flag; records R21, R09, R12, L13 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): C-W44-01 (card 2610.37255, exact placebo) and C-W44-05 (card 2610.32285, harness-delivered wrong fact) attached — both confirmed as probes of the presence-not-content sentence (system instructions and harness-delivered facts are scaffold layers); cheapest probe C-W43-07 -> C-W44-01; rank 4 -> 7 (two claims with broader consumers move above; the HRP race flag)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-10`, version 4)
- probe `C-W43-07`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-20`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-06`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-01`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-05`: `data/candidates/2026-W44.jsonl`
