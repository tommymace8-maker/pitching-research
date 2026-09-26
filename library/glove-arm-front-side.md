# THE GLOVE ARM AND THE FRONT SIDE

**Opened 2026-09-26.** Findings **F-483 → F-496**. Disputes **#43, #44**.

> ## ⭐ WHAT MAKES THIS CYCLE DIFFERENT
> **This is the first cycle in the corpus's history to analyse PRIMARY DATA.** Every previous number in this
> registry came from published literature, industry grey literature, or remembered Statcast values. Today the
> Driveline **OpenBiomechanics Project** CSVs were downloaded and analysed directly: **411 fastballs, 100
> pitchers, `pitch_speed_mph` included.** The corpus's standing structural gap — *"The corpus has no primary
> dataset of its own"* — is **partially closed**, and the analysis script is reproducible
> (`library/scripts/glove-arm-obp-analysis.py`).
>
> **And the first thing primary data did was kill the topic's headline claim in the corpus's own population.**

---

## 1. The claim under test

The oldest cue in pitching instruction. Two rival versions, both taught confidently, in direct opposition:

| Cue | What it asks for | Who teaches it |
|---|---|---|
| **"Pull the glove" / "firm front side" / "equal and opposite"** | Glove-side elbow folds and adducts hard into the ribs during arm acceleration; the glove shoulder becomes a fixed fulcrum | Traditional instruction; Barfield 2018 explicitly argues *against* the word "pull" while endorsing an "active" version |
| **"Chest to glove" / keep the glove out front** | Glove stays extended out front; the torso travels to meet it; no pull | Driveline ("Why We Don't Teach Equal and Opposite (or Firm Front Side)"), much of the modern private sector |

The stated mechanism in both cases is the same: **glove arm → trunk rotation → arm speed → ball speed.**
This page tests all three links.

---

## 2. THE STRUCTURAL FACT THAT FRAMES EVERYTHING (F-483)

**The glove arm is not in the elite pitching model.** Verified at source, three independent elite datasets:

| Dataset | n | Population | Mean FB velocity | Glove-arm variables |
|---|---|---|---|---|
| **ASMI / BioPitch** (McCutcheon, Slowik & Fleisig 2025, PMC11789100, **read in full**) | **523 pitchers** (425 pro, 98 collegiate), age 21.2 ± 2.3 | the reference database of professional baseball | **37.1–38.0 m/s = 83.0–85.0 mph** | **ZERO of 21 variables.** The only glove-*side* variable is *trunk contralateral tilt* — a trunk variable |
| **KinaTrax in-game D1** (PMC13519164, **read in full**) | NCAA D1, markerless, in competition | the most ecologically valid elite set | **40.2–40.4 m/s = 89.9–90.4 mph** | **ZERO** |
| **Driveline OpenBiomechanics** (analysed directly, this cycle) | **100 pitchers / 411 fastballs** | 314 college / 42 indy / 23 MiLB / 32 HS pitches | **84.70 ± 4.72 mph** (range 69.5–94.4) | **FOUR — and they are the only elite glove-arm data that exists** |

So: the canonical 21-variable model that every professional biomechanics report in baseball descends from
**does not measure the glove arm at all.** There are no published glove-arm norms for any population above
85 mph. That is why this topic sat uncovered through 482 findings.

**⚠️ And note population check #1 biting again:** ASMI's "425 professional pitchers" average **~83.9 mph** in
the lab. "Professional" is not 95 mph. The corpus has now recorded this on the largest elite dataset in existence.

---

## 3. THE EVIDENCE BASE, RANKED — and it is four studies, three of which are off-population

| Study | Design | n | Population | Ball velocity outcome? | 80%-power detectable r |
|---|---|---|---|---|---|
| **Ishida & Hirano 2004**, *Int J Sport Health Sci* 2:119–128 | ⭐ **MANIPULATION** — non-throwing arm restricted vs free | unknown | unknown | **DISPUTED — two contradictory accounts (F-493)** | unknown |
| **Barfield, Anz, Andrews & Oliver 2018**, OJSM 6(7), PMC6047254, **read in full** | CROSS_SECTIONAL, Spearman, 1 pitch/athlete | **33** | **age 13.6 ± 2.0 yr — YOUTH** | **NO — never reported (F-484)** | **r ≥ 0.471** |
| **Barfield et al. 2019**, *Int J Sports Med*, 10.1055/a-0810-8637 (snippet-only) | CROSS_SECTIONAL regression | **39** | **college SOFTBALL, windmill**, age 20.0 ± 1.4 | **NO** — outcome was a shoulder *moment* | r ≥ 0.436 |
| **Murata 2001**, *J Biomech* 34(12):1643–1647 (snippet-only, via third-party account) | CROSS_SECTIONAL, 2 groups by coach rating | **9** (4 vs 5) | **skilled 38.22 ± 1.02 m/s = 85.5 mph**; less-skilled 35.96 ± 1.45 = 80.4 mph | yes (group means) | **r ≥ 0.816** |
| **⭐ THIS CYCLE, OpenBiomechanics** | CROSS_SECTIONAL, primary data | **59 at ≥85 mph** (100 total) | **88.05 ± 2.21 mph, range 85.0–93.8** | **YES** | r ≥ 0.358 |

**Murata 2001 is the only prior sample at the corpus's velocity floor, and at n = 9 it could only have
detected an effect explaining two-thirds of the variance.** Its "skilled pitchers move the glove shoulder
less" result is the origin of the fulcrum theory and it is unfalsifiable at that sample size.

---

## 4. ⭐ THE PRIMARY-DATA RESULT: ALL THREE LINKS OF THE CHAIN FAIL AT 85+

Pitcher-level means (each pitcher contributes one observation — see §6 on why this matters). Fastballs only.

### Link 1 — glove-shoulder position → ball speed. **NULL.**

| Variable | r vs speed, **all 100** | r vs speed, **≥85 mph (n=59)** |
|---|---|---|
| `glove_shoulder_horizontal_abduction_fp` | +0.057 (p=.571) | **−0.100** (p=.451) |
| `glove_shoulder_abduction_fp` | +0.161 (p=.110) | **−0.007** (p=.957) |
| `glove_shoulder_external_rotation_fp` | −0.215 (p=.031) | **+0.112** (p=.400) — *sign flips* |
| `glove_shoulder_abduction_mer` | −0.069 (p=.495) | **−0.020** (p=.882) |

**Largest on-population association: |r| = 0.112, R² = 1.3%.** 95% CI −0.148 to +0.358.
Bonferroni threshold for 16 tests at n=59 is |r| = 0.376; nothing is close.

### Link 2 — trunk/arm rotational velocity → ball speed. **ALSO NULL at 85+.**

| Variable | r vs speed, all 100 (70–94 mph) | r vs speed, ≥85 mph (n=59) |
|---|---|---|
| `max_torso_rotational_velo` | **+0.328** (p=.0008, R²=10.8%) | **+0.108** (p=.417, R²=1.2%) |
| `max_shoulder_internal_rotational_velo` | **+0.292** (p=.0030, R²=8.5%) | **+0.086** (p=.517, R²=0.7%) |
| `max_pelvis_rotational_velo` | +0.013 (p=.895) | +0.194 (p=.142) |

**This is the finding with reach beyond the topic (F-488).** Even if the glove arm *did* buy trunk rotational
velocity, trunk rotational velocity buys essentially nothing in an all-hard-throwing sample. The chain has no
surviving link. **And it is the cleanest demonstration of Luera-2020 restriction of range this corpus holds** —
computed on new data, same variables, one sample split by the 85 mph floor.

### Link 3 — glove arm → trunk rotational velocity. **The one robust signal, and it is not velocity.**

`glove_shoulder_external_rotation_fp` vs `max_torso_rotational_velo`:
**r = −0.525 (n=100) and r = −0.465 (n=59), both p < .0005**, Spearman −0.467 / −0.470.
**Survives Bonferroni in BOTH samples and survives restriction of range almost intact.** R² ≈ 22–28%.

More glove-shoulder external rotation at foot plant ↔ slower peak torso rotational velocity. This is a real,
replicable association. It is also **a dead end for velocity**, because of Link 2.

A weak echo of Barfield's direction survives: `glove_shoulder_abduction_mer` vs shoulder IR velocity
**r = +0.269 at ≥85** (Barfield's youth value for the analogous pair was rs = +0.52). It does not survive
correction, and it does not reach ball speed (r = −0.020). **The marker propagates exactly one link, then dies.**

---

## 5. ⭐ FIRST GLOVE-ARM NORMS FOR AN 85+ POPULATION (F-489)

53 pitchers with ≥2 fastballs at ≥85 mph; pitcher-mean 88.05 mph.

| Variable | Mean | Between-pitcher SD | Within-pitcher SD | **ICC(1)** |
|---|---|---|---|---|
| `glove_shoulder_horizontal_abduction_fp` | **37.6°** | 13.08 | 3.59 | **0.929** |
| `glove_shoulder_abduction_fp` | **76.3°** | 9.60 | 2.74 | **0.925** |
| `glove_shoulder_external_rotation_fp` | **−43.3°** | 14.85 | 4.08 | **0.932** |
| `glove_shoulder_abduction_mer` | **35.5°** | 8.14 | 1.80 | **0.950** |
| *(context)* `max_torso_rotational_velo` | 1074 °/s | 82.55 | 23.53 | 0.928 |
| *(context)* `arm_slot` | 40.8° | 7.22 | 2.18 | 0.912 |
| *(context)* `stride_length` (× height) | 0.84 | 0.06 | 0.01 | 0.952 |

Nothing like this table exists in the literature. Sign conventions are OpenBiomechanics', not ASMI's or
Barfield's — **do not cross-compare absolute values with published papers** (see §7, check #3).

### And the SD comparison that kills the youth transfer (F-486)

Barfield 2018's glove-arm SDs at MER: **horizontal abduction 38.65°, elbow flexion 47.25°.**
Every glove-arm SD in the ≥85 sample: **8.14° to 14.85°.**
**Ratio 2.60× to 5.80×.** The youth sample's glove-arm variance is dominated by developmental
heterogeneity across an 11.6–15.6 year age band, not by technique choice. A correlation computed across that
spread cannot be read as a technique effect in a population three to six times tighter.

---

## 6. ⭐ F-476's DESIGN EFFECT, VALIDATED ON REAL DATA — AND IT MANUFACTURED A SIGNIFICANT RESULT (F-491)

F-476 warned that every command threshold in this registry assumes independent pitches, and that the ICC was
unpublished. Today it was **measured** — for kinematics, not location — and the correction **checks out
arithmetically**:

| | `glove_shoulder_external_rotation_fp` vs speed |
|---|---|
| **Naive pitch-level**, n = 217 pitches | **r = +0.135, p = .047 — SIGNIFICANT** |
| **Correct pitcher-level**, n = 59 pitchers | **r = +0.112, p = .400 — not significant** |

The significance was manufactured entirely by counting 217 pitches from 59 pitchers as 217 independent
observations. And the predicted effective n lands almost exactly:

`DE = 1 + (m−1)ρ` with m = 3.68 pitches/pitcher and ρ = 0.93 → **DE = 3.49 → effective n = 62.2**,
against an observed pitcher-level **n = 59**.

**⚠️ What this does and does not establish.** It validates F-476's *formula* on measured data — the first time
this corpus has done so. It does **NOT** supply ρ for pitch *location*, which remains unpublished and is the
number F-476 actually needs. A kinematic angle (ICC ≈ 0.93, a stable postural signature) and a pitch's
location (an outcome with a large trial-to-trial component) will not share an ICC. **The location ICC audit
stands open, now five days outstanding.**

---

## 7. THE FOUR CHECKS, RUN ON EVERY NUMBER KEPT

1. **Actual sample velocity.** ASMI n=523: **83.0–85.0 mph.** OpenBiomechanics full set: **84.70 mph.**
   Barfield 2018: **never reported, sample aged 13.6.** Murata "skilled": **85.5 mph, n=4.**
   KinaTrax D1 in-game: **90.2 mph.** Only the last is unambiguously on-population, and it has no glove data.
2. **Control group / manipulation?** **One study in the topic manipulated anything** (Ishida & Hirano 2004,
   restricted vs free) and its result is disputed (F-493). A second manipulation exists — a glove-weight
   thesis, four conditions (no glove / normal / 0.68 kg / 1.36 kg) — **egress-blocked, unread, and it
   reportedly also reports no ball velocity.** Everything else is cross-sectional.
3. **Does the number measure what the sentence says?** **No — and this is the topic's central problem.**
   Barfield's headline variable is glove-arm **ELBOW FLEXION**. OpenBiomechanics holds four glove **SHOULDER**
   variables and **no glove elbow variable at all** (checked: 81 columns, 4 contain "glove", all shoulder).
   So today's null tests glove-shoulder *position at two instants*; the coached construct is an elbow *motion*.
   **Conceded in Dispute #43.**
4. **Identity masquerading as a finding?** **Yes, caught (F-494).** PMC11789100's Table 2 reports three
   significant rows; "biomechanical efficiency" is *ball velocity ÷ normalized torque*, i.e. an algebraic
   function of the two rows above it. Its p < .001 carries no information the other two do not.

---

## 8. ⚠️ THREE ARITHMETIC ERRORS IN ONE PEER-REVIEWED PARAGRAPH (F-494)

PMC11789100, read in full. The text states the high-torque group had *"a 1% higher velocity (mean, 38.0 vs
37.1 m/s) but 28% higher normalized torque (0.0637 vs 0.0461)."* Differencing the printed cells (the F-465 rule):

| Printed | Cells | Correct | Verdict |
|---|---|---|---|
| "1% higher velocity" | 38.0 vs 37.1 m/s | **2.43%** | **wrong by 2.4×** |
| "28% higher torque" | 0.0637 vs 0.0461 | **38.2%** (28% only if the *larger* value is the base) | **inconsistent base, undeclared** |
| efficiency 601 vs 810 | 38.0/0.0637 = 597; 37.1/0.0461 = 805 | consistent | **an identity, not a finding** |

**The substantive number, corrected: the 174 highest-torque pitchers of 523 throw 0.9 m/s = 2.0 mph harder
than the 174 lowest, and pay 38% more normalized elbow varus torque for it.** Between-subject, cross-sectional,
not a lever — but on-population and worth having. The F-465 rule has now caught a printed error on two
consecutive readings of ASMI-lineage papers.

---

## 9. MECHANISM — the anatomist's brief, and it argues both ways

**The inertial mechanism is real and it is not small.** ⚠️ **DERIVED IN-CYCLE, not from a source.** One arm is
~5% of body mass — **4.7 kg** for the 93.7 kg ASMI mean. Its centre of mass sits roughly 0.45–0.55 m from the
body's long axis when abducted and 0.15–0.30 m when tucked, so repositioning it changes upper-body rotational
inertia by **order 0.6–1.0 kg·m²**, against a trunk-plus-head longitudinal inertia of **order 1–2 kg·m²**.
That is a change of *tens of percent* in the quantity that sets rotational velocity for a given angular
momentum. **The figure-skater intuition behind the cue is sound physics.**

**Three reasons it still does not deliver:**

1. **Angular momentum is not conserved.** The lead leg is on the ground applying external torque through the
   whole acceleration phase. The skater spins on a frictionless pivot; the pitcher does not. A moment-of-inertia
   argument licenses nothing without the ground-reaction term, and no study in this topic measures it.
2. **The timing is anatomically unavailable as a conscious act.** Arm acceleration from MER to release lasts
   **~30–50 ms**. Electromechanical delay alone — command to measurable force — is of the same order.
   **A voluntarily initiated glove pull cannot be timed inside the window it is supposed to act in.** Whatever
   the glove arm does during acceleration was pre-programmed before foot contact. *(MECHANISM; the phase
   duration is standard, the EMD comparison is derived.)*
3. **There is no headroom.** Peak torso rotational velocity in the ≥85 sample is **1074 ± 83 °/s** — a between-
   pitcher SD of **7.7% of the mean.** The variable the mechanism acts on is already nearly saturated in this
   population, which is the physiological face of the same restriction of range §4 found statistically.

**The honest anatomical reading: a large mechanism producing r ≈ 0 means the system compensates.** Pitchers
self-organise around glove-arm position rather than converting it into rotational speed. That is a more
interesting result than a small mechanism would have been, and it is the strongest argument yet that the glove
arm is a **postural/organisational** variable rather than a power one.

---

## 10. WHAT THE COACH GETS TO KEEP

**Not a velocity lever. A positioning and verification tool — and an unusually cheap one.**

The ICC result (F-490) has a practical edge nobody has stated. Within-pitcher SD for glove-shoulder abduction
at MER is **1.80°**. So to confirm a *deliberate change* actually happened:

| Change you asked for | Pitches per condition for 80% power |
|---|---|
| 5° at `glove_shoulder_abduction_mer` | **2** (call it 10) |
| 3° at `glove_shoulder_abduction_mer` | **6** |
| 5° at `glove_shoulder_abduction_fp` | **5** |
| 5° at `glove_shoulder_horizontal_abduction_fp` | **8** |
| 5° at `glove_shoulder_external_rotation_fp` | **11** |

**Compare ~200 tracked pitches for a 2-inch command claim (F-186), or ~85 paired observations for the
impulse→velocity slope (F-449).** The glove arm is **the cheapest thing in the delivery to verify you changed** —
by a factor of twenty. It is also, per §4, the thing least likely to pay you for changing it. **Those two facts
together are the finding: a variable that is trivially easy to audit and has no established return.**

**So the recommendation is a NEGATIVE one, and it is worth real training time:** stop spending blocks and
cueing attention on the front side in pursuit of velocity, and stop letting a pitcher believe his glove arm is
where his missing 2 mph lives. Use it to set position at foot plant — which is where F-179's *already
registered* consistency result points — and spend the block on something with a measured return.

---

## 11. WHAT DOES NOT EXIST (F-496)

1. **No glove-arm variable in ANY elite normative model** except OpenBiomechanics' four shoulder angles (F-483).
2. **No glove-arm ELBOW measurement in any sample above 85 mph.** Barfield's headline variable, unmeasured
   on-population. **The raw C3D files in OpenBiomechanics contain the markers — this is derivable, not absent.**
3. **No measurement of the glove arm's RATE of adduction** at any level. Every study measures static angles at
   discrete events. The cue is about a motion.
4. **No manipulation of the glove arm with a ball-velocity outcome that this corpus has been able to read.**
   One exists (Ishida & Hirano 2004), free and open-access, and its two published accounts disagree (F-493).
5. **No glove-arm study with a COMMAND outcome**, other than F-179's registered variability analysis.
6. **No test of whether glove-arm position is coachable at all** — no before/after on any population.
7. **The within-bullpen ICC for pitch LOCATION remains unpublished** (F-482 item 7), and §6 does not supply it.

---

## 12. Reproducibility

`library/scripts/glove-arm-obp-analysis.py` — pure Python, no dependencies. Data:
`raw.githubusercontent.com/drivelineresearch/openbiomechanics/main/baseball_pitching/data/poi/poi_metrics.csv`
and `.../data/metadata.csv` (both served HTTP 200 on 2026-09-26). 411 rows, 81 columns, 100 pitchers.
Re-run before quoting any number on this page.

## Sources

- McCutcheon TW, Slowik JS, Fleisig GS (2025). *Kinematic Parameters Associated With Elbow Varus Torque in Elite Adult Baseball Pitchers.* OJSM. [PMC11789100](https://pmc.ncbi.nlm.nih.gov/articles/PMC11789100/) — **read in full**
- Barfield JW, Anz AW, Andrews JR, Oliver GD (2018). *Relationship of Glove Arm Kinematics With Established Pitching Kinematic and Kinetic Variables Among Youth Baseball Pitchers.* OJSM 6(7). [PMC6047254](https://pmc.ncbi.nlm.nih.gov/articles/PMC6047254/) — **read in full**
- *Segmental Momentum Sequencing... Collegiate Pitchers With Different Arm Slots.* [PMC13519164](https://pmc.ncbi.nlm.nih.gov/articles/PMC13519164/) — **read in full** (no glove-arm content; used for population only)
- Driveline OpenBiomechanics Project. [openbiomechanics.org](https://openbiomechanics.org/) / [github](https://github.com/drivelineresearch/openbiomechanics) — **primary data, analysed directly**
- Ishida K, Hirano Y (2004). *Effects of Non-throwing Arm on Trunk and Throwing Arm Movements in Baseball Pitching.* Int J Sport Health Sci 2:119–128. [J-STAGE](https://www.jstage.jst.go.jp/article/ijshs/2/0/2_0_119/_article) — **EGRESS-BLOCKED, UNREAD, accounts conflict**
- Murata A (2001). J Biomech 34(12):1643–1647. [PubMed 11716867](https://pubmed.ncbi.nlm.nih.gov/11716867/) — **snippet-only via third-party account**
- Barfield JW et al. (2019). *The Influence of an Active Glove Arm in Softball Pitching.* Int J Sports Med. [10.1055/a-0810-8637](https://www.thieme-connect.com/products/ejournals/abstract/10.1055/a-0810-8637) — **snippet-only**
- Driveline, *Why We Don't Teach Equal and Opposite (or Firm Front Side)* — **snippet-only, egress-blocked**
- Driveline, *The Interaction of Biomechanics and Command* (Feb 2026) — **already registered as F-179**
