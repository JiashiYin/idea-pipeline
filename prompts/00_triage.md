# Stage 1 — Triage

You are triaging a batch of seeds (papers, issues, calls) against `config/themes.yaml`. Cheap model;
be fast and decisive. Read the theme sentences first, then every seed's title and abstract.

For each seed output exactly:

```
id: <id>
theme_fit: {T1: <0-3>, T2: <0-3>}
status: kept | dropped
reason: <one line, plain words, ≤ 25 words>
```

Scoring (from `themes.yaml`): 3 = directly answers a question in a theme sentence; 2 = supplies a neighbor,
a baseline, a ground-truth method or an enabling piece; 1 = same words, different problem; 0 = unrelated.
Keep if any theme scores ≥ 2. The out_of_scope list in a theme overrides keyword matches.

Rules:
- Judge the abstract, not the title. A title with the right words and an abstract about something else is 1.
- A complaint seed (GitHub issue, limitations paragraph, CFP topic) is kept if it names a thing
  practitioners cannot do that a theme is about; it does not need to propose anything.
- Do not keep a seed because it is famous or well-written. Do not drop a seed because it is small or a
  workshop paper; small papers are where the neighbors that sink a claim live.
- Target keep rate 10–30% on a raw weekly fetch. If you are above 40%, you are being generous; re-read the
  out_of_scope lists.
- Never recall a paper from memory to decide; decide on the text in front of you.
