Capture an idea raised in conversation as a thread, right now, before discussing it further: $ARGUMENTS

Read `config/themes.yaml`, `config/standards.md`, `prompts/11_claims.md`, `prompts/12_thread.md`. Write the idea as a
claim record in `data/claims/claims.jsonl` with id `CL-<week>-J<NN>`, `status: thought`, `source: chat`, the headline
in one plain sentence (ask for one if the idea cannot yet be said in one), the lane(s), `position`, and whatever of
current_belief / if_true / if_false the conversation already supports; file one seed in this week's seeds file with
`source: chat`. Run `python scripts/threads.py <id>` so the thread folder exists. Reply with the scorecard skeleton
filled only where the conversation supports it and the words "this is a thought until the kill search runs". The
next step is the automatic kill search on its cheapest probe, or `/discuss <id>` if Jacob wants to talk first.
