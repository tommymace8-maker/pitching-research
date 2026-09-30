# THE FRONT SIDE — the glove arm and the lead-leg block

**Opened 2026-09-29.** Findings **F-508 → F-518**. Disputes **#47**, **#48**.
Companion topic to `library/biomechanics.md` (trunk/pelvis) and `library/velocity-development.md`.

**Reading status: FIVE PRIMARY TEXTS READ IN FULL** via the PMC OA S3 route (see §0). The eighth consecutive reading cycle.

---

## 0. Egress note — the S3 prefix in INDEX.md was being applied wrongly

Every journal host probed on 2026-09-29 returned `000` (frontiersin, sportrxiv, ijspt.scholasticahq, nature, europepmc, tandfonline, api.openalex, api.crossref, and `en.wikipedia.org` as a control). **WebFetch to `pmc.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `journals.sagepub.com` and `etd.auburn.edu` all returned EGRESS_BLOCKED.** Only `pmc-oa-opendata.s3.amazonaws.com` answered (200).

⚠️ **The first three S3 attempts this cycle returned "not in OA subset" for articles that ARE in the subset**, because the prefix was built as `oa_comm/txt/all/PMC{id}.`. **That layout is wrong.** The working layout is the one INDEX.md states — **a bare root prefix**:

```
LIST : https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC{id}.
READ : https://pmc-oa-opendata.s3.amazonaws.com/PMC{id}.{v}/PMC{id}.{v}.txt
```

With the correct prefix, **8 of 10 probed PMCIDs returned full text in under two minutes.** Recorded here because two minutes of this cycle were lost to it and the next cycle should not repeat it.

---

## 1. The claim as the field states it

The classic amateur cue — "firm front side," "equal and opposite," "pull the glove to your chest," "bring your chest to your glove" — is one of the oldest teaching points in the sport. Against it sits an explicit industry rejection: Driveline's *Why We Don't Teach Equal and Opposite (or Firm Front Side)*, and the softer replacement cue "control your glove."

**Both camps argue from mechanism. Neither argues from data, because the data does not exist.** That is this topic's entire finding.

---

## 2. The only dedicated glove-arm study in baseball — and what it actually measured

**Barfield JW, Anz AW, Andrews JR, Oliver GD (2018).** *Relationship of Glove Arm Kinematics With Established Pitching Kinematic and Kinetic Variables Among Youth Baseball Pitchers.* Orthop J Sports Med 6(7):2325967118784937. PMID 30023405, PMCID PMC6047254. **READ IN FULL.**

**Sample:** n = 33 right-handed youth pitchers, **age 13.6 ± 2.0 y**, height 169.4 ± 14.3 cm, mass 63.5 ± 13.0 kg. Electromagnetic tracking. Three fastballs each; **only the fastest was analysed.** 🚨 **SAMPLE MISMATCH — directional only. The age SD alone spans roughly 11.6 to 15.6 years.**

### 🚨 2a. Ball velocity was never measured

**Check #3 (does the number measure what the sentence says it measures?) fails at the first pass.** A full-text search of the paper returns **no radar gun, no mph, no m/s ball speed, and no ball-velocity variable in any of the three correlation tables.** Every occurrence of the phrase "ball velocity" is in the introduction or discussion, citing *other* papers.

The measured outcomes are: pitching-arm elbow and shoulder forces (normalised to body mass), trunk lateral flexion, trunk axial rotation angle, pelvis axial rotation angle, and the **segment** velocity magnitudes of pelvis, torso, humerus and forearm.

The paper's own conclusion nevertheless reads: *"An extended glove arm elbow and more horizontally abducted glove arm shoulder at MER is more advantageous to performance."* **"Performance" here means humeral angular velocity, not pitch velocity.** The secondary paraphrase now circulating — *"for maximum ball velocity to be achieved… a pitcher needs to maintain an active glove arm"* — **inserts an outcome the study never recorded.** This is the exact failure mode Known Correction #6 exists for.

### 2b. The multiplicity arithmetic

Tables 2–4 report **3 event pairings × 12 dependent variables × 2 glove-arm variables = 72 Spearman tests.** The paper states no alpha level and applies **no multiple-comparison correction.** Fourteen results are flagged `P ≤ .05`; **3.6 are expected by chance alone.**

At n = 33 (df = 31):

| Threshold | Critical \|r\| | Results surviving |
|---|---|---|
| Uncorrected α = .05 | 0.344 | 14 of 72 |
| **Bonferroni α = .05/72 = .00069** | **0.5604** | **0 of 72** |
| Benjamini–Hochberg FDR, q = .05 | — | **3 of 72** |

🚨 **The largest correlation in the paper is \|rs\| = 0.52. The Bonferroni critical value is 0.5604. Not one result survives.**

Benjamini–Hochberg retains exactly three — and it is knife-edge. The three all carry the rounded value `P = .002`; the BH threshold at rank 3 is `3 × .05/72 = .002083`. **If the true p were .0021 the whole table would be empty.**

The three BH survivors, all \|rs\| = 0.52, all at MER:
1. glove-arm elbow flexion × pitching-arm elbow valgus/varus force (rs = **−0.52**) — *a kinetic, i.e. injury, outcome*
2. glove-arm horizontal abduction × pitching-arm humerus velocity (rs = **+0.52**) — *a segment velocity*
3. glove-arm horizontal abduction × pelvis axial rotation angle at BR (rs = **+0.52**) — *a joint angle*

**None of the three is a pitching outcome.** r = 0.52 is R² = 0.27, in a sample whose maturation spread is doing unknown work.

### 2c. The paper contradicts its own key citation

Barfield et al. write: *"Murata found less glove arm shoulder joint movement as a requirement for increased ball velocity."* **That is the opposite of the "active glove arm" the paper concludes for** — and Murata is the one cited source in the paragraph that used **ball velocity** as its outcome. The authors resolve this with *"We believe that it takes an active glove arm…"* — belief, stated as such, in place of the disagreeing measurement.

---

## 3. ⭐ The lead-leg block — F-050's 23× dispute is a POOLING ARTIFACT, and it is now resolved

**Dowling B, Hodakowski A, Brusalis CM, Luera MJ, Smith CD, Verma NN, Garrigues GE (2024).** *Influence of Lead Knee Extension on Ball Velocity and Elbow Varus Torque in Professional and High School Baseball Pitchers.* Orthop J Sports Med 12(8):23259671241257539. PMID 39157018, PMCID PMC11329978. **READ IN FULL.** This is the exact paper behind F-050's "+1.05 mph per degree."

### 3a. The published slope

> *"Values that derived significance from the 4 groups for lead knee extension were analyzed with regression correlation coefficients. For every 1° increase in lead knee extension, ball velocity increased by 0.47 m/s (1.06 mph) (R² = 0.22; β = 0.472; P < .001)."*

### 3b. Table 2, and the two numbers the paper never computed

| Group | n | Lead knee extension | Ball velocity | | Elbow varus torque |
|---|---|---|---|---|---|
| HS-Low | 17 | −7 ± 5° | 31.2 ± 1.8 m/s | **69.8 mph** | 56.3 ± 12.2 N·m |
| HS-High | 16 | 18 ± 6° | 34.1 ± 2.6 m/s | **76.3 mph** | 64.2 ± 14.7 N·m |
| PRO-Low | 16 | 1 ± 8° | 39.3 ± 1.3 m/s | **87.9 mph** | 95.4 ± 13.3 N·m |
| PRO-High | 18 | 33 ± 7° | 39.8 ± 1.1 m/s | **89.0 mph** | 85.3 ± 10.7 N·m |

**Within-level slopes, computed here:**

| | Δ knee ext. | Δ velocity | **Slope** |
|---|---|---|---|
| Within HS (69.8 → 76.3 mph) | 25° | 6.49 mph | **0.260 mph/deg** |
| **Within PRO (87.9 → 89.0 mph)** | **32°** | **1.12 mph** | **0.035 mph/deg** |
| *Published, pooled across both levels* | — | — | *1.05 mph/deg* |

🚨 **The published slope is 30× the within-professional slope.** The pooled regression is run across a sample whose ball velocity is **bimodal from 69.8 to 89.0 mph** — a 19 mph gap between competition levels. It is measuring the HS-vs-PRO difference and calling it a knee-extension effect. The R² = 0.22 is almost entirely the level split.

### 3b(i). And the resolution

F-050 registered a **23× dispute**: Dowling's 1.05 mph/deg against **Solomito MJ, Garibay EJ, Cohen A, Nissen CW (2024)**, *Sports Biomech* (PMID 35289727), **0.045 mph/deg in n = 121 collegiate — a single competition level.** F-050 attributed the gap to "marker vs markerless conventions, different knee-angle definitions, and between- vs within-subject modeling."

**That explanation is wrong.**

> **Dowling within-professional: 0.035 mph/deg. Solomito single-level collegiate: 0.045 mph/deg. Ratio: 1.29×.**

**The two studies agree.** The 23× was never a measurement-convention disagreement — it was one study's decision to pool two competition levels and the other's decision not to. **See Known Correction #9 and F-510.**

### 3c. 🚨 The elbow-torque sign reverses between levels

F-050's headline is *"buys velocity and charges elbow torque."* The pooled regression gives **+0.27 N·m/deg (R² = 0.075, P = .025).** Table 2 gives:

- **Within HS:** 56.3 → 64.2 N·m across 25° = **+0.32 N·m/deg — torque UP.**
- **Within PRO:** 95.4 → 85.3 N·m across 32° = **−0.32 N·m/deg — torque DOWN.**

**Equal magnitude, opposite sign.** The paper reports a significant group × level interaction for elbow varus torque (P = .005, partial η² = 0.118) and states the professional direction plainly, then publishes a pooled slope with the high-school sign on it.

**At the professional level — the only one on this program's population — more lead-knee extension came with LESS elbow varus torque, not more.** F-050's price clause does not hold for an 85+ arm. See F-511.

### 3d. A second inflation underneath the first

The four groups total **67**, not 100. Pitchers within ±0.5 SD of their group mean were **dropped**. The regression was run on *"values that derived significance from the 4 groups"* — i.e. on the **extreme-groups subsample with the middle third removed**, which inflates a correlation independently of the pooling. **Two inflations stacked, neither disclosed in the abstract.**

---

## 4. Contralateral trunk tilt — the third front-side variable, and a p-value that does not check out

**PMCID PMC13431036 (2025).** *Contralateral Trunk Tilt in High School Baseball Pitchers: Comparison and Relationship with Trunk Rotational Mobility, Compensatory Lateral Flexion, and Performance.* **READ IN FULL.**

- **n = 19** high-school pitchers, 2D video, **ball velocity 33.6 ± 1.8 m/s = 75.2 mph.** 🚨 **SAMPLE MISMATCH — ten mph under the floor.**
- **The paper's own a priori G\*Power analysis required 42 participants. It ran 19.** Registered against interest by the authors, to their credit — and it means every null in the paper (all of Table 1) is uninterpretable, per the F-439 / n ≥ 97 rule.
- Headline: CLT at MER × ball velocity, **r = 0.47, p = 0.004.**

🚨 **That pair is internally inconsistent at the stated n.** At n = 19 (df = 17), r = 0.47 gives **t = 2.195, two-tailed p = 0.042** — not 0.004. A p of 0.004 at n = 19 requires **\|r\| = 0.628.** At n = 57 (the 3 pitches × 19 pitchers the methods describe) r = 0.47 gives p = 0.0002, which is also not 0.004 — and would be pseudo-replication.

**Neither reading reproduces the printed p. The number cannot be used.** See F-514.

---

## 5. Marker or lever — the statement for the front side

**Nobody has ever manipulated glove-arm position in a baseball pitcher and measured ball velocity.**

The search located exactly one manipulation in the topic: **Auburn University ETD 10415/6770, *Effect of Weight in the Non-Throwing Hand on the Baseball Pitching Motion*** — randomised within-subject, four conditions (no glove / normal glove / 0.68 kg / 1.36 kg training glove), three fastballs per condition.

Three reasons it does not close the gap:
1. It manipulated **glove MASS, not glove POSITION** — a different independent variable from every coaching cue in circulation.
2. Its retrievable result is a **kinematic** one (heavier glove → more glove-arm elbow flexion at foot contact and ball release). **No ball-velocity effect is retrievable.**
3. It is an **unpublished master's thesis** and `etd.auburn.edu` is egress-blocked. ⚠️ **SNIPPET-ONLY. UNVERIFIED at source.**

**So the topic's causal ledger is:**

| Variable | Manipulated? | Ball velocity measured? |
|---|---|---|
| Glove-arm elbow flexion | no (mass only, unpublished) | **no** |
| Glove-arm horizontal abduction | **no** | **no** |
| Glove-arm "activity"/timing | **no** | **no** |
| Lead-knee extension | **no** | yes (cross-sectional, and see §3) |
| Contralateral trunk tilt | **no** | yes (cross-sectional, off-population) |

**Every front-side coaching cue in the sport is being taught off a column of "no."**

---

## 6. What the field is arguing, and its standing

| Source | Claim | Verdict |
|---|---|---|
| [Driveline, *Why We Don't Teach Equal and Opposite (or Firm Front Side)*](https://drivelinebaseball.com/blogs/blog/dont-teach-equal-opposite-firm-front-side) | The firm-front-side / equal-and-opposite cue should not be taught | **UNPROVEN — and correct to be unproven.** The rejection is argued from mechanism, exactly like the cue it rejects. Driveline's standing on mechanics data is high; the *evidence* here is not different in kind from the tradition's. |
| [Driveline, *The Interaction of Biomechanics and Command* (Feb 2026)](https://www.drivelinebaseball.com/2026/02/the-interaction-of-biomechanics-and-command/) | **More consistent glove-shoulder abduction and torso lateral tilt at foot plant correlate with lower miss distance**; a variable throwing-shoulder horizontal abduction at MER *also* correlates with lower miss distance | **PROMISING — the single most interesting item in the sweep.** ⚠️ Snippet-only, host blocked, **n unknown**. It is a within-pitcher-SD-against-miss-distance correlation — see Dispute #48. |
| [TopVelocity](https://www.topvelocity.net/2011/05/13/pitching-speed-and-the-glove/) | "Glove-blocking firm front side… absolutely kills shoulder angular rotational velocity, by far the most important component in creating the 90+ MPH fastball" | **MARKETING.** No sample, no measurement, no citation; superlatives in place of numbers. |
| [BetterPitching](https://betterpitching.com/control-your-glove/) | "Control your glove" — active but not yanked; lead elbow down to the side as you rotate | **UNPROVEN, but the best-shaped of the cues.** It is the only one of the four that is a *constraint* rather than an *action*, which is also the only one a pitcher can hold under fatigue. |

**Honest summary of the sweep: one genuinely new idea (the Driveline command/consistency result), and three restatements of a mechanism argument that has been running since the 1980s.**

---

## 7. What to do about it

See F-512's coaching block. The short version: **the front side is a CONSTRAINT to hold, not a POSITION to hit**, because no position has ever been shown to buy anything measurable in this population — but the one accuracy-flavoured result in the whole topic is about **consistency**, not about the mean.

**Do not chase lead-knee extension for velocity in an 85+ arm.** The honest exchange rate at that level is **0.035 mph per degree**. Thirty degrees of extension — which is the entire PRO-high-vs-PRO-low range — is worth **about one mile per hour**, and it is a between-pitcher difference that nobody has moved within an athlete.

---

## 8. What this topic needs

1. **The trivial experiment nobody has run.** Twelve 85+ arms, radar, two within-subject glove-arm conditions (habitual vs a single cue), ~30 pitches each, randomised order. It needs a gun and an afternoon. **F-518 item 1.**
2. **The within-pitcher glove-arm SD against miss distance, on an 85+ staff** — Driveline's result, replicated where it matters, with the n printed.
3. **The within-athlete lead-knee-extension → velocity slope.** Nobody has one. The corpus now has an honest between-pitcher bracket at the professional level (0.035 mph/deg) and nothing within.
