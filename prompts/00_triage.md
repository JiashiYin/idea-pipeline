# Stage 1 — Triage

You are triaging a batch of seeds (papers, issues, calls) against the lanes in `config/themes.yaml` (L1–L5) and
the open lane L0. Cheap model; be fast and decisive. Read the lane sentences, the `policy` and `open_lane` blocks and
the positioning spec first, then every seed's title and abstract. Retired theme ids (T1, T2) are never scored.

Lanes are priorities, not walls (2026-10-19). A seed that fits no lane is not dropped for that reason alone: it is kept
as a **scout** (lane L0) if it passes the headline test in `themes.yaml` — its result or gap can be said as one
sentence a stranger would repeat and that would be news if true; the positioning spec holds; it is not a frontier
lab's recipe fight. At most `scout_quota_per_week` scouts (config/generation.yaml) per week, best first; upvotes,
fame and polish are not reasons. The `scout` stream (Hugging Face daily papers, source `hf_daily`) is judged on the
headline test only; rank it by upvotes, read the top 30 abstracts, keep ≤ 5. A scout record gets `scout: true`,
`scout_theme: <two or three words naming the theme>`, `theme_fit: {L0: 3, ...}`, and a reason that states the
one-sentence headline it could carry.

For each seed output exactly:

```
id: <id>
theme_fit: {L1: <0-3>, L2: <0-3>, L3: <0-3>, L4: <0-3>, L5: <0-3>, L0: <0 or 3 — 3 only for a kept scout>}
source: <watch | complaint | pressure | import | owned | definitive | chat — copy from the seed's stream>
status: kept | dropped
reason: <one line, plain words, ≤ 25 words; for a scout, the headline it could carry>
scout: <true only for a kept L0 scout>   scout_theme: <two or three words, scouts only>
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
- 2026-10-18 — Every seed, dropped ones included, gets its own lane scores and its own reason line; a shared
  "domain application, no lane question" line with blanket zeros is a protocol bug (three of seven W42 subagents did
  it and had to redo their batches). Read the whole abstract; one W42 subagent cut abstracts at 700 characters.
- 2026-10-18 — The operator re-reads every kept abstract and every dropped seed that scored 1 before writing back;
  W42 calibration moved 11 of 214 verdicts (7 keeps demoted, 4 drops promoted).
