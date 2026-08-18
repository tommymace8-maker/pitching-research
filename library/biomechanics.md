# Biomechanics of the Pitching Motion — Foundational Reference (Elite / 85+ MPH Population)

**Day 1 of ongoing research program**
**Compiled:** 2026-08-12
**Author role:** sports biomechanics (overhead throwing)
**Status:** living document — revise as new studies land

---

## Table of Contents

0. [Population Scope](#0-population-scope)
1. [Reading This Document: Correlation, Causation, and Units](#1-reading-this-document-correlation-causation-and-units)
2. [The Six Phases and Their Timing Landmarks](#2-the-six-phases-and-their-timing-landmarks)
3. [Kinematics in the Elite Band](#3-kinematics-in-the-elite-band)
4. [Kinetics: Torque, Force, and Ground Reaction](#4-kinetics-torque-force-and-ground-reaction)
5. [The Kinematic Sequence](#5-the-kinematic-sequence)
6. [Velocity Determinants vs. Injury Risk — Where They Conflict](#6-velocity-determinants-vs-injury-risk--where-they-conflict)
7. [Measurement Technology](#7-measurement-technology)
8. [Practical Synthesis for the Coach](#8-practical-synthesis-for-the-coach)
9. [Open Questions / Research Gaps](#9-open-questions--research-gaps)
10. [References](#10-references)

---

## 0. Population Scope

**This entire research program is scoped to the ELITE band. Hard floor: 85 mph.**

The athlete this model serves is one of:

| Tier | Description | Typical game FB |
|---|---|---|
| Elite HS | Perfect Game / showcase-circuit caliber, D1-committed or draft-followed | 85–94 mph |
| NCAA D1 | Scholarship arm, weekend rotation or leverage bullpen | 88–96 mph |
| MiLB | Affiliated professional | 91–98 mph |
| MLB | Major league | 93–100+ mph |

**Target state:** 90–95+ mph.

### Rules this scope imposes on every report

1. **No youth data as a primary source.** Any study sampling Little League, unselected middle-school, or unselected high-school pitchers is either dropped or explicitly labeled **`[OFF-POPULATION]`** and treated as directionally suggestive only.
2. **Prioritized data sources:** the ASMI professional/collegiate database (n in the hundreds), Driveline's collegiate/professional force-plate and mocap datasets (OpenBiomechanics), KinaTrax in-game MLB/D1 markerless data, and any peer-reviewed study with a MiLB/MLB/D1 sample.
3. **The relevant question is never "how does a pitcher differ from a non-pitcher."** It is **"what separates a 95 mph delivery from an 87 mph delivery inside this band"** — i.e., *within-elite variance*.
4. **Watch the "elite HS" trap.** Most published "high school" cohorts average ~70 mph and are *not* our population. E.g., Escamilla/Fleisig's HS arm-slot cohort (n = 130) averaged 31.4 ± 3.2 m/s = **70.2 ± 7.2 mph** ([Escamilla et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/)). Our 85+ HS athlete sits ~2 SD above that mean and looks kinetically much more like a professional than like his published "HS" peers. **Treat published HS norms as a floor, not a target.**

### A critical measurement caveat before any number below

**Lab velocity ≠ game velocity.** ASMI's professional database averages ~38.1 ± 4.1 m/s = **85.2 ± 9.2 mph** in-lab ([Escamilla et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/)); the Fleisig UCL prospective cohort averaged **84.7–85.0 mph** in-lab for pitchers who were, in games, throwing 92–95 ([Fleisig et al., 2025 OJSM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227930/)). Lerch et al. (2025) note explicitly that "pitchers typically throw slower in a laboratory setting than they do in-game" ([J Biomech](https://asmi.org/wp-content/uploads/LERCH-Journal-of-Biomechanics-2025-188-112775.pdf)).

**Implication:** a lab-measured 85 mph pro is likely a 90–93 mph game arm. Do not read published lab means as game velocities, and do not conclude the pro database "only throws 85." **Torque values reported from these labs are therefore likely to UNDER-represent in-game torque.**

---

## 1. Reading This Document: Correlation, Causation, and Units

### 1.1 The epistemics problem

Almost the entire pitching-biomechanics literature is **cross-sectional**: a pitcher throws 8–12 fastballs in a lab on one day, and variables are correlated with velocity or with torque. This design cannot establish that changing a variable will change the outcome. Three specific traps:

- **Between-subject vs. within-subject associations diverge — sometimes wildly.** The single most important methodological finding in this literature: Slowik et al. (2019) analyzed 64 professional pitchers and found the association between fastball velocity and elbow varus torque was **weak between subjects (R² = 0.076, p = .03)** but **very strong within an individual pitcher (R² = 0.957, p < .001)** ([J Athl Train 54(3):296–301](https://pubmed.ncbi.nlm.nih.gov/30721094/)). Meaning: *comparing two pros, the harder thrower is not reliably under more elbow load; but when a given pitcher throws harder, his own elbow load reliably goes up.* Cross-sectional group comparisons systematically hide the individual dose-response.
- **Reverse causation and confounding.** Bigger, stronger, longer-levered athletes both throw harder and produce higher absolute torques. Leg length alone was a significant velocity predictor in professionals (β = 0.292, p < .001; [Diffendaffer/Fleisig group modeling study, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11322935/)).
- **Survivorship.** Every "professional pitcher norms" table is drawn from arms that survived to be tested. The mechanics that broke are underrepresented.

### 1.2 Prospective evidence is scarce

There is essentially **one** high-quality prospective biomechanics→injury study in professional baseball (Fleisig et al., 2025, 305 MiLB pitchers, ~4.5 yr follow-up). It is covered in §6.3. Everything else on "risky mechanics" is inference from cross-sectional torque.

### 1.3 Units convention

- Angles: degrees (°)
- Angular velocity: °/s
- Torque: N·m, and normalized as **%BW×BH** (percent of body weight × body height) — the ASMI convention that allows comparison across body sizes
- Force: N, and normalized as **%BW**
- Velocity: m/s and mph (1 m/s = 2.2369 mph)
- Time: ms

**Conversion worked example (why %BW×BH matters):** A professional at 94.7 kg (929 N) and 1.897 m with elbow varus torque of 5.1 %BW×BH produces:
`0.051 × 929 N × 1.897 m ≈ 90 N·m`
Same normalized value on a 79 kg, 1.83 m elite HS arm: `0.051 × 775 × 1.83 ≈ 72 N·m`. **Normalized torque is the mechanics; absolute torque is what the ligament feels.**

### 1.4 A note on terminology: varus torque vs. valgus load

The elbow experiences an external **valgus** load during arm cocking. The **varus torque** reported by labs is the internal (net muscle + ligament + bony) torque resisting it. They are the same magnitude, opposite sense. "Elbow varus torque," "elbow valgus torque," and "medial elbow load" are used near-interchangeably in the literature; I use **varus torque** for lab-computed inverse-dynamics values.

---

## 2. The Six Phases and Their Timing Landmarks

### 2.1 Phase definitions by landmark

The six-phase model is Fleisig's and is the field standard ([Fleisig et al., 1996/1999](https://www.sciencedirect.com/science/article/abs/pii/S002192909900127X); reviewed in [Diffendaffer et al., 2023, Sports Health](https://journals.sagepub.com/doi/abs/10.1177/19417381221078537)).

| # | Phase | Starts at | Ends at |
|---|---|---|---|
| 1 | **Wind-up** | Initiation of motion | Max lead-knee lift / hands separate |
| 2 | **Stride** (early cocking) | Hand separation | **Stride foot contact (FC)** |
| 3 | **Arm cocking** (late cocking) | Foot contact | **Max shoulder external rotation (MER)** |
| 4 | **Arm acceleration** | MER | **Ball release (BR)** |
| 5 | **Arm deceleration** | Ball release | **Max shoulder internal rotation (MIR)** |
| 6 | **Follow-through** | MIR | Balanced fielding position |

**The four hard landmarks a coach must be able to find on video: FC, MER, BR, MIR.** Every meaningful number in this document is indexed to one of them.

### 2.2 Durations

Reported durations vary by source and by how the wind-up is bounded. Values below are approximate and should be treated as **order-of-magnitude with real uncertainty**, not as precise norms — the literature is inconsistent here.

| Phase | Approx. duration | Notes |
|---|---|---|
| Wind-up | ~500–1000 ms | Highly individual; stretch delivery removes most of it |
| Stride | ~500–750 ms | Ends at FC |
| Arm cocking (FC→MER) | **~100–150 ms** | Where peak elbow varus torque occurs |
| Arm acceleration (MER→BR) | **~30–50 ms** | Fastest human joint motion recorded |
| Arm deceleration (BR→MIR) | **~30–50 ms** | Peak shoulder distraction force |
| Follow-through | ~300–1000 ms | |

**On arm acceleration duration:** the classic ASMI figure is **~0.03 s (30 ms)**. A review source gives **42–58 ms** ([summarized in general biomechanics reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC8811517/)). The discrepancy likely reflects different MER detection thresholds and sampling rates. **I would report "roughly 30–50 ms" and flag the wider figures as method-dependent.** *Do not treat any single millisecond figure as settled.*

**Total FC→BR is on the order of 130–200 ms.** This is the entire window in which velocity is produced and in which nearly all elbow and shoulder load is generated.

### 2.3 What happens in each phase — mechanically

**Wind-up.** Essentially zero joint load. Its only biomechanical function is to establish posture, direction, and the timing of the pelvis. Nothing in the literature associates wind-up variables with velocity in elite pitchers. Notably, Fleisig et al. (2024) found **professionals produce statistically similar ball velocity and kinematics from the wind-up and the stretch** ([AJSM](https://journals.sagepub.com/doi/10.1177/03635465241247543)) — the "you lose velo from the stretch" claim is, at the professional level, **not supported**.

**Stride.** Linear momentum is built by the back leg; the pelvis begins to rotate late in the stride; the arm gets into the cocked position. This is where the *setup* for everything downstream is fixed: stride length, foot placement, foot angle, trunk orientation, shoulder abduction, and elbow flexion at FC are all determined here. **Because the arm-cocking and acceleration phases are only ~30–150 ms long, they are effectively uncoachable in real time. The stride is the last phase where the athlete has time to organize anything.** (This is the mechanistic reason behind the widely repeated coaching heuristic that "it's easier to fix things before foot strike" — the heuristic is right, and the reason is the phase durations.)

**Arm cocking (FC→MER).** The pelvis and trunk decelerate; the arm lays back into 165–180° of apparent external rotation. **Peak elbow varus torque and peak shoulder internal-rotation torque both occur here, near MER.** This is the injury-generating phase for the UCL and the anterior shoulder.

**Arm acceleration (MER→BR).** Shoulder internal rotation velocity peaks (~6,000–7,500 °/s in elite arms) and elbow extension velocity peaks (~2,200–2,500 °/s). The trunk tilts forward and laterally. Ball release.

**Arm deceleration (BR→MIR).** The largest **forces** (not torques) of the delivery: shoulder distraction/proximal force peaks here or just after BR. Posterior cuff, posterior deltoid, teres major/minor, and lat contract eccentrically against a distraction load approaching or exceeding body weight.

**Follow-through.** Residual energy is dissipated through trunk flexion and lead-leg/trail-leg action. Poor follow-through is a *symptom* of poor deceleration capacity, not usually an independent problem.

---

## 3. Kinematics in the Elite Band

### 3.1 Reference table — professional pitchers (ASMI database)

Source: Escamilla, Fleisig et al. (2023), n = **288 professional** pitchers, age 21.9 ± 2.1 yr, height 189.7 ± 5.8 cm, mass 94.7 ± 9.6 kg, lab FB velocity 38.1 ± 4.1 m/s (85.2 mph lab). Values shown are for the **overhand (AS1, n=80)** and **sidearm (AS3, n=66)** arm-slot subgroups; the three-quarter group (AS2, n=142) sits between them. ([PMC10601404](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/))

#### At stride foot contact (FC)

| Parameter | Pro overhand | Pro sidearm | Unit |
|---|---|---|---|
| Stride length | 76 ± 9 | 75 ± 5 | % height |
| Lead knee flexion | 49 ± 7 | 44 ± 9 | ° |
| Shoulder abduction | 85 ± 12 | 82 ± 10 | ° |
| Elbow flexion | 101 ± 15 | 93 ± 19 | ° |
| Trunk flexion | −3 ± 11 | −17 ± 14 | ° |

#### At maximum external rotation (MER)

| Parameter | Pro overhand | Pro sidearm | Unit |
|---|---|---|---|
| **Max shoulder external rotation** | **165 ± 9** | **168 ± 10** | ° |
| Max elbow flexion | 90 ± 11 | 89 ± 9 | ° |
| Shoulder horizontal adduction | 7 ± 9 | 11 ± 7 | ° |

#### At ball release (BR)

| Parameter | Pro overhand | Pro sidearm | Unit |
|---|---|---|---|
| Arm slot | 44 ± 7 | 75 ± 15 | ° |
| Shoulder abduction | 95 ± 7 | 84 ± 9 | ° |
| **Trunk lateral flexion** | **34 ± 8** | **24 ± 11** | ° |
| Trunk flexion | 7 ± 11 | 15 ± 12 | ° |
| Elbow flexion | 30 ± 6 | 35 ± 6 | ° |

#### Peak angular velocities

| Parameter | Pro overhand | Pro sidearm | Unit |
|---|---|---|---|
| Max pelvis angular velocity | 622 ± 83 | 717 ± 92 | °/s |
| Max upper trunk angular velocity | 742 ± 221 | 711 ± 228 | °/s |
| Time of max upper trunk velocity | 56.5 ± 7.1 | 63.9 ± 7.4 | % pitch time |
| Max elbow extension velocity | 2403 ± 269 | 2191 ± 289 | °/s |
| **Max shoulder internal rotation velocity** | **6149 ± 1153** | **5456 ± 990** | °/s |

**Key reading:** Shoulder IR velocity in an elite arm is **~5,500–7,500 °/s** — the fastest recorded human joint rotation. Elbow extension ~2,200–2,500 °/s. Pelvis ~600–750 °/s, trunk ~700–1,200 °/s.

### 3.2 Wider elite ranges (cross-study)

Composite ranges from the clinician's-guide literature ([Diffendaffer et al., 2023](https://journals.sagepub.com/doi/abs/10.1177/19417381221078537); [Chalmers/clinician guide, PMC6542879](https://pmc.ncbi.nlm.nih.gov/articles/PMC6542879/)). These pool multiple competitive levels; **use them as bounds, not targets**:

| Parameter | Range | Landmark |
|---|---|---|
| Stride length | 77–90 (some report 85–100) | % height, at FC |
| Foot angle (closed) | 14–21.6 | °, at FC |
| Shoulder abduction | 78–95 | °, at FC |
| Elbow flexion | 74–101 | °, at FC |
| Lead knee flexion | 40–49 | °, at FC |
| Pelvis rotation velocity | 590–1202 | °/s |
| Max shoulder ER | 166–182 | °, at MER |
| Shoulder ER at release | 109–143 | ° |
| Elbow flexion at release | 24–39 | ° |
| Forward trunk tilt | 30–55 | °, at BR |
| Lateral trunk tilt | 21–35 | °, at BR |
| Lead knee flexion at BR | 31–41 | ° |
| Shoulder IR velocity | up to ~7,500 | °/s |
| Elbow extension velocity | 1742–2500 | °/s |

**Note on "max shoulder external rotation."** The 165–180° figure is **not** pure glenohumeral rotation. It is an apparent angle that includes scapulothoracic motion, trunk hyperextension, and elbow/forearm contributions. True GH external rotation is substantially less. **Never coach a pitcher toward a target MER number**; it is a composite output, and Fleisig's own regression found *higher* MER associated with *lower* normalized elbow varus torque (§6.2) while other work finds MER a positive velocity predictor — a direct conflict discussed in §6.

### 3.3 Hip–shoulder separation

- **At foot contact: ~50 ± 12°** in the pooled literature; commonly cited functional band **35–60°** at peak, and this is **strongly torso-length dependent** ([Role of Pelvis and Trunk Biomechanics in Generating Ball Velocity, 2022, PubMed 35836313](https://pubmed.ncbi.nlm.nih.gov/35836313/)).
- Hip–shoulder separation at FC individually predicted **17%** of variance in peak trunk rotation velocity (p = .027). Combined with peak pelvis velocity (23%, p = .008) and timing of peak trunk velocity, the model explained **55%** of trunk-rotation-velocity variance.
- **Interpretation:** separation is a *contributor to trunk speed*, and trunk speed is a contributor to ball speed. It is **two steps removed from velocity**, and it explains under a fifth of trunk velocity on its own. It is real but frequently over-weighted in coaching. There is no evidence supporting a specific separation target.

### 3.4 Release point

The literature treats release point as largely a **consequence** of arm slot, trunk lateral tilt, stride length, and height — not as an independent trainable variable. Arm slot in professionals: overhand 43.7 ± 6.5°, three-quarter 57.9 ± 4.1°, sidearm 75.0 ± 14.6° ([Escamilla et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/)). Professionals sit at a **more sidearm/lower slot on average (58 ± 14°) than high schoolers (50 ± 11°)** — the opposite of the common coaching assumption that professionals get "on top of the ball" more.

### 3.5 What separates 95 from 87 *inside* the elite band

This is the question the coach actually cares about, and the honest answer is that **the literature is thin here** — most studies compare across levels, not within them. What exists:

From the professional-only velocity model (n = 337 pro pitchers, 3,627 fastballs, adjusted **R² = 0.536**) ([PMC11322935](https://pmc.ncbi.nlm.nih.gov/articles/PMC11322935/)):

| Predictor of pitch velocity in PROFESSIONALS | β | p |
|---|---|---|
| **Trunk flexion at ball release** | **1.829** | <.001 |
| Peak shoulder internal rotation velocity | 0.381 | <.001 |
| **Stride length** | **0.334** | <.001 |
| **Max shoulder external rotation** | 0.333 | <.001 |
| Leg length (anthropometric — not trainable) | 0.292 | <.001 |
| Trunk rotation at foot contact | 0.289 | .005 |
| Elbow extension velocity | 0.176 | .006 |

Effect sizes given: **+10° trunk flexion at release ≈ +3.71 m/s (+8.3 mph)**; **+12.7 cm leg length ≈ +1.74 m/s (+3.9 mph)**.

**Caution on the trunk-flexion coefficient.** A β of 1.829 and an implied +8.3 mph per 10° of forward trunk tilt is an enormous effect and almost certainly **not causal at that magnitude**. Forward trunk tilt at release is partly a *downstream consequence* of a well-executed lead-leg block and a fast trunk — the pitchers who get out over the front leg are the ones who already produced the momentum to do so. Telling an 87 mph arm to "get more forward tilt" will not add 8 mph. Treat this as a **marker of a good delivery, not a lever**.

From Driveline's lead-leg block analysis (**800+ force-plate sessions**, HS/college/pro, arms up to 100 mph) ([Driveline, 2022](https://www.drivelinebaseball.com/2022/10/a-quantitative-analysis-of-the-lead-leg-block-and-its-contributions-to-velocity/)):

| Variable | r with velo (raw) | r with velo (bodyweight-controlled) |
|---|---|---|
| Lead-leg vertical (Z) GRF | 0.44 | **0.23** |
| Lead-leg anterior-posterior (X) GRF | 0.38 | **0.19** |
| Lead-leg lateral (Y) GRF | 0.19 | 0.10 |
| Max resultant lead-leg force | — | 0.25 |
| Knee extension FP→BR | 0.29 | — |
| Max front-knee extension angular velocity | 0.25 (inter-subject) | 0.20 (intra-subject) |
| COG deceleration | 0.20 | — |
| **Pelvis rotation change FP→BR** | **−0.07** | 0.10 |
| **Pelvis rotational velocity gain** | **−0.07** | −0.01 |

**Two findings that should change coaching:**
1. **Roughly half the raw lead-leg-force/velocity correlation is bodyweight.** Big guys push big numbers and throw hard. Once you control for mass, r drops from 0.44 → 0.23. That's ~5% of variance. The block is real but modest.
2. **The block does NOT work by driving more pelvis rotation.** Pelvis rotation change and pelvis rotational velocity gain after foot plant were **essentially zero-to-negative** correlates of velocity (r = −0.07). The widespread coaching model "block → pelvis whips → velo" is **not supported by this dataset.** The block appears to work by **decelerating the center of mass** (COG deceleration r = 0.20) and by **lead-knee extension** (r = 0.25–0.29), i.e., by converting linear momentum upward/rearward, not by adding pelvis spin.

**`[UNSOURCED COACHING CLAIM]`** — "You need X° of hip-shoulder separation," "get on top of the ball," "throw downhill," "the block whips the hips," and any specific stride-length prescription in inches. None of these have supporting elite-population evidence at the specificity at which they are coached.

---

## 4. Kinetics: Torque, Force, and Ground Reaction

### 4.1 Elbow varus torque — elite values

**Absolute (professional, in-lab):**

| Source | Population | Elbow varus torque |
|---|---|---|
| Fleisig et al., 2025 (OJSM prospective) | 305 MiLB, uninjured subgroup | **94.3 ± 16.1 N·m** |
| Fleisig et al., 2025 (OJSM prospective) | 305 MiLB, later-UCL-surgery subgroup | **100.8 ± 18.1 N·m** |
| Fleisig et al., 2025 (kinematic-parameters study) | 523 pitchers (425 pro, 98 D1) | "near 100 N·m" |
| Older ASMI reporting | professional | ~64 N·m (range 52–76); ~120 N·m at MER in some reports |

**The spread across sources (64 → 120 N·m) is a serious issue.** It reflects differences in marker sets, filtering cutoffs, inertial models, and the definition of the joint center. **Do not compare a torque number from one lab to a number from another lab.** Within a system, the numbers are usable; across systems they are not.

**Normalized (%BW×BH)** — from the ASMI arm-slot cohort ([Escamilla et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/)):

| | HS `[OFF-POPULATION — 70 mph mean]` | Professional |
|---|---|---|
| Elbow varus torque | 3.8–4.0 %BW×BH | **4.8–5.1 %BW×BH** |
| Shoulder internal rotation torque | 4.0–4.1 %BW×BH | **4.9–5.2 %BW×BH** |
| Shoulder horizontal adduction torque | 4.6–4.7 %BW×BH | **5.6 %BW×BH** |
| Elbow flexion torque | 2.7–3.2 %BW×BH | 3.8–4.1 %BW×BH |

And from the high-vs-low-torque split (n = 523, 425 pro + 98 D1) ([Fleisig et al., 2025 OJSM](https://pmc.ncbi.nlm.nih.gov/articles/PMC11789100/)):
- High-torque group: **0.0637 ± 0.006** (i.e., 6.37 %BW×BH)
- Low-torque group: **0.0461 ± 0.004** (4.61 %BW×BH)
- **28% difference in normalized torque for only a 1% difference in ball velocity** (38.0 vs 37.1 m/s).

**This is the central fact of this entire report.** Within elite pitchers, there exist arms producing essentially the same ball velocity at **28% less elbow load**. Efficiency is real, it is large, and it is measurable.

### 4.2 Shoulder internal rotation torque

- Professional: **4.9–5.2 %BW×BH** ≈ 87–92 N·m for a 94.7 kg / 1.897 m athlete.
- Shoulder IR torque is the **strongest single correlate of elbow valgus torque**, accounting for **~85% of its variance** once subject weight and height are controlled ([Werner et al. / correlation-of-throwing-mechanics literature](https://www.academia.edu/16801750/Correlation_of_Throwing_Mechanics_With_Elbow_Valgus_Load_in_Adult_Baseball_Pitchers)).
- **Practical meaning:** the elbow and shoulder are not independently loaded. You cannot meaningfully reduce elbow varus torque without addressing what is driving shoulder IR torque. Sleeve-based "elbow stress" management that ignores the shoulder is treating a symptom.
- Arm slot: in **professionals**, every +10° of arm slot (i.e., moving lower/more sidearm) was associated with **−0.1 %BW×BH** in *both* elbow varus torque (β = −0.22, p < .001) and shoulder IR torque (β = −0.20, p < .001). In high schoolers the relationship ran the other way for elbow flexion torque (β = +0.28, p = .002). **Arm-slot effects are level-dependent — another reason not to import HS findings into an elite model.**

### 4.3 Shoulder distraction / proximal force

| Population | Shoulder proximal (distraction) force |
|---|---|
| Professional (ASMI) | **113.9–114.2 %BW** |
| HS `[OFF-POPULATION]` | 81.6–88.8 %BW |
| Pooled literature range | 90–108 %BW |
| Youth `[OFF-POPULATION]` | 214.7 ± 47.2 N (49.8 ± 8.3 %BW) |

Elbow proximal force in professionals: **112.1–112.4 %BW**. Shoulder anterior force: **42.1–42.4 %BW**.

**For a 95 kg (932 N) professional: shoulder distraction ≈ 1,060 N — roughly 1.14× body weight, pulling the humeral head out of the glenoid, in a ~30–50 ms window, ~100 times per outing.** Compressive joint loads during deceleration exceed **1,000 N**.

**Interpretation:** the deceleration phase is a **force** problem, not a torque problem, and it is the least-trained phase in most programs. The posterior cuff and scapular stabilizers are the tissue at risk. This is a direct handoff to the anatomy agent (§9).

### 4.4 The UCL failure-load question — the most important number for this coach

This is where the coach's question lands, and it requires care.

**Published cadaveric UCL failure loads:**

| Source type | Failure torque |
|---|---|
| Dillman et al. (classic, most-cited) | **~32 N·m** |
| Cadavers, mean age 43 (younger) | **34 N·m** |
| Elderly cadaver studies | 17.1–22.7 N·m |

**Morrey & An:** the UCL provides approximately **54% of the varus restraint** needed to resist a valgus load at 90° of elbow flexion.

**The naive arithmetic:** a professional at ~95–100 N·m of elbow varus torque × 54% = **51–54 N·m through the UCL** — 1.6× the ~32 N·m cadaveric failure load. Even using the more conservative torque estimates (64 N·m peak), 54% = ~35 N·m — still at or above failure. This is the widely repeated claim that "every pitch should tear the UCL."

**Why the ligament does not, in fact, fail on every pitch — and what the gap actually means:**

1. **The 54% figure is a static, cadaveric, isolated-ligament number.** In vivo, the flexor-pronator mass (FCU, FDS, pronator teres) actively contributes to valgus restraint. Dynamic muscular contribution is not captured in cadaveric testing and is not captured in inverse-dynamics net-torque calculations either.
2. **Inverse dynamics computes a NET joint torque, not ligament load.** The lab number is the *sum* of all internal contributions — ligament, muscle, bone contact, capsule. Attributing 54% of it to the UCL is an approximation layered on an approximation.
3. **Cadaveric tissue is not living tissue.** Failure loads from elderly specimens (17–23 N·m) are clearly not representative of a 22-year-old professional's ligament, which has adapted to chronic loading. The 34 N·m figure from mean-age-43 cadavers is the closer analogue and is still not our population.
4. **Therefore: the "torque exceeds failure load" comparison is directionally informative but numerically unreliable.** It should not be used to compute a per-pitch failure probability.

**What it DOES mean, and what a coach should take from it:**

- The UCL operates with **little or no safety margin**. The gap between operating load and failure load is small enough that it is bridged by active muscular contribution and by tissue adaptation. **Anything that degrades either — fatigue, deconditioning of the flexor-pronator mass, a partially degenerated ligament — moves the arm from "adequate" to "insufficient."**
- **This is the mechanistic explanation for why fatigue is the dominant modifiable injury risk factor in the epidemiology.** It is not that tired mechanics generate more torque (evidence there is mixed); it is that a tired flexor-pronator mass stops sharing the load, and the ligament's share of a constant net torque rises.
- **Prospectively confirmed:** in 305 professional pitchers followed ~4.5 years, elbow varus torque **was** significantly higher in those who later required UCL surgery (100.8 ± 18.1 vs 94.3 ± 16.1 N·m, p = .049), with **HR 1.26 per 10 N·m increase (95% CI 1.01–1.56)** ([Fleisig et al., 2025 OJSM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227930/)). This is real prospective evidence that torque predicts UCL surgery. **But note the CI lower bound of 1.01 — this is a barely-significant finding, and the distributions overlap heavily.** A 6.5 N·m group difference against SDs of 16–18 N·m means torque is a **weak individual-level predictor** even though it is a real population-level risk factor.

### 4.5 How torque scales with velocity: 85 → 95 → 100

**Between pitchers: weakly.** R² = 0.076 (Slowik et al., 2019, 64 professionals). Two pros at 88 and 96 mph may have similar elbow torque.

**Within a pitcher: almost deterministically.** R² = 0.957 (same study). When *you* throw harder, *your* elbow torque goes up, nearly linearly.

**And critically — in the prospective cohort, fastball velocity itself did NOT differ between the UCL-surgery group (85.0 ± 3.0 mph) and the healthy group (84.7 ± 3.6 mph), p = .604.** Torque predicted injury; velocity did not.

**Synthesis for the coach — state this plainly:**

> Velocity is not the risk factor. **Torque is.** And within a given athlete, velocity and torque are locked together — you cannot add 5 mph to *this* arm without adding load to *this* elbow. But **across** athletes, the velocity-to-torque exchange rate varies enormously — some arms buy 95 mph at 4.6 %BW×BH and others buy 92 at 6.4. **The coachable target is not "throw harder with less stress." It is "become the kind of arm that converts effort into velocity efficiently, then apply effort."** This is exactly what Crotin et al. (2022) formalized as **biomechanical efficiency = fastball velocity per unit of normalized elbow varus torque** (n = 545: 447 professional, 98 collegiate) ([AJSM 50(12):3374–3380](https://journals.sagepub.com/doi/abs/10.1177/03635465221119194)).

### 4.6 Ground reaction forces

**Note on population:** the strongest GRF/energy-flow work (Howenstein et al., 2020) is in **youth** `[OFF-POPULATION — directionally suggestive only]`. The elite-relevant sources are Driveline's 800+ session force-plate dataset, Guido & Werner (collegiate), McNally et al. (2015, adult), and the professional impulse study below.

**Functional division of labor** ([Howenstein et al., 2020, J Biomech](https://pubmed.ncbi.nlm.nih.gov/32635991/) `[OFF-POPULATION]`; [Sports Biomechanics 2022, professional](https://www.tandfonline.com/doi/full/10.1080/14763141.2022.2108490)):

- **Back/drive leg — propulsive GRF and impulse:** correlates with energy flow into the **proximal** segments (pelvis, trunk), via the **joint force** component of energy transfer. It builds linear momentum and, per the professional impulse study, contributes to **whole-body rotation**.
- **Lead/stride leg — braking GRF and impulse:** correlates with energy flow into the **distal** segments (arm), via the **joint moment/power** component. It converts linear momentum into rotational and then distal energy.

**Elite magnitudes and correlations:**
- Guido & Werner (collegiate): higher-velocity pitchers showed **higher lead-leg braking GRF**.
- McNally et al. (2015, adult): significant relationship between **stride-leg peak propulsive and vertical GRF** and ball velocity.
- Driveline (800+ sessions, HS→pro): lead-leg vertical GRF r = 0.44 raw / **0.23 bodyweight-controlled**; A-P GRF r = 0.38 / **0.19**.

**Honest magnitude assessment:** after controlling for body mass, **lead-leg GRF explains roughly 4–6% of velocity variance between pitchers.** It is not the master variable it is often presented as. It matters more as an *intra-individual* target (does this athlete brake better than he did?) than as a between-athlete predictor.

**Braking impulse** (force × time) is the more mechanically meaningful quantity than peak force, since it is the actual change in momentum, and it is what correlates with energy flow into the arm. Elite-population impulse norms in %BW·s are **not well published**; this is a genuine gap.

---

## 5. The Kinematic Sequence

### 5.1 The proximal-to-distal principle

The intended order of **peak angular velocity** is:

**Pelvis → upper trunk → upper arm → forearm → hand** (conventionally coded **1-2-3-4-5**)

Each segment should peak **later and faster** than the one proximal to it. Mechanically this is a summation-of-speed / whip mechanism: the proximal segment accelerates the distal one, then decelerates, transferring angular momentum distally.

**Approximate elite peak magnitudes and order:**

| Segment | Peak angular velocity | Timing |
|---|---|---|
| Pelvis | 600–750 °/s (up to ~1200 reported) | earliest; shortly after FC |
| Upper trunk | 700–1200 °/s | ~53–64% of pitch time |
| Elbow extension | 2200–2500 °/s | arm acceleration |
| Shoulder internal rotation | 5500–7500 °/s | near/just before BR |

### 5.2 The uncomfortable finding: the "ideal" sequence is essentially never observed

A study of 14 pitchers (4 HS, 8 collegiate, 2 professional; 60 fastballs, 71 curveballs) found:

- The textbook **1-2-3-4-5 sequence was NEVER achieved** on any pitch.
- The closest observed pattern was **1-2-3-4-4** (forearm and hand peaking simultaneously).
- **8 distinct sequences** were observed on fastballs; **11** on curveballs.
- **43% of fastballs** showed altered *distal* upper-extremity sequencing.
- Each pitcher averaged **2.7 different sequences across 5–6 throws** — **no pitcher used only one sequence.**
- No significant difference in sequence variability between fastball and curveball (p = 0.67).

([Frontiers in Sports and Active Living, 2021](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2021.699251/full))

**Implications — and this is a big deal for coaching practice:**

1. **"Fixing the kinematic sequence" as a discrete, binary intervention is not well founded.** Healthy, competent pitchers throw 2–3 different sequences within a single bullpen. Sequence is not a stable trait you either have or don't.
2. **The proximal end (pelvis→trunk) is far more consistent than the distal end.** Nearly all observed disorder was in the arm/forearm/hand ordering. **The proximal-to-distal principle is well supported for the lower half and trunk; it is much shakier distally.**
3. **Sample caveat:** n = 14, mixed levels, small. This finding needs replication in a large professional sample. Treat it as an important warning against over-confidence, not as settled.

### 5.3 What a broken sequence costs

The best-supported specific failure mode is **trunk-before-pelvis**:

- **Torques increase when the trunk reaches peak rotational velocity BEFORE the pelvis does** (Aguinaldo & Escamilla, 2019). This is the "flying open" / "trunk rotating early" pattern.
- Oyama et al. found that pitchers with the **proper** pelvis-then-trunk sequencing had **decreased shoulder proximal force AND decreased shoulder external rotation angle** vs. improper sequencing. `[Sample: high school — flag as directionally suggestive for our population.]`
- Fleisig's high-vs-low-torque analysis found **percent time of maximum pelvic rotation velocity** was a (negative) contributor to the normalized-torque regression — i.e., **later pelvis peak associated with lower normalized elbow torque** — though this was the one parameter of eleven that did *not* differentiate the high- and low-torque groups on univariate testing.

**What a well-sequenced 95 mph delivery looks like vs. an 85 mph arm-dominant one:**

| | Efficient 95 | Arm-dominant 87 |
|---|---|---|
| Pelvis peak | Early, clearly before trunk | Late, or simultaneous with trunk |
| Trunk peak | ~55–60% of pitch time, distinctly after pelvis | Before or with pelvis ("flying open") |
| Peak magnitudes | High and *ordered* | Trunk may be fast but out of order |
| Shoulder IR velocity | 6,000–7,500 °/s | Can also be high — **this is why the arm-dominant pitcher still throws 87** |
| Normalized elbow torque | ~4.6 %BW×BH | ~6.4 %BW×BH |
| Lead-leg block | Strong COG deceleration, knee extending FP→BR | Knee continues flexing or collapses; poor braking |

**The core insight:** the arm-dominant pitcher is not slow. He is **expensive**. He is buying nearly the same velocity at ~28% more elbow load. The efficient pitcher's advantage shows up in the *denominator*, not the numerator.

### 5.4 Energy flow

Energy-flow (segment power) analysis decomposes transfer into:
- **Joint force power** — energy moved by the net joint force (translation)
- **Joint moment power** — energy moved by the net joint moment (rotation/muscle work)

Findings ([Howenstein et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32635991/) `[OFF-POPULATION: youth]`):
- Drive-leg peak GRF and both legs' GRF impulse → **joint force and power components of energy flow into pelvis and trunk**
- Stride-leg peak GRF and impulse → **joint moment and power components of energy flow into the arm**

This is the cleanest mechanistic account of why both legs matter and why they matter *differently*: **the back leg feeds the middle, the front leg feeds the arm.** It needs replication in an elite sample.

---

## 6. Velocity Determinants vs. Injury Risk — Where They Conflict

### 6.1 What predicts velocity in professionals

(n = 337 pro, 3,627 fastballs, adj. R² = 0.536 — see §3.5 table.) Positive predictors: trunk flexion at BR, peak shoulder IR velocity, stride length, max shoulder ER, leg length, trunk rotation at FC, elbow extension velocity.

### 6.2 What predicts elbow varus torque in elite pitchers

(n = 523: 425 pro, 98 D1; 11 kinematic parameters explained **40%** of variance in normalized torque) ([Fleisig et al., 2025 OJSM](https://pmc.ncbi.nlm.nih.gov/articles/PMC11789100/)):

**↑ Torque (positive contributors):**
- Ball velocity (strongest)
- Shoulder abduction at foot contact
- Elbow flexion at foot contact
- Max knee extension velocity during arm acceleration
- Max elbow extension velocity during arm acceleration
- Trunk contralateral (lateral) tilt at ball release

**↓ Torque (negative contributors):**
- Max shoulder external rotation
- Upper trunk tilt at foot contact
- Shoulder abduction at ball release
- Shoulder external rotation at foot contact
- Percent time of max pelvic rotation velocity (later = lower torque)

### 6.3 The conflict table

| Variable | Effect on VELOCITY | Effect on ELBOW TORQUE | Verdict |
|---|---|---|---|
| **Max shoulder ER** | ↑ velocity (β = 0.333) | **↓ normalized torque** | **Rare win-win.** But see caveat below. |
| **Elbow extension velocity** | ↑ velocity (β = 0.176) | **↑ torque** | **Direct conflict.** |
| **Max knee extension velocity** | ↑ velocity (Driveline r ≈ 0.25) | **↑ torque** | **Direct conflict.** The block costs. |
| **Trunk lateral tilt at BR** | ↑ velocity (part of the "get out over it" complex) | **↑ torque** | **Direct conflict.** |
| **Stride length** | ↑ velocity (β = 0.334) | Not a significant torque contributor | **Favorable.** |
| **Later pelvis peak (proper sequence)** | Enables trunk velocity | **↓ torque** | **Win-win.** Best available lever. |
| **Shoulder abduction at FC** | Not a velocity predictor | **↑ torque** | **Free reduction available.** |
| **Elbow flexion at FC** | Not a velocity predictor | **↑ torque** | **Free reduction available.** |
| **Shoulder abduction at BR** | Not a velocity predictor | **↓ torque** | **Free reduction available.** |
| **Lower arm slot (pro)** | Neutral | ↓ elbow varus AND ↓ shoulder IR torque | **Favorable in professionals only.** |
| **Ball velocity itself** | — | ↑↑ torque within-athlete (R² = .957) | **Unavoidable price.** |

**Caveat on max shoulder ER:** the finding that higher MER associates with *lower* normalized torque is counterintuitive and I would not act on it aggressively. MER is a composite angle (§3.2), and pitchers who achieve high apparent MER may be distributing lay-back across the thoracic spine and scapula rather than loading the anterior GH capsule and the UCL. That is a *hypothesis*. It is also possible this is a statistical artifact of the multivariate model. **Do not coach "more layback."**

### 6.4 The four "free" reductions — the practically actionable finding

Four variables **raise elbow torque without raising velocity**, per the two regressions above. These are the closest thing this literature offers to free lunch:

1. **Reduce shoulder abduction at foot contact** (pro norm 82–85°; higher = more torque, no velo benefit)
2. **Reduce elbow flexion at foot contact** (pro norm 93–101°; higher = more torque, no velo benefit)
3. **Increase shoulder abduction at ball release** (pro norm 84–95°; higher = less torque)
4. **Get the pelvis peak to occur later relative to the trunk** (proper sequencing)

**Caveats, stated firmly:** these are cross-sectional multivariate associations, not intervention trials. **No study has shown that changing these variables in an individual reduces his torque or his injury rate.** They are the best-supported hypotheses available, not proven interventions. They also come from a model explaining only 40% of torque variance — **60% is unexplained**, and much of that is likely anthropometry, tissue quality, and factors not visible in kinematics.

### 6.5 Fatigue

Not directly covered by the studies above, but the §4.4 mechanism makes fatigue the highest-leverage variable in the system: **net joint torque may be roughly preserved under fatigue while the ligament's share of it rises**, as the flexor-pronator mass loses its load-sharing contribution. This is a mechanistic argument, and I am labeling it as such — it is **inference, not a directly measured finding.** It should be a priority research target for this program.

---

## 7. Measurement Technology

### 7.1 Marker-based optical motion capture (the reference standard)

- **Systems:** Vicon, Motion Analysis, Qualisys. ASMI uses a 12-camera automated system at **240 Hz**.
- **What it gives:** full 3D kinematics + inverse-dynamics kinetics (the torque and force numbers in §4).
- **Validity:** it is the reference standard, but it is not truth. Soft-tissue artifact at the shoulder is substantial; joint-center estimation, segment inertial models, and filter cutoff all materially change computed torque. **This is why torque values differ 64 vs. 100 vs. 120 N·m across sources (§4.1).**
- **Reliability:** high within a lab and a protocol.
- **Cost:** $100k–$500k+ installed, plus a biomechanist. Not accessible to a private coach.
- **Fatal limitation for our purposes:** **it cannot capture a game.** And pitchers throw slower in the lab than in games (Lerch et al., 2025), so lab kinetics likely **under**-represent competitive load.

### 7.2 Markerless motion capture

This is where elite programs have moved.

**KinaTrax** — the in-stadium standard. **8 synchronized cameras at 300 Hz.** Deployed in MLB parks and at collegiate stadiums; a published normative study covered **51 pitchers from 5 collegiate teams during the 2023 season**. Captures **in-game**, which no marker system can do.

**Hawk-Eye** — MLB's league-wide optical system; ~12 cameras up to 300 fps; primarily ball/pose tracking, now used for player biomechanics.

**Theia3D** — portable markerless from ordinary video.

**pitchAI** — single-camera markerless.

**Documented accuracy:**

| System | Study | Accuracy |
|---|---|---|
| Hawk-Eye | 18 collegiate pitchers vs. marker-based, J Sports Sci 2025 | **MPJPE 56.6 ± 9.4 mm** |
| Theia3D | same study | **MPJPE 52.0 ± 12.3 mm** |
| pitchAI (single camera) | 10 pitchers vs. marker-based, 2022 | Time-series **R² 0.69–0.98**; **RMSE 4.37° (trunk lateral tilt) to 20.78° (glove-arm shoulder ER)**; arm speed RMSE 3.62 m/s; stride length RMSE 5.75 %height |

**How to read this:** ~5 cm of joint-center error is fine for stride length and trunk tilt and **potentially serious for computed joint kinetics**, because inverse-dynamics torque is sensitive to joint-center location and to the second derivative of position. **Kinematics from markerless: good. Kinetics from markerless: treat with caution and never compare across systems.** Both systems in the J Sports Sci study "demonstrated measurable discrepancies across variables."

**One genuinely encouraging finding:** Lerch et al. (2025, J Biomech) compared 30 lab marker-based pitchers to 30 NCAA D1 pitchers captured in-game markerless and found **pitch-to-pitch variability was broadly similar** between settings; only 2 of 10 kinematic parameters showed significantly greater in-game variability. **In-game markerless is capturing real movement, not noise.**

### 7.3 IMU sleeves (Motus / PULSE) — and the "stress" problem

**This section matters because the sleeve is the one lab-adjacent tool a private coach can actually buy, and its headline number is widely misunderstood.**

The device reports a metric called **"Stress"** in N·m, plus arm speed, arm slot, and shoulder external rotation.

**Original vendor claim:** Stress was validated against peak elbow valgus torque with a **0.99 intraclass correlation** to ASMI's measurements.

**What independent research found:**

- Driveline/Boddy et al. (2019, PeerJ, [PMC6348088](https://pmc.ncbi.nlm.nih.gov/articles/PMC6348088/)): the sleeve's Stress metric was **41 N·m (38.7%) LOWER than lab-measured elbow torque**, and **42 N·m (39.3%) lower than shoulder torque**. But correlations to the lab metrics were **extremely strong**. Conclusion: *"some magnitudes differ substantially and therefore fall short in validity, [but] the link between the metrics is strong enough to indicate reliable casual use."*
- Camp et al. (2021, AJSM): independent comparison of wearable sensors against marker-based mocap ([AJSM](https://journals.sagepub.com/doi/abs/10.1177/03635465211029017)) — same overall picture: correlated, not equivalent.

**The correct interpretation, stated bluntly:**

> **Motus/PULSE "Stress" is NOT elbow varus torque.** It underestimates lab torque by roughly 39%. It is a **relative workload index**, and a good one. Use it to track a single athlete's load over time and to compare today's bullpen to last week's. **Never** compare a sleeve number to a published torque value, **never** compare it to the 32 N·m UCL failure figure, and **never** compare sleeve numbers between two different athletes as if they were the same physical quantity.

Additional caveat: sleeve output is sensitive to placement, fit, and skin motion. Standardize placement or the longitudinal tracking — its one real strength — degrades.

### 7.4 Ball/pitch tracking

| System | Technology | Notes |
|---|---|---|
| **Trackman** | Doppler radar | Long-standing reference for velocity/spin |
| **Rapsodo** | Optical + radar hybrid | Driveline validation found **Rapsodo velocity significantly LOWER than Trackman**, spin slightly slower |
| **Hawk-Eye** | 12 optical cameras, up to 300 fps | Full 3D trajectory, spin axis, seam orientation |

**Practical rule: never mix systems in one dataset.** Radar and optical measure different things and produce systematically different values; movement and spin-direction differences between them should be *expected*, not treated as error. Pick one, and note that a "velocity gain" that coincides with a device change is not a velocity gain.

### 7.5 Force plates

The most underrated accessible technology for an elite program. Driveline's 800+ session dataset is force-plate based. Dual in-ground plates (drive leg + landing) give propulsive GRF, braking GRF, and impulse directly — **no inverse-dynamics assumptions, no marker error.** GRF is a *directly measured* quantity, which is exactly what torque is not. Cost is real but an order of magnitude below a full mocap lab.

### 7.6 What a coach without a lab can realistically measure

**Frame rate.** Ball release to max internal rotation is ~30–50 ms. At **30 fps**, one frame = 33 ms — you get **one frame, maybe zero**, in the entire acceleration phase. That is useless.

| Frame rate | ms per frame | Frames in the ~40 ms acceleration phase | Verdict |
|---|---|---|---|
| 30 fps | 33.3 | ~1 | Unusable for arm action |
| 60 fps | 16.7 | ~2 | Unusable for arm action |
| 120 fps | 8.3 | ~5 | Minimum viable |
| **240 fps** | **4.2** | **~10** | **Practical standard** |
| 300–1000 fps | 3.3–1.0 | 12–40 | Better; research-grade |

**Recommendation: 240 fps minimum for anything at or distal to the shoulder.** Modern phones do 240 fps at 1080p. Shutter speed matters as much as frame rate — you need **1/1000 s or faster** to avoid motion blur, which means a lot of light.

**Camera positions** (each answers different questions):

1. **Open side / third-base side for a RHP (perpendicular to the rubber-to-plate line), at hip height.** Best for: stride length, forward trunk tilt, lead-knee flexion/extension, arm slot, timing of FC/MER/BR.
2. **Closed side / first-base side for a RHP.** Best for: hip-shoulder separation, scapular loading, elbow position relative to trunk.
3. **Straight-on from behind or in front, centered.** Best for: lateral trunk tilt, foot placement relative to midline, foot angle, arm slot.
4. **Overhead** (if available). Best for: foot angle and stride direction.

**A single camera cannot measure a 3D angle.** Every 2D-video "measurement" of rotation is subject to perspective error. Be honest with the athlete about this.

**What is reliably measurable from 240 fps 2D video:**
- Stride length as % height (needs a calibrated reference in frame)
- Foot placement relative to midline, and foot angle
- Lead-knee flexion at FC and at BR, and whether it extends or collapses
- Forward and lateral trunk tilt at release (approximate; view-dependent)
- Timing landmarks (FC, MER, BR) and the intervals between them
- Whether the pelvis clearly leads the trunk (gross sequencing)

**What is NOT reliably measurable without 3D:**
- Max shoulder external rotation (composite angle, badly perspective-distorted)
- Hip-shoulder separation as a number (you can see gross early/late; you cannot get degrees)
- Any angular velocity
- **Any torque or force whatsoever**

**Realistic elite-program stack, cheapest to most capable:**
1. Radar (one system, consistently) + two 240 fps cameras — the floor
2. Add dual force plates — the highest value-per-dollar addition
3. Add a PULSE sleeve for longitudinal within-athlete workload (never as a torque number)
4. Portable markerless (Theia3D/pitchAI) for kinematics
5. Full markerless in-stadium (KinaTrax) — collegiate/professional programs only

---

## 8. Practical Synthesis for the Coach

**Ten statements I would defend from this literature, for an 85+ mph athlete:**

1. **Velocity does not cause injury; torque predicts it.** In 305 professionals followed 4.5 years, fastball velocity was identical between the UCL-surgery and healthy groups (85.0 vs 84.7 mph, p = .604); elbow varus torque differed (100.8 vs 94.3 N·m, HR 1.26 per 10 N·m).
2. **But within *your* athlete, velocity and torque are locked together** (R² = 0.957 within-subject). He cannot add velocity to his current delivery for free.
3. **The exchange rate between them varies ~28% across elite arms at the same velocity.** That gap is the entire coaching opportunity.
4. **The stride phase is the only phase long enough to coach.** Arm cocking is ~100–150 ms; acceleration is ~30–50 ms. Everything is decided by foot contact.
5. **Four variables raise elbow torque without adding velocity:** shoulder abduction at FC (too high), elbow flexion at FC (too high), shoulder abduction at BR (too low), and early pelvis peak. These are the least-costly targets — but they are cross-sectional associations, not proven interventions.
6. **The lead-leg block is real but smaller than advertised** — ~4–6% of between-pitcher velocity variance after controlling for bodyweight — and it does **not** work by increasing pelvis rotation (r = −0.07).
7. **The UCL runs with essentially no safety margin.** Peak varus torque (~95–100 N·m) × ~54% UCL share ≈ 51 N·m against cadaveric failure loads of ~32–34 N·m. The gap is bridged by active flexor-pronator load-sharing. **Fatigue removes the bridge.** (Mechanistic inference, not a directly measured finding.)
8. **The shoulder's problem is a force problem, in deceleration:** ~114% BW of distraction (~1,060 N for a 95 kg athlete) in a ~30–50 ms window, ~100×/outing. This is the least-trained phase in most programs.
9. **The elbow and shoulder are one system.** Shoulder IR torque explains ~85% of elbow valgus torque variance once size is controlled.
10. **Wind-up vs. stretch does not cost professionals velocity** — Fleisig et al. (2024) found similar velocity and kinematics from both.

**Three things I would stop saying:**
- "The block whips the hips." (Pelvis rotation gain after foot plant: r = −0.07 with velocity.)
- "Get on top of the ball." (Professionals throw from a *lower* average slot than high schoolers: 58 ± 14° vs 50 ± 11°; and in professionals, lower slot associates with *lower* elbow and shoulder torque.)
- "Fix your kinematic sequence." (No pitcher in the available study used a single sequence; each averaged 2.7 patterns across 5–6 throws; the textbook sequence was never observed.)

---

## 9. Open Questions / Research Gaps

**For the anatomy agent:**
1. **What is the actual in-vivo load-sharing between the UCL and the flexor-pronator mass (FCU, FDS, pronator teres) at valgus loads of 50+ N·m, and how does that share change with local muscular fatigue?** This is the linchpin of the entire injury model in §4.4 and I am currently reasoning from a static cadaveric 54% figure that almost certainly does not hold dynamically.
2. **What is the failure load of a chronically adapted 22-year-old professional's UCL?** All cadaveric data is from specimens aged 43+. If adaptation raises failure load meaningfully, the "every pitch exceeds failure" framing is wrong in a way that matters.
3. **What tissue actually absorbs the ~1,060 N shoulder distraction load in deceleration, in what proportions** (posterior cuff eccentric contraction vs. capsuloligamentous vs. bony/labral), and what is the trainable ceiling on the muscular contribution?

**For the coach:**
4. Which of the four "free" torque reductions (§6.4) is actually modifiable in an 85+ athlete without collateral velocity loss? Nobody has run this intervention trial.
5. What are elite braking-impulse norms in %BW·s? Peak GRF is published; impulse — the mechanically meaningful quantity — is not.
6. Does within-elite sequence timing (pelvis-to-trunk lag in ms) predict velocity or torque in a large professional sample? The n=14 sequence study is not adequate.

**Methodological gaps this program should track:**
- Torque values are not comparable across labs (64 vs. 100 vs. 120 N·m for the same population). Anchor to one system.
- Markerless kinetics validity against marker-based inverse dynamics is still being established (~50–57 mm MPJPE).
- Lab velocity underestimates game velocity, so all published kinetics likely underestimate competitive load.
- 60% of normalized elbow torque variance is unexplained by kinematics.

---

## 10. References

**Core kinematics / kinetics — elite populations**

- Escamilla RF, Fleisig GS, et al. (2023). *Kinematic and Kinetic Comparisons of Arm Slot Position Between High School and Professional Pitchers.* n = 130 HS, 288 professional. [PMC10601404](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601404/) — **primary source for the professional norms table.**
- Fleisig GS, Barrentine SW, Zheng N, Escamilla RF, Andrews JR (1999). *Kinematic and kinetic comparison of baseball pitching among various levels of development.* Journal of Biomechanics. n = 23 youth, 33 HS, 115 college, 60 pro. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S002192909900127X)
- Diffendaffer AZ, Bagwell MS, Fleisig GS, Yanagita Y, Stewart M, Cain EL, Dugas JR, Wilk KE (2023). *The Clinician's Guide to Baseball Pitching Biomechanics.* Sports Health. [SAGE](https://journals.sagepub.com/doi/abs/10.1177/19417381221078537)
- (2024). *Kinematic Modeling of Pitch Velocity in High School and Professional Baseball Pitchers.* n = 337 pro / 3,627 fastballs; adj. R² = 0.536. [PMC11322935](https://pmc.ncbi.nlm.nih.gov/articles/PMC11322935/)
- Fleisig GS, Slowik JS, Kutz CB, Escamilla RF (2024). *Comparison of Windup and Stretch Pitching Biomechanics in Baseball.* AJSM. [SAGE](https://journals.sagepub.com/doi/10.1177/03635465241247543)
- *A Clinician's Guide to Analysis of the Pitching Motion.* [PMC6542879](https://pmc.ncbi.nlm.nih.gov/articles/PMC6542879/)

**Elbow torque, velocity, and injury**

- Slowik JS, Aune KT, Diffendaffer AZ, Cain EL, Dugas JR, Fleisig GS (2019). *Fastball Velocity and Elbow-Varus Torque in Professional Baseball Pitchers.* J Athl Train 54(3):296–301. n = 64 pro. Between-subject R² = 0.076; within-subject R² = 0.957. [PubMed 30721094](https://pubmed.ncbi.nlm.nih.gov/30721094/)
- Fleisig GS, et al. (2025). *Risk Factors for an Ulnar Collateral Ligament Injury Resulting in Surgery: A Prospective Longitudinal Study of 305 Professional Baseball Pitchers.* OJSM. [PMC12227930](https://pmc.ncbi.nlm.nih.gov/articles/PMC12227930/) | [ASMI PDF](https://asmi.org/wp-content/uploads/Risk-factors-for-UCL-surgery-Fleisig-OJSM-2025.pdf) — **the only strong prospective study.**
- Fleisig GS, et al. (2025). *Kinematic Parameters Associated With Elbow Varus Torque in Elite Adult Baseball Pitchers.* n = 523 (425 pro, 98 D1); 11 parameters, 40% of variance. [PMC11789100](https://pmc.ncbi.nlm.nih.gov/articles/PMC11789100/) | [PubMed 39906602](https://pubmed.ncbi.nlm.nih.gov/39906602/)
- Crotin RL, Slowik JS, Brewer G, Cain EL, Fleisig GS (2022). *Determinants of Biomechanical Efficiency in Collegiate and Professional Baseball Pitchers.* AJSM 50(12):3374–3380. n = 545 (447 pro, 98 collegiate). [SAGE](https://journals.sagepub.com/doi/abs/10.1177/03635465221119194)
- Werner SL, et al. *Correlation of Throwing Mechanics With Elbow Valgus Load in Adult Baseball Pitchers.* Shoulder IR torque ≈ 85% of elbow valgus torque variance. [Academia](https://www.academia.edu/16801750/Correlation_of_Throwing_Mechanics_With_Elbow_Valgus_Load_in_Adult_Baseball_Pitchers)
- Werner SI (1993). *Biomechanics of the Elbow during Baseball Pitching.* JOSPT 17(6):274. [JOSPT](https://www.jospt.org/doi/pdf/10.2519/jospt.1993.17.6.274)
- *Association between pitching velocity and elbow varus torque.* Braz J Phys Ther, 2025. [BJPT](https://www.rbf-bjpt.org.br/en-download-pdf-S1413355525000516)
- *Ulnar collateral ligament injury in the elbow: current trends for treatment.* Annals of Joint — collates Dillman ~32 N·m failure load, Morrey & An 54% restraint share, cadaveric range 17.1–34 N·m. [AOJ](https://aoj.amegroups.org/article/view/5622/html)
- Fleisig GS, et al. (2025). *Increases in Ball Weight and Size Decrease Elbow Varus Torque During Baseball Pitching.* [ASMI PDF](https://asmi.org/wp-content/uploads/fleisig-et-al-2025-increases-in-ball-weight-and-size-decrease-elbow-varus-torque-during-baseball-pitching.pdf)

**Kinematic sequence and energy flow**

- Aguinaldo A, Escamilla R (2019). Trunk-before-pelvis sequencing increases shoulder and elbow torque. (Summarized in the Frontiers 2021 paper below.)
- (2021). *Comparison of Kinematic Sequences During Curveball and Fastball Baseball Pitches.* Frontiers in Sports and Active Living. n = 14 (4 HS, 8 collegiate, 2 pro). [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2021.699251/full) | [PMC8459924](https://pmc.ncbi.nlm.nih.gov/articles/PMC8459924/)
- (2022). *Role of Pelvis and Trunk Biomechanics in Generating Ball Velocity in Baseball Pitching.* Hip-shoulder separation 50 ± 12° at FC. [PubMed 35836313](https://pubmed.ncbi.nlm.nih.gov/35836313/)
- *Predicting elbow load based on individual pelvis and trunk (inter)segmental rotations in fastball pitching.* Sports Biomechanics. [T&F](https://www.tandfonline.com/doi/full/10.1080/14763141.2024.2315230)

**Ground reaction forces**

- Howenstein J, Kipp K, Sabick MB (2020). *Peak horizontal ground reaction forces and impulse correlate with segmental energy flow in youth baseball pitchers.* J Biomech. `[OFF-POPULATION — youth]` [PubMed 32635991](https://pubmed.ncbi.nlm.nih.gov/32635991/)
- (2022). *Roles of each leg in impulse generation in professional baseball pitchers.* Sports Biomechanics. [T&F](https://www.tandfonline.com/doi/full/10.1080/14763141.2022.2108490)
- McNally MP, et al. (2015). *Stride Leg Ground Reaction Forces Predict Throwing Velocity in Adult Recreational Baseball Pitchers.* [ResearchGate](https://www.researchgate.net/publication/276461272)
- Driveline Baseball (2022). *A Quantitative Analysis of the Lead Leg Block and its Contributions to Velocity.* 800+ force-plate sessions, HS→pro. [Driveline](https://www.drivelinebaseball.com/2022/10/a-quantitative-analysis-of-the-lead-leg-block-and-its-contributions-to-velocity/)
- Wasserberger KW, Brady AC, Besky DM, Jones BR, Boddy KJ (2022). *The OpenBiomechanics Project.* 411 fastballs, 100 athletes, HS→affiliated pro, 76 measurement points + force plates.
- (2023). *The Contribution of Lower-Body Kinematics to Pitching and Hitting Performance in Baseball: Utilizing the OpenBiomechanics Project.* [PubMed 37939700](https://pubmed.ncbi.nlm.nih.gov/37939700/)

**Measurement technology**

- Camp CL, Loushin S, Nezlek S, Fiegen AP, Christoffer D, Kaufman K (2021). *Are Wearable Sensors Valid and Reliable for Studying the Baseball Pitching Motion? An Independent Comparison With Marker-Based Motion Capture.* AJSM. [SAGE](https://journals.sagepub.com/doi/abs/10.1177/03635465211029017)
- Boddy KJ, et al. (2019). *Exploring wearable sensors as an alternative to marker-based motion capture in the pitching delivery.* PeerJ. Motus Stress 41 N·m (38.7%) below lab elbow torque. [PMC6348088](https://pmc.ncbi.nlm.nih.gov/articles/PMC6348088/) | [PeerJ](https://peerj.com/articles/6365/)
- (2022). *Validation of pitchAI markerless motion capture using marker-based 3D motion capture.* [PubMed 36409062](https://pubmed.ncbi.nlm.nih.gov/36409062/)
- (2025). *Assessing the accuracy of in-stadium and portable multi-camera markerless motion capture for baseball pitching kinematics and kinetics.* J Sports Sci. n = 18 collegiate; Hawk-Eye MPJPE 56.6 ± 9.4 mm, Theia3D 52.0 ± 12.3 mm. [PubMed 41294254](https://pubmed.ncbi.nlm.nih.gov/41294254/) | [T&F](https://www.tandfonline.com/doi/abs/10.1080/02640414.2025.2595411)
- Lerch (2025). *Variability of in-game markerless and laboratory marker-based baseball pitching biomechanics.* J Biomech 188:112775. n = 30 lab + 30 NCAA D1 in-game. [ASMI PDF](https://asmi.org/wp-content/uploads/LERCH-Journal-of-Biomechanics-2025-188-112775.pdf) | [PubMed 40418881](https://pubmed.ncbi.nlm.nih.gov/40418881/)
- *Predicting elbow valgus torque from upper extremity baseball pitching kinematics using markerless motion capture* (KinaTrax, 8 cameras @ 300 Hz). [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666337625000265)
- Driveline Baseball (2016). *Rapsodo, Trackman, and Pitch Tracking Technologies — Where We Stand.* [Driveline](https://www.drivelinebaseball.com/2016/11/rapsodo-trackman-pitch-tracking-technologies-stand/)

**Off-population sources retained for directional value only**

- Oyama S, et al. — pelvis/trunk sequencing and shoulder proximal force. `[HS sample]`
- Sgroi T, et al. — youth velocity determinants. `[OFF-POPULATION]`
- *Pitch Velocity Is a Predictor of Medial Elbow Distraction Forces in the Uninjured High School–Aged Baseball Pitcher.* `[unselected HS]` [PMC3435942](https://pmc.ncbi.nlm.nih.gov/articles/PMC3435942/)
