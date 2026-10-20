# Stage 12 — Thread notes (Jacob's interface to every idea)

Purpose: one folder per claim under `data/threads/<claim-id>-<slug>/`, one `THREAD.md` in each, uniform, with the
essentials in a fixed order: headline, status line, the claim (belief / if true / if false), scorecard, gates,
probes with costs and verdicts, kill search, red team, first steps, decisions, Jacob's section, log, record paths.
Jacob reads threads and the digest; nothing else is required reading. The records stay the source of truth; the
note is the view.

## Procedure

1. `python scripts/threads.py [claim-id]` regenerates the note(s) and `data/threads/README.md` from the records.
   Run it after `/claims`, after every kill search and red team, and at the end of `/week`.
2. Enrich what the script cannot derive: in the kill-search and red-team sections, the two closest papers with
   their one-sentence tricks and verbatim limitation text; in First steps, the concrete first week if pursued
   (commands, data, GPU-hours, dollars); in Decisions, at most three. Write these into the records (candidate
   `kill_search.summary`, claim `decisions`, `first_steps`) so the next regeneration keeps them — never only into
   the note.
3. The `## Jacob` section is his. Never overwrite it. Before regenerating, read it: a mark (`promote`,
   `jacob-dropped`, `park: <reason>`) is applied to the claim and probe records with a history entry; a question is
   answered in the Log with a dated line. His marks win over the automatic ranking.
4. A thread exists for every claim, including claims born from `/capture` (status `thought` until graded).
   Orphan probes have no thread; three orphans on one theme are a missing claim — write it.
5. The digest links each ranked claim to its thread folder.

## Rules

Plain words; every term glossed once; the headline is one sentence. Status moves only on evidence (a kill-search
or probe result), never on discussion. A thread whose claim is killed keeps its folder with the verdict on top.
