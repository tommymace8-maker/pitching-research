# The Hip in the Frontal Plane — abduction, adduction, and late-outing velocity retention

**Opened 2026-09-17. Cycle 16.** Companion to `FINDINGS.md` F-376 → F-387.

**Run condition:** egress probed before topic selection, as F-351 requires. **Four primary texts downloaded and read in full** from `pmc-oa-opendata.s3.amazonaws.com`: PMC8016437 (Zipser 2021), PMC6028199 (Yanai/Jobu 2018, re-read), PMC10830156 (Aso & Kagaya 2024), PMC11698006 (Gauthier, Unverzagt & Davies 2025). Third consecutive reading cycle.

**What is source-verified and what is not, stated once up front:**
- ✅ **SOURCE-VERIFIED (read in full):** every number in §2, §3, §4 and §6.
- ⚠️ **SNIPPET-ONLY:** Kageyama 2014 (§5.1), Ishøi 2016 (§5.2), Laudner 2010 (§2.3), Mullaney 2005 (§4.1, second-hand *through a paper this cycle read at source*).
- 🧮 **DERIVED IN-CYCLE:** §7 (the price) and §8 (detection). No source supports these; the arithmetic does.

---

## 1. Why this topic, and why it was flagged a cycle ago

F-359 (2026-09-15) read PMC6028199 in full for a different purpose and recorded a loose end: after 117 maximal pitches, **isometric hip abduction fell d = 0.41 and adduction d = 0.47, the adduction loss correlated r = 0.583 with the 9th-inning velocity loss, and every squat-jump variable was unchanged.** It was flagged as *"the first specific, measurable, trainable tissue this corpus has seen tied to a within-outing velocity decline — worth a cycle."*

This is that cycle. **The lead ran the other way.** What follows is mostly a demolition, and the one thing left standing is not what was flagged.

The topic matters because it sits at the intersection of two things this program cares about: **velocity retention** (the fade in innings 6–9, which F-289 established is measurable in ~16 fastballs) and **a trainable tissue** (the adductor group, which unlike stride length or pelvis timing can be loaded directly in a weight room).

---

## 2. The one on-population dataset — and it says something nobody has followed up

### 2.1 Zipser et al. 2021, read in full

**Zipser MC, Plummer HA, Kindstrand N, Sum JC, Li B, Michener LA (2021).** *Hip Abduction Strength: Relationship to Trunk and Lower Extremity Motion During A Single-Leg Step-Down Task in Professional Baseball Players.* Int J Sports Phys Ther 16(2):342–349. PMC8016437, PMID 33842030, doi 10.26603/001c.21415.

**n = 118 Minor League players from a single organization** (2017 pre-season physicals), of whom **n = 68 pitchers** (age 21.7 ± 2.2, height 187.4 ± 5.4 cm, mass 94.7 ± 12.8 kg) and **n = 50 position players** (21.4 ± 1.9, 181.5 ± 5.9 cm, 86.3 ± 12.6 kg).

⚠️ **POPULATION NOTE — this is the good news.** The pitcher subsample is an almost exact match for the ASMI professional kinematic cohort logged at F-088 (n = 288 professional, 189.7 cm, 94.7 kg). **This is on-population.** It is the only hip-abduction dataset in this file that is.

Hip abduction isometric strength: side-lying, hip at ~20° abduction, trunk strapped, hand-held dynamometer (MicroFet 2) strapped 5 cm proximal to the lateral knee joint line — so the strap, not the examiner's arm, is the ceiling. Torque (N·m) = force × greater-trochanter-to-dynamometer distance. Two trials averaged. Reliability from the authors' own pilot (n = 7): ICC(3,2) = 0.96, SEM 18.9 N, MDC₉₀ 44.2 N.

### 2.2 The number the authors did not compute

The paper reports descriptives and correlations. It never compares pitchers to position players. **Computed in-cycle from the paper's own Table 2:**

| | Pitchers (n=68) | Position (n=50) | Δ | Cohen's d | t | p |
|---|---|---|---|---|---|---|
| Lead-leg hip ABD torque | 163.3 ± 39.4 N·m | 191.8 ± 50.4 N·m | −28.5 | 0.64 | 3.45 | < .001 |
| Trail-leg hip ABD torque | 166.3 ± 35.0 N·m | 196.6 ± 42.0 N·m | −30.3 | 0.79 | 4.27 | < .0001 |

**And the pitchers are the bigger athletes** — 8.4 kg heavier and 5.9 cm taller. Normalise and the gap widens:

| Normalisation | Pitcher deficit |
|---|---|
| Raw torque | **−15%** |
| Per kg body mass | **−22%** |
| Per kg · m (dimensionally correct for a moment) | **−25%** |

**The sign is robust to every normalisation, and the correct normalisation is the least flattering one.** Torque is force × lever, and pitchers have longer levers, so their raw torque is *inflated* relative to their actual force production.

### 2.3 It replicates

Gauthier et al. 2025 (§6) report that **Laudner KG, Moore SD, Sipes RC, Meister K (2010),** *Functional hip characteristics of baseball pitchers and position players,* Am J Sports Med 38(2):383–387, PMID 19797617, found the same direction in professional baseball: pitchers significantly weaker in drive-leg hip abduction than position players. ⚠️ **SNIPPET-ONLY** — Laudner 2010 was not opened (AJSM is not in the object store). Existence and citation details are confirmed from the reference list of a paper read at source. **The magnitude is not claimed.**

So: **two independent professional samples, same direction.** That is a real, replicated cross-sectional fact, and it is on-population.

### 2.4 What it does NOT mean

Two readings survive the data equally well and they have opposite training implications:

- **(A) Deficiency.** Pitchers are under-loaded in the frontal plane — they do not sprint, cut, or change direction the way position players do — and this is a trainable hole.
- **(B) Irrelevance.** The quality the field says drives pitching velocity is a quality at which pitchers, the specialists, are *worse* than their own teammates. If it were load-bearing for throwing hard, selection would have found it.

**Nothing cross-sectional can separate these.** Reading (A) is the industry's default and is stated nowhere with evidence. See Dispute #28.

### 2.5 The paper's own hypothesis failed, and the failure is instructive

Zipser's actual question was whether hip abduction torque predicts movement quality on a single-leg step-down. Table 2 reports **five movement variables × two legs × three groupings = 30 correlation cells** (20 of them independent: 10 pitcher, 10 position player).

**Two survived, at p = .049 and p = .021.** Under a global null with 20 independent tests you expect 1.0 significant result and P(≥2) = **26%**. Neither survives any multiplicity correction. The largest |r| in the entire table is 0.28 — **R² = 7.8%.**

**For position players, nothing correlated with anything.** The authors' abstract nonetheless concludes *"Hip abduction strength contributes to dynamic control of the trunk and legs."*

**The step-down test does not index hip abduction strength in professional baseball players.** If you use one as a hip-strength screen, you are using an instrument with 6–8% shared variance with the thing you think you are measuring. That is a free, negative, on-population finding (F-378).

---

## 3. The r = 0.583 that started this — taken apart

**Yanai/Jobu University group (2018),** J Exerc Rehabil 14(3):430–435, PMC6028199. n = 18 Japanese collegiate pitchers, 117 pitches over 9 innings, 5-min between innings. Re-read in full this cycle *for its statistics section*, which F-359 did not quote.

### 3.1 It is one of up to fourteen tests

The paper's own words: *"Pearson's correlation coefficients (r) were used to evaluate the correlations between **lower extremity function** after the simulated game and **pitching performance** in the 9th inning; the rate of change in each variable was calculated."*

**Lower-extremity function** = hip abduction, hip adduction, squat-jump height, mean power, peak power, mean velocity, peak velocity = **7 variables.**
**Pitching performance** = ball velocity, pitching accuracy = **2 variables.**

The paper never states how many correlations it actually ran. **The floor is 4** (the two hip measures × the two outcomes); **the ceiling its own sentence licenses is 14.** One was reported significant, at p = 0.011.

| Number of tests | Bonferroni α | p = 0.011 survives? | P(≥1 significant under the null) |
|---|---|---|---|
| 4 | 0.0125 | **barely** | 18.5% |
| 7 | 0.0071 | no | 30.2% |
| 14 | 0.0036 | **no** | **51.2%** |

At the reading its own methods sentence supports, **a coin flip produces a result like this.**

### 3.2 The interval is uninformative

r = 0.583, n = 18. Fisher-z 95% CI: **r ∈ [0.16, 0.82]**, i.e. **R² ∈ [2.5%, 68%].** The point estimate is "a third of the variance"; the interval runs from "negligible" to "almost everything."

### 3.3 It is a correlation between two change scores, in one session

Both variables are rates of change measured on the same fatiguing afternoon. The pitchers who faded most in velocity also faded most in a strength test taken minutes later. **"Fatigue is shared" explains this exactly as well as "adductor capacity protects velocity,"** and the design cannot separate them. This is the F-094 problem (between- vs within-athlete) wearing a different hat.

### 3.4 ⚠️ The instrument cannot support the paper's own discussion

The dynamometer (T.K.K.3367b) was **placed between the thighs with the participant seated**; adduction was measured by squeezing the pads, abduction by pulling against fixation belts. **Both legs act simultaneously. There is no limb-specific measurement anywhere in the study.**

The paper's entire discussion is about **which leg does what** — pivot-leg abductors preventing contralateral pelvic drop during the wind-up, stride-leg adductors stabilising after foot contact. **Its instrument cannot distinguish the stride leg from the trail leg.** That discussion is imported from Kageyama and MacWilliams, not measured here.

### 3.5 What DOES survive from this paper

Do not over-correct. These stand:
- Ball velocity fell **130.3 → 127.8 km/h (1.55 mph)** by the 9th inning, p = 0.001, d = 0.38. A priori outcome, Dunnett-corrected. **Real.**
- Hip adduction strength fell 450.7 → 421.4 N, p = 0.001, d = 0.47 — survives Bonferroni across the seven lower-extremity measures (α = 0.0071). **Real.** Abduction (p = 0.009) does not, at 0.0071. Marginal.
- **Every squat-jump variable was unchanged** (F-359). Still the most useful thing in the paper: the jump mat is blind to pitching fatigue.

⚠️ **POPULATION: first-inning mean 130.3 km/h = 80.96 mph.** Four mph under this corpus's floor. Directional only.

---

## 4. The "replication" is twelve recreational men throwing from ten feet

### 4.1 Aso & Kagaya 2024, read in full

**Aso T, Kagaya Y (2024).** *Effects of repetitive baseball throwing on hip muscle strength and trunk and pelvic motions at the shoulder's maximum external rotation position during the late cocking phase and ball release.* J Phys Ther Sci 36(2):52–58. PMC10830156, PMID 38304150, doi 10.1589/jpts.36.52.

A search summariser offered this as the follow-up establishing that "hip muscle strength decreases after 135 pitches." Read at source:

- **n = 12**, described by the authors as **"nonstrenuous training level"** — *"those who did not engage in physical training and played baseball once or twice a week."*
- Mean mass **67.5 kg (149 lb)**, height **170.4 cm (5'7")**.
- **They threw 135 balls at a 1.1 × 1.1 m target from 3 METRES.** Not from a mound. Not from 60'6".
- **No ball velocity was measured at all.**

⚠️ **SAMPLE MISMATCH, SEVERE — the most severe this corpus has logged.** F-323 (a 76 mph slide-step sample) and F-361 (four consecutive sub-floor between-innings studies) are the prior art. This is worse than either: the task is not pitching.

### 4.2 And the result is internally self-refuting

| | Before (N) | After (N) | Change |
|---|---|---|---|
| Abduction, throwing side | 103.8 ± 32.4 | 79.8 ± 35.0 | **−23.1%** |
| Abduction, non-throwing | 97.8 ± 27.9 | 83.1 ± 30.2 | −15.0% |
| Adduction, throwing side | 86.1 ± 24.3 | 71.1 ± 18.2 | −17.4% |
| Adduction, non-throwing | 87.3 ± 24.2 | 71.3 ± 17.9 | −18.3% |
| External rotation, throwing | 89.8 ± 16.3 | 83.7 ± 15.1 | −6.8% |
| External rotation, non-throwing | 95.5 ± 19.0 | 82.3 ± 17.3 | −13.8% |
| Internal rotation, throwing | 98.7 ± 22.8 | 88.4 ± 23.5 | −10.4% |
| Internal rotation, non-throwing | 105.4 ± 18.5 | 88.3 ± 19.3 | −16.2% |

**All eight measures fell. Both legs. Every direction.** The non-throwing-side abductors — which do essentially nothing in a 3-metre target throw — lost 15%. Two of the four non-throwing-side losses are *larger* than their throwing-side counterparts.

**That is not a throwing-specific adductor fatigue signature. It is a global decline in what a hand-held dynamometer records at the end of a long session** — athlete motivation, examiner technique, or genuine whole-body fatigue, none of which is the claim.

### 4.3 The three studies run backwards

| Study | Population | Task | Hip strength loss |
|---|---|---|---|
| Mullaney 2005 ⚠️ snippet | **Professional** | Real game, 99 ± 29 pitches | **Minimal, NOT significant** |
| Yanai 2018 ✅ read | Collegiate, **81 mph** | 117 max-effort mound pitches | **−5 to −7%** |
| Aso 2024 ✅ read | **Recreational, untrained** | 135 throws from **3 m** | **−15 to −23%** |

⚠️ **THE EFFECT SIZE RUNS INVERSELY TO BOTH THE CALIBRE OF THE ATHLETE AND THE DEMAND OF THE TASK.** A dose-response relationship does not do that. An artifact of measurement and training status does exactly that.

*(Mullaney MJ, McHugh MP, Donofrio TM, Nicholas SJ (2005), Am J Sports Med 33(1):108–113, PMID 15611006. Existence and characterisation taken from the reference list and discussion of PMC6028199, which was read at source. The paper itself was not opened. **Second-hand — and under F-375's standing rule, that is a separate claim from the proposition it carries.**)*

### 4.4 The one thing worth keeping from Aso

Trunk lateral tilt toward the non-throwing side **at ball release** rose from **36.0 ± 8.9° (1st inning) to 41.9° (8th, d = 0.62) and 43.0° (9th, d = 0.77)**, Bonferroni-corrected. Pelvic tilt did not move; nothing moved at MER.

**As he tires, he tips over.** And trunk contralateral tilt at ball release is a **positive contributor to normalized elbow varus torque** (F-101). Injury line, one sentence, then move on: fatigue drifts a pitcher toward a torque-raising posture, and it shows up on a back-view camera before anything shows up on a radar gun. ⚠️ Recreational sample; directional only. Note the coincidence worth *not* over-reading: 36.0° matches the ASMI professional norm of 34 ± 8° (F-088).

---

## 5. The rest of the chain

### 5.1 The mechanism source — Kageyama 2014 ⚠️ SNIPPET-ONLY

**Kageyama M, Sugiyama T, Takai Y, Kanehisa H, Maeda A (2014).** *Kinematic and kinetic profiles of trunk and lower limbs during baseball pitching in collegiate pitchers.* J Sports Sci Med 13(4):742–750. PMID 25435765, PMC4234942.

**EXISTENCE: VERIFIED** — the full citation, PMID and PMCID appear in the reference list of PMC6028199, read at source.
**SUBSTANCE: NOT VERIFIED.** PMC4234942 is **absent from the object store** (see F-376); no other route exists. Everything below is snippet-level.

Reported: hip adduction torque of the **stride leg at foot contact** was significantly greater in a high-velocity group than a low-velocity group; pivot-leg hip abduction, hip IR and knee extension torques likewise.

⚠️ **AND THE GROUPS ARE 37.4 ± 0.8 m/s (83.7 mph) vs 33.3 ± 0.8 m/s (74.5 mph).** The "high-velocity" group is **below this corpus's floor**, and the contrast is manufactured from a **9.2 mph spread** that does not exist in an SEC bullpen. This is the restriction-of-range problem inverted: Luera 2020 (n = 149 pros) showed correlations collapse to r = .17–.29 when everybody throws hard; Kageyama's design widens the range until something separates.

**Two questions that must be asked before this paper is ever cited again, and cannot be asked until someone reads it:**
1. **Were the torques normalised to body mass × height?** If not, "bigger, faster athletes generate bigger joint torques" is a near-identity. F-061 already established that **roughly half** the raw lead-leg-force/velocity correlation in a Driveline dataset was **bodyweight**.
2. **Is a joint torque at foot contact an independent variable at all**, or a downstream readout of the momentum the athlete arrived with?

### 5.2 The trainability half — and it is the only established link ⚠️ SNIPPET-ONLY

**Ishøi L, Sørensen CN, Kaae NM, Jørgensen LB, Hölmich P, Serner A (2016).** *Large eccentric strength increase using the Copenhagen Adduction exercise in football: A randomized controlled trial.* Scand J Med Sci Sports. PMID 26589483.

Reported: **n = 24 U-19 sub-elite footballers**, randomised, 8 weeks supervised progressive Copenhagen Adduction in addition to usual training vs usual training alone. **Eccentric hip adduction strength +35.7%, eccentric hip abduction +20.3%, EHAD/EHAB ratio +12.3%.** No significant within-group change in controls. Compliance 91.25%, median soreness 0–2.

⚠️ **Existence corroborated across PubMed and a systematic review; the article was not opened.** Wrong sport, adolescent footballers, and the outcome is **strength, not throwing anything.**

### 5.3 So here is the whole chain, with each link's actual grade

| Link | Claim | Grade | Population |
|---|---|---|---|
| 1 | Hip adductor strength is **trainable**, and the dose is known | **ESTABLISHED (RCT)** ⚠️ snippet | U-19 **footballers** |
| 2 | Pitchers are **weaker** here than position players | **ESTABLISHED, replicated, cross-sectional** ✅ | **Professional** ✓ |
| 3 | Hip adduction torque is higher in **harder throwers** | **WEAK** ⚠️ snippet | 83.7 vs **74.5 mph** ✗ |
| 4 | Hip strength **falls** across an outing | **EMERGING, and the three studies run backwards** | 81 mph / recreational ✗ |
| 5 | That fall **explains** the velocity fade | **WEAK** — 1 of up to 14 tests, CI [0.16, 0.82] | 81 mph ✗ |
| 6 | **Training it raises or protects velocity** | **NEVER TESTED. ANYWHERE.** | — |

**Link 6 does not exist.** Not one intervention has ever manipulated hip frontal-plane strength in throwers and measured ball velocity, peak or retained. This was confirmed against a 2025 clinical review whose own text concedes *"only one known study evaluating hip strength changes with increasing pitching counts has been published."*

---

## 6. ⚠️ A citation error caught at source, in a peer-reviewed clinical review

**Gauthier ML, Unverzagt CA, Davies GJ (2025).** *Evaluation and Treatment of Baseball Pitchers: There's More to Assess than the Arm.* Int J Sports Phys Ther 20(1). PMC11698006, PMID 39758696, doi 10.26603/001c.127461. **Read in full.**

The review's stride-phase paragraph ends:

> *"Drive leg hip abduction strength has been shown to impact performance as well, as peak ground reaction force (GRF) of the drive leg is strongly associated with ball speed.²⁰ **This suggests that a stronger push off the pitching rubber via hip abduction increases pitch velocity.**"*

**Reference 20, from the review's own reference list, is:**

> McNally MP, Borstad JD, Oñate JA, Chaudhari AMW (2015). ***Stride leg** ground reaction forces predict throwing velocity in adult **recreational** baseball pitchers.* J Strength Cond Res 29(10):2708. PMID 26402471.

**Three unlicensed steps in one sentence, plus a population mismatch:**

1. **WRONG LEG.** A *drive-leg* claim is supported with a *stride-leg* study. The title says so.
2. **WRONG VARIABLE.** *Ground reaction force during the pitch* is substituted for *isometric hip abduction strength in a gym.* These are not the same construct and nobody has shown they covary in this population. **F-061 is directly on point: once bodyweight was controlled, the lead-leg block explained only ~4–6% of between-pitcher velocity variance, and roughly half the raw force/velocity correlation was body mass.**
3. **ASSOCIATION → CAUSATION.** "Strongly associated" becomes "increases pitch velocity," in the imperative-adjacent voice, two sentences before the review recommends implementing a strengthening program.
4. **POPULATION.** Adult **recreational** pitchers, in a review written about professional and elite arms.

This is the **F-245 pattern** (Driveline's inverted Sherwood label) at a higher altitude: a peer-reviewed clinical commentary, in a real journal, by three university faculty, with a correct citation attached to a sentence the citation does not support. **It is not a fabrication.** Every fabrication defence passes. It is the failure mode this program's 2026-08-13 operating rule was written for: *verifying a citation is not verifying a claim.*

Also in the same paragraph: Laudner's strength finding is reported as pitchers being weaker *"**requiring** increased demand on the trunk and upper extremity to generate force."* The requirement was not measured. It is an inference wearing a finding's grammar.

---

## 7. 🧮 What the whole prize is worth

Derived in-cycle. No source supports this; the arithmetic does.

**The fade, sized.** Yanai: −1.18 mph by the 7th, −1.55 mph by the 9th, i.e. roughly **−0.2 mph per inning after the first.** Over a 6-inning college start the *average* velocity deficit across the whole outing is therefore ≈ **0.5 mph** (0, 0.2, 0.4, 0.6, 0.8, 1.0). ⚠️ Ramp shape taken from an 81 mph sample; the absolute slope at 85+ is unmeasured.

**The conversion.** This corpus brackets **0.15–0.40 runs per mph per 9 IP** (`running-game.md` §5.2). A 90-inning starter is ten 9-inning units, so **1 mph sustained = 1.5–4.0 runs per season.**

**The prize.**

| Scenario | Velocity recovered | Runs / season |
|---|---|---|
| Fade eliminated entirely | 0.5 mph | **0.75 – 2.0** |
| Fade halved | 0.25 mph | **0.4 – 1.0** |
| Fade cut by a quarter | 0.125 mph | 0.2 – 0.5 |

**The whole topic is worth about one run a season.** That puts it in the same tier as times-through-the-order (~1 run, F-288) and an order of magnitude below a gross pitch-mix error (3–23 runs, F-272). ⚠️ Three stacked brackets; **the ordering is the output, the cells are not.**

**This is the finding that should govern the coaching decision, and it points away from the enthusiasm.** Do not spend a training block on velocity *retention*. If you train the adductors, train them for a reason that stands on its own.

---

## 8. 🧮 How you would know — and the asymmetry that decides the protocol

### 8.1 Velocity retention IS measurable, in about four simulated outings per side

Define retention **R = mean(last 15 fastballs) − mean(first 15 fastballs)** in a standardised ~90-pitch simulated outing.

Within-session SE(R) = σ_p × √(2/15), with the corpus's bracketed within-pitcher fastball SD σ_p = 0.8 / 1.0 / 1.2 mph (F-289) → **0.29 / 0.37 / 0.44 mph.**

Add session-to-session variation in *true* retention, σ_s. ⚠️ **σ_s has never been measured for any population** — new gap, and the tenth entry in the "already in every program's radar log, published by nobody" pattern. Taking σ_s = 0.3 mph gives a per-session SD of R of **0.42 / 0.47 / 0.53 mph.**

Minimum detectable effect at α = .05 two-sided, 80% power, k sessions per side: **MDE = 2.8 × SD_R × √(2/k).**

| k per side | σ_p = 0.8 | σ_p = 1.0 | σ_p = 1.2 |
|---|---|---|---|
| 3 | 0.96 | 1.07 | 1.21 |
| **4** | **0.83** | **0.93** | **1.05** |
| 6 | 0.68 | 0.76 | 0.86 |

**Four standardised simulated outings before and four after detects roughly a 1 mph change in retention** — against a total fade of ~1.5 mph. **You can detect "we cut the fade by two-thirds." You cannot detect "we cut it by a quarter."** And per §7, a quarter is what is actually on the table.

⚠️ **THE PRICE IS REAL AND THE ANATOMIST OBJECTS TO IT.** Eight standardised 90-pitch maximum-effort outings is a serious workload imposition that exists only to measure something worth under a run. It is only defensible if it replaces outings that were happening anyway.

### 8.2 The strength DROP is not measurable at all

Yanai's adduction drop was 29.3 N at d = 0.47 ⇒ SD of the drop ≈ **62.3 N.** Comparing the drop before and after a training block, SD of the change-in-drop ≈ 62.3 × √2 ≈ **88 N.** To detect a **halving** of the drop (Δ = 15 N): **n = (2.8 × 88 / 15)² ≈ 271 starts.**

⚠️ 62.3 N is a *between-subject* SD standing in for a within-subject test-retest SD. The order of magnitude survives any reasonable correction.

**So: never instrument this with a fatigue-drop measurement.** Change scores compound two noisy measurements; levels do not.

### 8.3 What you actually measure

**The compliance check is the strength LEVEL, not the velocity and not the drop.** Ishøi's effect is +35.7% on eccentric hip adduction — enormous relative to the SEM of a strapped dynamometer (Zipser's MDC₉₀ was 44.2 N on a ~450 N measure, ≈ 10%). **A single athlete's strength gain from an 8-week block is detectable in one retest.** His velocity retention is not.

**This is the eleventh instance of the corpus's governing shape:** verify the input, never the outcome. F-270/F-273 (mix), F-282 (counts), F-286 (TTOP), F-287, F-295 (sequencing), F-307, F-310 (location), F-320 (the running game), F-374 (arousal) — and now this.

---

## 9. What to actually say to an 85+ arm

**Say this:**
> "Your hips are probably weaker side-to-side than the shortstop's — that's true of basically every pro pitcher who's been measured. We're going to fix that because it's cheap, it takes eight weeks, and there's good evidence it protects your groin. **I am not telling you it will add velocity, and I'm not telling you it'll keep your velo in the seventh. Nobody has ever tested either one.** If it does, it's worth about a run a year, which is less than it sounds like."

**Never say:**
- "Your adductors are why you lose velo late." (One correlation, 1-of-14, n = 18, 81 mph, CI [0.16, 0.82].)
- "Push harder off the rubber with your hip abductors to throw harder." (§6 — that sentence is a citation error propagating out of a clinical review.)
- Anything derived from a single-leg step-down score about hip strength (§2.5 — 6–8% shared variance).

**The drill, and it is genuinely cheap:** Copenhagen Adduction, 8 weeks, 2–3×/week, progressive (short-lever → long-lever → added load). Ishøi's compliance was 91% and median soreness 0–2, which is the real argument for it — it is one of the few high-eccentric-load exercises athletes will actually keep doing.

**On video, the failure looks like:** nothing at the hip. Watch the **back view at ball release** for the trunk tipping further toward the glove side late in an outing (§4.4, 36° → 43° in the only study that measured it). That is the frontal-plane tell, and it is on the torque-raising side of F-101.

**Here is how we know it's working:** a handheld-dynamometer retest at 8 weeks showing an eccentric adduction gain well clear of the ~10% MDC. That is the whole verification. **Anything you claim about his seventh inning is a story.**

---

## 10. Open, and what would close it

1. **Dispute #28** — is the pitcher/position-player hip abduction gap a *deficiency* or a *selection signature*? (§2.4)
2. **The missing intervention.** Copenhagen block vs matched control, elite pitchers, outcomes = peak velocity AND retention. Nobody has run it. It is not expensive.
3. **Kageyama 2014's normalisation.** Unreadable through current egress. Until someone reads it, the field's only mechanism paper is a snippet.
4. **σ_s**, the session-to-session SD of within-outing velocity retention. In every radar log. Published by nobody.
5. **Does the frontal-plane deficit predict anything within pitchers?** Every result in this file is between-athlete. F-094 says that is the wrong denominator.
