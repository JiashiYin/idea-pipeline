# Idea pipeline — the user guide

For Jacob. Read this when you have lost track of what the machine is, where to look, or what to do. Everything here
is true of the repository as it stands; when the machine changes, this file changes with it (CLAUDE.md asks the
operator to keep it so). The operator's manual is `CLAUDE.md`; the two laws are `config/themes.yaml` (lanes) and
`config/standards.md` (gates).

Last revised 2026-10-30.

## 1. What this is, in one paragraph

A machine that reads the week's papers, turns what it finds into **claims** — one-sentence headlines that would be
news to the field if true — and then tries to **kill** each claim as cheaply as possible with evidence it fetched,
before you spend a minute of your own time on it. It does the reading, the searching and the arguing by itself: every
Sunday night on a schedule, and any other time you run it from Claude Code. It leaves you one note per idea and one
page per week. Your part is to read the notes, write a word or two in each, and change the rules when you want
something different. The bar is all-or-nothing by your choice: most weeks it finds nothing golden, and the kill
records of those weeks are the product.

## 2. The words

| Word | Meaning |
| --- | --- |
| **Lane** (L1–L5) | A research direction you approved, in `config/themes.yaml`. Lanes are priorities, not walls: they decide where the fetch looks hardest, not what is allowed. |
| **Scout** (L0) | A paper outside every lane kept anyway because its result or gap could carry a headline. Three scouts on one theme propose a new lane. |
| **Seed** | A paper (or complaint, or import) the fetch found. ~200 a week. You never read seeds. |
| **Triage** | Sorting seeds into kept / dropped / scout, one reason line each. |
| **Card** | A kept paper boiled down to its mechanism, its weakest part, and what it leaves out. Ideas come from cards. You never read cards. |
| **Claim** | The headline — *ours*, not the paper's. Example: "GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference." The paper's own claim is the field's **current belief** that ours would overturn. |
| **Probe** | A concrete cheap experiment under a claim — a control a paper skipped, a ruler for one effect — with a cost and a pre-written "if we see X, dead." Probes alone are footnotes; claims are what you pitch. |
| **Kill search** | A 12-month literature search with fetched abstracts and quoted limitation sections: has someone done this? Verdict: killed / parked / survived-kill. |
| **Red team** | Three adversarial reviewers with fetched evidence, run on a survivor. Nothing is "proper" before it. |
| **Gates** G0–G6 | The standards in `config/standards.md`. Golden = passes all; proper = passes the hard ones; parked = fails one for a reason that can change; thought = not yet graded. |
| **Thread** | One folder per claim under `data/threads/`, with a `THREAD.md` in a fixed format. **Your interface.** |
| **Digest** | `data/digests/<week>.md`, one page written last on Sunday night. |

## 3. Where you look (and nowhere else)

1. **`data/threads/README.md`** — the index: every claim ranked, status, probes (how many survived), cheapest probe,
   failing gate, a link to its folder. Below the table: scouts kept recently and orphan probes waiting for a claim.
   A banner at the top tells you if a run is in progress or if marks of yours are waiting to be applied.
2. **`data/threads/<claim>/THREAD.md`** — the same sections in the same order, always:
   Status · The claim (headline / the field's belief / if true / if false) · Scorecard · Gates · Probes with costs and
   verdicts · Kill search (closest papers, each with its one-sentence trick and the one-line difference) · Red team ·
   First steps if pursued · Decisions for Jacob · **`## Jacob`** (yours) · Log · Records.
3. **`data/digests/<week>.md`** — what ran, what died, what survived, scouts and proposed lanes, ≤ 3 decisions.

Push and email notifications tell you when a scheduled run has finished and pushed.

## 4. How you steer — all by editing files; your edits always win

| Lever | File | What to write |
| --- | --- | --- |
| Judge an idea | `## Jacob` section of its `THREAD.md` | `promote` (spend my time on it), `jacob-dropped` (not worth it), `park: <reason>`, a question, a correction. Nothing else is required; you do not have to announce it — every session and every run starts by reading these (`python scripts/threads.py --inbox`). |
| Change what the machine looks for | `config/themes.yaml` | Add, narrow, retire a lane; adopt a proposed lane from the digest by pasting it in. The biggest lever. |
| Raise or lower the bar | `config/standards.md` | The gates. |
| Change what other fields it imports from | `config/fields.yaml` | Problem shapes × fields. |
| Change the fetch | `config/sources.yaml` | arXiv queries per lane, categories, the scout stream thresholds. |
| Change budgets and automation | `config/generation.yaml` | Kill searches per week, red teams per week, scout quota, thresholds. |

## 5. What happens by itself

- **Sunday 20:53 New York time** (scheduled task "Idea pipeline weekly run"): pull → apply your marks → fetch (lane
  queries + scout stream) → triage → cards → cross-field imports → mutate → claims (grade and rank) → kill searches on
  the top 3 probes, claim by claim → red teams on the survivors → refresh every thread note → digest → push.
- **Kill searches and red teams run automatically.** Since 2026-10-30 every new claim gets its concept-level kill
  search the week it is born (`kill_budget_per_week: 12`, run as parallel subagents), probes are designed only for
  claims that survive, with the neighbours' limitation text in hand, and survivors get red teams
  (`redteam_budget_per_week: 6`). Your `promote` mark triggers a kill search immediately at the next session or run.
- One-off scheduled runs (a kill run, a red-team run) are created when a batch is owed and would otherwise wait a
  week; they announce themselves in `data/runs/ACTIVE.json` while they run.

## 6. What you do in a Claude Code session (your PC, repo open)

Always start with `bash scripts/start.sh` — it pulls, shows whether a run is live, lists marks of yours waiting to be
applied, and prints the threads index. End with `bash scripts/done.sh "what you did"` — it refreshes the notes, commits
and pushes (rebasing once if the cloud pushed meanwhile). Yes, every time: the cloud writes to `main` while you are
away. The slash commands below pull for themselves, but your hand edits (marks, config) need the two scripts. Then:

| You want to… | Type |
| --- | --- |
| Push one idea to its next gate tonight (kill search → red team → report → the probe's run plan) | `/sprint CL-W43-01` |
| Generate more ideas from the backlog of kept papers | `/sprint generate` |
| Look at what the community is reading this week, outside the lanes | `/sprint scout` |
| Run the owed kill searches now instead of Sunday | `/sprint kill` |
| Talk through an existing idea with the full record loaded | `/discuss CL-W43-01` |
| File a new idea of your own (becomes a claim with `status: thought` and its own thread folder) | `/capture <one sentence>` |
| Have your `## Jacob` marks applied and your questions answered right now | `/inbox` |
| Refresh the notes after a run | `/thread all` (or `python scripts/threads.py`) |
| Feed the machine a paper or thread you spotted (Zhihu, X, a talk) | paste the link or id as a line in `data/inbox/links.md` from any device; the next run judges it and files the keepers (or `/capture <one sentence>` if it is an idea) |

Never run `/week` yourself; the Sunday task owns it. Everything else is yours any day.

## 6a. Where the weird, counterfactual papers come from

Three scout streams feed triage every week, all judged by one question — *what common belief does this contradict?*:
the Hugging Face daily papers (what the community is reading); the counterfactual arXiv query (abstracts that say
"surprisingly", "contrary to", "does not improve", "fails to", "no evidence", "is not necessary"); and the banter sweep
(arXiv ids argued about this week on the Alignment Forum, LessWrong, Hacker News, r/MachineLearning and Zhihu). The
fourth stream is you: `data/inbox/links.md`. Social banter is the best sensor for this class of paper and you are the
only one with a Zhihu feed, so the inbox file makes you a first-class source rather than an exception.

## 6b. The names

| Code | Reads as | Example |
| --- | --- | --- |
| `2026-W43` | ISO week: year and week number, Monday to Sunday, in New York time. Sunday night's run belongs to the week that is ending. | `data/digests/2026-W43.md` |
| `L1` … `L5`, `L0` | Lanes; `L0` is the open scout lane. `T1`, `T2` are retired themes, kept only so old records read. | `config/themes.yaml` |
| `CL-W43-01` | **Claim** 01, written by the machine in week 43. | thread folder `data/threads/CL-W43-01-…` |
| `CL-W43-J01` | Claim 01 **captured from Jacob** (J) in week 43 — a `/capture`; status `thought` until its kill search. | |
| `C-W43-15` | **Candidate** (probe) 15 of week 43, a record in `data/candidates/2026-W43.jsonl`. | |
| `P-W43-J01-a` | Probe a of captured claim J01, specified on the claim and not yet a candidate record. | |
| `X-2026-W42-S7F9`, `import:2026-W43-S4xF9` | Cross-field import: problem **shape** 7 × **field** 9 of `config/fields.yaml`, week 42. | |
| `2610.22276` | A seed is named by its arXiv id; a chat seed is `chat-<date>-<slug>`. | |
| `2026-W43-kill-C-W43-15.md`, `2026-W43-redteam-C-W43-15.md` | Kill record and red-team log of probe C-W43-15, in `data/reports/`. | |
| `ORPHANS-W43` | The week's register of probes with no claim. | in `claims.jsonl` |
| git branch `capture-w43-j01`, `shakedown-w42`, `pending-rule-14` | Housekeeping, not content: a branch is used only when `main` is locked by a live run or when output is experimental; each was merged into `main` and can be deleted on GitHub. You never need to check one out. | |

## 7. Two operators, one repository — the sync rules

The Sunday task and your PC both push to `main`. The rules that keep them from racing:

1. Pull first, always: `git pull --rebase origin main`.
2. Whoever runs writes a lock, `data/runs/ACTIVE.json` (`operator`, `started`, `scope` = the ids it will touch),
   commits and pushes it, and removes it at the end; a lock older than 3 hours is ignored. A sprint stays out of a live
   lock's scope; a scheduled run stays out of a sprint's.
3. One stage, one commit, one push. Small commits rebase cleanly.
4. If a `.jsonl` file conflicts, keep both sides' lines — the files are append-only and the last record per id wins —
   then `python scripts/threads.py`. If a `THREAD.md` conflicts, regenerate it; notes are views of the records.
5. Your own edits (`## Jacob` sections, config files) are ordinary commits: `bash scripts/done.sh "marks"` does the
   add, commit and push for you (or `git add -A && git commit -m "<week>: Jacob — marks" && git push`).
6. If a push is rejected, the cloud pushed first: `git pull --rebase origin main`, resolve as in rule 4, push again.

## 8. Questions you have asked

**Are papers fetched at random from the latest arXiv?** No. `config/sources.yaml` holds about 25 arXiv API queries,
each written for a lane with mechanism words and role words, run over the last 7 days in cs.LG, cs.CL, cs.AI, cs.DC,
cs.SE, cs.MA, cs.RO, plus author and citation watchlists. Since 2026-10-19 there is also the **scout stream**: the
papers the community is reading this week regardless of our lanes (Hugging Face daily papers, ranked by reader
upvotes; the day's top 6 and anything over 60 upvotes), judged at triage only on whether they could carry a headline.

**Are the claims reasoned or glued together by rules?** Reasoned, by a Claude session — but until 2026-10-21 by an
unattended one whose only memory was the repo, working bottom-up from cards (what one paper leaves out), which is why
the first batch read as footnotes lifted into headlines. `prompts/taste.md` now carries the judgment from the live
sessions (what made ideas alive, what killed them, your stated taste), every generating stage reads it first, and the
claims stage runs a top-down pass (from lane sentences, pressure points and the field's own stated assumptions) before
the bottom-up one. Each claim records its `origin` (top-down | bottom-up | chat) and the scoreboard shows which origin
survives kill searches and red teams, so the question "is the distribution his or the cards'?" gets a number.

**Is the claim the paper's claim or ours?** Ours. A card records what a paper does and what it leaves out; the
mutation operators turn that into probes; the claims stage writes the headline those probes would establish if they
came out one way. The paper's own claim becomes the "current belief" line in the thread note.

**How are the "top 3 probes" picked, and what is the difference between a probe and a claim?** A claim is the
sentence about the world; a probe is an experiment that could kill it, with a cost and a pre-written kill criterion.
The claims stage ranks *claims* by the gates (community-wide consumers and durability weigh most) and writes its
reasons in the record's `grading`; within a claim, probes are ordered by cost. The week's kill budget then takes the
cheapest live probe of the top-ranked claim, then of the second, then of the third. It is a judgment ranking with
stated reasons, not a formula; your `promote` / `jacob-dropped` marks override it.

**Do kill searches and red teams run on everything?** No — on the top of the ranking, within the weekly budget (3
and 3). The rest of the queue waits with status `proposed`. A sprint runs them on demand (`/sprint kill`, or
`/sprint <claim-id>` for one thread).

**Which stage does `/sprint` run?** Whichever is owed. `/sprint <claim-id>` reads the thread's First steps and
runs the next gate for it — kill search if none has run, red team if a probe survived, report if the red team passed,
then the probe's own pre-registered run plan — stopping at the first verdict. `/sprint generate` runs cards → mutate →
claims on the backlog; `/sprint scout` refreshes and triages the scout stream; `/sprint kill` runs the owed kill
searches. For thinking rather than running — an old topic or a new thread — use `/discuss <claim-id>` (the full record
is loaded and the conclusions land in the thread's Log) or simply talk in a session; a new headline that emerges is
`/capture`d within one reply.

**Is the machine idle between Sundays?** Only if you let it be. `/sprint` runs any stage on demand with the same
rules; the Sunday run picks up whatever you did (it pulls first and skips what is already done).

**Do I have to tell the agent I left comments?** No. `python scripts/threads.py --inbox` lists every `## Jacob`
section with marks not yet applied, and every session and scheduled run starts by running it. Write in the section,
commit, push.

**I only need to look in `data/threads/`, right?** Yes: the index tells you what claim threads exist and their
status; each note tells you what it takes to proceed (First steps) and what is being asked of you (Decisions); your
section is where your commentary goes. The Sunday digest is the only other page.

## 9. Where things stand

See `data/threads/README.md` (always current) and the latest `data/digests/`.

## 10. For a fresh clone, and the design documents

    pip install -r requirements.txt
    bash scripts/run_week.sh            # stage 0 by hand (the Sunday task normally runs it)
    claude                              # then any command from section 6

Design history: `SPEC.md` (what to build and how it scales) · `LANDSCAPE.md` (what we borrow from public
auto-research systems) · `BUILD_BRIEF.md` (the brief the first build was made from) · `DECISIONS.md`.
Only `scripts/fetch_arxiv.py`, `scripts/run_week.sh` and `scripts/threads.py` are code; every other stage is an agent
run from a slash command in `.claude/commands/`, reading its prompt in `prompts/`.
