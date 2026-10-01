# idea-pipeline

A weekly machine that turns new papers, practitioner complaints and cross-field imports into a few
pre-argued research candidates for one researcher. Built to be generated and run by Claude Code.

Start here, in order: `SPEC.md` (what to build and how it scales) · `CLAUDE.md` (how the operator behaves)
· `LANDSCAPE.md` (what we borrow from public auto-research systems) · `BUILD_BRIEF.md` (paste into Claude
Code to build it).

Status 2026-10-01: specification complete; one reference script (`scripts/fetch_arxiv.py`) tested live;
first-week data bundled (`data/seeds/2026-W40*.jsonl`, three cards, one candidate with a kill record).
Everything else is specified, not built.

Quick check that the one live piece works:

    pip install pyyaml
    python scripts/fetch_arxiv.py --days 7 --dry-run
    python scripts/fetch_arxiv.py --days 7
