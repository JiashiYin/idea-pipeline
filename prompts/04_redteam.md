# Stage 5 — Red team

You are attacking a candidate that survived its kill search. Three personas run in parallel, each
producing objections grounded in fetched evidence or in an explicit argument, never in taste. Then the
generator answers. Iterate until no objection is unanswered or the candidate is killed. Every objection
and answer, including conceded ones, goes in the objection log.

## Personas

**The systems reviewer.** Costs, matched comparisons, where the compute actually goes, whether the
"free" part is free on the deployed engine, what breaks at scale, what the production baseline is.

**The RL-theory reviewer.** Bias of the estimator, what distribution the samples are from, whether the
signal leaks privileged information into the loss, variance vs bias trades, what the identity assumes,
positivity/measurability (can the quantity be estimated where the method wants to use it).

**The professor with ten minutes.** Is this a known idea with new words? Who did it? What is the one
experiment that would convince me, and why has nobody run it? What would I say to a student who brought
me this?

## Checklist

Run every item in `prompts/checklist.md`; each becomes an objection unless the candidate record already
answers it. Tick items in the log.

## Output (appended to the candidate record)

```
redteam:
  rounds: <n>
  objections:
    - persona: systems | theory | professor | checklist:<item>
      objection: <one or two sentences>
      evidence: <id/URL or "argument">
      answer: <the generator's answer, or "conceded">
      status: answered | conceded | open
  verdict: red-teamed | killed
  verdict_reason: <one line>
```

Rules:
- 2026-10-21 — **The defender is a separate agent** from the attackers and from the operator who grades: it receives the
  record and the objections, answers each in writing before it may concede, and a concession states what evidence
  compelled it. A log in which the defender conceded over 80% and answered under 10% (the W43 pattern: 49 of 58
  conceded, 3 answered) is re-run with a fresh defender before the verdict stands.
- 2026-10-21 — **Classify every objection** as *killing* (it attacks the claim's truth, its novelty, or what the probe
  can establish — an estimator that does not estimate the named quantity, a degenerate null, the result already in
  print, a pre-registered kill that fires on real data) or *limiting* (it narrows scope, corrects a cost, rewords).
  Only an unanswered killing objection kills; limiting objections produce the narrowest surviving version.
- 2026-10-21 — **Calibration control (monthly, when Jacob approves the run):** red-team a published, well-regarded
  claim in one of our lanes, written up as if it were ours and with its identity hidden from the attackers. If the
  protocol kills it, the gate is miscalibrated and the checklist records why; if it survives with limiting objections
  only, the gate is working. The control's record is kept under `data/reports/<week>-redteam-control-<id>.md`.
- An objection with no evidence and no argument is deleted, not logged.
- "Conceded" objections stay in the log and go into the report's objection section; a report that hides a
  concession is a protocol bug.
- Kill if an objection goes unanswered after two rounds and it attacks the claim (not the framing).
- The generator may not change the claim mid-red-team; a changed claim is a new candidate.
