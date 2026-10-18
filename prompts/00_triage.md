# Stage 1 — Triage

You are triaging a batch of seeds (papers, issues, calls) against the lanes in `config/themes.yaml` (L1–L5;
if only `config/themes.proposed.yaml` exists, use it). Cheap model; be fast and decisive. Read the lane sentences
and the positioning spec first, then every seed's title and abstract. Retired theme ids (T1, T2) are never scored.

For each seed output exactly:

```
id: <id>
theme_fit: {L1: <0-3>, L2: <0-3>, L3: <0-3>, L4: <0-3>, L5: <0-3>}
source: <watch | complaint | pressure | import | owned | definitive | chat — copy from the seed's stream>
status: kept | dropped
reason: <one line, plain words, ≤ 25 words>
```

Scoring (from `themes.yaml`): 3 = directly answers a question in a lane sentence; 2 = supplies a neighbor,
a baseline, a ground-truth method or an enabling piece; 1 = same words, different problem; 0 = unrelated.
Keep if any lane scores ≥ 2. The out_of_scope list in a lane overrides keyword matches. A seed whose only fit is a
lab-contested recipe (L2's or L4's out_of_scope) is kept only as a neighbor for kill searches: score 2, note "neighbor".

Rules:
- Judge the abstract, not the title. A title with the right words and an abstract about something else is 1.
- A complaint seed (GitHub issue, limitations paragraph, CFP topic) is kept if it names a thing
  practitioners cannot do that a theme is about; it does not need to propose anything.
- Do not keep a seed because it is famous or well-written. Do not drop a seed because it is small or a
  workshop paper; small papers are where the neighbors that sink a claim live.
- Target keep rate 10–30% on a raw weekly fetch. If you are above 40%, you are being generous; re-read the
  out_of_scope lists.
- Never recall a paper from memory to decide; decide on the text in front of you.
