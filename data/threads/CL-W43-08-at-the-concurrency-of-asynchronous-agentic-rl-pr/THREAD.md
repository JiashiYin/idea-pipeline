# At the concurrency of asynchronous agentic RL, Prorsa's prefill-decode role-switching rule with its ten-second arrival forecast zeroed captures, at matched damping, within ten points of the oracle-normalised headroom that the same rule captures with the forecast.

`CL-W43-08` · lane **L3** · status **open** · rank 3 · position both · refreshed 2026-11-16

## Status

Open claim. The claim survived its concept-level kill search (2026-11-15); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: none hard after the design red team; graded proper (narrow): Gate 3 one community (engine/router maintainers, RL infra); Gate 2B against the occupant's stated belief (Prorsa); Gate 5 flag. Grade on paper: proper (narrow). Next action: see First steps.

## The claim

- **Headline:** At the concurrency of asynchronous agentic RL, Prorsa's prefill-decode role-switching rule with its ten-second arrival forecast zeroed captures, at matched damping, within ten points of the oracle-normalised headroom that the same rule captures with the forecast.
- **Current belief (the field's):** Prorsa 2610.16592 reports forecast error (WAPE 5.4-14.4%) for role switching without the throughput it costs and no oracle; FluidPD's abstract motivates observation-only reassignment against forecasting-free autoscaling, never against an oracle
- **If true:** Switching papers report capture ratio against the hindsight oracle; training-infra teams drop the forecaster from the recipe when the rule matches it, and stop building forecasters where the oracle headroom is under 10%
- **If false:** The forecaster captures most of a large headroom: the field gets its first oracle-normalized number for 10-second forecasting and the next question is which ignored term closes the rest

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: Prorsa reports WAPE 'sufficient to guide role switching' (§5.5) and a static-only baseline (§5.4), no oracle, no damping statement, no throughput cost of forecast error; FluidPD §V-F: thresholds 'directly control reaction time ... overly aggressive values can cause churn'; SGLang roadmap 43699 (open item): 'a router-driven policy that flips roles on load instead of an operator call'; PR 28403: 'an automatic load-based flip policy is out of scope here'. Who pays: SGLang's PD maintainers choosing the router's flip policy; every team running asynchronous agentic RL on verl, ROLL, AReaL or slime deciding whether Prorsa's 6.4K lines of forecasting and switching are worth building; serving teams reading FluidPD.
- **Impact ceiling:** **floor**: A released replay harness with the first oracle-normalised headroom bracket and capture ratios for P/D role switching on one public coding trace, with the damping-versus-information decomposition. Requires steps 0–2. Judgment p 0.65.; **middle**: The scaling result across three workloads, two regimes and three switch-cost models, cited by rollout-engine and router papers as the reason to switch (or not) at a given concurrency and as the reason a damped backlog rule suffices; the SGLang router policy item cites it. Requires the calibration gate to pass and one real-trace confirmation of timing. Judgment p 0.3.; **ceiling**: Switching papers adopt the oracle bracket as a reporting standard and a damped backlog rule ships as a framework default (SGLang router or verl); Prorsa/PEARL revisions report $\rho$. Requires one maintainer to adopt and the optional live calibration arm. Judgment p 0.08.
- **Relevance:** L3 routes (Lloyd / Netravali / Tri Dao): direct — a definitive comparison of a rollout-engine control decision with a hindsight bound. Industry: RL-infra teams choosing topology, SGLang router maintainers. Jacob's edge: stochastic processes (superposition and the fluctuation-versus-drift decomposition), online algorithms with switching costs (the import: Chen et al. 2015 AFHC, ABCS 2021), computer engineering for the replay. Zero relevance to L1, L2 (no training signal touched), L4, L5.
- **Kill probe:** Steps 0–2 on CPU, 0 GPU-hours, $0, 7 days (optional 16 GPU-hours, about $60 for the shipped-flip calibration); 08a dead if the perfect-forecast arm captures at least 0.3 more than the zeroed arm at matched damping (band excluding 0.1) in two of three workloads at $N \ge 1024$ async with $\hat H \ge 0.05$; 08b likewise for hysteresis versus damped forecaster.
- **Density and ownership:** Concept kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W43-08.md): eleven dynamic-P/D-boundary papers in twelve months, role-flip controllers about one per six weeks (Arrow, DOPD, TokenScale, PEARL, FluidPD, Prorsa, SGLang PR 28403 + three follow-up PRs); the oracle-normalised comparison has zero occupants (Q2, Q2b: 3 and 17 hits, none on role switching); FluidPD's 'oracle' is a per-window static ratio, TokenScale's hindsight check is a correlation on single-turn serving. Occupied: the forecaster and the RL-side flip (Prorsa), the observation rule with persistence and cool-down in serving (FluidPD), the flip mechanism (SGLang), the simulator (Frontier). Pre-window precedents: Splitwise 2311.18677 (mixed pool), DistServe 2401.09670 (static split), Hofri–Ross 1987 (two queues with setup times, threshold optimality), Chen et al. 1504.06681 (value of a prediction window under switchi…
- **Why now:** Prorsa 2026-10-12 (forecaster and WAPE in print, static-only baseline, no damping stated); FluidPD 2026-10-02 (the damped observation rule in print, serving only); SGLang PR 28403 merged and listed done in the Q4-2026 roadmap with the load-driven policy open (read 2026-11-15/16); Nebius trajectories public since 2024-12. Race window about 1–2x time-to-result: Prorsa's or PEARL's group could add an oracle to a revision in a week, which is why the solo replay is filed first.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass: premise numbers fetched and dated (Prorsa WAPE 5.40-14.37%, speedup 1.0-1.44x over hindsight static, 5-s cancel-and-resend switch, 1.74x ratio drift; SGLang PR 28403 drain-to-idle and prefix-cache release); conditioning set written (deterministic given the trajectory set; no sampling party, no temperature); H and rho are properties of the named (workload, protocol, switch model, constants) tuple |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass: $0, 0 GPU-hours, 7 days (about 200 CPU-hours; optional 16 GPU-h / $60 shipped-flip calibration); three pre-registered kills (08a, 08b) and a pre-registered guard; both outcomes informative (first oracle bracket for role switching either way) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass, route A (Prorsa text; FluidPD threshold-churn sentence; SGLang roadmap 43699 open router-policy item and PR 28403 'out of scope' sentence - three source types) and route B (expected result differs from the occupant's stated belief 'sufficient to guide role switching') |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass at one community: rollout-engine and router maintainers (the flip policy), RL-infra teams choosing topology; proper, not golden |
| G4 | mechanism and consequence | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass with the mechanism rewritten: two terms - a fluctuation term that shrinks like 1/N and a KV-capacity drift term that grows with N and lifetime; consequences per outcome written (delete the forecaster / keep it with its first oracle-normalised value / switching dead at steady state) |
| G5 | durability; lab-adjacent | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass with a flag: constants (theta_P, C_KV, t_0, t_1, switch model) enter through the reported tuple; the ruler applies to any disaggregated engine |
| G6 | ownership, density, race window; position clause | design red team 2026-11-15 (data/reports/2026-W46-redteam-C-W43-04.md): pass: measurement unoccupied (kill search 2026-11-15); density one role-flip controller per six weeks; pre-window precedents Splitwise, DistServe, Hofri-Ross, AFHC, ABCS; race window about 1-2x time-to-result and timing inputs partly synthetic keep it from golden; solo survives, lab version is the same arms on a timestamped trace |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-04 | Hindsight-optimal switching bounds forecast-guided prefill-decode role switching (v2: designed after the concept-level… | Steps 0–2 on CPU, 0 GPU-hours, $0, 7 days (optional 16 GPU-hours, about $60 for the shipped-flip calibration); 08a dead if the perfect-forecast arm captures at least 0.3 more than the zeroed arm at matched damping (band excluding 0.1) in t… | red-teamed | — |

## Kill search

### Concept level (CL-W43-08) — survived-kill (2026-11-15)
No paper compares a threshold role-switching rule against a hindsight-optimal schedule or reports a capture ratio; Prorsa owns the forecaster (static-split baseline only, zero 'oracle'/'hindsight' occurrences), FluidPD the hysteresis rule in serving (its 'oracle' is a per-window static ratio), TokenScale a correlation-only hindsight check on single-turn serving; SGLang's Q4-2026 roadmap ships the switch mechanism (PR 28403) and lists the load-driven policy as open. Proper grade; two design flags (Prorsa's W_P already includes the backlog; Prorsa's stated lever is KV capacity that grows with concurrency).
Full record: [`data/reports/2026-W46-kill-CL-W43-08.md`](../../../data/reports/2026-W46-kill-CL-W43-08.md).
**Why not done before:** Enabling pieces landed: SGLang runtime P<->D role switching shipped (PR 28403, roadmap Q2/Q4 2026) with the load-driven policy still open; Prorsa (2026-10-12) put the forecaster and its WAPE in print without the cost of error; FluidPD (2026-10-02) put the observation rule in print without a forecaster arm; Frontier PDD support since 2026-08; the oracle belongs to none of the three groups.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.16592` Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcemen… — Watch every trajectory's lifecycle stage to forecast ten seconds of prefill tokens and decode KV admissions, then flip verl/SGLang rollout engines between prefill and decode roles by a sizing rule. *Difference:* Owns the forecaster and the RL-side role switch; compares only to a hindsight-chosen static split, no oracle, no observation-only arm, no throughput cost of forecast error; its W_P already counts the backlog; its stated lever (KV capacity) grows with concurre…
- `2610.06917` FluidPD: In-Place Elasticity for SLO-Aware Prefill-Decode Disaggregated LLM Serving — Steal bounded prefill onto decode workers for bursts and reassign a running worker's role in place when two pressure indices stay past thresholds for K intervals, with a cool-down. *Difference:* The hysteresis arm shipped in serving; compared against static engines and Dynamo autoscaling, never against a forecaster or a switching oracle; its 'oracle' is a per-window static ratio; open arrivals, no RL.
- `2512.03416` TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velo… — Scale prefillers and decoders by the tokens per second each stage can absorb, and convert a profiled share of decoders into temporary prefillers during bursts. *Difference:* Observation-derived leading indicator for role conversion; hindsight check is provisioned-vs-required instance counts by correlation only, utilization-derived; single-turn serving by its own statement.
- `2609.35158` PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learni… — Refit a closed-form makespan model from telemetry each rollout step, enumerate P/D configurations under the GPU budget, and switch only when the predicted makespan improves by more than a mode-dependent threshold. *Difference:* Step-granularity model-predicted switching with hysteresis on a prediction, triggered by elastic GPU events; no oracle, no observation-only arm.
- `2606.01839` Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serv… — Make the conversation the scheduling unit so first-turn prefill goes to a prefiller and the memory-bound tail stays on one decoder. *Difference:* Removes prediction by changing the unit, not by a threshold rule; no role switching, no oracle.
*Search degraded:* ['s2', 'arxiv-api: Q8 and second id_list (Rate exceeded x2)', 'conference exports not built', 'complaint stream: verl/AReaL 422 via search endpoint; issues endpoint 403']

## Red team

**C-W43-04** — {"date": "2026-11-16", "rounds": 2, "protocol": "attackers (systems, RL-theory, professor, checklist) as three sequential passes in one agent (no Agent tool in this session), written before any answer; defender a separate pass (rule 2026-10-21); evidence fetched: Prorsa / FluidPD / PEARL / TokenScale full texts (kill-search scratchpad), SGLang PR 28403 body and four follow-up PRs (GitHub search endpoint), nebius/SWE-agent-trajectories schema (Hugging Face API), toy replay sim/pdswitch.py on synthetic traces (ten cells, one or two seeds); arXiv API not called (0 of 6)", "objections": [{"persona": "systems", "round": 1, "objection": "The 5-s cancel-and-resend switch is Prorsa's own mechanism (KV persisted to remote storage, retries on retained prefixes, 6.4K lines on verl + SGLang), not what any team gets from the shipped engine. SGLang's flip (PR 28403) drains to idle before teardown as a correctness requirement, releases the prefix cache on the flip, is driven by an operator or router call, is default-off and exists for the Mooncake and Mori backends only; no flip duration is reported. A headroom read under the 5-s model is not the headroom the roadmap's router policy could realis…

## First steps if pursued

1. D
2. a
3. y
4. 
5. 1
6. -
7. 2
8. 
9. (
10. C
11. P
12. U
13. ,
14. 
15. $
16. 0
17. )
18. :
19. 
20. d
21. o
22. w
23. n
24. l
25. o
26. a
27. d
28. 
29. n
30. e
31. b
32. i
33. u
34. s
35. /
36. S
37. W
38. E
39. -
40. a
41. g
42. e
43. n
44. t
45. -
46. t
47. r
48. a
49. j
50. e
51. c
52. t
53. o
54. r
55. i
56. e
57. s
58. 
59. (
60. 1
61. 2
62. 
63. p
64. a
65. r
66. q
67. u
68. e
69. t
70. 
71. s
72. h
73. a
74. r
75. d
76. s
77. )
78. ,
79. 
80. t
81. o
82. k
83. e
84. n
85. i
86. z
87. e
88. 
89. p
90. e
91. r
92. -
93. t
94. u
95. r
96. n
97. 
98. p
99. r
100. o
101. m
102. p
103. t
104. 
105. a
106. n
107. d
108. 
109. o
110. u
111. t
112. p
113. u
114. t
115. 
116. l
117. e
118. n
119. g
120. t
121. h
122. s
123. 
124. w
125. i
126. t
127. h
128. 
129. t
130. h
131. e
132. 
133. Q
134. w
135. e
136. n
137. 3
138. 
139. t
140. o
141. k
142. e
143. n
144. i
145. z
146. e
147. r
148. ,
149. 
150. k
151. e
152. e
153. p
154. 
155. t
156. h
157. e
158. 
159. e
160. x
161. i
162. t
163. _
164. s
165. t
166. a
167. t
168. u
169. s
170. 
171. m
172. i
173. x
174. ;
175. 
176. f
177. e
178. t
179. c
180. h
181. 
182. t
183. h
184. e
185. 
186. s
187. w
188. e
189. -
190. b
191. e
192. n
193. c
194. h
195. /
196. e
197. x
198. p
199. e
200. r
201. i
202. m
203. e
204. n
205. t
206. s
207. 
208. .
209. t
210. r
211. a
212. j
213. 
214. l
215. i
216. s
217. t
218. i
219. n
220. g
221. 
222. f
223. r
224. o
225. m
226. 
227. a
228. 
229. m
230. a
231. c
232. h
233. i
234. n
235. e
236. 
237. w
238. i
239. t
240. h
241. 
242. G
243. i
244. t
245. H
246. u
247. b
248. 
249. a
250. c
251. c
252. e
253. s
254. s
255. 
256. a
257. n
258. d
259. 
260. r
261. e
262. a
263. d
264. 
265. e
266. x
267. e
268. c
269. u
270. t
271. i
272. o
273. n
274. _
275. t
276. i
277. m
278. e
279. 
280. p
281. e
282. r
283. 
284. s
285. t
286. e
287. p
288. 
289. (
290. e
291. l
292. s
293. e
294. 
295. p
296. r
297. e
298. -
299. r
300. e
301. g
302. i
303. s
304. t
305. e
306. r
307. 
308. t
309. h
310. e
311. 
312. l
313. o
314. g
315. n
316. o
317. r
318. m
319. a
320. l
321. 
322. t
323. o
324. o
325. l
326. -
327. g
328. a
329. p
330. 
331. s
332. w
333. e
334. e
335. p
336. ,
337. 
338. m
339. e
340. d
341. i
342. a
343. n
344. s
345. 
346. 1
347. /
348. 3
349. /
350. 1
351. 0
352. 
353. s
354. )
355. ;
356. 
357. f
358. e
359. t
360. c
361. h
362. 
363. o
364. n
365. e
366. 
367. p
368. u
369. b
370. l
371. i
372. c
373. 
374. D
375. A
376. P
377. O
378. /
379. O
380. p
381. e
382. n
383. R
384. 1
385. 
386. r
387. o
388. l
389. l
390. o
391. u
392. t
393. 
394. r
395. e
396. l
397. e
398. a
399. s
400. e
401. '
402. s
403. 
404. f
405. i
406. l
407. e
408. 
409. l
410. i
411. s
412. t
413. i
414. n
415. g
416. 
417. f
418. o
419. r
420. 
421. m
422. a
423. t
424. h
425. 
426. l
427. e
428. n
429. g
430. t
431. h
432. s
433. ;
434. 
435. f
436. i
437. x
438. 
439. t
440. h
441. e
442. t
443. a
444. _
445. P
446. ,
447. 
448. C
449. _
450. K
451. V
452. ,
453. 
454. t
455. _
456. 0
457. ,
458. 
459. t
460. _
461. 1
462. 
463. f
464. r
465. o
466. m
467. 
468. o
469. n
470. e
471. 
472. p
473. u
474. b
475. l
476. i
477. s
478. h
479. e
480. d
481. 
482. R
483. o
484. o
485. f
486. l
487. i
488. n
489. e
490. 
491. p
492. r
493. o
494. f
495. i
496. l
497. e
498. 
499. o
500. f
501. 
502. a
503. 
504. 3
505. 0
506. B
507. -
508. A
509. 3
510. B
511. 
512. F
513. P
514. 8
515. 
516. i
517. n
518. s
519. t
520. a
521. n
522. c
523. e
524. 
525. a
526. n
527. d
528. 
529. w
530. r
531. i
532. t
533. e
534. 
535. t
536. h
537. e
538. 
539. f
540. i
541. l
542. e
543. 
544. n
545. a
546. m
547. e
548. 
549. i
550. n
551. t
552. o
553. 
554. t
555. h
556. e
557. 
558. r
559. e
560. c
561. o
562. r
563. d
564. ;
565. 
566. s
567. e
568. n
569. d
570. 
571. t
572. h
573. e
574. 
575. l
576. e
577. t
578. t
579. e
580. r
581. 
582. t
583. o
584. 
585. P
586. r
587. o
588. r
589. s
590. a
591. '
592. s
593. 
594. a
595. u
596. t
597. h
598. o
599. r
600. s
601. 
602. a
603. s
604. k
605. i
606. n
607. g
608. 
609. f
610. o
611. r
612. 
613. o
614. n
615. e
616. 
617. t
618. i
619. m
620. e
621. s
622. t
623. a
624. m
625. p
626. e
627. d
628. 
629. r
630. o
631. l
632. l
633. o
634. u
635. t
636. 
637. t
638. r
639. a
640. c
641. e
642. .
643. 
644. D
645. a
646. y
647. 
648. 3
649. -
650. 5
651. 
652. (
653. C
654. P
655. U
656. ,
657. 
658. $
659. 0
660. )
661. :
662. 
663. e
664. x
665. t
666. e
667. n
668. d
669. 
670. s
671. i
672. m
673. /
674. p
675. d
676. s
677. w
678. i
679. t
680. c
681. h
682. .
683. p
684. y
685. 
686. (
687. p
688. e
689. r
690. -
691. i
692. n
693. s
694. t
695. a
696. n
697. c
698. e
699. 
700. K
701. V
702. 
703. p
704. o
705. o
706. l
707. s
708. ,
709. 
710. c
711. h
712. u
713. n
714. k
715. e
716. d
717. 
718. p
719. r
720. e
721. f
722. i
723. l
724. l
725. ,
726. 
727. c
728. a
729. c
730. h
731. e
732. 
733. r
734. a
735. t
736. i
737. o
738. 
739. h
740. ,
741. 
742. t
743. h
744. e
745. 
746. t
747. h
748. r
749. e
750. e
751. 
752. s
753. w
754. i
755. t
756. c
757. h
758. 
759. m
760. o
761. d
762. e
763. l
764. s
765. 
766. w
767. i
768. t
769. h
770. 
771. (
772. c
773. )
774. 
775. f
776. r
777. o
778. m
779. 
780. P
781. R
782. 
783. 2
784. 8
785. 4
786. 0
787. 3
788. ,
789. 
790. c
791. l
792. o
793. n
794. e
795. -
796. a
797. h
798. e
799. a
800. d
801. 
802. f
803. o
804. r
805. e
806. c
807. a
808. s
809. t
810. ,
811. 
812. W
813. A
814. P
815. E
816. 
817. p
818. e
819. r
820. t
821. u
822. r
823. b
824. a
825. t
826. i
827. o
828. n
829. ,
830. 
831. f
832. l
833. u
834. i
835. d
836. 
837. r
838. e
839. l
840. a
841. x
842. a
843. t
844. i
845. o
846. n
847. ,
848. 
849. t
850. h
851. e
852. 
853. n
854. o
855. n
856. -
857. s
858. t
859. a
860. t
861. i
862. o
863. n
864. a
865. r
866. y
867. 
868. s
869. e
870. g
871. m
872. e
873. n
874. t
875. 
876. t
877. r
878. a
879. c
880. e
881. 
882. a
883. t
884. 
885. P
886. r
887. o
888. r
889. s
890. a
891. '
892. s
893. 
894. 1
895. .
896. 7
897. 4
898. x
899. /
900. 1
901. .
902. 2
903. 0
904. x
905. 
906. r
907. a
908. t
909. i
910. o
911. 
912. l
913. e
914. v
915. e
916. l
917. s
918. )
919. 
920. w
921. i
922. t
923. h
924. 
925. t
926. h
927. e
928. 
929. u
930. n
931. i
932. t
933. 
934. t
935. e
936. s
937. t
938. s
939. 
940. (
941. w
942. o
943. r
944. k
945. 
946. c
947. o
948. n
949. s
950. e
951. r
952. v
953. a
954. t
955. i
956. o
957. n
958. ,
959. 
960. s
961. t
962. a
963. t
964. i
965. c
966. 
967. c
968. o
969. n
970. v
971. e
972. x
973. i
974. t
975. y
976. ,
977. 
978. o
979. r
980. a
981. c
982. l
983. e
984. 
985. <
986. =
987. 
988. e
989. v
990. e
991. r
992. y
993. 
994. s
995. e
996. e
997. d
998. )
999. .
1000. 
1001. D
1002. a
1003. y
1004. 
1005. 6
1006. -
1007. 7
1008. 
1009. (
1010. a
1011. b
1012. o
1013. u
1014. t
1015. 
1016. 2
1017. 0
1018. 0
1019. 
1020. C
1021. P
1022. U
1023. -
1024. h
1025. o
1026. u
1027. r
1028. s
1029. 
1030. o
1031. n
1032. 
1033. 1
1034. 6
1035. 
1036. c
1037. o
1038. r
1039. e
1040. s
1041. )
1042. :
1043. 
1044. r
1045. u
1046. n
1047. 
1048. t
1049. h
1050. e
1051. 
1052. g
1053. r
1054. i
1055. d
1056. ,
1057. 
1058. r
1059. e
1060. a
1061. d
1062. 
1063. t
1064. h
1065. e
1066. 
1067. P
1068. r
1069. o
1070. r
1071. s
1072. a
1073. -
1074. b
1075. a
1076. n
1077. d
1078. 
1079. c
1080. o
1081. n
1082. s
1083. i
1084. s
1085. t
1086. e
1087. n
1088. c
1089. y
1090. 
1091. r
1092. o
1093. w
1094. 
1095. f
1096. i
1097. r
1098. s
1099. t
1100. ,
1101. 
1102. t
1103. h
1104. e
1105. n
1106. 
1107. t
1108. h
1109. e
1110. 
1111. 0
1112. 8
1113. a
1114. /
1115. 0
1116. 8
1117. b
1118. /
1119. 0
1120. 8
1121. c
1122. 
1123. c
1124. e
1125. l
1126. l
1127. s
1128. 
1129. w
1130. i
1131. t
1132. h
1133. 
1134. t
1135. h
1136. e
1137. 
1138. p
1139. a
1140. i
1141. r
1142. e
1143. d
1144. 
1145. t
1146. -
1147. i
1148. n
1149. t
1150. e
1151. r
1152. v
1153. a
1154. l
1155. s
1156. ;
1157. 
1158. w
1159. r
1160. i
1161. t
1162. e
1163. 
1164. t
1165. h
1166. e
1167. 
1168. o
1169. r
1170. a
1171. c
1172. l
1173. e
1174. 
1175. b
1176. r
1177. a
1178. c
1179. k
1180. e
1181. t
1182. 
1183. t
1184. a
1185. b
1186. l
1187. e
1188. .
1189. 
1190. O
1191. p
1192. t
1193. i
1194. o
1195. n
1196. a
1197. l
1198. 
1199. d
1200. a
1201. y
1202. 
1203. 8
1204. 
1205. (
1206. 1
1207. 6
1208. 
1209. G
1210. P
1211. U
1212. -
1213. h
1214. ,
1215. 
1216. a
1217. b
1218. o
1219. u
1220. t
1221. 
1222. $
1223. 6
1224. 0
1225. )
1226. :
1227. 
1228. d
1229. r
1230. i
1231. v
1232. e
1233. 
1234. S
1235. G
1236. L
1237. a
1238. n
1239. g
1240. '
1241. s
1242. 
1243. /
1244. p
1245. d
1246. _
1247. r
1248. o
1249. l
1250. e
1251. _
1252. s
1253. w
1254. i
1255. t
1256. c
1257. h
1258. 
1259. o
1260. n
1261. 
1262. a
1263. 
1264. 2
1265. -
1266. G
1267. P
1268. U
1269. 
1270. 1
1271. P
1272. 1
1273. D
1274. 
1275. d
1276. e
1277. p
1278. l
1279. o
1280. y
1281. m
1282. e
1283. n
1284. t
1285. 
1286. u
1287. n
1288. d
1289. e
1290. r
1291. 
1292. a
1293. 
1294. r
1295. e
1296. p
1297. l
1298. a
1299. y
1300. e
1301. d
1302. 
1303. c
1304. l
1305. o
1306. s
1307. e
1308. d
1309. 
1310. l
1311. o
1312. o
1313. p
1314. 
1315. a
1316. t
1317. 
1318. N
1319. 
1320. =
1321. 
1322. 6
1323. 4
1324. 
1325. t
1326. o
1327. 
1328. m
1329. e
1330. a
1331. s
1332. u
1333. r
1334. e
1335. 
1336. d
1337. r
1338. a
1339. i
1340. n
1341. 
1342. t
1343. i
1344. m
1345. e
1346. ,
1347. 
1348. f
1349. l
1350. i
1351. p
1352. 
1353. d
1354. u
1355. r
1356. a
1357. t
1358. i
1359. o
1360. n
1361. 
1362. a
1363. n
1364. d
1365. 
1366. p
1367. o
1368. s
1369. t
1370. -
1371. f
1372. l
1373. i
1374. p
1375. 
1376. c
1377. a
1378. c
1379. h
1380. e
1381. 
1382. m
1383. i
1384. s
1385. s
1386. e
1387. s
1388. 
1389. f
1390. o
1391. r
1392. 
1393. s
1394. w
1395. i
1396. t
1397. c
1398. h
1399. 
1400. m
1401. o
1402. d
1403. e
1404. l
1405. 
1406. (
1407. c
1408. )
1409. .

## Decisions for Jacob

- Spend the seven CPU days on a replay whose timing inputs are synthetic unless the SWE-agent .traj listing is confirmed, or wait for a timestamped rollout trace (the letter to Prorsa's authors is the re-open test).
- Approve the narrowed headline (claim_headline_v2: the forecast increment inside Prorsa's rule at matched damping) as CL-W43-08 v9, or keep the literal threshold-rule sentence as the headline with 08b as its kill.
- Fund the optional 16 GPU-hour arm that drives SGLang's shipped flip (PR 28403) to calibrate the drain-to-idle switch model, which is the cost model the roadmap's router-policy consumer needs.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-20 — claim open: new claim, split from CL-W43-07 (one sentence per headline); probe C-W43-04
- 2026-10-25 — claim open: claims (closing W43): re-ranked to 11 — no new probe this week
- 2026-11-01 — claim open: ranked 6 after the W44 kill searches: unchanged; kill search owed
- 2026-11-02 — claim open: pressure #10 (2026-11-02): L21 'discarding early-returned short samples', L24 'kept out of training batches [...] the orchestrator backfills samples that were filtered out', L23 '33 billion tokens per day [...] around 16 billion are trainable'; density P10a = 0, P10b = 1; the length-fate question is unposed and bears on this claim's demand model; records L21, L23, L24, Q09 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): no new probe; rank 11 -> 14
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 6 -> 14; ranked 14 (was 6): unchanged probe; a second control loop (C-W45-11) filed as an orphan beside it rather than widening the headline before its kill search; kill search owed since W43
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 3: L3 open; kill search owed; orphan C-W45-11 attaches after it
- 2026-11-15 — claim open: claims (W46, 2026-11-15): rank 3 -> 10; kill search owed since W43; unchanged probe
- 2026-11-15 — claim open: concept-level kill search (data/reports/2026-W46-kill-CL-W43-08.md): survived-kill — gate none; No paper compares a threshold role-switching rule against a hindsight-optimal schedule or reports a capture ratio; Prorsa owns the forecaster (static-split baseline only, zero 'oracle'/'hindsight' occurrences), FluidPD the hysteresis rule in serving (its 'oracle' is a per-window static ratio), TokenSca…
- 2026-11-15 — claim open: design red team of C-W43-04 v2 (data/reports/2026-W46-redteam-C-W43-04.md): red-teamed — No killing objection stands after two rounds; five killing objections (fit-to-target calibration, oracle definition, forecaster information set, known-theorem charge, stationary straw man) were answered or conceded with rewrites that narrow the probe to the forecast increment inside Prorsa's rule at matched d…
- 2026-11-15 — claim open: re-ranked after the W46 kill searches and red teams: rank 10 -> 3: proper (narrow) after this week's kill search and design red team of C-W43-04 v2 ($0 replay, 7 CPU-days); headline narrowed to the forecast increment inside Prorsa's rule at matched damping

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-08`, version 10)
- probe `C-W43-04`: `data/candidates/2026-W43.jsonl`
