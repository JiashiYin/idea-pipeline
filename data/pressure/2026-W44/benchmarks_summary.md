# Pressure harvest (b) benchmarks, 2026-W44 (2026-11-02)

25 records, 18 sources (tbench.ai, ARC Prize, Scale, Artificial Analysis, Vals, LMArena, METR, Sierra, Nebius, ten arXiv papers of 2026-10-13..29). 21 new since 2026-10-09; R05, R06, R09, R13 are older, missed by W41. Alignment L1 18, L4 3, L5 2, L3 1, L2 1; register measurement 22; positioning lab-adjacent 24.

Since W41: TB 4.0 filled, with three evaluators giving three frontier values; SWE-Bench Pro V2 saturated three weeks after relaunch; provider-side state plus compaction moved one model 37 points on ARC-AGI-3 (L4); METR, tau-bench and SWE-rebench stalled; harness attribution went dense; LIBERO forked five times.

| # | Source | H | Observation |
|---|---|---|---|
| R01 | TB4 board pass@k | 2 | pass@5 computed but hidden; reorders top 5 |
| R02 | TB4 board cost | 6 | cost unranked; $9.6k run ranks 33rd |
| R03 | TB4 board effort | 9 | top efforts within CI; max +44% cost |
| R04 | TB4 release note | 4 | 8 h timeout; 27 tasks changed; trials void |
| R05 | TB Continuous Benchmarks | 8 | owner: agent benchmarks broadly broken |
| R06 | ARC Prize Astra | 9 | 62.7% vs 99.9% via provider state/compaction |
| R07 | SWE-Pro V2 paper | 7 | 480/731 tasks repaired; forged go.sum |
| R08 | SWE-Pro V2 tables | 2 | 'harder' relaunch at 99.4% in 3 weeks |
| R09 | AA Index v4.3 | 9 | Fable 5.1: 52.0 (AA) vs 57.9 (official) |
| R10 | AA Index v5 | 6 | 60% private; 10x cost across effort |
| R11 | AA Coding Agent Index | 9 | three TB4 frontier numbers; top is a router |
| R12 | Vals TB4 | 9 | 9-pt vendor-harness premium |
| R13 | Vals MiMo audit | 7 | 67% of RL tasks leak the fix |
| R14 | LMArena Bash Reliability | 4 | LLM judge replaces rules; ranks shift |
| R15 | LMArena Alignment Index | 5 | deceptive completion now scored live |
| R16 | METR horizons | 1 | tracker stopped; last model April |
| R17 | taubench.com | 1 | no frontier entry since July; no pass^k on voice |
| R18 | swe-rebench.com | 9 | rolling clean board stalled since July |
| R19 | 2610.31778 | 7 | compaction drops 1/3 of constraints; benchmarks hide it |
| R20 | 2610.25899 | 7 | inherited failed work: 20-54 pt drops |
| R21 | 2610.37255 (+2) | 9 | null reorder 85% to 19%; harness encoded |
| R22 | 2610.24649 | 7 | cheap critic: +19% cost, same pass rate |
| R23 | 2610.35426 | 7 | adversarial user cuts pass^4 up to 69% |
| R24 | LIBERO-RIG (+4 forks) | 2 | LIBERO 93% nominal; forks drop 17-42 pts |
| R25 | SPECOLA, UED quadrupeds | 7 | binary success hides margin and violations |

Blocked: WebFetch refused tbench.ai, metr.org, labs.scale.com (re-fetched with curl); 403 on arena.ai alignment board; no OSWorld 2.0 board found.
