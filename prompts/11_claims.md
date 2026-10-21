# Stage 11 — Claims (the headline layer)

Purpose: the generators produce probes — controls a paper skipped, a ruler for one effect, an audit of one
critic — and probes alone read as footnotes to other people's papers (Jacob, 2026-10-19). A research program
is a claim with probes under it. This stage writes and maintains the claims, so that what gets ranked, pursued
and pitched is a headline, and the probes are the cheap ways to kill it.

A **claim** is one plain sentence a stranger could repeat that would be news to the field if true.
Examples of the shape (not verdicts): "GPU physics engines trade physics for speed through solver iteration
caps, and RL policies exploit the difference." "Most published real-to-sim validity claims cannot be resolved
by their own real-world sample." "Reported scaffold gains on agent benchmarks are mostly effort and restart
effects."

Inputs: `config/themes.yaml`, `config/standards.md`, this week's candidates (`data/candidates/<week>.jsonl`),
imports (`data/seeds/<week>.jsonl`, stream import), pressure points (`data/reports/*-pressure-points.md`),
and `data/claims/claims.jsonl`.

## Procedure (weekly, after mutate, before kill searches)

0. Read `prompts/taste.md` — the judgment from the live sessions. Claims are reasoned, not assembled: every headline
   is a sentence about the world a stranger would repeat, and the operators in `02_mutate.md` are prompts for
   thinking, not templates.
1. Read the open claims. For every new candidate, attach it to the claim it tests (`claim_id`) or mark it
   `orphan`. An orphan is allowed but flagged; three orphans on the same theme are a missing claim.
2. Write new claims in two passes and record which pass produced each (`origin`). **Top-down** first: for each live
   lane and each scout theme, before looking at any probe, write the one sentence that would be news if true — from
   the lane sentence, this month's pressure points, the field's own stated assumptions (quoted), and `taste.md` §2;
   then look for probes, existing or new; a top-down claim with no probe under one GPU-week is a `thought` queued for
   `/sprint generate`. **Bottom-up** second: from orphans and imports, lift three probes on one theme into a claim.
   At most two new claims per lane per week, at least one open claim per live lane. Each claim record carries: `id` (CL-<week>-NN), `lane`,
   `headline` (one sentence), `current_belief` (what the field assumes, quoted from one source), `if_true`
   (the belief or ruler that changes, and for whom — Gate 3), `if_false` (what is learned anyway), `probes`
   (candidate ids with their kill-probe cost), `cheapest_probe`, `position` (solo | lab | both), `origin` (top-down | bottom-up | chat), `status`
   (thought | open | supported | refuted | killed | parked — `thought` is a claim from `/capture` not yet graded), `history`.
3. Grade each claim against the gates in `config/standards.md`: Gates 2–6 apply to the claim; Gate 1 is
   satisfied by its cheapest probe. Name the gate that fails. A claim with no probe under one GPU-week is a
   thought until one exists.
4. Update status from probe results: a probe's kill result refutes or weakens the claim; write which.
5. Rank open claims by the standards (community-wide consumers and durability weigh most), then rank probes
   within each claim by kill-probe cost. Write the ranking's reason in `grading`. The digest reports this order, and
   the monthly scoreboard reports survival through kill search and red team **by origin**, so the pass that earns its
   keep is visible.

## Rules

One sentence per headline; if it needs a second sentence it is two claims or not clear yet. `current_belief`
is quoted, never paraphrased from memory. No claim is called supported until a probe has run and been red-
teamed. A claim that is already the title of a published paper (fetched) is `killed` with the id. Jacob's
edits to `status` win.
