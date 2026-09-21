# The Ball–Hand Interface — friction, rosin, finger force, and whether spin is buyable

**Opened 2026-09-21 (Cycle 19).** Findings **F-425 → F-437**. Six primary texts read in full.
Companion to `stuff-and-command.md` (which holds the spin PHYSICS, F-142→F-159) — this file holds the INTERFACE that generates it.

---

## 1. Why this topic is different from everything else in the corpus

This corpus runs roughly **30:1 cross-sectional to intervention**, and eighteen prior cycles have mostly returned capacity channels an elite arm has already saturated. Friction inverts both problems:

- **It is trivially manipulable.** You can wet a hand or chalk it in one second. You cannot randomise a man into a stride length. Consequently the pitching-side friction literature, small as it is, is **genuinely experimental** — within-subject, randomised order, with washout.
- **It was manipulated at league scale in June 2021** on thousands of 90+ arms at once (F-434).

**So this is the rare topic where the marker/lever rule comes back with an answer rather than a warning.** The answer is: *friction is a lever, and it points almost entirely downward.*

---

## 2. The result, stated carefully

**Destroying friction is catastrophic. Adding it is nearly inert.**

| Manipulation | Effect on spin | Source | Design |
|---|---|---|---|
| Soaked hand vs rosin | **−28.8%, ≈ −620 rpm** | F-425 | INTERVENTION, n = 6, 80.8 mph |
| Rosin vs bare hand, **dry** | **≈ nothing** (μ "not necessarily increased") | F-427 | INTERVENTION, bench, n = 10 non-pitchers |
| Rosin vs bare hand, **wet** | μ increased at high normal force | F-427 | as above |
| Illegal tack removed, league-wide | **≈ −2.6% to −4%** (snippet-only) | F-434 | NATURAL_EXPERIMENT, MLB |

🚨 **The single most important line in this file: the 620 rpm figure is the PENALTY FOR A SOAKED HAND, not the BONUS FOR A CHALKED ONE.** The no-application condition sat between water and rosin. Anyone quoting −28.8% as rosin's upside has inverted the study.

**The two manipulations bracket the real answer.** Destroying friction: ~29%. Removing an *illegal enhancer*: ~3%. **The margin a legally-equipped college pitcher can move is closer to the small number than the large one, and probably much closer to zero.** Friction is a **floor you can fall below**, not a resource you can stockpile.

---

## 3. The mechanism (F-426) — and why it is the best part

At 2000 fps, the decomposition is clean:

- **ω_fc — the fingertip's motion relative to the ball centre — is UNAFFECTED by friction (p = 0.978).** The athlete does the same thing every time.
- **What changes is whether the ball comes with the finger.** Total slip: water **21.6 ± 5.3 mm** vs rosin **8.9 ± 3.5 mm** vs pine resin **8.2 ± 2.2 mm**.
- In every condition but water, **the finger catches a seam** and slip arrests mid-release. Under water, slip runs continuously to release and **no seam catch occurs at all.**

**Two consequences for coaching:**
1. **A slipping pitcher is not making a mechanical error.** Do not coach his hand. Fix the interface.
2. **Seam catch is a binary mechanical event that has never been studied as a trainable skill.** This is the most interesting unopened question in the release phase — see §8.

---

## 4. The compensation (F-429) — what it looks like on video

Under low friction, pitchers **lengthen the radius of the hand path and de-tune the delivery** to reduce the centrifugal force pulling the ball out of the fingers:

- Pitching radius **significantly greater** at 38–52% (p = 0.006) and 62–90% (p < 0.001) of foot-contact-to-release.
- Centrifugal index **significantly lower** at 70–84% (p < 0.001).
- Hand velocity trended lower but **was never significant** — "he slows his arm down" is a trend, not a result.
- Exit questionnaire: *"some participants answered that they pitched the ball by pushing their arms forward."* **Partly conscious.**

**Video signature: a long, pushed arm path, with misses up and to the arm side (F-430).** If a pitcher's arm suddenly gets long on a humid night, **check his hand before you touch his mechanics.**

⚠️ **Honest limit on the miss direction:** the **vertical ARRIVAL location was NOT significant (p = 0.204)** — only the release angle was. And the study measured **bias only, never variability**, by its own admission. **This is not evidence that friction widens location scatter**, which is the quantity command actually cares about.

---

## 5. The finger-strength question — a marker, and not a close call

**F-431.** The only study relating finger characteristics to spin:

- n = 21, **77.9 ± 4.0 mph** (range 70.5–86.1), spin **1,751 ± 171 rpm** against an MLB four-seam mean of 2,313.
- ~13 significant correlations, r = 0.49–0.58, **every single p-value between 0.01 and 0.05**, across 20+ tested pairings. **Bonferroni for 10 tests needs r ≈ 0.62. None survives.**
- **Restriction of range runs backwards and inflates**: an SD of 4.0 mph is far wider than any 85+ staff. Per Luera 2020 (r = .17–.29, n = 149 pros), expect collapse toward zero here.
- **Hand grip strength correlated with nothing.**

**The grip-strength null is the useful part, and it is the cleanest available refutation of the commercial grip-training market.** Nobody has ever trained finger strength in a pitcher and measured spin. Until someone does, this is a marker.

---

## 6. The within-outing thread (F-432 → F-433) — the cycle's best new idea

**F-432, conference abstract only.** Pinch strength across a single outing:

| Cohort | Onset of decline | Pulp / tip at 100 pitches |
|---|---|---|
| Elementary (12) | **none through 70** | — |
| High school (17) | ~60 pitches | −16% / −14% |
| **Collegiate (19)** | **10–20 pitches** | **−22% / −24%** |

⚠️ **The reported velocity correlation (r = −0.64) is rejected by this corpus.** Pooled across three age cohorts, the slowest throwers are also the non-decliners; **that is an age gradient wearing a velocity label**, and the within-collegiate correlation is not reported.

**What survives is enough: the normal-force term in μ × F_normal decays ~a fifth to a quarter across 100 pitches in collegiate arms, starting inside the first 20.**

**F-433 — the prediction, which is NOT a finding:** spin should decay across an outing, and decay faster in humid conditions. **Nobody has measured this in any sport.** It is free to test — spin rate by pitch number, split by humidity, from data every program already logs.

---

## 7. Measurement hazards found in this topic

| Hazard | Where | Rule |
|---|---|---|
| **Effect sizes r > 1** (−1.369, 1.461, 1.187, 1.278), self-acknowledged, uncorrected | PMC11950353 (F-436) | **Read the p-values and direction. Never quote an effect size from this paper.** |
| **r = 0.945 instrument agreement** sold as a strong correlation; **RMSE = 136.2 rpm** is the real number | PMC11950353 (F-435) | When a paper reports r for two measurements of the same quantity, **read the RMSE instead.** 136 rpm of method error cannot resolve a small effect. |
| **Velocity instructed constant at 130 km/h** | Both pitching studies (F-428) | **Never quote the ball-velocity results.** Spin and slip results are unaffected. |
| **Bias measured, variance not** | PMC11950353 (F-430) | Do not claim friction widens command scatter. Unmeasured. |
| **Conference abstract, no full paper, no velocity reported** | PMC13530651 (F-432) | Magnitude is a real measurement; population is unknown. |

⚠️ **F-436 is the one to remember.** That paper is real, indexed, peer-reviewed, open-access, correctly cited, by real authors — **every fabrication defence this corpus owns passes it.** What caught the error was reading the limitations section. Cf. F-373, F-379.

---

## 8. What to actually do — the 20-pitch friction-sensitivity screen

**The individual differences are the coaching content**, and they are the least-quoted result in the source. In F-425's cohort, **participant f lost nothing under a soaked hand** while **b and d fell apart**. Friction sensitivity is a trait, it varies widely, and **twenty pitches identifies it.**

**Protocol.** 10 four-seams with a lightly dampened throwing hand, 10 with rosin, alternating in blocks of 5 (never one block of each — F-432 says fatigue moves inside 20 pitches). TrackMan or Rapsodo running.

**Output:** one number per arm — the wet-vs-rosin spin gap. Near zero = a seam-catch technique that survives a bad hand. Several hundred rpm = **a June risk, identified in March.**

**Detection arithmetic** (80% power, α = 0.05, two-sided, mean four-seam spin difference), computed 2026-09-21:

| within-pitcher spin SD | detect 30 rpm | 50 rpm | 75 rpm |
|---|---|---|---|
| 60 rpm | 63 / condition | 23 | 10 |
| 80 rpm | 112 / condition | 40 | 18 |
| 100 rpm | 174 / condition | 63 | 28 |

⚠️ **The corpus holds no within-pitcher four-seam spin SD for an 85+ arm** — the table is bracketed for that reason, and this is a registered gap.
⚠️ **At 10 pitches per condition you can only see a gap of ~150 rpm or larger.** That is fine for screening. **Do not report a 40 rpm difference from 20 pitches as anything at all.**
⚠️ **The variance test — the one F-427 actually predicts — needs on the order of 200 pitches per condition.** That is a season of charting, not a bullpen. Say so out loud.

**And the honest prediction: the mean test on dry hands comes back NULL.** If the mean moves, be suspicious.

---

## 9. Open questions carried forward

1. **Is seam catch coachable?** (F-426) The binary event that defeats slip, and nobody has asked whether it is a skill.
2. **Does spin decay within an outing, steeper on humid nights?** (F-433) Free to measure.
3. **Does ball-to-ball leather variation exceed the grip-aid effect?** (F-437) If so, every A/B here — including §8 — is underpowered for an unpriced reason.
4. **No friction study has ever been run on a pitcher above 81 mph.**
5. **Nobody has trained finger strength and measured spin.** (F-431)
6. **The within-collegiate velocity/pinch-decline correlation is unreported.** (F-432)

---

## 10. Sources read in full, 2026-09-21

| Source | PMCID | What it is worth |
|---|---|---|
| Yamaguchi et al. 2025, *Sci Rep* 15:9514 | PMC11950353 | ⭐ **The manipulation.** Spin, slip, control. Effect sizes unusable (F-436). |
| Yamaguchi et al. 2025, *Sci Rep* 15:27759 | PMC12310948 | The kinematic compensation. n = 8, SPM1D. |
| Yamaguchi et al. 2020, *Front Sports Act Living* 2:30 | PMC7739770 | ⭐ **The rosin correction.** Bench, non-pitchers, but the only direct μ measurement. |
| Yeh et al. 2024, *Sensors* 24:3523 | PMC11175286 | The finger-strength marker, at 77.9 mph. Grip-strength null. |
| Yasui et al. 2026, *OJSM* 14(8 suppl 6) | PMC13530651 | Pinch decline within an outing. Abstract only; velocity correlation rejected. |
| Pradeep et al. 2024, *PNAS* 121:e2413514121 | PMC11588067 | The ball side of the interface is real. |

**NOT read (blocked or unavailable):** the NYT/Athletic 2021 analyses that the peer-reviewed literature itself cites (F-434); the Louisiana Tech MS thesis (Watson) gating the "40% of spin efficiency" claim; Shibata et al. 2022, *Sports Biomech*, on tangential finger force and spin (no PMC deposit located).
