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
- An objection with no evidence and no argument is deleted, not logged.
- "Conceded" objections stay in the log and go into the report's objection section; a report that hides a
  concession is a protocol bug.
- Kill if an objection goes unanswered after two rounds and it attacks the claim (not the framing).
- The generator may not change the claim mid-red-team; a changed claim is a new candidate.
