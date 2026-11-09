# Top-$k$ retrieval logs cannot price a memory but can rank one against another, and ranking is all a fixed-size memory store ever does with the price: the expected effect of every same-size swap (replacing one retrieved memory by another at the same $k$) is orthogonal to the kernel that fixed size creates (the directions in value space the log cannot see — a two-line identity), and on the card's own pooled HotpotQA log at least one pairwise contrast (a difference of two memory values) in five among memories retrieved five or more times is determined where one memory value in a thousand is.

`CL-W45-07` · lane **L4** · status **open** · rank 8 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; race flag (three papers in five weeks). Next action: see First steps.

## The claim

- **Headline:** Top-$k$ retrieval logs cannot price a memory but can rank one against another, and ranking is all a fixed-size memory store ever does with the price: the expected effect of every same-size swap (replacing one retrieved memory by another at the same $k$) is orthogonal to the kernel that fixed size creates (the directions in value space the log cannot see — a two-line identity), and on the card's own pooled HotpotQA log at least one pairwise contrast (a difference of two memory values) in five among memories retrieved five or more times is determined where one memory value in a thousand is.
- **Current belief (the field's):** 2611.03289 abstract (fetched 2026-11-09): 'we prove that top-$k$ retrieval leaves every memory value undetermined, however many episodes are logged'; its remedy LEDGER 'retrieves so that the next log determines more' at 'a cost of 2.6 accuracy points on HotpotQA'; the card's information_asymmetry quotes the paper: 'the history fixes only the differences between values'. CMP 2610.02070 abstract (fetched): 'identified memory utility alone is insufficient for retention decisions'. RoMeRL, Memory-R2 and FadeMem score or learn per-memory values from fixed-size logs as if levels mattered (card neighbours).
- **If true:** Memory systems keep top-$k$ and lose nothing a retention, merge or retrieval policy can use; the proposed 'fraction of values determined' column becomes the fraction of contrasts determined, or is dropped; LEDGER's 2.6-point price is paid only when the store-size decision is on the table, which is when $k$ varies and the level is identified anyway; for RL memory agents the rewards fix the within-group contrasts GRPO-style objectives use, so the card's 'fixed by the learner and not by the rewards' applies to the level only.
- **If false:** The kernel under real top-$k$ logs is wide (aliasing of always-co-retrieved pairs, private stores), contrasts are undetermined too, and LEDGER's remedy is necessary for ranking, not only for pricing; or the LEDGER-value ranking retains a better store by at least 3 accuracy points, and the level bought something a store can act on.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card leaves the decision consequence open ('the pre-registered real-data retention test was not completed.', F.7; 'Finding at query time the questions where spreading retrieval costs nothing is the open problem that remains.', sec. 6) and its synthetic retention test ranks the truth below the average (5.52 against 7.14 of 300, F.7); CMP 2610.02070 states the retention gap from the other side ('identified memory utility alone is insufficient for retention decisions'). Who pays: memory-system builders (Mem0-, Letta-, FadeMem-class forgetting and retention) deciding whether to change retrieval in response to the card; memory-benchmark owners deciding whether to add the proposed determined-fraction column; RL memory-agent authors (RoMeRL, Memory-R2) reading the card's 'fixed by the learner' sentence.
- **Impact ceiling:** **floor**: A short note: the fixed-size kernel is orthogonal to every same-size swap, with the fraction of contrasts determined on the card's public setup and the completed retention test; cited as the reply to LEDGER. Requires steps 0 and 1. Judgment p 0.55.; **middle**: Memory benchmarks report contrasts determined (or nothing) instead of values determined; LEDGER-style retrieval changes leave recipes; the retention test on real data settles the synthetic ordering. Requires the expected result on two corpora (HotpotQA and LoCoMo). Judgment p 0.25.; **ceiling**: The general statement — identifiability is judged against the decision's functional space, not the parameter — adopted for the card's own scope list (tools an agent calls, passages a generator reads, slates a recommender shows), where the same fixed-size kernel appears and the same swap orthogonality holds. Judgment p 0.1.
- **Relevance:** L4 (Narasimhan's self-evolving memory interest; product memory teams): direct, the measurement register the lane demands with a recipe consequence (do not change retrieval to price memories). L2: moderate, the RL-credit reading (rewards fix contrasts, not levels). L1: small, a benchmark column. Systems routes: zero. Industry: memory products deciding on retrieval changes. Jacob's edge: the identity is linear algebra of estimable functions, napkin-checkable; GPUs zero.
- **Kill probe:** Step 0 at $0-10 (two days, the kernel computation on regenerated or released logs) and step 1 at about $20 (three days, 300 held-out questions x five rankings); 0 GPU-hours; dead if $F_{\mathrm{pair}} < 0.20$ under top-$k$ while LEDGER's log exceeds 0.60, or if LEDGER's values beat top-$k$ contrasts in retention by at least 3 points with the interval excluding zero.
- **Density and ownership:** arXiv API 2026-11-09, twelve months: (estimable OR identifiab* OR 'design matrix') AND memory AND agent AND (retention OR forgetting OR prune OR Shapley) = 33, on target LEDGER 2611.03289, CMP 2610.02070 (positivity failure for never-retrieved memories, inverse-propensity estimation under reserved random slots, retention insufficiency), 2611.03930 (task-conditioned utility by paired with/without, a designed measurement), 2607.17545 (retain versus consolidate by budget), 2610.07100 (category-conditioned retention threshold), MemPrice 2610.24955, 2610.35496 (trajectory deletion costs in coding agents); (Shapley OR 'data valuation' OR 'memory value' OR 'memory utility') AND agent memory AND (retention OR forgetting OR pruning) = 32, on target the same plus 2606.12945 (multi-factor memory value model) and 2608.04562 (Shapley valuation of agent skills). Three identifiability-of-memory-utilit…
- **Why now:** LEDGER (2026-11-02) names the kernel, publishes a reproducible setup and leaves the retention test incomplete; CMP (2026-10-01) states the retention gap; the identity is textbook, recorded as the flag.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | the identity before the estimator: with $(\mathbf{x}_S)_B = \mathbb{1}[B \subseteq S]$ the design row of a retrieved set $S$ and Theorem 1's kernel vectors $\mathbf{h}_B = \sum_{j \notin B} \mathbf{e}_{B \cup \{j\}} - (k - |B|)\,\mathbf{e}_B$ for $|B| < d$ ($d$ the dividend resolution), $$(\mathbf{x}_{S'} - \mathbf{x}_{S})^{\top}\mathbf{h}_B = 0 \quad \text{for every } |B| < d \text{ and every } |S'| = |S| = k.$$ The determined-contrast fraction $F_{\mathrm{pair}}$ is a function of the log's design matrix alone, computed before any outcome is read (the card's kernel test with $\tau = 10^{-8}$… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: about $30, 0 GPU-h, 5 days; kill written: $F_{\mathrm{pair}}$ under plain top-$k$ below 0.20 while LEDGER's size-varying log gives above 0.60 among the same memories; second kill: the LEDGER-value ranking beats the top-$k$ contrast ranking in retention by at least 3 points with the paired interval excluding zero; pre-registered uninformative reading: all five rankings within 2 points of random at 30% retention voids the retention clause (CMP's finding) while the kernel clause stands or falls on $F_{\mathrm{pair}}$ alone |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler (fraction of pairwise contrasts determined) is computable from any deployed retrieval trace with no outcomes; pre-registered surprise — expected (judgment 0.6) $F_{\mathrm{pair}} \geq 0.6$ against the card's 0.001 for levels; the field assumes the undetermined direction matters (the card's remedy and reporting proposal; RoMeRL's and Memory-R2's learned values); nobody in the fetched set says it is decision-irrelevant |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: memory-system builders (keep top-$k$; drop level-identifying retrieval), memory-benchmark owners (report contrasts determined, or nothing), RL memory-agent authors (read 'fixed by the learner' as a level statement only). One community (agent memory) — proper-shaped, with a general statement (identifiability judged against the decision space) as the ceiling |
| G4 | mechanism and consequence | mechanism: fixed $k$ confounds the intercept with the sum of values (Scheffé's one-way layout: only contrasts are estimable), and every decision a store makes is a same-size swap whose expected effect is a contrast; consequence: keep top-$k$, or LEDGER's rule is needed for ranking too |
| G5 | durability; lab-adjacent | durable: an identity about designs, independent of model, benchmark or memory recipe; lab-adjacent (the card's authors are the natural reviewers and could answer in a v2 — race flag) |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: estimable functions, contrasts, identifiability, positivity, Shapley, retention, memory utility, off-policy, slate). Nearest: CMP 2610.02070 (fetched; retention from the positivity side; 'no aggregation available to a retention policy predicts a memory's value on unseen queries'), 2611.03930 (paired with/without-memory design), 1605.04812 Swaminathan et al. (the kernel projected out for the policy estimand — the pre-window precedent for decision-space identifiability), Scheffé 1959 ch. 1-2 and Rao 1973 (estimable functions). Three identifiability-of-m… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-12 | What top-k cannot price it can still rank: the kernel fixed-size retrieval leaves is orthogonal to every swap a memory… | Step 0 at $0-10 (two days, the kernel computation on regenerated or released logs) and step 1 at about $20 (three days, 300 held-out questions x five rankings); 0 GPU-hours; dead if $F_{\mathrm{pair}} < 0.20$ under top-$k$ while LEDGER's l… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W45-12** (Sunday run), or run `/kill C-W45-12` in a session.
2. If it survives: `/redteam C-W45-12`, then the probe as pre-registered — Step 0 at $0-10 (two days, the kernel computation on regenerated or released logs) and step 1 at about $20 (three days, 300 held-out questions x five rankings); 0 GPU-hours; dead if $F_{\mathrm{pair}} < 0.20$ under top-$k$ while LEDGER's log exceeds 0.60, or if LEDGER's values beat top-$k$ contrasts in retention by at least 3 points with the interval excluding zero.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-12; headline quantifier ('at least one pairwise contrast in five') set at the probe's kill, with the expected reading (three in five) in the scorecard; took one of L4's two new-claim slots (the W44 orphan C-W44-17's 'L4 slot free next week' note is superseded; it stays orphan); concept-level kill search owed (rule 17); ranked 8

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-07`, version 1)
- probe `C-W45-12`: `data/candidates/2026-W45.jsonl`
