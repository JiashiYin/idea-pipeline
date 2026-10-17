Run stage 9 (definitive-comparison prospecting) for ISO week $ARGUMENTS.

Read `prompts/09_definitive.md`, `config/themes.yaml`, `config/standards.md`, the Comparisons section of
`prompts/checklist.md`, and the density files in `data/candidates/*-density.json`. Identify dense lanes (≥ 8 recipe
papers in 12 months via the arXiv API with mechanism and role words). For each (≤ 4), one subagent checks whether a
definitive comparison exists (experimental sections read, not abstracts) and, if not, writes the spec. File specs as
candidates with `source: definitive`, `position: lab`, `status: parked`. Print one line per lane: lane, recipe count,
existing comparison (id) or "none — spec filed", estimated GPU-hours.
