# Stage 4 — Kill search

You are trying to kill one candidate before anyone spends time on it. Strong model with tools. Be
adversarial and sourced: every neighbor you name must come from a fetched abstract or page, with its id or
URL recorded. Memory is not a source.

Search in this order and record what you searched:
1. arXiv API: the candidate's claim rephrased three ways (mechanism words, problem words, the import
   field's words). Last 18 months first, then all time.
2. Semantic Scholar: citations and references of the card's paper and of the top two neighbors found in
   step 1 (skip with a `degraded: s2` note if unavailable).
3. Conference exports: the local index built by `scripts/fetch_exports.py` (NeurIPS/ICML/ICLR Downloads
   pages); abstracts-only hits count and are marked `abstract-only`.
4. The complaint stream: is anyone asking for exactly this in verl/vLLM/SWE-Gym issues? (Supports
   "why now"; does not kill.)

Write the kill record:

```
kill_search:
  date: <YYYY-MM-DD>
  queries: [<the strings you actually searched>]
  neighbors:   # at least 5, closest first
    - id: <arXiv id or venue:title>
      title: <...>
      trick: <one plain sentence, mechanism only>
      difference: <one line: what the candidate does that this does not, or "none — occupied">
      evidence_level: full-text | abstract-only
  occupied_by: <id or none>            # a neighbor whose difference line is "none"
  why_not_done:  <"an enabling piece landed: <what, when>" | "it is hard because <what>" | "no reason found">
  killing_experiment_check: <restate the experiment; confirm cost ≤ 1 GPU-week or set status parked>
  verdict: killed | survived-kill | parked
  verdict_reason: <one line>
```

Verdicts:
- **killed** if any neighbor's difference is "none", or if the "why not done" answer is "no reason found"
  and the search was thorough (≥ 8 neighbors examined), or if the claim is already a published negative.
- **parked** if the killing experiment costs more than one GPU-week or needs infrastructure that does not
  exist yet; record what would unpark it.
- **survived-kill** otherwise. Survival is provisional; the red team may still kill it.

Rules:
- Name the closest neighbor first, not the most famous.
- "Different domain" is not a difference unless the domain changes the mechanism. Say what changes.
- If the candidate survives only because its domain is new, say so in `verdict_reason`; that is a weak
  survival and the report must say so.
