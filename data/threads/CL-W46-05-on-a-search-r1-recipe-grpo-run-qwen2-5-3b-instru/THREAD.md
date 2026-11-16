# On a Search-R1-recipe GRPO run (Qwen2.5-3B-Instruct, HotpotQA, four turns), at least half of the problems in the greedy union-versus-best gap (solved by some checkpoint's greedy decode and not by the best checkpoint's) are coin-flip cells, with success probability between 0.2 and 0.8 at the best checkpoint at the training temperature, the band estimated from at least 16 sampled decodes and the shares corrected for binomial misclassification, and at most a fifth are strict probability drops (at or above 0.8 at some earlier checkpoint, at or below 0.2 at the best).

`CL-W46-05` · lane **L2** · status **open** · rank 4 · position both · refreshed 2026-11-16

## Status

Open claim. The claim survived its concept-level kill search (2026-11-15); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: none hard after the design red team; graded proper (narrow, weak): Gate 2B weak (magnitude and the five-way partition only), Gate 3 one community, Gate 6 race flag (Temporal Sampling's authors hold the samples). Grade on paper: proper (narrow, weak). Next action: see First steps.

## The claim

- **Headline:** On a Search-R1-recipe GRPO run (Qwen2.5-3B-Instruct, HotpotQA, four turns), at least half of the problems in the greedy union-versus-best gap (solved by some checkpoint's greedy decode and not by the best checkpoint's) are coin-flip cells, with success probability between 0.2 and 0.8 at the best checkpoint at the training temperature, the band estimated from at least 16 sampled decodes and the shares corrected for binomial misclassification, and at most a fifth are strict probability drops (at or above 0.8 at some earlier checkpoint, at or below 0.2 at the best).
- **Current belief (the field's):** Agentic-OPD 2611.12799 (card, full text): 'We use greedy decoding for all checkpoint evaluations' (sec. 2); 'the final checkpoint solves 2,808 tasks, while 4,553 tasks are solved by at least three checkpoints, a difference of 62%' (sec. 2), read as 'forgotten agent capabilities' and made a training target by selecting teachers on greedy failure sets (eqs. 4-9); 'measuring how much of the historical task coverage can be reliably recovered' is conceded only as a 'useful next step' (sec. 5). Temporal Sampling 2505.20196 (abstract fetched 2026-11-16; sec. 2.2 quoted by the import from the full text): 'models often forget how to solve problems they previously answered correctly during training. We term this phenomenon temporal forgetting'; 'To minimize variability arising from different sampling methods during evaluation, we employ greedy sampling'; the resulting table is read as 'the model oscillates between correct and incorrect answers across checkpoints' (Figure 3). Neither paper decodes a checkpoint twice on the forgetting set or reports a noise floor.
- **If true:** 'Temporal forgetting' and the union-versus-best gap are protocol numbers until a draw floor is reported: checkpoint-consolidation and temporal-ensembling papers (Agentic-OPD, Temporal Sampling, GTR-Turbo) report $\rho_1$ and $m$ beside the score; HCN-style teacher selection moves from greedy set cover to $\hat p$ differences with a replicate rule; the recoverable target of a consolidation stage becomes the strict-drop count, about a fifth of the headline; RL frameworks' per-checkpoint validation adopts a two-stage draw rule (one draw on settled cells, more where draws disagree); L1's pass^k-across-versions reading extends to checkpoints as versions.
- **If false:** If strict drops are at least half of the gap: forgetting within one RL run is a large, problem-specific property of the policy, the greedy ruler over-counts by under 2x, and the record is a footnote licensing it with the first variance-component card for an RL run. If the draw facet is empty (90% of cells settled at $T = 1$): the policy is near-deterministic at its own training temperature (the Sharpening Tax reading, 2610.01509), the greedy gap is argmax churn under parameter updates, the persistence statistics become the forgetting measurement, and Temporal Sampling at $T > 0$ recovers nothing one checkpoint's sampling would not.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: Agentic-OPD sec. 2 ('greedy decoding for all checkpoint evaluations'), sec. 4.3 (60/45 of 2,000, 'describes consolidation behavior'), sec. 5 ('reliably recovered' as a next step); Temporal Sampling sec. 2.2 (greedy to minimize variability); 2609.22547 Limitations ('multi-turn agentic or tool-use settings remains open'); 2606.10709 sec. 3.3 ('a stochastic observation'). Who pays: whoever is about to buy a consolidation stage on the strength of a greedy gap; authors of forgetting scores; anyone selecting a checkpoint from a run.
- **Impact ceiling:** **floor**: A four-number note ($q$, $f$, $A$, $\delta_0$) with the misclassification check for one public RL'd search agent, cited by C-W46-13 and the next forgetting paper. Requires steps 0-3. Judgment 0.6.; **middle**: The kill fires or the pool clears with margin, deciding for $30 whether C-W46-13's 150 GPU-h are spent; with step 4, the first three-way split with a draw floor of a between-policy greedy disagreement set. Judgment 0.3.; **ceiling**: None beyond C-W46-13's: this is its step 0.
- **Relevance:** Narasimhan route and any RL group: direct (how many draws a checkpoint table needs; what a 3B GRPO policy's success-probability histogram looks like at its training temperature). L1: direct (serving floor of greedy agent tables). Industry: direct for consolidation buyers. Systems route, L4, L5: zero. Jacob's edge: the pool bound, the misclassification matrix and the NPMLE inversion are napkin statistics; a first result in a weekend.
- **Kill probe:** This probe: about 6 GPU-h (12 with step 4), $30-50, 3-4 days; kills CL-W46-05's coin-flip clause if the corrected $\hat A$ upper bound is below $0.31\,\hat q$.
- **Density and ownership:** Kill search 2026-11-15: no fetched source splits a greedy checkpoint gap by a draw floor; the direction is in print (2606.10709; 2609.22547's placebo); about one checkpoint-forgetting paper a month. Occupied: the greedy table and recovery count (Agentic-OPD); the oscillation reading (Temporal Sampling); bimodalisation at 128 rollouts base-vs-post (Sharpening Tax); temperature-0 serving variance in general (2602.07150). Owners of the data: Temporal Sampling authors (64 samples on 8 checkpoints), Agentic-OPD authors (100 checkpoints), Search-R1 authors (training logs). Race flag carried from the kill report.
- **Why now:** As above; the public checkpoint and harness make the pool bound free of training.
- **Register, and what it is not:** A one-sided kill and a noise-floor measurement; the cheapest first move under CL-W46-05. It is not the G-study (no checkpoint facet), not a test of the strict-drop clause, not a verdict on forgetting, and not a claim about the paper's own run: it bounds the claim's coin-flip clause through a stated transfer assumption.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Pass with the v2 headline: premise numbers fetched and dated; conditioning set written (deterministic exact-search retriever; the policy's training temperature 1.0 / top-p 1.0 in print; zero decision variance at T = 0, delta_0 the serving stack's); 'under eight draws' removed because it made the band a protocol quantity (19% of p = 0.1 cells in the band at m = 8). Flags: 2,808 / 4,553 has no denominator in print; the released checkpoint is final-or-last-stable, not best-validation (2505.15117 App. G.1). |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Pass: C-W46-14 v2 kills the coin-flip clause at about 8 GPU-h, $35, 3 days plus download, conditional on the stated transfer assumption, kill written before the run (corrected A upper bound below 0.31 q; raw and corrected within 0.03); both outcomes at least a footnote; C-W46-13 (about 150 GPU-h) kills either clause. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Route B holds on magnitude and the split only (kill report): the direction is in print (2606.10709 sec. 3.3; 2609.22547 sec. 4.3). Weak. |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): One community plus one adjacent (consolidation / temporal-ensembling authors; training-dynamics measurers); proper-shaped. |
| G4 | mechanism and consequence | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Pass after correction: five-way partition written; one consequence per outcome (pool sufficient / kill / format diagnostic / greedy below its own mode / serving floor large); if_true recoverable target corrected to strict plus soft drops. |
| G5 | durability; lab-adjacent | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Ruler durable; the 3B numbers expire; race flag (Temporal Sampling and Agentic-OPD authors hold the data). |
| G6 | ownership, density, race window; position clause | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W46-14.md): Survived the concept-level kill search weakly (2026-11-15); about one relevant paper a month; why now: Agentic-OPD 2026-11-09, 2609.22547 2026-09-18, public checkpoint; position: solo viable for the kill, lab for both clauses. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-14 | One public checkpoint decoded sixteen times: the coin-flip pool under a greedy forgetting gap, the serving floor of the… | This probe: about 6 GPU-h (12 with step 4), $30-50, 3-4 days; kills CL-W46-05's coin-flip clause if the corrected $\hat A$ upper bound is below $0.31\,\hat q$. | red-teamed | survived-kill ([record](../../../data/reports/2026-W46-kill-CL-W46-05.md)) |
| C-W46-13 | The checkpoint x problem x draw table of one GRPO run: what the greedy 'forgetting' gap is made of | C-W46-14 first (about 8 GPU-h, $20, 3 days), then steps 1-3 (about 150 GPU-h, $350, 12 days); dead if the strict-drop share of $G$ is at least 0.5 (lower bound above 0.35), or 90% of cells settled at $m = 8$, or temperature-0 disagreement… | redesign-owed | redesign-owed ([record](../../../data/reports/2026-W46-kill-CL-W46-05.md)) |

## Kill search

### Concept level (CL-W46-05) — survived-kill (2026-11-15)
Weak survival: no fetched source splits a greedy checkpoint gap by a draw floor or states most of it is single-decode noise, but the direction (finite-sample solved status is stochastic; flips are partly sampling noise, partly drift) is written in the same search-agent GRPO setting by 2606.10709 and the same-checkpoint placebo statistic is published (2609.22547 sec. 4.3); what survives is the magnitude (half coin flips, a fifth strict drops) and the three-way split, with a race flag (Temporal Sampling authors hold the data).
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
**Why not done before:** Enabling pieces: Agentic-OPD (2026-11-09) made the greedy gap a training target; the split-generation placebo statistic (2609.22547, 2026-09-18) is a ready estimator; the public Search-R1 3B GRPO checkpoint (Hub listing fetched 2026-11-16) removes training from step 0; the data owners built methods on the gap and the replicate-aware papers asked other questions.
Closest neighbors (one-sentence trick; one-line difference):
- `2606.10709` Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries Du… — On GRPO for an LLM search agent, keep prompts whose rollout group was all-correct or all-wrong in a pool and resample them later, because their status flips as the policy moves. *Difference:* States the direction in the claim's own setting (finite-rollout status is 'a stochastic observation'; about 20% of queries flip; flips partly 'sampling noise', partly drift) on training queries with K=4/8 groups; no greedy table, no validation gap set, no spl…
- `2609.22547` When Pass@k Crossovers Are Real - and Why: Paired Inference and the Markov Kernel of RLVR — Test RL-versus-base pass@k crossovers by a paired prompt-level bootstrap and show per-prompt success probabilities disperse after RL via a split-generation covariance test whose placebo is two halves of the same model. *Difference:* Owns the same-checkpoint placebo as noise floor and the replicated per-prompt dispersion finding, base-versus-RL on math and code; no intermediate checkpoints, no greedy table, no forgetting set; 'multi-turn agentic or tool-use settings remains open'.
- `2505.20196` Temporal Sampling for Forgotten Reasoning in LLMs — Count final-checkpoint errors some earlier checkpoint got right (6.4-56.1%) and spread the k samples over several checkpoints to raise pass@k by 4-19 points. *Difference:* The occupant of the greedy forgetting score and the oscillation reading; chose greedy 'to minimize variability'; holds 64 samples on 8 checkpoints for its method and never applies them to the score; no draw floor, no split.
- `2611.12799` Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agent… — Keep every GRPO checkpoint, mark greedy-solved validation problems, and distill the best checkpoint toward the earlier one covering most of its current failures. *Difference:* The seed; greedy gap as training target; 60 recovered / 45 lost of 2,000 read as consolidation; no repeated decode of any checkpoint.
- `2610.01509` Sharpening Tax in Post-Training — Measure with 128 rollouts per task how post-training pushes per-task success probabilities to always or never solved, and tax the lost retry value. *Difference:* The competing reading (few coin-flip cells after RL), base-versus-post-trained on 14 pairs with a Lost/Gained/Both/Neither split at 128 rollouts; its own RL runs select the best-validation checkpoint without a checkpoint table; smaller backbones keep more int…
*Search degraded:* ['s2', 'conference-exports-not-built', 'Q11 arXiv 503 twice', 'gh issue bodies 403 (titles only)']

### C-W46-14 — survived-kill (2026-11-15)
A claim, weak: the three-way split (strict drop / coin flip / argmax flip) of a greedy checkpoint gap with a same-checkpoint draw floor, pre-registered at half and a fifth; the direction alone is a footnote already written by 2606.10709 and 2609.22547.
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
Per position — **solo**: red-teamed (narrowed): a one-sided, conditional kill of the coin-flip clause at about 8 GPU-h; the drop clause waits for C-W46-13 or a continuation run; **lab**: red-teamed: the same reading on the data owners' checkpoints decides both clauses in a day; the letter is step 0c

### C-W46-13 — redesign-owed (2026-11-15)
A claim, weak: the three-way split (strict drop / coin flip / argmax flip) of a greedy checkpoint gap with a same-checkpoint draw floor, pre-registered at half and a fifth; the direction alone is a footnote already written by 2606.10709 and 2609.22547.
Full record: [`data/reports/2026-W46-kill-CL-W46-05.md`](../../../data/reports/2026-W46-kill-CL-W46-05.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched

## Red team

**C-W46-14** — {"date": "2026-11-15", "rounds": 1, "protocol": "attackers (systems, RL-theory, professor, checklist) as three separate passes by the design agent (no Agent tool in this session); defender a separate written pass (rule 2026-10-21); evidence: 2503.09516v5 and 2505.15117 HTML, the Search-R1 repository README, docs/retriever.md, docs/experiment_log.md, infer.py and qa_em.py (raw.githubusercontent.com), Hub API listings, the kill search's four full texts, simulations sim/power.py, sim/flips.py, sim/power_greedy_sens.py; arXiv API calls used: 0 of 6", "objections": [{"persona": "theory; checklist:2026-10-20 (each pre-registered outcome informative); checklist:2026-11-08 (write the decomposition identity before a share headline)", "class": "killing", "objection": "The kill imports $|G| = \\rho q N$ with $\\rho = 0.62$, but 0.62 is $|U_{\\geq 3}| / |Q_{\\mathrm{final}}| - 1$ (4,553 / 2,808) and the claim's gap is $U_{\\geq 1} \\setminus Q_{\\mathrm{best}}$; $U_{\\geq 1} \\supseteq U_{\\geq 3}$, so the claim's $\\rho$ is larger than 0.62 by an unknown amount (the record's own stationary ceiling puts the independent-draw ratio at 1.5-2.0 of $q$). A larger $\\rho$ raises the kill line $0.5…

## First steps if pursued

1. D
2. a
3. y
4. 
5. 0
6. -
7. 1
8. :
9. 
10. d
11. o
12. w
13. n
14. l
15. o
16. a
17. d
18. 
19. t
20. h
21. e
22. 
23. w
24. i
25. k
26. i
27. -
28. 1
29. 8
30. 
31. c
32. o
33. r
34. p
35. u
36. s
37. 
38. a
39. n
40. d
41. 
42. t
43. h
44. e
45. 
46. f
47. l
48. a
49. t
50. 
51. E
52. 5
53. 
54. i
55. n
56. d
57. e
58. x
59. 
60. f
61. r
62. o
63. m
64. 
65. t
66. h
67. e
68. 
69. H
70. u
71. b
72. 
73. (
74. t
75. e
76. n
77. s
78. 
79. o
80. f
81. 
82. G
83. B
84. )
85. ,
86. 
87. s
88. t
89. a
90. r
91. t
92. 
93. t
94. h
95. e
96. 
97. f
98. a
99. i
100. s
101. s
102. 
103. r
104. e
105. t
106. r
107. i
108. e
109. v
110. a
111. l
112. 
113. s
114. e
115. r
116. v
117. e
118. r
119. 
120. o
121. n
122. 
123. a
124. 
125. C
126. P
127. U
128. 
129. b
130. o
131. x
132. 
133. w
134. i
135. t
136. h
137. 
138. a
139. t
140. 
141. l
142. e
143. a
144. s
145. t
146. 
147. 9
148. 6
149. 
150. G
151. B
152. 
153. R
154. A
155. M
156. 
157. (
158. o
159. r
160. 
161. f
162. a
163. i
164. s
165. s
166. -
167. g
168. p
169. u
170. 
171. o
172. n
173. 
174. a
175. 
176. s
177. e
178. c
179. o
180. n
181. d
182. 
183. G
184. P
185. U
186. )
187. ,
188. 
189. p
190. u
191. l
192. l
193. 
194. t
195. h
196. e
197. 
198. v
199. 0
200. .
201. 3
202. 
203. 3
204. B
205. -
206. i
207. t
208. 
209. G
210. R
211. P
212. O
213. 
214. c
215. h
216. e
217. c
218. k
219. p
220. o
221. i
222. n
223. t
224. 
225. (
226. 1
227. 3
228. .
229. 6
230. 
231. G
232. B
233. )
234. 
235. a
236. n
237. d
238. 
239. t
240. h
241. e
242. 
243. H
244. o
245. t
246. p
247. o
248. t
249. Q
250. A
251. 
252. d
253. e
254. v
255. 
256. f
257. i
258. l
259. e
260. ;
261. 
262. r
263. e
264. a
265. d
266. 
267. t
268. h
269. e
270. 
271. v
272. e
273. r
274. l
275. 
276. v
277. a
278. l
279. i
280. d
281. a
282. t
283. i
284. o
285. n
286. 
287. d
288. e
289. c
290. o
291. d
292. i
293. n
294. g
295. 
296. s
297. e
298. t
299. t
300. i
301. n
302. g
303. ,
304. 
305. q
306. a
307. _
308. e
309. m
310. .
311. p
312. y
313. 
314. a
315. n
316. d
317. 
318. t
319. h
320. e
321. 
322. p
323. u
324. b
325. l
326. i
327. c
328. 
329. w
330. a
331. n
332. d
333. b
334. 
335. r
336. u
337. n
338. 
339. (
340. s
341. t
342. e
343. p
344. s
345. ,
346. 
347. c
348. o
349. l
350. l
351. a
352. p
353. s
354. e
355. ,
356. 
357. w
358. h
359. i
360. c
361. h
362. 
363. r
364. u
365. l
366. e
367. 
368. p
369. r
370. o
371. d
372. u
373. c
374. e
375. d
376. 
377. t
378. h
379. e
380. 
381. r
382. e
383. l
384. e
385. a
386. s
387. e
388. )
389. ;
390. 
391. d
392. r
393. a
394. w
395. 
396. a
397. n
398. d
399. 
400. c
401. o
402. m
403. m
404. i
405. t
406. 
407. t
408. h
409. e
410. 
411. 1
412. ,
413. 0
414. 0
415. 0
416. -
417. q
418. u
419. e
420. s
421. t
422. i
423. o
424. n
425. 
426. s
427. u
428. b
429. s
430. e
431. t
432. 
433. w
434. i
435. t
436. h
437. 
438. s
439. e
440. e
441. d
442. 
443. 2
444. 0
445. 2
446. 6
447. 1
448. 1
449. 1
450. 5
451. ;
452. 
453. s
454. e
455. n
456. d
457. 
458. t
459. h
460. e
461. 
462. l
463. e
464. t
465. t
466. e
467. r
468. 
469. t
470. o
471. 
472. t
473. h
474. e
475. 
476. A
477. g
478. e
479. n
480. t
481. i
482. c
483. -
484. O
485. P
486. D
487. 
488. a
489. u
490. t
491. h
492. o
493. r
494. s
495. 
496. (
497. |
498. U
499. >
500. =
501. 1
502. |
503. ,
504. 
505. |
506. Q
507. _
508. b
509. e
510. s
511. t
512. |
513. ,
514. 
515. v
516. a
517. l
518. i
519. d
520. a
521. t
522. i
523. o
524. n
525. 
526. s
527. i
528. z
529. e
530. ,
531. 
532. s
533. i
534. x
535. t
536. e
537. e
538. n
539. 
540. d
541. r
542. a
543. w
544. s
545. 
546. o
547. n
548. 
549. t
550. h
551. e
552. 
553. g
554. a
555. p
556. 
557. s
558. e
559. t
560. )
561. 
562. a
563. n
564. d
565. 
566. t
567. h
568. e
569. 
570. n
571. o
572. t
573. e
574. 
575. t
576. o
577. 
578. t
579. h
580. e
581. 
582. T
583. e
584. m
585. p
586. o
587. r
588. a
589. l
590. 
591. S
592. a
593. m
594. p
595. l
596. i
597. n
598. g
599. 
600. a
601. u
602. t
603. h
604. o
605. r
606. s
607. ;
608. 
609. w
610. r
611. i
612. t
613. e
614. 
615. t
616. h
617. e
618. 
619. m
620. i
621. s
622. c
623. l
624. a
625. s
626. s
627. i
628. f
629. i
630. c
631. a
632. t
633. i
634. o
635. n
636. 
637. m
638. a
639. t
640. r
641. i
642. x
643. 
644. a
645. n
646. d
647. 
648. t
649. h
650. e
651. 
652. k
653. i
654. l
655. l
656. 
657. l
658. i
659. n
660. e
661. 
662. i
663. n
664. t
665. o
666. 
667. t
668. h
669. e
670. 
671. a
672. n
673. a
674. l
675. y
676. s
677. i
678. s
679. 
680. s
681. c
682. r
683. i
684. p
685. t
686. .
687. 
688. D
689. a
690. y
691. 
692. 2
693. 
694. (
695. a
696. b
697. o
698. u
699. t
700. 
701. 7
702. 
703. G
704. P
705. U
706. -
707. h
708. 
709. o
710. n
711. 
712. o
713. n
714. e
715. 
716. H
717. 1
718. 0
719. 0
720. ,
721. 
722. a
723. b
724. o
725. u
726. t
727. 
728. $
729. 2
730. 5
731. )
732. :
733. 
734. g
735. r
736. e
737. e
738. d
739. y
740. 
741. u
742. n
743. d
744. e
745. r
746. 
747. m
748. a
749. x
750. _
751. n
752. u
753. m
754. _
755. s
756. e
757. q
758. s
759. 
760. 1
761. 
762. (
763. s
764. u
765. b
766. s
767. e
768. t
769. )
770. ,
771. 
772. 1
773. 6
774. 
775. (
776. s
777. u
778. b
779. s
780. e
781. t
782. )
783. 
784. a
785. n
786. d
787. 
788. 6
789. 4
790. 
791. (
792. f
793. u
794. l
795. l
796. 
797. d
798. e
799. v
800. )
801. ,
802. 
803. t
804. h
805. e
806. n
807. 
808. s
809. i
810. x
811. t
812. e
813. e
814. n
815. 
816. s
817. a
818. m
819. p
820. l
821. e
822. d
823. 
824. e
825. p
826. i
827. s
828. o
829. d
830. e
831. s
832. 
833. p
834. e
835. r
836. 
837. s
838. u
839. b
840. s
841. e
842. t
843. 
844. q
845. u
846. e
847. s
848. t
849. i
850. o
851. n
852. 
853. a
854. t
855. 
856. t
857. e
858. m
859. p
860. e
861. r
862. a
863. t
864. u
865. r
866. e
867. 
868. 1
869. .
870. 0
871. ,
872. 
873. t
874. o
875. p
876. -
877. p
878. 
879. 1
880. .
881. 0
882. ,
883. 
884. p
885. r
886. e
887. f
888. i
889. x
890. 
891. c
892. a
893. c
894. h
895. i
896. n
897. g
898. 
899. a
900. n
901. d
902. 
903. c
904. h
905. u
906. n
907. k
908. e
909. d
910. 
911. p
912. r
913. e
914. f
915. i
916. l
917. l
918. 
919. o
920. f
921. f
922. ,
923. 
924. p
925. i
926. n
927. n
928. e
929. d
930. 
931. v
932. L
933. L
934. M
935. 
936. b
937. u
938. i
939. l
940. d
941. .
942. 
943. D
944. a
945. y
946. 
947. 3
948. 
949. (
950. C
951. P
952. U
953. )
954. :
955. 
956. r
957. a
958. w
959. 
960. a
961. n
962. d
963. 
964. N
965. P
966. M
967. L
968. E
969. -
970. c
971. o
972. r
973. r
974. e
975. c
976. t
977. e
978. d
979. 
980. b
981. a
982. n
983. d
984. 
985. s
986. h
987. a
988. r
989. e
990. s
991. ,
992. 
993. A
994. ,
995. 
996. A
997. /
998. q
999. ,
1000. 
1001. r
1002. h
1003. o
1004. *
1005. ,
1006. 
1007. t
1008. h
1009. e
1010. 
1011. k
1012. i
1013. l
1014. l
1015. 
1016. t
1017. e
1018. s
1019. t
1020. 
1021. w
1022. i
1023. t
1024. h
1025. 
1026. t
1027. h
1028. e
1029. 
1030. r
1031. a
1032. w
1033. -
1034. c
1035. o
1036. r
1037. r
1038. e
1039. c
1040. t
1041. e
1042. d
1043. 
1044. g
1045. u
1046. a
1047. r
1048. d
1049. ,
1050. 
1051. d
1052. e
1053. l
1054. t
1055. a
1056. _
1057. 0
1058. ,
1059. 
1060. t
1061. h
1062. e
1063. 
1064. K
1065. 
1066. =
1067. 
1068. 4
1069. 
1070. /
1071. 
1072. K
1073. 
1074. =
1075. 
1076. 8
1077. 
1078. s
1079. a
1080. m
1081. e
1082. -
1083. c
1084. h
1085. e
1086. c
1087. k
1088. p
1089. o
1090. i
1091. n
1092. t
1093. 
1094. f
1095. l
1096. i
1097. p
1098. 
1099. r
1100. a
1101. t
1102. e
1103. s
1104. 
1105. a
1106. g
1107. a
1108. i
1109. n
1110. s
1111. t
1112. 
1113. 2
1114. 6
1115. 0
1116. 6
1117. .
1118. 1
1119. 0
1120. 7
1121. 0
1122. 9
1123. '
1124. s
1125. 
1126. 2
1127. 0
1128. %
1129. ,
1130. 
1131. t
1132. h
1133. e
1134. 
1135. p
1136. 
1137. >
1138. =
1139. 
1140. 0
1141. .
1142. 8
1143. 
1144. g
1145. r
1146. e
1147. e
1148. d
1149. y
1150. -
1151. f
1152. a
1153. i
1154. l
1155. u
1156. r
1157. e
1158. 
1159. s
1160. h
1161. a
1162. r
1163. e
1164. ,
1165. 
1166. t
1167. h
1168. e
1169. 
1170. m
1171. i
1172. s
1173. s
1174. i
1175. n
1176. g
1177. -
1178. a
1179. n
1180. s
1181. w
1182. e
1183. r
1184. 
1185. s
1186. p
1187. l
1188. i
1189. t
1190. ,
1191. 
1192. a
1193. n
1194. d
1195. 
1196. t
1197. h
1198. e
1199. 
1200. h
1201. a
1202. r
1203. n
1204. e
1205. s
1206. s
1207. 
1208. c
1209. a
1210. l
1211. i
1212. b
1213. r
1214. a
1215. t
1216. i
1217. o
1218. n
1219. s
1220. .
1221. 
1222. O
1223. p
1224. t
1225. i
1226. o
1227. n
1228. a
1229. l
1230. 
1231. d
1232. a
1233. y
1234. 
1235. 4
1236. 
1237. (
1238. a
1239. b
1240. o
1241. u
1242. t
1243. 
1244. 6
1245. 
1246. G
1247. P
1248. U
1249. -
1250. h
1251. )
1252. :
1253. 
1254. t
1255. h
1256. e
1257. 
1258. v
1259. 0
1260. .
1261. 1
1262. 
1263. s
1264. i
1265. b
1266. l
1267. i
1268. n
1269. g
1270. 
1271. f
1272. o
1273. r
1274. 
1275. t
1276. h
1277. e
1278. 
1279. b
1280. e
1281. t
1282. w
1283. e
1284. e
1285. n
1286. -
1287. r
1288. e
1289. c
1290. i
1291. p
1292. e
1293. 
1294. t
1295. h
1296. r
1297. e
1298. e
1299. -
1300. w
1301. a
1302. y
1303. 
1304. s
1305. p
1306. l
1307. i
1308. t
1309. 
1310. a
1311. n
1312. d
1313. 
1314. t
1315. h
1316. e
1317. 
1318. 2
1319. 6
1320. 0
1321. 9
1322. .
1323. 2
1324. 2
1325. 5
1326. 4
1327. 7
1328. 
1329. p
1330. l
1331. a
1332. c
1333. e
1334. b
1335. o
1336. .

## Decisions for Jacob

- Spend the 8 GPU-h now on the conditional kill (steps 0-3), or wait for the Agentic-OPD authors' answer to the letter, which would fix rho and could decide both clauses on their own 100 checkpoints.
- If the pool clears the line, fund the cheapest second checkpoint for the drop clause: a 50-step GRPO continuation from the public checkpoint saving every 5 steps (30-50 GPU-h, judgment) or C-W46-13's fresh 300-step run (about 150 GPU-h).
- Accept the narrowed headline (band on the true probability from >= 16 draws, corrected; gap U>=1 against the best) as CL-W46-05 v3, or split the two quantifiers into two claims.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L2 lane sentence plus the card's protocol quotes); probes C-W46-14 (cheapest, 8 GPU-h) and C-W46-13 (import S12xF1, 150 GPU-h); concept-level kill search owed (rule 17); Gate 2B flagged at filing
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 5: born W46: $20 step-0 probe on a public checkpoint kills before any training; reverses the two occupants' stated reading; direction is pass@k folklore (2B flag); concept-level kill search runs this week (rule 17)
- 2026-11-15 — claim open: concept-level kill search (data/reports/2026-W46-kill-CL-W46-05.md): survived-kill — gate none; Weak survival: no fetched source splits a greedy checkpoint gap by a draw floor or states most of it is single-decode noise, but the direction (finite-sample solved status is stochastic; flips are partly sampling noise, partly drift) is written in the same search-agent GRPO setting by 2606.10709 and th…
- 2026-11-15 — claim open: design red team of C-W46-14 v2 (data/reports/2026-W46-redteam-C-W46-14.md): red-teamed — Red-teamed, narrowed: 3 killing objections answered or conceded with the design rewritten (support reading withdrawn, rho* reported; kill made explicitly conditional on the released final-or-last-stable checkpoint; novelty answered by register); the probe is a one-sided conditional kill of the coin-flip claus…
- 2026-11-15 — claim open: re-ranked after the W46 kill searches and red teams: rank 5 -> 4: proper (narrow, weak) after this week's kill search and design red team of C-W46-14 v2 (8 GPU-h, $35 conditional kill on a public checkpoint); the drop clause needs a second checkpoint
- 2026-11-15 — C-W46-14 survived-kill: claim-level kill search of CL-W46-05 (data/reports/2026-W46-kill-CL-W46-05.md): survived-kill — Run as written plus a split-half placebo and an m=16 sensitivity row on the 0.2/0.8 band edges; state the transfer assumption from the public final checkpoint.

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-05`, version 4)
- probe `C-W46-14`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-05.md`
- probe `C-W46-13`: `data/candidates/2026-W46.jsonl`; kill record `data/reports/2026-W46-kill-CL-W46-05.md`
