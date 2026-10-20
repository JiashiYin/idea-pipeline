Open a discussion session on thread $ARGUMENTS (a claim id or thread folder name).

Start with `git pull --rebase origin main`. Read `prompts/12_thread.md`, `config/standards.md`, `prompts/checklist.md`,
the thread's `THREAD.md`, its claim record and every probe record under it. Reply first with a six-line brief: the
headline, status line, failing gate, cheapest probe and its verdict, the open decisions, and what Jacob wrote in his
section. Then discuss under the standing rules: the scorecard before any new proposal; a new sub-idea becomes a probe
record under this claim (or `/capture` for a new claim) within one reply, never a debate; nothing is called supported
or golden without a kill search and red team; every paper mentioned gets its one-sentence trick; equations with
every symbol defined when a method is explained. At the end of the session write the conclusions as dated lines in
the thread's Log (via the claim record's history), apply any marks Jacob made, run `python scripts/threads.py <id>`,
commit and push.
