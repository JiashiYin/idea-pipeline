# Stage 3 — Mutate

You are generating candidates from one trick card by applying the seven operators. Strong model. Output
at most 4 candidates per card; prefer fewer, sharper ones. Each candidate serves a named theme or is not
written.

Operators (apply each; write a candidate only when the result is specific and testable):

1. **Principled replacement** — replace the learned or heuristic component (the `weakest_component`) with a
   principled quantity that exists at training time. Name the quantity and the identity that justifies it.
2. **Regime move** — move the method to the stage where the `information_asymmetry` field says the missing
   information exists (inference → training, forward → hindsight, policy-only → environment-aware).
3. **Unit change** — change the unit being allocated: tokens → steps → forks → environments → tasks, or
   the reverse. Say what is now allocated and what is saved.
4. **Ruler** — turn the mechanism into a measurement instrument. What would it grade, and what published
   signal would it grade first?
5. **Missing comparison** — the compute-matched or dose-matched comparison the paper did not run. Name
   both arms and the matched quantity.
6. **Import** — the other field's standard answer to this problem shape (design of experiments, control,
   statistical physics, market microstructure, operations research). Explain the import in two plain
   sentences; name the source field's term and the mapping.
7. **Role inversion** — a loss weight becomes a sampler decision; a sampler decision becomes a
   measurement; a mechanism becomes a control arm.

For each candidate output (`schemas/candidate.schema.json`):

```
cid: <computed by the orchestrator>
theme_id: L1 | L2 | L3 | L4 | L5   (lane ids; retired T1/T2 are never assigned)
from_card: <id>
operator: <1-7>
statement: <≤ 3 sentences: what we would do, on what, measured how>
claim: <the one sentence that would be true if it works>
why_now: <what landed recently that makes this possible or urgent; "nothing" is allowed and is a flag>
killing_experiment:
  design: <the cheapest experiment whose negative result kills the claim>
  cost_gpu_hours: <number>
  kills_if: <the observable result that kills it>
```

Rules:
- A candidate with no killing experiment is not a candidate; park it with a note.
- Do not write candidates that are the card's own method on a new benchmark.
- Do not write candidates that require a new learned model unless operator 1 cannot apply.
- If two operators give the same candidate, write it once and list both operators.
