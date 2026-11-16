# On the released Genie Sim Benchmark at its shipped physics default (120 Hz CPU PhysX, schema-default solver iterations and contact offsets, named nowhere the validity claim is read), refining the physics step to 240 Hz or 960 Hz or doubling the contact offset moves the released pi0.5 baseline's Score on at least 3 of 8 contact-rich board tasks by more than the 10 points the README claims as its real-to-sim discrepancy, while raising the solver iterations to 64/16 moves fewer than two.

`CL-W46-07` · lane **L5** · status **open** · rank 8 · position both · refreshed 2026-11-16

## Status

Open claim. The claim survived its concept-level kill search (2026-11-15); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: none at filing; Gate 6 not yet established (kill search owed); Gate 2B flagged. Grade on paper: proper (narrow, weak). Next action: see First steps.

## The claim

- **Headline:** On the released Genie Sim Benchmark at its shipped physics default (120 Hz CPU PhysX, schema-default solver iterations and contact offsets, named nowhere the validity claim is read), refining the physics step to 240 Hz or 960 Hz or doubling the contact offset moves the released pi0.5 baseline's Score on at least 3 of 8 contact-rich board tasks by more than the 10 points the README claims as its real-to-sim discrepancy, while raising the solver iterations to 64/16 moves fewer than two.
- **Current belief (the field's):** Genie Sim README (github.com/AgibotTech/genie_sim, fetched 2026-11-15): 'Discrepancy between simulation and real-world test results is less than 10%', with no engine, time step, iteration count or contact setting named; 2611.15020 sec. II-C (card, full text): 'Simulation evaluation uses a fixed Genie Sim experimental branch' — the task-layer engine and setting are not in the text, while the object layer names '1 ms steps', 'CPU TGS, 32/1 solver iterations' and shows one engine swap at identical parameters moving error 25.50 to 524.61 mm (App. D.3); SIMPLER 2405.05941 (card neighbour): validity from matching 'the simulator's controller and camera image'; X2Real 2609.27449 (abstract fetched 2026-11-15): 'calibrates simulation visual and physical properties ... achieving a 0.84 linear correlation'. The real-to-sim evaluation community treats visuals, controller and assets as the validity axes and the numerics as fixed infrastructure; the sim-to-sim community holds the opposite datum for RL trackers (2610.32277, abstract fetched 2026-11-15: 'the first sim-to-sim gap we saw came from the harness, a missing floor and a wrong timestep').
- **If true:** A real-to-sim validity number is conditional on (engine, step, iterations, contact offset): validity tables and leaderboards (RoboColiseum, X2Real, SIMPLER-family, REALM) print the setting and a one-at-a-time sensitivity row beside the correlation; engine builders' defaults stop being certified by proxy; the lane's 'silent numerics' question gets its first answer on a validated benchmark, with the repeat floor (CL-W43-09) measured on the way.
- **If false:** Within shipped ranges the numerics are a second-order term for real-trained VLA evaluation at Score granularity: the sim-to-sim time-step datum does not transfer to this register, evaluation-twin builders are entitled to treat numerics as fixed infrastructure, with a citation, and the lane confines its numerics question to training (where the policy can exploit the setting) and to deformables; the repeat-floor table survives as CL-W43-09's datum.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.15020 names 'CPU TGS, 32/1 solver iterations and a 1 ms step' at the object layer (App. D.3) and 'a fixed Genie Sim experimental branch' at the task layer (sec. II-C), while the release ships 120 Hz; the README's 'less than 10%'; Kaedim 2610.00731 sec. 6: 'cannot say ... which object property matters most. As an extension of this work, we would change one factor at a time'; 2609.37771: 'success criteria and simulation settings do not fully capture how acceleration affects task execution'; Manda: 'force peaks are not timestep-converged'; 2610.32277: 'a wrong timestep'; Genie Sim issue #198: fingertips penetrate a dynamic object by 'centimeters'. Who pays: RoboColiseum / Genie Sim (what to print with a board and whether the '<10%' footnote transfers to sim-trained entries), evaluation-twin builders (X2Real, REALM, PolaRiS, Kaedim) choosing what to report beside a correlatio…
- **Impact ceiling:** **floor**: A sensitivity table for one shipped validated benchmark's own baseline (8 tasks x 4 knobs + the protocol knob, with a harness repeat floor), cited by Genie Sim's v2 and by the next validity table as the reason to print the setting and a sensitivity row. Requires steps 0-3. Judgment p 0.5.; **middle**: A reporting rule — step, iterations, offsets, inference-pause state and a one-at-a-time sensitivity row beside every real-to-sim correlation and board — adopted by one benchmark (RoboColiseum or X2Real) and asked for by reviewers; the lab arm (22 real-trained checkpoints, real column) answers the validity question proper. Requires AgiBot's cooperation or a second benchmark (about 60 GPU-h more).…; **ceiling**: The numerics-sensitivity row is a standard column of simulated robot evaluation and the V&V triad frames validity papers. Requires three benchmarks and an engine owner's endorsement. Judgment p 0.08.
- **Relevance:** Robotics and learning faculty: direct (what a validated benchmark certifies, and for which policy population). Engine builders (NVIDIA PhysX / Isaac, Newton): direct (schema defaults as the knob). Industry (AgiBot, RoboColiseum, evaluation-twin vendors): direct. HAL / evaluators: indirect (benchmark-validity shape). Narasimhan route: zero. Systems route (Lloyd / Netravali / Tri Dao): zero. Jacob's edge: load-bearing — step, iteration count and contact offset are discretisation and convergence choices; the protocol knob is a timing/systems reading; no mechanical engineering is built.
- **Kill probe:** Steps 0-3 at about 120-150 GPU-h (ceiling 168 by the cut list), about $200-300 or $0 on owned GPUs, 14 days; dead if under every numerics knob fewer than 2 of 8 tasks move (interval excludes 0, $|\hat\delta| > 0.10$) and none exceeds 0.10; parked at step 0 by the three written triggers.
- **Density and ownership:** Exact shape (a real-validated evaluation benchmark re-scored under its own physics step and contact offset, the shift read against its published validity number): 0 in nine kill-search queries (data/reports/2026-W46-kill-CL-W46-07.md sec. 1, 2026-11-15); the real-to-sim x numerics conjunction 58 hits / 24 in window / 1 adjacent (Kaedim); the anchored numerics x success-rate conjunction 12 / 5 / 1 (2609.37771). Occupied coarser shapes: Kaedim (assets and physical parameters varied, numerics fixed and printed), SimuGuard (one-parameter reruns, other knobs), 2609.37771 (checkers and masses), 2610.32277 (one-at-a-time numerics for RL trackers), Manda (numerics at the object layer, scripted controller). Pre-window: Erez-Tassa-Todorov ICRA 2015, Kadian 2019 (sim-trained agents exploit, SRCC 0.18). Owners: AgiBot / Genie Sim (policies, real column, board), the 2610.32277 authors (method), Kaed…
- **Why now:** Genie Sim v3.5.0 (2026-11-02) with CLI physics-step override and Season I baseline checkpoints; 2611.15020 (2026-11-11); 2610.32277 (2026-10-23); SimuGuard (2026-10-30); Manda (2026-10-05); Kaedim (2026-09-30). Flag: the baseline is sim-trained and its training setting is unstated; the paper's checkpoints are unreleased.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): pass after rewrite: premise numbers fetched and dated with their verbs (README '<10%' claimed; Table B1 r 0.9686 / MAE 0.0405 reported over 22 pairs, 30-100 rollouts; params.py physics_step 120 / fps 30 / rendering_step 60 / pause_physics_during_inference False read; Kaedim Table 2 reported); conditioning set written (released pi0.5 baseline as served, fixed layouts and seed, setting pair, Isaac Sim 6.2 build, CPU PhysX, inference pause on); the quantity is the exploit cell for the named sim-trained policy and the headlin… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): pass: 120-150 GPU-h (168 ceiling enforced by a priority cut list), about $200-300 or $0 owned, 14 days; kill written (fewer than 2 of 8 movers under 240 Hz, 960 Hz and 2x offset alike, none above 0.10); power computed under the design's noise model with the between-arm correlation stated (the v1 rule failed Gate 1 and was replaced); both outcomes informative (floor to CL-W43-09, protocol knob 07d as a pressure point) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): pass, Route B narrowly: engine comparison (Manda) says coarse outcomes are step-robust, sim-to-sim (2610.32277) says the step is decisive for a tuned policy, the validity community (Kaedim, PolaRiS, Genie Sim) reports no sensitivity; neither has the number for a VLA Score on a validated benchmark; the expected result contradicts one community's statement; weak because the register is occupied with other knobs (SimuGuard, 2609.37771, Kaedim) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): one community (benchmark owners, validity-table authors, reviewers): print the setting, add a sensitivity row, qualify the '<10%' footnote by setting and policy population; contestants' actions unchanged -> proper, not golden |
| G4 | mechanism and consequence | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): pass: mechanism (per-step penetration and contact generation scale with h and d_c; a policy tuned to h_0 has margins set by h_0 force histories; iteration count converged at >= 4 substeps per tick) with pre-registered predictions, refuting observations and consequences both ways; convergence pattern pre-registered |
| G5 | durability; lab-adjacent | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): the reporting rule is durable, the numbers expire with the next release; lab-adjacent (measurement of shipped artifacts) |
| G6 | ownership, density, race window; position clause | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-18.md): concept-level kill search survived 2026-11-15 (no occupant for the exact shape); enabling piece Genie Sim v3.5.0 (2026-11-02) + 2611.15020 (2026-11-11); race window judged 4-8 weeks vs 14 days to result (adequate for proper, borderline for golden); solo position = board register (exploit cell of the sim-trained baseline); lab position (AgiBot/RoboColiseum: 22 real-trained checkpoints, real column) is the version that tests the validity number itself |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-18 | v2: designed after the concept-level kill search of CL-W46-07 — re-scoring the released Genie Sim Benchmark's own pi0.5… | Steps 0-3 at about 120-150 GPU-h (ceiling 168 by the cut list), about $200-300 or $0 on owned GPUs, 14 days; dead if under every numerics knob fewer than 2 of 8 tasks move (interval excludes 0, $|\hat\delta| > 0.10$) and none exceeds 0.10;… | red-teamed | — |
| C-W46-20 | The engine swing at the task layer: the same Genie Sim task and policy on the PhysX and Newton runtimes the platform sh… | Steps 0-2: about 90 GPU-h with the policy build (about 30 if shared with C-W46-18), about $270 or $0 on owned GPUs, 10 days; dead if every two-runtime task's swing is inside the floor or the real-sim gap; parked at step 0 if fewer than 3 t… | parked | parked ([record](../../../data/reports/2026-W46-kill-CL-W46-07.md)) |

## Kill search

### Concept level (CL-W46-07) — survived-kill (2026-11-15)
No occupant for the exact shape (real-validated benchmark re-scored under its own physics step / contact offset); Gate 0 fails as worded: the time step is a shipped default (params.py physics_step = 120, CPU PhysX) the paper and README do not name, and Kaedim 2610.00731 Table 2 already prints and gates the numerics in a validity table; survival is weak (register occupied three times with other knobs; outcome-level numerics data say coarse outcomes are step-robust); headline rewritten before probe design.
Full record: [`data/reports/2026-W46-kill-CL-W46-07.md`](../../../data/reports/2026-W46-kill-CL-W46-07.md).
**Why not done before:** Enabling piece: Genie Sim v3.5.0 (2026-11-02) is the first real-validated benchmark with a CLI physics-step override and baseline weights, its validity number followed on 2026-11-11; the validity community freezes or defaults the numerics, the engine-comparison community measures them without policies, the sim-to-sim community measured them on sim-trained trackers; hard because the paper's 22 policies are unreleased.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.00731` Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation (Kaedim) — Build the same real robot cell twice in Isaac Sim (authored metric geometry and physics vs generative mesh and engine-default physics), run two policies on five tasks twenty times per build, and score both against the same 200 third-party-graded real trials. *Difference:* Varies assets and physical parameters on a real-validated cell and reads the shift against real (score error 17.54 to 6.97 points); the numerics are held fixed and printed (Table 2: PhysX 240 Hz, contact offset 6 mm, 64/16 iterations) and gated; its announced…
- `2610.41857` When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot B… — Record every physics step of benchmark rollouts, flag objects accelerating faster than robot contact or gravity allow, replay bit for bit, rerun with one simulation parameter changed. *Difference:* One-parameter reruns of a shipped evaluation benchmark with frozen policies (collision constant: 89% to 98%); knobs are mass, solver iterations, depenetration velocity, contact time constant; no time step, no contact offset, no real column.
- `2609.37771` Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of VLA Ac… — Audit seven VLA benchmarks for bugs and design limitations, localize them with object paths against checker regions, fix checkers and masses, show rankings reverse. *Difference:* Its 'simulation settings' are checkers and object masses (26-point swing); zero mentions of time step, solver or Hz; no real column.
- `mandarobotics.com/blog/comparing-physics-engines (2026-10-05; seed paper's ref [5])` Comparing physics engines for robotics simulation — Match scenes, robot and one explicit torque controller across PhysX CPU, Newton/MuJoCo-Warp, MuJoCo CPU and Genesis, and measure outcomes, force histories, half-timestep sensitivity and repeats. *Difference:* Numerics sensitivity at the object layer with a scripted controller: 'engines agree on coarse outcomes', 'force peaks are not timestep-converged'; repeat table (PhysX CPU identical x3; Newton 11/8/7; Genesis 10/8/8 of 15); no policy, no success rate, no real;…
- `2610.32277` Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers — Train humanoid trackers in mjlab, verify a CPU MuJoCo harness by restoring settings one at a time, then stress command delay. *Difference:* One-at-a-time numerics attribution for sim-trained RL trackers (time step decisive, solver flat); tracking error, no real column, no evaluation benchmark.
*Search degraded:* ['s2', 'arxiv Q8 (503 x2)', 'arxiv Q9 (Rate exceeded, 503)', 'conference exports not built', 'GitHub repo tree (403; raw.githubusercontent.com and HF API used instead)']

### C-W46-20 — parked (2026-11-15)
A claim one level narrower than filed: on the released benchmark at its shipped 120 Hz CPU-PhysX default (named nowhere the validity claim is read), refining the step or doubling the contact offset moves at least 3 of 8 contact-rich Scores by more than the claimed 10 points, solver iterations flat; the reporting consequence is the sensitivity row (the setting line is already Kaedim's practice). It is a weak claim solo and the board-column version in the lab position.
Full record: [`data/reports/2026-W46-kill-CL-W46-07.md`](../../../data/reports/2026-W46-kill-CL-W46-07.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched

## Red team

**C-W46-18** — {"date": "2026-11-15", "rounds": 2, "protocol": "attackers (systems, RL-theory, professor, checklist) as three written passes and the defender as a separate fourth pass, all by this agent (the Agent tool was not available; degraded \u2014 the defender separation is by pass, not by agent); evidence: release files and full texts fetched by the kill search 2026-11-15, three new fetches 2026-11-16 (RoboColiseum skills README, challenge-baseline-model SKILL.md, ACoT-VLA README), the power simulation power.py; arXiv API 429 twice (degraded)", "objections": [{"persona": "systems; checklist:2026-10-20 (open the README's data layout before costing an arm); checklist:2026-11-08 ('released X' names an artefact the README lists)", "class": "limiting", "objection": "The v1 cost line ('roughly 25 s each, judgment') is not an Isaac Sim number. The benchmark renders three cameras with RTX ray tracing at 60 Hz, the pi0.5 server adds an inference round-trip per action chunk, and the 960 Hz arm multiplies CPU-PhysX work per simulated second by eight; a 30-60 s episode is 60-120 s of wall time. At 7 cells x 8 tasks x 100 episodes that is 93-187 GPU-h before the pilot, and a two-GPU deployment (Isaac…

## First steps if pursued

1. D
2. a
3. y
4. 
5. 1
6. :
7. 
8. `
9. g
10. e
11. n
12. i
13. e
14. s
15. i
16. m
17. 
18. d
19. o
20. c
21. k
22. e
23. r
24. 6
25. .
26. 2
27. 
28. b
29. u
30. i
31. l
32. d
33. 
34. &
35. &
36. 
37. g
38. e
39. n
40. i
41. e
42. s
43. i
44. m
45. 
46. d
47. o
48. c
49. k
50. e
51. r
52. 6
53. .
54. 2
55. 
56. u
57. p
58. 
59. -
60. -
61. h
62. e
63. a
64. d
65. l
66. e
67. s
68. s
69. `
70. 
71. (
72. I
73. s
74. a
75. a
76. c
77. 
78. S
79. i
80. m
81. 
82. 6
83. .
84. 2
85. 
86. i
87. m
88. a
89. g
90. e
91. )
92. ,
93. 
94. d
95. o
96. w
97. n
98. l
99. o
100. a
101. d
102. 
103. t
104. h
105. e
106. 
107. S
108. e
109. a
110. s
111. o
112. n
113. 
114. I
115. 
116. b
117. o
118. a
119. r
120. d
121. 
122. a
123. s
124. s
125. e
126. t
127. s
128. 
129. p
130. e
131. r
132. 
133. t
134. h
135. e
136. 
137. a
138. s
139. s
140. e
141. t
142. 
143. g
144. u
145. i
146. d
147. e
148. 
149. a
150. n
151. d
152. 
153. t
154. h
155. e
156. 
157. t
158. h
159. r
160. e
161. e
162. 
163. b
164. a
165. s
166. e
167. l
168. i
169. n
170. e
171. 
172. c
173. h
174. e
175. c
176. k
177. p
178. o
179. i
180. n
181. t
182. s
183. 
184. w
185. i
186. t
187. h
188. 
189. `
190. s
191. c
192. r
193. i
194. p
195. t
196. s
197. /
198. d
199. o
200. w
201. n
202. l
203. o
204. a
205. d
206. _
207. c
208. h
209. e
210. c
211. k
212. p
213. o
214. i
215. n
216. t
217. .
218. s
219. h
220. 
221. i
222. n
223. s
224. t
225. r
226. u
227. c
228. t
229. i
230. o
231. n
232. _
233. a
234. n
235. d
236. _
237. r
238. o
239. b
240. u
241. s
242. t
243. _
244. p
245. i
246. 0
247. 5
248. 
249. /
250. 
251. m
252. a
253. n
254. i
255. p
256. u
257. l
258. a
259. t
260. i
261. o
262. n
263. _
264. p
265. i
266. 0
267. 5
268. 
269. /
270. 
271. s
272. p
273. a
274. t
275. i
276. a
277. l
278. _
279. p
280. i
281. 0
282. 5
283. `
284. 
285. (
286. M
287. o
288. d
289. e
290. l
291. S
292. c
293. o
294. p
295. e
296. ,
297. 
298. ~
299. 6
300. 
301. G
302. B
303. 
304. e
305. a
306. c
307. h
308. )
309. ,
310. 
311. c
312. l
313. o
314. n
315. e
316. 
317. A
318. C
319. o
320. T
321. -
322. V
323. L
324. A
325. 
326. (
327. b
328. r
329. a
330. n
331. c
332. h
333. 
334. a
335. g
336. i
337. b
338. o
339. t
340. _
341. w
342. o
343. r
344. l
345. d
346. _
347. c
348. h
349. a
350. l
351. l
352. e
353. n
354. g
355. e
356. )
357. ,
358. 
359. `
360. u
361. v
362. 
363. s
364. y
365. n
366. c
367. `
368. ,
369. 
370. s
371. t
372. a
373. r
374. t
375. 
376. t
377. h
378. e
379. 
380. p
381. i
382. 0
383. .
384. 5
385. 
386. s
387. e
388. r
389. v
390. e
391. r
392. 
393. o
394. n
395. 
396. t
397. h
398. e
399. 
400. s
401. a
402. m
403. e
404. 
405. 4
406. 8
407. 
408. G
409. B
410. 
411. G
412. P
413. U
414. 
415. a
416. n
417. d
418. 
419. p
420. a
421. s
422. s
423. 
424. `
425. g
426. e
427. n
428. i
429. e
430. s
431. i
432. m
433. 
434. b
435. e
436. n
437. c
438. h
439. m
440. a
441. r
442. k
443. 
444. c
445. h
446. e
447. c
448. k
449. -
450. i
451. n
452. f
453. e
454. r
455. e
456. n
457. c
458. e
459. `
460. ;
461. 
462. s
463. e
464. n
465. d
466. 
467. t
468. h
469. e
470. 
471. l
472. e
473. t
474. t
475. e
476. r
477. 
478. t
479. o
480. 
481. t
482. h
483. e
484. 
485. G
486. e
487. n
488. i
489. e
490. 
491. S
492. i
493. m
494. 
495. a
496. u
497. t
498. h
499. o
500. r
501. s
502. 
503. a
504. s
505. k
506. i
507. n
508. g
509. 
510. f
511. o
512. r
513. 
514. t
515. h
516. e
517. 
518. 2
519. 2
520. -
521. p
522. a
523. i
524. r
525. 
526. s
527. t
528. u
529. d
530. y
531. '
532. s
533. 
534. t
535. a
536. s
537. k
538. -
539. l
540. a
541. y
542. e
543. r
544. 
545. p
546. h
547. y
548. s
549. i
550. c
551. s
552. 
553. s
554. e
555. t
556. t
557. i
558. n
559. g
560. 
561. a
562. n
563. d
564. 
565. t
566. h
567. e
568. 
569. c
570. h
571. e
572. c
573. k
574. p
575. o
576. i
577. n
578. t
579. s
580. .
581. 
582. D
583. a
584. y
585. 
586. 2
587. :
588. 
589. `
590. g
591. e
592. n
593. i
594. e
595. s
596. i
597. m
598. 
599. b
600. e
601. n
602. c
603. h
604. m
605. a
606. r
607. k
608. 
609. l
610. i
611. s
612. t
613. 
614. -
615. -
616. r
617. o
618. b
619. o
620. t
621. =
622. g
623. 2
624. o
625. p
626. `
627. ,
628. 
629. r
630. e
631. a
632. d
633. 
634. e
635. v
636. e
637. r
638. y
639. 
640. b
641. o
642. a
643. r
644. d
645. 
646. t
647. a
648. s
649. k
650. '
651. s
652. 
653. s
654. t
655. a
656. g
657. e
658. -
659. c
660. h
661. e
662. c
663. k
664. e
665. r
666. 
667. l
668. i
669. s
670. t
671. 
672. (
673. e
674. x
675. c
676. l
677. u
678. d
679. e
680. 
681. V
682. L
683. M
684. -
685. g
686. r
687. a
688. d
689. e
690. d
691. 
692. s
693. t
694. a
695. g
696. e
697. s
698. )
699. ,
700. 
701. d
702. u
703. m
704. p
705. 
706. t
707. h
708. e
709. 
710. l
711. i
712. v
713. e
714. 
715. s
716. t
717. a
718. g
719. e
720. '
721. s
722. 
723. p
724. h
725. y
726. s
727. i
728. c
729. s
730. 
731. (
732. t
733. i
734. m
735. e
736. S
737. t
738. e
739. p
740. s
741. P
742. e
743. r
744. S
745. e
746. c
747. o
748. n
749. d
750. ,
751. 
752. s
753. o
754. l
755. v
756. e
757. r
758. 
759. t
760. y
761. p
762. e
763. ,
764. 
765. C
766. C
767. D
768. ,
769. 
770. p
771. e
772. r
773. -
774. p
775. r
776. i
777. m
778. 
779. i
780. t
781. e
782. r
783. a
784. t
785. i
786. o
787. n
788. 
789. c
790. o
791. u
792. n
793. t
794. s
795. ,
796. 
797. p
798. e
799. r
800. -
801. s
802. h
803. a
804. p
805. e
806. 
807. c
808. o
809. n
810. t
811. a
812. c
813. t
814. O
815. f
816. f
817. s
818. e
819. t
820. /
821. r
822. e
823. s
824. t
825. O
826. f
827. f
828. s
829. e
830. t
831. )
832. 
833. w
834. i
835. t
836. h
837. 
838. a
839. 
840. 5
841. 0
842. -
843. l
844. i
845. n
846. e
847. 
848. s
849. c
850. r
851. i
852. p
853. t
854. ,
855. 
856. c
857. o
858. n
859. f
860. i
861. r
862. m
863. 
864. `
865. -
866. -
867. a
868. p
869. p
870. .
871. p
872. h
873. y
874. s
875. i
876. c
877. s
878. _
879. s
880. t
881. e
882. p
883. 
884. 2
885. 4
886. 0
887. `
888. 
889. c
890. h
891. a
892. n
893. g
894. e
895. s
896. 
897. t
898. h
899. e
900. 
901. s
902. t
903. a
904. g
905. e
906. ,
907. 
908. r
909. e
910. a
911. d
912. 
913. h
914. o
915. w
916. 
917. t
918. h
919. e
920. 
921. l
922. o
923. o
924. p
925. 
926. a
927. d
928. v
929. a
930. n
931. c
932. e
933. s
934. 
935. p
936. h
937. y
938. s
939. i
940. c
941. s
942. 
943. p
944. e
945. r
946. 
947. 3
948. 0
949. 
950. H
951. z
952. 
953. t
954. i
955. c
956. k
957. 
958. (
959. g
960. r
961. e
962. p
963. 
964. p
965. h
966. y
967. s
968. i
969. c
970. s
971. _
972. s
973. t
974. e
975. p
976. 
977. /
978. 
979. f
980. p
981. s
982. 
983. /
984. 
985. w
986. o
987. r
988. l
989. d
990. .
991. s
992. t
993. e
994. p
995. )
996. 
997. a
998. n
999. d
1000. 
1001. t
1002. h
1003. e
1004. 
1005. d
1006. a
1007. t
1008. a
1009. -
1010. c
1011. o
1012. l
1013. l
1014. e
1015. c
1016. t
1017. i
1018. o
1019. n
1020. 
1021. c
1022. o
1023. n
1024. f
1025. i
1026. g
1027. '
1028. s
1029. 
1030. s
1031. t
1032. e
1033. p
1034. ;
1035. 
1036. w
1037. r
1038. i
1039. t
1040. e
1041. 
1042. t
1043. h
1044. e
1045. 
1046. o
1047. r
1048. d
1049. e
1050. r
1051. e
1052. d
1053. 
1054. c
1055. o
1056. n
1057. t
1058. a
1059. c
1060. t
1061. -
1062. r
1063. i
1064. c
1065. h
1066. 
1067. t
1068. a
1069. s
1070. k
1071. 
1072. l
1073. i
1074. s
1075. t
1076. 
1077. a
1078. n
1079. d
1080. 
1081. t
1082. h
1083. e
1084. 
1085. s
1086. t
1087. e
1088. p
1089. -
1090. 0
1091. 
1092. p
1093. a
1094. r
1095. k
1096. i
1097. n
1098. g
1099. 
1100. d
1101. e
1102. c
1103. i
1104. s
1105. i
1106. o
1107. n
1108. .
1109. 
1110. D
1111. a
1112. y
1113. s
1114. 
1115. 3
1116. -
1117. 4
1118. 
1119. (
1120. a
1121. b
1122. o
1123. u
1124. t
1125. 
1126. 6
1127. 
1128. G
1129. P
1130. U
1131. -
1132. h
1133. )
1134. :
1135. 
1136. p
1137. i
1138. l
1139. o
1140. t
1141. 
1142. 2
1143. 0
1144. 
1145. e
1146. p
1147. i
1148. s
1149. o
1150. d
1151. e
1152. s
1153. 
1154. p
1155. e
1156. r
1157. 
1158. c
1159. a
1160. n
1161. d
1162. i
1163. d
1164. a
1165. t
1166. e
1167. 
1168. t
1169. a
1170. s
1171. k
1172. 
1173. a
1174. t
1175. 
1176. t
1177. h
1178. e
1179. t
1180. a
1181. _
1182. 0
1183. 
1184. w
1185. i
1186. t
1187. h
1188. 
1189. -
1190. -
1191. b
1192. e
1193. n
1194. c
1195. h
1196. m
1197. a
1198. r
1199. k
1200. .
1201. p
1202. a
1203. u
1204. s
1205. e
1206. _
1207. p
1208. h
1209. y
1210. s
1211. i
1212. c
1213. s
1214. _
1215. d
1216. u
1217. r
1218. i
1219. n
1220. g
1221. _
1222. i
1223. n
1224. f
1225. e
1226. r
1227. e
1228. n
1229. c
1230. e
1231. =
1232. t
1233. r
1234. u
1235. e
1236. 
1237. a
1238. n
1239. d
1240. 
1241. f
1242. i
1243. x
1244. e
1245. d
1246. 
1247. -
1248. -
1249. b
1250. e
1251. n
1252. c
1253. h
1254. m
1255. a
1256. r
1257. k
1258. .
1259. i
1260. n
1261. s
1262. t
1263. a
1264. n
1265. c
1266. e
1267. _
1268. i
1269. d
1270. s
1271. 
1272. /
1273. 
1274. -
1275. -
1276. b
1277. e
1278. n
1279. c
1280. h
1281. m
1282. a
1283. r
1284. k
1285. .
1286. s
1287. e
1288. e
1289. d
1290. ,
1291. 
1292. p
1293. l
1294. u
1295. s
1296. 
1297. 1
1298. 0
1299. 
1300. a
1301. t
1302. 
1303. 2
1304. 4
1305. 0
1306. 
1307. a
1308. n
1309. d
1310. 
1311. 1
1312. 0
1313. 
1314. a
1315. t
1316. 
1317. 9
1318. 6
1319. 0
1320. 
1321. H
1322. z
1323. 
1324. o
1325. n
1326. 
1327. t
1328. w
1329. o
1330. 
1331. t
1332. a
1333. s
1334. k
1335. s
1336. ;
1337. 
1338. r
1339. e
1340. c
1341. o
1342. r
1343. d
1344. 
1345. w
1346. a
1347. l
1348. l
1349. 
1350. t
1351. i
1352. m
1353. e
1354. 
1355. p
1356. e
1357. r
1358. 
1359. l
1360. e
1361. v
1362. e
1363. l
1364. 
1365. a
1366. n
1367. d
1368. 
1369. t
1370. h
1371. e
1372. 
1373. p
1374. e
1375. r
1376. -
1377. e
1378. p
1379. i
1380. s
1381. o
1382. d
1383. e
1384. 
1385. s
1386. c
1387. o
1388. r
1389. e
1390. 
1391. S
1392. D
1393. ;
1394. 
1395. f
1396. i
1397. x
1398. 
1399. t
1400. h
1401. e
1402. 
1403. 8
1404. 
1405. t
1406. a
1407. s
1408. k
1409. s
1410. 
1411. w
1412. i
1413. t
1414. h
1415. 
1416. h
1417. e
1418. a
1419. d
1420. r
1421. o
1422. o
1423. m
1424. 
1425. i
1426. n
1427. 
1428. [
1429. 0
1430. .
1431. 1
1432. 0
1433. ,
1434. 
1435. 0
1436. .
1437. 9
1438. 0
1439. ]
1440. 
1441. a
1442. n
1443. d
1444. 
1445. n
1446. 
1447. (
1448. 1
1449. 0
1450. 0
1451. 
1452. o
1453. r
1454. 
1455. 1
1456. 5
1457. 0
1458. )
1459. .
1460. 
1461. D
1462. a
1463. y
1464. s
1465. 
1466. 5
1467. -
1468. 1
1469. 2
1470. 
1471. (
1472. a
1473. b
1474. o
1475. u
1476. t
1477. 
1478. 1
1479. 1
1480. 0
1481. -
1482. 1
1483. 4
1484. 0
1485. 
1486. G
1487. P
1488. U
1489. -
1490. h
1491. )
1492. :
1493. 
1494. r
1495. u
1496. n
1497. 
1498. t
1499. h
1500. e
1501. 
1502. c
1503. e
1504. l
1505. l
1506. s
1507. 
1508. i
1509. n
1510. 
1511. p
1512. r
1513. i
1514. o
1515. r
1516. i
1517. t
1518. y
1519. 
1520. o
1521. r
1522. d
1523. e
1524. r
1525. 
1526. R
1527. 1
1528. ,
1529. 
1530. 2
1531. 4
1532. 0
1533. ,
1534. 
1535. 9
1536. 6
1537. 0
1538. ,
1539. 
1540. R
1541. 2
1542. ,
1543. 
1544. 2
1545. x
1546. 
1547. o
1548. f
1549. f
1550. s
1551. e
1552. t
1553. ,
1554. 
1555. (
1556. 6
1557. 4
1558. ,
1559. 1
1560. 6
1561. )
1562. ,
1563. 
1564. P
1565. -
1566. o
1567. f
1568. f
1569. 
1570. (
1571. n
1572. =
1573. 5
1574. 0
1575. )
1576. ,
1577. 
1578. R
1579. 3
1580. 
1581. (
1582. n
1583. =
1584. 5
1585. 0
1586. )
1587. ,
1588. 
1589. e
1590. a
1591. c
1592. h
1593. 
1594. w
1595. i
1596. t
1597. h
1598. 
1599. -
1600. -
1601. b
1602. e
1603. n
1604. c
1605. h
1606. m
1607. a
1608. r
1609. k
1610. .
1611. r
1612. e
1613. c
1614. o
1615. r
1616. d
1617. =
1618. t
1619. r
1620. u
1621. e
1622. ;
1623. 
1624. s
1625. t
1626. o
1627. p
1628. 
1629. a
1630. d
1631. d
1632. i
1633. n
1634. g
1635. 
1636. c
1637. e
1638. l
1639. l
1640. s
1641. 
1642. a
1643. t
1644. 
1645. 1
1646. 6
1647. 8
1648. 
1649. G
1650. P
1651. U
1652. -
1653. h
1654. .
1655. 
1656. D
1657. a
1658. y
1659. s
1660. 
1661. 1
1662. 3
1663. -
1664. 1
1665. 4
1666. 
1667. (
1668. $
1669. 0
1670. )
1671. :
1672. 
1673. p
1674. a
1675. i
1676. r
1677. e
1678. d
1679. 
1680. b
1681. o
1682. o
1683. t
1684. s
1685. t
1686. r
1687. a
1688. p
1689. 
1690. p
1691. e
1692. r
1693. 
1694. t
1695. a
1696. s
1697. k
1698. 
1699. a
1700. n
1701. d
1702. 
1703. k
1704. n
1705. o
1706. b
1707. ,
1708. 
1709. m
1710. o
1711. v
1712. e
1713. r
1714. s
1715. 
1716. t
1717. a
1718. b
1719. l
1720. e
1721. ,
1722. 
1723. c
1724. o
1725. n
1726. v
1727. e
1728. r
1729. g
1730. e
1731. n
1732. c
1733. e
1734. 
1735. p
1736. a
1737. t
1738. t
1739. e
1740. r
1741. n
1742. ,
1743. 
1744. h
1745. a
1746. r
1747. n
1748. e
1749. s
1750. s
1751. 
1752. f
1753. l
1754. o
1755. o
1756. r
1757. ,
1758. 
1759. 0
1760. 7
1761. c
1762. 
1763. b
1764. o
1765. u
1766. n
1767. d
1768. e
1769. d
1770. 
1771. m
1772. e
1773. a
1774. n
1775. ,
1776. 
1777. 0
1778. 7
1779. d
1780. 
1781. p
1782. r
1783. o
1784. t
1785. o
1786. c
1787. o
1788. l
1789. 
1790. s
1791. h
1792. i
1793. f
1794. t
1795. ;
1796. 
1797. p
1798. r
1799. i
1800. n
1801. t
1802. 
1803. t
1804. h
1805. e
1806. 
1807. R
1808. E
1809. A
1810. D
1811. M
1812. E
1813. 
1814. '
1815. <
1816. 1
1817. 0
1818. %
1819. '
1820. 
1821. a
1822. n
1823. d
1824. 
1825. T
1826. a
1827. b
1828. l
1829. e
1830. 
1831. B
1832. 1
1833. 
1834. b
1835. e
1836. s
1837. i
1838. d
1839. e
1840. 
1841. t
1842. h
1843. e
1844. 
1845. t
1846. a
1847. b
1848. l
1849. e
1850. ;
1851. 
1852. f
1853. i
1854. l
1855. e
1856. 
1857. t
1858. h
1859. e
1860. 
1861. f
1862. l
1863. o
1864. o
1865. r
1866. 
1867. t
1868. o
1869. 
1870. C
1871. L
1872. -
1873. W
1874. 4
1875. 3
1876. -
1877. 0
1878. 9
1879. 
1880. a
1881. n
1882. d
1883. 
1884. 0
1885. 7
1886. d
1887. 
1888. a
1889. s
1890. 
1891. a
1892. 
1893. p
1894. r
1895. e
1896. s
1897. s
1898. u
1899. r
1900. e
1901. 
1902. p
1903. o
1904. i
1905. n
1906. t
1907. .

## Decisions for Jacob

- Run the solo probe in the board register now (released sim-trained pi0.5 baseline, exploit cell, ~130 GPU-h, result cited as a sensitivity row beside the README's '<10%'), or hold it until the letter to Genie Sim/AgiBot answers (task-layer setting; the 22 real-trained checkpoints) and pursue the lab version that tests the validity number itself?
- Accept the narrowed object — a shipped board's own baseline moving under its own CLI knobs — as a claim worth a semester in L5, or park CL-W46-07 with the trigger 'a real-trained policy on a released task' (AgiBot World Challenge 2025 real episodes on a G1 task, or the paper's checkpoints)?
- Fund the 960 Hz arm (the convergence leg, +35% wall time per episode, the only way to say whether 240 Hz is a reference) or stop at 240 Hz and spend the hours on the contact-offset arm at full n?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L5 lane sentence read against card 2611.15020 and the Genie Sim README fetched 2026-11-15); probes C-W46-18 (cheapest) and C-W46-20 attached; concept-level kill search owed (rule 17); Gate 2B flagged; the per-pair interval column from the same card is CL-W43-02's refuted ruler and was not filed; the failure-stage disagreement column is a lab-only thought (r…
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 8: born W46: L5 numerics-vs-validity claim; probe 50-130 GPU-h with policies rebuilt (nothing released); Gate 2B flagged (magnitude against a shipped validity claim is the content); concept-level kill search runs this week (rule 17)
- 2026-11-15 — claim open: concept-level kill search (data/reports/2026-W46-kill-CL-W46-07.md): survived-kill — gate G0; No occupant for the exact shape (real-validated benchmark re-scored under its own physics step / contact offset); Gate 0 fails as worded: the time step is a shipped default (params.py physics_step = 120, CPU PhysX) the paper and README do not name, and Kaedim 2610.00731 Table 2 already prints and gates t…
- 2026-11-15 — claim open: design red team of C-W46-18 v2 (data/reports/2026-W46-redteam-C-W46-18.md): red-teamed — No killing objection unanswered; four concessions (power of the mover rule, the unestablishable 'flat' clause, the sim-trained baseline making the solo readout the exploit cell, no Table B1 overlap) narrow the probe and the claim to the board register; proper (narrow, weak). Claim graded proper (narrow, weak)…
- 2026-11-15 — C-W46-20 parked: claim-level kill search of CL-W46-07 (data/reports/2026-W46-kill-CL-W46-07.md): parked — step-0 trigger fires from the release docs: one runtime per task config, fewer than 3 released tasks on two runtimes without new assets; re-open on a release with a second runtime for 3+ rigid contact-rich tasks; Manda's announced policy-transfer post is the scoop watch

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-07`, version 3)
- probe `C-W46-18`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-20`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-07.md`
