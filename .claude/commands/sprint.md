Run an on-demand sprint: $ARGUMENTS (a claim id, or `generate`, `scout`, `kill`, `inbox`).

Read `prompts/13_sprint.md`, `prompts/taste.md`, `CLAUDE.md`, `config/standards.md`, `prompts/checklist.md` and `config/generation.yaml`
(`on_demand`). Sync protocol first: `git pull --rebase origin main`; read `data/runs/ACTIVE.json` and stay out of a
live lock's scope; write your own lock, commit and push it. Then `python scripts/threads.py --inbox` and apply any
marks before doing anything else (`--mark-applied` after). Run the mode as the prompt specifies, one stage per commit
and push, refreshing the thread notes after every step. Remove the lock in the final commit. Final message: what moved
(id, from → to, gate or verdict), the thread folders touched, and at most three decisions only Jacob can make.
