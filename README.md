# idea-pipeline

A weekly machine that turns new papers, practitioner complaints and cross-field imports into a few
pre-argued research candidates for one researcher. Built to be generated and run by Claude Code.

Start here, in order: `SPEC.md` (what to build and how it scales) · `CLAUDE.md` (how the operator behaves)
· `LANDSCAPE.md` (what we borrow from public auto-research systems) · `BUILD_BRIEF.md` (paste into Claude
Code to build it).

Status 2026-10-17: operating. Three weeks of runs (W40–W42) in `data/`; generation stages 7–10 and the
weekly `/week` cycle added; `config/standards.md` is the second law; the operator skill is in `.claude/skills/`.
Only `scripts/fetch_arxiv.py` and `scripts/run_week.sh` are code; every other stage is an agent run from a slash
command. Durable home: the private GitHub repo `JiashiYin/idea-pipeline`; every run ends with commit and push.

Quick start on a fresh clone:

    pip install -r requirements.txt
    bash scripts/run_week.sh            # stage 0: arXiv watch + import streams for this ISO week
    claude                              # then: /week <YYYY-Www>  for the full cycle, or single stages
