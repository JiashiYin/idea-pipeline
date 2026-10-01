# Public auto-research systems — what we borrow, what we don't

Checked 2026-10-01. One plain sentence per system, then the specific pattern taken or rejected. The point
of this file is to stop us hand-crafting something worse than what exists, and to be precise about why
our machine differs: the public systems automate the whole arc from idea to paper; ours automates the
part between the literature and one human's judgment, because that judgment is the bottleneck we have.

## Systems

**karpathy/autoresearch** — https://github.com/karpathy/autoresearch
An agent edits one file (`train.py`), trains for exactly five minutes, keeps the change if the single
metric (validation bits per byte) improves, and repeats — about a hundred experiments overnight, steered
by a human-edited `program.md`.
- *Borrow:* the single human-steering file (our `config/themes.yaml` + `CLAUDE.md`); the single editable
  surface so diffs stay reviewable; a fixed time budget per unit of work; one metric per experiment;
  append-only results. These are the design of our experiment hook (SPEC §12) and the reason our weekly
  budgets are hard numbers.
- *Don't borrow:* it has no literature stage at all; it optimizes a metric, not a position in a field.

**SakanaAI/AI-Scientist-v2** — https://github.com/sakanaai/ai-scientist-v2 · paper arXiv 2504.08066
From a topic description it brainstorms ideas, checks novelty against Semantic Scholar, runs a best-first
tree search over experiments with an experiment-manager agent (parallel workers, bounded debug depth),
then writes and reviews a paper; about $15–20 per run.
- *Borrow:* novelty checking as a tool call, not an opinion; parallel workers over independent nodes with
  a bounded retry depth (our stage fan-out and `max_debug_depth` for the experiment hook); a reviewer
  agent as a stage, not an afterthought.
- *Don't borrow:* the end-to-end autonomy. Their own README says v2 "doesn't necessarily produce better
  papers than v1" despite broader exploration — more idea volume did not help. That is the evidence for our
  design choice to spend compute on seeds and kills rather than generation. Also: their novelty check is
  Semantic-Scholar-only; ours adds conference exports and a one-line-difference table, because the
  neighbors that sink a paper are often abstracts-only posters.

**HKUDS/AI-Researcher** — https://github.com/HKUDS/AI-Researcher (paper on OpenReview; fetch blocked here,
summary from the earlier session's read)
Ingests reference papers, decomposes them into atomic ideas, generates and refines a research idea, then
implements and iterates; evaluated at two levels (detailed idea given vs reference papers only).
- *Borrow:* reference-paper ingestion as the start of ideation — this is our trick card: a paper reduced to
  mechanism, assumption, weakest component and information asymmetry before anything is generated.
- *Don't borrow:* generation from a fixed reference set; our seeds arrive weekly and are triaged against
  themes.

**SamuelSchmidgall/AgentLaboratory** — https://github.com/SamuelSchmidgall/AgentLaboratory
Literature review → experimentation → report writing by specialized agents, with a "copilot" mode that
inserts human feedback at stage boundaries.
- *Borrow:* the copilot pattern — human decisions at fixed gates, not continuously. Ours has exactly two
  gates: the theme file, and Sunday pruning of statuses; plus the ≤3 decisions at the end of each report.

**Si, Yang & Hashimoto (2024), "Can LLMs Generate Novel Research Ideas?"** — the large ideation study.
LLM-generated ideas were rated more novel than human ones on paper, less feasible, and the novelty edge
largely vanished after execution.
- *Borrow:* the conclusion. Our kill stage exists because the cheap part (ideas) is not where quality is
  decided; the killing experiment and its cost are mandatory fields, and a candidate without one under one
  GPU-week is parked.

**Tool layer worth reusing rather than rewriting**
- Semantic Scholar Graph API (`/paper/arXiv:<id>/citations|references`, author search) for citation
  expansion of the lab map; needs a key for real throughput.
- arXiv Atom API for the adjacent-lab and import streams (works everywhere; 3 s between calls).
- Conference `Downloads` pages (neurips.cc, icml.cc, iclr.cc) for abstracts-only neighbors before
  camera-ready; GitHub issues API for the complaint stream.
- Future-House `paper-qa` for grounded question answering over cached PDFs, if full-text reading becomes
  a bottleneck in the kill stage (**optional**; not in v0.1).

## How ours differs, in one paragraph

The public systems ask "can an agent do research end to end?" and spend their compute on generating and
executing many ideas. Ours asks "what does one new researcher need in order to pick well?" and spends its
compute on three things those systems do weakly: differentiated seeds (an adjacent-lab stream, a cross-field
import stream, a complaint stream — none of which is arXiv-by-keyword alone), sourced kills (named neighbors
with one-line differences, conference exports included, a why-now test, a costed killing experiment), and a
pre-argued report whose last section is the only part the human must think about. The human stays in the
loop at two fixed gates, and the lab map grows from what survives rather than from reputation.
