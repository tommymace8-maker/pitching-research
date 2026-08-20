# FINDINGS — Verified Finding Registry

**A flat, greppable index of every substantive finding in `research/`.**
Compiled 2026-08-17 from `library/*.md`, `daily/*.md`, and `src/core/biomech/references.ts`.
Population scope: **elite throwers, 85 mph floor** (elite HS prospect -> NCAA D1 -> MiLB -> MLB). Nothing here is written for youth or average high-school pitchers.

---

## How to use this

Search by field. Every entry has the same fields, one per line, so `grep` works:

```
grep "CAUSALITY: MANIPULATED_NULL" FINDINGS.md     # what has been tested and failed
grep "EVIDENCE: UNSOURCED" FINDINGS.md             # the fabrications, so the debunking surfaces
grep -i "stride" FINDINGS.md                       # everything on one topic
grep "POPULATION: MLB" FINDINGS.md
```

**Fields**

| Field | Meaning |
|---|---|
| `### F-###` | Stable ID. Never reuse or renumber. |
| `TOPIC` | Keyword list for searching. Deliberately redundant. |
| `CLAIM` | The finding in one sentence, at the strength the source supports. |
| `NUMBERS` | Every number with its units and its sample size. |
| `POPULATION` | Who was measured. `off_population_youth` / `off_population_HS` = below our floor, directional only. |
| `EVIDENCE` | ESTABLISHED / EMERGING / WEAK / FOLKLORE / UNSOURCED |
| `CAUSALITY` | INTERVENTION / MANIPULATED_NULL / CROSS_SECTIONAL / MECHANISM |
| `SOURCE` | Author, year, journal, PMID/PMC where the corpus records one. |
| `COACHING` | What may be said out loud, or explicitly that nothing may be. |
| `CONFIDENCE` | Plain-language limit on the entry. |
| `SEE ALSO` | Related F-IDs. |

**EVIDENCE grades**

- **ESTABLISHED** — replicated across independent studies, or undisputed basic mechanics/physics.
- **EMERGING** — real data, but limited, conflicting, single-lab, or the effect size is unsettled.
- **WEAK** — real data whose design cannot support the claim made from it: uncontrolled, no comparison arm, retrospective, or grey literature.
- **FOLKLORE** — widely repeated in baseball, unsupported or actively contradicted.
- **UNSOURCED** — no traceable source, or the claim is a misreading of a real source. Entries at this grade exist so that a future search surfaces the debunking rather than the myth.

**CAUSALITY is the most important field. It says whether anyone actually moved the variable.**

- **INTERVENTION** — someone changed it and measured the result. It worked.
- **MANIPULATED_NULL** — someone changed it and measured the result. It did **not** work. The strongest evidence in this file and the most ignored.
- **CROSS_SECTIONAL** — observed association only. Nobody has moved it. Direction unknown.
- **MECHANISM** — basic mechanics, cadaveric, physics, or instrument behaviour. Not a training claim.

> ### THE ONE RULE
> **`CAUSALITY: CROSS_SECTIONAL` must never be phrased as a coaching instruction.**
> A cross-sectional finding describes how hard throwers are built. It does not license telling an athlete to move the variable. Stride length is the worked example: it correlates with velocity across 315 professionals and has been experimentally moved twice by independent groups, with no gain and one loss (F-043, F-044, F-045). Six corrections were applied to this corpus on 2026-08-13 and **every one moved the same direction — toward more confidence than the source supported.** Compressing a study into an instruction is inherently a confidence-increasing operation, so the guard lives in this field, not in the reader.

**Three questions that caught every correction this corpus has ever made:**
1. What was the sample's ACTUAL velocity? ("Collegiate" has meant 78 mph.)
2. Was there a control group, and did anyone actually manipulate the variable? **Never infer a design from a p-value.**
3. Does the number measure what the sentence says it measures? Verifying a citation is not verifying a claim.

**Standing methodological facts that bound everything below:** lab velocity is ~5-8 mph below game velocity (F-208); torque is not comparable across labs (F-091, F-203); ~60% of normalized elbow torque variance is unexplained by kinematics (F-100); every "professional norms" table is survivorship-selected (F-244).

---

# 1 — VELOCITY: PHYSICAL QUALITIES AND TRAINING TRANSFER

### F-001 | Body mass is the strongest single physical correlate of fastball velocity
TOPIC: velocity, body mass, anthropometry, strength training, lean mass, physical testing
CLAIM: Body mass correlates with fastball velocity more strongly than any trainable strength or power test in collegiate pitchers.
NUMBERS: r = 0.58, p = .0004; n = 33 NCAA D1 pitchers (~34% of variance)
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: King BW, Snow TK, Millard-Stafford M (2025), J Strength Cond Res, PMID 39446825
COACHING: Do not promise mph for weight gain. State it as the strongest correlate in the literature and the one nobody has ever tested as an intervention.
CONFIDENCE: high for the association, zero for causation — no mass-gain intervention with a velocity outcome exists in pitchers
SEE ALSO: F-002, F-003, F-004, F-055

### F-002 | Lean mass correlates with velocity nearly as strongly as total mass
TOPIC: velocity, lean mass, body composition, hypertrophy, strength training
CLAIM: Lean mass correlates with fastball velocity in D1 pitchers.
NUMBERS: r = 0.52, p = .002; n = 33 NCAA D1 (~27% of variance)
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: King BW et al. (2025), JSCR, PMID 39446825
COACHING: "Your mass is part of the machine, not a penalty you carry." Never state a mph figure per pound of lean mass — none exists.
CONFIDENCE: high for the association; the causal question is Open Question 3 in the velocity file
SEE ALSO: F-001, F-004, F-055

### F-003 | CMJ concentric impulse is the strongest jump-test correlate of velocity
TOPIC: velocity, countermovement jump, impulse, force plate, absolute power, momentum
CLAIM: Absolute CMJ concentric impulse and absolute CMJ peak power correlate with fastball velocity; pelvis and trunk pitching kinematics do not correlate with any CMJ variable.
NUMBERS: concentric impulse r = 0.71; peak power r = 0.68; impulse vs A-P linear momentum during pitching r = 0.68; lean/body mass vs pitching linear momenta r = 0.71-0.83; pelvis/trunk kinematics vs CMJ |r| < 0.45; n = 19 NCAA D1
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Sakurai M, Qiao M, Szymanski DJ, Crotin RL (2024), JSCR 38(7):1288-1294, PMID 38900174
COACHING: Test and train ABSOLUTE impulse. Never per-kilogram, never jump height.
CONFIDENCE: medium — n = 19; the highest CMJ-velocity correlations in the literature, unreplicated at that magnitude
SEE ALSO: F-004, F-005, F-006, F-007

### F-004 | NULL — Jump height does not predict pitch velocity
TOPIC: velocity, jump height, vertical jump, null, refuted, force plate, testing
CLAIM: Bilateral vertical jump height has no significant relationship with fastball velocity.
NUMBERS: r = 0.07, NS; n = 33 NCAA D1. Sparta Score r = -0.06 NS in the same sample.
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: King BW et al. (2025), JSCR, PMID 39446825
COACHING: An athlete who added two inches to his vertical moved a variable with r = 0.07. Say that. Jump height is a mass-normalized quantity in disguise — height is set by takeoff velocity, not momentum.
CONFIDENCE: high — a clean null, and it resolves the apparent conflict in the jump-testing literature
SEE ALSO: F-003, F-005, F-006

### F-005 | NULL — Power expressed per kilogram of body mass does not predict velocity
TOPIC: velocity, relative power, per-kilogram, normalization, null, refuted, force plate
CLAIM: CMJ power relative to body mass shows no significant relationship with fastball velocity, while the same sample's absolute power does.
NUMBERS: relative power r = 0.19 NS vs absolute CMJ peak power r = 0.43 (p = .014) and Wingate absolute peak power r = 0.44 (p = .011); n = 33 D1
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: King BW et al. (2025), JSCR, PMID 39446825
COACHING: Dividing power by body mass deletes the term carrying the signal. Momentum is mass x velocity.
CONFIDENCE: high — the authors' own stated conclusion
SEE ALSO: F-001, F-003, F-004

### F-006 | Reactive strength is the only jump quality that survives into a professional sample
TOPIC: velocity, reactive strength, RSI, drop jump, plyometrics, stiffness, professional
CLAIM: Drop-jump variables predict ball velocity in professional pitchers where countermovement and squat jump do not.
NUMBERS: drop jump -> ball velocity R2 = 0.30 (F = 3.93, p = 0.005); RSI specifically p = .002; CMJ R2 = 0.10 (p = .28 NS); squat jump R2 = 0.07 (p = .44 NS); CMJ -> spin rate R2 = 0.20 (p = .03); n = 53 professional, age 24.5 +/- 3.6
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wong R, Laudner K, Amonette W, Vazquez J, Evans D, Meister K (2023), JSCR 37(4):823-828, PMID 36026465
COACHING: Train braking and short ground contacts. The lead-leg block is a ~50-80 ms braking event, not a countermovement jump. No RSI-training intervention with a velocity outcome exists.
CONFIDENCE: medium — single sample, but mechanically coherent and in the right population
SEE ALSO: F-003, F-004, F-061

### F-007 | Absolute cycle-ergometer power replicates at r ~ 0.44 in two independent samples
TOPIC: velocity, absolute power, Wingate, cycle ergometer, anaerobic power, replication
CLAIM: Absolute 30-second cycle mean power correlates with throwing velocity in minor-league pitchers, matching an independent D1 Wingate result.
NUMBERS: 30-s cycle mean power vs peak throwing velocity r = 0.441; vs mean velocity r = 0.428; n = 27 MiLB. Independent D1 Wingate absolute peak power r = 0.44, n = 33.
POPULATION: MiLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Donahue PT, Beiser E, Wilson SJ, Hill CM, Garner JC (2018), J Trainology 7(2):24-27; King BW et al. (2025)
COACHING: The quality is absolute power output, not any particular jump. CMJ measures were NOT the significant predictors in the MiLB sample.
CONFIDENCE: medium — two independent samples converging on the same coefficient is one of the better-replicated findings in this space
SEE ALSO: F-003, F-005

### F-008 | Stride-leg unilateral jump outperforms bilateral, and pitcher asymmetry is normal
TOPIC: velocity, unilateral, asymmetry, single-leg jump, stride leg, drive leg, testing
CLAIM: Stride-leg unilateral CMJ height is the strongest single association with fastball velocity in its sample, and pitchers jump significantly higher on the stride leg than the drive leg.
NUMBERS: stride-leg unilateral CMJ height vs FB velocity r >= 0.65, p < .01; stride > drive leg p < .01, eta2 = 0.34; bilateral CMJ exceeded summed single-leg by 27%; n = 19 D1
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Lis R, Szymanski DJ, Qiao M, Crotin RL (2023), JSCR 37(9):1852-1859, PMID 37389938
COACHING: Do NOT coach unilateral asymmetry toward zero in pitchers. The asymmetry is directional and normal.
CONFIDENCE: medium — n = 19
SEE ALSO: F-003, F-009

### F-009 | Frontal-plane unilateral power (lateral-to-medial jump) is the most overlooked field test
TOPIC: velocity, lateral bound, frontal plane, field test, med-ball, broad jump
CLAIM: Across a battery of med-ball throws, vertical jumps and broad jumps, the lateral-to-medial jump was the only test correlating with throwing velocity across all four throwing conditions and in both RH and LH throwers.
NUMBERS: n = 42 college players; reported multiple-R up to 0.982 for the LH subgroup is overfit and must not be quoted
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Lehman G, Drinkwater EJ, Behm DG (2013), JSCR 27(4):902-908, PMID 22706576
COACHING: Include a lateral bound in the testing battery. Note the outcome was shuffle/stretch throw velocity, NOT mound pitch velocity.
CONFIDENCE: low-medium — off-outcome, overfit subgroup statistics; corroborated only informally by Howell/Cressey 2021
SEE ALSO: F-008, F-061

### F-010 | Height carries 81% of variable importance in the largest in-game velocity model
TOPIC: velocity, height, anthropometry, ceiling, in-game, markerless, non-modifiable
CLAIM: With 322 D1 pitchers and complete in-game biomechanics available, a single non-modifiable anthropometric variable carried the overwhelming majority of the model's variable importance, and total explained variance was still under a third.
NUMBERS: R2 = 0.29, RMSE = 2.70 mph; height 81.2% of variable importance; body mass 2.47%; cross-conference generalization SEC->ACC RMSE 3.04 mph, ACC->SEC 2.55 mph; n = 322 NCAA D1, in-game markerless, 2022-2024, Super Learner ensemble
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fernandez G, Bullock G, Zappa R, Oliver G, Nicholson K (2026), Sports Biomechanics, PMID 42253247
COACHING: A 6'6" pitcher and a 5'11" pitcher do not have the same ceiling and no program closes that gap. The authors argue AGAINST universal mechanics models.
CONFIDENCE: high — largest in-band sample with full mechanics; the 2.70 mph error bar is larger than a realistic annual gain
SEE ALSO: F-011, F-055, F-073, F-079

### F-011 | Leg length is retained as a velocity predictor at both high-school and professional level
TOPIC: velocity, leg length, anthropometry, levers, ceiling, non-modifiable
CLAIM: Leg length is the only anthropometric variable retained in both the HS and professional kinematic velocity models, and its coefficient roughly halves in professionals.
NUMBERS: professional beta = 0.292, p < .001; +12.7 cm ~ +1.74 m/s ~ +3.9 mph; unstandardized B = 26.406 (HS, n = 59) vs 13.706 (pro, n = 337, 3,627 fastballs)
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE, Dowling B, Wang Z, et al. (2024), OJSM 12(8), PMID 39143985 / PMC11322935
COACHING: Anthropometric leverage compresses through the selection funnel but does not disappear. Not recoverable by training.
CONFIDENCE: medium-high — large professional sample, replicated direction
SEE ALSO: F-010, F-055, F-079

### F-012 | Sprint ratio and height survive in an adult tryout velocity model
TOPIC: velocity, sprint, acceleration, height, tryout, regression, field test
CLAIM: In an adult tryout population, stepwise regression retained height, loaded/unloaded CMJ ratio, and 10 m / 30 m sprint ratio as velocity predictors.
NUMBERS: height t = 2.79 (p = .007); CMJ ratio t = 2.35 (p = .022); sprint ratio t = 2.98 (p = .004); adjusted R2 = 0.230, model p = .0003; n = 64 adults at professional tryout, age 23.9 +/- 2.8, 180.3 +/- 5.9 cm, 81.4 +/- 10.9 kg; back-solved sample mean ~128 km/h ~ 79.5 mph
POPULATION: unspecified (adult amateur tryout — BELOW the 85 mph floor)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Huang JH, Chen SH, Chiu CH (2022), PLoS One 17(3):e0265525, PMC8929570
COACHING: Directionally suggestive only — the sample throws ~79.5 mph. There is NO intervention study showing sprint training raises pitch velocity in pitchers.
CONFIDENCE: low-medium — sample mismatch; third independent confirmation of height as a predictor
SEE ALSO: F-010, F-038

### F-013 | NULL — Grip strength does not predict velocity in the best population-matched sample available
TOPIC: velocity, grip strength, forearm, null, refuted, hand strength
CLAIM: No significant univariate association exists between any grip-strength variable and ball velocity in D1 pitchers averaging almost exactly the 85 mph floor.
NUMBERS: n = 87 NCAA D1 pitchers, mean age 19.6, mean ball velocity 37.87 m/s = 84.83 mph; all grip variables non-significant
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Barrack AJ et al. (2024), OJSM 12(11), PMID 39600416 / PMC11590131
COACHING: Stop selling grip work as velocity work. Grip still matters mechanistically for medial-elbow stress shielding — that is a load-sharing argument, not a velocity argument.
CONFIDENCE: high — closest sample-to-target match of any cross-sectional study in the corpus
SEE ALSO: F-014, F-114, F-218

### F-014 | Shoulder rotational strength explains ~12% of velocity; rate of force development explains nothing
TOPIC: velocity, shoulder strength, internal rotation, external rotation, RFD, rate of force development, null
CLAIM: Isometric shoulder IR and ER maximum force show a small but real association with throwing velocity; RFD and arm length contributed nothing to the regression models.
NUMBERS: IR and ER Fmax vs throwing velocity R2 = 0.12-0.13; RFD and arm length contributed nothing; n = 26 HS + collegiate
POPULATION: NCAA_D1 (mixed HS + collegiate)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Job TDW, Cross MR, Cronin JB (2024), J Biomech 176:112339, PMID 39326246
COACHING: Note the direction — max force beat RFD, the opposite of the usual assumption. Do not sell RFD training as velocity work.
CONFIDENCE: medium — small sample, mixed level
SEE ALSO: F-013, F-016, F-022

### F-015 | NULL — Trunk rotation mobility and upper-quarter dynamic stability do not predict velocity
TOPIC: velocity, mobility, movement screen, trunk rotation, Y-balance, null, refuted
CLAIM: Throwing-side trunk rotation ROM and Upper Quarter Y-Balance show no relationship with fastball velocity in D1 pitchers.
NUMBERS: trunk rotation vs FB velocity r = 0.131, p = .491; Y-Balance no correlation; n = 30 NCAA D1
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Bullock GS, Schmitt AC, Chasse PM, Little BA, Diehl LH, Butler RJ (2018), JSCR 32(1):261-266, PMID 28225709
COACHING: A clean published null against the movement-screen-drives-velocity claim. Authors' conclusion: "increased upper extremity stability and trunk mobility are not directly related to fastball velocity."
CONFIDENCE: high
SEE ALSO: F-014, F-016

### F-016 | NULL — Trunk muscle endurance does not relate to trunk lean or pitch speed
TOPIC: velocity, core endurance, trunk endurance, flexibility, balance, null, refuted, core training
CLAIM: No significant relationship exists between trunk muscle endurance, flexibility, or stride-foot balance and contralateral trunk lean in collegiate pitchers; lean itself did not predict pitch speed.
NUMBERS: lean vs pitch speed B = -0.631, p = 0.175; collegiate pitchers (n not recorded in corpus)
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Myrick KM, Pallone AS, Feinn RS, Ford KM, Garbalosa JC (2019), JSCR 33(10):2641-2647, PMID 31361734
COACHING: A clean null for core ENDURANCE. Kept because nulls stop programs being built on nothing. Note this is endurance, not rotational power — see F-034.
CONFIDENCE: medium — sample size not recorded
SEE ALSO: F-034, F-015

### F-017 | Rotational medicine-ball throw velocity correlates with pitch velocity — in D3 pitchers
TOPIC: velocity, medicine ball, rotational power, monitoring, sample mismatch
CLAIM: Rotational med-ball throw velocity correlates with pitching velocity in a Division III sample.
NUMBERS: r = 0.62, p = .02, R2 = 0.38; n = 15 NCAA D3 pitchers; 95% CI on that r ~ 0.16-0.86
POPULATION: off_population_HS (D3, typically low-80s — below the floor)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Taniyama D et al. (2021), JSCR, PMID 34570055
COACHING: Reasonable as a cheap MONITORING metric. Not evidence that med-ball training raises pitch velocity — see F-034 for the one controlled trial and F-230 for the commercial and grey-literature claims that get miscited here.
CONFIDENCE: low — n = 15, sample below floor, enormous confidence interval
SEE ALSO: F-034, F-230

### F-018 | Force-plate batteries predict velocity at R2 = 0.54 with +/-2.7 mph error
TOPIC: velocity, force plate, prediction, testing, squat jump, IMTP, RSI, industry data
CLAIM: A commercial force-plate model predicts pitch velocity with a mean absolute error larger than a realistic annual velocity gain, weighting absolute power and reactive strength.
NUMBERS: R2 = 0.54, MAE +/-2.7 mph; weights in order — squat jump peak power (absolute watts), CMJ RSI-modified, 10-to-5 hop RSI, IMTP net peak force; n and level NOT disclosed; explicitly no limb-length and no upper-body input
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball (2021), "Predicted Velocity Through Jump and Strength Testing"
COACHING: NEVER validate a strength block against a predicted velocity — the error bar exceeds the effect. Validate the strength block against the strength quality. Note the convergence: absolute power and reactive strength, the same two families that survived peer review.
CONFIDENCE: medium for direction, low for the number — vendor-published, sample undisclosed
SEE ALSO: F-003, F-006, F-079, F-085

### F-019 | Jump testing may predict velocity CONSISTENCY rather than velocity magnitude
TOPIC: velocity, consistency, variance, CMJ, RSI-modified, longitudinal, monitoring
CLAIM: Across a season, no CMJ metric predicted mean velocity, but jump height predicted lower velocity variance and RSI-modified predicted higher variance.
NUMBERS: jump height -> velocity variance gamma = -0.060, p = .001; RSI-modified -> variance gamma = 3.800, p < .001; n = 8 collegiate pitchers, weekly across 15 weeks / 53 games
POPULATION: NCAA_D1
EVIDENCE: WEAK
CAUSALITY: CROSS_SECTIONAL
SOURCE: Burke AA et al. (2026), JSCR ahead of print, PMID 42423608
COACHING: Hypothesis-generating only. But it reframes the jump-test nulls: these tests may be answering a stability question, not a ceiling question.
CONFIDENCE: low — n = 8
SEE ALSO: F-004, F-006, F-186

### F-020 | A scoping review of 34 studies found only three physical qualities associated with pitching performance
TOPIC: velocity, review, physical qualities, body weight, age, jumping
CLAIM: A scoping review identified body weight, age, and jumping-test performance as the complete list of physical qualities associated with pitching performance.
NUMBERS: 34 cross-sectional studies reviewed
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Mercier MA, Tremblay M, Daneau C, Descarreaux M (2020), BMJ Open Sport Exerc Med 6(1):e000704, PMID 32153984
COACHING: The list is short and two of the three are not trainable. Say so before selling a testing battery.
CONFIDENCE: medium — mixed-level pooling
SEE ALSO: F-001, F-004, F-010

### F-021 | GAP — No verified IMTP-versus-velocity study exists in college or professional pitchers
TOPIC: velocity, IMTP, isometric mid-thigh pull, gap, missing evidence, testing
CLAIM: IMTP appears in this literature only inside an undisclosed commercial model. Anyone quoting an IMTP-to-velocity correlation is quoting something unpublished.
NUMBERS: zero studies
POPULATION: unspecified
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 2.5 (documented absence, not a study)
COACHING: Use IMTP net peak force as a strength-quality readout, never as a velocity predictor with a published coefficient.
CONFIDENCE: high that the gap exists — it was searched for and not found
SEE ALSO: F-018

### F-022 | Upper-body strength adds little, or the measurement gap is real — both readings live
TOPIC: velocity, upper body strength, gap, force plate, model, arm strength
CLAIM: A force-plate velocity model reaches R2 = 0.54 with explicitly no upper-body input; two peer-reviewed nulls tilt toward "adds little" rather than "unmeasured."
NUMBERS: R2 = 0.54 with zero upper-body input; shoulder rotational strength R2 = 0.12-0.13 (F-014); grip null (F-013)
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline (2021); Job 2024; Barrack 2024
COACHING: Do not build a velocity program around arm strength. See F-064 and F-067 — the arm is the last and least powerful link.
CONFIDENCE: medium — the alternative reading (genuine measurement gap) has not been excluded
SEE ALSO: F-013, F-014, F-064, F-067

---

# 2 — VELOCITY: INTERVENTIONS (what happened when someone actually trained it)

### F-023 | The structural fact — the controlled training literature at 85+ is nearly empty
TOPIC: velocity, intervention, evidence gap, controlled trial, 85 mph floor, structural
CLAIM: Controlled trials at or above 85 mph baseline are rare, non-randomized and largely grey literature, and there is still no published controlled trial in PROFESSIONAL pitchers with velocity as an outcome.
NUMBERS: exactly two controlled samples clear the 85 mph floor — Ake 2016 (n = 56, 87.25/86.80 mph, null) and Lee/Choi/Jeon 2026 (n = 29, max 86.2/85.9 mph, positive)
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: INTERVENTION
SOURCE: velocity-development.md 1, corrected 2026-08-13
COACHING: The honest prior for a mature 85+ arm is 2-3% — roughly 1.5-2.5 mph per well-executed year — with a meaningful probability of zero. The earlier absolutism "there is not a single published controlled study at 85+, not one" was WRONG and must not be re-imported.
CONFIDENCE: high — this is the corrected version; the professional weighted-ball literature (Sussman, IJSPT) is observational injury work, not a training trial
SEE ALSO: F-024, F-034, F-072, F-226

### F-024 | NULL — The highest-velocity controlled sample in the literature found no weighted-implement gain
TOPIC: velocity, weighted balls, weighted implements, null, refuted, D1, SEC, intervention
CLAIM: A weighted-implement block in NCAA D1 SEC pitchers produced no significant velocity change and no between-group difference.
NUMBERS: n = 56 (35 weighted implement, 21 normal throwing); baseline 87.25 +/- 2.32 mph (WI) vs 86.80 +/- 1.32 mph (control); within-group p = 0.071; between-group p = 0.271; 4/5/6 oz implements, off-season
POPULATION: NCAA_D1
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Ake H, Haynes H, Galloway R, Donahue P, Garner JC (2016), Univ. of Mississippi M.S. thesis + IJES Conference Proceedings, eGrove etd/559
COACHING: The highest-velocity controlled sample that exists, and it is null. Retrospective, non-randomized, self-selected groups, never peer-reviewed as a full paper — so it cannot rule out a small true effect either.
CONFIDENCE: medium — weak design in both directions. The corpus previously recorded this baseline as "not reported," which was wrong.
SEE ALSO: F-023, F-027, F-029

### F-025 | Weighted-implement effect size shrinks toward zero as baseline velocity rises
TOPIC: velocity, weighted balls, gradient, ceiling, effect size, transfer, novice, experienced
CLAIM: The published velocity-training effect declines monotonically with baseline velocity, confirmed independently outside baseball.
NUMBERS: ~67 mph HS +2.2 mph (randomized control) -> ages 10-17 underload +4.8 mph (uncontrolled) -> NCAA D1 null -> collegiate/pro null. Overarm-throwing systematic review (17 studies): underweighted-implement gains 11-12% in novices vs 2-3% in experienced athletes.
POPULATION: mixed
EVIDENCE: ESTABLISHED
CAUSALITY: INTERVENTION
SOURCE: Fredriksen AB & van den Tillaar R (2024), Sports Med Open 10:122, PMID 39520628; intervention table in velocity-development.md 3.1
COACHING: "Every mph figure you have ever been quoted was measured on someone slower than your athlete." When a facility tells an 88 mph arm to expect 3-5 mph, that is extrapolated from 15-year-olds throwing 67.
CONFIDENCE: high — the gradient runs in exactly one direction and is confirmed cross-sport
SEE ALSO: F-023, F-027, F-072, F-228

### F-026 | NULL — The Driveline collegiate/professional weighted-implement study found no velocity change
TOPIC: velocity, weighted balls, Driveline, null, refuted, external rotation, ROM
CLAIM: A 6-week weighted-implement plus multimodal block in an older, higher-level sample produced no velocity change, no ER ROM change and no elbow valgus torque change.
NUMBERS: n = 17 collegiate + professional, age 19.9 +/- 1.3, baseline 35.1 +/- 1.8 m/s = 78.5 mph (submaximal lab test); 9 of 17 gained, 8 lost; ER ROM 122 +/- 21 deg -> 123 +/- 10 deg, p = .637; elbow valgus torque p = .942; NO control group
POPULATION: professional_mixed
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Marsh JA, Wagshol MI, Boddy KJ, O'Connell ME, Briend SJ, Lindley KE, Caravan A (2018), PeerJ 6:e6003, PMC6254244
COACHING: Closest sample to our population and it is null — but it is a null against nothing (no control), used marker-encumbered mocap, and post-tested at "throw as hard as comfortable." A submaximal encumbered post-test cannot resolve a 1-2 mph change.
CONFIDENCE: medium-low — underpowered and confounded (weighted implements + manual therapy + lifting + other modalities bundled)
SEE ALSO: F-027, F-024, F-234

### F-027 | The only weighted-ball RCT: +1.6 mph net in 15-year-olds, with a 24% injury rate
TOPIC: velocity, weighted balls, RCT, injury, external rotation, high school, stress cost
CLAIM: A 6-week weighted-baseball program raised velocity in high-school-aged pitchers and produced a 24% arm-injury rate versus 0% in the control arm.
NUMBERS: 38 randomized / 34 analyzed, age 15.3 +/- 1.2, baseline 66.9-69.1 mph, 2-32 oz implements, 6 weeks. EXP +2.24 mph (+3.3%), p < .001; CONTROL +0.67 mph NS -> net ~ +1.6 mph. Responder split 80% gained / 8% unchanged / 12% decreased; 67% of controls also gained. ER PROM +3.3 deg (reported elsewhere as ~8 deg at 16-32 oz). Injuries 24% vs 0% — 2 olecranon stress fractures, 1 partial UCL, 1 UCL reconstruction, concentrated the FOLLOWING season, associated with the 16-32 oz work.
POPULATION: off_population_HS
EVIDENCE: ESTABLISHED (best design in the literature, wrong population)
CAUSALITY: INTERVENTION
SOURCE: Reinold MM, Macrina LC, Fleisig GS, Aune K, Andrews JR (2018), Sports Health 10(4):327-333, PMID 29882722
COACHING: The famous positive result is +1.6 mph NET in 15-year-olds throwing 67. The ER "gain" is best read as acquired laxity, not improved mobility. Title is frequently mis-cited as "...Strength..." — the published title says "Pitching Arm Biomechanics."
CONFIDENCE: high for the study, low for transfer to an 85+ arm
SEE ALSO: F-024, F-026, F-234, F-030

### F-028 | Uncontrolled underload work in 10-17 year-olds produced +4.8 mph
TOPIC: velocity, underload, weighted balls, youth, uncontrolled, maturation
CLAIM: A 15-week underload-only program in adolescents produced a large velocity gain with no control group.
NUMBERS: n = 44, ages 10-17 (14.7 +/- 1.8), 3-4 oz underload, 15 weeks, no control; +4.8 mph (95% CI 4.0-5.6), p < .001; 98% improved
POPULATION: off_population_youth
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Erickson BJ, Atlee TR, Chalmers PN, et al. (2020), OJSM 8(3), PMID 32258183
COACHING: Severe sample mismatch. Fifteen weeks of adolescent maturation with no control arm cannot be attributed to the implement.
CONFIDENCE: low for our population
SEE ALSO: F-029, F-025

### F-029 | Underload is the better-evidenced implement direction than overload
TOPIC: velocity, underload, overload, weighted balls, arm speed, implement, 3-7 oz
CLAIM: Four independent lines converge on underload (3-4.4 oz), not overload, as the better-supported implement lever, and heavy implements measurably slow the arm.
NUMBERS: Yang 2013 underload-only controlled +2.1 mph significant, control NS, n = 24 adolescent. DeRenne 1990 underload +4.72 vs overload +3.75 mph, n = 30 HS. Erickson 2020 underload-only +4.8 mph uncontrolled. Fleisig 2017 (n = 25 HS/collegiate): with a 4 oz ball arm and trunk velocities MATCH standard pitching, and "arm and trunk velocities steadily decreased as ball weight increased from 5 to 32 oz." Also DeRenne 1994, n = 225 HS + university, 4 or 6 oz, 10 wk, controlled, ~+5 mph (extracted second-hand; primary text not obtained).
POPULATION: mixed, mostly off_population
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Yang W-W et al. (2013) PMID 23603999; DeRenne C et al. (1990, 1994); Erickson 2020; Fleisig GS et al. (2017), Sports Health 9(3):210-215, PMID 27872403
COACHING: If using implements for arm speed in a mature arm, the 3-7 oz window is where mechanism and outcome both point. Heavy implements decelerate the arm — a measured fact — so any velocity mechanism they carry must be indirect and delayed.
CONFIDENCE: medium — best-supported implement claim; all positives are off-population
SEE ALSO: F-030, F-028, F-234

### F-030 | Ball weight 3-7 oz changes arm speed without changing measured arm kinetics — concentric phase only
TOPIC: velocity, weighted balls, kinetics, arm speed, elbow torque, deceleration, implement
CLAIM: Across 3-7 oz, ball weight significantly affected pitch velocity and arm speed while none of the measured arm joint kinetics changed.
NUMBERS: n = 26 collegiate/professional pitchers, five ball weights 85-198 g, single acute session
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION (acute)
SOURCE: O'Connell ME, Lindley KE, Scheffey JO, Caravan A, Marsh JA, Brady AC (2022), J Appl Biomech, PMID 35981710
COACHING: This measured the CONCENTRIC ACCELERATION PHASE ONLY. The Reinold injury signal was olecranon stress fractures and UCL tears — cumulative and deceleration-phase events an acute concentric study cannot speak to. The paper also does not specify plyoball vs hard leather. "Weighted balls don't increase arm stress" as it propagates is a half-truth.
CONFIDENCE: medium for what was measured, low for what it is used to claim
SEE ALSO: F-027, F-029, F-234, F-098

### F-031 | Heavier and larger balls DECREASE elbow varus torque
TOPIC: velocity, implement, ball weight, torque reduction, constraint, drill
CLAIM: Increases in ball weight and size decrease elbow varus torque during pitching.
NUMBERS: effect sizes not recorded in the corpus
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION (acute)
SOURCE: Fleisig GS et al. (2025), ASMI; repeated as a formal proposal in Fleisig (2026), Sports Biomech
COACHING: Usable as a bullpen CONSTRAINT with a published torque reduction. Irrelevant as a rule change — no governing body is changing the ball.
CONFIDENCE: medium
SEE ALSO: F-029, F-030, F-182

### F-032 | Reframe — pitch speed, not ball weight, may drive the joint-stress difference
TOPIC: weighted balls, ball weight, joint stress, elbow varus, covariate, youth
CLAIM: After mass correction, lighter balls produced HIGHER joint moments than 5 oz, but the difference largely disappeared once pitch speed was entered as a covariate.
NUMBERS: n = 30 youth, age 13.3 +/- 0.7 yr, 57.0 +/- 12.3 kg. Mass-corrected elbow varus: 4 oz vs 5 oz +3.0 N-m (p = .006, g = 0.53); 6 oz vs 5 oz -5.4 N-m (p < .001, g = 1.06). With pitch speed as covariate, 4 oz vs 5 oz falls to 1.2 N-m, ns (p = .07). SPM: 46% of the elbow cycle, 52% of the shoulder.
POPULATION: off_population_youth
EVIDENCE: WEAK
CAUSALITY: INTERVENTION (acute)
SOURCE: Boddy K, Cochrane A, Marsh J, Pouch G, Morgan D (2026), SportRxiv preprint 821
COACHING: The "heavy balls are safer / light balls are dangerous" debate may be a velocity-management question wearing an implement costume. Thirteen-year-olds, n = 30, authored by the founder of the company selling the implements.
CONFIDENCE: low for our population — promising as a reframe only
SEE ALSO: F-030, F-029

### F-033 | INTERVENTION POSITIVE — 8 weeks of lumbopelvic-hip strength training raised ball speed, and raised elbow varus moment
TOPIC: velocity, intervention, lumbopelvic, hip, trunk, strength training, controlled trial, stress cost
CLAIM: A controlled 8-week lumbopelvic-hip strength block significantly increased ball speed in high-school pitchers and also significantly increased elbow varus moment.
NUMBERS: n = 54, age 15.6 +/- 1.5, 8 weeks, controlled. Ball speed t45 = 2.37, p = .014. Elbow varus moment t45 = 2.06, p = .046.
POPULATION: off_population_HS
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Oyama S, Palmer T, Laudner K (2026), J Athl Train 61(6):408-415, PMID 42245140
COACHING: One of only two controlled non-implement studies with a positive velocity outcome. Velocity is not free — the authors explicitly recommend reducing pitch counts as ball speed rises.
CONFIDENCE: medium — HS sample, directional for our population; converges with F-034 on the same anatomical target
SEE ALSO: F-034, F-065, F-066

### F-034 | INTERVENTION POSITIVE — the first positive controlled velocity result above the 85 mph floor
TOPIC: velocity, core training, rotational power, medicine ball, intervention, controlled trial, collegiate, core-coiling
CLAIM: A 12-week rotational medicine-ball and tubing program raised peak and average velocity versus a machine-based general-strength comparator in collegiate pitchers whose baseline MAX velocity clears 85 mph.
NUMBERS: n = 15 CCT vs 14 comparator, age 20.13 +/- 0.63 / 20.07 +/- 0.61, Korean collegiate. Baseline MAX 138.66 +/- 4.30 km/h = 86.2 mph vs 138.21 +/- 4.35 km/h = 85.9 mph. Baseline AVERAGE 135.20 +/- 4.31 = 84.0 mph vs 134.35 +/- 3.87 = 83.5 mph (below floor). Max velocity p = .003 (comparator NS p = .547); average p = .011 (comparator NS p = .165); between-group ANCOVA p = .014 max / p = .042 avg; agility p = .002. CONTROL/ACCURACY: no improvement in either group. Protocol: 70-min sessions (10 warm-up / 50 main / 10 cool-down), 4x/week x 12 weeks, 60% 1RM wk 1-4 -> 65% wk 5-8 -> 70% wk 9-12. Eight exercises: Tubing Torso Rotation, One-Side Torso Rotation, One-Leg Torso Rotation, Medicine Ball Side Throw, Medicine Ball Side Catch, Jump and Wall Ball Side Throw, Side Jumping and Wall Ball Throw, Walking Lunge and Twist. Comparator: chest press, pull-down, shoulder press, arm curl/triceps extension, squat, leg press, leg extension, leg curl.
POPULATION: NCAA_D1 (Korean collegiate equivalent)
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Lee CM, Choi W, Jeon BH (2026), Asian J Kinesiology 28(1):19, DOI 10.15758/ajk.2026.28.1.19
COACHING: Cite as "one non-randomized 12-week trial, active comparator, collegiate, positive on peak velocity." NEVER as "core training adds velocity." Say out loud that command did not improve — rotational-power marketing implies it will.
CONFIDENCE: medium-low — not randomized; the comparator trained neither rotational power nor explosive lower body, so the finding is "explosive rotational work beats bodybuilding machines," not "the trunk is special." Clears the floor on peak velocity only. n = 29, one squad, low-profile regional journal, not PubMed-indexed at review.
SEE ALSO: F-033, F-065, F-066, F-017, F-208

### F-035 | NULL — Wearable resistance above the elbow did not change throwing velocity
TOPIC: velocity, wearable resistance, intervention, null, refuted, arm speed
CLAIM: Six weeks of wearable resistance above the elbow produced no significant difference in throwing velocity or arm speed.
NUMBERS: n = 17 collegiate, 6 weeks, quasi-control
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: MANIPULATED_NULL
SOURCE: Job TDW 3rd, Cross MR, Cronin JB (2025), Int J Sports Physiol Perform, PMID 40537114
COACHING: A designed null in a collegiate sample. Do not sell wearable resistance as velocity work.
CONFIDENCE: medium — quasi-control, small n
SEE ALSO: F-023

### F-036 | A D1 control group LOST rotator-cuff strength across 8 normal offseason weeks
TOPIC: strength, offseason, detraining, rotator cuff, BFR, blood flow restriction, maintenance
CLAIM: In a randomized BFR trial, the BFR arm gained shoulder lean mass while the control group doing its normal program lost flexion and IR strength across the offseason.
NUMBERS: n = 28 NCAA D-IA, 8 weeks, RCT. BFR +227 g shoulder lean mass vs +75 g. Pitch velocity NOT measured.
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Lambert BS, Hedt C, Ankersen JP, et al. (2023), JSES, PMID 36933646
COACHING: Maintenance is not the default state. The better-designed of the two studies supporting continued lifting — its weakness is that the outcome is cuff strength, not velocity.
CONFIDENCE: medium — real control arm, off-outcome for velocity
SEE ALSO: F-039, F-163

### F-037 | Three different 6-week programs all raised velocity in HS pitchers and none beat the others
TOPIC: velocity, intervention, Throwers Ten, plyometrics, Keiser, controlled trial, modality
CLAIM: In a controlled four-arm design, Throwers Ten, Keiser pneumatic resistance and plyometric training each produced small significant velocity gains and none was superior; the control did not change.
NUMBERS: n = 68, ages 14-17, 6 weeks, 4 arms. Throwers Ten +1.7%, Keiser +1.2%, plyometric +2.0% (all p < .05); control unchanged.
POPULATION: off_population_HS
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Escamilla RF, Ionno M, deMahy MS, et al. (2012), JSCR 26(7):1767-81, PMID 22549085
COACHING: At a developing level the specific modality appears to matter less than doing something structured. Whether that generalizes to a mature arm is exactly what is untested.
CONFIDENCE: medium for HS, unknown for 85+
SEE ALSO: F-023, F-025

### F-038 | GAP — no evidence base exists for plyo-ball protocols, constraint drills, long toss, sprint training, olympic lifts, or VBT as velocity interventions
TOPIC: velocity, gap, untested, long toss, plyo balls, constraint drills, VBT, olympic lifts, sprint, periodization
CLAIM: None of these has a published intervention study with a pitch-velocity outcome in ANY baseball population.
NUMBERS: zero studies
POPULATION: unspecified
EVIDENCE: FOLKLORE (as evidenced practice)
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 3.4 and 7 "Genuinely unknown"
COACHING: They may work. There is no evidence either way. Say so out loud. Also untested: block vs undulating vs concurrent periodization, detraining/retraining timelines, transfer lag, mechanics-coaching interventions with a velocity outcome at 85+.
CONFIDENCE: high that the gap exists
SEE ALSO: F-039, F-084, F-217

### F-039 | WEAK — the "removing strength training costs velocity" study is an uncontrolled pre-post
TOPIC: velocity, detraining, resistance training, removal, uncontrolled, design error, correction
CLAIM: Twelve D1 pitchers threw significantly slower after eight off-season weeks of LIMITED resistance-equipment access. There was no control group, no assignment, and no comparison.
NUMBERS: n = 12 NCAA D1, 8 weeks; ball velocity decreased p < 0.001; peak arm slot angle, peak arm velocity and peak elbow varus torque all unchanged (p > .05); mph magnitude is PAYWALLED and was never obtained
POPULATION: NCAA_D1
EVIDENCE: WEAK
CAUSALITY: CROSS_SECTIONAL
SOURCE: Gdovin JR, Hogan B, Williams CC (2025), JSCR 39(3):347-351, PMID 39495235
COACHING: CORRECTED 2026-08-13. This corpus previously called it a "removal experiment" / "natural-experiment removal design" and made it the #1 highest-confidence recommendation. DO NOT RE-IMPORT "REMOVAL DESIGN." A pre-post with no control cannot separate detraining from season phase, throwing volume, fatigue or measurement drift — and league velocity normally RISES across a season (F-082). The athlete still lifts; the warrant is the correlational case (F-001, F-002, F-003, F-006), not this study.
CONFIDENCE: low — correct PMID, correct n, correct p-value, attached to a design that does not exist
SEE ALSO: F-001, F-036, F-082, F-226, F-240

### F-040 | Do not carry the periodized-training meta-analytic effect size forward
TOPIC: velocity, meta-analysis, periodization, publication bias, overhead athlete
CLAIM: A pooled meta-analysis of 13 RCTs across baseball, tennis and softball reported an implausibly large periodized-training effect.
NUMBERS: periodized training g = 3.445 (95% CI 1.976-4.914); 6 of the 13 studies had confidence intervals crossing zero
POPULATION: unspecified
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Myers NL, Sciascia AD, Westgate PM, Kibler WB, Uhl TL (2015), JSCR 29(10):2964-2979, PMID 25763521
COACHING: A Hedges' g of 3.4 is not a plausible training effect — it is a small-study-bias artifact. Do not carry that number forward.
CONFIDENCE: high that the number is unusable
SEE ALSO: F-025, F-041

### F-041 | A temperate review: 8 of 12 comparative studies favored resistance training on throwing velocity
TOPIC: velocity, resistance training, systematic review, throwing
CLAIM: Of 16 studies reviewed, the 12 with comparative statistics favored the experimental group on throwing velocity in 8 cases; no pooled estimate was produced.
NUMBERS: 16 studies, all ages; 8/12 favored experimental
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Zhang H, Jiang Q, Li A (2023), Heliyon 9(12):e22797, PMID 38125451
COACHING: Mixed ages, no pooled effect, minimal injury data. Directional support only.
CONFIDENCE: low-medium
SEE ALSO: F-040, F-025

### F-042 | Concurrent endurance and power training appear incompatible — on one fragile baseball study
TOPIC: concurrent training, endurance, aerobic, interference, power, conditioning, running, poles
CLAIM: Across a season, a moderate-to-high-intensity endurance group lost lower-body power while a speed/speed-endurance group gained it.
NUMBERS: n = 16 NCAA D1 baseball players (POSITION PLAYERS, not pitchers). Endurance group -39.50 +/- 128.03 W; speed group +210.63 +/- 168.96 W; between-group p < .05. No velocity outcome.
POPULATION: NCAA_D1
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Rhea MR, Oliverson JR, Marshall G, Peterson MD, Kenn JG, Naclerio Ayllon F (2008), JSCR 22(1):230-4, PMID 18296980
COACHING: The most-cited baseball concurrent-training result and it is fragile — the endurance group's SD is 3x its own mean change. No study exists on aerobic-training interference with throwing velocity specifically. "Running poles builds something relevant to velocity" is FOLKLORE.
CONFIDENCE: low — n = 16, position players, no velocity outcome
SEE ALSO: F-155, F-166

---

# 3 — VELOCITY: MECHANICS

### F-043 | Stride length correlates with velocity across 315 professionals — and it is CROSS-SECTIONAL
TOPIC: velocity, stride length, mechanics, marker not lever, elbow torque, professional
CLAIM: Longer stride as a percentage of body height is associated with higher ball velocity in professional pitchers, with no significant elbow varus torque difference across quartiles.
NUMBERS: mean stride 78.3 +/- 5.3 %BH; +0.9 m/s (+2.0 mph) per 10% BH increase (B = 0.089, beta = 0.25, p < .001); elbow varus torque n.s. across quartiles (p = 0.072); n = 315 professional
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE, Dowling B, et al. (2021), J Sports Sci 39(23):2658-2664, PMID 34240663
COACHING: NEVER phrase this as an instruction. Display it as a description of how hard throwers are built. The cue "get your stride out toward 80% of your height" was RETIRED 2026-08-13. First author is Manzi, not Dowling — the corpus previously mis-attributed this.
CONFIDENCE: high for the association, refuted for the causal reading — see F-044, F-045
SEE ALSO: F-044, F-045, F-046, F-047, F-048

### F-044 | MANIPULATED NULL — plus/minus 25% stride change produced equivalent ball velocity
TOPIC: stride length, manipulation, null, refuted, crossover, randomized, velocity
CLAIM: In a randomized crossover, pitchers threw at +/-25% of self-selected stride and hand and ball velocity were equivalent across conditions despite stride differing significantly.
NUMBERS: n = 19 (15 collegiate, 4 elite HS), ~73-81 mph; two 80-pitch simulated games, 72 h washout; 8-camera mocap at 240 Hz + 2 force plates + radar; stride differed p <= .001; hand and ball velocity EQUIVALENT
POPULATION: NCAA_D1 (below the 85 mph floor)
EVIDENCE: ESTABLISHED
CAUSALITY: MANIPULATED_NULL
SOURCE: Ramsey DK, Crotin RL, White S (2014), Hum Mov Sci 38:185-196, PMID 25457417
COACHING: Someone moved the variable and nothing happened. This 19-athlete Buffalo cohort is reported across at least SEVEN papers — COUNT IT ONCE (F-046).
CONFIDENCE: high for the null; acute instructed manipulation of a habituated stride, below our floor
SEE ALSO: F-043, F-045, F-046, F-048

### F-045 | MANIPULATED NULL, WORSE — lengthening the stride made pitchers SLOWER
TOPIC: stride length, manipulation, null, refuted, self-optimized, over-stride, velocity
CLAIM: An independent group instructed three stride conditions and found the pitcher's own self-selected stride significantly faster than both a shortened and a lengthened stride.
NUMBERS: n = 20 college pitchers, +/-20% instructed. Ball velocity: under-stride 32.48 +/- 1.72 m/s (72.7 mph), NORMAL 33.90 +/- 1.86 m/s (75.8 mph), over-stride 32.48 +/- 1.70 m/s (72.7 mph). Normal significantly faster than both; under vs over did not differ (p = 1.00).
POPULATION: NCAA_D1 (below the 85 mph floor)
EVIDENCE: EMERGING
CAUSALITY: MANIPULATED_NULL
SOURCE: Matsuda T, Hirano A, Umakoshi Y, Kimura A (2025), Front Sports Act Living, PMID 40264933
COACHING: This goes further than a null — deliberately lengthening stride made pitchers slower acutely. Self-selected stride appears to be self-optimized. Independent of the Buffalo cohort.
CONFIDENCE: medium-high — acute and instructed, n = 20, sub-elite velocity, but genuinely independent
SEE ALSO: F-043, F-044, F-046

### F-046 | METHODOLOGICAL — the Buffalo stride cohort is one experiment reported across seven papers
TOPIC: stride length, replication, citation hazard, one experiment many papers, Buffalo, Crotin, Ramsey
CLAIM: The 19-athlete Ramsey/Crotin cohort appears across at least seven publications. Counting it as multiple independent replications is a mistake this corpus has already made once.
NUMBERS: n = 19; PMIDs 25457417, 26707678, 23917472, 25804970, 29578381, 37109515, plus Life 15(9):1440 (2025) PMID 41010383. Canonical velocity citation PMID 25457417.
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM (citation practice)
SOURCE: open-disputes.md #13; daily/2026-08-13-coach.md 4
COACHING: Before treating multiple citations by one group as independent replication, check whether it is one dataset. The coach logged making this error himself, in the direction he was already arguing.
CONFIDENCE: high
SEE ALSO: F-044, F-240

### F-047 | The %-body-height normalization for stride length is contradicted twice, by critiques that disagree with each other
TOPIC: stride length, normalization, body height, leg length, null, contradiction, threshold
CLAIM: Two independent samples find no significant association between stride length normalized to body height and ball velocity, and propose different replacements.
NUMBERS: Solomito 2023, n = 99 collegiate — no significant association with normalized stride length; proposes 131-137% of LEG length, with stride acting indirectly through trunk and pelvic rotation at foot contact (p < .001). Yanagisawa 2020, n = 18 collegiate — ABSOLUTE stride length r = 0.55, p = .02, but as % body height r = 0.36, p = .15 NOT significant; also null vs lower-extremity length and hip-abduction width.
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Solomito MJ, Cohen AD, Garibay EJ (2023), Sports Biomech 22(11):1460-1469, PMID 32912079; Yanagisawa O, Taniguchi H (2020), J Phys Ther Sci 32(9):578-583, PMID 32982054
COACHING: You cannot prescribe a threshold in units whose validity is disputed. Do NOT treat "80% of height" as a hard threshold. Absolute thresholds are also system-specific (F-200).
CONFIDENCE: medium — two contradictions that disagree with each other is worse than either alone
SEE ALSO: F-043, F-200, F-048

### F-048 | A SHORTER stride cut heart rate 11.1 bpm at no velocity cost
TOPIC: stride length, stamina, heart rate, endurance, starter, simulated game
CLAIM: In the Buffalo crossover, the shorter stride condition reduced mean heart rate across an 80-pitch simulated game with no velocity penalty.
NUMBERS: -11.1 bpm mean heart rate across 80 pitches; n = 19
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: MANIPULATED_NULL (velocity) / INTERVENTION (heart rate)
SOURCE: Crotin RL et al., MSSE 46(3):565-71, PMID 23917472 — same Buffalo cohort as F-044
COACHING: For a starter, stride length may be a STAMINA lever rather than a velocity lever. Genuinely counterintuitive and worth keeping.
CONFIDENCE: medium — same n = 19 cohort, count it once
SEE ALSO: F-044, F-046

### F-049 | An open pelvis at foot contact is associated with ~1.6 mph and no torque penalty
TOPIC: velocity, pelvis, foot contact, open pelvis, free lever, elbow torque, professional
CLAIM: Professional pitchers with an open pelvis at foot contact threw harder than closed-pelvis pitchers with no significant difference in elbow varus torque.
NUMBERS: ball velocity 39.1 +/- 1.7 vs 38.4 +/- 2.1 m/s (87.5 vs 85.9 mph), P = .029; elbow varus torque 87.8 +/- 14.7 vs 90.5 +/- 17.2 N-m, P = .311; open n = 78, closed n = 79, total n = 157 professional. Open group also had longer stride, greater lead-knee flexion, faster peak knee-extension velocity.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Dowling B, Knapik DM, Luera MJ, Garrigues GE, Nicholson GP, Verma NN (2022), OJSM, PMID 36479467
COACHING: An open PELVIS is not an open CHEST — the chest-square-at-foot-strike failure still stands (F-107). Every co-travelling variable in that list is itself a velocity correlate, so "open pelvis" may be a label for "the delivery that did everything else right." Nobody has opened a pitcher up and measured the gain.
CONFIDENCE: medium — the same error pattern that cost the stride-length recommendation is live here
SEE ALSO: F-043, F-107, F-240

### F-050 | Lead knee extension buys velocity and charges elbow torque — with a 23x magnitude dispute
TOPIC: velocity, lead knee, block, knee extension, elbow torque, exchange rate, conflict
CLAIM: Lead knee extension is associated with higher ball velocity and higher elbow varus torque, but the two published magnitudes differ by roughly 23x.
NUMBERS: Dowling 2024 (n = 50 pro + 50 HS): +1.05 mph per degree, +0.27 N-m per degree. Solomito 2024 (n = 121 collegiate): 0.045 mph per degree in the inverse direction. Same sign, ~23x apart. DO NOT AVERAGE THEM.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Dowling B et al. (2024), OJSM, PMID 39157018; Solomito MJ, Garibay EJ, Cohen A, Nissen CW (2024), Sports Biomech, PMID 35289727
COACHING: Take the direction, not the decimal. The gap almost certainly reflects marker vs markerless conventions, different knee-angle definitions, and between- vs within-subject modeling. If you coach the block, name the price out loud.
CONFIDENCE: medium for direction, low for magnitude
SEE ALSO: F-051, F-052, F-099, F-200

### F-051 | Trunk transverse rotation at ball release: +1.34 mph per 10 degrees, +2.54 N-m
TOPIC: velocity, trunk rotation, ball release, elbow torque, exchange rate, conflict
CLAIM: Greater trunk transverse rotation at ball release is associated with higher velocity and higher elbow varus moment.
NUMBERS: +1.34 mph per 10 deg; +2.54 N-m; n = 99 collegiate
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Solomito MJ et al. (2019), PMID 31424975
COACHING: A lever you pay for. State the exchange rate.
CONFIDENCE: medium
SEE ALSO: F-050, F-052, F-099

### F-052 | Sagittal trunk tilt at ball release: +0.81 to +1.57 mph per 10 degrees, with a torque cost
TOPIC: velocity, trunk tilt, sagittal, ball release, elbow torque, exchange rate
CLAIM: Greater sagittal trunk tilt at release is associated with higher velocity and higher elbow moment, with the two published magnitudes ~2x apart.
NUMBERS: Manzi 2022 (n = 100 pro + 57 HS): +0.81 mph per 10 deg in professionals. Solomito 2018 (n = 99 collegiate): +1.57 mph per 10 deg above 28 deg, +2.9 N-m.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE et al. (2022), JSES 31(1):151-158, PMID 34474134 (has an erratum, PMID 37076208, plus a published letter and author response — check before quoting); Solomito MJ et al. (2018), OJSM, PMID 30349837
COACHING: Same direction, ~2x apart. Take the direction, not the decimal. And note the command cost — F-136.
CONFIDENCE: medium for direction, low for magnitude
SEE ALSO: F-053, F-136, F-050

### F-053 | Trunk flexion at ball release is the strongest velocity coefficient in the literature — and is almost certainly not causal
TOPIC: velocity, trunk flexion, ball release, marker not lever, get out over the front side, downstream
CLAIM: Trunk flexion at ball release is the single strongest kinematic velocity predictor in the professional model, implying an effect size that cannot plausibly be causal at that magnitude.
NUMBERS: beta = 1.829, p < .001; implied +10 deg ~ +3.71 m/s = +8.3 mph; n = 337 professional, 3,627 fastballs, adj. R2 = 0.536
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Diffendaffer / Fleisig group (2024); Manzi JE et al. (2024), OJSM 12(8), PMC11322935
COACHING: MARKER, NOT LEVER. Forward tilt is largely a CONSEQUENCE of a good block and a fast trunk. "Get out over the front side" is already the most over-coached cue in baseball and this number hands it an 8-mph price tag. Telling an 87 mph arm to tip forward buys the posture without the mechanism. It is also the posture the command data penalizes (F-136).
CONFIDENCE: high that the coefficient is real, high that the causal reading is wrong
SEE ALSO: F-136, F-137, F-240

### F-054 | Early arm path: +0.79 mph per 30 cm, with a torque cost
TOPIC: velocity, arm path, elbow torque, professional, exchange rate
CLAIM: For each 30 cm increase in early arm path, ball velocity rose and elbow varus torque rose, in a large professional sample.
NUMBERS: +0.354 m/s (+0.79 mph) per 30 cm; within-pitcher R2 for arm path vs velocity ~ 0.79, vs elbow varus torque ~ 0.96; n = 182 professional
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Dowling B, Hodakowski A, Olmanson BA, et al. (2023), OJSM, PMID 38045766
COACHING: One of the few mechanical variables with a professional sample, a per-unit mph coefficient AND a stated stress cost. Nobody has lengthened a pitcher's arm path and measured what happened.
CONFIDENCE: medium
SEE ALSO: F-050, F-052

### F-055 | Kinematic explanatory power collapses as the population becomes more selected
TOPIC: velocity, ceiling, model, R-squared, selection, restriction of range, professional
CLAIM: Standard 3D kinematics explains 93% of velocity variance in high schoolers and 54% in professionals; the largest in-game D1 model explains 29%.
NUMBERS: HS n = 59 (538 pitches) at 31.3 +/- 2.9 m/s = 70.0 mph -> R2 = 0.925. Professional n = 337 (3,627 pitches) at 38.3 +/- 2.1 m/s = 85.7 mph -> adj. R2 = 0.536. D1 in-game n = 322 -> R2 = 0.29, RMSE 2.70 mph. Also Sgroi 2015 youth R2 = 0.78 but age alone 0.658; Werner 2008 collegiate ~0.68 on 10 predictors / n = 54 (overfit); Huang 2022 adult amateur adj. R2 = 0.230.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE, Dowling B, Wang Z, et al. (2024), OJSM 12(8), PMID 39143985; Fernandez 2026 PMID 42253247
COACHING: Half or more of what separates an 87 mph professional from a 93 mph professional is not captured by any measurement currently taken. Expect WEAKER relationships on a roster of 85+ arms than the literature advertises, and do not read that as a data problem.
CONFIDENCE: high — the gradient, not any single row, is the finding
SEE ALSO: F-010, F-056, F-073, F-079

### F-056 | RESTRICTION OF RANGE — kinematic correlations collapse in a sample that all throws hard
TOPIC: velocity, restriction of range, correlation, elite, methodology, trunk angular velocity
CLAIM: In a professional sample split at ~89.9 vs ~89.0 mph, correlations between kinematics and pitch velocity collapse to small values.
NUMBERS: trunk angular velocity r = .29; upper-trunk rotation at hand separation r = .18; at foot contact r = .17; n = 149 professional
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Luera MJ, Dowling B, Muddle TWD, Jenkins NDM (2020), J Appl Biomech 36(2):68-75, PMID 32143191
COACHING: Published correlations from mixed-level samples are INFLATED relative to what an elite roster will show. The standing warning against importing coefficients across levels.
CONFIDENCE: high
SEE ALSO: F-055, F-023

### F-057 | Sequencing TIMING is a discriminator at lower levels and saturates in the elite band
TOPIC: velocity, kinematic sequence, timing, trunk rotation, saturation, professional
CLAIM: Timing of peak trunk rotational velocity is retained in the high-school velocity model and drops out of the professional model entirely.
NUMBERS: HS beta = 0.133 retained; NOT retained in the professional model (n = 337). Professional retained predictors (B, p): leg length 13.706 (<.001), stride length 0.060 (<.001), trunk flexion at BR 0.371 (<.001), max shoulder ER 0.688 (<.001), elbow extension velocity 0.001 (.006).
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE et al. (2024), OJSM 12(8), PMC11322935
COACHING: By 85+, essentially everyone sequences well enough; it stops separating people. "Fix the sequence" is a lower-level intervention.
CONFIDENCE: medium
SEE ALSO: F-105, F-106, F-107

### F-058 | Hip-shoulder separation is real, over-weighted, and two steps removed from ball speed
TOPIC: velocity, hip shoulder separation, x-factor, trunk rotation, foot contact, pooled review
CLAIM: Hip-shoulder separation is associated with velocity in a pooled review that is nearly half youth, and explains under a fifth of peak trunk rotation velocity on its own.
NUMBERS: pooled association +2.6 +/- 0.5 mph across 12 studies / 930 pitchers (46.1% youth, 17.6% HS, 16.5% collegiate, 19.8% professional). Separation at FC ~50 +/- 12 deg; commonly cited functional band 35-60 deg at peak; strongly torso-length dependent. Separation at FC individually predicted 17% of peak trunk rotation velocity variance (p = .027); combined with peak pelvis velocity (23%, p = .008) and timing of peak trunk velocity, the model explained 55%.
POPULATION: off_population_youth (pooled)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Kew ME et al. (2023), OJSM systematic review, PMID 38035212; Role of Pelvis and Trunk Biomechanics (2022), PMID 35836313
COACHING: "You need X degrees of hip-shoulder separation" is UNSOURCED at the specificity it is coached. No validated target exists, and separation cannot be measured as a number from a single 2D camera.
CONFIDENCE: medium — over-weighted in coaching relative to its measured contribution
SEE ALSO: F-059, F-194, F-229

### F-059 | A quantified trade-off — more pivot-leg rotation can eat your separation
TOPIC: velocity, pivot leg, pelvis rotation, separation, trade-off, collegiate
CLAIM: Trunk separation angle at stride foot contact was the only kinematic variable correlated with ball speed in its sample, and pivot-leg rotational displacement correlated positively with pelvis rotation but NEGATIVELY with trunk separation.
NUMBERS: separation vs ball speed rho = 0.50; pivot-leg rotation vs pelvis rotation rho = 0.70; pivot-leg rotation vs trunk separation rho = -0.49; n = 18 collegiate at 134.2 +/- 5.7 km/h = 83.4 mph
POPULATION: NCAA_D1 (borderline below floor)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wada et al. (2025), Heliyon, PMID 39975838
COACHING: A real mechanical trade-off worth knowing: spinning the back leg more can cost separation.
CONFIDENCE: low-medium — n = 18, borderline population
SEE ALSO: F-058

### F-060 | Ground reaction force — the peak is the wrong measurement; the signal is in braking TIMING
TOPIC: velocity, ground reaction force, GRF, braking, timing, SPM, force plate, lead leg
CLAIM: Discrete GRF peaks are weak velocity predictors in skilled throwers; using statistical parametric mapping across the full time series, pitch velocity significantly predicted lead-leg braking GRF in a specific window.
NUMBERS: braking GRF predicted at ~27% to ~35% of the interval between front-foot contact and ball release; n = 105 high-velocity pitchers, rear + lead force plates. Separately: ball speed showed only a weak association with stride-leg medial force and max elbow valgus torque showed NO correlation with GRF at all (n = 50 HS + 26 collegiate). Peak GRF magnitudes exceeded prior published values, consistent with a higher-velocity sample.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wasserberger KW, Giordano KA (2025), Sports Biomech 24(5):1464-1478, PMID 37991012; Nicholson KF, Hulburt TC, Kimura BM, Aguinaldo AL (2022), J Sports Med Phys Fitness, PMID 34821495
COACHING: This is a MEASUREMENT, not a training target — a ~20 ms slice inside a 30-50 ms phase. When the braking force arrives appears to matter more than how big it is.
CONFIDENCE: medium — genuine methodological insight, no intervention
SEE ALSO: F-061, F-063, F-240

### F-061 | The lead-leg block is real but explains only ~4-6% of between-pitcher velocity variance
TOPIC: velocity, lead leg block, GRF, bodyweight, force plate, Driveline, block
CLAIM: Roughly half the raw lead-leg-force/velocity correlation is bodyweight; once mass is controlled the block explains a small share of between-pitcher velocity variance.
NUMBERS: lead-leg vertical (Z) GRF r = 0.44 raw -> 0.23 bodyweight-controlled; A-P (X) GRF 0.38 -> 0.19; lateral (Y) 0.19 -> 0.10; max resultant lead-leg force 0.25 controlled; knee extension FP->BR r = 0.29; max front-knee extension angular velocity r = 0.25 inter-subject / 0.20 intra-subject; COG deceleration r = 0.20. 800+ force-plate sessions, HS->pro, arms up to 100 mph.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball R&D (2022), "A Quantitative Analysis of the Lead Leg Block and its Contributions to Velocity"
COACHING: The block works by decelerating the center of mass and extending the lead knee, not by adding pelvis spin. Between-pitcher variance may be the wrong denominator — "does his block hold at pitch 75" is a within-athlete question. Corroborating: Guido & Werner (collegiate) higher-velocity pitchers showed higher lead-leg braking GRF; McNally 2015 (adult) stride-leg peak propulsive and vertical GRF related to ball velocity.
CONFIDENCE: medium — single-organization dataset, not peer reviewed
SEE ALSO: F-062, F-050, F-200

### F-062 | REFUTED — the lead-leg block does not work by "whipping the hips"
TOPIC: velocity, block, pelvis rotation, folklore, retired cue, ground reaction force, hips
CLAIM: Pelvis rotation change and pelvis rotational velocity gain after foot plant are essentially zero-to-negative correlates of ball velocity.
NUMBERS: pelvis rotation change FP->BR r = -0.07 raw / 0.10 bodyweight-controlled; pelvis rotational velocity gain r = -0.07 raw / -0.01 controlled; 800+ force-plate sessions
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball R&D (2022), force-plate dataset
COACHING: Do not cue "block to whip the hips" as a velocity mechanism. The cue is retired. NARROWING ON THE RECORD: two nominally different signs on a variable this weak means the honest reading is "indistinguishable from zero," not "negative" — and a between-subject null in a population where everyone already blocks is a restricted-range problem, not proof of irrelevance. One industry dataset should not retire a century-old model unreplicated.
CONFIDENCE: medium — single-organization dataset, not peer reviewed
SEE ALSO: F-061, F-229, F-056

### F-063 | "Get down the mound faster" is mostly wrong — only early body drift matters
TOPIC: velocity, center of mass, COM velocity, body drift, tempo, in-game, D1
CLAIM: In the largest in-band mechanics sample, max forward center-of-mass velocity showed only a weak positive trend with pitch velocity; time-series analysis found significant associations only very early in the motion.
NUMBERS: significant associations only at 0-1% and 4-7% of the motion — i.e. COM velocity generated BEFORE peak knee height; high between-pitcher variability; n = 332 NCAA D1, 8-camera markerless at 300 Hz, IN-GAME
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Zappa RM et al. (2026), J Biomech 205:113411 — verified via LSUHSC institutional repository; NO PubMed record confirmed
COACHING: "Body drift" before peak knee height is beneficial; max COM velocity per se is not a robust predictor. Like F-060, this is a measurement, not a cue.
CONFIDENCE: low-medium — no PubMed record confirmed
SEE ALSO: F-060

### F-064 | The shoulder is a spring, not a motor
TOPIC: mechanism, elastic energy, shoulder, internal rotation, power, layback, arm strength
CLAIM: Peak shoulder internal-rotation power during acceleration is far beyond the contractile capacity of the internal rotators; the power comes from elastic recoil of energy stored during cocking.
NUMBERS: peak shoulder IR power 11,838 +/- 4,170 W in a ~30-50 ms window; negative work at the shoulder during cocking (elastic storage) -201 +/- 70 J; n = 20 baseball players, 3D mocap at 1000 Hz
POPULATION: unspecified — mean ball speed 27.7 +/- 3.8 m/s (~62 mph), target throws from 10 m, NOT off a mound
EVIDENCE: ESTABLISHED (architecture) / EMERGING (magnitudes)
CAUSALITY: MECHANISM
SOURCE: Roach NT, Lieberman DE (2014), J Exp Biol 217(12):2139-2149; mechanism paper Roach et al. (2013), Nature 498:483-486, PMID 23803849
COACHING: "You are not trying to build a bigger motor, you are trying to build a better spring and a better loader of that spring." This is why arm-strength training has never produced velocity in a controlled trial.
CONFIDENCE: high for the architecture; the magnitudes do not transfer to our velocity band
SEE ALSO: F-065, F-067, F-127, F-133

### F-065 | The hips do ~90% of the work of rotating the torso and supply ~30% of the power reaching the shoulder
TOPIC: mechanism, hips, torso rotation, power, lower half, selective restriction
CLAIM: Selective restriction of segments quantifies the lower half's contribution to throwing power.
NUMBERS: hip rotators ~30% of the power for rapid shoulder IR; ~90% of torso rotation work; elbow and wrist direct power generation minimal (passively driven). Selective restriction, change in ball speed: shoulder ER limited -8 +/- 6% (p < .001); torso rotation -5 +/- 6% (p < .001); clavicle -3 +/- 6% (p = .031); wrist inconclusive (sham effects).
POPULATION: unspecified (~62 mph target throws)
EVIDENCE: ESTABLISHED (architecture)
CAUSALITY: MECHANISM
SOURCE: Roach NT, Lieberman DE (2014), J Exp Biol 217(12):2139-2149
COACHING: The mechanistic justification for lower-body training as the primary velocity lever, and consistent with F-033 and F-034 being the only positive controlled non-implement trials.
CONFIDENCE: high for architecture, magnitudes off-population
SEE ALSO: F-064, F-066, F-068, F-034

### F-066 | Trunk power ALONE predicts ball velocity at R2 = 0.731
TOPIC: mechanism, trunk power, energy, segmental power, professional, high school
CLAIM: Trunk power alone predicted ball velocity, professionals generated significantly greater trunk power than high schoolers, and normalized elbow valgus torque did not differ between levels.
NUMBERS: R2 = 0.731; n = 31 (16 professional at 81.2 mph, 15 HS at 68.0 mph); absolute elbow valgus torque higher in pros (71.3 vs 50.7 N-m) but NORMALIZED torque did not differ
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Aguinaldo A, Escamilla R (2019), OJSM 7(2), PMID 30828584
COACHING: The extra absolute load in professionals is body-size scaling, not riskier mechanics. Do NOT restate this as "r = .840 for trunk rotation power" — that figure is a garbled version of this R2 and should be discarded (F-217).
CONFIDENCE: medium — n = 31
SEE ALSO: F-034, F-067, F-217

### F-067 | The trunk is the energy SOURCE; shoulder and elbow are TRANSFER elements — and ~27% never reaches the ball
TOPIC: mechanism, energy flow, trunk, transfer, loss, work, collegiate
CLAIM: Trunk muscular torques are the primary energy sources; the shoulder and elbow function predominantly as transfer mechanisms; roughly a quarter of generated work does not reach the ball.
NUMBERS: of 329.2 J of total muscular work from trunk + arm joints, 72.7% was directed to moving the throwing hand and ball -> ~27% loss; n = 16 male collegiate pitchers
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: MECHANISM
SOURCE: Naito K (2021), J Exp Biol, PMID 34495332
COACHING: The cleanest quantified loss term in the literature. The arm is the last and least powerful link, and every intervention aimed at it is aimed at the smallest term in the equation.
CONFIDENCE: medium — n = 16
SEE ALSO: F-064, F-065, F-066, F-127

### F-068 | The two legs do different jobs — rear leg generates, front leg conducts and brakes
TOPIC: mechanism, energy flow, trail leg, lead leg, generation, transfer, GRF
CLAIM: Energy generation was higher in the trailing leg, arising primarily from the trailing hip; the lead leg mainly transfers energy upward in a distal-to-proximal order.
NUMBERS: n = 22 (de Swart, HS). Youth energy-flow work: drive-leg peak GRF and both legs' GRF impulse -> joint force and power components of energy flow into pelvis and trunk; stride-leg peak GRF and impulse -> joint moment and power components of energy flow into the arm.
POPULATION: off_population_HS / off_population_youth
EVIDENCE: EMERGING
CAUSALITY: MECHANISM
SOURCE: de Swart AFMJ, van Trigt B, Wasserberger K, Hoozemans MJM, Veeger DHEJ, Oliver GD (2022/2025), Sports Biomech, PMID 36226680; Howenstein J, Kipp K, Sabick MB (2020), J Biomech, PMID 32635991
COACHING: "The back leg feeds the middle, the front leg feeds the arm." Needs replication in an elite sample.
CONFIDENCE: medium for the principle, low for magnitudes at 85+
SEE ALSO: F-060, F-061, F-065

### F-069 | Wind-up and stretch produce statistically similar velocity and kinematics in professionals
TOPIC: mechanics, windup, stretch, slide step, velocity, retired cue
CLAIM: Professionals produce statistically similar ball velocity and kinematics from the wind-up and from the stretch.
NUMBERS: effect sizes not recorded in the corpus; replicated on dirt mounds
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS, Slowik JS, Kutz CB, Escamilla RF (2024), AJSM; Escamilla RF, Slowik JS, Imamura R, et al. (2026), J Appl Biomech (dirt-mound replication)
COACHING: "You lose velo from the stretch" is RETIRED at the professional level.
CONFIDENCE: medium-high — replicated
SEE ALSO: F-229

### F-070 | Lower arm slot: less torque, more run value, slightly less velocity — but it is not universal
TOPIC: arm slot, arm angle, torque, VAA, run value, spin rate, platoon, sidearm
CLAIM: In professionals, a lower (more sidearm) slot associates with lower elbow varus AND shoulder IR torque; MLB pitchers dropping slot gained run value and spin at a small velocity cost.
NUMBERS: professionals, every +10 deg of slot (lower/more sidearm) -> -0.1 %BW x BH in BOTH elbow varus torque (beta = -0.22, p < .001) and shoulder IR torque (beta = -0.20, p < .001). In HIGH SCHOOLERS the relationship INVERTS for elbow flexion torque (beta = +0.28, p = .002). ~4.23 N-m less varus torque per 10 deg of higher/more-overhand slot at consistent velocity (n = 66 elite college, OpenBiomechanics). ~4% torque reduction per 10 deg. MLB release points ~2 in lower than 2016; arm angle down 1.41 deg since 2020; pitchers dropping slot 2 deg+ gained +2.14 run value and +18.3 rpm on the four-seam at a cost of ~0.15 mph. Pro slot 58 +/- 14 deg vs HS 50 +/- 11 deg (higher number = more sidearm).
POPULATION: professional_mixed / NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Escamilla/Fleisig (2023), PMC10601404; Sports Biomechanics 24(8), n = 66, PMID 39744973; Sawchik T / Driveline (2026)
COACHING: The one lever where the velocity cost is trivial and the stress reduction is real. BUT: it inverts at the HS level; it requires wrist radial-deviation mobility to hold spin efficiency (Skenes tried and reverted); the common failure mode is "lowering the slot" by adding trunk lateral tilt, which RAISES elbow varus torque; it is platoon-dependent (F-071); and the plus-command arms sit HIGHER (F-136). Slot is a package, not a dial.
CONFIDENCE: medium-high for direction in professionals, low for universality
SEE ALSO: F-071, F-136, F-178, F-229

### F-071 | Arm angle is platoon-dependent
TOPIC: arm slot, arm angle, platoon, handedness, wOBA, run value, deployment
CLAIM: Lower arm angles perform better against same-handed batters; higher arm angles perform better against opposite-handed batters.
NUMBERS: same-sided correlations arm angle -> wOBA .13, -> xwOBA .23; velocity -.18. The author flags an unexplained anomaly: every metric correlated better with xwOBA than with actual wOBA.
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Andrews D (27 Nov 2024), "An Arm Angle Update That Ends With a Mystery," FanGraphs
COACHING: Lower slot is a same-handed weapon. Contraindicated for a pitcher facing predominantly opposite-handed hitters. Prior context: Eisert, FanGraphs, Feb 2023 — +0.02% called-strike rate per degree toward sidearm across 473 pitchers with 500+ pitches; effect disappears when controlling for pitch selection and count.
CONFIDENCE: medium — public analytics, author transparent about an anomaly he cannot explain
SEE ALSO: F-070, F-136, F-178

---

# 4 — VELOCITY: THE CEILING, AGING, AND REAL BASE RATES

### F-072 | The best population-matched training result: +0.65 mph in arms entering at 88+
TOPIC: velocity, base rate, ceiling, Driveline, 88 mph, training block, responder, expectation
CLAIM: In the only public dataset restricted to arms entering at 88+ mph, a dedicated program moved the group about two-thirds of a mile per hour on average, with nearly one in five losing more than a full mph.
NUMBERS: n = 58 "high-level athletes," entry fastball >= 88 mph, age >= 19 (mean 23), >= 3 weeks training, mean 67 days between measurements. Mean pen velocity 89.6 -> 90.3 = +0.65 mph — verified two ways: the article's own summary table, and its binned distribution reconstructing to +0.63. 41.95% gained >= 1 mph; 18.39% LOST > 1 mph.
POPULATION: professional_mixed — described as "high-level athletes," NOT explicitly professionals
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Driveline Baseball (4 Apr 2019), "The Value in Developing Velocity in the Minors" — site byline Kaitlyn Neiswender, closing credit Dan Aucoin
COACHING: This is the number to say to an 88 mph athlete on day one. Any facility quoting "3-5 mph" to an 88 mph arm is off by a factor of five to eight against the best-matched public evidence. Say the 18% out loud before he pays, not after he loses.
CONFIDENCE: medium for the figure, low for the design — grey literature, vendor-published, no control group. CORRECTED 2026-08-13 from a previously recorded +1.35 mph. DO NOT RE-IMPORT +1.35.
SEE ALSO: F-073, F-074, F-240

### F-073 | The ceiling measured directly: year-over-year MLB velocity change is monotone decreasing in baseline
TOPIC: velocity, ceiling, year over year, Statcast, MLB, baseline, aging, distribution
CLAIM: Expected annual velocity change decreases with baseline velocity and turns negative above roughly 93 mph.
NUMBERS: Statcast 2021-2023, four-seam + sinker, min 50 pitches, n = 1,163 pitcher x pitch-type x consecutive-season PAIRS (one pitcher can contribute two rows; rows are not independent). Distribution: >= +2 mph 30 rows = 2.5%; >= +1 mph 141 = 12.1%; <= -1 mph 191 = 16.4%; <= -2 mph 14 = 1.2%. By bin: 92 mph bin (n = 127) mean +0.26 mph — the ONLY bin above 91 with a positive mean; 54% gained but only 16/127 (12.5%) added more than 1 mph. 93-97 bins mean negative. 98+ bin (n = 16) negative.
POPULATION: MLB
EVIDENCE: ESTABLISHED (as industry analysis with a transparent method)
CAUSALITY: CROSS_SECTIONAL
SOURCE: "Investigating Fastball Velo Changes," MLB Data Warehouse Substack, author "Jon A" (13 Feb 2024)
COACHING: TWO CORRECTIONS 2026-08-13. (1) The unit is NOT "pitcher-seasons" — do not re-import that. (2) The reported -1.15 mph mean is internally inconsistent with the source's own distribution and is probably a source error — a sample where only 1.2% lost more than 2 mph cannot average -1.15. Flag it or do not cite it.
CONFIDENCE: medium for the distribution, zero for the mean. Single-author grey literature, no code, no data file, no peer review. Confound: velocity bin correlates with age in MLB, mixing ceiling effects with aging and regression to the mean.
SEE ALSO: F-072, F-075, F-240

### F-074 | Aggregate training-block results, and the ~20% who lose velocity
TOPIC: velocity, base rate, Driveline, training block, responder, non-responder, aggregate
CLAIM: A single training block at the best-resourced facility in the sport, in a mixed HS-to-pro population, produces roughly +1 mph on average with a ~20% chance of losing velocity; sustained engagement over 200+ days produces ~+3.3 mph.
NUMBERS: 2018 summer — 265 assessed, 120 with entry/exit data; mean gain all athletes +0.74 mph; >= 3 weeks +0.95 mph; distribution at >= 3 wk 60.6% gained >= 0.5 / 19.2% maintained / 20.2% LOST. 2019-2020 — single block 52% gained > 1 mph / 27% within +/-1 / 21% lost; first-to-latest mocap mean +1.8 mph; athletes with 200+ days between assessments (n = 35) +3.29 mph.
POPULATION: professional_mixed (HS -> pro)
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Driveline Baseball (2018), "2018 Summer Pitching Review"; Driveline (2021), "Pitching Training Velocity Results 2019-2020"
COACHING: Both figures are inflated by the developing athletes in the sample and neither is isolated to 85+ arms. "Roughly 18-21% of trained pitchers LOSE velocity over a block" is the base rate at the best-resourced facility in the sport. Driveline's own line: "It's generally tougher to gain velocity for hard throwers."
CONFIDENCE: medium — no control group, self-selected, motivated population, heterogeneous goals
SEE ALSO: F-072, F-073, F-231

### F-075 | The aging curve — the default professional trajectory is DOWN, but 40% hold
TOPIC: velocity, aging, age curve, decline, starters, relievers, career, maintenance
CLAIM: At the major-league level velocity does not improve with age; starters begin losing it in their mid-20s. But roughly two in five professional pitchers hold velocity essentially flat.
NUMBERS: within ~0.5 mph of peak at ages 23-28; cumulative loss accelerates ~1 mph/yr from age 29; total career cumulative loss ~3.75 mph. Starters peak early 20s (~24), down a full 1 mph by age 26, ~2 mph below peak by 30. Relievers do not lose a full mph off peak until age 32, then decline sharply. Age-24 mean FB 91.1 -> age-34 89.4 (survivorship-attenuated). ~40% of pitchers hold velocity, losing only 0.3 mph total from 21 -> 38, plateauing 25-30; ~60% decline.
POPULATION: MLB
EVIDENCE: ESTABLISHED (with survivorship caveat)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Petti B & Zimmerman J (2012), "Pitcher Aging Curves" series, FanGraphs — delta/paired-season method, BIS 2002-2011, 2013 SABR Analytics Research Award; blog analysis, not peer-reviewed
COACHING: The window for ADDING velocity is roughly 17-24. After that the goal shifts to delaying the loss. Holding 88 for six more years puts an athlete in the top two-fifths of professional pitchers at the thing that ends most careers — a real trainable outcome, not a consolation prize. Kalk (2008, THT, n = 143) reported peak at 28-29; treat as historical, superseded by the larger delta-method work.
CONFIDENCE: medium-high — canonical but not peer-reviewed, survivorship-attenuated
SEE ALSO: F-073, F-077, F-080

### F-076 | The league is getting faster, which is selection, not development
TOPIC: velocity, league average, trend, selection, MLB, context
CLAIM: League-average four-seam velocity has risen for six consecutive seasons; this reflects who gets rostered, drafted, and reliever usage, not individuals gaining.
NUMBERS: 2008 (first tracked) 91.9 -> 2013 92.7 -> 2021 93.7 -> 2025 94.5 -> 2026 (through mid-July) 94.7. RHP average 95.2; RH relievers 95.6. Triple-A 92.7 (2022) -> 93.6 (2026). Six pitchers averaged >= 100 mph on the four-seamer in 2026. Starters aged <= 25 averaged 94.7 mph in early 2022, an all-time cohort high. Population mean rising ~0.2 mph/year.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Blum R / Associated Press (July 2026); Choi J (2022), FanGraphs; MLB pitcher-injury report (Dec 2024) records 91.3 (2008) -> 94.2 (2024) -> 94.6 (2026)
COACHING: A rising league average does not mean individual pitchers are gaining — F-073 says most are not. Do not let one be used as evidence for the other.
CONFIDENCE: high
SEE ALSO: F-073, F-075

### F-077 | Adolescent velocity gains decelerate exactly as a ceiling hypothesis predicts
TOPIC: velocity, adolescent, development, maturation, trajectory, ceiling, youth
CLAIM: A reconstructed trajectory of 25 MLB pitchers through adolescence shows year-on-year gains decelerating steadily through the 85+ transition.
NUMBERS: age 13 -> 72 mph; 14 -> 78 (+6); 15 -> 84 (+6); 16 -> 89 (+5); 17 -> 92 (+3); 18 -> 94 (+2). 80% of peak velocity at ~13.5 yr; 90% at ~15.4 yr; several at 100% of peak by 17-18. Plateau across 85-91% of adult height (around peak height velocity), then resumption at >= 95% of adult height. n = 25, 154 retrospective observations from Perfect Game records, Baseball-Reference and Statcast.
POPULATION: MLB (retrospective adolescent reconstruction)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Eisenmann J (2026), "Chasing Velo," Archives of IronMan Performance Vol. 1 — self-published, NOT peer-reviewed
COACHING: By the time an athlete reaches 85+, he is on the flat part of his own curve.
CONFIDENCE: low-medium — severe retrospective selection on the outcome (all 25 became MLB pitchers); sample explicitly tall, large and early-maturing (~1 yr ahead of norms)
SEE ALSO: F-075, F-078

### F-078 | WARNING — youth velocity models are maturation models wearing mechanics clothes
TOPIC: velocity, youth, model, age, maturation, off population, prediction, caution
CLAIM: The most-quoted youth velocity model's explanatory power collapses once age is removed.
NUMBERS: n = 420 youth/adolescent; R2 = 0.78 total but age alone carries R2 = 0.658 — the rest is ~12%. Its per-unit figures: +1.5 mph/year of age, +1.2 mph/inch of height, +2.6 mph for hip-shoulder separation, +1.9 mph per 10% stride-length increase.
POPULATION: off_population_youth
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Sgroi T, Chalmers PN, Riff AJ, et al. (2015), JSES 24(9):1339-45, PMID 25842029
COACHING: These per-unit figures should NOT anchor priors for an adult. They circulate widely as if they do.
CONFIDENCE: high that the model is maturation-driven
SEE ALSO: F-055, F-058, F-077

### F-079 | GAP — no velocity-ceiling model and no heritability estimate for throwing velocity exist
TOPIC: velocity, ceiling, model, gap, heritability, twin study, missing, fabrication risk
CLAIM: No published velocity-ceiling model exists, peer-reviewed or industry. No heritability estimate for throwing or pitching velocity exists.
NUMBERS: the ceiling concept appears only as (i) Driveline's informal exclusion of 45+ FV prospects as "closer to their velocity ceiling"; (ii) the bin-wise pattern in F-073; (iii) the 40%-who-hold split in F-075; (iv) capacity-based prediction with +/-2.7 mph error. Nearest adjacent twin work (Maes 1996, MSSE, 105 twin pairs, nine motor tests, PMID 8970142) contains NO throwing test at all. Adolescent twin estimates for grip (~59%), vertical jump (~49%) and standing long jump (~52%) exist but are proxies and were not verified at primary source.
POPULATION: unspecified
EVIDENCE: UNSOURCED (as an absence)
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 6.6
COACHING: This is exactly where AI content farms fabricate. If you encounter a "twin study on throwing velocity heritability" with a specific h2, assume it is invented until you open the PubMed record yourself.
CONFIDENCE: high that both gaps are real — both were searched for
SEE ALSO: F-220, F-234

### F-080 | Realistic annual velocity gain, by population
TOPIC: velocity, expectation, annual gain, base rate, coaching conversation, prognosis
CLAIM: Expected annual gain declines sharply with baseline velocity and turns negative at the top.
NUMBERS: developing HS arm 67-75 mph -> +2 to +5 mph (NOT our population). Elite HS / D1 85-90 mph -> +1.5 to +3 mph in a committed year. >= 88 mph high-level cohort -> +0.65 mph mean, 42% gain >= 1 mph, 18.4% LOSE > 1 mph. MLB 92+ -> only 12.1% gain >= 1 mph, only 2.5% gain >= 2 mph.
POPULATION: mixed
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION / CROSS_SECTIONAL (mixed)
SOURCE: synthesis in velocity-development.md 5.6
COACHING: 88 to 93 is a five-mph ask against a population-matched mean of two-thirds of a mile an hour per block. That is a multi-year project or it does not happen at all. Say it in the first meeting.
CONFIDENCE: medium — assembled from grey literature and off-population trials
SEE ALSO: F-072, F-073, F-075

### F-081 | UNVERIFIED — the college-to-pro velocity cohort that would matter most is paywalled
TOPIC: velocity, draft, college to pro, transition, window, unverified, paywalled
CLAIM: Of 100 college pitchers tracked from draft spring to a later professional measurement, 64 increased velocity, 50 by >= 1 mph and 27 by >= 2 mph.
NUMBERS: n = 100; 64 / 50 / 27
POPULATION: NCAA_D1 -> MiLB
EVIDENCE: UNSOURCED (paywalled; figures taken from a search abstract, never read in full)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball America — PAYWALLED. Verify before relying.
COACHING: If it holds, 27% gaining >= 2 mph vs 2.5% in MLB is exactly the signature of a population not yet at its ceiling, and would be the strongest argument that the D1-to-pro transition is the last real window. Do not quote until verified.
CONFIDENCE: low — flagged as an outstanding verification item
SEE ALSO: F-073, F-075, F-242

### F-082 | REFUTED — in-season velocity RISES; it does not decay
TOPIC: velocity, in season, decay, maintenance, monthly, MLB, MiLB, folklore
CLAIM: MLB starting-pitcher fastball velocity climbs across a season, and minor-league velocity rises linearly across early games.
NUMBERS: MLB starters 2007-2011 five-year average by month: Mar/Apr 90.1 -> May 90.4 -> Jun 90.5 -> Jul 90.6 -> Aug 90.7 -> Sep/Oct 90.7 (season 90.5). +0.6 mph across the season, largest jump April -> May (+0.3), plateau from June. MiLB: fastball velocity increased linearly across the first 8 games (R = 0.91, p < .001), ~2 m/s total, n = 12; rest days and work:rest ratios had no significant effect.
POPULATION: MLB / MiLB
EVIDENCE: ESTABLISHED (at the league level)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Podhorzer M (2012), "Historical Monthly Velocity Trends," RotoGraphs/FanGraphs; Crotin RL, Bhan S, Karakolis T, Ramsey DK (2013), JSCR 27(8):2206-2212, PMID 23222081
COACHING: The widespread belief in monotonic in-season velocity decay is wrong. This reframes "in-season maintenance" as protecting a RISING curve. An individual's mid-season velocity drop is a signal worth investigating, not the expected pattern. This is also the missing counterfactual that sinks F-039. Podhorzer's operational line: "pitchers do not suddenly regain two miles per hour on their fastball in the middle of the season."
CONFIDENCE: high at the league level; individual variation not addressed
SEE ALSO: F-039, F-083

### F-083 | The in-season strength-loss evidence is much thinner than commonly claimed
TOPIC: in season, strength loss, detraining, shoulder strength, maintenance, gap
CLAIM: There is no good in-season strength-loss dataset in collegiate or professional baseball; the largest samples are n = 9 and n = 12 and the D1 longitudinal study shows gains.
NUMBERS: Wilkin & Haddock 2006, n = 9 D-II — isokinetic shoulder IR/ER at preseason/midseason/postseason, "no differences at any speed tested or time point examined." Merfeld 2024, n = 12 NCAA D-II/III across a 12-week summer league — throwing-arm shoulder strength composite -9.03% (ES 0.72, p = .08); non-throwing arm -2.03%; the same paper reports CMJ peak power +44.79% in 12 weeks, implausible and almost certainly familiarization drift. Hornsby 2021, n = 4 D1 across 3 seasons — IMTP peak force INCREASED year over year. Lambert 2023 — D1 control group lost shoulder flexion and IR strength across 8 offseason weeks.
POPULATION: NCAA_D1 / NCAA D-II/III
EVIDENCE: WEAK
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wilkin LD, Haddock BL (2006), JSCR 20(4):829-32, PMID 17194237; Merfeld B et al. (2024), JFMK 9(2):98, PMID 38921634; Hornsby WG et al. (2021), PMID 33462166; Lambert 2023, PMID 36933646
COACHING: In-season strength maintenance is a defensible practice recommendation with a thin evidence base — and the velocity data (F-082) suggest whatever is happening to strength is not costing mph. The asymmetry (throwing arm only) in Merfeld is the credible part. Read Wilkin as "no detectable change," not "no change."
CONFIDENCE: low
SEE ALSO: F-036, F-082, F-132, F-215

### F-084 | GAP — transfer lag between a strength adaptation and its expression in ball speed has never been measured
TOPIC: velocity, transfer lag, periodization, time course, gap, phase potentiation, offseason
CLAIM: No study anywhere — baseball, handball, any throwing sport — measures the latency between a strength or power adaptation and its expression in throwing velocity.
NUMBERS: nearest proxies — minimum throwing-intervention length to expect anything >= 6 weeks; implement/throwing blocks express at 6-10 weeks; trunk/lower-body strength -> ball speed at 8 weeks (Oyama, HS); shoulder lean mass +227 g at 8 weeks with BFR; aggregate velocity change at 200+ days -> +3.29 mph (n = 35)
POPULATION: unspecified
EVIDENCE: FOLKLORE (as a quantified concept)
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 5.2; the concept exists only in Verkhoshansky/Issurin periodization theory and is applied to baseball by analogy
COACHING: The 6-10 week window is where throwing-specific interventions express; the strength/mass signal appears on a much slower clock. Different time constants — sequence them, do not run both at full volume simultaneously.
CONFIDENCE: high that the gap exists
SEE ALSO: F-085, F-038

### F-085 | The industry offseason block structure implies a lead-time constraint
TOPIC: program design, offseason, periodization, block, scheduling, velocity phase, industry
CLAIM: A published four-phase offseason structure, built backward from spring training, implies that a velocity block does not fit unless the athlete starts early.
NUMBERS: ~20-week professional offseason (Oct-Feb): on-ramping 3-4 weeks (low volume -> high intent); velocity 1-4 weeks (scheduled throwing at 100% effort); mound blending ~1 week; mound development 1-4 weeks. Stated consequence: an October start gets the full block; November still includes velocity work; a December start gets on-ramping and mound development with NO velocity phase at all; January is preparation only.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball, "Off-Season Baseball Throwing Program"
COACHING: Practical rule: if the athlete is not on the mound by early November, the offseason does not contain a velocity block. An industry scheduling heuristic, not a trial result — but the most concrete statement of transfer lag available.
CONFIDENCE: medium — no validation study
SEE ALSO: F-084, F-086

### F-086 | Autoregulation thresholds from industry practice
TOPIC: program design, autoregulation, fatigue, velocity decline, session termination, undulation
CLAIM: An industry protocol targets a ~6% weekly velocity decline distributed across sessions, with stated thresholds for productive stress versus exhaustion.
NUMBERS: within-week undulation targeting ~6% weekly velocity decline; 1-9% performance decline = productive stress; >= 10% = exhaustion requiring 2-3 weeks of recovery; session termination at 4-6% drop (frequency work) or 6-10% (capacity work)
POPULATION: unspecified
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball (2025), "Understanding and Managing Training Fatigue: From Theory to Practice"
COACHING: Industry practice, no validation study. A starting heuristic, not a threshold with evidence behind it.
CONFIDENCE: low-medium
SEE ALSO: F-085, F-160

---

# 5 — BIOMECHANICS: PHASES, KINEMATICS, KINETICS

### F-087 | The six phases and the four landmarks that index every number
TOPIC: biomechanics, phases, landmarks, foot contact, MER, ball release, MIR, timing
CLAIM: The field-standard six-phase model is indexed to four hard landmarks a coach can find on video: FC, MER, BR, MIR.
NUMBERS: wind-up (initiation -> max lead-knee lift / hands separate); stride/early cocking (hand separation -> stride foot contact FC); arm cocking/late cocking (FC -> max shoulder external rotation MER); arm acceleration (MER -> ball release BR); arm deceleration (BR -> max shoulder internal rotation MIR); follow-through (MIR -> balanced fielding position)
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Fleisig et al. (1996/1999); reviewed in Diffendaffer AZ et al. (2023), Sports Health
COACHING: Every meaningful number in the corpus is indexed to one of these four landmarks. Learn to find them at 240 fps.
CONFIDENCE: high
SEE ALSO: F-088, F-089

### F-088 | Phase durations — the stride is the only phase long enough to coach
TOPIC: biomechanics, timing, phase duration, foot contact, coachability, acceleration phase
CLAIM: Arm cocking and arm acceleration are too short to steer consciously, which makes foot contact the last moment the athlete can organize anything.
NUMBERS: wind-up ~500-1000 ms; stride ~500-750 ms; arm cocking FC->MER ~100-150 ms; arm acceleration MER->BR ~30-50 ms (classic ASMI figure ~30 ms; a review source gives 42-58 ms — method-dependent, do not treat any single millisecond figure as settled); arm deceleration BR->MIR ~30-50 ms; follow-through ~300-1000 ms. Total FC->BR is on the order of 130-200 ms.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 2.2, ASMI convention
COACHING: This is the mechanistic reason behind "it's easier to fix things before foot strike." If a fix has to happen after front-foot strike, it is not a fix — it is a wish. Build it into the stride or into a constraint.
CONFIDENCE: high for the order of magnitude, medium for any specific figure
SEE ALSO: F-087, F-107

### F-089 | Professional kinematic norms (ASMI database, n = 288)
TOPIC: biomechanics, norms, kinematics, ASMI, reference values, arm slot, stride length, MER
CLAIM: The ASMI professional arm-slot cohort supplies the field's reference kinematic values, by landmark and by arm-slot subgroup.
NUMBERS: n = 288 professional, age 21.9 +/- 2.1, height 189.7 +/- 5.8 cm, mass 94.7 +/- 9.6 kg, lab FB 38.1 +/- 4.1 m/s (85.2 mph IN LAB). Overhand subgroup (AS1, n = 80) / sidearm (AS3, n = 66). AT FC: stride length 76 +/- 9 / 75 +/- 5 %height; lead knee flexion 49 +/- 7 / 44 +/- 9 deg; shoulder abduction 85 +/- 12 / 82 +/- 10 deg; elbow flexion 101 +/- 15 / 93 +/- 19 deg; trunk flexion -3 +/- 11 / -17 +/- 14 deg. AT MER: max shoulder ER 165 +/- 9 / 168 +/- 10 deg; max elbow flexion 90 +/- 11 / 89 +/- 9 deg; shoulder horizontal adduction 7 +/- 9 / 11 +/- 7 deg. AT BR: arm slot 44 +/- 7 / 75 +/- 15 deg; shoulder abduction 95 +/- 7 / 84 +/- 9 deg; trunk lateral flexion 34 +/- 8 / 24 +/- 11 deg; trunk flexion 7 +/- 11 / 15 +/- 12 deg; elbow flexion 30 +/- 6 / 35 +/- 6 deg.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Escamilla RF, Fleisig GS, et al. (2023), PMC10601404
COACHING: Norms are the bounds of the possible, not a target for this arm. Absolute thresholds do not transfer across capture systems (F-200).
CONFIDENCE: high for the values, with the lab-vs-game caveat (F-208)
SEE ALSO: F-090, F-208, F-200

### F-090 | Peak angular velocities — shoulder internal rotation is the fastest recorded human joint motion
TOPIC: biomechanics, angular velocity, shoulder internal rotation, elbow extension, pelvis, trunk
CLAIM: Elite peak segment angular velocities span from ~600 deg/s at the pelvis to ~6,000-7,500 deg/s at the shoulder.
NUMBERS: max pelvis angular velocity 622 +/- 83 (overhand) / 717 +/- 92 (sidearm) deg/s; max upper trunk 742 +/- 221 / 711 +/- 228 deg/s; time of max upper trunk velocity 56.5 +/- 7.1 / 63.9 +/- 7.4 % pitch time; max elbow extension velocity 2403 +/- 269 / 2191 +/- 289 deg/s; max shoulder IR velocity 6149 +/- 1153 / 5456 +/- 990 deg/s. Cross-study bounds: pelvis 590-1202; trunk 700-1200; elbow extension 1742-2500; shoulder IR up to ~7,500 deg/s.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Escamilla RF, Fleisig GS, et al. (2023), PMC10601404
COACHING: These are OUTPUTS, not training targets. Peak shoulder IR velocity and elbow extension velocity are readouts of upstream delivery.
CONFIDENCE: high
SEE ALSO: F-089, F-127

### F-091 | Elbow varus torque — absolute values, and the 64-to-120 N-m problem
TOPIC: kinetics, elbow varus torque, valgus load, norms, lab comparability, N-m
CLAIM: Published absolute elbow varus torque in professionals spans nearly a factor of two across laboratories for the same population.
NUMBERS: 94.3 +/- 16.1 N-m (n = 305 MiLB, uninjured subgroup); 100.8 +/- 18.1 N-m (later-UCL-surgery subgroup); "near 100 N-m" in n = 523 (425 pro, 98 D1); older ASMI reporting ~64 N-m (range 52-76) and ~120 N-m at MER in some reports
POPULATION: professional_mixed / MiLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), OJSM, PMC12227930 and PMC11789100; biomechanics.md 4.1
COACHING: DO NOT compare a torque number from one lab to a number from another lab. Within a system the numbers are usable; across systems they are not. See F-203 for the mechanism.
CONFIDENCE: high that the spread is real and methodological
SEE ALSO: F-092, F-203, F-208

### F-092 | Normalized kinetic norms in %BW x BH — the mechanics, versus what the ligament feels
TOPIC: kinetics, normalized torque, %BW x BH, elbow varus, shoulder IR, professional, high school
CLAIM: Normalized torque allows comparison across body sizes; absolute torque is what the tissue experiences.
NUMBERS: PROFESSIONAL — elbow varus 4.8-5.1 %BW x BH; shoulder IR torque 4.9-5.2; shoulder horizontal adduction torque 5.6; elbow flexion torque 3.8-4.1. HIGH SCHOOL (off-population, 70 mph mean) — elbow varus 3.8-4.0; shoulder IR 4.0-4.1; shoulder horizontal adduction 4.6-4.7; elbow flexion 2.7-3.2. Worked example: 0.051 x 929 N x 1.897 m ~ 90 N-m for a 94.7 kg / 1.897 m professional; the same normalized value on a 79 kg / 1.83 m elite HS arm gives ~72 N-m.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Escamilla RF, Fleisig GS, et al. (2023), PMC10601404
COACHING: Normalized torque is the mechanics; absolute torque is what the ligament feels. Both are needed.
CONFIDENCE: high
SEE ALSO: F-091, F-093

### F-093 | THE CENTRAL FACT — 28% different elbow load for 1% different velocity
TOPIC: kinetics, efficiency, elbow varus torque, high torque, low torque, coaching opportunity
CLAIM: Within elite pitchers there exist arms producing essentially the same ball velocity at 28% less normalized elbow load.
NUMBERS: high-torque group 6.37 +/- 0.6 %BW x BH vs low-torque group 4.61 +/- 0.4 for a 1% velocity difference (38.0 vs 37.1 m/s); n = 523 (425 professional, 98 D1); 11 kinematic parameters explained 40% of variance in normalized elbow varus torque
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), OJSM, PMC11789100 / McCutcheon TW, Slowik JS, Fleisig GS (2025), PMID 39906602
COACHING: Efficiency is real, large and measurable. The arm-dominant pitcher is not slow — he is EXPENSIVE. But nobody has demonstrated a within-athlete curve shift; the gap may be anthropometry, tissue quality and humeral torsion rather than mechanics.
CONFIDENCE: high for the gap, unknown for its coachability — this is Dispute 3, the central open question of the program
SEE ALSO: F-094, F-100, F-101

### F-094 | Between-pitcher and within-pitcher velocity-torque associations diverge wildly
TOPIC: kinetics, within subject, between subject, methodology, elbow torque, velocity, Slowik
CLAIM: Fastball velocity is a weak between-subject predictor of elbow varus torque and an almost deterministic within-subject one.
NUMBERS: BETWEEN subjects R2 = 0.076 (p = .03); WITHIN an individual R2 = 0.957 (p < .001); n = 64 professional. Corroborated: between-pitcher R2 = 0.228 for shoulder distraction vs within-pitcher R2 > 0.85 across 10 kinetic measures, n = 91 pro analyzed.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Slowik JS, Aune KT, Diffendaffer AZ, Cain EL, Dugas JR, Fleisig GS (2019), J Athl Train 54(3):296-301, PMID 30721094; Manzi JE et al. (2021), JSES, PMID 33930560
COACHING: Comparing two pitchers tells you almost nothing about their relative elbow load; comparing one pitcher to himself tells you almost everything. YOUR athlete cannot add velocity to his current delivery for free. Every cross-athlete ranking in this corpus is suspect by default.
CONFIDENCE: high — the most important methodological finding in this literature
SEE ALSO: F-093, F-095, F-100

### F-095 | PROSPECTIVE — torque predicts UCL surgery; velocity does not
TOPIC: injury, UCL, prospective, elbow varus torque, velocity, risk, MiLB, hazard ratio
CLAIM: In the only high-quality prospective biomechanics-to-injury study in pro baseball, elbow varus torque differed between pitchers who later required UCL surgery and those who did not, while fastball velocity did not differ.
NUMBERS: n = 305 MiLB pitchers, ~4.5 yr follow-up. Elbow varus torque 94.3 +/- 16.1 N-m (no surgery) vs 100.8 +/- 18.1 N-m (later UCL surgery), p = .049. HR 1.26 per 10 N-m (95% CI 1.01-1.56). Fastball velocity 84.7 +/- 3.6 vs 85.0 +/- 3.0 mph, p = .604.
POPULATION: MiLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL (prospective observational)
SOURCE: Fleisig GS et al. (2025), OJSM, PMC12227930
COACHING: Velocity is not the risk factor. Torque is. BUT the CI lower bound is 1.01 and the distributions overlap heavily — a 6.5 N-m group difference against SDs of 16-18 N-m means torque is a real POPULATION risk factor and a WEAK INDIVIDUAL predictor.
CONFIDENCE: high for the finding, low for individual prediction
SEE ALSO: F-093, F-094, F-097

### F-096 | The elbow and shoulder are one system — shoulder IR torque explains ~85% of elbow valgus torque variance
TOPIC: kinetics, shoulder IR torque, elbow valgus, coupling, sleeve, load management
CLAIM: Shoulder internal-rotation torque is the strongest single correlate of elbow valgus torque once subject weight and height are controlled.
NUMBERS: ~85% of variance; professional shoulder IR torque 4.9-5.2 %BW x BH ~ 87-92 N-m for a 94.7 kg / 1.897 m athlete
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Werner SL et al., "Correlation of Throwing Mechanics With Elbow Valgus Load in Adult Baseball Pitchers"
COACHING: You cannot meaningfully reduce elbow varus torque without addressing what is driving shoulder IR torque. Sleeve-based "elbow stress" management that ignores the shoulder is treating a symptom.
CONFIDENCE: medium — source is a repository copy, not a verified journal record
SEE ALSO: F-091, F-193

### F-097 | The UCL runs with essentially no safety margin — and the failure arithmetic is unreliable
TOPIC: injury, UCL, failure load, cadaveric, Morrey, Dillman, safety margin, fatigue
CLAIM: Peak elbow varus torque times the UCL's cadaveric restraint share exceeds cadaveric failure loads, but the comparison is directionally informative and numerically unreliable.
NUMBERS: UCL provides ~54% of the varus restraint at 90 deg elbow flexion (Morrey & An, static, cadaveric, isolated). Cadaveric UCL failure ~32 N-m (Dillman); 34 N-m at mean age 43; 17.1-22.7 N-m in elderly specimens. Naive arithmetic: 95-100 N-m x 54% = 51-54 N-m through the UCL, ~1.6x the ~32 N-m failure load. Even at the conservative 64 N-m estimate, 54% = ~35 N-m, still at or above failure. Modeling attributes roughly one third each to UCL, flexor-pronator mass, and bony articulation.
POPULATION: cadaveric
EVIDENCE: ESTABLISHED (as mechanism)
CAUSALITY: MECHANISM
SOURCE: Morrey & An; Dillman; Fleisig GS et al. (1995), AJSM 23(2):233-239
COACHING: MUST NOT be used to compute a per-pitch failure probability. Inverse dynamics yields a NET joint torque, not ligament load; the 54% figure is static, cadaveric and isolated; elderly cadaveric tissue is not a 22-year-old professional ligament. What it DOES mean: the gap is bridged by active flexor-pronator load-sharing and tissue adaptation, and FATIGUE REMOVES THE BRIDGE.
CONFIDENCE: high for the qualitative claim, low for the arithmetic. The fatigue mechanism is explicitly labeled INFERENCE, not a measured finding.
SEE ALSO: F-095, F-125, F-128, F-129

### F-098 | Shoulder deceleration is a FORCE problem, not a torque problem
TOPIC: kinetics, shoulder, distraction force, deceleration, posterior cuff, %BW, follow-through
CLAIM: The largest forces of the delivery occur at or just after ball release, with distraction approaching or exceeding body weight in a 30-50 ms window.
NUMBERS: professional shoulder proximal (distraction) force 113.9-114.2 %BW; HS (off-population) 81.6-88.8 %BW; pooled literature range 90-108 %BW; youth 214.7 +/- 47.2 N (49.8 +/- 8.3 %BW). Elbow proximal force in professionals 112.1-112.4 %BW; shoulder anterior force 42.1-42.4 %BW. For a 95 kg (932 N) professional: shoulder distraction ~1,060 N, ~1.14x body weight, in ~30-50 ms, ~100 times per outing. Compressive joint loads during deceleration exceed 1,000 N.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Escamilla RF, Fleisig GS, et al. (2023), PMC10601404
COACHING: The deceleration phase is the least-trained phase in most programs. The posterior cuff and scapular stabilizers are the tissue at risk. Diffuse ache in follow-through is a deceleration-capacity gap — it gets programmed, not rested.
CONFIDENCE: high
SEE ALSO: F-097, F-125, F-140

### F-099 | The velocity-vs-torque conflict table
TOPIC: kinetics, conflict, velocity, elbow torque, trade-off, exchange rate, coaching decision
CLAIM: Some mechanical variables buy velocity and charge torque; a few do neither; one is a win-win; and velocity itself is an unavoidable price.
NUMBERS: TORQUE UP + VELOCITY UP (direct conflict): elbow extension velocity (velocity beta = 0.176); max knee extension velocity (velocity r ~ 0.25); trunk lateral tilt at BR. TORQUE NEUTRAL + VELOCITY UP: stride length (velocity beta = 0.334) — but see F-043/F-044/F-045, it is a marker not a lever. WIN-WIN: later pelvis peak (enables trunk velocity, lowers normalized torque). FREE REDUCTIONS (torque up, no velocity benefit): shoulder abduction at FC, elbow flexion at FC, low shoulder abduction at BR. FAVORABLE IN PROS ONLY: lower arm slot. UNAVOIDABLE: ball velocity itself (within-athlete R2 = .957). RARE APPARENT WIN-WIN, DO NOT ACT ON: max shoulder ER (velocity beta = 0.333, LOWER normalized torque) — see F-102.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: biomechanics.md 6.3; Fleisig 2025 n = 523; professional velocity model n = 337
COACHING: Rule 1 of the coaching playbook: no velocity cue without its stress cost.
CONFIDENCE: medium — all cross-sectional, from a model explaining 40% of torque variance
SEE ALSO: F-093, F-100, F-101, F-102

### F-100 | The four "free" torque reductions — best-supported hypotheses, not proven interventions
TOPIC: kinetics, free reduction, elbow torque, shoulder abduction, elbow flexion, pelvis timing
CLAIM: Four variables raise normalized elbow varus torque without contributing to velocity in the two elite regressions.
NUMBERS: (1) REDUCE shoulder abduction at FC — pro norm 82-85 deg (ranges pool 78-95). (2) REDUCE elbow flexion at FC — pro norm 93-101 deg. (3) INCREASE shoulder abduction at BR — pro norm 84-95 deg. (4) LATER pelvis peak relative to the trunk — the only clear win-win. All from a model explaining 40% of normalized-torque variance; 60% unexplained. Positive torque contributors also include ball velocity (strongest), max knee extension velocity, max elbow extension velocity, trunk contralateral tilt at BR. Negative contributors also include max shoulder ER, upper trunk tilt at FC, shoulder ER at FC.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), OJSM, PMC11789100
COACHING: NO study has shown that changing these in an individual reduces his torque or his injury rate. "Free" is a property of a regression coefficient, not of a bullpen — and in a real athlete these variables covary. The coach's ranking of real-world modifiability: shoulder abduction at FC is MOST modifiable (a position at a landmark, in the stride phase, with a felt cue); later pelvis peak only via upstream causes (lead-hip IR, thoracic rotation, landing foot angle); shoulder abduction at BR barely (inside the 30-50 ms window, and the only route is trunk lateral tilt, itself a positive torque contributor — likely a wash); elbow flexion at FC least (it is arm path, not a dial).
CONFIDENCE: medium — the closest thing to a free lunch, and entirely untested
SEE ALSO: F-099, F-101, F-118

### F-101 | 60% of normalized elbow torque variance is unexplained by kinematics
TOPIC: kinetics, unexplained variance, model, limits, anthropometry, tissue quality
CLAIM: The best available kinematic model of normalized elbow varus torque leaves the majority of variance unexplained.
NUMBERS: 11 kinematic parameters explain 40% of normalized torque variance; n = 523 (425 pro, 98 D1)
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), OJSM, PMC11789100
COACHING: Much of the unexplained 60% is likely anthropometry and tissue quality that kinematics cannot see. Until somebody knows what is in there, every mechanics-based stress claim is a claim about the minority of the problem.
CONFIDENCE: high
SEE ALSO: F-093, F-100

### F-102 | CAUTION — higher max shoulder ER associates with LOWER normalized torque, and should not be acted on
TOPIC: kinetics, MER, layback, external rotation, composite angle, conflict, caution
CLAIM: Higher apparent maximum shoulder external rotation associates with lower normalized elbow torque in the multivariate model, which is counterintuitive and may be an artifact.
NUMBERS: velocity beta = 0.333 (positive predictor) AND a negative contributor to normalized elbow torque, in a model explaining 40% of torque variance
POPULATION: professional_mixed
EVIDENCE: EMERGING (contested)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), PMC11789100; velocity model PMC11322935
COACHING: DO NOT coach "more layback." MER is a COMPOSITE angle (F-134) — pitchers achieving high apparent MER may be distributing lay-back across the thoracic spine and scapula rather than loading the anterior GH capsule and the UCL. That is a hypothesis. It is also possible this is a statistical artifact of the multivariate model.
CONFIDENCE: low — flagged in the corpus as a finding not to act on aggressively
SEE ALSO: F-099, F-134, F-229

### F-103 | Biomechanical efficiency, formalized
TOPIC: kinetics, efficiency, Crotin, velocity per torque, metric, professional, collegiate
CLAIM: Biomechanical efficiency has been formalized as fastball velocity per unit of normalized elbow varus torque.
NUMBERS: n = 545 (447 professional, 98 collegiate)
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Crotin RL, Slowik JS, Brewer G, Cain EL, Fleisig GS (2022), AJSM 50(12):3374-3380
COACHING: The coachable target is not "throw harder with less stress." It is "become the kind of arm that converts effort into velocity efficiently, then apply effort." Whether an individual's efficiency ratio can be moved is unproven and is Dispute 3.
CONFIDENCE: medium — a real, measurable, varying quantity; no longitudinal within-athlete data is public
SEE ALSO: F-093, F-094

### F-104 | Arm-slot torque effects are level-dependent and invert at high school
TOPIC: arm slot, torque, level dependence, high school, professional, inversion
CLAIM: In professionals, lower slot associates with lower elbow varus and shoulder IR torque; in high schoolers the relationship runs the other way for elbow flexion torque.
NUMBERS: professionals -0.1 %BW x BH per +10 deg in both elbow varus (beta = -0.22, p < .001) and shoulder IR (beta = -0.20, p < .001); high schoolers beta = +0.28, p = .002 for elbow flexion torque
POPULATION: professional_mixed vs off_population_HS
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Escamilla RF, Fleisig GS, et al. (2023), PMC10601404
COACHING: Our population's floor (85 mph HS prospect) sits astride that inversion and we do not know which side of it he is on. Another reason not to import HS findings into an elite model.
CONFIDENCE: medium
SEE ALSO: F-070, F-071

---

# 6 — THE KINEMATIC SEQUENCE

### F-105 | REFUTED — the textbook proximal-to-distal sequence is essentially never observed
TOPIC: kinematic sequence, proximal to distal, 1-2-3-4-5, refuted, folklore, variability
CLAIM: The textbook pelvis-trunk-arm-forearm-hand ordering was never achieved on any pitch in the study that looked, and each pitcher used multiple sequences within a single session.
NUMBERS: n = 14 (4 HS, 8 collegiate, 2 professional), 60 fastballs + 71 curveballs. Textbook 1-2-3-4-5 NEVER achieved. Closest observed pattern 1-2-3-4-4 (forearm and hand peaking simultaneously). 8 distinct sequences on fastballs, 11 on curveballs. 43% of fastballs showed altered distal upper-extremity sequencing. Each pitcher averaged 2.7 different sequences across 5-6 throws; no pitcher used only one. No significant difference in sequence variability between fastball and curveball (p = 0.67).
POPULATION: unspecified (mixed levels)
EVIDENCE: EMERGING (individually) / ESTABLISHED (with F-106)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Frontiers in Sports and Active Living (2021), 3:699251, PMC8459924
COACHING: "Fix your kinematic sequence" as a discrete binary intervention is RETIRED. Sequence is not a stable trait you either have or don't. The proximal end (pelvis -> trunk) is far more consistent than the distal end — nearly all observed disorder was in the arm/forearm/hand ordering.
CONFIDENCE: medium alone (n = 14); high in combination with F-106
SEE ALSO: F-106, F-107, F-108

### F-106 | REPLICATED — 14 sequence patterns in 22 pitchers, and sequence variability is not a skill marker
TOPIC: kinematic sequence, replication, patterns, skill marker, high school, professional
CLAIM: Two larger independent samples replicate the sequence-variability finding, and sequence variability was similar in high-school pitchers and professionals.
NUMBERS: n = 22 pitchers, 208 pitches, 14 distinct sequence patterns, NOT ONE fully proximal-to-distal; fewer than 10% of pitchers used a single pattern; variability similar in HS and pro. A further sample: 30 pitchers, 249 fastballs, 17 patterns. Across three labs: ~50 pitchers, 600+ pitches, same result.
POPULATION: mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Scarborough DM, et al. (2020), Sports Biomechanics 19(5)
COACHING: Because variability is the same in HS and pro, sequence order is not even a skill marker. This is the replication that forced the coach to CONCEDE Dispute 11 on 2026-08-12.
CONFIDENCE: high — three independent samples
SEE ALSO: F-105, F-107

### F-107 | The ONE supported sequence fault — trunk before pelvis ("flying open")
TOPIC: kinematic sequence, flying open, trunk before pelvis, torque, fault, coachable
CLAIM: Joint torques increase when the trunk reaches peak rotational velocity BEFORE the pelvis.
NUMBERS: effect sizes not recorded in the corpus. Related: pitchers with proper pelvis-then-trunk sequencing showed DECREASED shoulder proximal force AND decreased shoulder external rotation angle vs improper sequencing (HS sample).
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Aguinaldo A & Escamilla R (2019); Oyama et al. (HS sample)
COACHING: This is the ONE well-supported sequence fault. Distal (arm/forearm/hand) ordering variation is normal and scoring it as a defect INVENTS a problem. The coachable claim narrows to "don't let your chest beat your hips to foot strike" — one specific, upstream, screenable failure.
CONFIDENCE: high for the direction
SEE ALSO: F-105, F-106, F-108, F-118

### F-108 | Later pelvis peak lowers normalized torque AND enables trunk velocity — the only clean win-win
TOPIC: kinematic sequence, pelvis timing, torque, win-win, sequencing, percent pitch time
CLAIM: A later pelvis peak relative to the trunk associates with lower normalized elbow torque and enables trunk velocity.
NUMBERS: percent time of maximum pelvic rotation velocity was a negative contributor to the normalized-torque regression (n = 523); it was the one parameter of eleven that did NOT differentiate the high- and low-torque groups on univariate testing
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Fleisig GS et al. (2025), OJSM, PMC11789100
COACHING: Not modifiable as a timing instruction — nobody can feel 15 ms. Modifiable only through upstream causes: lead-hip IR availability, thoracic rotation, front-foot landing angle.
CONFIDENCE: medium — one univariate inconsistency inside the multivariate result
SEE ALSO: F-099, F-100, F-107

### F-109 | Skill is not less variability — it is better-STRUCTURED variability (a VELOCITY finding, not command)
TOPIC: variability, uncontrolled manifold, UCM, synergy index, velocity, release point, Bloebaum
CLAIM: Higher-velocity pitchers show both lower absolute joint variability AND a higher uncontrolled-manifold synergy index, with variability confined to directions that do not move the release point.
NUMBERS: 43,650 game-speed pitches, 4,338 athlete-sessions, 2,052 pitchers, median 9 trials/session, markerless capture; 15 throwing-side joint angles from peak knee height to ball release. Synergy index partial rho = 0.22, p < 10^-47 at release, and the index SURGES at ball release. Joint-angle SD does NOT decline monotonically toward release — convergence is SEGMENT-STAGGERED: trunk/pelvis reach their variability minimum BEFORE foot plant, the shoulder only at MER. Proportional funnel depth is INVARIANT across skill levels — higher-velocity pitchers have a lower absolute variability floor, not a different convergence shape. Trunk degrees of freedom carry only ~5% of release-preserving variance. Reproduced on the public OpenBiomechanics marker-based cohort; all velocity associations survived athlete-level mixed models.
POPULATION: professional_mixed (youth -> pro)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Bloebaum A (Driveline), SportRxiv preprint 1010, doi 10.51224/SportRxiv.1010; method from Scholz JP & Schoner G (1999), Exp Brain Res 126(3):289-306, PMID 10382616
COACHING: CORRECTED 2026-08-13. rho = 0.22 is an association with PITCH VELOCITY, not with command. The paper contains NO accuracy or location measure. The release point appears in the methods as the PERFORMANCE VARIABLE BEING PROTECTED, not as an outcome being predicted — which is why the misreading is easy. If a future cycle encounters the old "skilled pitchers / command" framing, it is this error propagating. DO NOT RE-IMPORT.
CONFIDENCE: medium — preprint, Driveline analyzing its own athletes with its own pipeline, rho = 0.22 is modest; but the sample is an order of magnitude beyond anything else and the method is well established outside baseball
SEE ALSO: F-139, F-140, F-110, F-240

### F-110 | Elite throwers reproduce their own nonlinear signature more consistently — at the pelvis and trunk
TOPIC: variability, complexity, reproducibility, pelvis, trunk, Bernstein, markerless
CLAIM: Elite throwers do not have simpler or more complex joint trajectories on average; they reproduce their own nonlinear signature more consistently trial to trial, with the strongest signal at the pelvis and trunk rather than the throwing arm.
NUMBERS: 28,307 game-speed fastballs, 1,722 athletes, 3,713 athlete-sessions (youth -> pro), markerless at 300 Hz, 8-camera Edgertronic SC1 array -> Theia3D -> Visual3D. EFFECT SIZES UNVERIFIED — the full PDF was not opened.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Bloebaum A (Driveline), SportRxiv preprint 919, 8 Jun 2026
COACHING: Converges from a third independent direction with "stable proximal base, adaptive arm chain." Operationalizes Bernstein's "repetition without repetition."
CONFIDENCE: low-medium — preprint, effect sizes unverified, Driveline analyzing Driveline athletes
SEE ALSO: F-109, F-140, F-242

### F-111 | UNVERIFIED SAMPLE — the energy-transfer preprint whose n was manufactured by a search engine
TOPIC: energy transfer, preprint, unverified, sample size, hazard, Bloebaum
CLAIM: Pitch velocity and elbow loading are argued to be dominated by energy TRANSFERRED into the arm rather than generated locally at the shoulder or elbow.
NUMBERS: SAMPLE SIZE COULD NOT BE VERIFIED. A search summary attributed the 43,650-pitch / 2,052-pitcher sample from a DIFFERENT preprint (1010) onto this one. Do not cite any n for this paper without opening the PDF.
POPULATION: unspecified
EVIDENCE: UNSOURCED (for the sample size)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Bloebaum A (Driveline), SportRxiv DOI 10.51224/SportRxiv.871, 19 May 2026
COACHING: The claim itself is consistent with F-064, F-065 and F-067, so the conclusion is unsurprising even if the sample is unverified. The hazard is the point — see F-237.
CONFIDENCE: low
SEE ALSO: F-237, F-242, F-067

---

# 7 — ANATOMY AND ADAPTED TISSUE STATE

### F-112 | The arm is the last, smallest and most fragile link, and at 85+ it is already the binding constraint
TOPIC: anatomy, kinetic chain, ligament, adaptation, organizing principle
CLAIM: Ligaments do not hypertrophy the way muscle does; everything upstream exists to reduce demand on tissue whose strength ceiling is essentially fixed.
NUMBERS: shoulder internal rotation angular velocity at release on the order of 7,000-7,500 deg/s in adult pitchers
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 1.2; Fleisig et al. (1995/1999)
COACHING: You cannot strengthen your way past a bad sequence, and at this velocity band you cannot outlast a bad one either.
CONFIDENCE: high — the specific 7,000-7,500 deg/s numeral is flagged in the corpus as widely reproduced but not verified at primary source in that session
SEE ALSO: F-090, F-113, F-127

### F-113 | The UCL survives only because muscle and bone shield it — roughly a third each
TOPIC: anatomy, UCL, flexor-pronator, load sharing, stress shielding, radiocapitellar, elite specific
CLAIM: Peak valgus load in adult pitching far exceeds the isolated UCL's cadaveric tensile capacity; the load is shared between the ligament, the flexor-pronator mass and the bony articulation.
NUMBERS: peak elbow varus torque ~100 N-m; modeling attributes roughly one third each to UCL anterior bundle, flexor-pronator mass (FCU primary, FDS secondary, pronator teres contributory), and radiocapitellar/osseous articulation under compression. Order of arrival: osseous compression is passive and instantaneous; flexor-pronator EMG rises FROM cocking THROUGH acceleration, i.e. ramping into the peak; the UCL takes what is left, and takes it last.
POPULATION: professional_mixed / cadaveric
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Fleisig GS et al. (1995), AJSM 23(2):233-239; anatomy-physiology.md 1.3, 2.9
COACHING: "Your ligament is the backup. Your forearm is the starter. When the forearm is tired, the ligament plays the whole inning." This is the entire physiological justification for arm care in this population.
CONFIDENCE: high
SEE ALSO: F-097, F-114, F-125

### F-114 | Grip pressure literally narrows the medial elbow under valgus load
TOPIC: anatomy, grip, FDS, FCU, flexor-pronator, stress shielding, valgus, ultrasound, elastography
CLAIM: FCU and FDS are dynamic valgus stabilizers, and index/middle-finger FDS contraction measurably reduces medial joint gapping under valgus stress.
NUMBERS: EMG activity rises from cocking through acceleration; medial elbow musculature provides measurable stress shielding of the UCL in competitive pitchers (MSSE varus-strength work); ultrasound and shear-wave elastography evidence for grip narrowing the medial joint
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (mechanism) / EMERGING (whether targeted training reduces UCL injury incidence)
CAUSALITY: MECHANISM
SOURCE: JBJS "Dynamic Contributions of the Flexor-Pronator Mass to Elbow Valgus Stability"; MSSE varus-strength work; PMC7110663; PMC11863580
COACHING: "Grip is arm care." How hard he holds the baseball is the one voluntary act inside the last 150 ms that changes the load-sharing. The outcome trial does not exist — coach this off mechanism and say so.
CONFIDENCE: high for the mechanism, zero for the injury-incidence outcome
SEE ALSO: F-013, F-113, F-125

### F-115 | Humeral retrotorsion is laid down in adolescence and locked at skeletal maturity
TOPIC: anatomy, humeral retrotorsion, retroversion, GIRD, bone, ROM, ceiling, adolescence
CLAIM: The humeral shaft torsionally remodels during skeletal growth under repetitive high-torque throwing, shifting the entire rotational arc posteriorly with no soft-tissue pathology whatsoever.
NUMBERS: dominant-arm retrotorsion in throwers commonly exceeds the non-dominant side by roughly 10-15 deg; remodeling occurs while the proximal humeral physis is open, roughly ages 8-16, greatest in early adolescence, essentially locked at skeletal maturity. Professional pitchers with GIRD show greater humeral retrotorsion than those without.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 4.1; Ruotolo/Crockett line of work, PMC3763355; handedness differences Harris J et al. (2022), AJSM
COACHING: "Stretch out his GIRD" is FOLKLORE when the deficit is osseous — and in this population much of it is. Attempting to stretch a 23-year-old's internal rotation toward a normative number is attempting to remodel bone with a towel, and the tissue that actually yields is the anterior capsule you did not want to lengthen. Retrotorsion is also plausibly the most under-appreciated CEILING determinant in the sport (it enables the elastic loading in F-064).
CONFIDENCE: high
SEE ALSO: F-116, F-064, F-134

### F-116 | Total rotational motion beats GIRD, and preseason ROM screening is a weak predictor
TOPIC: anatomy, GIRD, total rotational motion, TRM, ROM screening, injury risk, professional
CLAIM: A total-rotational-motion deficit carried a significant injury association in professional pitchers where GIRD alone did not, and subsequent meta-analyses conflict.
NUMBERS: n = 122 professional pitchers over 5 seasons — TRM deficit > 5 deg carried ~2.5x shoulder injury risk; GIRD carried ~1.9x odds but did NOT reach significance (P = .17). A 2018 Sports Health systematic review/meta-analysis found GIRD associated with elevated upper-extremity injury risk in overhead athletes. A separate systematic review/meta-analysis of preseason ROM screening across 17 studies failed to reach statistical significance for ANY shoulder motion measurement as an in-season predictor.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (as a finding) / EMERGING (the specific 5 deg threshold)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wilk KE, Macrina LC, Fleisig GS, et al. (2011), AJSM 39(2):329-335, PMID 21131681; Sports Health (2018) meta-analysis; PMC7456673
COACHING: Preseason ROM screening is a weak POPULATION-level predictor and is NOT a pass/fail gate. TRM asymmetry is more defensible than raw GIRD because it partially controls for the osseous contribution: IR lost AND ER gained equally = the arc rotated (likely bone); IR lost WITHOUT an ER gain = the arc shrank (more likely soft tissue). The real value of ROM measurement is longitudinal and individual, not cross-sectional and normative. "Every pitcher needs X degrees of internal rotation" is FOLKLORE — no validated universal threshold exists.
CONFIDENCE: medium — most injured pitchers do not have GIRD, and many with GIRD never get hurt
SEE ALSO: F-115, F-117, F-129

### F-117 | Internal rotation loss has three different tissue sources producing one clinical number
TOPIC: anatomy, capsule, posterior capsule, retroversion, pennation, ROM, interpretation
CLAIM: Internal rotation loss in professional pitchers has independent contributions from humeral retroversion, posterior capsule thickness, and posterior rotator cuff pennation angle.
NUMBERS: three independent contributors identified in a professional cohort
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: JSES Int (2022), professional cohort
COACHING: This is why a single ROM measurement cannot tell you what to do. Also established: posteroinferior capsular thickening is measurable by ultrasound; a stiff posteroinferior capsule produces obligate anterosuperior humeral head translation in flexion/adduction/IR (cadaveric). Whether that translation or the peel-back mechanism is the operative SLAP pathway in living elite throwers is EMERGING — both are widely taught, neither is proven dominant.
CONFIDENCE: high for the three-source finding
SEE ALSO: F-115, F-116, F-122

### F-118 | Acquired anterior capsular laxity is part of how the athlete reaches 90+
TOPIC: anatomy, anterior capsule, IGHL, laxity, layback, external rotation, adaptation
CLAIM: Years of repetitive maximal external rotation produce plastic deformation of the anterior band of the inferior glenohumeral ligament.
NUMBERS: assume it has occurred to some degree in any 85+ arm
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 4.3
COACHING: More MER can come from thoracic extension and scapular posterior tilt (adaptable, cheap) or from the anterior capsule (already-deformed tissue, expensive). THE ANGLE LOOKS IDENTICAL ON VIDEO. "I never want more layback. I want more room to lay back into — that's your mid-back and your shoulder blade, not your shoulder." Never stretch a lax elite arm into more ER.
CONFIDENCE: high
SEE ALSO: F-115, F-102, F-119, F-134

### F-119 | Laxity is not instability, and in this population laxity is frequently an asset
TOPIC: anatomy, laxity, instability, microinstability, screening, elite specific
CLAIM: Laxity is a sign (quantity of passive translation available); instability is a symptom plus a sign (translation producing pain, apprehension or dysfunction).
NUMBERS: —
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 4.5
COACHING: "He's loose, that's a red flag" is FOLKLORE. Many high-level throwers are lax and rely on exceptional dynamic control. Aggressively stretching an already-lax elite thrower converts an asset into a problem. Microinstability — small increments of anterior translation at MER driving the internal-impingement/SLAP cascade — is EMERGING: widely taught, mechanistically plausible, hard to measure in vivo.
CONFIDENCE: high
SEE ALSO: F-118, F-122

### F-120 | "Abnormal" imaging is the baseline in asymptomatic elite throwers
TOPIC: anatomy, imaging, MRI, ultrasound, asymptomatic, labrum, elite specific, screening
CLAIM: Asymptomatic professional pitchers carry imaging findings that would be called pathology in anyone else, and those findings do not predict future injury-list placement.
NUMBERS: labrum abnormal in ~79% of asymptomatic professional throwing shoulders (55% signal change, 45% frank tear), with no significant supraspinatus/infraspinatus differences between sides. In one cohort of asymptomatic professionals: rotator cuff pathology ~94%, labral tears ~76%, Bennett lesions ~52%. High-resolution 3-T MRI in non-symptomatic professional draft picks shows frequent abnormalities of cuff tendons, coracohumeral and inferior glenohumeral ligaments, labrum and osseous structures. Glenohumeral MRI findings CORRELATE WITH INNINGS PITCHED in asymptomatic pitchers. MRI findings of the asymptomatic shoulder may impact performance but did NOT predict future injured-list placement in MLB pitchers. Elbow MRI findings do NOT correlate with future disabled-list placement in asymptomatic professional pitchers.
POPULATION: professional_mixed / MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Miniaci A et al. (2002), AJSM, PMID 11798999; AJSM (2015) 3-T draft picks, PMID 26529676; PMID 31300356; PMID 23775245; Arthrosc Sports Med Rehabil (2022), PMC9042760; Wilcox et al. (2017), PMID 28394713
COACHING: A scan cannot CLEAR or CONDEMN an asymptomatic elite arm. "His MRI is ugly, so he's hurt" and "his MRI is clean, so he's fine" are BOTH wrong here. Symptoms, strength, ROM trajectory and performance are the operative signals. The image is context.
CONFIDENCE: high
SEE ALSO: F-121, F-129

### F-121 | The elite UCL is a partially remodeled, scarred, load-adapted structure
TOPIC: anatomy, UCL, ultrasound, remodeling, calcification, asymptomatic, professional
CLAIM: Ultrasound in asymptomatic professional pitchers shows large dominant-arm differences in hypoechoic foci and calcification, and MRI shows scar remodeling of the anterior bundle.
NUMBERS: n = 368 asymptomatic professional pitchers, 10-year stress sonography study — dominant-arm hypoechoic foci 28.0% vs 3.5%; calcifications 24.9% vs 1.6%. Of a 26-pitcher MRI subset, 13 showed scar remodeling of the anterior bundle of the UCL.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Atanda A et al. (2014), PMID 24473498
COACHING: Assume damage history in any 85+ arm with years of mileage. The question is not "is it damaged" but "is the rate of damage exceeding the rate of repair."
CONFIDENCE: high
SEE ALSO: F-120, F-113, F-153

### F-122 | Scapular dyskinesis is prevalent in ASYMPTOMATIC elite throwers and is not a reliable predictor
TOPIC: anatomy, scapular dyskinesis, winging, screening, consensus, asymptomatic
CLAIM: Scapular dyskinesis is highly prevalent in shoulder-injured populations AND in asymptomatic professional and collegiate baseball players — a majority in some series.
NUMBERS: majority prevalence in asymptomatic pros in some series
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Kibler WB, Ludewig PM, McClure PW, Michener LA, Bak K, Sciascia AD (2013), "Scapular Summit" consensus, BJSM 47(14):877-885, PMID 23580420
COACHING: "His scap wings, so he's going to get hurt" is FOLKLORE. The consensus statement's own words: "the exact role of the dyskinesis in creating or exacerbating shoulder dysfunction is not clearly defined." Treat it as an impairment/modifier, not a diagnosis. Also: the dominant scapula in throwers normally sits slightly LOWER and more PROTRACTED — asymmetry alone is not pathology. REFER if dyskinesis is new, unilateral, dramatic and accompanied by weakness — true winging can be neurologic.
CONFIDENCE: high
SEE ALSO: F-123, F-120

### F-123 | Periscapular strength is a depleting resource across a season
TOPIC: anatomy, periscapular, scapula, in season, strength decline, scaption, collegiate
CLAIM: In collegiate pitchers tracked pre-, mid- and post-season, all measured periscapular strength values declined.
NUMBERS: decline range 3-14%; scaption strength down a statistically significant ~8% over the season, including a 5% drop from mid- to post-season
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED (for collegiate pitchers)
CAUSALITY: CROSS_SECTIONAL
SOURCE: IJSPT (2024), collegiate cohort, PMC11144669
COACHING: Scapular capacity is a depleting resource across a season, not a fixed trait. In-season maintenance work is not optional for an 85+ arm. IMPORTANT: this 3-14% figure is REAL — but do NOT attribute it to Wilkin & Haddock, which is a different paper reporting no significant change (F-215).
CONFIDENCE: high
SEE ALSO: F-083, F-215, F-132

### F-124 | Elite-specific soft-tissue injuries: oblique and lat/teres major strains
TOPIC: anatomy, oblique strain, latissimus dorsi, teres major, elite specific, time loss, refer
CLAIM: Oblique strains and latissimus dorsi / teres major strains are signature professional and collegiate baseball injuries, essentially absent from general-population sports medicine.
NUMBERS: oblique strain disproportionately affects pitchers and disproportionately the LEAD/non-throwing side — the side that lengthens eccentrically at MER then contracts violently; time loss measured in weeks; meaningful re-injury rates. Lat/teres presents as posterior axillary or lateral chest-wall pain, often with ABRUPT VELOCITY LOSS.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 2.5, 2.6
COACHING: REFER for any sudden sharp lateral trunk pain, especially with a reported "pop," and for posterior axillary pain with abrupt velocity loss.
CONFIDENCE: high
SEE ALSO: F-129, F-130

### F-125 | Fatigue neurally DISCONNECTS the primary deceleration muscle
TOPIC: fatigue, infraspinatus, voluntary activation, central inhibition, deceleration, elite specific
CLAIM: After a simulated game, pitchers show a voluntary activation deficit of the infraspinatus measured by interpolated twitch — a central neural inhibition, independent of the muscle's own condition.
NUMBERS: contractile strength loss after a SINGLE game in asymptomatic pitchers: ~11% external rotation, ~15% flexion, ~18% internal rotation, ~11% adduction versus pre-game
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: PMC3910170, "Voluntary activation deficits of the infraspinatus present as a consequence of pitching-induced fatigue"
COACHING: The primary deceleration muscle is neurally inhibited exactly when the arm most needs it. One of the single most important findings in the pitching literature, and specific to pitching-induced fatigue. NOTE: because the deficit is CENTRAL, any field test requiring a maximal voluntary contraction measures the same inhibited system with a cruder instrument — see F-131.
CONFIDENCE: high
SEE ALSO: F-126, F-127, F-131

### F-126 | ROM is measurably still depressed 24 hours after an outing
TOPIC: fatigue, ROM, recovery, internal rotation, elbow extension, 24 hours, between start
CLAIM: Significant acute decreases in shoulder internal rotation, total rotational motion and elbow extension occur immediately after pitching and PERSIST at 24 hours.
NUMBERS: documented both after a single game and across a season in collegiate starting pitchers
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Reuter et al. / collegiate ROM work, PMID 24565823
COACHING: The arm is measurably not back to baseline a day later. That is the physiological basis for a structured between-start map, and it means a "baseline" taken on a random Tuesday in a dense stretch is not a baseline.
CONFIDENCE: high
SEE ALSO: F-125, F-127, F-156

### F-127 | The fatigue hierarchy — command drifts first, velocity goes LAST
TOPIC: fatigue, command drift, velocity, pull decision, observation, hierarchy, outing
CLAIM: Coach-observable fatigue signs appear in a consistent order, with velocity as the final indicator.
NUMBERS: order — command drift (arm-side misses, elevated fastballs) -> loss of breaking-ball depth/finish -> visible slot drop -> longer time between pitches -> VELOCITY DECLINE LAST. Pitch-count phases: 1-25 PCr near-full each pitch, kinematics stable, cuff activation intact. 25-60 incremental strength and activation loss begins, athlete compensates with intent, velocity often holds — the deceptive window. 60-90 posterior cuff voluntary activation drops, hip-shoulder separation narrows, command degrades before velocity, kinetics per pitch stay high or rise relative to velocity. 90+ the passive restraints (UCL, labrum, capsule) absorb a larger share of load.
POPULATION: professional_mixed
EVIDENCE: EMERGING (as a formal hierarchy) / ESTABLISHED (that command and secondaries degrade first)
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 3.3
COACHING: "Velocity's still there, so he's not tired" is BACKWARDS. Pull decisions keyed to the radar gun are keyed to the final signal.
CONFIDENCE: medium-high
SEE ALSO: F-125, F-126, F-131

### F-128 | Kinematic drift under fatigue — load per unit of output RISES
TOPIC: fatigue, kinematics, drift, kinetics, load, hip shoulder separation, arm slot
CLAIM: With fatigue, measured kinematics change and joint kinetics do NOT fall proportionally with velocity.
NUMBERS: reduced hip-shoulder separation, altered trunk position, lower arm slot; kinetics per pitch stay high or rise relative to velocity
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 3.2
COACHING: Late in an outing the passive structures carry a larger share of an undiminished load. This is the mechanistic case for why fatigue is the dominant modifiable risk variable.
CONFIDENCE: high
SEE ALSO: F-097, F-125, F-127

### F-129 | "Dead arm" is three physiologically distinct states, and the distinction is high-value
TOPIC: dead arm, fatigue, differential, refer, neurovascular, microinstability, decision rule
CLAIM: "Dead arm" is a symptom description covering at least three distinct states requiring different responses.
NUMBERS: —
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (as phenomenon) / EMERGING (as a defined entity)
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 3.5
COACHING: (a) PHYSIOLOGIC — activation deficits, residual strength loss, unresolved ROM deficits. NO localized pain, no night pain, no neurological symptom; ROM symmetric-to-baseline without a hard or painful end-feel; resolves with load reduction and sleep over days. (b) STRUCTURAL — classically the anterior microinstability -> internal impingement -> labral/cuff cascade; the athlete reports not pain but velocity and command loss, sometimes a clunk at MER. REFER. (c) NEUROVASCULAR — thoracic outlet, quadrilateral space, suprascapular neuropathy. Heaviness PLUS any paresthesia, coldness, color change, swelling, rapid fatigability out of proportion to work, or ER strength loss with visible infraspinatus atrophy. REFER — this category is routinely missed for months in professional pitchers. DECISION RULE: dead arm without pain or neuro symptoms resolving in 2-5 days is (a); dead arm that persists, recurs on schedule, or carries any pain, paresthesia, night symptoms, swelling or atrophy is not a training problem.
CONFIDENCE: high
SEE ALSO: F-125, F-130

### F-130 | Thoracic outlet syndrome — frequently missed, and the return-to-play numbers
TOPIC: anatomy, thoracic outlet, TOS, first rib resection, return to play, MLB, refer
CLAIM: In MLB pitchers undergoing first-rib resection for neurogenic or vascular TOS, most returned to MLB pitching, at roughly ten months post-op.
NUMBERS: ~74-81% returned to MLB pitching, at a mean of ~10 months post-op; average post-op career length ~3 seasons; performance metrics not significantly different from matched controls among those who returned
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Arnold MT, Hart CM, Greig DE, Trikha R, Gelabert HA, Jones KJ (2022), OJSM; 2021 companion work, PMID 33472488
COACHING: Encouraging but sobering — and one of the most frequently missed diagnoses in professional pitching, often carried for months as "dead arm." Venous TOS (arm swelling, cyanosis, prominent superficial veins) is URGENT.
CONFIDENCE: high
SEE ALSO: F-129

### F-131 | GAP — there is no validated dugout-measurable marker of posterior-cuff activation deficit
TOPIC: fatigue, field test, dynamometry, monitoring, gap, posterior cuff, in-game
CLAIM: No validated between-innings field test exists that fires before command drifts.
NUMBERS: three candidates, all inadequate — (1) handheld dynamometry ER strength between innings: HHD is reliable and post-game ER strength drops ~11%, but no between-innings protocol, no minimal detectable change for this use, and the maximal contraction is itself a load; (2) grip dynamometry: $60, 5 seconds, indexes the flexor-pronator load-sharing — but it is a FOREARM marker, not a posterior-cuff marker; (3) slot drop on video: free, but fires AFTER command drift
POPULATION: professional_mixed
EVIDENCE: UNSOURCED (as an absence)
CAUSALITY: CROSS_SECTIONAL
SOURCE: open-disputes.md #5
COACHING: The request may be malformed — if the deficit is CENTRAL voluntary activation, any test requiring a maximal voluntary contraction measures the same inhibited system with a cruder instrument, and will be noisier than the pitcher's own 100-repetition-per-outing performance readout. "The best available marker of a pitcher's arm may just be the pitcher." Formalize the observation ladder (chart arm-side miss rate and breaking-ball finish by inning) rather than chasing a number.
CONFIDENCE: high that the gap exists
SEE ALSO: F-125, F-127

---

# 8 — PHYSIOLOGY, RECOVERY, AND WORKLOAD

### F-132 | Energy systems — pitching is alactic; the aerobic system is the recovery engine
TOPIC: physiology, energy systems, phosphagen, lactate, aerobic, conditioning, PCr, running
CLAIM: The pitch itself is phosphagen-dominant, produces little lactate, and the aerobic system's role is PCr resynthesis between efforts.
NUMBERS: a pitch takes ~1.5-2 s from first movement to follow-through; the high-velocity portion (front-foot strike to release) lasts ~0.05-0.15 s; between pitches ~15-25 s; between innings several minutes. PCr resynthesis: fast phase (~half of PCr) in ~20-30 s, near-complete in ~3-5 min.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 3.1
COACHING: "Distance running builds endurance for starts" is FOLKLORE — the aerobic DEMAND of a start is low; the aerobic RECOVERY function matters, but there is no evidence high-volume slow running develops it best in pitchers, and it competes with power adaptations. "Poles the day after flush lactic acid" is FOLKLORE — there is essentially no lactate to flush, and lactate is a fuel, not a waste product. Cardiac-output and repeat-sprint methods are EMERGING as better-suited.
CONFIDENCE: high for the physiology, emerging for the method recommendation
SEE ALSO: F-042, F-166

### F-133 | Connective tissue is net-catabolic for ~36 hours after loading
TOPIC: recovery, collagen, tendon, ligament, between start, loading, net balance, tendinopathy
CLAIM: After a loading bout, tendon collagen synthesis peaks around 24 h and stays elevated ~72 h, but degradation rises earlier, so net collagen balance is negative to roughly 36 h and positive from ~36-72 h.
NUMBERS: synthesis peaks ~24 h, elevated ~72 h; net balance negative up to ~36 h, net positive ~36-72 h
POPULATION: unspecified (patellar tendon and Achilles in NON-THROWERS)
EVIDENCE: ESTABLISHED (in non-throwing tissue)
CAUSALITY: MECHANISM
SOURCE: Magnusson SP, Langberg H, Kjaer M (2010), Nat Rev Rheumatol 6(5):262-268, PMID 20308995; Kjaer M et al. (2009); Miller BF et al. (2005), J Physiol
COACHING: Repeatedly reloading connective tissue inside the negative-balance window produces net matrix degradation — a mechanistic account of tendinopathy from insufficient rest, and the best physiological argument against stacking high-intent throwing days. CAVEAT STATED PLAINLY: this has NEVER been mapped for the UCL under pitching loads. It is the best available model, not a measurement of your athlete's ligament. Bone remodels resorption-first, creating a transient window of WEAKENED bone after a load increase — the basis for olecranon and rib stress reactions when volume ramps too fast.
CONFIDENCE: high for the tissue biology, unknown for transfer to the UCL
SEE ALSO: F-156, F-134

### F-134 | The 165-180 degree "max external rotation" is a composite, not glenohumeral rotation
TOPIC: anatomy, MER, layback, composite angle, thoracic, scapular, measurement, cue
CLAIM: Apparent MER includes scapulothoracic motion, thoracic extension, trunk hyperextension and elbow/forearm contributions; true glenohumeral external rotation is substantially less.
NUMBERS: 165-180 deg apparent; pro overhand 165 +/- 9 deg, sidearm 168 +/- 10 deg; cross-study bound 166-182 deg
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 3.2; anatomy-physiology.md 2.6, 2.8, 4.1, 4.3
COACHING: NEVER coach a pitcher toward a target MER number — it is a composite output. More MER can come from the thoracic spine and scapula (adaptable, cheap) or from the anterior capsule (already-deformed, expensive), and THE TWO LOOK IDENTICAL ON VIDEO. The coach's stated conclusion: "I will never again coach toward an MER target, and I will never stretch an elite arm into more external rotation."
CONFIDENCE: high — described in the corpus as the single most consequential thing learned on Day 1
SEE ALSO: F-102, F-115, F-118

### F-135 | Lumbar rotation is anatomically limited to ~2 degrees per segment
TOPIC: anatomy, lumbar, rotation, thoracic, hips, compensation, low back
CLAIM: Lumbar facets are sagittally oriented, permitting roughly 2 degrees of axial rotation per segment; rotation is supposed to come from the hips and thoracic spine.
NUMBERS: ~2 deg per segment, ~10-13 deg total
POPULATION: general anatomy
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 2.5 (standard textbook physiology, not cited to a specific paper)
COACHING: When the hips or thoracic spine are restricted, the lumbar spine makes up the difference — a mechanism for facet irritation, pars stress and disc loading. Screen lead-hip IR and seated thoracic rotation before touching the delivery.
CONFIDENCE: high
SEE ALSO: F-107, F-118, F-136

### F-136 | Total high-intent throwing volume is the exposure variable, not game pitch count
TOPIC: workload, pitch count, exposure, bullpens, showcase, ACWR, chronic load, monitoring
CLAIM: Bullpens, flat-ground, long toss, showcase outings, pre-draft workouts and velocity-testing days all load the same tissue, and game-day pitch counts systematically undercount true workload.
NUMBERS: ACWR thresholds — elevated risk above roughly 1.27-1.5, with the under-appreciated finding that LOW CHRONIC WORKLOAD IS ITSELF A RISK STATE. ACWR methodology is genuinely contested in the sports-science literature.
POPULATION: off_population_HS (Zaremski) / NCAA_D1 (preseason workload work)
EVIDENCE: ESTABLISHED (the principle) / EMERGING (the thresholds)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Zaremski JL, Pazik M, Vasilopoulos T, Horodyski M (2024), AJSM; Univ. of Florida unaccounted-workload work; ACWR critique PMC7739681
COACHING: Count pens, flat-ground, long toss, showcases and testing days as load. Treat ACWR thresholds as heuristics, not laws. THE HIGHEST-RISK SINGLE EXPOSURE in this population: a maximal-intent showcase or pro-day outing performed cold, off-schedule, with low chronic load, minimal warm-up and strong incentive to hide fatigue.
CONFIDENCE: high for the principle, low for thresholds
SEE ALSO: F-137, F-156

### F-137 | Elbow varus torque at 120 ft of long toss is similar to pitching off a mound
TOPIC: workload, long toss, interval throwing, distance, elbow varus torque, dosing, ACWR
CLAIM: A large flat-ground throwing dataset modeled distance against peak elbow varus torque and found mound-equivalent load past roughly 120 ft.
NUMBERS: 238,611 flat-ground throws from 34 healthy NCAA D1 pitchers (reported elsewhere in the corpus as 111,196 throws — the corpus is internally inconsistent on this figure and it should be re-verified); second-order polynomial regression of throwing distance to peak elbow varus torque; four published programs (6-week, 12-week, 5-month, 7-month) with 91-100% ACWR compliance in the 0.7-1.3 band using 7-day acute / 28-day chronic windows
POPULATION: NCAA_D1
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL (modeling paper, no injury outcomes)
SOURCE: Reinold MM, Dowling B, Fleisig GS, Macrina LC, Wilk KE, Alexander FJ, Ahmad CS, Dugas J, Andrews JR (2026), IJSPT 21(4):428-439
COACHING: Reclassifies long toss past ~120 ft from "arm care" to mound-equivalent load. It goes in the workload column. Note this is a MODELING paper — 34 athletes, all healthy, no injury outcomes, and ACWR methodology is itself contested.
CONFIDENCE: medium; INTERNAL INCONSISTENCY FLAGGED — the throw count is recorded as both 238,611 and 111,196 in different corpus files
SEE ALSO: F-136, F-231

### F-138 | Sleep is the highest-return, lowest-cost recovery intervention, and the most compromised
TOPIC: recovery, sleep, growth hormone, injury odds, travel, night games, extension
CLAIM: Sleep is when the majority of growth hormone is secreted; restriction impairs reaction time, decision-making and glucose handling; adolescent athletes sleeping under 8 h/night had elevated injury odds.
NUMBERS: ~1.7x the odds of musculoskeletal injury at <8 h/night (adolescent athletes broadly, NOT elite pitchers — directional only). Sleep extension improves performance metrics in small, unblinded studies.
POPULATION: off_population_youth (for the injury odds)
EVIDENCE: ESTABLISHED (mechanism) / EMERGING (extension effect)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Milewski MD et al. (2014), J Pediatr Orthop 34(2):129-133; Mah CD et al. (Stanford extension studies — referenced from secondary summaries, UNVERIFIED at primary source)
COACHING: Target 8-10 h, consistent timing, protected through travel and night games. Elite-specific threats: night games with late arousal, cross-country travel, showcase schedules, and school schedules stacked on evening outings.
CONFIDENCE: high for the mechanism, medium for the injury odds (sample mismatch)
SEE ALSO: F-156, F-176

### F-139 | Recovery-modality audit — what has evidence and what does not
TOPIC: recovery, modalities, cold water immersion, icing, stretching, cryotherapy, NSAIDs, BFR
CLAIM: Most recovery modalities have perceptual effects only; two have documented harms in specific contexts.
NUMBERS: CWI after resistance training ATTENUATES hypertrophy (meta-analysis; small, consistent; strength/power gains blunted in some analyses).
POPULATION: unspecified
EVIDENCE: mixed by modality
CAUSALITY: INTERVENTION
SOURCE: anatomy-physiology.md 6.4; Pinero A et al. (2024), Eur J Sport Sci, PMC11235606
COACHING: ESTABLISHED — sleep (do this first), adequate energy and protein, high-intent load management (the most effective recovery intervention is not overloading in the first place), CWI for the PERCEPTUAL effect. ESTABLISHED HARM — do NOT routinely ice after lifting; use CWI tactically only. EMERGING — structured standardized warm-up (injury-reduction RCT evidence exists but in youth cohorts), active recovery, compression, massage, whole-body cryotherapy, dry needling/cupping/percussion/tape, BFR in rehab (clinician-supervised only), collagen peptide + vitamin C pre-load. FOLKLORE — icing the arm after an outing as a treatment claim; static stretching as injury prevention (a baseball RCT found shoulder strengthening non-inferior/favorable vs stretching); post-outing running to flush lactate. EMERGING CONCERN — routine NSAIDs suppress the inflammatory signaling that drives repair; physician's call, not a clubhouse habit. Sleeper/cross-body stretch to "fix GIRD" — appropriate only for a demonstrated SOFT-TISSUE posterior restriction; assume a large osseous component first.
CONFIDENCE: high for the audit as a whole
SEE ALSO: F-115, F-133, F-138

### F-140 | Protein and fueling targets
TOPIC: recovery, nutrition, protein, carbohydrate, muscle protein synthesis, collagen peptide
CLAIM: Standard protein and fueling targets support lean mass in trained athletes; the "anabolic window" as a narrow requirement is folklore.
NUMBERS: muscle protein synthesis elevated ~24-48 h after resistance exercise; stimulated by ~0.3 g/kg high-quality protein per feeding (~20-40 g, ~2-3 g leucine); ~1.6-2.2 g/kg/day total; distribution across ~3-5 feedings modestly superior to skewed intake. Collagen peptide ~15 g + vitamin C ~30-60 min before loading may raise collagen synthesis markers (EMERGING, unproven for injury prevention in throwers).
POPULATION: unspecified
EVIDENCE: ESTABLISHED (protein dosing) / FOLKLORE (the narrow anabolic window)
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 6.3 — standard textbook physiology, not cited to a specific paper
COACHING: For a starter, carbohydrate availability is a full-week fueling question, not a post-game-shake question.
CONFIDENCE: high for standard sports-nutrition consensus; the specific dose thresholds are not cited to a primary source in the corpus
SEE ALSO: F-002, F-139

### F-141 | UCL injury risk factors — established, emerging, and one piece of folklore
TOPIC: injury, UCL, risk factors, velocity, workload, fatigue, curveball, pitch characteristics
CLAIM: The established UCL risk factors are exposure-based; the emerging ones come from MLB pitch-tracking; and pitch type is not one of them at this level.
NUMBERS: ESTABLISHED — higher pitch velocity; higher workload/volume; pitching while fatigued; pitching with arm pain; year-round throwing with no true off-season; prior arm injury. EMERGING (MLB pitch-tracking): increased fastball, changeup and sinker velocity; increased slider spin rate; increased cutter release extension (n = 115 UCLR pitchers vs 230 matched controls, Apr 2018 - Nov 2023). Four-seam spin rate 100 rpm above league average ~ +20% odds of UCLR; cutter arm-side movement +1 inch above league average ~ +36% odds (MLB 2016-2024).
POPULATION: MLB
EVIDENCE: ESTABLISHED / EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Mastroianni et al. (2025), AJSM, PMID 40230317; Arthroscopy (2025), Baseball Savant data; J ISAKOS (2021) systematic review
COACHING: "Curveballs cause Tommy John" is FOLKLORE for this population — even in youth data it failed to hold. NOTE THE DIRECTION: the pitch characteristics the modern development industry chases are the ones associated with the injury. Case-control -> association, not causation.
CONFIDENCE: medium — association studies with confounding by role and workload
SEE ALSO: F-095, F-179, F-234

---

# 9 — STUFF: PITCH PHYSICS

### F-142 | Spin efficiency is a geometric quantity — only transverse spin produces Magnus force
TOPIC: stuff, spin, spin efficiency, gyro, active spin, Magnus, axis, physics
CLAIM: A spinning baseball's spin vector decomposes into a transverse component (perpendicular to travel, produces Magnus force) and a gyro component (parallel to travel, produces zero Magnus force).
NUMBERS: spin efficiency = transverse / total = sin(theta), where theta is the angle between spin axis and velocity vector; gyro degree is the complement
POPULATION: n/a (physics)
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Nathan AM — "components of spin perpendicular to the direction of motion result in movement, whereas the component parallel to the direction of motion does not"
COACHING: Clock-face TILT is a 2D projection and says nothing about the gyro component. Two pitches with identical 1:30 tilt and identical spin rate can move completely differently if one is 90% efficient and the other 55%. TILT WITHOUT EFFICIENCY IS CLOSE TO UNINFORMATIVE.
CONFIDENCE: high
SEE ALSO: F-143, F-144, F-146

### F-143 | MLB four-seam distributions, computed directly from Statcast
TOPIC: stuff, four-seam, spin rate, Bauer Units, IVB, extension, release height, distribution
CLAIM: League four-seam characteristics are tighter than commonly implied, and spin and velocity are nearly independent at the elite level.
NUMBERS: n = 6,113 four-seam fastballs, 2024-06-01 to 2024-06-05. Velocity mean 94.5 mph, SD 2.4, p5 90.6, p25 93.0, median 94.6, p75 96.0, p95 98.2, p99 100.1. Spin rate mean 2,313 rpm, SD 174, p5 2,030, p25 2,206, median 2,317, p75 2,432, p95 2,584, p99 2,668. Bauer Units mean 24.5, SD 1.8, p5 21.7, p95 27.2. Extension mean 6.51 ft, SD 0.45, p95 7.30, p99 7.60. Release height mean 5.87 ft, SD 0.48. IVB mean 15.7 in, SD 2.9, p5 10.2, p95 19.8. Restricting to 95+ mph (n = 2,657) barely moves spin (mean 2,350).
POPULATION: MLB
EVIDENCE: ESTABLISHED (own computation)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball Savant pitch-level CSV, computed in stuff-and-command.md 2.1
COACHING: "24 Bauer Units is average" is empirically correct (measured mean 24.48). 2,600 rpm is roughly the 95th percentile, NOT exotic. Five days is good for central tendency, weak for individual tails.
CONFIDENCE: high for central tendency
SEE ALSO: F-142, F-144, F-150

### F-144 | Active spin by pitch type — the typical MLB slider is predominantly gyro
TOPIC: stuff, active spin, spin efficiency, slider, sweeper, four-seam, benchmark, distribution
CLAIM: Spin efficiency varies enormously by pitch class, with four-seams compressed near a ceiling and sliders predominantly gyro.
NUMBERS: n = 708 pitchers, Statcast Active Spin leaderboard 2024. Mean / p10 / median / p90 / max — Four-seam 89.4% / 77.0 / 91.5 / 98.2 / 99.6. Sinker 85.9 / 73.0 / 87.1 / 96.8 / 99.6. Changeup 90.2 / 77.3 / 93.2 / 98.9 / 99.7. Splitter 83.0 / 65.5 / 85.1 / 96.6 / 99.1. Curveball 70.8 / 49.3 / 73.5 / 88.8 / 99.6. Sweeper 50.4 / 36.4 / 50.9 / 64.5 / 81.4. Cutter 46.5 / 28.0 / 47.3 / 64.2 / 79.8. Slider 32.3 / 17.5 / 30.9 / 46.9 / 83.0.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Statcast Active Spin leaderboard, computed in stuff-and-command.md 2.1
COACHING: Elite four-seam efficiency benchmark: 95%+ ~ p75; 98%+ ~ p90. There is FAR LESS HEADROOM in four-seam efficiency than the market implies. The real efficiency room is in the breaking balls. Caution: active spin derived from MOVEMENT INFERENCE conflates efficiency loss with seam effects (F-146).
CONFIDENCE: high
SEE ALSO: F-142, F-146, F-159

### F-145 | FOLKLORE — "spin has diminishing returns because of the lift curve"
TOPIC: stuff, spin rate, Magnus, lift coefficient, diminishing returns, folklore, physics
CLAIM: The lift coefficient rises steeply below a low spin factor and then increases approximately linearly above it; every MLB fastball lives in the linear regime.
NUMBERS: C_L is mainly a function of spin factor S = R x omega / v; in SI units Re = 2180v and S = 8.53 x omega / v; experimental range covered S = 0.090-0.595; transition confirmed at S = 0.15. MLB fastball at 94.5 mph / 2,313 rpm sits at S ~ 0.21; elite (2,600 rpm, 95 mph) S ~ 0.235. Also: at low spin the lift of the four-seam orientation was nearly constant and THREE TIMES LARGER than the two-seam orientation, due to a periodic REVERSE MAGNUS effect at low spin rates; C_L for the two orientations converged at S = 0.15. 416 tests, six new Rawlings ROMLB balls, pitching machine + high-speed camera.
POPULATION: n/a (physics)
EVIDENCE: ESTABLISHED (physics) / FOLKLORE (the coaching claim)
CAUSALITY: MECHANISM
SOURCE: Nathan AM (2008), Am J Phys 76(2):119-124, DOI 10.1119/1.2805242; Lyu B, Smith L, Elliott J, Kensrud J (2022), Proc IMechE Part P 239:235-241, DOI 10.1177/17543371221113914
COACHING: The aerodynamic marginal return to spin is roughly CONSTANT across the elite band. Coaches quoting the low-S part of a curve no pitcher operates in are misapplying the physics.
CONFIDENCE: high
SEE ALSO: F-146, F-149

### F-146 | The real diminishing return on spin — raw rpm explains ~4% of IVB variance
TOPIC: stuff, spin rate, IVB, induced vertical break, efficiency, regression, marketing
CLAIM: Regressing induced vertical break on spin and velocity across the four-seam sample shows raw spin explaining only a small share of cross-sectional IVB variance, well below the theoretical Magnus value.
NUMBERS: IVB = 3.86 + 0.00315 x spin + 0.048 x velocity -> +0.32 in of IVB per +100 rpm, R2 = 0.041 (~4% of variance), n = 6,113. Theoretical Magnus value for a 100%-efficient pitch is roughly +0.5 to +0.6 in per 100 rpm. THE GAP BETWEEN 0.57 THEORETICAL AND 0.32 OBSERVED IS THE EFFICIENCY PROBLEM.
POPULATION: MLB
EVIDENCE: ESTABLISHED (own computation)
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 2.2
COACHING: Spin rate is largely a fixed athlete trait. Efficiency and axis are the trainable variables — and F-159 says even efficiency is ~two-thirds fixed. "Raise your spin rate" is MARKETING: selling the least trainable, least effective term. The second, separate diminishing return is that the IVB-to-whiff relationship saturates BEHAVIORALLY — that is a hitter-response fact, not a fluid-dynamics fact. Do not conflate them.
CONFIDENCE: high
SEE ALSO: F-145, F-159, F-234

### F-147 | Seam-shifted wake — the mechanism and the population magnitude are established
TOPIC: stuff, seam shifted wake, SSW, boundary layer, PIV, sinker, Hawk-Eye, axis deviation
CLAIM: Seams at specific positions force the boundary layer to separate earlier than it otherwise would; when this happens asymmetrically the wake deflects and a net force results, in a direction independent of the Magnus force.
NUMBERS: League-average 2D axis deviation on SINKERS ~17.6 deg, worth +3 in run and +4 in drop. Cutters +3 in glove-side, +2 in drop. Changeups/splitters substantial added drop. Four-seamers a fair amount of cut. Sliders/curveballs NO large league-wide effect. At the extremes ~9 inches of lateral and/or vertical movement. Controlled test: two zero-gyro changeup-like pitches oriented 180 deg apart measured ~8 inches of break difference; a deliberate-scuff test produced movement COUNTER to Magnus. Hawk-Eye calibration: park error under 2 deg maximum, 21 of 30 parks under 1 deg.
POPULATION: MLB
EVIDENCE: ESTABLISHED (mechanism and population effect)
CAUSALITY: MECHANISM
SOURCE: A.W. Smith & B.L. Smith (2021), Proc IMechE Part P 235(1):21-28, DOI 10.1177/1754337120961609; A.W. Smith (2020) MS thesis, Utah State; Smith BL, Nathan AM, Pavlidis H (5 Nov 2020), Baseball Prospectus; Driveline (Nov 2020, Mar 2021)
COACHING: CORRECTION TO A WIDELY CIRCULATED CLAIM: the foundational SSW work was CANNON/FIELD EXPERIMENTS AND PIV, not wind-tunnel smoke visualization. The evidence chain is PIV separation-point measurement -> cannon repeatability tests -> Hawk-Eye population data. The term was coined in 2019 by Andrew W. Smith, an MS student, not by Barton Smith.
CONFIDENCE: high for mechanism and population magnitude
SEE ALSO: F-148, F-149, F-153

### F-148 | SSW adds movement, and movement is not automatically value
TOPIC: stuff, seam shifted wake, SSW, Stuff+, value, marketing, residual, Reynolds
CLAIM: Driveline's own data found a large share of SSW-affected pitches had LOWER Stuff+ despite their actual trajectory breaks.
NUMBERS: ~42% of the pitches analyzed had LOWER Stuff+
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline (10 Mar 2021), "The Impact of Seam-Shifted Wakes on Pitch Quality"
COACHING: SSW adds movement. Movement is not value. THE RESIDUAL PROBLEM, which almost nobody states: the SSW signal is computed as a residual after removing modeled Magnus, drag and environment — so anything the model gets wrong lands in the "SSW" bucket, INCLUDING HAWK-EYE ERROR. Population averages are trustworthy; any single-pitch SSW number should be read skeptically. REYNOLDS DEPENDENCE: seam effects scale with Re — Utah State's Logan altitude (4,500 ft) means 90 mph at Logan ~ 76 mph at sea level ~ 92 mph at Denver. Lab results must be Re-matched before being applied.
CONFIDENCE: high
SEE ALSO: F-147, F-234

### F-149 | SSW is NOT SOLVED as a prescriptive coaching pathway
TOPIC: stuff, seam shifted wake, SSW, prescription, marketing, stability, gap, death ball
CLAIM: The physics is settled and the population effect is real, but the prescriptive pathway, pitch-to-pitch stability, and the value case are not.
NUMBERS: pitch-to-pitch stability of seam orientation at release: UNKNOWN — nobody has published the within-pitcher variance
POPULATION: MLB
EVIDENCE: UNSOURCED (for the prescriptive claim)
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 2.3
COACHING: "Seam-shifted wake lets us add X inches to your sinker" is MARKETING AT THE SERVICE LAYER. The "death ball" branding, the one-session promise, and the framing that SSW REPLACES Magnus rather than adding a few inches to it are all marketing. The underlying pitch (heavy-drop, arm-side-fade changeup from a seam-oriented, low-efficiency spin — Barton Smith calls it a discoball changeup) is physically real. SSW is now mainstream application, not frontier research.
CONFIDENCE: high that the gap exists
SEE ALSO: F-147, F-148, F-153

### F-150 | Perceived velocity — the formula, recovered empirically
TOPIC: stuff, extension, perceived velocity, effective speed, release point, geometry
CLAIM: Statcast's effective_speed field was reverse-engineered against release speed and extension, recovering an exact formula and an implied reference distance.
NUMBERS: Perceived Velocity = Release Velocity x 54.17 / (60.5 - Extension). Implied reference distance 54.173 ft, SD only 0.216 ft across 6,109 pitches. Neutral extension = 60.5 - 54.17 = 6.33 ft. At 94 mph: 5.5 ft -> 92.59 mph; 6.0 -> 93.44; 6.5 -> 94.30; 7.0 -> 95.18; 7.5 -> 96.08. ~1.7 mph per foot at 94 mph — but MULTIPLICATIVE, not additive: ~1.55 mph/ft at 85 mph, ~1.83 mph/ft at 100 mph. MLB 2024 four-seam mean extension 6.51 ft (the 6.33 reference is now slightly stale); p95 7.30; p99 7.60. Documented elite ~7.5 ft; extension ~1.04x pitcher height on average (Devin Williams at 1.22x is the outlier); low end 5.3 ft.
POPULATION: MLB
EVIDENCE: ESTABLISHED (own computation)
CAUSALITY: MECHANISM
SOURCE: stuff-and-command.md 2.4; matches Fink D (24 Jun 2021), FanGraphs
COACHING: ~7.5 ft appears to be a practical CEILING — a handful of pitchers, not a tail you can push indefinitely. TWO QUALIFICATIONS THE ENTHUSIASTS SKIP: (1) extension is mostly anthropometry plus stride length, and stride length just got demoted (F-043) — so this is not an independent lever either; (2) extension LOWERS release height and FLATTENS VAA — good for a four-seam at the top of the zone, BAD for a curveball. Chase extension globally, never per-pitch (it is nearly constant across pitch types league-wide, 6.35-6.54 ft). ALWAYS report release velocity separately from perceived velocity or you cannot tell an arm-speed gain from a geometry gain.
CONFIDENCE: high — the recovery is essentially exact
SEE ALSO: F-043, F-151, F-153

### F-151 | VERTICAL APPROACH ANGLE — release height beats IVB roughly 2:1
TOPIC: stuff, VAA, vertical approach angle, release height, arm slot, IVB, location, geometry
CLAIM: VAA is fully determined by plate height, release height, IVB and velocity, with release height by far the largest controllable term.
NUMBERS: |VAA| = 9.069 - 1.084 x (plate height, ft) + 1.055 x (release height, ft) - 0.0927 x (IVB, in) - 0.0630 x (velocity, mph); n = 6,110, R2 = 0.999; coefficients stable when restricted to top-of-zone pitches (n = 1,597, R2 = 0.996). Distributions: all four-seams mean |VAA| 4.75 deg, SD 1.01, p5 3.12, median 4.76, p95 6.40. TOP OF ZONE (plate_z 2.8-3.6 ft, n = 2,093) mean 4.40 deg, SD 0.55, p5 3.50, median 4.38, p95 5.31 — a flat four-seamer at the top is ~3.5-4.0 deg, a steep one ~5.3 deg+. Per-input: release height +1.06 deg steeper per foot; pitch location -1.08 deg per foot higher; IVB only -0.093 deg per inch; velocity -0.063 deg per mph; EXTENSION DROPS OUT entirely once release height is included.
POPULATION: MLB
EVIDENCE: ESTABLISHED (own computation). ⚠ CORRECTED 2026-08-20 — this line previously read "independently reproduces Zahradnik 2020, n = 2,350 pitchers, R2 = 0.945 from extension and release height." IT DOES NOT REPRODUCE IT AND MUST NOT CLAIM TO. Zahradnik (Medium/Iowa Baseball Managers, 26 Oct 2020) is a blog post: two predictors (extension + release height), NO coefficients published, NO season or level stated, and PLATE HEIGHT NOT MODELLED (he stratified by zone band instead). This model has four inputs including plate height and reaches R2 = 0.999. They are different models of the same geometry, and this one is the stronger. Extension appears predictive in Zahradnik ONLY as a proxy for release height — see this entry's own finding that extension drops out once release height is included. See daily/2026-08-20-verification-extension.md §4 and F-248.
CAUSALITY: MECHANISM
SOURCE: stuff-and-command.md 2.5
COACHING: Half a foot of release height (0.53 deg) is worth about 5.7 inches of IVB. Five extra inches of ride buys 0.46 deg — roughly half what half a foot of release height buys. LOCATION IS A VAA VARIABLE with nearly equal and opposite leverage. VAA IS GEOMETRY, NOT A "STUFF" TRAIT. Any VAA figure quoted WITHOUT ITS LOCATION IS MEANINGLESS. This is very likely why the league is drifting to lower slots (F-070).
CONFIDENCE: high
SEE ALSO: F-070, F-152, F-150

### F-152 | VAA and whiffs — the defensible claim is the INTERACTION, not "flat causes whiffs"
TOPIC: stuff, VAA, whiff, location, interaction, dead zone, expectation, benchmark
CLAIM: Flat VAA works high in the zone and steep VAA works low; VAA matters most at the edges of the zone, not in the heart.
NUMBERS: VAA-Above-Average benchmarks after adjusting for pitch height: +1 SD = 0.5 deg, +2 SD = 0.9 deg, +3 SD = 1.4 deg. Reported R2 ~ 0.237 for SwStr% and ~0.224 for whiff rate. At the BOTTOM of the zone, fastballs get roughly half the whiffs-per-swing of non-fastballs; at the TOP edge they match non-fastballs.
POPULATION: MLB
EVIDENCE: EMERGING (magnitude) / ESTABLISHED (direction)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Chamberlain A (7 Jan 2021 and 1 Feb 2022), FanGraphs
COACHING: "Flat VAA causes whiffs" is INCOMPLETE. Flatter four-seamers generate whiffs higher in the zone and tolerate a lower target line; steeper ones must be located down. A low-slot pitcher with a flat VAA who lives at the belt gets punished. BETTER FRAMEWORK, and it supersedes league-wide VAA: Max Bay's DYNAMIC DEAD ZONE models arm angle, height-scaled extension and acceleration components as a PER-PITCHER multivariate normal — what matters is distance from YOUR OWN expected shape given your slot, not from a league-wide average. (Chamberlain's May 2025 Andres Munoz piece shows VAA-above-average ignoring hitter EXPECTATION: Munoz's four-seam is +0.59 deg flat yet generates groundballs.) HORIZONTAL APPROACH ANGLE: EMERGING at best — not on Savant, thin public evidence, NO verifiable quantitative HAA-to-whiff study found. Treat confident HAA coaching claims as unsupported.
CONFIDENCE: medium
SEE ALSO: F-151, F-161

### F-153 | Spin efficiency is roughly two-thirds FIXED across three years
TOPIC: stuff, spin efficiency, trainability, fixed trait, arm slot, pronation, supinator
CLAIM: Across three seasons of professional coaching, spin efficiency was largely stable, and the one publicly documented large mover bought it with a delivery change.
NUMBERS: 185 pitchers with >= 25 fastballs in both 2023 and 2026 — three-year spin-efficiency r2 = 0.65 (roughly two-thirds fixed, one-third movable). The documented mover: arm angle 23 deg -> 13 deg, landing moved crossbody, which "cut off his tendency to pronate"; four-seam spin efficiency FELL from 99% and that was GOOD for him — it unlocked a glove-side breaking ball, 2.38 FIP, 30.6% K%.
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Rosen M (13 Apr 2026), "Emerson Hancock Became Less Efficient and More Effective," FanGraphs
COACHING: If the one-third of spin efficiency that moves, moves via ARM SLOT and LANDING POSITION, then efficiency work may be a MECHANICS project in a grip's costume — carrying every cost in F-070, F-071 and F-136, and nobody is quoting that price. Counterweight: four-seam efficiency is already compressed near its ceiling (p75 ~95%, p90 ~98%), so there was never much to win there; the real room is in the breaking balls (slider median 31%, sweeper 51%, cutter 47%) and nobody has shown THOSE require a delivery change. Field line: "once you go supinator, it's hard to go back."
CONFIDENCE: medium — public analytics, single case for the mover
SEE ALSO: F-144, F-070, F-235

---

# 10 — PITCH DESIGN, ARSENAL, AND STUFF MODELS

### F-154 | MLB 2025 pitch-characteristic baseline table, RHP
TOPIC: pitch design, baseline, benchmark, velocity, spin, IVB, HB, VAA, tilt, arsenal
CLAIM: Per-pitch-type league baselines for velocity, spin, active spin, break, VAA and measured tilt.
NUMBERS: Four-seam 95.1 mph / 2339 rpm / 89.1% active (IQR 84.8-95.8) / +15.7 IVB / 7.4 in arm-side / -4.66 VAA / 1:05 tilt. Sinker 94.2 / 2201 / 85.5 (79.8-92.8) / +6.8 / 15.0 arm / -5.76 / 1:26. Cutter 90.7 / 2434 / 46.5 (37.7-55.4) / +8.7 / 1.9 glove / -5.83 / 12:06. Gyro slider 86.8 / 2478 / 32.0 (23.5-39.2) / +1.4 / 4.6 glove / -7.61 / 9:56. Sweeper 83.3 / 2641 / 50.6 (43.4-57.4) / +0.7 / 14.0 glove / -7.68 / 8:10. Slurve 83.1 / 2387 / 54.9 / -3.7 / 12.2 glove / -8.53 / 7:41. Curveball 80.1 / 2611 / 70.8 (61.2-82.2) / -10.2 / 9.8 glove / -9.77 / 7:25. Knuckle/spike CU 83.1 / 2599 / ~71 / -9.6 / 6.8 glove / -9.48 / 7:25. Changeup 87.1 / 1802 / 88.5 (83.1-96.5) / +3.8 / 14.5 arm / -7.38 / 2:02. Splitter 87.0 / 1390 / 83.4 (77.6-91.9) / +2.8 / 11.7 arm / -7.66 / 1:52. Extension nearly constant across pitch types (6.35-6.54 ft).
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball Savant endpoints, computed in stuff-and-command.md 3.1. Mirror clock tilts and flip HB sign for LHP.
COACHING: The gap between Hawk-Eye MEASURED tilt and movement-INFERRED tilt is the SSW / axis-deviation signal — largest on cutter (12:06 measured vs 11:16 inferred), slider, changeup, splitter. That gap is the number to look at to answer "is this pitch getting non-Magnus help." Your own gym's distribution is a better benchmark than any MLB table.
CONFIDENCE: high
SEE ALSO: F-147, F-155, F-156

### F-155 | Velocity separation norms off the athlete's own four-seam
TOPIC: pitch design, velocity separation, arsenal, timing, changeup, sweeper, sinker
CLAIM: Per-pitcher velocity deltas off the athlete's own four-seam have stable league norms.
NUMBERS: mean (IQR) mph — Changeup 7.6 (6.1-8.7); Splitter 8.2 (6.7-9.6); Slider 8.5 (7.3-9.8); Sweeper 11.6 (10.3-12.9); Curveball 14.2 (12.2-15.7); Cutter 4.7 (3.5-5.7); Sinker 0.4 (0.0-0.8)
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball Savant 2025, computed in stuff-and-command.md 3.2
COACHING: Two consequences. (1) The SINKER IS NOT A VELOCITY-SEPARATION PITCH — it is a shape/plane pitch at the SAME speed, and the four-seam/sinker pair is a legitimate and underrated plane split (+15.7 vs +6.8 IVB, 0.4 mph apart). (2) A sweeper costs ~3 mph more separation than a gyro slider — a real timing cost you pay for the sweep.
CONFIDENCE: high
SEE ALSO: F-154, F-158, F-161

### F-156 | Whiff and value ordering by pitch type
TOPIC: pitch design, whiff rate, wOBA, usage, arsenal, survivorship
CLAIM: Whiff-per-swing, usage share and wOBA-against order the pitch classes.
NUMBERS: WHIFF-PER-SWING 2025 — Knuckle/spike CU 38.3, Splitter 34.6, Curveball 33.6, Slider 33.0, Changeup 32.1, Sweeper 30.4, Cutter 22.3, Four-seam 21.5, Sinker 11.9. USAGE SHARE — FF 31.9%, SL 16.5%, SI 15.1%, CH 10.3%, ST 6.8%, FC 6.8%, CU 6.5%, FS 2.8%, KC 2.3%. wOBA-AGAINST (min 100 pitches) — FS .263, CH .271, ST .276, CU .279, SL .284, FF .335, FC .335, SI .346.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball Savant 2025, computed in stuff-and-command.md 3.3
COACHING: The min-100 pool is SURVIVORSHIP-BIASED — every RV/100 in it is positive. Use for RELATIVE ORDERING ONLY, never absolute levels. Also: the knuckle/spike curve posting the highest whiff rate is very likely a SELECTION EFFECT (only pitchers who get something out of the grip keep throwing it), not a mechanism.
CONFIDENCE: high for the ordering, low for absolute levels
SEE ALSO: F-154, F-157

### F-157 | The sweeper — the alpha is gone
TOPIC: pitch design, sweeper, platoon, adoption, run value, popup, BABIP, hitter adaptation
CLAIM: The sweeper is a correctly-priced, same-handed, weak-contact pitch that the league has fully absorbed.
NUMBERS: RHP vs RHB — Sweeper whiff 36.4% vs non-sweeper SL 35.3; wOBA on contact .325 vs .357; BABIP .246 vs .277; GB% 33.0 vs 45.6; POPUP% 20.3 vs 13.1; RV/100 -0.94 vs -0.26. RHP vs LHB — whiff 28.5 vs 31.8; wOBA on contact .370 vs .370; BABIP .284 vs .268; RV/100 -0.05 vs -0.35 (the ordinary slider is BETTER). Adoption: league sweeper share 1.1% (2020) -> 7.6% (2025); slider share fell 16.8% -> 14.9%; RHP-to-RHB sweeper usage 2.6% (2021) -> 10.7% (2025). Decay: sweeper whiff% 33.4 (2023) -> 31.0 (2024) -> 31.2 (2025) while the ordinary slider held ~35; Driveline's Stuff+ v4 REPRICED IT DOWNWARD; 2026 usage flat-to-down at ~7%.
POPULATION: MLB
EVIDENCE: ESTABLISHED (platoon table) / EMERGING (the decay)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Clemens B (2 Sept 2022 and 1 May 2025), FanGraphs; Lambert J (31 May 2024), Driveline Stuff+ v4; Johnson B (29 May 2026), RotoWire
COACHING: The sweeper's edge is NOT whiffs — it is POPUPS and BABIP suppression (+7.2 pts popup rate, -31 pts BABIP vs same-handed hitters). The entire effect vanishes and inverts against opposite-handed hitters. Building an arsenal around it as a primary weapon in 2026 is LATE. Origin note: not a new pitch — NPB pitchers, Darvish prominently, threw accentuated sweeping sliders for years; what is new is deliberate design targeting from late 2021 and Statcast creating "ST" as its own classification in 2023. Skeptical footnote: a self-published 2026 analysis argues sweepers and sliders are genuinely distinct (sweeper xwOBA .246-.275 vs slider .282-.302, 2021-25) but presents NO formal bimodality test — treat "distinct pitch type" as a convention, not a fact.
CONFIDENCE: high
SEE ALSO: F-155, F-165, F-234

### F-158 | Deployment warning — the league solved the sinker's platoon problem by DROPPING the pitch
TOPIC: pitch design, sinker, platoon, usage, arsenal construction, deployment
CLAIM: RHP sinker usage to left-handed batters has collapsed to the lowest level on record.
NUMBERS: 21% a decade ago -> 9.7% in 2025
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Clemens B (1 May 2025), FanGraphs
COACHING: Read that as a warning about single-handedness arsenals generally. Cover both movement halves — sweeper-only right-handers get neutralized by LHB.
CONFIDENCE: high
SEE ALSO: F-157, F-161

### F-159 | The changeup — buy SEPARATION, kill spin, preserve arm speed
TOPIC: pitch design, changeup, velocity separation, attack angle, spin axis, arm speed, correction
CLAIM: The argued mechanism is velocity differential producing early swings producing whiffs; what has no relationship to whiff rate is the changeup's ABSOLUTE velocity.
NUMBERS: MLB changeup velocity separation norm 7.6 mph off the four-seam (IQR 6.1-8.7); splitter 8.2. Gaddis's changeup induced a -26.1 deg pull-oriented attack angle, the most extreme in baseball. A 92 mph changeup and a 78 mph changeup both post ~57% whiff. Driveline's spin target: 500-800 rpm below the fastball; the splitter class averages 1,390 rpm (lowest of any pitch) and posts the best wOBA-against in baseball (.263).
POPULATION: MLB
EVIDENCE: EMERGING (single-source)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Rosen M (17 Jun 2025), "Changeups Are Weird," FanGraphs
COACHING: CORRECTED 2026-08-13 — THE LIBRARY BRIEFLY CARRIED THIS INVERTED. "Velocity separation doesn't matter on a changeup" is a REVERSAL OF THE SOURCE and must not be re-imported. ABSOLUTE VELOCITY IS NOT VELOCITY SEPARATION. Two nulls in the same article (spin-axis similarity to the fastball; arm-angle change) are EACH A SINGLE UNQUANTIFIED SENTENCE — no coefficient, no n, no chart, no method. Label them EMERGING-unquantified, NOT folklore and NEVER "a published null." "Match your changeup's spin axis to your fastball" is UNSUPPORTED-BUT-UNTESTED: don't chase it, don't claim it has been disproven. THE VARIABLE THE AUTHOR THINKS MATTERS MOST — ARM-SPEED SIMILARITY — HE COULD NOT TEST; it is not publicly measurable, and 240 fps video is the only instrument a coach has for it. Cues: roll over the ball, throw it with your ring finger, pronate sooner, swipe the inside of the ball, flexible wrist. Lateral finger tilt toward the thumb on a two-seam grip reduces raw spin.
CONFIDENCE: medium for the main chain, low for the two nulls
SEE ALSO: F-155, F-160, F-232

### F-160 | The kick-change — real, low-cost, and a small-sample snapshot
TOPIC: pitch design, kick change, supinator, grip, middle finger, changeup, 2025
CLAIM: A spiked-middle-finger changeup variant developed for supinators is real and reported across multiple independent outlets, with promising but selection-biased early results.
NUMBERS: Early-2025 snapshots — Davis Martin ~90 mph, +1 to -1 in vertical, 10-20 in horizontal. Clay Holmes -10 in vertical at 88 mph, 38.2% whiff, .182 BAA, 16.2% usage, 2.95 ERA through 7 starts. Tylor Megill 50% whiff on 41 kick-changes, 2.50 ERA over 7 outings. Griffin Canning 2.50 ERA through 7 starts after a 5.19 prior. Hayden Birdsong 46.7% whiff, .188 BAA. Other adopters: Jack Leiter, Pablo Lopez, Andres Munoz.
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Developer Leif Strom, Tread Athletics, 2023; first MLB game use Hayden Birdsong (SF), June 2024; ESPN (2025); Yahoo Sports, Baker & Tracy (9 May 2025); FanGraphs Davis Martin / Matt Bowman interview
COACHING: MECHANISM: the middle finger is spiked/raised rather than laid flat, is the last thing to touch the ball, and "kicks" the axis forward through release; the ring finger cuts efficiency, creating tumble. Two-seam base, trace the seam, spike with the middle finger, targeting a 3 o'clock axis. It sits on the same spectrum as a split-change, differentiated primarily by rpm. WHY IT IS THE RIGHT KIND OF PROJECT: a GRIP-AND-RELEASE change, not a mechanics change — cheap to test, low stress cost, reversible. That risk profile is rare. COUNTERWEIGHT: MLB pitch-tracking studies associate increased changeup velocity and increased changeup spin/movement with UCL-reconstruction odds (F-141). "The pitch of 2025" is MARKETING — the written-up results are only the successes, no end-of-2025 league-wide evaluation exists, and STATCAST DOES NOT CLASSIFY IT SEPARATELY (it shows up as CH or FS), so public tracking is currently impossible. Sole-inventor claims are UNVERIFIED — an independent parallel line exists via Ethan Katz and Brian Bannister.
CONFIDENCE: medium for the mechanism, low for the results
SEE ALSO: F-159, F-141

### F-161 | Arsenal construction — shape gaps are relative to YOUR release, not the league
TOPIC: pitch design, arsenal, shape gap, dead zone, construction, platoon, plane
CLAIM: The defensible framework models release characteristics and acceleration components jointly as a PER-PITCHER multivariate normal, measuring how far each pitch sits from the shape a hitter would expect given that pitcher's slot.
NUMBERS: —
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Max Bay's Dynamic Dead Zone; stuff-and-command.md 4.1
COACHING: Construction rules that survive the evidence: (1) cover both movement halves; (2) separate on plane and timing, not just movement — F-155 supplies the guardrails; (3) the sinker/four-seam pair is a legitimate PLANE split at identical velocity; (4) most amateur pitch-design projects try to improve the pitcher's BEST breaking ball, and most of the available value is in the MISSING QUADRANT.
CONFIDENCE: medium — the right mental model, not a validated method
SEE ALSO: F-152, F-155, F-158

### F-162 | The pitch-design method that transfers
TOPIC: pitch design, method, protocol, grip, seam orientation, retest, command, device
CLAIM: A repeatable design method: measure, find the arsenal gap, change exactly one thing, A/B side by side, re-test cold, then test whether he can locate it.
NUMBERS: 5-10 pitches per variant, side by side, one device; judge on axis moved, efficiency held, velocity held within ~1 mph
POPULATION: professional_mixed
EVIDENCE: EMERGING (synthesis, not a validated protocol)
CAUSALITY: MECHANISM
SOURCE: stuff-and-command.md 3.4
COACHING: CHANGE EXACTLY ONE THING: grip, seam orientation, or intent cue. NOT MECHANICS — pitch design that requires a delivery change is a mechanical intervention in a costume, and it will cost command. NEVER mix Rapsodo and Trackman. RE-TEST COLD ON A DIFFERENT DAY: a grip that works the day you find it and not the following week is a mood, not a pitch. STEP 6 MATTERS MOST AND GETS DONE LEAST: a designed pitch he cannot command is worse than the one it replaced.
CONFIDENCE: medium
SEE ALSO: F-153, F-193, F-235

### F-163 | Tunneling is over-sold — the metric suite was published with no outcome validation
TOPIC: pitch design, tunneling, tunnel point, sequencing, refuted, folklore, release angle
CLAIM: Neither the original pitch-tunnel introduction nor its update reported a single correlation with outcomes, and an independent test found essentially no relationship with run value.
NUMBERS: Tunnel point originally 23.8 ft from the plate (~175 ms); revised to 150 ms, calculated from batter eye height, citing a study that the final third of the trajectory contributes nothing because required angular eye velocity exceeds physiological limits. League means: tunnel diff 10.0 in, plate diff 18.7 in, break diff 2.6 in, release diff 2.4 in, break:tunnel 27.6%. INDEPENDENT TESTS: Roegele (2014, PITCHf/x 2013-14, >= 150 sequences) found a real in-band effect, SwStr% lift 0.7-8.2 pts by pitcher (Hamels +6.0), but pitcher year-over-year repeatability R2 = 0.24 and it was NEVER converted to run values. Augustine (2020, 401 pitchers): top-15% vs bottom tunnelers SwStr 10.1% vs 6.1%, K/BB 2.69 vs 2.26, EV ~1 mph — but he explicitly notes he cannot establish intent and it is confounded with overall pitcher quality. Bryant (27 Sept 2024, 100 random pitchers, custom Tunnel Score+ vs Savant run values): r = 0.07, "almost no relationship at all."
POPULATION: MLB
EVIDENCE: FOLKLORE (as a training target)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Long J, Judge J, Pavlidis H (25 Jan 2017) and Long, Pavlidis, Alonso (31 Jan 2018), Baseball Prospectus; Roegele J (2014), THT; Augustine M (2020); Bryant Z (2024)
COACHING: "Tunnel your fastball and slider through a 24-foot window" is FOLKLORE as a training target — and nobody can execute a tunnel intentionally, pitch to pitch, at the inch scale those metrics measure. BP itself pivoted (Jan 2025) to four ARSENAL-LEVEL metrics — Pitch Type Probability, Movement Spread, Velocity Spread, Surprise Factor — reporting that above-average values worsen batter decision rates and raise whiff probability. TRAIN RELEASE CONSISTENCY. DO NOT BUILD SEQUENCES AROUND TUNNELS.
CONFIDENCE: high
SEE ALSO: F-164, F-234

### F-164 | The Kirby Corollary — horizontal release-angle overlap beats stuff models at predicting swings
TOPIC: pitch design, deception, release angle, HRA overlap, swing decision, Kirby, tunneling
CLAIM: Horizontal release-angle overlap between fastball and slider predicts swings better than Stuff+ does, and slider Stuff+ is essentially unrelated to called-strike rate.
NUMBERS: HRA overlap predicts swings at 59% accuracy vs Stuff+'s 54%. Slider Stuff+ vs called-strike% r2 = 0.001; release-angle overlap r2 = 0.12 (2023), 0.20 (2022).
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Rosen M (13 Jun 2024), "The Kirby Corollary," FanGraphs
COACHING: This is a STATIC PROPERTY OF THE DELIVERY, TRAINABLE IN A BULLPEN, not a sequencing decision. Kershaw and Strider maximize HRA overlap and generate swings through visual confusion; George Kirby's command precision comes AT THE COST of release-angle overlap — a real, named trade. Measure from Trackman across ~100 pitches of each type. This is the deception half of the release-consistency story; the command half is F-135/F-137.
CONFIDENCE: high
SEE ALSO: F-163, F-137, F-070

### F-165 | Stuff models — construction, scales, and what each one uses
TOPIC: stuff models, Stuff+, Location+, PitchingBot, tjStuff+, construction, scale, SD
CLAIM: The public stuff models differ in inputs, method and scale, and are not interchangeable.
NUMBERS: Stuff+ — release point, velocity, V/H movement, spin rate, axis differential (SSW proxy), pitch type; secondaries judged RELATIVE TO THE PITCHER'S OWN PRIMARY FASTBALL; decision-tree; 100 = avg, 10 pts = 1 SD at pitch level. Location+ — LOCATION ONLY, count-adjusted, pitch-type adjusted, batter handedness; no velocity, no movement. Pitching+ — physical characteristics + location + count + handedness; NOT a weighted average. PitchingBot — adds extension, spin efficiency, spin-axis deviation, plate location; XGBoost, many small event-probability sub-models split by pitch family; botStf/botCmd/botOvr on the 20-80 scouting scale plus botxRV100, botERA. tjStuff+ v3 — LightGBM, >1.6M pitches, RobustScaler, LHP mirrored; mean 100 / SD 10, built on xRV/100 (mean 0.35, SD 0.68) so 130 tjStuff+ ~ +2 runs per 100 pitches. Driveline Stuff+ — velocity, VB, HB, arm angle, extension, location-adjusted VAA/HAA; no locations; three non-comparable buckets. OBSERVED STARTER SDs: Stuff+ 12.16, Location+ 3.34, Pitching+ 4.94. Relievers 17.02 / 5.87 / 6.61. A reliever-to-starter transition costs ~5.5 Stuff+ points. Driveline: velocity-to-Stuff+ is EXPONENTIAL above ~96 mph, not linear; sinkers grade above four-seams below ~97 mph (no R2, RMSE or training-set size disclosed).
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: FanGraphs Library; Nestico T (tjStuff+); Grove C (PitchingBot); Lambert J (31 May 2024), Driveline
COACHING: Pitch-type Stuff+ averages for starters — FF 99.2 +/- 18.3, SL 110.8 +/- 15.6, KC 110.3 +/- 16.4, FS 109.6 +/- 30.2, CU 105.5 +/- 16.8, FC 102.1 +/- 14.0, SI 92.5 +/- 13.6, CH 87.2 +/- 16.4. THIS IS THE SINGLE MOST MISUSED TABLE IN PUBLIC PITCH ANALYTICS: sliders average 110 and changeups 87 NOT because sliders are better pitches, but because the model is scaled WITHIN pitch type. A pitcher does not improve his arsenal by throwing more sliders because sliders "grade higher."
CONFIDENCE: high
SEE ALSO: F-166, F-167, F-168

### F-166 | THE TEAM-SWITCHER TEST — Stuff+'s predictive power largely vanishes when a pitcher changes teams
TOPIC: stuff models, Stuff+, team switcher, prediction, environment, development, transfer
CLAIM: Stuff+'s correlation with next-year ERA collapses for pitchers who changed teams, while Location+ and DRA hold up better.
NUMBERS: weighted Spearman, 2021 metric -> 2022 ERA; 342 same-team pitchers vs 231 who changed teams; bootstrapped 5,000 samples, SD .05-.07. Stuff+ .41 same-team / .33 all / .14 SWITCHED. Location+ .00 / .09 / .24. Pitching+ .35 / .31 / .23. DRA .32 / .30 / .27.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Baseball Prospectus, "An Updated Evaluation of Hitting and Pitching, Including Stuff Metrics"
COACHING: Stuff+ is partly measuring THE TEAM's pitch-design program, defense, catching and park — not the pitcher. For a developing athlete who will change environments repeatedly, r ~ .14 is the number to remember.
CONFIDENCE: high — described in the corpus as "established and damning"
SEE ALSO: F-165, F-167

### F-167 | GOODHART'S LAW — stuff models are decaying as everyone optimizes to them
TOPIC: stuff models, Goodhart, model decay, compression, vintage, retraining
CLAIM: The standard deviation of Stuff+ across pitchers has compressed and the correlation between stuff grades and outcomes has declined.
NUMBERS: 2,860 pitcher-seasons 2020-25, min 400 pitches — Stuff+ SD across pitchers fell 9.7 (2020) -> 8.8 (2025), ~9% compression. Below-average-stuff pitchers fell from 12% (2021-23) to 9% (2024-25). Correlation between stuff grades and wOBA declined across all four measures. Population drift: the sweeper fell from ~115 Stuff+ (2021) to under 95 today as hitters adapted.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Andrews D (20 Jan 2026), "They Don't Make Pitch Models Like They Used To," FanGraphs
COACHING: When everyone optimizes to the metric, the metric stops discriminating. Models get retrained and silently reprice arsenals — CROSS-VINTAGE STUFF+ COMPARISONS ARE INVALID.
CONFIDENCE: high
SEE ALSO: F-157, F-166

### F-168 | What stuff models miss, and how to use them anyway
TOPIC: stuff models, limitations, sequencing, platoon, command, usage, injury gradient
CLAIM: No public stuff model handles sequencing, arsenal interaction, bullpen-vs-game intent, within-game usage decay, or platoon deployment; and the inputs they reward overlap the UCL-surgery gradient.
NUMBERS: Location+ correlates -0.54 with BB%; Stuff+ only -0.15. Real predictive performance for calibration: tjStuff+ v1 vs ERA same-season r = -0.38; prior-season tjStuff+ -> ERA r = -0.34 (vs prior xFIP 0.29, prior ERA 0.20). Stabilization: tjStuff+ v2 median 220 pitches (~3 starts); meaningful wOBA prediction ~400. Stickiness: tjStuff+ v2 2022->23 R2 = 0.78; v3 2023->24 r = 0.85.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 4.4-4.5
COACHING: SHOULD — use as a fast, low-sample (80-250 pitch) SHAPE SCREEN: "does this new pitch grade better than the one it replaces?" A/B grips in a bullpen. Use WITHIN a pitcher, WITHIN a season, WITHIN one model vintage. Read Location+/botCmd separately and never average them mentally. SHOULD NOT — compare across years or across models; treat a high Stuff+ as a forecast for an athlete changing environments (r ~ .14); chase Stuff+ by adding velocity and slider spin without weighing F-141; assume the model prices platoon, sequencing or arsenal fit. BP's doctrine worth adopting verbatim: include an input only if you can ARTICULATE ITS CAUSAL PATHWAY and it IMPROVES OUT-OF-SAMPLE. A coach optimizing an 85+ arm's Stuff+ should know he is optimizing toward a measured risk gradient (F-141).
CONFIDENCE: high
SEE ALSO: F-141, F-165, F-166, F-167

---

# 11 — COMMAND

### F-169 | What stuff and command are actually worth
TOPIC: command, stuff, value, FIP, Location+, Stuff+, xERA, measurement asymmetry
CLAIM: On any single pitch location outweighs shape; across a season shape is the more reliable asset; and the industry's preference for stuff is substantially a measurement artifact.
NUMBERS: Location+ correlates with walk rate at -0.54; Stuff+ at only -0.15 — yet Stuff+ carries roughly THREE TIMES Location+'s weight in explaining xERA. Stuff+ becomes reliable at ~80 pitches; Location+ at ~400. Observed starter SDs: Stuff+ 12.16, Location+ 3.34. Canonical case: Eury Perez, Stuff+ 117.8 / Location+ 93.4, 47.7% hard-hit on the fastball, xERA 4.91 — elite shape, ordinary results.
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: FanGraphs Library; Martin J (25 Jun 2026), RotoGraphs
COACHING: You can prove a pitch-design win in ten pitches. You cannot prove a command win in ten bullpens (F-138). That asymmetry — not the underlying value — is why one industry exists and the other does not. Know that you are being steered by it.
CONFIDENCE: high
SEE ALSO: F-170, F-138, F-181

### F-170 | The measured price of command — one inch of miss distance is worth about 0.3 FIP
TOPIC: command, FIP, xCTRL, miss distance, value, innings, Stuff+ equivalence
CLAIM: Improving fastball miss distance by one inch, holding Stuff+ constant, gives an expected reduction of roughly 0.3 FIP — comparable to a one-standard-deviation increase in Stuff+.
NUMBERS: 1 inch of fastball xCTRL ~ 0.3 FIP; elite fastball control ~ +36 IP/season; 118 pitcher-seasons; a starter's Stuff+ SD is 12.16 points, so moving a pitcher from an 11-inch average miss to a 9-inch miss is worth roughly what adding 24 points of Stuff+ is worth
POPULATION: MLB
EVIDENCE: EMERGING (preprint)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Ludwig M, Brill RS, Wyner AJ (2025), arXiv:2508.19184 (Wharton Sports Analytics)
COACHING: Two inches of command is worth more than most pitch-design projects deliver. VERIFIED CLEAN 2026-08-13 — do not re-check.
CONFIDENCE: medium — preprint, not peer-reviewed
SEE ALSO: F-169, F-176, F-177

### F-171 | COMMAND IS AN ANGULAR PROBLEM — 30 cm of plate location per 1 degree of release angle
TOPIC: command, release angle, geometry, trigonometry, elevation, azimuth, location, mechanism
CLAIM: Pitch location varies by approximately 30 cm for every 1 degree of change in release angle, in both elevation and azimuth, while 1 cm of release POSITION moves the ball 1 cm.
NUMBERS: elevation release angle ~30 cm per 1 deg; azimuth release angle ~30 cm per 1 deg; release speed ~20 cm per 1 m/s (vertical); vertical release point ~1 cm per 1 cm; horizontal release point ~1 cm per 1 cm. Model fit R2 = 0.97 +/- 0.02 (vertical), 0.96 +/- 0.04 (horizontal). Standardized coefficients largest for elevation/azimuth angle (~0.30). Within-pitcher SDs: release speed +/-1.0 m/s, elevation angle +/-1.1 deg, azimuth angle +/-1.09 deg. n = 7 skilled pitchers (one former NPB professional), 187 four-seam fastballs, TrackMan plus aerodynamic simulation. INDEPENDENT GEOMETRIC CHECK: release is ~54.5 ft from the plate; tan(1 deg) x 54.5 ft = 0.951 ft = 11.4 in = 29 cm. THE RESULT IS TRIGONOMETRY AND IS THEREFORE NOT SAMPLE-DEPENDENT.
POPULATION: unspecified (sample mean ~32.6 m/s ~ 73 mph — SAMPLE MISMATCH on velocity, but the physics is velocity-independent)
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Kusafuka A, Kobayashi H, Miki T, Kuwata M, Kudo K, Nakazawa K, Wakao S (2020), Front Sports Act Living 2:36, PMID 33345028
COACHING: Release angle is roughly 30x more consequential than release position. Multiply through: +/-1.1 deg x 30 cm/deg ~ 33 cm ~ 13 INCHES of 1-SD location scatter from release angle alone — essentially the entire observed miss distance. THE COACHABLE IMPLICATION IS NEGATIVE: it tells you what NOT to chase. There is no cue, no drill, no feedback channel and no device in a college program that returns a pitcher's release angle at a latency he can use inside 150 ms. VERIFIED CLEAN 2026-08-13 (PMID 33345028) — do not re-check.
CONFIDENCE: high — pure geometry
SEE ALSO: F-172, F-173, F-175, F-236

### F-172 | Skilled pitchers show COMPENSATORY COVARIATION — reducing each parameter's variability is not the optimum
TOPIC: command, release parameters, covariation, uncontrolled manifold, repeatability, optimum
CLAIM: The authors' own conclusion is that improving the reproducibility of each release parameter individually is NOT optimal, because skilled pitchers show different combinations of release parameters landing in the same spot.
NUMBERS: —
POPULATION: unspecified
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Kusafuka A et al. (2020), Front Sports Act Living 2:36
COACHING: This is the uncontrolled-manifold idea arriving independently from ballistics. "Should he repeat his delivery?" is the wrong question. The right question is: WHICH joint variability moves the release point, and which doesn't? Only the first kind costs command.
CONFIDENCE: high
SEE ALSO: F-171, F-109, F-139

### F-173 | Velocity variability IS a command metric, and it is free to measure
TOPIC: command, velocity variability, release speed, radar, vertical miss, free, uncoached
CLAIM: Release-speed variability translates directly into vertical location scatter via the same sensitivity analysis.
NUMBERS: ~20 cm of vertical location per 1 m/s of release speed -> 1 mph (0.447 m/s) ~ 9 cm ~ 3.5 INCHES of vertical miss. A pitcher whose fastball ranges 91-95 in an outing carries ~14 INCHES of vertical scatter from velocity alone, before any angular error. That is LARGER than the entire elite-to-average command gap (7 in vs 11 in).
POPULATION: unspecified (derived)
EVIDENCE: ESTABLISHED (arithmetic on a verified sensitivity)
CAUSALITY: MECHANISM
SOURCE: derived in stuff-and-command.md 5.1 from Kusafuka 2020
COACHING: LABEL IT HONESTLY — this is ARITHMETIC, NOT AN EMPIRICAL COMMAND FINDING. Nobody has regressed within-outing release-speed SD against vertical miss in a real dataset. It is trivially computable from any Statcast or Trackman database and apparently nobody has done it — the cheapest high-value study in the corpus. Meanwhile: compute the SD of his fastball velocity within an outing and treat it as a command metric. It costs NOTHING — the readings are already in your radar log. Needs ~25 fastballs per outing and ~8-10 outings before a change in an SD is believable.
CONFIDENCE: high for the arithmetic, zero for empirical confirmation
SEE ALSO: F-171, F-183, F-243

### F-174 | The Kirby Index — release angles predict location; drop them and the model collapses
TOPIC: command, release angle, Kirby Index, location prediction, MLB scale, corroboration
CLAIM: At MLB scale, release angles plus release points predict actual pitch location very well; a model using spin, velocity, extension and release height/width but EXCLUDING release angles collapses.
NUMBERS: with release angles R2 = 0.92 vertical / 0.85 horizontal, across ~230,000 four-seam fastballs; without release angles R2 = 0.06 / 0.05
POPULATION: MLB
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Rosen M (3 May 2024), "Introducing the Kirby Index," FanGraphs
COACHING: Independent MLB-scale corroboration of F-171 by a completely different method. Kirby Index stabilization: 1-2 starts for a stable vertical release angle; R2 = 0.50 year over year (2022->23).
CONFIDENCE: high
SEE ALSO: F-171, F-164

### F-175 | REFUTED — release-point variability does NOT predict walks
TOPIC: command, release point, variability, BB/9, K/9, HR/9, deception, null, refuted, MLB
CLAIM: Release-point variability relates to strikeouts and home runs — deception and pitch quality — and has essentially no relationship with walk rate.
NUMBERS: n = 344 MLB starters (300,884 four-seams, 517,530 breaking balls) plus 64 MiLB, 2021-2023; inclusion >= 1,500 pitches/season, >= 70% starts, > 5% four-seam usage; variability = 95% confidence ellipse dimensions. MODELS: xFIP R2 = 0.207 (RPX variability beta = +0.161, p = .002, second predictor after velocity beta = -0.398); K/9 R2 = 0.345 (RPX beta = -0.122, p = .006); HR/9 R2 = 0.072 (RPX beta = +0.168, p = .002); **BB/9 R2 = 0.011, only velocity entered (beta = 0.118, p = .029), release-point variability NOT SIGNIFICANT.** MLB vs MiLB four-seam release variability: RPX 30.60 +/- 12.29 vs 35.21 +/- 16.17 cm (p = .014); RPZ coronal 15.21 +/- 2.52 vs 17.48 +/- 3.43 (p < .001); RPZ sagittal 15.70 +/- 3.06 vs 17.30 +/- 3.22 (p < .001); 95% ellipse area coronal 373.50 +/- 184.81 vs 497.06 +/- 300.81 cm2 (p < .001). Breaking balls RPX 35.39 +/- 15.24 vs 39.54 +/- 16.77 (p = .002); ellipse 471.00 +/- 287.70 vs 625.54 +/- 352.58.
POPULATION: MLB
EVIDENCE: ESTABLISHED (as a null)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Wakamiya K, Nagamoto H, Yamaguchi S, Okunuki T, Maemichi T, Liu X, Ogawa T, Kobayashi H, Kumai T (2024), Front Sports Act Living 6:1447665, PMC11608975
COACHING: The folk model "repeatable release point -> command -> doesn't walk guys" is NOT SUPPORTED at the MLB level. RELEASE-POINT CONSISTENCY IS A DECEPTION VARIABLE, NOT A COMMAND VARIABLE. Exactly what F-171 predicts: release position moves location ~1:1 against a ~30 cm/deg angular term. The cue "repeat your release point and you'll command the ball" was RETIRED 2026-08-13. MLB pitchers ARE tighter than MiLB, and horizontal is the discriminator (~4.6 cm gap vs ~2.3 cm vertical). LIMITATIONS: season-aggregated variability confounds intentional release differences across locations and pitch types; starters only; breaking balls pooled; no spin or biomechanical data; only ~20% of xFIP variance explained. A release point that moves in the 6th when it didn't in the 1st is still a FATIGUE signal — a different claim. VERIFIED CLEAN 2026-08-13 (PMC11608975) — do not re-check.
CONFIDENCE: high
SEE ALSO: F-171, F-164, F-229

### F-176 | THE MECHANICAL SIGNATURE OF PLUS COMMAND — taller, less tilted, higher slot, velocity-matched
TOPIC: command, mechanics, trunk tilt, arm slot, consistency, professional, velocity matched
CLAIM: In a velocity-matched professional sample split by location consistency, the high-consistency group sat at a higher arm slot with less lateral and forward trunk tilt at release.
NUMBERS: n = 338 professional (MLB and Low-A through AAA), high-consistency n = 91 vs low-consistency n = 98 at +/-0.5 SD of location spread normalized to grid width; 8-12 fastballs each, marker-based mocap at 480 Hz; velocity ~37.9-38.4 m/s ~ 85-86 mph IN LAB. AT BALL RELEASE (high vs low, p): arm slot 59.7 +/- 13.5 vs 54.7 +/- 12.4 deg, p = .009; trunk LATERAL flexion -27.1 +/- 9.3 vs -31.8 +/- 9.0 deg, p < .001; trunk tilt -33.4 +/- 9.1 vs -37.2 +/- 8.9 deg, p = .004; trunk flexion 11.9 +/- 10.0 vs 15.9 +/- 9.0 deg, p = .005; stride length 77.8 +/- 5.5 vs 79.4 +/- 5.3 %BH, p = .048 (n.s. at alpha = .01); shoulder distraction force 112.4 +/- 15.9 vs 118.3 +/- 15.1 %BW, p = .001; elbow distraction force 110.5 +/- 17 vs 117.0 +/- 15.2 %BW, p = .006. **VELOCITY DID NOT DIFFER (p = .055)** — a genuine command contrast, not a velocity confound.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE, Dowling B, Wang Z, Arzani A, Chen J, Nicholson KF, Dines JS (2021), Journal of Orthopaedics 27:28-33, PMID 34475727
COACHING: THE MECHANISM IS F-171: less lateral trunk tilt means the release-angle vector is less sensitive to small trunk perturbations. If the release angle is generated by a heavily tilted trunk, a 1 deg trunk error becomes a 1 deg release-angle error — AND 1 DEG IS 12 INCHES. THE DELIVERIES THAT MAXIMIZE VELOCITY ARE NOT THE DELIVERIES THAT MAXIMIZE COMMAND. Say that out loud before pushing an athlete toward "get out over the front side." WEAKNESSES, STATED HONESTLY: cross-sectional and between-subject (two populations, not one athlete moved); command operationalized as location SPREAD around a target grid — dispersion, not accuracy, with no intent inference; differences are ~4-5 deg on SDs of 9-10 deg so the distributions OVERLAP HEAVILY (a population signal, not an individual diagnostic); and REVERSE CAUSATION IS LIVE — pitchers who already command the ball may throw with less effort, and less effort produces less tilt.
CONFIDENCE: high for the contrast, low for the causal reading
SEE ALSO: F-053, F-070, F-137, F-177

### F-177 | Foot contact is where command is decided — three independent routes converge
TOPIC: command, foot contact, trunk tilt, hip, repeatability, convergence, random forest
CLAIM: Trunk tilt and hip variables at foot contact are the top predictors in both accuracy and consistency models of pitch location.
NUMBERS: n = 322 professional, velocity 38.4 +/- 1.7 m/s (population match), elastic net + random forest. ACCURACY MODEL top random-forest importances: trunk tilt at foot contact 6.6%, lead hip flexion at FC 4.2%, shoulder abduction at FC 4.2%, trunk tilt at BR 3.8%. CONSISTENCY MODEL (R2 = 0.57): trunk tilt at FC 3.7%, trunk flexion at BR 3.3%, lead foot rotation at FC 3.2%, back hip flexion at FC 2.6%. Authors: "Four of the top six parameters in both models involved variance at the hip and trunk."
POPULATION: professional_mixed
EVIDENCE: EMERGING (low-tier venue)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Manzi JE et al. (2021), "Kinematic Models For Pitch Location Metrics in Professional Baseball Pitchers," Archives of Sports Medicine (Scholars.Direct) — low-profile open-access venue with weak indexing; location charted MANUALLY by pitching staff from behind the mound. The author group (Dines, HSS) is legitimate and the sample overlaps the J Orthop paper.
COACHING: Three independent routes converge on foot contact: these professional datasets, the Driveline command study (F-139), and the phase-duration argument (F-088). Corroborating off-population: a HS study (n = 59) found high-consistency pitchers showed decreased lead hip flexion at elbow extension (40 +/- 12 vs 52 +/- 13 deg), decreased back hip extension, increased back hip internal rotation at FC; multiregression predicted 0.49 of location-consistency variance. Directionally consistent — do NOT transfer the joint-angle values to an 85+ athlete.
CONFIDENCE: medium — effect sizes modest, venue weak
SEE ALSO: F-088, F-139, F-176

### F-178 | Command lives at the end-effector; velocity lives in proximal-to-distal sequencing
TOPIC: command, forearm, acceleration, IMU, velocity, sequencing, distal, end effector
CLAIM: In an IMU study, only peak forearm resultant linear acceleration survived as a command predictor, while ten variables predicted velocity.
NUMBERS: COMMAND — only peak forearm resultant linear acceleration survived (beta = 0.008, SE 0.003, p = .010). VELOCITY — ten variables, including torso-pelvis peak separation angle (beta = 0.29, p < .001), torso peak rotation rate (beta = 0.03, p < .001), upper-arm orientation at foot strike (beta = 0.16, p < .001), time of torso-pelvis peak separation (beta = 3.82, p = .016), ball release timing (beta = -66.15, p = .017). n = 10 collegiate, six IMUs at 512 Hz, ~35 pitches.
POPULATION: NCAA_D1
EVIDENCE: EMERGING (at best)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Agresta C, Freehill M, Nakamura A, Guadagnino B, Cain S (2022), Sensors 22(21):8488
COACHING: Consistent with F-171 — command is a release-angle problem and the release angle is set distally. CRITICAL LIMIT: command was measured by a SUBJECTIVE 5-POINT LIKERT SELF-RATING SPOKEN ALOUD, n = 10.
CONFIDENCE: low
SEE ALSO: F-171, F-176

### F-179 | Repeatability at foot plant, adjustability everywhere else — the "funnel in, funnel out" pattern
TOPIC: command, repeatability, adjustability, dampening, funnel, foot plant, Driveline, PCA
CLAIM: Variability that DAMPENS from peak knee height to foot plant associates with better command, while variability that OPENS UP after foot plant also associates with better command.
NUMBERS: n = 27 athletes, 270 throws (first 10 per athlete), from weekly sessions of 8-20 middle-middle fastballs at ~90% intensity on Velocity-phase "A Days"; college -> independent -> affiliate -> MLB. Command = average miss distance in inches (Intended Zone Tracker + TrackMan Mobile). Kinematics at PKH, FP, MER, BR. RESULTS: multiple features with |Pearson r| > 0.5 on raw SD; glove-shoulder abduction at FP and torso lateral tilt at FP significant (repeatability helping). Predominantly NEGATIVE correlations elsewhere — MORE variability associated with BETTER command — concentrated in angular velocities at peak knee height. "Dampening scores" (SD at an earlier chain point / SD at a later one) produced LARGER correlations than raw SD. PKH -> FP: all significant dampening features negative (|r| >~ 0.6) -> FUNNEL IN is good early. FP -> MER and MER -> BR: all significant features positive -> FUNNEL OUT is good late. Variable shoulder horizontal abduction at MER is a "clean-up point"; variable pronation rate into release does the same. PCA: 10 components = 80% of variance; PC3 (adjustability; 14/15 loadings angular velocities at PKH) strongest negative; PC9 (repeatability; features post-PKH) strongest positive, though PC9's loadings were self-described as "a mixed bag." REFERENCE VALUE SUPPLIED: MLB average fastballs miss their intended spot by roughly 11 inches.
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Driveline Baseball (Feb 2026), "The Interaction of Biomechanics and Command" — winner of the 2025 SABR Dr. Mike Marshall Pitching Biomechanics Research Award
COACHING: The cue this supports: "different every time on the way there, same every time when the foot lands." DRILL: variable leg-lift / variable-tempo bullpens converging to one FC position — slow lift, fast lift, no lift, slide-step, exaggerated drift, all required to arrive at the same front-foot position and trunk angle at FC. HONEST ASSESSMENT: no per-variable correlation table published, no sample miss-distance values published, no ANOVA (authors state n was too small, which is why they pivoted to the SD/dampening analysis). With n = 27 and many features screened at |r| > 0.5, MULTIPLE-COMPARISONS INFLATION IS A REAL RISK. The task is also a non-competitive bullpen aiming at one location at submaximal intent. IF THE DAMPENING RESULT REVERSES ON A HELD-OUT SAMPLE, THE CUE LOSES ITS ONLY DIRECT COMMAND EVIDENCE — the other two supports (F-176 between-subject posture, F-109 a velocity paper) are not command findings.
CONFIDENCE: low-medium — hypothesis-generating, already converted into a drill
SEE ALSO: F-109, F-176, F-177

### F-180 | Reconciling the apparent conflict — stable proximal base, adaptive arm chain
TOPIC: command, variability, trunk, UCM, reconciliation, foot plant, proximal, arm chain
CLAIM: The finding that the trunk carries only ~5% of release-preserving variance and the finding that trunk/hip posture at foot contact is the top command predictor are NOT the same claim and must never be quoted as if they were.
NUMBERS: trunk degrees of freedom carry ~5% of release-preserving variance (F-109); trunk tilt at FC is the top random-forest importance in both command models (F-177)
POPULATION: professional_mixed
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 8.5
COACHING: One decomposes WITHIN-delivery variance about the release point with VELOCITY as the outcome; the other predicts BETWEEN-pitcher command from trunk POSTURE and posture variability at foot contact. A stable proximal base is exactly what lets the arm chain do the release-preserving covariation. "Get the trunk to the same place at foot plant, then let the arm negotiate." Same sentence, three datasets.
CONFIDENCE: medium
SEE ALSO: F-109, F-177, F-179

### F-181 | HORIZONTAL CORRECTIVE CAPACITY — the best adjustability evidence in the peer-reviewed literature
TOPIC: command, correction, autocorrelation, azimuth, elevation, horizontal, trial to trial, coachable
CLAIM: Vertical correction is near-optimal in all skilled throwers; horizontal correction is where pitchers differ, and the failure to correct horizontally is what separates wide from tight side-to-side scatter.
NUMBERS: n = 14 skilled pitchers, top-level Japanese university league, velocity 30.84 +/- 2.61 m/s ~ 69 mph (SAMPLE MISMATCH), 30 four-seams each, 960 fps cameras, DeepLabCut. Maximum SDs: elevation 1.81 deg, azimuth 2.81 deg -> via F-171, ~54 cm and ~84 cm of 1-SD scatter. ELEVATION: no relation between lag-1 ACF and SD (r = -0.18, p = .46). AZIMUTH: correlation between each pitcher's lag-1 autocorrelation coefficient (ACF1) and the SD of his azimuth release angle r = 0.54, p = .02; correlation between the "No"-correction transition probability and SD of azimuth release angle r = 0.73, p < .01. Friedman chi2 = 25.79, df = 15, p = .04.
POPULATION: unspecified (~69 mph — sample mismatch)
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Kusafuka A, Okegawa H, Yamamoto S, Miyata K, Kudo K (2025), Scientific Reports 15:12300, doi 10.1038/s41598-025-97146-5, PMID 40210939
COACHING: LABEL DISCIPLINE — CORRECTED 2026-08-13. r = 0.54 is NOT an autocorrelation value and r = 0.73 is NOT a "staying-in-the-same-state" correlation. BOTH ARE CORRELATIONS BETWEEN A PER-PITCHER CORRECTION STATISTIC AND THAT PITCHER'S AZIMUTH VARIABILITY. Both were mislabelled in this corpus once already. The coachable direction survives unchanged. TRANSLATION: command training that only counts hits and misses trains the wrong thing. What separates command is THE CORRECTION AFTER THE MISS, and specifically the HORIZONTAL correction. TWO CONSECUTIVE SAME-DIRECTION HORIZONTAL MISSES IS THE ACTIONABLE EVENT. Citation and both coefficients re-verified 2026-08-13.
CONFIDENCE: medium — n = 14 x 30 balls, sub-elite velocity, bullpen task; but a large effect with a clean mechanism
SEE ALSO: F-171, F-183, F-236

### F-182 | Measuring command — the intended-target problem and the four approaches
TOPIC: command, measurement, intent, CSAA, Location+, xCTRL, Command+, glove tagging
CLAIM: Command measurement is bounded by the intended-target problem, and four public approaches handle it differently.
NUMBERS: (a) GLOVE TAGGING / COMMANDf/x — Baseball Prospectus explicitly calls glove-based intent inference "flawed"; the glove moves pre-pitch, the target may be a zone rather than a point, framing motion contaminates the frame. DEPRECATED. (b) BP COMMAND / CSAA — called strikes above average on TAKEN PITCHES ONLY, from a mixed model controlling pitcher, catcher, batter, umpire and location; sidesteps intent entirely. 2016 leaders (min 500 chances): Zach Davies 3.5%, Josh Tomlin 2.8%, Kyle Hendricks 2.5%, Zack Greinke 2.1%. Jered Weaver's decline 2.1% (2014) -> 0.6% (2016), WARP 0.4 -> -5.3. BP NEVER PUBLISHED FORMAL STABILIZATION FIGURES — in the comments only "a couple weeks of games is a reasonable rule of thumb." LABEL ANY CSAA STABILITY CLAIM UNVERIFIED. (c) LOCATION+ — explicit that it "only looks at actual locations and implicitly assumes the intent is generally the same across the league in certain counts with certain pitches." It CANNOT distinguish a missed spot from an executed pitcher's pitch. (d) xCTRL — Gaussian mixture model fit via EM to each pitcher's historical location tendencies (K discrete targets, >= 250 pitches/bin); Bayesian posterior update over which target he was aiming at given the realized location; xCTRL = posterior-weighted execution distance. Statcast 2008-2023 (primary 2021-2023), 23,831 fastball at-bats for validation, 118 pitcher-seasons. Elite ~7.05 in miss distance; worst exceed 10 in. Correlation with Location+ is only r = -0.46 — they disagree meaningfully. Also COMMAND+ (Sarris/STATS 2018), modeling intent as selection from 13 target zones incorporating catcher glove placement; proprietary, and discretization limits precision.
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: Pavlidis & Judge (BP); FanGraphs Library; Ludwig M, Brill RS, Wyner AJ (2025), arXiv:2508.19184
COACHING: DECLARED-TARGET-BEFORE-THE-PITCH is the only approach that SOLVES rather than infers the intent problem. It requires discipline, not hardware. The cost is ecological validity: a bullpen is not a game.
CONFIDENCE: medium
SEE ALSO: F-170, F-183, F-184

### F-183 | Three independent methods converge on how far an MLB fastball misses
TOPIC: command, miss distance, benchmark, convergence, inches, athlete facing, anchor
CLAIM: Physics, an intent-tracking bullpen protocol, and a Bayesian intent model all land on roughly the same miss distance.
NUMBERS: release-angle SD x 30 cm/deg -> ~13 in; Intended Zone Tracker + InsideEdge -> ~11 in; Bayesian intent inference on Statcast -> ~7 in elite, 10+ in poor
POPULATION: MLB
EVIDENCE: ESTABLISHED (order of magnitude)
CAUSALITY: MECHANISM / CROSS_SECTIONAL
SOURCE: Kusafuka 2020; Driveline (Feb 2026); Ludwig, Brill & Wyner (2025)
COACHING: ATHLETE-FACING ANCHOR: "The best command in the major leagues misses by about seven inches. The average major leaguer misses by about a foot. If you think you're hitting the glove, you're not — and neither is anybody else."
CONFIDENCE: high for the order of magnitude
SEE ALSO: F-170, F-171, F-182

### F-184 | Much of "command is unstable / command is luck" may be a MEASUREMENT ARTIFACT
TOPIC: command, reliability, stabilization, intent, artifact, year over year, Location+
CLAIM: The intent-aware command metric shows year-over-year reliability much nearer to Stuff+ than to Location+, suggesting the historic instability finding partly reflects ignoring intent.
NUMBERS: WITHIN-SEASON STABILIZATION / YEAR-OVER-YEAR — Stuff+ ~80 pitches / r ~ 0.73. Location+ ~400 pitches (Cronbach's alpha ~ 0.9) / R2 = 0.39, r ~ 0.48. Pitching+ ~250 (RP) / ~400 (SP). tjStuff+ v2 ~220 pitches (~3 starts) / R2 = 0.78 (2022->23). Kirby Index 1-2 starts for a stable vertical release angle / R2 = 0.50 (2022->23). **xCTRL (fastball) — inter-season r = 0.65 across 53 pitcher-season pairs.**
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 9.2
COACHING: The 5x stabilization gap between Stuff+ (80) and Location+ (400) is the empirical core of "stuff is easy, command is noisy." But the intent-aware metric sits at r = 0.65 — much nearer Stuff+ (0.73) than Location+ (0.48). If this holds it is one of the more consequential ideas in the corpus.
CONFIDENCE: medium — preprint-dependent
SEE ALSO: F-169, F-182, F-170

### F-185 | What to program for command, honestly labeled
TOPIC: command, training, protocol, declared target, miss distance, RPE, drill, defaults
CLAIM: A twelve-element command program can be assembled from the evidence, but it is a list of DEFAULTS, not validated interventions.
NUMBERS: —
POPULATION: professional_mixed
EVIDENCE: EMERGING (synthesis, not a validated program)
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 11.2; Driveline (Sept 2018), "Implementing Command Training Into Team Practice"
COACHING: (1) DECLARE THE TARGET before every pitch — free, and the highest-value change available. (2) SCORE MISS DISTANCE IN INCHES, not strikes. (3) SCORE THE SIGN of the miss, especially horizontal — two consecutive same-direction horizontal misses is the actionable event (F-181). (4) HAVE HIM CALL HIS OWN MISS before he sees the number — a calibration test, and track his calling accuracy separately. (5) FEEDBACK FREQUENCY: don't overthink it — F-192 found no effect at any time point; both "screen on every pitch" and "hide the numbers" are unsupported. (6) TRAIN AT RPE >= 70% AND RADAR-GATE IT (F-196). (7) ATTACK RELEASE-SPEED VARIABILITY (F-173) — costs nothing. (8) VARIABLE-TEMPO BULLPENS converging to one foot-plant position (F-179). (9) RANDOM/INTERLEAVED pitch selection — default it, don't oversell it (F-193). (10) VARIED IMPLEMENTS — plausible rationale, absent evidence (F-194). (11) REPRESENTATIVE DESIGN — add the hitter EARLY, not last. (12) SPREAD THE VOLUME (F-197). The published Driveline protocol (overload 6 oz / regulation 5 oz / underload 4 oz alternated within a session; not fastball-only; strike %, location accuracy vs intended target, RPE minimum 70%, radar; gamified scoring sheets; progression 50 ft -> regulation, flat ground -> mound, increasing RPE, then contextual distraction) PUBLISHES ZERO QUANTIFIED OUTCOMES — no pre/post, no retention test, no control condition. Well-reasoned is not the same as effective.
CONFIDENCE: low-medium — a defaults list. Per F-186, exactly ONE element can be tested per athlete per year; the corpus's own vote is element 7, because it costs zero additional pitches.
SEE ALSO: F-173, F-179, F-181, F-186

### F-186 | POWER ANALYSIS — you need ~200 tracked pitches before you can claim a 2-inch command improvement
TOPIC: command, power analysis, sample size, bullpen, evaluation, noise, retention test
CLAIM: With a within-pitcher miss-distance SD of ~10 inches, detecting a 2-inch improvement at 80% power requires roughly 200 tracked declared pitches per condition.
NUMBERS: d = 2/10 = 0.2 -> n ~ (1.96 + 0.84)^2 / 0.2^2 ~ 196 pitches per condition, i.e. seven to ten bullpens. A single 30-pitch bullpen can only detect d ~ 0.52, i.e. a ~5-inch change. Velocity equivalent (F-243): ~8 separately-dated sessions of >= 25 fastballs for 1 mph.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (standard power analysis on a verified SD)
CAUSALITY: MECHANISM
SOURCE: stuff-and-command.md 11.4
COACHING: ANY COMMAND INTERVENTION DECLARED SUCCESSFUL AFTER ONE BULLPEN IS NOISE. Every one of them. Location+ needing ~400 pitches to stabilize is NOT a defect of the metric — it is the actual signal-to-noise ratio of command; the metric is telling the truth and coaches don't want to hear it. And per F-187, in-session improvement is not learning anyway — the comparison must be a delayed retention test, ideally in a game. A college starter throws 2-3 command pens a week at 25-40 declared pitches: that is ONE CONDITION EVERY TWO TO THREE WEEKS. You cannot A/B twelve things at 200 pitches each on one athlete in a career.
CONFIDENCE: high
SEE ALSO: F-185, F-187, F-243

---

# 12 — SKILL ACQUISITION AND MOTOR LEARNING

### F-187 | ACQUISITION IS NOT LEARNING — the most-violated rule in applied baseball
TOPIC: motor learning, acquisition, retention, transfer, delayed test, evaluation, methodology
CLAIM: Conditions that raise in-session performance frequently LOWER retention and transfer, and vice versa.
NUMBERS: repeated dissociations between acquisition curves and delayed retention/transfer across motor and verbal domains
POPULATION: n/a (motor learning)
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Soderstrom NC & Bjork RA (2015), Perspectives on Psychological Science 10:176-199
COACHING: Learning is only visible on (a) a DELAYED test (>= 24 h, ideally days), (b) under CHANGED conditions (transfer), (c) WITHOUT the feedback or support present in practice. A bullpen where a pitcher hits 80% of his targets tells you almost nothing about whether he learned anything. Any command program evaluated by within-session hit rate is measuring the wrong variable.
CONFIDENCE: high — the single most defensible finding in the field
SEE ALSO: F-186, F-198, F-199

### F-188 | SCOPE WARNING — almost the entire motor-learning literature is novices on lab tasks
TOPIC: motor learning, scope, novices, lab task, replication crisis, power, generalization
CLAIM: The experimental motor-learning literature uses novices on lab tasks with tiny samples, and has had a genuine replication reckoning.
NUMBERS: dart throwing, golf putting, key-pressing, balance boards; typically 20-60 total participants and 1-3 sessions; median sample sizes ~15/group giving ~20-30% power for realistic effects. When robust publication-bias models are applied, headline effects repeatedly collapse toward zero.
POPULATION: n/a (novices)
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: stuff-and-command.md 10 preamble
COACHING: An elite 85+ mph pitcher is the extreme opposite of these samples: 10-20 years of deliberate practice on a ballistic, high-force, open-loop task with a ~150 ms execution window. ALMOST NOTHING IN THIS SECTION WAS TESTED ON THAT POPULATION. Several things baseball coaching education teaches as settled science are, as of the current evidence, falsified or unsupported.
CONFIDENCE: high
SEE ALSO: F-189, F-192, F-193

### F-189 | External focus of attention — the best-supported of Wulf's claims, and it still is not clean
TOPIC: motor learning, external focus, internal focus, cue design, OPTIMAL theory, publication bias
CLAIM: A large pro-external-focus meta-analysis is contradicted by a robust Bayesian re-analysis that found publication bias in every prior analysis and bias-corrected effects near zero.
NUMBERS: PRO-EF META (143 studies): performance g ~ 0.26 (73 studies, N = 1,824); retention g ~ 0.58 (40 studies, N = 1,274). RE-ANALYSIS of the data from SEVEN prior EF meta-studies using robust Bayesian meta-analysis with multiple publication-bias models: moderate-to-strong evidence of publication bias in EVERY analysis; bias-corrected means g = 0.01 (performance), 0.15 (retention), 0.09 (transfer), 0.06 (EMG), -0.01 (the "farther is better" distance effect); BAYES FACTORS FAVORED THE NULL IN EVERY ANALYSIS (BF01 = 1.3 to 5.75); large residual heterogeneity.
POPULATION: n/a (novices, lab tasks)
EVIDENCE: EMERGING / CONTESTED
CAUSALITY: INTERVENTION
SOURCE: Chua LK, Jimenez-Diaz J, Lewthwaite R, Kim T, Wulf G (2021), Psychological Bulletin 147(6):618-645; McKay B, Corson A, Seedu J, De Faveri C, Hasan H, Arnold K, Adams FC, Carter MJ (2024), Psychological Bulletin 150(11):1347-1362, PMID 39480294
COACHING: Honest label: EMERGING/CONTESTED, not ESTABLISHED. The direction is plausibly positive; the bias-corrected magnitude is near-trivial (g ~ 0.1). "MORE DISTAL IS BETTER" IS FOLKLORE (g = -0.01). Use external cues as a LOW-COST DEFAULT with weak average benefit, and MEASURE individual response rather than assuming it. Elite pitchers frequently self-report internal cues that work for them; the data do not license overriding that.
CONFIDENCE: high that it is contested
SEE ALSO: F-190, F-191, F-197

### F-190 | The motivational pillars of OPTIMAL theory are essentially unsupported
TOPIC: motor learning, self-controlled practice, autonomy support, enhanced expectancies, OPTIMAL, folklore
CLAIM: Self-controlled practice, enhanced expectancies and autonomy support do not survive bias correction, and the theory's causal mechanism was almost never tested.
NUMBERS: SELF-CONTROLLED PRACTICE — k = 52, N = 2,061; naive g = 0.44 [0.31, 0.56] -> after correcting for selective reporting g = 0.107 [0.047, 0.18]; published studies showed benefits, unpublished did not; p-curve indicated inadequate evidential value; authors: "not currently distinguishable from zero." ENHANCED EXPECTANCIES + AUTONOMY SUPPORT — reporting bias plus underpowered designs "substantially exaggerated" both; secondary reporting gives bias-corrected EE d ~ 0.26 [-0.07, 0.63] and AS d ~ 0.034 (PARTIALLY VERIFIED, paywalled; the qualitative conclusion is verified). THE MECHANISM WAS NEVER TESTED — of 166 experiments testing OPTIMAL predictions, only 21% (n = 35) measured motivation at all; of those, ~23% showed group-level motivational effects; of those 8, only 5 also showed learning benefits. DIRECT HIGH-POWERED FAILURES: autonomy support and reduced feedback frequency had trivial effects on golf putting; irrelevant-choice AS showed no benefit; learner-controlled feedback schedules not advantageous; autonomy-supportive instructional language did not beat controlling language.
POPULATION: n/a (novices)
EVIDENCE: FOLKLORE (as applied learning levers)
CAUSALITY: INTERVENTION
SOURCE: McKay B, Yantha ZD, Hussien J, Carter MJ, Ste-Marie DM (2022), Meta-Psychology 6; McKay B, Bacelar MFB, Parma JO, Miller MW, Carter MJ (2023), IRSEP 18:242-262; Parma JO, Miller MW, Bacelar MFB (2024), Psychology of Sport and Exercise 74:102690; McKay & Ste-Marie (2020, 2022); Yantha et al. (2022); St. Germain et al. (2023, 2024)
COACHING: Giving pitchers choices and telling them they're doing great may be good coaching for adherence and rapport. THERE IS NO CREDIBLE EVIDENCE IT ACCELERATES MOTOR LEARNING. Do not build a program around it and do not claim a learning mechanism.
CONFIDENCE: high
SEE ALSO: F-189, F-192

### F-191 | Coaches cue internally about 2:1 against the (weak) evidence — and athletes prefer it that way
TOPIC: motor learning, cue design, internal focus, external focus, field study, preference
CLAIM: In a field study of instructional statements to elite youth pitchers, only about a third of focus-inducing statements were external, and the pitchers reported preferring internal instruction.
NUMBERS: six coaches, 70 elite youth pitchers (mean 15.3 yr — SAMPLE MISMATCH), four weeks, 1,699 recorded instructional statements; of the 717 that induced a specific focus, only 224 (31%) were external
POPULATION: off_population_HS
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: "Focus of attention instructions during baseball pitching training," International Journal of Sports Science & Coaching (2018), TU Delft
COACHING: An external-focus conversion is a change the athlete will initially DISLIKE. Plan for that.
CONFIDENCE: medium
SEE ALSO: F-189

### F-192 | THE GUIDANCE HYPOTHESIS IS FALSIFIED
TOPIC: motor learning, feedback, guidance hypothesis, faded feedback, bandwidth, KR, folklore
CLAIM: Reduced relative feedback frequency has no significant effect at any time point, no significant moderators, and does not produce the acquisition-to-retention dissociation the hypothesis predicts.
NUMBERS: 61 eligible papers, k = 75, N = 2,228. No significant effect at any time point. No significant moderators — frequency, amount of practice, bandwidth vs faded vs yoked schedule all non-significant. No significant change in effect from acquisition/immediate retention to delayed retention. Authors: "The guidance hypothesis is not supported by the extant research."
POPULATION: n/a (novices)
EVIDENCE: FOLKLORE (the hypothesis)
CAUSALITY: INTERVENTION
SOURCE: McKay B, Hussien J, Vinh MA, Mir-Orefice A, Brooks H, Ste-Marie DM (2022), Psychology of Sport and Exercise; original claim Salmoni AW, Schmidt RA, Walter CB (1984), Psychological Bulletin 95:355-386
COACHING: This is the most widely taught applied principle in coaching education and it does not hold up. AND IT CUTS BOTH WAYS: the fashionable advice to WITHHOLD Trackman/Rapsodo data from pitchers to "avoid dependency" has NO empirical support either. Neither does the opposite claim that more data is better. THE DEFENSIBLE POSITION IS AGNOSTIC: feedback FREQUENCY is not a major learning lever. What matters is feedback CONTENT and VALIDITY — does the metric actually index command? — and whether TESTING is done without feedback, for MEASUREMENT reasons (F-187), not guidance-hypothesis reasons.
CONFIDENCE: high
SEE ALSO: F-187, F-190, F-185

### F-193 | Contextual interference is NOT supported in applied settings with skilled performers
TOPIC: motor learning, contextual interference, blocked, random, interleaved, applied, field
CLAIM: The contextual-interference benefit is large in laboratory settings and negligible and non-significant in applied/field settings.
NUMBERS: 54 studies, 2,068 participants, 194 effect sizes. Overall retention SMD = 0.63 [0.33, 0.93] (0.43 after outlier removal). BY SETTING: LABORATORY SMD = 0.92 [0.48, 1.36] vs APPLIED/FIELD SMD = 0.23 [-0.16, 0.62], p = 0.24 — negligible and non-significant. BY AGE: young (<18) SMD = 0.02 (null); adults 0.63; older adults 1.45. I2 = 88-90%; NO formal publication-bias test reported. Separately: "The myth of contextual interference learning benefit in sports practice" found NO CI benefit in sports settings at acquisition, retention or transfer; a multilevel meta-analysis found only ~20% of 183 pooled outcomes agreed with the paradoxical CI pattern. Earlier: Brady (2004), 61 studies, 139 ES, mean ~0.38 — pools fine lab and gross sport skills, no baseline-equivalence requirement, weak by current standards. THE FAMOUS BASEBALL STUDY: 30 collegiate players, n = 10 PER GROUP (random, blocked, no-extra-practice control), 12 extra BP sessions over 6 weeks, 45 pitches each (15 FB / 15 CB / 15 CH); pretest-to-random-transfer improvement random +56.7%, blocked +24.8%, control +6.2%.
POPULATION: n/a (mostly novices; the baseball study is HITTERS)
EVIDENCE: ESTABLISHED (lab) / NOT SUPPORTED (applied)
CAUSALITY: INTERVENTION
SOURCE: Czyz SH, Wojcik A, Solarska P, Kiper P (2024), Scientific Reports 14:15974; Ammar A, Trabelsi K, Boujelbane MA, Boukhris O, Glenn JM, Chtourou H, Schollhorn W (2023), Educational Research Review 39:100537; Hall KG, Domingues DA, Cavazos R (1994), Percept Mot Skills 78(3 Pt 1):835-841, PMID 8084699; Farrow & Buszard (2017); Buszard et al. (2017)
COACHING: The CI effect is LEAST well-supported precisely in the population this program serves. The famous baseball study is n = 10 per cell, one team, one coach, unblinded, no delayed retention beyond the 6-week endpoint, no effect sizes reported — and IT IS A HITTING STUDY being generalized to pitching, a different task class (self-paced, no reactive component). Cite it as suggestive, never as evidential. WHAT SURVIVES, IN A NARROWER FORM: practicing pitch-to-pitch variation the way it occurs in competition improves transfer to competition — which is the SPECIFICITY/representative-design argument (F-197), not the CI-elaboration argument. There is a live published methodological exchange; the debate is not settled.
CONFIDENCE: high that applied support is absent
SEE ALSO: F-194, F-197, F-185

### F-194 | Variable practice and Differential Learning — theory abandoned, effect unreliable
TOPIC: motor learning, differential learning, variable practice, schema theory, single lab bias
CLAIM: Schema theory is largely abandoned in its original form, and the Differential Learning literature has a serious single-lab and publication-bias problem.
NUMBERS: DL META: 27 articles / 31 experiments, N = 897 (DL 453, control 446). Acquisition d = 0.26 [0.10, 0.42]; retention d = 0.61 [0.30, 0.91]; sport-technical retention d = 0.63 [0.34, 0.91]. BUT: high risk of bias, I2 = 77-79%, substantial publication-bias concerns, most studies from a single research group (the originator's), low power throughout. The authors themselves state that inferences about DL effectiveness "would be premature."
POPULATION: n/a
EVIDENCE: EMERGING (with a serious allegiance problem)
CAUSALITY: INTERVENTION
SOURCE: Tassignon B et al. (2021), Frontiers in Psychology 12:533033; original schema theory Schmidt RA (1975), Psychological Review 82:225-260
COACHING: "Differential learning improves pitching command" is FOLKLORE — NO DIRECT EVIDENCE IN PITCHERS EXISTS. Given how aggressively DL is marketed in baseball (weighted and odd-shaped implements, constraint drills sold as DL), that gap should be stated plainly. Effect sizes are exactly the magnitude that bias correction has repeatedly reduced to zero elsewhere in this literature. Independent critiques argue that structured variation WITH corrections — which contradicts DL's core premise — outperforms DL protocols.
CONFIDENCE: high that the claim as marketed is unsupported
SEE ALSO: F-193, F-195, F-185

### F-195 | The constraints-led approach is a framework, not an evidence-based intervention
TOPIC: motor learning, constraints led, CLA, ecological dynamics, nonlinear pedagogy, RCT
CLAIM: The best available systematic review of nonlinear/constraints-led interventions found most technical outcomes showed no difference, with benefits concentrated in tactical outcomes and all studies carrying risk-of-bias concerns.
NUMBERS: nine studies, youth to elite, 78% SOCCER, ages 9-27, mean 15.8 +/- 6.6 sessions. TECHNICAL OUTCOMES: 66% showed NO difference; 34% favored nonlinear. TACTICAL: after removing high-bias studies, 66% favored nonlinear (decision-making, game sense). RISK OF BIAS: all six RCTs "some concerns" under RoB 2; two non-randomized studies "serious risk." Heterogeneity prevented meta-analysis. FOR PITCHING SPECIFICALLY: ZERO RCTs.
POPULATION: n/a (78% soccer)
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Bromilow S, Milne N, Woods CT, Dowsett J, Keogh JWL (2025), Sports Medicine - Open 11:90; Newell's constraints model (1986)
COACHING: Note the mismatch — pitching command is largely a CLOSED, SELF-PACED skill, while the tactical/decision-making outcomes where CLA looks best are the outcomes LEAST relevant to raw command. Constraint manipulation for pitchers is DEFENSIBLE-BY-ANALOGY, NOT EVIDENCED. Its real practical virtue is that it disciplines the coach into changing the ENVIRONMENT rather than adding another verbal cue.
CONFIDENCE: high that it is a framework rather than an intervention
SEE ALSO: F-182, F-194

### F-196 | REFUTED — there is no speed-accuracy trade-off in overarm throwing
TOPIC: motor learning, speed accuracy, Fitts law, effort, RPE, submaximal, folklore, impulse variability
CLAIM: Spatial error showed no significant relationship with speed across 40-100% of maximum in overarm throwing, and force-output variability peaked around 60% of maximum.
NUMBERS: n = 30 (16 skilled, 14 unskilled), tennis ball, target at 30 ft, seven percentages of maximum velocity (40-100%) in random order, 9 trials per condition. (1) Throwing-velocity variability rose from 40%, PEAKED AT 60%, then decreased at every higher interval — supporting the inverted-U from impulse-variability theory. (2) SPATIAL ERROR SHOWED NO SIGNIFICANT RELATIONSHIP WITH SPEED ACROSS THE ENTIRE 40-100% RANGE. A children's replication FAILED to find the inverted-U, so part 1 is contested; part 2 is the more robust half.
POPULATION: unspecified — SAMPLE MISMATCH (tennis ball, mixed skill, short distance)
EVIDENCE: EMERGING
CAUSALITY: INTERVENTION
SOURCE: Urbin MA, Stodden DF, Boros R, Shannon D (2012), Motor Control 16(1):19-30, PMID 22402218; children's replication Motor Control (2018), PMID 28657818
COACHING: "TAKE A LITTLE OFF AND THROW A STRIKE" IS NOT SUPPORTED. Force-output variability is HIGHEST around 60% of maximum, which is exactly where "take something off" lands the athlete. Submaximal command work may be simultaneously the least accurate and the least specific thing in the program. This dovetails with the effort-level findings (F-211): perceived effort is a badly calibrated instrument. Driveline's own protocol independently arrived at the same rule — RPE minimum 70%, preferably higher.
CONFIDENCE: medium for part 2, low for part 1
SEE ALSO: F-211, F-185

### F-197 | GAP — no bullpen-to-game command transfer evidence exists in baseball
TOPIC: motor learning, transfer, specificity, representative design, bullpen, game, gap
CLAIM: No peer-reviewed intervention study tests whether a bullpen-design manipulation improves in-game command.
NUMBERS: zero studies
POPULATION: n/a
EVIDENCE: UNSOURCED (as an absence)
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 10.7 — described as "the largest hole in the applied command literature"
COACHING: What DOES exist is biomechanical evidence that bullpen is not game, which supports the specificity argument indirectly: pitch-to-pitch variability in-game vs lab (F-200), pitchers throwing meaningfully slower in lab/no-batter conditions, and kinematics differing with a batter present and on mound vs flat ground. THE DEFENSIBLE CLAIM: "Representative bullpen design is theoretically indicated and biomechanically motivated; its transfer benefit in pitchers is untested." MEASUREMENT COROLLARY: since acquisition is not learning, evaluation of any command intervention must use IN-GAME command metrics across a subsequent window, not bullpen hit rates. A frequently cited "Differences between bullpen and game baseball pitching biomechanics" appears on ResearchGate only — no verifiable peer-reviewed journal version found. UNVERIFIED, do not cite.
CONFIDENCE: high that the gap exists
SEE ALSO: F-187, F-186, F-193

### F-198 | Dosage — distributed practice at the SESSION level, and no dose-response for command reps
TOPIC: motor learning, dosage, spacing, distributed practice, massed, reps, sleep, volume
CLAIM: Distributed beats massed at the level of SESSIONS, with strong task-type moderation; there is no dose-response curve for throwing-accuracy practice volume.
NUMBERS: Donovan & Radosevich (1999), J Applied Psychology 84:795-805 — meta-analysis, effect strongly moderated by task type and interstudy interval ("now you see it, now you don't"); larger spacing advantages for SIMPLER tasks, smaller or reversed for complex ones. Lee & Genovese (1988), RQES 59:277-287 — distributed practice benefits PERFORMANCE more than LEARNING. Spruit, Band & Hamming (2015), Surgical Endoscopy 29:2235-2243 — laparoscopic training, 3x75 min in one day vs 1x75 min/week for 3 weeks: SPACED better at end of training, at 2-week retention AND at 1-year retention; 65% of the spaced group vs 21% of massed reached proficiency (the closest analogue to a dosage RCT available; still novice surgeons). COUNTER-EVIDENCE AT SHORT INTERVALS: Dutra et al. (2026), QJEP 79(4):896-904 found 2-s inter-trial intervals BEAT 30-s for a serial key-press task — INTER-TRIAL and INTER-SESSION spacing are different phenomena, do not conflate them. SLEEP: Schmid D, Erlacher D, Klostermann A, Kredel R, Hossner E-J (2020), Neurosci Biobehav Rev 118:270-281 — 48 studies, 53 sleep groups (n = 829) vs 53 wake groups (n = 825); overall relative sleep gain g = 0.43; finger tapping 0.47; mirror tracing 0.62.
POPULATION: n/a
EVIDENCE: EMERGING to ESTABLISHED (cross-domain)
CAUSALITY: INTERVENTION
SOURCE: as listed
COACHING: Practical inference at weak-to-moderate confidence: spreading a fixed volume of command work across MORE, SHORTER sessions per week is better supported than consolidating it into fewer long bullpens. This also aligns with arm-health constraints. SLEEP CAVEAT MATTERS ENORMOUSLY: the sleep-consolidation effect is largely demonstrated on EXPLICIT MOTOR SEQUENCE tasks, not continuous/ballistic whole-body skills — generalizing "sleep consolidates your bullpen" to a pitching delivery is UNWARRANTED EXTRAPOLATION. Advocate sleep on other grounds; those arguments are stronger. REPS PER SESSION: no direct evidence exists for pitching command; anyone quoting an optimal number of command reps is extrapolating. On dart/free-throw studies: dominated by small single-session studies on novices with NO retention tests — mechanistic hints only, never programming guidance for pitchers.
CONFIDENCE: medium for the session-spacing inference, high that the rep dose-response gap is real
SEE ALSO: F-138, F-185, F-197

---

# 13 — MEASUREMENT AND TECHNOLOGY

### F-199 | Markerless motion capture — ~5 cm of joint-centre error, fine for kinematics, risky for kinetics
TOPIC: measurement, markerless, Hawk-Eye, Theia3D, KinaTrax, MPJPE, accuracy, kinetics
CLAIM: Multi-camera markerless systems show roughly 5 cm of per-joint position error against marker-based capture, which is acceptable for some kinematics and potentially serious for computed kinetics.
NUMBERS: Hawk-Eye MPJPE 56.6 +/- 9.4 mm; Theia3D 52.0 +/- 12.3 mm; n = 18 collegiate pitchers. STRIDE LENGTH showed the strongest cross-system agreement (CCC > 0.85); SHOULDER ROTATIONAL VARIABLES showed the greatest variability. KinaTrax: 8 synchronized cameras at 300 Hz, deployed in MLB parks and collegiate stadiums; a published normative study covered 51 pitchers from 5 collegiate teams during the 2023 season. Hawk-Eye: ~12 cameras up to 300 fps.
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Aguinaldo AL, Cardinale T, La Salle DT, Escamilla RF, Buffi JH (2026), J Sports Sci, PMID 41294254
COACHING: KINEMATICS FROM MARKERLESS: GOOD. KINETICS FROM MARKERLESS: TREAT WITH CAUTION, NEVER COMPARE ACROSS SYSTEMS — inverse-dynamics torque is sensitive to joint-centre location AND to the SECOND DERIVATIVE of position. NOTE THE PATTERN: the variable with the cleanest in-band effect size (stride length) is also the one that measures most consistently, and the variables with the most suspicious pooled effect sizes (MER, shoulder rotation) are the ones that measure worst. That is not a coincidence.
CONFIDENCE: high
SEE ALSO: F-200, F-201, F-192

### F-200 | Variability transfers across capture methods; absolute means do NOT
TOPIC: measurement, markerless, in-game, variability, thresholds, transfer, comparability
CLAIM: Pitch-to-pitch variability is broadly similar between lab marker-based and in-game markerless capture, while absolute means are not transferable.
NUMBERS: 30 lab marker-based vs 30 NCAA D1 in-game markerless; only 2 of 10 kinematic parameters showed significantly greater in-game variability
POPULATION: NCAA_D1
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Lerch BG, Fleisig GS, Slowik JS, Oliver GD (2025), J Biomech 188:112775, PMID 40418881
COACHING: Encouraging — in-game markerless is capturing real movement, not noise. Within-system regression SLOPES are probably comparable across the literature. But ABSOLUTE THRESHOLDS — "80% of body height," "28 degrees of trunk tilt" — ARE SYSTEM-SPECIFIC AND MUST NOT BE TRANSPORTED BETWEEN STUDIES. This alone may explain the lead-knee and stride-length magnitude contradictions (F-047, F-050).
CONFIDENCE: high
SEE ALSO: F-047, F-050, F-199

### F-201 | Single-camera markerless error EXCEEDS the effect sizes being measured
TOPIC: measurement, pitchAI, single camera, error, stride length, arm speed, validation
CLAIM: Single-camera markerless produces stride-length and arm-speed errors larger than the mechanical effects the corpus is trying to detect.
NUMBERS: time-series joint-angle R2 = 0.69-0.98; RMSE from 4.37 deg (trunk lateral tilt) to 20.78 deg (glove-arm shoulder ER); ARM SPEED ERROR 3.62 m/s; STRIDE LENGTH ERROR 5.75% OF BODY HEIGHT. Recall that a 10% BH stride change is what is worth ~0.9 m/s of ball velocity.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Dobos TJ et al. (2025), Sports Biomech, PMID 36409062
COACHING: THE MEASUREMENT ERROR IS MORE THAN HALF THE EFFECT. Single-camera markerless is not adequate for these effect sizes. If you cannot measure his stride to better than ~2% BH repeatably, you cannot run a stride project. Establish his own TEST-RETEST ERROR before claiming any change.
CONFIDENCE: high
SEE ALSO: F-043, F-199

### F-202 | Motus/PULSE "Stress" is NOT elbow varus torque
TOPIC: measurement, sleeve, IMU, Motus, PULSE, stress, workload, validity, comparison
CLAIM: The sleeve's Stress metric runs substantially below lab-measured elbow torque while correlating strongly with it.
NUMBERS: sleeve Stress ran 41 N-m (38.7%) BELOW lab-measured elbow torque, and 42 N-m (39.3%) below shoulder torque, though correlations to the lab metrics were extremely strong. Original vendor claim was a 0.99 intraclass correlation to ASMI's measurements. Independent comparison against marker-based mocap gives the same overall picture — correlated, not equivalent.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Boddy KJ, et al. (2019), PeerJ, PMC6348088; Camp CL, Loushin S, Nezlek S, Fiegen AP, Christoffer D, Kaufman K (2021), AJSM
COACHING: It is a RELATIVE WITHIN-ATHLETE WORKLOAD INDEX, and a good one. Use it to track a single athlete's load over time. NEVER compare a sleeve number to a published torque value, NEVER to the 32 N-m UCL failure figure (F-097), and NEVER between two different athletes as if they were the same physical quantity. Sleeve output is sensitive to placement, fit and skin motion — standardize placement or the longitudinal tracking degrades.
CONFIDENCE: high
SEE ALSO: F-097, F-091

### F-203 | Sampling rate and filter cutoff materially change computed pitching data
TOPIC: measurement, filter, sampling rate, inverse dynamics, torque, comparability, methodology
CLAIM: Published studies sample at 240-500 Hz with low-pass filter cutoffs varying widely, and those choices materially change the computed data.
NUMBERS: sampling 240-500 Hz; filter cutoffs 13.4 and 18.0 Hz most common
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Dowling B, Slowik JS, Fleisig GS (2026), Sports Biomechanics, DOI 10.1080/14763141.2026.2625797
COACHING: Since inverse-dynamics torque rides on the SECOND DERIVATIVE of position, filter cutoff is not a detail — it is a large fraction of the answer. This is the mechanism behind the 64 vs 100 vs 120 N-m spread across labs (F-091). OPERATING RULE ADOPTED: A TORQUE NUMBER WITHOUT ITS SAMPLING RATE AND FILTER CUTOFF IS NOT A NUMBER.
CONFIDENCE: high
SEE ALSO: F-091, F-199

### F-204 | Frame rate — 240 fps minimum for anything at or distal to the shoulder
TOPIC: measurement, video, frame rate, shutter speed, camera, 240 fps, acceleration phase
CLAIM: At consumer frame rates you get essentially no frames in the entire arm-acceleration phase.
NUMBERS: 30 fps = 33.3 ms/frame = ~1 frame in the ~40 ms acceleration phase (unusable); 60 fps = 16.7 ms = ~2 frames (unusable); 120 fps = 8.3 ms = ~5 frames (minimum viable); 240 fps = 4.2 ms = ~10 frames (practical standard); 300-1000 fps = 3.3-1.0 ms = 12-40 frames (research-grade). Shutter speed 1/1000 s or faster to avoid motion blur.
POPULATION: n/a
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 7.6
COACHING: Modern phones do 240 fps at 1080p. Shutter speed matters as much as frame rate, which means a lot of light. CAMERA POSITIONS: (1) open side, perpendicular to the rubber-plate line, at hip height — stride length, forward trunk tilt, lead-knee flexion/extension, arm slot, FC/MER/BR timing; (2) closed side — hip-shoulder separation, scapular loading, elbow position relative to trunk; (3) straight-on — lateral trunk tilt, foot placement relative to midline, foot angle, arm slot; (4) overhead — foot angle and stride direction.
CONFIDENCE: high
SEE ALSO: F-088, F-205

### F-205 | What 2D video CAN and CANNOT measure
TOPIC: measurement, video, 2D, claims, honesty, torque, separation, MER, angular velocity
CLAIM: A single camera cannot measure a 3D angle, and there are hard limits on what may be claimed from 240 fps 2D video.
NUMBERS: —
POPULATION: n/a
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 7.6; coaching-translation.md 8
COACHING: RELIABLY MEASURABLE from 240 fps 2D — stride length as % height (needs a calibrated reference in frame), foot placement relative to midline and foot angle, lead-knee flexion at FC and at BR and whether it extends or collapses, approximate forward and lateral trunk tilt at release (view-dependent), the FC/MER/BR timing landmarks and the intervals between them, whether the pelvis clearly leads the trunk (gross sequencing). NOT MEASURABLE WITHOUT 3D — max shoulder external rotation (composite and badly perspective-distorted), hip-shoulder separation AS A NUMBER, ANY angular velocity, AND ANY TORQUE OR FORCE WHATSOEVER. Be honest with the athlete about this.
CONFIDENCE: high
SEE ALSO: F-204, F-058, F-134

### F-206 | Never mix pitch-tracking systems
TOPIC: measurement, Trackman, Rapsodo, Hawk-Eye, radar, optical, comparability, device change
CLAIM: Radar and optical tracking measure different things and produce systematically different values.
NUMBERS: Trackman is Doppler radar, long-standing reference for velocity/spin. Rapsodo is optical + radar hybrid — validation found Rapsodo velocity significantly LOWER than Trackman, spin slightly slower. Hawk-Eye is 12 optical cameras up to 300 fps, giving full 3D trajectory, spin axis and seam orientation.
POPULATION: n/a
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Driveline Baseball (2016), "Rapsodo, Trackman, and Pitch Tracking Technologies"
COACHING: Pick one and never mix. Movement and spin-direction differences BETWEEN systems should be EXPECTED, not treated as error. A "velocity gain" that coincides with a device change is not a velocity gain. One gun, one position, one operator — a radar change mid-project ends the project.
CONFIDENCE: high
SEE ALSO: F-162, F-243

### F-207 | Force plates measure directly — but the meaningful quantity has no published elite norms
TOPIC: measurement, force plate, GRF, braking impulse, norms, gap, purchase decision
CLAIM: Ground reaction force is directly measured with no inverse-dynamics assumptions, but braking impulse in %BW-s — the mechanically meaningful quantity — has no published elite norms.
NUMBERS: dual in-ground plates give propulsive GRF, braking GRF and impulse directly; cost is an order of magnitude below a full mocap lab. Elite braking-impulse norms in %BW-s: NOT PUBLISHED — searched for across three sweeps and not found.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (the instrument) / UNSOURCED (the norms)
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 4.6, 7.5; open-disputes.md #4
COACHING: DIRECTLY MEASURED IS NOT THE SAME AS IMPORTANT. After controlling for bodyweight, lead-leg GRF explains ~4-6% of between-pitcher velocity variance (F-061), while modeled torque predicts UCL surgery (F-095). Precision and importance are different things, and force plates are frequently sold as if they were the same. You would be buying an instrument to measure a variable with no reference values — fine for within-athlete tracking, useless for evaluation. Say so on the purchase order.
CONFIDENCE: high that the norms gap is real
SEE ALSO: F-060, F-061, F-095

### F-208 | LAB VELOCITY IS NOT GAME VELOCITY — the ~5-8 mph gap that bounds every kinetic number
TOPIC: measurement, lab velocity, game velocity, gap, kinetics, underestimate, norms
CLAIM: Pitchers throw slower in the laboratory than in games, so published lab kinetics likely UNDER-represent competitive load.
NUMBERS: ASMI's professional database averages 38.1 +/- 4.1 m/s = 85.2 +/- 9.2 mph IN LAB; the Fleisig UCL prospective cohort averaged 84.7-85.0 mph in-lab for pitchers throwing 92-95 in games. Comparing a game TrackMan reading to a lab norm overstates the athlete by ~5-8 mph.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: Escamilla RF et al. (2023), PMC10601404; Fleisig GS et al. (2025), PMC12227930; Lerch et al. (2025)
COACHING: A lab-measured 85 mph pro is likely a 90-93 mph game arm. Do not read published lab means as game velocities, and do not conclude the pro database "only throws 85." Every torque figure in this corpus is probably a FLOOR.
CONFIDENCE: high
SEE ALSO: F-089, F-091, F-176

### F-209 | The realistic elite-program measurement stack
TOPIC: measurement, technology, stack, purchase, radar, camera, force plate, sleeve, markerless
CLAIM: There is a defensible cheapest-to-most-capable ordering for what an elite program should buy.
NUMBERS: cost of full marker-based mocap $100k-$500k+ installed plus a biomechanist — not accessible to a private coach, and it cannot capture a game
POPULATION: n/a
EVIDENCE: EMERGING
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 7.6
COACHING: (1) Radar (one system, consistently) + two 240 fps cameras — the floor. (2) Add dual force plates — the highest value-per-dollar addition, with F-207's caveat. (3) Add a PULSE sleeve for longitudinal within-athlete workload, never as a torque number. (4) Portable markerless (Theia3D/pitchAI) for kinematics. (5) Full markerless in-stadium (KinaTrax) — collegiate/professional programs only.
CONFIDENCE: medium
SEE ALSO: F-202, F-204, F-207

### F-210 | The OpenBiomechanics Project is a DATASET, not a paper
TOPIC: measurement, dataset, OpenBiomechanics, citation, licence, force plate, POI metrics
CLAIM: The dataset is real and excellent; the journal article is not confirmed to exist.
NUMBERS: ~411 fastballs / ~100 pitchers, HS to affiliated pro, force plates + 81 POI metrics per trial (also recorded elsewhere in the corpus as 76 measurement points)
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (the dataset) / UNSOURCED (the paper)
CAUSALITY: MECHANISM
SOURCE: Driveline Baseball Research and Development; Kyle Boddy. GitHub drivelineresearch/openbiomechanics, CC BY-NC-SA 4.0
COACHING: The repository's own CITATION.cff lists type DATASET with no DOI. CITE IT AS A DATASET, not a publication. Note the licence also forbids use by employees, contractors or significant shareholders of professional sports organizations and financial analysis firms.
CONFIDENCE: high
SEE ALSO: F-221

---

# 14 — COACHING OPERATIONS: EFFORT, CONSTRAINTS, RULES, AND THE BETWEEN-START MAP

### F-211 | Effort-level dosing — the strategy is defensible, the load arithmetic is poor
TOPIC: effort, RPE, submaximal, varied effort, torque reduction, radar gated, dosing
CLAIM: Reducing perceived effort reduces elbow torque, but sublinearly and inefficiently, and the three primary datasets disagree with each other on whether kinematics are preserved.
NUMBERS: Fiegen 2023 (n = 10 HS, OFF-POPULATION) — at 75% perceived effort: 81% of max elbow stress, 90% of max velocity; per 25% effort reduction -13% stress, -7.5% velocity. Wolf 2025 (n = 19 collegiate, KinaTrax) — only elbow varus torque differed by effort, and only 100% vs 60%: 92.5 -> 73.2 N-m (P = .017); KINEMATICS UNCHANGED across all five effort levels. Hyeamang 2026 (n = 38 HS + 24 PROFESSIONAL) — at 50% RPE, HS pitchers threw 86% of max velocity, 75% of max varus torque, 80% cumulative torque, 67% torque loading rate; PROS FAR MORE CONSISTENT at submaximal efforts than HS.
POPULATION: mixed (one professional subsample)
EVIDENCE: ESTABLISHED (small samples)
CAUSALITY: INTERVENTION (acute)
SOURCE: Fiegen AP, Nezlek SP, Loushin SR, et al. (2023), AJSM, PMID 36625428; Wolf JH, Kinney S, Waterman BR, Bullock GS, Nicholson K (2025), OJSM, PMID 40933947; Hyeamang LJ, Dowling B, Hodakowski A, et al. (2026), OJSM, PMID 41573128; proposal in Fleisig GS (2026), Sports Biomech, PMID 42312376
COACHING: Asking for 25% less effort buys ~13-19% less stress at ~7.5-10% of velocity. Asking for HALF effort buys only ~20-25% less stress. THERE IS NO DOSING REGIME HERE THAT PRODUCES A LARGE STRESS REDUCTION AT A SMALL VELOCITY COST. Fleisig's STRATEGIC case (deception, disrupting hitter timing) is separate from and probably stronger than his LOAD case. PRACTICAL FIX: submaximal throwing days are RADAR-GATED, NOT FEEL-GATED — give a target VELOCITY BAND with the gun visible, not a target effort percentage. THE UNRESOLVED DISAGREEMENT: if Wolf is right that kinematics are preserved at 60%, submaximal work is a clean training stimulus; if Hyeamang is right that HS pitchers are highly variable at submaximal effort, submaximal work in a young arm is a different, sloppier movement — a motor-learning problem on top of a load problem. FAILURE ON VIDEO: kinematic drift at the FC frame between his hardest and softest pitch in the same set.
CONFIDENCE: medium — small samples, and the three primary studies disagree
SEE ALSO: F-196, F-186, F-185

### F-212 | Constraint-design heuristics — four levers, and a rule for using them
TOPIC: constraints, drill design, implement mass, moment of inertia, center of mass, time
CLAIM: A published framework identifies four constraint levers and an organizing principle for why a constraint works.
NUMBERS: (1) IMPLEMENT MASS — heavier = longer force application, lower peak force, teaches position and relaxation; lighter = higher peak force, MAGNIFIES sequencing errors at speed. (2) MOMENT OF INERTIA (size/shape) — larger implements demand prolonged external rotation before IR; linear implements (javelin) force centre-of-mass management along the pull line. (3) CENTRE-OF-MASS KINEMATICS — mound vs flat, displacement from target, pre-throw velocity (pulldown, drop-step, roll-in); manipulates rotational vs linear momentum. (4) DISTAL LIMB KINEMATICS — preset arm positions (90/90, figure-8, javelin) remove degrees of freedom; fastest route to a new arm path and the easiest to over-use.
POPULATION: professional_mixed
EVIDENCE: EMERGING (framework) / UNSOURCED (specific dosing)
CAUSALITY: MECHANISM
SOURCE: Crider B / Driveline Baseball (Feb 2025), "Constraint Based Learning Heuristics for Throwers"
COACHING: Organizing principle, adopted verbatim: "Manipulating time is the most valuable tool you have" — shape the force-time curve to maximize impulse into the implement. STRESS COST: none of these have published kinetics at the 85+ level except weighted implements, where the evidence is split. A constraint that changes the arm path changes the torque, and nobody has measured most of them. Use is: heavy for organization, light for exposure; MOI is the route to changing elbow flexion at FC without cueing the elbow.
CONFIDENCE: medium as a framework, low as dosing
SEE ALSO: F-100, F-029, F-195

### F-213 | The four standing coaching rules, and the retired-cue ledger
TOPIC: coaching, rules, cue, stress cost, foot contact, norms, feelable, retired cues
CLAIM: Four rules govern how any finding in this corpus becomes a coaching instruction, and eleven cues have been formally retired.
NUMBERS: —
POPULATION: professional_mixed
EVIDENCE: n/a (operating doctrine)
CAUSALITY: MECHANISM
SOURCE: coaching-translation.md 1, 2, 9, 12
COACHING: RULE 1 — no velocity cue without its stress cost (within an athlete, velocity and elbow varus torque are locked at R2 = 0.957; what you CAN sell is a better exchange rate, since elite arms at the same velocity differ by 28% in normalized torque). RULE 2 — everything is decided by foot contact; if a fix has to happen after front-foot strike it is not a fix, it is a wish. RULE 3 — coach the position, measure the trend, never the norm. RULE 4 — if the pitcher cannot feel it, it is not a cue; science stated at a precision the athlete cannot act on is science you have wasted. RETIRED CUES: "the block whips the hips" (F-062); "get on top of the ball" (F-070); "fix your kinematic sequence" (F-105, F-106); "more layback" / chase MER (F-102, F-134); "you lose velo from the stretch" (F-069); "velocity's still there so he's not tired" (F-127); "he needs X degrees of hip-shoulder separation" (F-058); any stride-length prescription in inches (F-047); "get your stride out toward 80% of your height" — RETIRED 2026-08-13 (F-043, F-044, F-045); "repeat your release point and you'll command the ball" — RETIRED 2026-08-13 (F-175); "he needs to stretch out his GIRD" when the deficit is osseous (F-115). NARROWED, NOT RETIRED: "drop the arm slot 5-10 degrees" — still the best stress-per-mph lever, no longer a default, because it is platoon-dependent and associated with worse command (F-070, F-071, F-176).
CONFIDENCE: high — this is the corpus's own operating doctrine
SEE ALSO: F-043, F-062, F-070, F-105, F-175

### F-214 | The between-start framework, and why it may not fit the actual athlete
TOPIC: recovery, between start, schedule, day plus one, gating, showcase, triage
CLAIM: A physiologically reasoned between-start template exists, gated on the athlete's own markers rather than the calendar.
NUMBERS: DAY 0 (start / high-intent outing) — peak load; post-outing fuel, hydrate, sleep; perceptual modalities only. DAY +1 — ROM and strength measurably still depressed; collagen net balance still NEGATIVE; low-intensity movement, blood flow, mobility; NO HIGH-INTENT THROWING. DAY +2 — collagen balance now net positive; reintroduce lower-body strength and moderate-intent throwing. DAY +3 — highest-intent secondary work / bullpen, GATED ON the athlete's own ROM and ER-strength markers having returned to his individual baseline, not on the calendar. DAY +4 — taper, mobility, sleep emphasis. THROUGHOUT — track individual baselines: ER strength, total rotational motion, elbow extension, perceived arm readiness.
POPULATION: professional_mixed
EVIDENCE: EMERGING (reasoned template, not tested)
CAUSALITY: MECHANISM
SOURCE: anatomy-physiology.md 6.5
COACHING: NOT PRESCRIPTIVE MEDICINE — discuss with medical and performance staff. TWO STANDING OBJECTIONS ON THE RECORD. (1) The framework assumes a five-day cycle, one high-intent exposure and control of the calendar; the actual athlete may be a draft-followed HS arm throwing Friday for his school, Sunday for his travel org, with a showcase Wednesday and three organizations each believing they own one appearance. The corpus NAMES this hazard (F-136) and then writes a framework that presumes it away. WHAT IS MISSING IS THE TRIAGE VERSION. (2) "Track him against his own baseline" has NO PROTOCOL — how often, by whom, at what time relative to throwing, and how many measurements before it is a baseline rather than a data point. Post-outing ROM is still down at 24 h, so a "baseline" taken on a random Tuesday in a dense stretch is not a baseline. SHOWCASE ADDENDUM: a maximal-intent outing off-schedule with low chronic load is the highest-risk exposure this population faces; if unavoidable, precede it with a genuine chronic-load ramp and a full warm-up and follow it with the same recovery map as a start.
CONFIDENCE: medium — physiologically sound, operationally incomplete
SEE ALSO: F-126, F-133, F-136, F-131

---

# 15 — UNSOURCED, FABRICATED, MISATTRIBUTED, AND MARKETING

> Every entry in this section exists so a future search surfaces the DEBUNKING rather than the myth. Grep `EVIDENCE: UNSOURCED` to list them all.

### F-215 | UNSOURCED — "collegiate pitchers lose 3-14% of strength across a season, per Wilkin & Haddock"
TOPIC: unsourced, misattribution, strength loss, in season, Wilkin, periscapular, correction
CLAIM: This is a misattribution. The named paper reports no significant change at any speed or timepoint.
NUMBERS: Wilkin & Haddock (2006), n = 9 D-II pitchers — "no differences at any speed tested or time point examined." A REAL 3-14% periscapular decline exists from a DIFFERENT 2024 IJSPT collegiate cohort (F-123), with scaption down ~8%.
POPULATION: NCAA D-II
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: misattribution documented in velocity-development.md 5.4 and 8
COACHING: The 3-14% figure is real. Do NOT attach Wilkin's name to it.
CONFIDENCE: high
SEE ALSO: F-083, F-123

### F-216 | UNSOURCED — "ASMI position statement on weighted balls"
TOPIC: unsourced, fabrication, ASMI, position statement, weighted balls, institutional claim
CLAIM: No such document exists.
NUMBERS: ASMI's actual Position Statement for Adolescent Baseball Pitchers (updated April 2013) contains ZERO text on weighted balls, weighted implements, overload/underload training, or long toss.
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: verified against asmi.org
COACHING: ASMI has PAID COURSE CONTENT titled "Are Weighted Ball Programs Safe and Effective? A Roundtable Discussion" — that is course material behind a paywall, not a position statement. Every institutional claim gets verified at the institution's own publication list or on PubMed before it enters the corpus.
CONFIDENCE: high
SEE ALSO: F-224, F-225

### F-217 | UNSOURCED — "r = .840 for trunk rotation power as the sole predictor of ball speed"
TOPIC: unsourced, fabrication, trunk rotation, correlation, garbled, discard
CLAIM: Untraceable, and almost certainly a garbled restatement of a real R2.
NUMBERS: almost certainly a garbling of Aguinaldo & Escamilla's R2 = 0.731 (F-066)
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 8 #14
COACHING: Discard.
CONFIDENCE: high
SEE ALSO: F-066

### F-218 | UNSOURCED — grip strength r = 0.705 / 0.667 / 0.655 versus fastball velocity
TOPIC: unsourced, fabrication, grip strength, correlation, Academia.edu, contradicted
CLAIM: These figures have no journal record, no DOI and no PubMed entry, and are directly contradicted by a real n = 87 D1 null.
NUMBERS: total grip r = 0.705 / dominant r = 0.667 / non-dominant r = 0.655, in a sample with a conveniently on-target mean fastball of 38.8 m/s (86.8 mph). They trace to an Academia.edu PDF only. Contradicted by Barrack 2024, n = 87 D1 at 84.83 mph, null (F-013).
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 2.4, 8 #9
COACHING: DO NOT CITE. The excellent population match is exactly why the numbers spread; it is not evidence they exist. (A separate REAL study — Tremblay M et al. 2022, Front Sports Act Living 4:822454, PMID 35425896 — reports grip tau = 0.653, but the sample spans AGES 10-22, so the correlation is substantially age-driven.)
CONFIDENCE: high
SEE ALSO: F-013

### F-219 | UNSOURCED — "Escamilla's 10-week weighted-ball program in college pitchers"
TOPIC: unsourced, fabrication, Escamilla, weighted balls, narrative review, no original data
CLAIM: No such study exists. What exists is a narrative review with no original data, no sample and no control group.
NUMBERS: Escamilla RF, Speer KP, Fleisig GS, Barrentine SW, Andrews JR (2000), Sports Medicine 29(4):259-272, PMID 10783901 — a NARRATIVE REVIEW
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 8 #3
COACHING: Do not cite it as a training study.
CONFIDENCE: high
SEE ALSO: F-222

### F-220 | UNSOURCED — a twin study or heritability estimate for throwing velocity
TOPIC: unsourced, fabrication, heritability, twin study, h2, genetics, content farm
CLAIM: None exists anywhere.
NUMBERS: the most-cited adjacent twin study (Maes 1996, MSSE, 105 twin pairs, nine motor tests, PMID 8970142) contains NO throwing test
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 6.6, 8 #15
COACHING: Any specific h2 for throwing velocity should be assumed fabricated until verified at PubMed. This is exactly where AI content farms fabricate.
CONFIDENCE: high
SEE ALSO: F-079, F-225

### F-221 | UNSOURCED — "The OpenBiomechanics Project" cited as a peer-reviewed paper
TOPIC: unsourced, citation error, dataset, OpenBiomechanics, Driveline, licence
CLAIM: The dataset is real and excellent; the journal article is not confirmed to exist.
NUMBERS: the repository's CITATION.cff lists only "Driveline Baseball Research and Development; Kyle Boddy," type DATASET, with no DOI
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 8 #11
COACHING: Cite it as a dataset (GitHub, CC BY-NC-SA 4.0), not as a publication.
CONFIDENCE: high
SEE ALSO: F-210

### F-222 | UNSOURCED — a pooled meta-analytic mph figure for weighted-ball training
TOPIC: unsourced, meta-analysis, weighted balls, pooled effect, Caldwell, fabrication
CLAIM: No pooled velocity estimate for weighted-ball training exists.
NUMBERS: the systematic review of 10 studies from 4,119 titles performed NO meta-analysis and reports NO pooled effect size; heterogeneity was judged too great; its verdict was "the quality of available evidence was determined to be very poor." The overarm-throwing systematic review also provides no pooled estimate.
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: Caldwell JE, Alexander FJ, Ahmad CS (2019), OJSM 7(2), PMID 30800693 / PMC6378453
COACHING: ANY "pooled mph" attributed to Caldwell is fabricated. As of this review, no meta-analysis of weighted-ball training with a pooled velocity estimate exists.
CONFIDENCE: high
SEE ALSO: F-025, F-227

### F-223 | UNSOURCED — "a study proved max-distance long toss decreases pitching velocity"
TOPIC: unsourced, misreading, long toss, Fleisig 2011, kinetics, no velocity outcome
CLAIM: This is a blog misreading of a single-session biomechanics comparison that measured no velocity outcome whatsoever.
NUMBERS: n = 17 college pitchers. Max-distance throws produce the greatest shoulder ER (180 +/- 11 deg), shoulder IR torque (101 +/- 17 N-m), elbow varus torque (100 +/- 18 N-m) and elbow extension velocity (2,573 +/- 203 deg/s). NO VELOCITY OUTCOME MEASURED.
POPULATION: NCAA_D1
EVIDENCE: UNSOURCED (the claim) / ESTABLISHED (the actual kinetics)
CAUSALITY: MECHANISM
SOURCE: Fleisig GS, Bolt B, Fortenbaugh D, Wilk KE, Andrews JR (2011), JOSPT 41(5):296-303, PMID 21212502
COACHING: FALSE AS STATED. It is a biomechanics comparison, not a training study. The real long-toss workload finding is F-137.
CONFIDENCE: high
SEE ALSO: F-137, F-038

### F-224 | UNSOURCED — "a 2026 ASMI consensus statement" and the arm-slot SD gate
TOPIC: unsourced, fabrication, ASMI, consensus, content farm, arm slot, threshold
CLAIM: Fabricated. No such document exists.
NUMBERS: the fabricated claim prescribed weighted-ball sequencing gated on "arm slot standard deviation of <+/-2.5 degrees across two consecutive assessment sessions." Other fabrications from the same domains: "New 2026 ASMI data confirms pitchers aged 12-16 maintaining <+/-3 degrees arm slot variation exhibit 68% lower shoulder stress and 41% higher strike-zone efficiency"; "Per USA Baseball's 2026 coach survey, drills prioritizing trunk rotation before arm action reduce late-arm stressors by 19%"; "2026 NCAA injury data shows pitchers chasing velocity without slot consistency faced 37% more shoulder/elbow issues."
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: surfaced from AI content-farm domains; verified absent from ASMI's own publication list
COACHING: THE PRECISION IS THE TELL. Real biomechanics papers do not report clean numbers like "68% lower shoulder stress" for a screening threshold.
CONFIDENCE: high
SEE ALSO: F-216, F-225

### F-225 | HAZARD — the AI content-farm domain blocklist
TOPIC: hazard, content farm, fabrication, blocklist, search, standing rule
CLAIM: Generic web search on pitching topics now surfaces synthetic content with invented citations attributed to real institutions, ABOVE the real literature.
NUMBERS: Sweep 1 blocklist — accio.com, mlbanalytic.com, sportsorca.com, mkdcbaseball.com, seemagnus.com, sportstrace.com, talksox.com, baseballscouter.com. Added Sweep 2 — oreateai.com, afroliterarymagazine.com, baseballmode.com, myzservices.substack.com.
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: idea-scouting.md Sweep 1 #12, Sweep 2 #12
COACHING: STANDING RULE: every institutional claim gets verified at the institution's own publication list or on PubMed before it enters the corpus. THE TELL IS UNEARNED PRECISION.
CONFIDENCE: high
SEE ALSO: F-216, F-224, F-237

### F-226 | CORRECTED — "there is not a single published controlled training study at 85+. Not one."
TOPIC: correction, absolutism, 85 mph floor, controlled trial, negative claim, rhetoric
CLAIM: This absolutism was wrong. Two controlled samples clear the floor.
NUMBERS: Ake 2016 baseline 87.25 / 86.80 mph (the corpus had recorded it as "not reported"); Lee/Choi/Jeon 2026 baseline max 86.2 / 85.9 mph and POSITIVE
POPULATION: NCAA_D1
EVIDENCE: UNSOURCED (the claim as written)
CAUSALITY: CROSS_SECTIONAL
SOURCE: corrected 2026-08-13; see F-023, F-024, F-034
COACHING: The structural argument survives; the absolutism does not. STANDING LESSON: nobody checks a negative claim as hard as a positive one, and "not one" was doing rhetorical work it had not earned.
CONFIDENCE: high
SEE ALSO: F-023, F-024, F-034, F-240

### F-227 | UNSOURCED — three citation errors that circulate about the weighted-ball literature
TOPIC: unsourced, citation error, Caldwell, Driveline, PeerJ, Reinold, title, affiliation
CLAIM: Three specific citation errors recur and should be corrected on sight.
NUMBERS: (1) "Caldwell JME" / Driveline affiliation — the author is Caldwell JE (Jon-Michael E. Caldwell), Columbia/Ahmad group, NOT Driveline-affiliated. (2) "Driveline's 2019 PeerJ weighted-ball paper" — the PeerJ paper is 2018 (e6003); there is no separate 2019 one. Driveline's entire published weighted-ball output is TWO papers, Marsh 2018 and O'Connell 2022, and DRIVELINE HAS PUBLISHED NO RCT. (3) Reinold 2018's title is frequently mis-cited as "...Pitch Velocity, Passive Arm Range of Motion, STRENGTH, and Injury Rates" — the published title says "Pitching Arm Biomechanics."
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 8 #5, #6, #8
COACHING: Correct on sight.
CONFIDENCE: high
SEE ALSO: F-026, F-027, F-222

### F-228 | MISQUOTED — Driveline's "MaxVelo" +7.1 mph in 12 weeks
TOPIC: misquote, MaxVelo, Driveline, baseline mismatch, youth, marketing, +7.1
CLAIM: A widely requoted +7.1 mph figure came from a junior-high/high-school-aged cohort with a 68-72 mph baseline.
NUMBERS: baseline 68-72 mph, +7.1 mph in 12 weeks, non-randomized, acknowledged selection bias; the author himself questioned the analysis
POPULATION: off_population_youth
EVIDENCE: WEAK
CAUSALITY: INTERVENTION
SOURCE: Boddy K (2013), "MaxVelo Velocity Program Study and Results," Driveline
COACHING: SEVERE SAMPLE MISMATCH. It is routinely requoted in industry writing as if it applied to advanced arms. It does not.
CONFIDENCE: high
SEE ALSO: F-025, F-234

### F-229 | UNSOURCED COACHING CLAIMS — the standing list
TOPIC: unsourced, coaching claim, cue, folklore, specificity, hip shoulder separation, downhill
CLAIM: These are coached at a specificity no elite-population evidence supports.
NUMBERS: "You need X degrees of hip-shoulder separation" (F-058 — separation explains 17% of trunk rotation velocity, is two steps removed from ball speed, strongly torso-length dependent, and has no validated target); "get on top of the ball" (F-070 — professionals throw from a LOWER average slot than high schoolers); "throw downhill"; "the block whips the hips" (F-062, r = -0.07); any specific stride-length prescription in inches (F-047); "more layback" (F-102, F-134 — MER is a composite angle); "you lose velo from the stretch" (F-069); "fix your kinematic sequence" (F-105, F-106); "repeat your release point and you'll command the ball" (F-175, BB/9 R2 = 0.011); "take a little off and throw a strike" (F-196); "run to flush the lactic acid" (F-132); "his scap wings, so he's going to get hurt" (F-122); "he's loose, that's a red flag" (F-119); "velocity's still there, so he's not tired" (F-127).
POPULATION: n/a
EVIDENCE: UNSOURCED / FOLKLORE
CAUSALITY: CROSS_SECTIONAL
SOURCE: biomechanics.md 3.5; anatomy-physiology.md 7.3; coaching-translation.md 9
COACHING: None of these have supporting elite-population evidence at the specificity at which they are coached.
CONFIDENCE: high
SEE ALSO: F-213, F-058, F-062, F-105, F-175

### F-230 | UNSOURCED — three commercial and grey-literature claims that surface repeatedly in search
TOPIC: unsourced, marketing, TopVelocity, broad jump, recruiting bands, ResearchGate, conference abstract
CLAIM: Three claims circulate with no published methodology, sample or model.
NUMBERS: (1) "Broad jump is the #1 velocity predictor across a database of 1,500+ professional evaluations" (TopVelocity.org) — commercial marketing, no published methodology, n or model; surfaces repeatedly in search; treat as unreliable. (2) "Correlation of Power to Fastball Velocity of Collegiate Baseball Pitchers" (n = 19 collegiate, med-ball and jump battery), circulating as a ResearchGate PDF attributed to Szymanski and colleagues — no PubMed record, no DOI, no journal of record; likely a conference-supplement abstract; UNVERIFIED. (3) Recruiting-site velocity bands (D1 88-95+, D2 84-88, D3 80-86, etc.) — commercial recruiting sites, no stated methodology; NOT EVIDENCE.
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: velocity-development.md 8 #12, #13, #16
COACHING: Do not cite any of them.
CONFIDENCE: high
SEE ALSO: F-225, F-234

### F-231 | INTERNAL INCONSISTENCIES the corpus has not resolved
TOPIC: internal inconsistency, corpus, conflict, verification, self contradiction, register
CLAIM: A small number of figures appear at different values in different corpus files and should be re-verified before being quoted.
NUMBERS: (1) The interval-throwing dataset is recorded as 238,611 flat-ground throws in one file and 111,196 throws in another, both attributed to Reinold 2026 with n = 34 D1 pitchers (F-137). (2) The OpenBiomechanics dataset is recorded as "81 POI metrics per trial" in one file and "76 measurement points" in another (F-210). (3) The MLB velocity-trend figures differ slightly across files: 2008 league-average four-seam is given as 91.9 in one place and 91.3/91.8 elsewhere, and 2026 as 94.7 and 94.6. (4) The Driveline stride/lead-leg block dataset is described as "800+ force-plate sessions" consistently, but the derived pelvis-rotation correlation is reported with two signs (-0.07 raw, +0.10 bodyweight-controlled) that the corpus itself flags as indistinguishable from zero (F-062). (5) Shoulder IR velocity is given as 5,456-6,149 deg/s from the ASMI table and as "7,000-7,500 deg/s" in the anatomy file, the latter explicitly flagged as widely reproduced but unverified at primary source.
POPULATION: n/a
EVIDENCE: UNSOURCED (pending resolution)
CAUSALITY: CROSS_SECTIONAL
SOURCE: cross-file comparison performed 2026-08-17
COACHING: Do not quote any of these five without re-verifying against the primary source.
CONFIDENCE: high that the inconsistencies exist
SEE ALSO: F-137, F-210, F-076, F-062, F-090

### F-232 | CORRECTED AND REVERSED — "velocity separation doesn't matter on a changeup"
TOPIC: correction, reversal, changeup, velocity separation, absolute velocity, collapse
CLAIM: This statement is a REVERSAL of its source and was briefly carried in this corpus.
NUMBERS: the source's main argued chain is velocity DIFFERENTIAL -> hitters get out in front (attack direction) -> whiffs, characterized as STRONG. What has basically no relationship to changeup whiff rate is the pitch's ABSOLUTE velocity (a 92 mph and a 78 mph changeup both post ~57% whiff).
POPULATION: MLB
EVIDENCE: UNSOURCED (the reversed claim)
CAUSALITY: CROSS_SECTIONAL
SOURCE: corrected 2026-08-13 against Rosen M (17 Jun 2025), FanGraphs
COACHING: ABSOLUTE VELOCITY IS NOT VELOCITY SEPARATION. Collapsing the two INVERTED the coaching conclusion. DO NOT RE-IMPORT. Related downgrade: the article's spin-axis-similarity and arm-angle-change nulls are each a single unquantified sentence with no coefficient, no n and no method — label them EMERGING-unquantified, never "a published null."
CONFIDENCE: high
SEE ALSO: F-159, F-240

### F-233 | MISQUOTED — "stuff models predict ERA at r-squared = .99"
TOPIC: misquote, stuff models, r squared, bucketed means, curve fit, ERA, laundering
CLAIM: The circulating r-squared figures are curve-fits of BUCKETED GROUP MEANS to ERA, not pitcher-level predictive r-squared.
NUMBERS: r2 = .996 (Stuff+) and .992 (PitchingBot) as reported; actual pitcher-level performance for calibration is tjStuff+ v1 vs same-season ERA r = -0.38, prior-season -> ERA r = -0.34
POPULATION: MLB
EVIDENCE: UNSOURCED (as a predictive claim)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Zimmerman J (5 May 2023), RotoGraphs — routinely laundered as pitcher-level prediction
COACHING: If you see r2 > .9 for a stuff model predicting ERA, it is this number being misquoted.
CONFIDENCE: high
SEE ALSO: F-165, F-168

### F-234 | THE MARKETING REGISTER — claims whose packaging outruns their evidence
TOPIC: marketing, register, spin rate, SSW, sweeper, Stuff+, tunneling, case study, transformation
CLAIM: A consolidated list of claims where the underlying finding may be fine but the commercial packaging is a sales instrument.
NUMBERS: (1) "Raise your spin rate" — raw spin explains ~4% of cross-sectional IVB variance (F-146). (2) "Seam-shifted wake lets us add X inches to your sinker" — physics settled, prescriptive pathway unsolved, pitch-to-pitch stability unknown, ~42% of SSW-affected pitches had LOWER Stuff+ (F-148, F-149). (3) "Death ball" branding and the one-session promise (F-149). (4) Building an arsenal around the sweeper in 2026 — the alpha is gone (F-157). (5) "The kick-change is the pitch of 2025" — real mechanism, selection-biased snapshot (F-160). (6) Optimizing Stuff+ as the objective — r ~ .14 for team-switchers, ~9% metric compression, and its rewarded inputs overlap the UCL-surgery gradient (F-166, F-167, F-141). (7) "Tunnel your fastball and slider through a 24-foot window" — the metric suite was published with zero outcome validation and independently tests at r = 0.07 (F-163). (8) Velocity case-study marketing — "84-88 to 92-95," "94 to 100," "gained 30 lb and 5-6 mph," and the specific "89 to 98 in less than a year" (n = 1, no data, no denominator); a facility training hundreds will ALWAYS be able to publish a dozen transformations, and THE DENOMINATOR IS THE 18-21% WHO LOSE VELOCITY (F-074). (9) The "89 to 98" article's featured lateral-tilt rocker cue carries TWO unnamed prices — trunk lateral tilt at BR is a positive contributor to elbow varus torque AND is the exact posture associated with worse command in 338 velocity-matched pros.
POPULATION: n/a
EVIDENCE: UNSOURCED / MARKETING
CAUSALITY: CROSS_SECTIONAL
SOURCE: stuff-and-command.md 12; idea-scouting.md Sweep 2 #11; velocity-development.md 5.1
COACHING: In each case, name the price the article does not.
CONFIDENCE: high
SEE ALSO: F-146, F-149, F-157, F-163, F-166, F-074

---

# 16 — OPEN DISPUTES, CORRECTIONS, AND OUTSTANDING VERIFICATION

### F-235 | OPEN DISPUTE #15 — is spin efficiency trainable, and does the industry price the cost honestly?
TOPIC: dispute, spin efficiency, trainability, grip, mechanics, arm slot, cost, open question
CLAIM: If the third of spin efficiency that moves, moves via arm slot and landing position, then efficiency work is a mechanics project in a grip's costume.
NUMBERS: three-year spin-efficiency r2 = 0.65 across 185 pitchers; the one documented mover changed arm angle 23 deg -> 13 deg and moved his landing crossbody; four-seam efficiency headroom is compressed (p75 ~95%, p90 ~98%) while breaking-ball medians are 31% (slider), 51% (sweeper), 47% (cutter)
POPULATION: MLB
EVIDENCE: EMERGING
CAUSALITY: CROSS_SECTIONAL
SOURCE: open-disputes.md #15; Rosen M (13 Apr 2026), FanGraphs
COACHING: Nobody is quoting the price — a delivery change carries platoon consequences (F-071), a possible command tax (F-176) and a torque change (F-070). WHAT WOULD SETTLE IT: 20-30 elite arms randomized to grip/seam-only intervention or no intervention, 8-12 weeks, spin efficiency on ONE device with a COLD RETEST >= 1 week later, plus arm slot and release height tracked to detect whether the delivery moved without anyone intending it — reporting effect size SEPARATELY for four-seams and breaking balls. The coach predicts the four-seam arm shows almost nothing and the breaking-ball arm shows a real effect. NOTE: there is still NO controlled spin-efficiency intervention trial with a delayed retention test anywhere.
CONFIDENCE: OPEN
SEE ALSO: F-153, F-070, F-162

### F-236 | OPEN DISPUTE #16 — does release-angle precision have any coachable channel?
TOPIC: dispute, release angle, coachable, device, latency, geometry, inert, open question
CLAIM: The 30 cm/degree finding is true, geometric and sample-independent — and inert as a coaching instruction.
NUMBERS: no cue, no drill, no feedback channel and no device in a college program returns a pitcher's release angle in a form he can act on inside the ~150 ms he has
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (the geometry) / UNSOURCED (any coachable channel)
CAUSALITY: MECHANISM
SOURCE: open-disputes.md #16
COACHING: The source's own conclusion is that reducing each release parameter's variability individually is NOT the optimum (F-172), so the coachable implication of 30 cm/deg is NEGATIVE — it tells you what NOT to chase. As written, a coach reads "30 cm per degree," concludes he has found the master variable, and goes and buys something. TWO THINGS BENEATH THE HEADLINE ARE IMMEDIATELY ACTIONABLE AND SHOULD BE PROMOTED ABOVE IT: release-speed variability as a command variable (F-173, free — the data is in every radar log) and horizontal corrective capacity (F-181, also free). WHAT WOULD SETTLE IT: name a device that returns per-pitch release angle at usable latency in a college bullpen. If one exists, this becomes the most important number in the corpus. If not, it is a beautiful fact about geometry and should be labeled as one.
CONFIDENCE: OPEN
SEE ALSO: F-171, F-172, F-173, F-181

### F-237 | HAZARD — search-summary sample conflation, which requires no bad actor
TOPIC: hazard, search summary, sample size, conflation, verification, standing rule
CLAIM: An ordinary search-result summary auto-attributed one preprint's sample size onto a different preprint by the same author on the same platform, manufacturing a phantom n with no fabricated source anywhere in the chain.
NUMBERS: the 43,650-pitch / 2,052-pitcher sample from preprint 1010 was attributed to preprint 871
POPULATION: n/a
EVIDENCE: UNSOURCED
CAUSALITY: CROSS_SECTIONAL
SOURCE: idea-scouting.md Sweep 2 #13
COACHING: This is WORSE than the content-farm hazard because it has NO TELL — the paper is real, the author is real, the number is real, and it belongs to a different paper. NEW STANDING RULE: SAMPLE SIZES ARE VERIFIED ON THE PAPER'S OWN PAGE. Never from a search summary, never from an abstract aggregator, never from another paper's citation of it.
CONFIDENCE: high
SEE ALSO: F-111, F-225, F-240

### F-238 | THE OPEN DISPUTES REGISTER — sixteen arguments the three agents have not resolved
TOPIC: dispute, open questions, register, unresolved, index, honest disagreement
CLAIM: Sixteen disputes are logged with status, the strongest evidence on each side, and what would settle each.
NUMBERS: #1 NARROWED — are the four "free" torque reductions actually modifiable? #2 OPEN — is elbow flexion at FC an independent variable or just arm path? #3 OPEN — can mechanics decouple velocity from varus torque WITHIN an individual (the central question of the program)? #4 NARROWED — force plates vs modeled torque, what to buy and what to believe. #5 OPEN — is there a dugout-measurable posterior-cuff activation marker? #6 OPEN — does "vary your effort" reduce load or mostly reduce velocity? #7 OPEN — is the lead-leg block worth coaching given that it RAISES torque? #8 OPEN — weighted implements in a mature 85+ arm. #9 NARROWED — does "the block whips the hips" deserve FULL retirement? #10 NARROWED — lower arm slot, universal or individual? #11 CONCEDED by the coach 2026-08-12 — the kinematic sequence. #12 OPEN — does the velocity-optimal delivery cost command? #13 OPEN — is stride length a velocity LEVER or only a CORRELATE? #14 LARGELY RESOLVED in the coach's favour 2026-08-13 — "keep lifting = floor protection" was a design artifact. #15 OPEN — is spin efficiency trainable and does the industry price the cost honestly? #16 OPEN — does release-angle precision have any coachable channel?
POPULATION: n/a
EVIDENCE: n/a (register)
CAUSALITY: CROSS_SECTIONAL
SOURCE: open-disputes.md
COACHING: Ground rule from the program README: manufactured consensus is a failure state. An honest open dispute is more useful than a fake answer.
CONFIDENCE: n/a
SEE ALSO: F-239, F-100, F-093, F-176

### F-239 | DISPUTE #12 — the velocity-optimal delivery may cost command, or the whole trade may be a mirage
TOPIC: dispute, velocity, command, trunk tilt, arm slot, trade off, mirage, decision
CLAIM: Every degree of forward and lateral trunk tilt the velocity model rewards is a degree the command data penalizes, in the same population, at the same velocity, at the same landmark — but the velocity side may never have been causal.
NUMBERS: VELOCITY SIDE — trunk flexion at BR beta = 1.829, implying +8.3 mph per 10 deg (n = 337 pro, 3,627 fastballs, adj. R2 = 0.536). COMMAND SIDE — velocity-matched (p = .055) n = 338 professionals: trunk flexion 11.9 vs 15.9 deg (p = .005), trunk lateral flexion -27.1 vs -31.8 deg (p < .001), trunk tilt -33.4 vs -37.2 deg (p = .004), arm slot 59.7 vs 54.7 deg (p = .009). THE ARM-SLOT SQUARE: higher slot -> better command but higher torque; lower slot -> better VAA and lower torque but worse command; AND lower slot is better same-handed, worse opposite-handed — so it is at least a PENTAGON.
POPULATION: professional_mixed
EVIDENCE: EMERGING (as a synthesis; the underlying findings are individually ESTABLISHED)
CAUSALITY: CROSS_SECTIONAL
SOURCE: open-disputes.md #12
COACHING: SAY THE TRADE OUT LOUD BEFORE YOU PUSH: "What I'm about to ask you for buys velocity and it costs command. That might be the right trade for you right now. It is not automatically the right trade, and I'm not making it silently." THE COACH'S ANSWER WHEN FORCED TO PICK: 18-21 needing velocity to be seen at all -> VELOCITY-OPTIMAL (a 21-year-old at 88 with plus command is org-filler; at 94 with 12-inch command he gets drafted and then gets three years of professional instruction — the market prices velocity as an option on future command, and it is right to). 22-25, already 93+, in pro ball, not getting outs -> COMMAND-OPTIMAL (he is past the window, expected year-over-year change is negative above 93, and 1 inch ~ 0.3 FIP ~ a full SD of Stuff+). 88-90 college arm with average command -> NEITHER: buy extension, buy slot, buy the missing pitch — all three are cheaper than either horn and NONE requires resolving the dispute. AND THE CAVEAT IN WRITING: THE DISPUTE MAY BE A MIRAGE. If beta = 1.829 is non-causal — and the stride-length collapse makes that MORE likely, since it is the same error one variable over — then nobody should have been coaching forward tilt in the first place, and the command data is simply a second independent reason not to. WHAT CERTAINLY EXISTS IS A BAD CUE THAT TWO LITERATURES INDEPENDENTLY FLAG.
CONFIDENCE: OPEN, drifting toward the mirage reading
SEE ALSO: F-053, F-070, F-071, F-176, F-043

### F-240 | THE ERROR PATTERN — six corrections in one day, none a fabrication, all in the same direction
TOPIC: correction, error pattern, verification, epistemics, operating rule, confidence, compression
CLAIM: Six library corrections landed on 2026-08-13 and not one was a fabrication. Every one was a real source, correctly cited, read slightly wrong — and all six erred toward MORE confidence than the source supported.
NUMBERS: THE SIX — (1) a CROSS-SECTIONAL FINDING READ AS A CAUSAL LEVER (stride length; the number is right, the inference is wrong). (2) TWO ADJACENT QUANTITIES COLLAPSED (absolute changeup velocity vs velocity separation — which INVERTED the conclusion). (3) A SUMMARY FIGURE TAKEN OVER THE UNDERLYING TABLE (+1.35 vs the article's own 89.6 -> 90.3 = +0.65 mph). (4) A SAMPLING UNIT MISREAD ("1,163 pitcher-seasons" vs pitcher x pitch-type x season pairs). (5) AN ABSOLUTISM DOING RHETORICAL WORK IT HAD NOT EARNED ("not one study at 85+"; the baseline was IN the paper, listed as "not reported"). (6) A STUDY DESIGN INFERRED FROM A RESULT (Gdovin's p < .001 read as a "removal experiment"; the paper is an uncontrolled pre-post with no control group). PLUS TWO LABEL FIXES — first authorship on PMID 34240663 is Manzi, not Dowling; and both Kusafuka 2025 coefficients were described as an autocorrelation and a state probability when both are correlations BETWEEN a correction statistic and azimuth variability. EVERY ONE OF THE SIX WOULD HAVE SURVIVED A PUBMED CHECK — in every case the citation, the n and the p-value were correct.
POPULATION: n/a
EVIDENCE: n/a (process finding)
CAUSALITY: MECHANISM
SOURCE: daily/2026-08-13-coach.md 9, 11; open-disputes.md standing methodological disputes
COACHING: OPERATING RULES ADOPTED. (A) VERIFYING A CITATION IS NOT VERIFYING A CLAIM. The verification pass asks two further questions after "does this source exist": does the source support THIS SENTENCE, or a weaker one? and WHAT WAS THE ACTUAL DESIGN, AND IS THERE A CONTROL GROUP? Never infer a design from a p-value. (B) SECONDARY SOURCES ARE NOT THE HAZARD — OUR OWN PROSE IS. Every number came from a legitimate primary source; the corruption happened in the RESTATEMENT, in the compression from a paper into a table row into a recommendation. Each compression step is a chance to lose a qualifier, and qualifiers are exactly what distinguishes "correlate" from "lever." Therefore: any claim promoted to a NUMBERED RECOMMENDATION gets re-read against the primary source before it ships. (C) THE SAME SCRUTINY APPLIES TO DISCONFIRMING EVIDENCE — the coach presented one 19-athlete cohort as multiple independent studies, in the direction he was already arguing, on the same day he accused colleagues of the same error. (D) THE ERRORS WERE NOT RANDOMLY DISTRIBUTED, AND THAT IS THE FINDING. Random transcription error would have moved some of them toward UNDER-claiming. A one-directional error pattern is a SYSTEMATIC BIAS, and the most likely mechanism is that COMPRESSION TOWARD A USABLE RECOMMENDATION IS INHERENTLY A CONFIDENCE-INCREASING OPERATION. (E) Sample sizes are verified on the paper's own page, never from a search summary (F-237).
CONFIDENCE: high — this is the most important epistemic finding in the corpus
SEE ALSO: F-039, F-043, F-072, F-073, F-226, F-232, F-237

### F-241 | RESOLVED 2026-08-17 — the daily briefs contained the PRE-CORRECTION text; they are now annotated in place
TOPIC: warning, daily briefs, uncorrected, snapshot, propagation, corpus hygiene, back-correction, resolved
STATUS: **BACK-CORRECTION COMPLETED 2026-08-17.** All five affected daily briefs now carry (a) a "⚠ This brief contains claims later corrected" banner at the top listing which claims, and (b) an inline `⚠ CORRECTED 2026-08-17` notice immediately after each superseded assertion, citing the current number and the library file and F-ID. **No original text was deleted or rewritten** — the briefs remain dated historical records of what the program believed and when, and the corrections sit alongside them. FILES ANNOTATED (16 inline notices in total, across 5 files): `daily/2026-08-13-velocity.md` (10 notices: the "not one study at 85+" absolutism and the Ake "NR" baseline; the refuted underload 11-12%/2-3% novice-vs-experienced split; the Gdovin removal framing and the floor-protection pitch resting on it; stride length as one of "the two free mechanical levers"; the 1,163 sampling unit and the -1.15 mean; the Driveline +1.35; the realistic-annual-gain table rows; the tomorrow's-hooks premises). `daily/2026-08-13-stuff-command.md` (1 notice: the inverted changeup framing). `daily/2026-08-13-coach.md` (3 notices: the §2.2 athlete script's "not one" absolutism; the Kusafuka r = 0.73 "staying-in-state" mislabel in the §5 table; the §5 changeup row, which contradicts that same file's own §9). `daily/2026-08-12-biomechanics.md` (1 notice: stride length as the "clean win"). `daily/2026-08-12-coach.md` (1 notice: Bloebaum rho = 0.22 presented in a command context; it is a VELOCITY association, F-109). `daily/2026-08-12-anatomy.md` — CHECKED, NOTHING WRONG, deliberately left untouched.
CLAIM: The corrections applied on 2026-08-13 were written into the library files but NOT back into the dated daily briefs, which still asserted the superseded claims. **Closed 2026-08-17 by inline annotation rather than by editing the originals.**
NUMBERS: daily/2026-08-13-velocity.md still states "There is not a single published, controlled training study whose sample mean baseline velocity is at or above 85 mph. Not one" (superseded, F-226); "+1.35 mph mean" for the Driveline >= 88 cohort (superseded, F-072); "n = 1,163 pitcher-season pairs ... mean -1.15 mph" (superseded, F-073); "Adding strength training ... Removing it demonstrably costs velocity" and the Gdovin framing (superseded, F-039); and lists stride length as one of "the two free mechanical levers" (superseded, F-043). daily/2026-08-13-stuff-command.md states "spin-axis similarity showed no predictive value ... Neither did velocity" (the reversed changeup framing, superseded, F-232).
POPULATION: n/a
EVIDENCE: n/a (corpus hygiene)
CAUSALITY: MECHANISM
SOURCE: cross-file comparison performed 2026-08-17
COACHING: THE DAILY BRIEFS ARE STILL DATED SNAPSHOTS, NOT CURRENT REFERENCE — read the library files (or this registry) for current state. **But as of 2026-08-17 the re-import vector is closed at the point of contact:** a grep that lands on a superseded number in a daily brief now lands within a few lines of a dated correction notice carrying the right number, the right design, and a pointer to the library and the F-ID. This was the failure mode described in F-240, and the fix is deliberately ADDITIVE — annotate, never overwrite — because silently editing a dated record destroys the trail of what the program believed and when, which is itself the evidence base for F-240. STANDING RULE ADOPTED: when a library correction lands, the same-cycle back-annotation of every daily brief asserting the old claim is part of shipping the correction, not a later cleanup task.
CONFIDENCE: high — verified by direct comparison; back-correction verified by re-grep of daily/ on 2026-08-17
SEE ALSO: F-240, F-039, F-043, F-072, F-073, F-109, F-232, F-242

### F-242 | OUTSTANDING — items flagged for verification that were never checked
TOPIC: unverified, outstanding, verification, backlog, fabrication risk, priority
CLAIM: The corpus is NOT fully vetted; a named set of items was flagged and never reached a verifier.
NUMBERS: (1) TWO ITEMS PRE-FLAGGED AS HIGH FABRICATION RISK were flagged at the outset of the 2026-08-13 cycle and NEVER REACHED A VERIFIER — they are the only items still carrying an active fabrication flag, and they are not individually named in the corpus. HIGH priority. (2) Bloebaum SportRxiv 871 SAMPLE SIZE — a search summary was observed attributing another preprint's n to it; do not cite any n without opening the PDF. HIGH. (3) Bloebaum SportRxiv 919 EFFECT SIZES — claim recorded, magnitudes never opened. MEDIUM. (4) Smith, Smith & Bowman (2017), SABR Baseball Research Journal — a third stride manipulation (30 college pitchers, +/-10%, repeated-measures ANOVA, 30 randomized pitches, radar: 10% SHORTER was 0.8 mph FASTER, F(2,522) = 14.01, p < .001). GREY LITERATURE, never independently verified, directionally consistent with F-045 — DO NOT LEAN ON IT. MEDIUM. (5) Gdovin 2025 MPH MAGNITUDE — paywalled; the corpus quotes a p-value with no effect size under what was its own #1 recommendation. MEDIUM. (6) Nevada/Reno (Buck) THESIS OUTCOMES — unpublished; request the thesis. LOW. (7) Baseball America college-to-pro cohort — paywalled, figures from a search abstract only. MEDIUM.
POPULATION: n/a
EVIDENCE: UNSOURCED (pending)
CAUSALITY: CROSS_SECTIONAL
SOURCE: daily/2026-08-13-coach.md 9b
COACHING: STANDING INSTRUCTION: do not treat any claim in this corpus as vetted merely because it survived 2026-08-13. Absence of a correction is not evidence of accuracy; it is partly evidence of where the verifier got to before it stopped.
CONFIDENCE: high that these remain outstanding
SEE ALSO: F-081, F-110, F-111, F-240

### F-243 | POWER ANALYSIS — you need ~8 dated sessions before you can believe a 1 mph velocity change
TOPIC: velocity, power analysis, sample size, sessions, radar, evaluation, noise, detection
CLAIM: Detecting a realistic velocity change requires a session count most programs never run.
NUMBERS: assume a BETWEEN-SESSION mean-fastball-velocity SD of ~1.0 mph (an ASSUMPTION — measure the athlete's own SESSION-TO-SESSION variation, not his within-outing SD). Paired, alpha = .05, 80% power: 0.5 mph -> d = 0.5 -> ~31 sessions (you cannot detect this in a season; stop trying). 1.0 mph -> d = 1.0 -> ~8 separately-dated sessions per condition, >= 25 fastballs each. 2.0 mph -> d = 2.0 -> ~2-3 sessions.
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED (standard power analysis)
CAUSALITY: MECHANISM
SOURCE: coaching-translation.md 11.13; daily/2026-08-13-coach.md 2.5
COACHING: A velocity intervention needs roughly EIGHT DATED SESSIONS ON ONE GUN before a 1 mph claim is anything but noise. That is a whole fall. It is still an order of magnitude cheaper than the command equivalent (~200 tracked pitches for 2 inches, F-186) — WHICH IS EXACTLY THE MEASUREMENT-CONVENIENCE ASYMMETRY THAT MADE VELOCITY DEVELOPMENT A COMMERCIAL INDUSTRY AND COMMAND DEVELOPMENT A HOBBY. Never validate against a PREDICTED velocity (capacity models carry +/-2.7 mph error). One gun, one position, one operator — a radar change mid-project ends the project.
CONFIDENCE: high
SEE ALSO: F-186, F-018, F-206, F-169

### F-244 | SURVIVORSHIP — every "professional norms" table is drawn from arms that survived to be tested
TOPIC: survivorship, selection, norms, bias, methodology, standing caveat
CLAIM: Professional biomechanics norms are drawn exclusively from pitchers whose mechanics did not end their careers before testing.
NUMBERS: —
POPULATION: professional_mixed
EVIDENCE: ESTABLISHED
CAUSALITY: MECHANISM
SOURCE: biomechanics.md 1.1; open-disputes.md standing methodological disputes
COACHING: The mechanics that broke are underrepresented in every norms table in this corpus. Combine with the aging-curve survivorship attenuation (F-075) and the restriction-of-range warning (F-056): elite norms describe the survivors of a filter, not the population of throwers.
CONFIDENCE: high
SEE ALSO: F-056, F-075, F-089

### F-245 | Sherwood, Hinrichs & Yamaguchi (1997) is REAL — and is a conference abstract with no retrievable data
TOPIC: extension, shoulder horizontal abduction, adduction, Driveline, citation hygiene, mechanism, conference abstract, verification
CLAIM: The paper Driveline cites for "shoulder horizontal abduction is negatively correlated with fastball velocity" exists, but is an unretrievable 1997 ASB conference abstract, is anatomically mislabelled by Driveline, and does not measure release extension at all.
NUMBERS: NO sample size, NO competition level, NO mean fastball velocity, NO correlation coefficient, NO p-value is publicly retrievable — none is reported by Driveline or by any downstream citation. Citation verified against Richard N. Hinrichs's curriculum vitae (Arizona State University, July 2017 edition), where it appears as a conference presentation, not a journal article.
POPULATION: UNKNOWN — not reported at any retrievable level
EVIDENCE: UNVERIFIED (citation confirmed to exist; abstract content unverified — full ASB 1997 proceedings not online)
CAUSALITY: MECHANISM (as used); underlying design not retrievable
SOURCE: Sherwood CP, Hinrichs RN, Yamaguchi GT (1997), "Relationships between ball release velocity and 3D joint kinematics in baseball throwing," 21st Annual Meeting of the American Society of Biomechanics, Clemson SC, September 1997. Cited in: Driveline Baseball, "Pitching Mechanics Myths: Chin to Target, Extend to Release" (Jan 2012).
COACHING: THREE THINGS TO SAY AND ONE NEVER TO SAY. (1) It is NOT a fabrication — this one is real, which matters given 16 caught fabrications. (2) Driveline's anatomical label is INVERTED: an arm "translated closer to home plate with respect to the trunk" is horizontal ADDUCTION under standard convention, not abduction. Anyone reading the term rather than the description gets the sign backwards. (3) The substantive DIRECTION is independently corroborated by Stodden 2005 within-pitcher (F-246), so the claim is probably true — it just does not need Sherwood, and Sherwood cannot supply a magnitude. NEVER SAY: that this makes release EXTENSION costly. Sherwood and Stodden both measure SHOULDER HORIZONTAL POSITION RELATIVE TO THE TRUNK AT FOOT CONTACT AND DURING ACCELERATION. Release extension is how far in front of the rubber the ball leaves the hand — stride length, height, forward trunk tilt, arm length. DIFFERENT CONSTRUCTS AT DIFFERENT INSTANTS. A pitcher can gain half a foot of extension through stride and trunk tilt without changing shoulder horizontal position at foot contact by one degree. THE "EXTENSION IS BIOMECHANICALLY COSTLY" INFERENCE IS A NON-SEQUITUR AND MUST NOT BE RE-IMPORTED.
CONFIDENCE: high that the citation is real and that the inference drawn from it is invalid; zero confidence in any magnitude
SEE ALSO: F-246, F-150, F-247, F-043

### F-246 | Stodden 2005 — the only WITHIN-ATHLETE support for a near-release kinematic variable, and it carries no effect size
TOPIC: velocity, trunk tilt, forward trunk flexion, release, within-pitcher, mixed model, Stodden, ASMI, shoulder horizontal adduction
CLAIM: Within a pitcher's own trial-to-trial velocity variation, increased forward trunk tilt at release is the only release-instant kinematic variable significantly related to higher ball velocity — but no magnitude is retrievable and the sample's velocity is unknown.
NUMBERS: n = 19 pitchers, 3-D high-speed motion analysis, 6 to 10 fastball trials each. Inclusion required >= 1.8 m/s within-subject velocity variation (observed range 1.8-3.5 m/s = 4.0-7.8 mph). Three mixed-model analyses over 7 kinetic, 11 temporal and 12 kinematic parameters (30 tests). EIGHT SIGNIFICANT: kinetic (3) — elbow flexion torque, shoulder proximal force, elbow proximal force; temporal (2) — increased time to max shoulder horizontal adduction, decreased time to max shoulder internal rotation; kinematic (3) — decreased shoulder horizontal adduction at foot contact, decreased shoulder abduction during acceleration, INCREASED TRUNK TILT FORWARD AT RELEASE. NO beta, r or p is retrievable (paywalled). MEAN FASTBALL VELOCITY NOT REPORTED AND NOT RETRIEVABLE. Companion paper on the identical cohort and identical inclusion criterion — Stodden, Fleisig, McLean, Lyman & Andrews (2001), J Appl Biomech 17(2):164-172 — describes them only as "nineteen elite baseball pitchers."
POPULATION: "elite" per authors — LEVEL AND MEAN VELOCITY UNVERIFIED. Do NOT record as an 85+ sample without the full text.
EVIDENCE: EMERGING (genuine within-subject design; n = 19; no retrievable effect size; 8 hits across 30 tests with no stated multiplicity correction)
CAUSALITY: CROSS_SECTIONAL (within-subject observational — NOT an intervention, NOT a manipulated null; nothing was trained or manipulated, naturally occurring trial-to-trial variance was exploited. NO CONTROL GROUP, and none is called for.)
SOURCE: Stodden DF, Fleisig GS, McLean SP, Andrews JR (2005), J Appl Biomech 21(1):44-56, DOI 10.1123/jab.21.1.44, PMID 16131704. Bowling Green State University / American Sports Medicine Institute. Verified against the journal.
COACHING: THE DESIGN IS THE VALUE — each pitcher is his own control, so height, mass, arm length and training age are differenced out. That is structurally better than the cross-sectional correlations that dominate this literature. BUT: attach NO magnitude to it. DO NOT FUSE IT WITH F-236's beta = 1.829 (~ +8.3 mph per 10 deg) — that is a DIFFERENT, BETWEEN-SUBJECTS dataset (n = 337 pro), and it is exactly the kind of number the stride-length collapse (F-043) teaches us to distrust. Note also that all three significant KINETIC variables are load readouts that rise with velocity — consequences, not levers. Treat the eight-variable list as hypothesis-generating.
CONFIDENCE: high on design and on the variable list; none on magnitude; none on sample velocity
SEE ALSO: F-236, F-245, F-043, F-056

### F-247 | The "extension is costly" mechanism has never been established — it was imported from a different instant of the delivery
TOPIC: extension, mechanism, non-sequitur, foot contact, release, shoulder horizontal adduction, citation hygiene, standing caveat
CLAIM: Every published finding used to argue that gaining release extension costs velocity actually measures shoulder horizontal position relative to the trunk at foot contact or during acceleration, not release extension.
NUMBERS: —
POPULATION: mixed / not applicable
EVIDENCE: ESTABLISHED (as a statement about what the cited literature measures)
CAUSALITY: MECHANISM
SOURCE: daily/2026-08-20-verification-extension.md 1; Sherwood/Hinrichs/Yamaguchi 1997 (F-245); Stodden et al. 2005 (F-246)
COACHING: WHEN SOMEONE SAYS "REACHING FOR EXTENSION COSTS YOU VELOCITY," ASK WHICH INSTANT THEY MEAN. Arm carried across the front of the trunk AT FOOT CONTACT is associated with less velocity — that is real, and it is corroborated within-athlete. How far in front of the rubber the ball leaves the hand is a different variable, produced by stride length, standing height, forward trunk tilt and arm length. The two are not the same thing and the literature has never linked them. THE COST IS UNMEASURED, NOT PROVEN AND NOT DISPROVEN. What IS true and separately documented: extension lowers release height, which flattens VAA (F-150, F-151) — good for a four-seam at the top, bad for a curveball. That is the real trade, and it is geometric, not biomechanical.
CONFIDENCE: high
SEE ALSO: F-245, F-246, F-150, F-151, F-250

### F-248 | The VAA R2 = .945 figure is a geometric identity reported as a statistical finding
TOPIC: VAA, vertical approach angle, extension, release height, R2, Zahradnik, geometry, identity, grey literature
CLAIM: The widely quoted "extension and release height predict VAA at R2 = .945" is a real number from a blog post, and it demonstrates geometry rather than any independent leverage of extension on VAA.
NUMBERS: Zahradnik, Medium / Iowa Baseball Managers, 26 October 2020. Verbatim: "A simple regression equation with those variables as inputs returns an R-Squared value of .945, a great predictor of VAA." Sample stated as "2,350 pitchers." NO season, NO league level, NO pitch count, NO coefficients published. Direction only. PLATE HEIGHT WAS NOT A PREDICTOR — the author stratified into top-of-zone (3-4 ft) and bottom-of-zone (1-2 ft) bands instead. Compare F-151: four inputs including plate height, n = 6,110, R2 = 0.999, and EXTENSION DROPS OUT ENTIRELY once release height is included.
POPULATION: unstated — presumed MLB, UNVERIFIED
EVIDENCE: WEAK (blog, no coefficients, no level, no season, location not modelled)
CAUSALITY: MECHANISM (geometric identity)
SOURCE: Zahradnik R (26 Oct 2020), "Fastball Vertical Approach Angle," Medium/Iowa Baseball Managers. Read at source 2026-08-20.
COACHING: R2 = .945 IS NOT IMPRESSIVE, IT IS EXPECTED. VAA is fully determined by geometry — F-151 recovers it at R2 = 0.999 and there is essentially no residual. Anything predicting VAA from release-point variables is fitting an equation, not discovering a relationship. Extension looks predictive in a two-variable model ONLY because extension and release height are strongly negatively correlated: you get more extension largely by getting lower. EXTENSION IS A PROXY FOR RELEASE HEIGHT, NOT A SECOND LEVER. And omitting plate height — which has leverage nearly equal and opposite to release height, -1.08 vs +1.06 deg/ft — inflates what remains. THE DEFENSIBLE SENTENCE: release height sets VAA; extension tracks VAA because extension lowers release height.
CONFIDENCE: high
SEE ALSO: F-151, F-150, F-152, F-247

### F-249 | Extension and hitter outcomes — the perceived-minus-actual GAP is a clean public extension variable, and it is worth under 5% of variance
TOPIC: extension, perceived velocity, gap, whiff, swinging strike, K rate, xwOBACON, hitter outcomes, Statcast, instrument
CLAIM: The perceived-velocity-minus-actual-velocity gap is a pure extension variable available on Savant, and across MLB it correlates weakly but consistently with whiff and strikeout rate — while Driveline found perceived velocity adds nothing over release speed on contact quality.
NUMBERS: PODHORZER (RotoGraphs/FanGraphs, 8 Jul 2025), MLB pitcher-seasons since 2021, min 300 pitches. Correlation of (perceived velo - actual velo) with Whiff/Swing% and K%: ALL n = 1,753, r = 0.11 / 0.14; four-seam n = 1,216, r = 0.07 / 0.12; sinker n = 438, r = 0.07 / 0.12; cutter n = 99, r = 0.17 / 0.21. R2 range approximately 0.5% to 4.4%. Gap tracks K% more than Whiff/Swing%. NO control for velocity, VAA, movement, release height or command. — WILKES (Redleg Nation, 5 Jun 2019), 174 MLB pitchers with 500+ fastballs: SwStr% 10.6% at or above 6.1 ft extension vs 9.4% below (1.2-point gap), univariate split, NO velocity control. Glasnow 2019: 96.6 actual -> 99.4 perceived, +2.77 mph, 7.61 ft extension, releasing 52.89 ft from the plate. — AUCOIN (Driveline, 23 May 2019), 2018 Savant player PV estimates raced against Release Speed: "Perceived Velocity was found to have a slight edge over Release Speed in swinging strike percentage, but once xwOBACON and Projected RA9 were considered, Release Speed once again remained king." NO sample size, NO coefficients published for that comparison.
POPULATION: MLB
EVIDENCE: EMERGING (three independent cross-sectional analyses, consistent sign, tiny effect, no controls; the Driveline leg is UNQUANTIFIED grey literature)
CAUSALITY: CROSS_SECTIONAL
SOURCE: Podhorzer M (8 Jul 2025), "All About Pitcher Perceived Velocity," RotoGraphs/FanGraphs; Wilkes M (5 Jun 2019), "The Art of Deception: A Primer on Perceived Pitch Velocity," Redleg Nation; Aucoin D (23 May 2019), "Calling the Right Pitch: Investigating Effective Velocity at the MLB Level," Driveline Baseball. All three read at source 2026-08-20.
COACHING: THE INSTRUMENT IS THE FINDING. At fixed velocity, effective_speed minus release_speed is a monotone function of extension AND NOTHING ELSE — so any future extension question can be asked directly against Savant without new data collection. THE ANSWER IT GIVES: extension's standalone value at MLB level is real, consistent in sign across every pitch type, and worth UNDER 5% OF VARIANCE in whiff and K rate. TWO RESULTS THAT LOOK CONTRADICTORY AND ARE NOT: extension may buy a small WHIFF edge and NO CONTACT-QUALITY edge. Driveline's null is on xwOBACON and projected RA9, NOT on swinging strikes — where PV actually beat release speed. Do not quote the Driveline result as a blanket null; it is narrower than that, and it carries no numbers at all. NOBODY HAS ISOLATED EXTENSION FROM VELOCITY AND VAA — no controlled regression, no occlusion or VR study manipulating release distance at fixed velocity. THE QUESTION IS OPEN. ALWAYS report release velocity separately from perceived velocity (F-150).
CONFIDENCE: medium — the sign is probably real, the magnitude is a ceiling not an estimate, and confounding with velocity is uncontrolled in all three
SEE ALSO: F-150, F-153, F-247, F-250, F-232

### F-250 | +1 FOOT OF EXTENSION IS A SCALE BAR, NOT A TRAINING TARGET — and no intervention has ever trained extension
TOPIC: extension, perceived velocity, per-inch, arithmetic, realistic range, intervention, absence, trainability
CLAIM: The perceived-velocity geometry is exact and reproduces independently, but the "+1 foot = +1.8 mph" framing describes a move spanning nearly the entire major-league range, and nothing has ever been published on whether extension can be trained at all.
NUMBERS: Recomputed 2026-08-20 from PV = velo x 54.17 / (60.5 - extension). At 95 mph, 6.5 -> 7.5 ft: 95.30 -> 97.10 mph, delta = +1.80 mph/ft (CONFIRMED). Timing 54.0 -> 53.0 ft at 139.33 ft/s: 387.6 -> 380.4 ms, delta = 7.18 ms (CONFIRMED; with in-flight drag at a ~91 mph flight average the true figure is ~7.5 ms, so 7.2 is the conservative one). PER-INCH IS EXTENSION-DEPENDENT, d(PV)/d(ext) = v x 54.17 / (60.5 - ext)^2: at 6.00 ft = 0.1444; 6.33 ft = 0.1461; 6.51 ft (MLB 2024 four-seam mean) = 0.1471; 7.00 ft = 0.1511; 7.50 ft = 0.1554 mph per inch. USE 0.15 mph/inch at 95 mph. SCALE: MLB 2024 four-seam extension mean 6.51 ft, SD 0.45 (F-153) — so +1 ft = +2.2 SD, moving a median pitcher past the 99th percentile (p99 = 7.60). Extension is ~1.04x pitcher height (F-150). Scaling to a plausible individual change of 0.1-0.3 ft gives +0.18 to +0.54 mph perceived and 0.7-2.2 ms.
POPULATION: MLB (distribution); geometry is population-independent
EVIDENCE: ESTABLISHED (geometry, reproduced independently this cycle) / NONE WHATSOEVER (trainability)
CAUSALITY: MECHANISM
SOURCE: daily/2026-08-20-verification-extension.md 3 and 7; F-150; F-153. Absence search 2026-08-20 covering intervention/pre-post/randomised designs on extension, release extension, release point and release distance; stride-length training transfer; Statcast year-over-year extension analyses; drill protocols.
COACHING: QUOTING "+1.8 mph PER FOOT" WITHOUT THE SCALE BAR IS THE SINGLE MOST MISLEADING WAY TO PRESENT THIS GEOMETRY, and it is how it is nearly always presented. One foot is roughly the full observed range of the major leagues. STATE THE BASELINE EXTENSION WHENEVER A PER-INCH FIGURE IS QUOTED — the rate is not constant. NO INTERVENTION EXISTS AT ANY LEVEL, not merely none at 85+. The three nearest misses and why each fails: (1) Ramsey & Crotin stride-length CROSSOVER — blinded randomised, +25%/-25% of desired stride, >=72 h washout, 8-camera VICON 240 Hz + 2 Kistler plates 960 Hz — the strongest design in the neighbourhood, but it manipulates STRIDE LENGTH acutely and RELEASE EXTENSION WAS NOT AN OUTCOME. (2) Diffendaffer/Fleisig six-week weighted-implement program, n = 17 (9 collegiate, 8 professional), age 19.9 +/- 1.3, PRE-POST WITH NO CONTROL GROUP, pre-training velocity 35.1 +/- 1.8 m/s = 78.5 mph — SAMPLE MISMATCH, DIRECTIONAL ONLY, below the 85 floor — no velocity change, and stride length, release point and release extension WERE NOT MEASURED. (3) University of Nevada Reno 4-week ankle-mobility intervention measuring stride length — announced 2026, NO PUBLISHED RESULTS, outcome is stride not extension. WATCH ITEM ONLY. Everything this corpus says about extension is either geometry or between-pitcher cross-section; NOT ONE LINE establishes that extension can be trained, by how much, or at what cost. Given extension ~ 1.04x height and stride length already demoted from lever to marker (F-043), the prior should be that the trainable share is SMALL.
CONFIDENCE: high on the geometry and on the absence; the absence was searched for deliberately, not assumed
SEE ALSO: F-150, F-153, F-043, F-247, F-249, F-226


---

*End of registry. 250 entries. Numbering is stable — never reuse or renumber an F-ID. New findings append from F-251.*
