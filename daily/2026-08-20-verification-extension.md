# 2026-08-20 — VERIFICATION PASS: Extension and Perceived Velocity

**Purpose.** The 2026-08-19 cycle (topic: EXTENSION AND PERCEIVED VELOCITY) ran with **zero source-level reads** — every industry claim came from search snippets. This pass has full web access and went to the primary sources. Seven claims checked.

**Population scope:** elite, 85 mph floor. Off-population samples are flagged `SAMPLE MISMATCH — directional only`.

**Headline:** the geometry survives intact. The *mechanism* claim that made extension look biomechanically costly does not survive as stated, and the *attribution* on the outcome claim was wrong. Nothing was fabricated; two things were misread.

---

## Verdict summary

| # | Claim | Verdict |
|---|---|---|
| 1 | Sherwood, Hinrichs & Yamaguchi (1997) supports "horizontal abduction negatively correlated with velocity" | **CORRECTED** — source exists but is a conference abstract with no retrievable data; Driveline's anatomical label is inverted; and it does not bear on release extension at all |
| 2 | The Driveline "Myths" article shows no correlation between perceived velocity and xwOBA-on-contact / SwStr% | **REFUTED as to source** — not in that article. Traced to the real source; substance roughly holds but has NO published numbers |
| 3 | +1 ft extension = +1.8 mph perceived, 7.2 ms at 95 mph; 0.145 mph/inch | **CONFIRMED with a minor arithmetic correction** — 1.80 mph/ft and 7.2 ms are right; 0.145 mph/in is slightly low and internally inconsistent with the 1.8 figure |
| 4 | Extension + release height predict VAA at R² = .945 | **CORRECTED** — the number is real and correctly quoted, but it is a near-geometric identity reported as a statistical finding, and it does NOT show extension has independent leverage on VAA |
| 5 | Stodden (2005) — forward trunk tilt at release is the only near-release variable with within-athlete velocity support | **CONFIRMED** (design and result), **UNVERIFIABLE** on sample level and mean velocity |
| 6 | Does extension change hitter outcomes independent of VAA and velocity? | **UNRESOLVED — but no longer empty.** Three real analyses found, all cross-sectional, none isolating extension from velocity or VAA |
| 7 | No intervention has trained extension in 85+ pitchers and measured the change | **CONFIRMED** — absence holds, and holds at *every* level, not just 85+ |

---

## 1. Sherwood, Hinrichs & Yamaguchi (1997) — **CORRECTED**

**The source exists.** It is:

> Sherwood, C.P., Hinrichs, R.N., & Yamaguchi, G.T. (1997). *Relationships between ball release velocity and 3D joint kinematics in baseball throwing.* Presented at the **21st Annual Meeting of the American Society of Biomechanics**, Clemson, SC, September 1997.

Verified against **Richard N. Hinrichs's curriculum vitae** (Arizona State University, July 2017 edition), where it is listed among conference presentations. NOT a fabrication — this one is real, which is worth saying given the 16 named fabrications this corpus has already caught.

**But four things are wrong with how it is being used.**

**(a) It is a conference abstract, not a peer-reviewed paper.** ASB annual-meeting submissions of that era were one-to-two-page abstracts. There is no journal version. The full ASB 1997 proceedings are not retrievable online. Therefore:
- **Sample size: NOT AVAILABLE.**
- **Competition level: NOT AVAILABLE.**
- **Mean fastball velocity: NOT AVAILABLE.**
- **The actual correlation coefficient: NOT AVAILABLE.** No r, no n, no p is reported by Driveline or by any downstream citation.

`ABSTRACT CONTENT UNVERIFIED.` The citation is verified; the data behind it is not, and the corpus should never quote a magnitude from it.

**(b) The anatomical label is inverted.** Driveline writes: "a pitching upper arm that is **translated closer to home plate** with respect to the trunk (**shoulder horizontal abduction**) is negatively correlated with fastball velocity." Under standard convention, an arm carried *forward, toward the plate, across the plane of the trunk* is horizontal **ADDUCTION**. Horizontal abduction is the arm *behind* the trunk plane. The parenthetical contradicts the phrase it is defining. Anyone reading the term rather than the description gets the sign backwards.

**(c) The substantive direction is independently corroborated — by Stodden 2005.** Stodden et al. found *decreased shoulder horizontal adduction at foot contact* significantly related to *increased* ball velocity, within-pitcher. Less arm-across-the-body = more velocity. That is the same direction Driveline is describing, arrived at by a different lab with a retrievable design. **So the claim itself is probably true.** It just does not need Sherwood to stand up, and Sherwood cannot be quoted for a magnitude.

**(d) — and this is the important one — NEITHER SOURCE IS ABOUT RELEASE EXTENSION.** Both Sherwood (per Driveline's description) and Stodden measure **shoulder horizontal position relative to the trunk, at foot contact and during acceleration**. Release extension is *how far in front of the rubber the ball leaves the hand* — a function of stride length, standing height, forward trunk tilt and arm length. These are different constructs at different instants of the delivery.

**The inference "extension is biomechanically costly because horizontal abduction is negatively correlated with velocity" is a non-sequitur.** A pitcher can gain a half-foot of release extension through stride and trunk tilt without changing shoulder horizontal position at foot contact by one degree. Yesterday's framing — that this mechanism "makes extension look costly" — imported a cost that the cited literature does not establish.

`CAUSALITY: CROSS_SECTIONAL (Sherwood, presumed — design not retrievable) / MECHANISM as used.`
`CONTROL GROUP: N/A — not an intervention. Do not infer otherwise.`

---

## 2. The Driveline "Myths" article — **REFUTED as to source**

Fetched: `drivelinebaseball.com/blogs/blog/pitching-mechanics-myths-chin-to-target-release-ball-closer-to-the-plate` (originally published January 2012).

**What is actually in it:** almost nothing quantitative. The complete numeric content is one worked example — David Robertson, 93 mph average fastball, ~7 ft extension, ~95 mph effective velocity — plus the Sherwood citation, plus a passing reference to TrackMan releasing "effective velocities" (linked to a 2011 Sports Illustrated piece). **No sample sizes. No correlations. No r or R² values. No xwOBA. No swinging-strike rate. No figures.**

**Yesterday's claim is not in this article.** It is not in any Driveline article under that framing either. Here is the actual provenance chain:

1. **Aucoin, D. (23 May 2019), "Calling the Right Pitch: Investigating Effective Velocity at the MLB Level," Driveline Baseball.** This is the real analysis. Dataset: **MLB Statcast 2015–2018, >2.8 million pitches.** Its subject is **Perry Husband's Effective Velocity** — a *location*-based construct that adjusts pitch speed by where contact is estimated to occur — **not** extension-based Perceived Velocity. Findings on EV: peak offensive production at ~89 EV mph rather than the theorized 90; batter production *increased* as back-to-back EV difference increased, opposite to theory; real zone adjustment ~1.25 EV mph vs a theorized 8–10 mph spread. Conclusion: "little evidence supporting EV sequencing theory at the MLB level since 2015."
2. **In a secondary robustness check**, Aucoin substituted **Perceived Velocity** (2018 Baseball Savant player estimates) for EV and raced it against Release Speed. Result, verbatim: *"Perceived Velocity was found to have a slight edge over Release Speed in swinging strike percentage, but once xwOBACON and Projected RA9 were considered, Release Speed once again remained king."* Conclusion: *"Perceived Velocity did not describe performance more accurately than release speed... It is unlikely that pitchers benefit from manipulating batter reaction time (within the rules of the game)."* **No sample size, no coefficients, no R² are published for this comparison.**
3. **Wilkes, M. (5 June 2019), "The Art of Deception: A Primer on Perceived Pitch Velocity," Redleg Nation** paraphrased (2) as: a Driveline study found *"little correlation between perceived velocity and xwOBA... on batted balls and swinging-strike rate."* This paraphrase is the sentence yesterday's cycle picked up from a snippet and mis-attributed to the 2012 Myths article.

**Verdict:** the *substance* of yesterday's claim survives — Driveline did conclude Perceived Velocity adds nothing over Release Speed on xwOBACON and projected RA9. But three things must be recorded:
- It is in a **different article**, about a **different construct** (EV, not PV), with PV as a secondary check.
- It is **entirely unquantified**. There is not one number attached to the PV-vs-Release-Speed comparison. It cannot be called "a published null" — it is an unquantified assertion in grey literature, the same error class as F-232.
- Aucoin's own PV result contains a detail the paraphrase drops: **PV beat Release Speed on swinging-strike percentage.** The null is on contact quality and run prevention, not on whiffs. That is a meaningfully narrower claim than the one the corpus was about to record.

`EVIDENCE: WEAK (grey literature, vendor-published, no numbers disclosed)`
`CAUSALITY: CROSS_SECTIONAL`
`POPULATION: MLB`

---

## 3. The perceived-velocity geometry — **CONFIRMED, minor arithmetic correction**

Recomputed independently from the corpus's own recovered formula (F-150):

    PV = release_velocity × 54.17 / (60.5 − extension)

**At 95 mph, 6.5 ft → 7.5 ft extension:**
- 6.5 ft: 95 × 54.17 / 54.00 = **95.30 mph**
- 7.5 ft: 95 × 54.17 / 53.00 = **97.10 mph**
- **Δ = +1.80 mph per foot.** ✅ Yesterday's +1.8 mph is correct.

**Timing at 95 mph** (139.33 ft/s, constant-speed): 54.0 ft → 387.6 ms; 53.0 ft → 380.4 ms. **Δ = 7.18 ms.** ✅ Yesterday's 7.2 ms is correct. *Refinement:* real fastballs shed ~8–10% of release speed in flight; using a ~91 mph flight average gives Δ ≈ **7.5 ms**. So 7.2 ms is a slight *under*-estimate, not an over-estimate. Either figure is fine to quote; 7.2 is the conservative one.

**Per-inch — ⚠ this is where yesterday slipped.** The derivative is
`d(PV)/d(ext) = v × 54.17 / (60.5 − ext)²`, so the per-inch figure is **extension-dependent**:

| Extension | mph per inch (at 95 mph) |
|---|---|
| 6.00 ft | 0.1444 |
| 6.33 ft (formula's neutral point) | 0.1461 |
| **6.51 ft (MLB 2024 four-seam mean)** | **0.1471** |
| 7.00 ft | 0.1511 |
| 7.50 ft | 0.1554 |

Yesterday's **0.145 mph/inch** corresponds to an extension of about **6.05 ft** — below league average and not the baseline yesterday used. At the league-mean 6.51 ft it is **0.147**. And the two figures yesterday quoted are internally inconsistent: 1.80 mph ÷ 12 = **0.150**, not 0.145. **Use 0.15 mph per inch at 95 mph as the round number, and state the baseline extension whenever the per-inch figure is quoted.** The error is ~3% and changes no decision — but the corpus should not carry two numbers that do not reconcile.

**The realistic range of extension change — the answer that actually matters.**

The corpus's own MLB 2024 four-seam distribution (F-153, n = 6,113): **mean 6.51 ft, SD 0.45 ft, p95 7.30, p99 7.60, floor ~5.3.**

A **+1 ft** gain is therefore **+2.2 SD**. It moves a median-extension pitcher from the 50th percentile to *past the 99th*. It is roughly the full observed range of the major leagues. **"+1 foot of extension" is not a training target; it is a scale bar.** Quoting +1.8 mph without that context is the single most misleading way to present this geometry, and it is how it is nearly always presented.

Extension is ~**1.04× pitcher height** on average (F-150) — that is, it is dominated by anthropometry, plus stride length, which this corpus already demoted from lever to marker (F-043). No published data exists on within-athlete trainable range (see Claim 7). **Scaling honestly to a plausible individual change of 0.1–0.3 ft gives +0.18 to +0.54 mph perceived, and 0.7–2.2 ms.** That is the size of the real prize.

`EVIDENCE: ESTABLISHED (own computation, reproduced independently this cycle)`
`CAUSALITY: MECHANISM`

---

## 4. The VAA claim, R² = .945 — **CORRECTED**

**Source found and read:** Zahradnik, R. (26 October 2020), *"Fastball Vertical Approach Angle,"* **Medium / Iowa Baseball Managers**. Blog post. Yesterday's "blog-level" flag was correct.

Verbatim: *"A simple regression equation with those variables as inputs returns an R-Squared value of .945, a great predictor of VAA."* Sample: **"a sample of 2,350 pitchers."** No season stated. No league level stated. No pitch count stated. **No coefficients published.** Direction only: "More extension leads to a flatter VAA, and a higher release height shows a steeper approach angle."

**Is R² = .945 plausible? Yes — trivially so, and that is the problem.**

**This is very close to a geometric identity being reported as a statistical finding.** Three reasons:

1. **VAA is fully determined by geometry, not by athleticism.** This corpus's own computation (F-151, n = 6,110) recovers VAA at **R² = 0.999** from plate height, release height, IVB and velocity. There is essentially no residual. Anything predicting VAA from release-point variables is fitting an equation, not discovering a relationship.
2. **⚠ Extension has NO independent contribution once release height is in the model.** F-151 is explicit: *"EXTENSION DROPS OUT entirely once release height is included."* Extension appears predictive in Zahradnik's two-variable model only because extension and release height are strongly negatively correlated — you get more extension largely by getting lower. Extension is a **proxy for release height**, not a second lever.
3. **Plate height is not in the model.** Zahradnik **stratified** by zone (top 3–4 ft, bottom 1–2 ft) instead of entering plate height as a predictor. Location is a VAA variable with leverage nearly equal and opposite to release height (−1.08 deg/ft vs +1.06 deg/ft, F-151). Stratifying it away rather than modelling it inflates the apparent explanatory power of what remains.

**So .945 is real, correctly quoted, and means less than it sounds like.** It is not evidence that training extension moves VAA. The defensible statement is: *release height sets VAA; extension tracks VAA because extension lowers release height.*

**⚠ This also corrects the vault.** F-151 currently reads that this corpus's own computation "independently reproduces Zahradnik 2020, n = 2,350 pitchers, R² = 0.945 from extension and release height." **It does not reproduce it and should not claim to.** F-151's model has four inputs including plate height and reaches R² = 0.999; Zahradnik's has two, omits location, and reaches .945. They are different models of the same geometry. F-151 is the stronger of the two and does not need Zahradnik as corroboration. Annotated in place.

`EVIDENCE: WEAK (blog, no coefficients, no level, no season, location not modelled)`
`CAUSALITY: MECHANISM (geometric identity)`
`POPULATION: unstated — presumed MLB, UNVERIFIED`

---

## 5. Stodden et al. (2005), PMID 16131704 — **CONFIRMED design / UNVERIFIABLE sample**

**Verified real against the journal.** Stodden DF, Fleisig GS, McLean SP, Andrews JR. *Relationship of biomechanical factors to baseball pitching velocity: within pitcher variation.* **Journal of Applied Biomechanics 2005;21(1):44–56.** DOI 10.1123/jab.21.1.44. PMID **16131704**. Lead affiliation: Kinesiology Division, Bowling Green State University; data from the American Sports Medicine Institute.

**Design — this is the part worth protecting.** n = **19 pitchers**, 3-D high-speed motion analysis, **6 to 10 fastball trials each**. Inclusion required each pitcher to display **at least 1.8 m/s of within-subject velocity variation** (observed range 1.8–3.5 m/s ≈ 4.0–7.8 mph). **Three mixed-model analyses** assessed the independent effects of **7 kinetic, 11 temporal and 12 kinematic** parameters on ball velocity.

**This is a genuine within-athlete design** — each pitcher is his own control, so between-pitcher confounds (height, mass, arm length, training age) are differenced out. That is what makes it structurally more informative than the cross-sectional correlations that dominate this literature. **It is NOT an intervention.** Nothing was trained or manipulated; the naturally occurring trial-to-trial velocity variance was exploited. **There was no control group and none is called for.**

**Significant variables (8 of 30):**
- **Kinetic (3):** elbow flexion torque; shoulder proximal force; elbow proximal force. *(All three are load readouts that rise with velocity — consequences, not levers.)*
- **Temporal (2):** increased time to max shoulder horizontal adduction; decreased time to max shoulder internal rotation.
- **Kinematic (3):** decreased shoulder horizontal adduction at foot contact; decreased shoulder abduction during acceleration; **increased trunk tilt forward at release.**

**Yesterday's characterisation holds.** Of the eight, exactly one is a kinematic variable measured **at release**: forward trunk tilt. It is the only near-release variable in this literature with **within-athlete** velocity support. ✅ CONFIRMED.

**But three caveats that were not recorded yesterday:**
- **No effect size is available at abstract level.** The paper is paywalled; no β, no r, no p is retrievable. Do not attach a magnitude to it. The vault's F-236 figure of β = 1.829 (≈ +8.3 mph per 10 deg) is from a **different, between-subjects** dataset (n = 337 pro) and must not be fused with Stodden. That between-subjects β is exactly the kind of number the stride-length collapse (F-043) teaches us to distrust.
- **n = 19 with 30 parameters tested across three models.** Eight significant results at α = .05 across 30 tests is roughly what multiple comparisons would produce on their own if a subset were null. The abstract states no correction. Treat the list as hypothesis-generating.
- ⚠ **Sample level and mean fastball velocity: NOT REPORTED in the abstract and NOT RETRIEVABLE.** The companion paper using the identical cohort and identical inclusion criterion — Stodden, Fleisig, McLean, Lyman & Andrews (2001), *J Appl Biomech* 17(2):164–172 — describes them as **"nineteen elite baseball pitchers."** That is the only level descriptor available, and "elite" in this literature has meant everything from 78 mph up. **The sample's actual mean fastball velocity is UNVERIFIED.** Flag any use accordingly: `LEVEL UNVERIFIED — "elite" per author, mean velocity not reported.` Do NOT record this as an 85+ sample without the full text.

`EVIDENCE: EMERGING (real within-subject design, small n, no retrievable effect size, multiplicity uncontrolled)`
`CAUSALITY: CROSS_SECTIONAL (within-subject observational — NOT an intervention, NOT a manipulated null)`
`POPULATION: "elite" per authors — LEVEL AND MEAN VELOCITY UNVERIFIED`

---

## 6. Does extension change hitter outcomes independent of VAA and velocity? — **UNRESOLVED, but no longer empty**

Yesterday logged this as a brand-new open dispute with nothing behind it. **That was too pessimistic — three real analyses exist.** None of them answers the question as posed, but they bound it.

**(a) Podhorzer, M. (8 July 2025), "All About Pitcher Perceived Velocity," RotoGraphs / FanGraphs.** The single most useful thing found this cycle. He correlates **the gap (perceived velocity − actual velocity)** — which, at fixed velocity, is a *pure monotone function of extension* and nothing else — against outcomes. MLB pitcher-seasons since 2021, minimum 300 pitches:

| Pitch type | Pitcher-seasons | r, Whiff/Swing% | r, K% |
|---|---|---|---|
| All | 1,753 | 0.11 | 0.14 |
| Four-seam (FF) | 1,216 | 0.07 | 0.12 |
| Sinker (SI) | 438 | 0.07 | 0.12 |
| Cutter (FC) | 99 | 0.17 | 0.21 |

**Interpretation:** the extension gap explains roughly **0.5% to 4.4% of variance** in whiff and strikeout rate between pitchers. It is positive and consistent in sign across every pitch type — so probably a real signal — and it is *small*. Podhorzer notes the gap tracks K% more than Whiff/Swing%. **No control for velocity, VAA, movement, release height or command.** Population is MLB — on-scope.

**(b) Wilkes, M. (5 June 2019), Redleg Nation.** A univariate split of **174 MLB pitchers with 500+ fastballs**: swinging-strike rate **10.6%** at or above 6.1 ft extension vs **9.4%** below. A 1.2-point gap. Also reports Glasnow 2019 as the perceived-velocity leader: 96.6 actual → 99.4 perceived, +2.77 mph, 7.61 ft extension, releasing 52.89 ft from the plate. **No velocity control** — higher-extension pitchers are not a random draw, and Wilkes himself notes that of the top-20% differential group, six of the notable performers were already ≥1 mph above league-average velocity.

**(c) Aucoin, D. (2019), Driveline** — see Claim 2. PV edged Release Speed on SwStr%; Release Speed won on xwOBACON and projected RA9. Unquantified.

**What nobody has done.** No study — published, preprint or public grey literature — has:
- regressed hitter outcomes on extension **while holding velocity, VAA and movement fixed**; or
- run an **occlusion or VR study** manipulating release distance with velocity held constant, which is the design that would actually isolate the perceptual mechanism.

**Searched and not found.** State this plainly: **the question is open.** The available evidence is three uncontrolled between-pitcher correlations pointing weakly in the same direction, and the most rigorous of the three (Driveline's) concludes extension-driven perceived velocity adds *nothing* over release speed on contact quality and run prevention while possibly adding a little on whiffs. Those two facts are compatible: extension may buy a small whiff edge and no contact-quality edge.

`EVIDENCE: EMERGING (three independent cross-sectional analyses, consistent sign, tiny effect, no controls)`
`CAUSALITY: CROSS_SECTIONAL`
`POPULATION: MLB`

---

## 7. Any intervention that trained extension and measured the change — **CONFIRMED ABSENT**

**Yesterday's absence claim holds, and it is broader than yesterday stated.** There is no such study **at any level** — not just none at 85+.

Searched: intervention/pre-post/randomised designs on extension, release extension, release point, release distance, stride-length training transfer to extension; Statcast year-over-year extension change analyses; drill-based extension protocols. **The only "extension training" content in the index is content-farm listicles** — towel drills, "Stride and Fire," "Walk-Through Drill" — with no measurement of anything, in the exact hazard class this corpus already blocklists.

**The three nearest misses, and why each fails:**

| Study | Design | Why it does not count |
|---|---|---|
| **Ramsey & Crotin** (stride-length crossover) — blinded **randomised crossover**, pitchers threw simulated games at **+25% and −25% of desired stride length**, ≥72 h washout, 8-camera VICON at 240 Hz + 2 Kistler plates at 960 Hz | **MANIPULATED** | The strongest design in the neighbourhood, and it manipulates **stride length**, not extension. **Release extension was not an outcome variable.** It also manipulates acutely, telling us nothing about trainability. |
| **Diffendaffer / Fleisig et al.** — six-week weighted-implement program, **n = 17** (9 collegiate, 8 professional), age 19.9 ± 1.3, pre/post, 28 biomechanical parameters | **Pre-post, NO CONTROL GROUP** | **Pre-training mean velocity 35.1 ± 1.8 m/s ≈ 78.5 mph — `SAMPLE MISMATCH — directional only`, below the 85 floor.** No velocity change across the 17. And decisively: **stride length, release point and release extension were not measured.** Significant changes were joint angles and ROM only (max IR velocity 4,527 → 4,759 °/s, p = .013; shoulder abduction at BR 96 → 93°, p = .041; ER at BR 95 → 86°, p = .009; shoulder adduction torque 103 → 138 N·m, p = .012; dominant-arm IR ROM 53 → 60°, p = .006; total ROM 174 → 184°, p = .031). |
| **University of Nevada, Reno** — 4-week ankle-mobility/balance intervention, stride length measured pre/post | **Intervention, in progress** | Announced 2026, **no published results**. Outcome is stride length, not extension. Watch item only. |

**Verdict: the absence is real and was searched for properly.** Every quantitative statement this corpus makes about extension is either geometry (Claim 3, solid) or between-pitcher cross-section (Claim 6, weak). **Not one line of it establishes that extension can be trained, by how much, or at what cost.** Given that extension ≈ 1.04× height and that stride length has already been demoted from lever to marker (F-043), the prior should be that the trainable share is small.

---

## What yesterday got wrong, and what held

**Held:**
- The perceived-velocity geometry: +1.8 mph/ft and 7.2 ms at 95 mph, both reproduced independently. ✅
- Stodden 2005's design and its status as the only within-athlete support for a near-release kinematic variable. ✅
- The "blog-level" flag on the VAA R² = .945 claim. ✅
- The absence of any extension intervention. ✅ (And it is broader than claimed.)
- Every cited source **exists**. Zero fabrications this cycle. Worth noting after 16.

**Wrong:**
1. **Attribution error (Claim 2).** The xwOBA/SwStr result is not in the Driveline Myths article. It is in Aucoin (May 2019), it is a secondary check inside an analysis of a *different* construct (Perry Husband's Effective Velocity), and it is **completely unquantified**. It also has a sign detail the paraphrase dropped: PV *beat* release speed on swinging-strike rate. Same failure mode as F-232 — a snippet paraphrase recorded as a published null.
2. **Mechanism over-reach (Claim 1).** Sherwood 1997 is an unretrievable conference abstract; Driveline's anatomical label is inverted; and neither Sherwood nor Stodden measures release extension. The "extension is costly" mechanism was imported from studies of shoulder position at foot contact. **The cost is not established.**
3. **Arithmetic (Claim 3).** 0.145 mph/inch is the marginal rate at ~6.05 ft extension, not at the league-mean 6.51 ft (0.147), and it does not reconcile with the 1.8 mph/ft figure quoted alongside it (1.8/12 = 0.150).
4. **Over-pessimism (Claim 6).** "Nobody has tested it" was too strong. Three real analyses exist; they just do not control for anything.

**The single most useful thing learned:** the **perceived-velocity-minus-actual-velocity gap is a clean, publicly available, pure extension variable** — at fixed velocity it is a monotone function of extension and nothing else. Podhorzer used it across 1,753 MLB pitcher-seasons and got r = 0.07–0.21 against whiff and K%. That is the honest ceiling on extension's standalone value at the major-league level: **real, consistent in sign, and worth under 5% of variance.** It also hands the program a ready-made instrument — any future extension question can be asked directly against Savant's `effective_speed − release_speed` without needing new data collection.

---

## Vault changes made this cycle

- **New findings appended:** F-245 through F-250.
- **⚠ CORRECTED 2026-08-20** annotation added to **F-151** — the claim that this corpus's VAA computation "independently reproduces Zahradnik 2020" is withdrawn. Different model, different variable set, location not modelled by Zahradnik, and extension has no independent contribution once release height is included.
- No existing text deleted or rewritten.

