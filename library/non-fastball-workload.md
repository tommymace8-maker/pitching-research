# NON-FASTBALL WORKLOAD ACCOUNTING — what a breaking-ball-heavy outing actually costs

**Opened 2026-09-27.** Companion to `FINDINGS.md` F-483 → F-493. Registry gap closed: *"Non-fastball workload accounting — whether a slider-heavy outing loads differently from a fastball-heavy one at equal pitch count"*, carried in INDEX §5 since 2026-08-17 and escalated 2026-09-09 as the boundary condition on F-303.

## ✅ SOURCE-ACCESS NOTE — THIS IS A READING CYCLE

WebFetch to every journal host remains blocked (`frontiersin.org`, `ncbi.nlm.nih.gov`, `arxiv.org`, `sagepub.com`, and a practitioner blog, `rocklandpeakperformance.com`, all refused; `en.wikipedia.org` refused as a control — `connect_rejected`, the F-277 gateway denial). **The PMC open-access S3 object store at the key layout F-388 established is WORKING**, and **four primary texts were read in full** through it:

| Retrieved at source | What it is |
|---|---|
| **PMC12695764** — Qin et al. 2025, *Front Sports Act Living* 7:1724517 | Player Load by pitch type, trunk sensor, Chinese college |
| **PMC9698011** — Agresta et al. 2022, *Sensors* 22:9008 | Sensor location × pitch type, n = 10 NCAA D1 |
| **PMC12820011** — Hodakowski et al., RPE vs elbow varus torque, HS + PRO | The effort→torque manipulation |
| **PMC11789100** — McCutcheon, Slowik & Fleisig 2025, *OJSM* | n = 523 elite adults, kinematics vs normalized varus torque |

**Snippet-only, and labelled as such everywhere below:** Fleisig 2006 (AJSM 34:423–430), Escamilla 2017 (AJSM), Makhni 2018 (*Arthroscopy* 34:816–822), Okoroha 2018 (AJSM), **Hodakowski 2025 (AJSM 53(3))**, and **Streepy et al. 2024 OJSM Poster 171**, which supplies the load-bearing magnitudes in §3. ⚠️ **The poster is exactly the "real-but-thin source" the standing brief warns about** — see §9.

---

## 1. The question, stated so it can be answered

A coach asks one question with three unrelated answers hiding inside it:

1. **Does a breaking ball cost more ARM LOAD per pitch?** → Answerable. Answer below, and it runs backwards from folklore.
2. **Does a breaking-ball-heavy outing cost more PERFORMANCE later — velocity, command, next-outing readiness?** → **Nobody has ever measured this. Not once, in any population** (§8).
3. **Does a breaking-ball-heavy outing cost more INJURY RISK?** → Out of this corpus's scope, and the literature is inconclusive anyway.

Question 2 is the one a pitching coach is actually asking, and it is the one with zero evidence. Everything published addresses question 1.

---

## 2. Question 1 is settled, and the folklore has the sign backwards

Every study that measured **joint kinetics** — inverse dynamics from motion capture, or a forearm IMU estimating medial elbow torque — puts the **fastball at the top**:

| Study | Population | Finding (as reported) |
|---|---|---|
| Fleisig 2006 (snippet) | 21 collegiate | Elbow/shoulder loads greatest in FB, least in CH. **"Few kinetic differences" between FB and CB.** Slider inconclusive — too few |
| Escamilla 2017 (snippet) | professional | Elbow varus torque **8–9% greater in FB and SL than CH**; shoulder horizontal adduction torque 17–20% greater in SL and CB than CH |
| Makhni 2018 (snippet) | 37 competitive, 8 pitches each, **randomized order** | Torque significantly higher in FB than CB and CH |
| Okoroha 2018 (snippet) | youth/adolescent ⚠️ SAMPLE MISMATCH | FB 47.3 ± 0.5 > CB 45.0 ± 0.5 > CH 44.2 ± 0.5 N·m |
| **Hodakowski 2025**, AJSM 53(3) (snippet) | professional | **FB had significantly greater CUMULATIVE varus torque AND loading rate than ALL other pitch types.** No difference in cumulative torque between CH and breaking balls. **No relationship between spin rate and varus torque, within or across pitch types** |

**Five independent samples, one direction.** The "the slider is what breaks arms" folklore is **not supported by any kinetics measurement.** Graded **ESTABLISHED** for the direction; see §9 for why the *magnitudes* are weaker than the direction.

⚠️ **One caveat the whole table shares: every one of these is a lab bullpen, in sequence, on command.** Nobody measured a pitch thrown to a hitter in the seventh inning.

---

## 3. ⭐ THE RESULT — a breaking ball is NOT a slower fastball at the elbow

This is the cycle's central finding and it is a **derivation from two source-verified numbers plus one snippet**, not a measurement.

### 3a. The within-pitcher torque–velocity exponent (SOURCE-VERIFIED, MANIPULATED)

Hodakowski et al. (PMC12820011), read in full. **24 PROFESSIONAL pitchers**, 3D motion capture at 480 Hz, throwing **fastballs at instructed 75% and 100% effort**. This is an **INTERVENTION** — effort was manipulated within pitcher, analysed with a linear mixed-effects model.

| | 75% effort | 100% effort |
|---|---|---|
| Ball velocity | 35.6 ± 1.0 m/s = **79.6 mph** | 39.7 ± 0.7 m/s = **88.8 mph** |
| Peak elbow varus torque | 73.1 ± 3.0 N·m | 92.1 ± 3.5 N·m |

✅ **The sample clears the 85 mph floor at maximum effort (88.8 mph). This is an ON-POPULATION manipulation, which is rare in this corpus.**

Elasticity: `ln(92.1/73.1) / ln(39.7/35.6)` = **2.12**.

> **Within a pitcher, throwing a fastball, peak elbow varus torque scales as roughly the SQUARE of ball velocity.**

### 3b. Apply it across pitch types

Streepy et al. 2024 (OJSM Poster 171, **n = 41 professional**, ⚠️ **snippet-only**): peak elbow varus torque **FB 93.7 ± 3.3**, **CB 91.0 ± 2.3**, **CH 84.1 ± 2.4 N·m**.

If a curveball were simply a fastball thrown slower, its torque should fall off at the v^2.12 rate. It does not:

| | speed ratio to FB | **predicted** torque ratio at v^2.12 | **observed** torque ratio |
|---|---|---|---|
| CB, 16 mph slower off 94 | 0.830 | 67.3% | — |
| CB, 12 mph slower off 94 | 0.872 | 74.9% | — |
| CB, 12 mph slower off 88 | 0.864 | 73.3% | — |
| **Curveball (observed)** | — | **67–75% across the bracket** | **97.1%** |
| CH, 9 mph slower off 94 | 0.904 | 80.8% | — |
| **Changeup (observed)** | — | **~81%** | **89.8%** |

> ### The curveball carries **22 to 30 percentage points MORE elbow torque than its ball speed predicts.** The changeup carries ~9 points more.

**What this means in one sentence: at the elbow, a breaking ball looks like a 97%-effort fastball that happens to leave the hand 12–15 mph slower.** The pitcher's *arm* is not taking a breather; only the *radar gun* is.

⚠️ **THIS IS A DERIVATION AND ITS WEAKEST LINK IS NAMED.** The exponent comes from a within-pitcher **fastball-effort** manipulation; the ratios come from a **between-pitch-type** comparison in a different sample whose velocities are **not reported in any retrievable form**. The velocity gap is therefore **bracketed at 12–16 mph**, and the conclusion survives the whole bracket. It would be **falsified** by a poster sample whose curveball was only ~5 mph off the fastball — which no professional sample has ever been.

---

## 4. ✅ The arsenal shift is now priced — and F-303's "free lever" SURVIVES

F-303 (2026-09-09) shipped a recommendation to shift the arsenal, noting the cost was unpriced once the shift exceeded ~15 points toward breaking balls. Price it:

```
mean per-pitch peak varus torque, shifting s of pitches FB -> CB
  Δ = s × (91.0 − 93.7) N·m
  s = 0.10 → −0.27 N·m  (−0.29%)
  s = 0.15 → −0.41 N·m  (−0.43%)
  s = 0.20 → −0.54 N·m  (−0.58%)
```

> **A 15-point arsenal shift toward curveballs moves mean per-pitch peak elbow torque by LESS THAN HALF A PERCENT — and the sign is NEGATIVE.** On cumulative torque and loading rate (Hodakowski 2025) the shift is, if anything, mildly protective, because the fastball leads on both.

**F-303's "sequencing is the only lever in this corpus with zero tissue cost" is CONCEDED and upheld** — not because breaking balls are cheap (§3 says they are not), but because they are **priced almost identically to the pitch they replace.** The two results are not in tension: the breaking ball is expensive *relative to its velocity*, and nearly free *relative to the fastball it displaces*.

⚠️ **Boundary: this prices PEAK TORQUE ONLY, at the ELBOW, per PITCH, using a snippet magnitude.** It does not price shoulder load, grip/forearm load (§6), or anything about recovery.

---

## 5. Trunk sensors are blind to pitch type — and one 2025 paper does not know it

Agresta et al. 2022 (PMC9698011), read in full. **10 NCAA D1 pitchers**, five IMUs at 512 Hz, ~35-pitch bullpen, three sensor locations, four workload calculations.

**Trunk sensor, across all four calculations, across all five pitch types:**

| | WL1 peak resultant accel | WL2 peak PlayerLoad | WL3 cumulative PL | WL4 normalized accel |
|---|---|---|---|---|
| **p** | **0.34** | **0.57** | **0.73** | **0.34** |

> **Nothing. Four metrics, four nulls.** The authors' conclusion is explicit: *"trunk-based workload estimates may not appropriately reflect external mechanical load at the elbow (throwing forearm) or the shoulder (throwing upper arm)."*

**And this matters because the newest paper in the topic did not get the memo.** Qin et al. 2025 (*Frontiers*, PMC12695764) mounted a Catapult Vector S7 **between the scapulae** — a trunk sensor — reported large significant pitch-type differences in Max PL, and concluded that *"variable-speed pitches generate greater peak external training loads."* See §7 for why that paper cannot carry the claim.

⚠️ **The null is small: n = 10, and only 5 slider and 6 cutter pitches.** Under the corpus's own F-439 threshold (n ≥ 97) this is an **underpowered null** and must be reported as one. What it defensibly supports: *the trunk is a poor place to look*, which is also what the physics says and what the forearm contrast (§6) demonstrates positively.

---

## 6. The forearm sees something — and it points the OTHER way

Same study, **forearm** sensor. Now everything separates (p < 0.001 for peak resultant acceleration):

| Pitch | Peak resultant accel (m/s²) | vs FB | Cohen's d vs FB | n (pitches) |
|---|---|---|---|---|
| **Fastball** | 1288.7 ± 184.1 | — | — | 184 |
| Change-up | 1241.3 ± 190.6 | −3.7% | −0.25 (n.s.) | 76 |
| **Curveball** | **1450.9 ± 243.5** | **+12.6%** | **+0.75** | 95 |
| Slider | 1840.5 ± 82.0 | +42.8% | — | ⚠️ **5** |
| Cutter | 1336.3 ± 116.2 | +3.7% | — | ⚠️ **6** |

Normalized resultant acceleration, CB vs FB: **0.90 ± 0.05 vs 0.81 ± 0.08, d = 1.35.**

> **At the forearm the curveball is ~13% HIGHER than the fastball and the changeup is INDISTINGUISHABLE from it — the opposite ordering to every joint-kinetics study in §2.**

**This is not a contradiction; it is two different constructs.** Peak forearm resultant acceleration is a **kinematic** quantity dominated by forearm pronation/supination and the deceleration phase. Elbow varus torque is a **kinetic** quantity peaking at maximum external rotation, late in arm cocking. A curveball reorganises the forearm without reorganising the elbow's peak valgus demand. **Both can be true, and the practical upshot is that "workload" is not one number.**

### 🚨 The slider column is five pitches from one pitcher

Table 1 of the paper, read at source: **only player 3 threw sliders (5), and only players 8 and 9 threw cutters (4 and 2).** Every "sliders load the forearm 43% more" claim traceable to this study rests on **five pitches by one human being.**

### ⚠️ A measurement flag, raised as a question not a finding
The accelerometers are specified at **±200 g = 1962 m/s² per axis.** The slider's forearm mean is **1840.5 m/s² — 94% of a single axis's full scale** — and its SD (82.0) is by far the smallest forearm cell in the table. If the resultant is single-axis-dominated at these instants, the largest values are the ones most at risk of clipping, which compresses variance and biases means *downward*. **Unresolved. It requires the raw traces, which are not published.** Dispute #44.

---

## 7. 🚨 Qin et al. 2025 — a published paper that fails four checks at once

*Differences in external loads of different pitch types in Chinese male college baseball players*, Front Sports Act Living 7:1724517, PMC12695764, **read in full**. Registered because it is the newest paper in this topic, it is open-access, it is already being surfaced by search, and **it should not be cited.**

**① The sample is FOUR PITCHERS.** 320 pitches, 80 per type. The paper's own limitations section: *"The small sample size of only four right-handed pitchers…"* The Kruskal-Wallis H statistics (up to **254.68**) are computed as though the 320 pitches were independent. **Pseudoreplication** — the design has 4 clusters, not 320 observations. Nothing in the paper is a mixed model, unlike Agresta 2022 and Hodakowski, which both used one.

**② The sample throws 75.5 mph.** Fastball 121.53 ± 4.68 km/h = **75.5 ± 2.9 mph**, median 122 km/h, P75 126 km/h = 78.3 mph. Described as *"national-level competitors."* ⚠️ **HARD SAMPLE MISMATCH — nearly 10 mph under this corpus's floor.**

**③ THE REGRESSION IS UNIT-MISLABELLED — confirmed arithmetically at source.** The paper reports `mph = 78.816 + 7.001·MaxPL`, R² = 0.192. But speed is measured and tabled in **km/h**. Evaluate at the sample's mean Max PL of 4.217:

```
78.816 + 7.001 × 4.217 = 108.34
mean tabled speed across the four pitch types = 108.33 km/h
the corresponding mph mean would be 67.31
```

**The dependent variable is km/h and it is labelled mph.** The slope is **4.35 mph per AU**, not 7.0. **Second published unit mislabel this corpus has caught at source in four days** (after F-465, 2026-09-24).

**④ The R² is pitch type wearing a Player Load costume.** The regression pools four pitch types whose mean velocities differ by **23 km/h by construction** (FB 121.5, CB 98.6). Across the four type-means alone, Max PL and speed correlate r = 0.456, **R² = 0.21** — essentially the entire reported pooled R² of 0.192. **The within-pitch-type relationship, the only one that could be a lever, is never reported.** "Load up more to throw harder" is not available from this paper.

**⑤ The discussion contradicts the paper's own Table 1.** The text asserts *"the fastball generates higher maximum loads"* and the abstract concludes *"variable-speed pitches generate greater peak external training loads."* Table 1: **Changeup 4.56 is the highest and the SLIDER 3.78 is the LOWEST of all four** — the fastball is third at 4.24. The conclusion is false for the slider, the most-thrown breaking ball in modern baseball. (Table 2 medians agree: slider 3.65, lowest.) The same paragraph calls the fastball *"a strategic off-speed pitch,"* which is not a sentence about baseball.

**Verdict: DO NOT CITE FOR ANY MAGNITUDE.** It is registered here so that a future search surfaces this audit rather than the abstract.

---

## 8. 🚨 What does not exist — and it is the question the coach is asking

Confirmed absent across this cycle's searches (⚠️ **WebSearch only — this is a search of the public web, not of a bibliographic database, which this environment cannot reach**):

1. **🚨 NO STUDY, IN ANY POPULATION, HAS TESTED WHETHER BREAKING-BALL SHARE PREDICTS WITHIN-OUTING VELOCITY OR COMMAND RETENTION.** The entire literature measures **per-pitch load**, never **per-outing consequence**. Fourteenth entry in the F-264 / F-289 / F-295 / F-307 / F-320 / F-336 / F-348 / F-363 / F-374 / F-385 / F-396 / F-457 / F-471 pattern.
2. **No study of pitch-type composition and next-outing readiness.** Interval throwing programs count throws; none weights them by type.
3. **No accuracy outcome anywhere in the pitch-type literature.** Every study in §2 measured torque. ⚠️ **This is the Dispute #27 pattern in its sixth venue** — after the mound (F-471), the pre-game warm-up (F-423), caffeine (F-398), sleep and friction. *The field measures the instrument's favourite variable, not the athlete's.*
4. **No within-pitcher velocity for the pitch-type kinetics samples.** Check #1 cannot be run on Streepy/Hodakowski at all.
5. **Nobody has separated "the breaking ball loads the elbow" from "this pitcher's breaking ball is badly executed."** Strasburg's own account of his 2019–2021 elbow trouble named **delivery inconsistency on an unfamiliar slider**, not the pitch's intrinsic load — a different and untested mechanism.
6. **No within-athlete data on the torque cost of a NEW pitch during acquisition.** If (5) is right, the cost lives in the learning phase, not the pitch.

---

## 9. ⚠️ Evidence-quality ledger — read before quoting anything above

| Number | Status |
|---|---|
| §3a exponent 2.12, PRO 79.6 → 88.8 mph, 73.1 → 92.1 N·m | ✅ **SOURCE-VERIFIED, READ IN FULL, MANIPULATED, ON-POPULATION** |
| §5 trunk nulls (p = 0.34/0.57/0.73/0.34) | ✅ SOURCE-VERIFIED. ⚠️ Underpowered null, n = 10 |
| §6 forearm table, all cells, sensor range, Table 1 pitch counts | ✅ SOURCE-VERIFIED, READ IN FULL |
| §7 every claim about Qin 2025 | ✅ SOURCE-VERIFIED, READ IN FULL, arithmetic reproduced |
| **§3b FB 93.7 / CB 91.0 / CH 84.1 N·m** | 🚨 **SNIPPET-ONLY, AND IT IS A CONFERENCE-POSTER ABSTRACT.** The standing brief's exact warning: *"a conference abstract with no retrievable sample is not evidence for a magnitude."* **§3's and §4's entire arithmetic rests on it.** Its sample's velocities are unknown |
| §2 rows other than Hodakowski 2025 | SNIPPET-ONLY. Direction is corroborated five ways; no single magnitude is verified |
| Hodakowski 2025 AJSM 53(3) | SNIPPET-ONLY. `sagepub.com` blocked. **Top of the verification queue for this topic** |

**Corollary, stated against interest:** if the poster's magnitudes are wrong, §3 and §4 both fall. They are retained because **the direction is independently supported** (Fleisig 2006's "few kinetic differences between FB and CB" says the same thing qualitatively in a *read* paper), and because §3 is framed as a **falsifiable prediction** with a stated bracket.

---

## 10. What to tell the pitcher, and how you would know

**THE SENTENCE:** *"Your breaking ball is not a rest pitch. It costs your elbow about what a fastball costs, at 12 mph less on the gun. You do not get to 'take one off' by spinning one — but you also don't pay extra for it, so mix freely."*

**THE DRILL:** none. This is a **planning** finding, not a cue. There is nothing here a pitcher can feel or consciously change.

**ON VIDEO, THE FAILURE LOOKS LIKE:** a pitcher who visibly dials down for a breaking ball — slower tempo, shorter stride, an arm that "guides." That pitcher is not reducing elbow load (the torque is velocity-squared *within* a pitch type and nearly flat *across* types); he is reducing **stuff**. The cost is spin and shape, and it is paid for nothing.

**THE MEASURABLE CHECK, and the honest sample size:**
Log **breaking-ball share** and **fastball velocity by pitch number** for every outing. The question: does the fastball fade faster in high-breaking-ball outings?

- Within-outing velocity fade at this level is **~0.2 mph/inning** (F-384, borrowed from an 81 mph sample), and the corpus **holds no measured within-outing velocity SD for an 85+ arm** (the tenth entry in the missing-variance pattern). With σ_s bracketed at 0.3/0.5/0.8 mph, detecting a *difference in slopes* between high- and low-breaking-ball outings needs **dozens of starts per arm** — i.e. **more than one season**.
- **So the within-athlete version of this test is UNAFFORDABLE for one pitcher, and the staff-level version is not.** Pooled across ~12 arms × ~14 outings ≈ 170 outings, a slope difference of ~0.15 mph/inning is reachable in one season. **That is the study, and it is a spreadsheet, not a lab.**

⚠️ **Do not run the bullpen version.** F-197: no bullpen-to-game command transfer has ever been demonstrated.

---

## 11. Handed forward

1. **Read Hodakowski 2025 (AJSM 53(3)) and get the poster's sample velocities.** It is the single number that decides whether §3 stands. Route: check the PMC OA bucket periodically; AJSM articles sometimes deposit.
2. **Run the staff-level breaking-ball-share × velocity-fade regression.** It closes gap #1 in §8 with data every program already has.
3. **Separate the pitch from its execution.** Does a *newly acquired* breaking ball cost more than a mature one? Nobody has looked, and Strasburg's own account says that is where the cost is.
