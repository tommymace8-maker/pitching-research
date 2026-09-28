# Nutrition, Body Mass and Energy Availability — reference file

**Opened 2026-09-28.** Covers: in-season and off-season body-mass and body-composition change in college baseball; the energy-availability / RED-S construct as it applies (and does not apply) to a pitcher; the detection arithmetic for mass management; and the marker-vs-lever status of the corpus's single strongest velocity correlate.

**Findings:** F-494 → F-507. **Companion entries:** F-001, F-002, F-003, F-005, F-140, F-442.
**Primary texts read in full:** PMC4595292, PMC11205132, PMC11792141, PMC12899827, PMC9101736. **Blocked and unread:** PMC5358033 (Rossi 2017 full text), the NCAA D1 seasonal body-composition papers.

---

## 1. THE HEADLINE, AND IT IS A REFUSAL

**Body mass is the strongest single physical correlate of fastball velocity in this corpus (F-001, r = 0.58, n = 33 NCAA D1). Nobody has ever measured a within-athlete mass-change → velocity-change slope, in any population, at any level.**

There is no mph per pound. One cannot be quoted, estimated, or bracketed. This is the same failure that took down stride length (F-013, F-046) and extension, and that forced the jump-height regrade on 2026-09-22 (F-004 → F-442). Body mass is the largest of the family and the most commercially loaded.

**The asymmetry that IS defensible:** protecting a correlate is a much weaker claim than moving one, and it is the only claim this literature supports. Defend against unintentional in-season mass loss on mechanism grounds (momentum, F-003/F-005). Do not sell mass gain as mph.

---

## 2. WHAT THE EVIDENCE ACTUALLY IS

### 2.1 Interventions (there is one, and it is a null)

**Cholewa/Rossi et al. 2015, ISSN Conf P44, PMC4595292 — read in full.** n = 30 D1 baseball, 82.4 ± 8.2 kg, 13.7 ± 5% BF, 12 weeks off-season, 15 education / 15 position-matched control, identical training (4 h strength + 3 h conditioning + 20 h skills per week).

| Outcome | Change (pooled) | Between groups |
|---|---|---|
| Fat-free mass | +3.7 ± 3.6 kg | **none** |
| Body mass | +3.3 ± 4.8 kg | **none** |
| Back squat 1RM | +25.5 ± 15.9 kg | **none** |
| Vertical jump | +0.144 ± 0.09 m | **none** |
| Broad jump | +0.135 ± 0.1 m | **none** |
| Body fat % | −1.2 ± 2.3 vs +0.3 ± 1.7 | intervention only |
| Sport-nutrition knowledge | 56 ± 11 → 70 ± 9 % | intervention arm measured |
| Energy intake | 35.5 → 41.2 kcal/kg (target 45) | intervention arm measured |
| Protein | 1.7 → 2.2 g/kg (target 2) | intervention arm measured |
| **Carbohydrate** | **3.6 → 3.8 g/kg (target 6)** | **never approached target** |

**Read it honestly:** everything that moved, moved in both arms. The mass and strength gains belong to the training program. **No velocity outcome.** ⚠️ Conference abstract; the 2017 peer-reviewed version is unread and is F-494's stated withdrawal condition.

### 2.2 Observational, across a season

- **Merfeld 2024 (PMC11205132, read in full), n = 12 summer league (6 pitchers):** FFM −0.05 kg, **95% CI [−4.40, +4.33] kg**. Body fat −0.32 pp, CI [−4.05, +3.42]. **Uninformative. Do not cite as stability.** Throwing-arm shoulder strength −9.03% vs −2.03% non-throwing (arm×time p = 0.08).
- **NCAA D1 seasonal work (F-503, SNIPPET-ONLY, hosts blocked):** team-wide body weight and lean mass fall; the decline reportedly sits with **position players**, with pitchers showing no significant change. **No n, no kg, no CIs.** And "no significant change in pitchers" at roster size is itself an underpowered null.

### 2.3 Intake

- **Iio 2025 (PMC11792141, read in full), n = 92 Japanese collegiate, median 75 kg:** FFQ median intake **2,077 kcal/day** vs a stated **3,555 kcal/day** requirement; only 4 of 92 ate ≥3,000 kcal; protein 79 g/day. **The implied deficit predicts ~27 kg of loss per season in a sample where 42% have BMI ≥ 25. It is an under-reporting artifact of roughly 40%.** ⚠️ SAMPLE MISMATCH: Japanese collegiate, no velocity, includes third/fourth teams. Directional only.
- **Rossi's D1 sample sat at 1.7 g/kg protein BEFORE any education** — i.e. already inside F-140's 1.6–2.2 g/kg band. **The gap in actual D1 baseball was carbohydrate, not protein**, and twelve weeks of education did not close it.

---

## 3. THE ENERGY-AVAILABILITY CONSTRUCT — do not use it on a pitcher

`EA = (EI − EEE) / FFM`, kcal·kg⁻¹ FFM·day⁻¹.

**Three independent reasons it does not transfer (F-500, F-501, F-502):**

1. **The threshold is borrowed from the wrong people.** The <30 kcal/kg FFM/day cutoff comes from short-term laboratory studies in regularly menstruating women (Loucks & Thuma 2003; Loucks & Heath 1994). The 2026 review surveying the field says in its own summary table: *"Derived from laboratory-controlled studies and sedentary women; not validated in free-living athletic settings... **Use as a conceptual tool, not a diagnostic cut-off value.**"* Male induction studies have used 15 kcal/kg FFM for 4–6 days. **No validated male threshold exists; none exists for a 95 kg power athlete.**
2. **It falls on hard days by construction.** `∂EA/∂EEE = −1/FFM` identically, so at constant intake the highest-expenditure day is the lowest-EA day. Empirically: *"The number of LEA days were associated with higher EEE"* (Vardardottir 2024, n = 19, read in full). **A starter's bullpen day and his start day are LEA days by arithmetic.** Cousin of the geometric-identity hazard this corpus caught in the R² = .945 claim.
3. **The screening tool failed its own validation.** LEAM-Q, n = 310: *"Sub section and total LEAM-Q scores were not different between LEA cases and control cohorts, with the exception of the sex drive score."* Best item runs **87% sensitivity / 26% specificity**. Validation sample **VO2max 68.1 ± 7.2** — distance runners and cyclists. **SAMPLE MISMATCH, severe.**

**What the review does say about performance, and it runs opposite to the industry story:** LEA *"does not consistently impair maximal aerobic capacity (VO2max), peak power output, or anaerobic threshold, particularly during short-term or moderate energy restriction"*; decrements appear in *"training tolerance, fatigue, neuromuscular function"* via *"impaired recovery, reduced training quality, or low carbohydrate availability."*

**→ THE PREDICTION FOR A PITCHING STAFF: underfueling should NOT show up first in peak velocity. It should show up in the back half of outings, the second start of a weekend, and the fourth week of a block.** ⚠️ A DIRECTION, not a magnitude (F-473). Nobody has tested it.

---

## 4. THE DETECTION ARITHMETIC (F-495, F-506)

**SD of 12-week body-mass change in D1 baseball = 4.8 kg (10.6 lb). SD of FFM change = 3.6 kg (7.9 lb).**

At 80% power, α = .05 two-tailed (z = 2.80):

| Design | Smallest detectable |
|---|---|
| Paired pre-post, n = 10 | 4.3 kg (9.4 lb) |
| **Paired pre-post, n = 15** | **3.5 kg (7.7 lb)** |
| Paired pre-post, n = 20 | 3.0 kg (6.6 lb) |
| Paired pre-post, n = 30 | 2.5 kg (5.4 lb) |
| **Two arms, 15 each** | **4.9 kg (10.8 lb)** |
| Two arms, 30 each | 3.5 kg (7.7 lb) |
| **Two arms, 1 kg difference** | **~362 per arm** |

**Consequence: a college program can never run a controlled test of its own nutrition plan on its own pitchers.** The honest unit of decision is the individual athlete's own trend.

⚠️ Conservative: the SD contains BodPod measurement error, so the biological SD is smaller. Not by enough to change the conclusion.

---

## 5. THE PROTOCOL — what to actually run

**Cost: one scale.**

1. **Morning weight, post-void, pre-food, same scale, every day.** Logged.
2. **Seven-day rolling mean per man.** A single morning weight is noise — day-to-day hydration swing is on the order of a kilogram.
3. **Establish each man's own four-week baseline now**, in the fall, while the schedule is calm.
4. **Trigger: a seven-day mean 3 lb below HIS OWN four-week baseline.** Individual, never a roster target.
5. **The trigger starts a conversation about food.** Not a DXA. Not a questionnaire. Not an EA calculation.
6. **Say the limit out loud:** you will never prove at team level that the program worked (§4). Stop building slides that claim it.

**What to say to the athlete:** *"Heavier college pitchers throw harder than lighter ones. Nobody has ever shown a pitcher throws harder after he gains weight. We're not chasing weight. We're not losing it by accident either."*

**The secondary log, for the staff and not for any individual (F-500's prediction):** fastball velocity by pitch number, every outing; one number per start = (innings 1–2 mean) − (innings 5–6 mean); overlaid on the weight trend. ⚠️ With within-outing fade at ~0.2 mph/inning (F-384, from an 81 mph sample) and start-to-start SD bracketed at 0.8–1.2 mph (F-289), **one start proves nothing and an individual needs ~20–30 logged starts.** This is a staff-level pattern check across a dozen arms or it is nothing.

---

## 6. STANDING WARNINGS EARNED IN THIS TOPIC

- **F-497 — force-plate familiarization.** Merfeld 2024 prints a **+44.79%** CMJ peak-power gain (37.64 → 54.50 W/kg, ES 1.41, p = 0.01) across a summer league with no training intervention described and no explanation offered. Same twelve men, same device, ten weeks apart. **A pre-post force-plate design without a familiarization session can manufacture an effect the size of a year of training.** Whoever runs F-449's within-athlete impulse design must build in familiarization trials and record device/software version every session.
- **F-499 — the deficit reductio.** Convert any reported energy deficit to kg/season (`deficit × days ÷ 7,700`) and ask whether the athletes would still exist. Under a minute. It invalidated a 2025 peer-reviewed conclusion on first use. Third member of the thirty-second-check family with F-465 and F-489.
- **The search summariser is not a reader.** It merged two different NCAA D1 body-composition papers into one answer this cycle (F-503), presenting a cross-sectional n = 201 DXA study's methods as a seasonal study's methods. Same failure mode as the 2026-09-24 mound catch.

---

## 7. OPEN QUESTIONS

1. Does the 2017 peer-reviewed Rossi paper report a between-group difference the 2015 abstract does not? **If yes, F-494 is withdrawn.**
2. What are the actual n, kg and CIs in the NCAA D1 seasonal body-composition split by position?
3. Is there any dataset pairing an individual pitcher's body-mass trajectory with his velocity trajectory? **This is the only thing that converts F-001 from a marker into a lever — or kills it.**
4. What is the within-athlete SD of in-season weekly body mass for a college pitcher? (F-507 item 6 — a scale and a season.)
5. Does the back-half prediction (F-500) hold? Nobody has measured a nutrition or energy variable against any pitching outcome, ever.
