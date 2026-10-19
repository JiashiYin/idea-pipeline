# Decisions log

Builder appends one line per default taken or deviation made: date · what · why.

- 2026-10-01 · spec author · `q_opd_privileged` narrowed after the first live pull hit the 50-result cap with
  off-theme "privileged" papers; added an RL/verifier clause.
- 2026-10-01 · spec author · bundled `data/seeds/2026-W40-live.jsonl` is a raw 7-day pull (115 records,
  untriaged) kept as a fixture for the triage acceptance test; `2026-W40.jsonl` is the curated set (31, kept).
- 2026-10-19 · operator (W43 run) · cards chosen by lane balance (L1×2, L2, L3, L4×2, L5×2) instead of strictly newest-first,
  because the eight newest kept seeds were all L1/L3 and rule 12 needs three lanes live; noted in the digest.
- 2026-10-19 · operator (W43 run) · the W43 fetch returned 25 new seeds, mostly L5, because W42's 214 seeds were never triaged and
  `seen_ids` hides them; 15 were triaged this week as a catch-up slice (title pre-screen, then full read), the other 199 stay `new`
  pending Jacob's decision (digest §8.1). Card-limitation complaint seeds (24) filed with status `new` because the 40-seed triage
  budget was spent.
- 2026-10-19 · operator (W43 run) · two mutate workers produced the same candidate from different cards (grading LVRL's critic on
  2610.17633's released V-curves); merged into C-W43-01 with `also_from`. C-W43-03 parked at filing (probe ~400 GPU-hours, over
  Gate 1 from the solo position) rather than written as `proposed`.
