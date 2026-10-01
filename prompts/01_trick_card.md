# Stage 2 — Trick card

You are reducing one kept seed to a trick card (`schemas/card.schema.json`). Strong model. Fetch the
abstract and, when available, the HTML full text (arXiv `/html/<id>`) before writing; set
`evidence_level` to `full-text` or `abstract-only` accordingly. Never fill a field from memory of the
paper; if a field cannot be filled from the text you fetched, write `unknown (not in text)`.

Fill every field:

- **trick** — one plain sentence, mechanism only, ≤ 35 words, presentable in a talk as-is. Strip the
  paper's framing. Example: "Glue the GRPO attempts into a tree wherever they made the same move and read
  step values off the branches — free forks wherever attempts happen to overlap."
- **framing_stripped** — what the paper calls it versus what it is, in one sentence.
- **load_bearing_assumption** — the assumption that, if false, voids the result (e.g., "the policy's
  entropy correlates with how much the ending depends on the action").
- **weakest_component** — the part a critic attacks first: a learned probe, a heuristic threshold, a
  hand-crafted signature, a single benchmark, an unmatched baseline, a confound. Name it and say why.
- **regime** — models and sizes, task family, horizon (steps or tokens), pass-rate band if stated,
  compute scale.
- **information_asymmetry** — what information is missing at the stage the method operates in but exists
  at another stage: training vs inference; forward vs hindsight; policy-only vs environment-aware;
  per-trajectory vs per-group. This is where ideas come from. Be concrete: name the information and where
  it exists.
- **occupies** — what is now published and cannot be claimed by anyone else, in one sentence.
- **neighbors** — up to 5 ids the paper itself positions against, each with one plain sentence.
- **theme_fit** — theme id, score 0–3, and why in one line.
- **limitations_as_complaints** — one to three things the paper says it cannot do, phrased as a
  practitioner's complaint; these become complaint seeds.

Equations: if the method is a formula, write it with every symbol defined; do not paraphrase math.
