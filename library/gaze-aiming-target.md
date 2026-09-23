# Gaze, the Quiet Eye, and the Aiming Target in Pitching

**Opened 2026-09-23. Cycle 24.** Companion to `FINDINGS.md` F-450 → F-461.

> ## 🚨 CORRECTED 2026-09-23 — MID-CYCLE. THE RUN CONDITION STATED BELOW WAS WRONG, AND IT WAS WRONG IN THIS CYCLE'S OWN FAVOUR.
>
> **What was written first:** *"WebFetch was denied on every host attempted... NOT ONE SOURCE BELOW WAS READ AT SOURCE."* That was true of **WebFetch** and it was **false as a statement about this cycle's reading access.**
>
> **What was wrong with it:** the cycle probed WebFetch and `curl` against *journal websites* and, on getting `000` from all of them, declared a blockade — **without probing the two object stores `INDEX.md` §0 has documented as SERVING since 2026-09-15.** F-351 requires probing before topic selection; the probe was run against the wrong hosts. **This is the corpus's own documented retrieval pattern and the cycle skipped it.**
>
> **What actually serves, re-confirmed 2026-09-23:**
> - `pmc-oa-opendata.s3.amazonaws.com` — **HTTP 200, listable**, keyed `PMC<id>.<ver>/`, serving `.txt`/`.xml`/`.pdf`.
> - `storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/<yymm>/<id>v1.pdf` — **HTTP 200.**
>
> **THREE PRIMARY TEXTS WERE THEN DOWNLOADED AND READ IN FULL:** PMC7739699 (the darts intervention), **arXiv 2603.04874** (the corpus's named highest-value unread item since 2026-09-07) and **arXiv 2508.19184** (xCTRL). **Sections §4.4, §5 and §8.1 are SOURCE-VERIFIED and are marked as such in place.** The original snippet-era text is retained where it was wrong so the error cannot be re-imported.
>
> **THE LESSON, REGISTERED AS F-462:** *"WebFetch is blocked"* is not the same proposition as *"this cycle cannot read papers,"* and the corpus has now conflated them at least twice. **The probe is against the OBJECT STORES, not against the journals.**

**Run condition — as originally written, superseded above.** Egress was probed before topic selection. **WebFetch was denied on every host attempted**, including `pmc.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `europepmc.org`, `frontiersin.org`, `mdpi.com`, `arxiv.org`, `semanticscholar.org`, `thescholarship.ecu.edu` and `perceptionaction.com` — and including **`en.wikipedia.org` as a control**. `curl` to those same hosts returns `000`. **WebSearch worked.** *(All of this remains true. The error was the inference drawn from it.)*

**What is what, corrected:**
- 🧮 **DERIVED IN-CYCLE — unaffected by any of this.** §2 (angular geometry), §3 (optics), §6 (detection). The arithmetic stands on its own and is checkable on a calculator.
- ✅ **SOURCE-VERIFIED, read in full:** §4.4 (PMC7739699), §5 (arXiv 2603.04874), §8.1 (arXiv 2508.19184).
- ⚠️ **STILL SNIPPET-ONLY:** §4.1 (Kuchmaner — `digitalcommons.wku.edu` not probed against an object store; no PMCID or arXiv ID exists), §4.2 (the ECU thesis), §4.3 (Lebeau 2016 — **not in the PMC OA subset**), §4.5 (NCT04289376), §8.2–§8.6.

---

## 1. Why this topic

`INDEX.md` §5 has carried **"Quiet eye in throwing — flagged, not opened"** since 2026-09-16, with the note that the flagship quiet-eye training interventions are **n = 14 and n = 16 novices** in golf putting and basketball free throws. `gaze` returned **zero hits** across `FINDINGS.md` before today.

The topic is worth a cycle because the corpus's own position is that **command is the biggest lever most 90+ arms leave on the table** (README), and "look at the target" is the single most universal command instruction in the sport. If it is a lever, that is enormous and free. If it is not, a great deal of bullpen attention is being spent on nothing.

**The cycle's answer is: it is not a lever, and the reason is geometric rather than empirical.** The literature question turned out to be secondary to an arithmetic one nobody in the quiet-eye literature appears to have asked.

---

## 2. 🧮 THE CENTRAL RESULT — the quiet-eye criterion is twice as wide as the entire strike zone

### 2.1 The definition, and the part of it that does not travel

Two independent search snippets — the Kuchmaner conference abstract (§4.1) and the Lebeau-lineage summaries (§4.3) — state the standard definition identically:

> the final fixation on a specific location or object in the task environment, **within 3° of visual angle**, for a minimum of **100 ms**, before movement initiation.

The **100 ms** is a duration and travels between tasks unchanged. The **3°** is an *angle*, and an angle is not a size. **The linear region it admits scales with the distance to the target**, and the quiet-eye literature's canonical tasks are all near-field while pitching is far-field by an order of magnitude.

The subtended width of a 3° cone at distance $D$ is

$$s = 2 D \tan(1.5°) = 0.05241\,D$$

### 2.2 The table

| Task | Eye→target distance | 3° window | Target's own width | **Window ÷ target** |
|---|---|---|---|---|
| Golf putt | 0.9 m | 4.7 cm | hole, 10.8 cm | **0.44** |
| Darts | 2.4 m | 12.6 cm | board, 34 cm | **0.37** |
| Basketball free throw | 4.4 m | 23.0 cm | rim, 45.7 cm | **0.51** |
| **Pitching, to the zone** | **18.44 m (60.5 ft)** | **96.6 cm = 38.0 in** | **zone, 43.2 cm = 17 in** | **2.24** |
| **Pitching, to a glove** | 18.44 m | 38.0 in | mitt, ~12 in | **3.2** |

In every flagship quiet-eye task the criterion admits a window **roughly 0.4–0.5 times the target's own width** — a genuinely demanding constraint. On a mound it admits a window **2.2 times the width of the strike zone**, and **3.2 times the width of a catcher's mitt**.

### 2.3 Said the other way — the angular budget the pitch actually has

Ball travel from release is `60.5 ft − extension`; at the corpus's 6.0 ft convention (`hitter-perception.md` §2) that is **54.5 ft = 654 in**.

- **1 inch of lateral miss at the plate = `atan(1/654)` = 0.0876° = 5.3 arcminutes.**
- A **6-inch** command miss = **0.53°**.
- The **entire strike zone**, seen from release, is `atan(17/654)` = **1.49° wide**. From the eyes at 60.5 ft it is **1.34°**.

> ### 🚨 **The quiet-eye tolerance (3°) is TWICE the angular width of the entire strike zone (1.3–1.5°).**
> A pitcher can satisfy the textbook quiet-eye criterion while his gaze wanders across a region containing the glove, the catcher's mask, both of the catcher's shoulders and a foot of dirt on either side. **The measurement does not resolve the thing it is named for.**

**This is not an objection to quiet-eye theory. It is an objection to importing quiet-eye *numbers* into pitching.** Whatever a quiet-eye duration means in putting, the same number measured on a mound is a much weaker statement about where the athlete was looking, and the two are not comparable. Every published quiet-eye effect size was estimated under a spatial constraint 4–6× tighter, relative to the target, than the one a mound imposes.

### 2.4 What this does and does not kill

It does **not** show that gaze is irrelevant to pitching. It shows that:
1. **The pitcher-side quiet-eye measurements cannot inherit the literature's effect sizes** (Lebeau's d = 0.84 for intervention performance, §4.3).
2. Any pitcher-side quiet-eye study using the standard 3° criterion is measuring **"did he look roughly at the catcher"**, not **"did he look at the target."**
3. A pitcher-specific criterion would have to be on the order of **0.75°** to be as demanding, relative to the target, as putting's 3° is — which is **inside the width of the fovea (~2°)** and therefore at the edge of what head-mounted eye trackers resolve in the field.

---

## 3. 🧮 THE OPTICS — at 60 feet, the eyes cannot tell the pitcher how far away the target is

Interpupillary distance ≈ 6.3 cm. Binocular vergence at distance $D$ is $\theta = 2\arctan(\text{IPD}/2D)$:

| Distance | Vergence angle | Change in vergence per unit of depth error |
|---|---|---|
| 0.9 m (putt) | 4.01° = 241 arcmin | 1 cm of depth → **2.7 arcmin** |
| 4.4 m (free throw) | 0.82° = 49 arcmin | — |
| **18.44 m (60.5 ft)** | **0.196° = 11.7 arcmin** | **1 ft of depth → 0.19 arcmin = 11.7 arcsec** |

Stereoacuity in good observers runs **20–30 arcsec** and degrades with distance. So:

> **A one-foot depth error at 60.5 ft produces a vergence change at or below the stereo threshold. Binocular depth information about the catcher's mitt is effectively unavailable to the pitcher.**

**Why it matters.** Quiet-eye's proposed mechanism includes *parameterising the movement from a precise target localisation*. At putting distance the eyes supply depth richly. At 60.5 ft they do not: the pitcher's distance-to-plate is **a constant he knows, not a quantity he sees**. His aiming problem is two-dimensional and angular, and the depth dimension — which is where most of a fastball's command error actually lives, since high/low miss is dominated by release *timing* rather than by aim — **receives no visual input at all.**

This is the strongest mechanistic reason to expect quiet-eye transfer to pitching to be poor, and it is independent of §2.

---

## 4. ⚠️ THE LITERATURE — snippet-only, and thinner than the topic's reputation

### 4.1 The only pitcher-specific quiet-eye study found is **n = 3**

**Kuchmaner JI.** *Identifying the Quiet Eye — Duration and Target Acquisition Significance in Pitching.* International Journal of Exercise Science: Conference Proceedings, vol. 16 iss. 2 art. 21. `digitalcommons.wku.edu/ijesab/vol16/iss2/21`

- **n = 3 elite pitchers**, 30 pitches each to live hitters, 15 in a **set-target** condition (catcher flashes and holds the glove at the intended target right after the call) and 15 in a **non-set-target** condition (catcher does not move until after release).
- A search summary reports *"a significant difference in fixation duration in the set versus non-set targeted conditions (1126.88 ms)."*

**⚠️ THREE REASONS THIS IS NOT EVIDENCE FOR A MAGNITUDE.**
1. **It is a conference abstract.** The corpus's standing rule (F-247 lineage): *a conference abstract with no retrievable sample is not evidence for a magnitude.*
2. **The reported number is almost certainly mis-paraphrased.** A **1,127 ms difference** in fixation duration is not a plausible between-condition delta; it is far more likely the *mean fixation duration in the set condition*. **The corpus has inherited exactly one wrong claim before, from a third-party paraphrase of a source nobody read.** This is that shape. Recorded as **UNVERIFIED**.
3. **n = 3 athletes.** 90 pitches is not 90 independent observations. The comparison is within-athlete across conditions, so the athlete-level n is **three**. Analysed at the pitch level without a random intercept — which an abstract gives no way to check — the p-value is uninterpretable. F-439's n ≥ 97 rule does not even get a chance to apply.

### 4.2 A second pitcher-side document exists and could not be identified

**"JUST THROW STRIKES! THE RELATIONSHIP BETWEEN QUIET EYE DURATION AND BASEBALL PITCHING ACCURACY IN LOW- AND HIGH-PRESSURE TASKS"**, East Carolina University repository, `thescholarship.ecu.edu/items/53f1bb07-6535-489d-afe1-4c39b157a14e`. **Egress-blocked.** Three separate searches failed to return its author, its year, its sample size, or a single number. Two of the three searches **conflated it with the Kuchmaner abstract**, returning Kuchmaner's title and method under this document's URL.

**Recorded as UNREAD and UNIDENTIFIED, and flagged as a live re-import vector**: any future cycle that meets an "n =" for this thesis from a search summary should assume it may be Kuchmaner's until a primary read says otherwise.

### 4.3 The general quiet-eye evidence base

**Lebeau JC, Liu S, Sáenz-Moncaleano C, Sanduvete-Chaves S, Chacón-Moscoso S, Becker BJ, Tenenbaum G (2016).** *Quiet Eye and Performance in Sport: A Meta-Analysis.* J Sport Exerc Psychol 38(5):441–457. PMID 27633956.

- **Non-intervention synthesis**, 27 studies / 38 effect sizes: expert-vs-novice quiet-eye difference **d = 1.04**; within-individual successful-vs-unsuccessful **d = 0.58**.
- **Intervention synthesis**, **9 articles**: quiet-eye period **d = 1.53**, performance **d = 0.84**.

**How to read this, per this corpus's own rules:**
- The **d = 1.04** and **d = 0.58** are **CROSS_SECTIONAL**. Marker, not lever. d = 1.04 is a between-groups expert/novice contrast and is exactly the design `F-094` says is the wrong denominator; d = 0.58 is within-individual but still observational — quiet eye is *longer on the shots that went in*, which is as consistent with "a good shot is preceded by a calm system" as with "a long look causes a good shot."
- The **d = 0.84** is the only **INTERVENTION** number, and it rests on **nine articles**. The corpus has repeatedly found (F-189, F-190, F-192) that small intervention syntheses in motor learning **do not survive bias correction**: Wulf's external-focus literature went from g = 0.26/0.58 to bias-corrected **g = 0.01/0.15** under robust Bayesian re-analysis, and the OPTIMAL-theory pillars went to zero. **A k = 9 synthesis with d = 1.53 on the mediator and d = 0.84 on the outcome is the exact profile those re-analyses were run on.**
- ⚠️ A search summary reports that *"quiet eye effect sizes were found to be more resistant to publication bias than performance effect sizes"* — i.e. **the mediator is better-supported than the outcome**, which is the wrong way round for a training claim. **Snippet-only, attributed to no specific paper, and not usable.**

**Grading: EMERGING, and CONTESTED by analogy rather than by a located re-analysis. No bias-corrected quiet-eye estimate was retrieved.**

### 4.4 ✅ SOURCE-VERIFIED — the one manipulated throwing result, and it is WORSE for quiet eye than the title says

**Rienhoff-lineage / Oldenburg group (2020).** *Looking to Learn Better — Training of Perception-Specific Focus of Attention Influences Quiet Eye Duration but Not Throwing Accuracy in Darts.* Frontiers in Sports and Active Living 2:79, 10.3389/fspor.2020.00079, PMID 33345070, **PMC7739699 — downloaded and READ IN FULL 2026-09-23.**

**Design.** **n = 36 dart NOVICES**, randomised after a pretest into **four** groups — internal-visual (n = 10, *"concentrate on your eye"*), external-visual (n = 9, *"concentrate on the bullseye"*), internal-kinesthetic (n = 7, *"concentrate on your hand"*), external-kinesthetic (n = 10, *"concentrate on the dart"*). Four participants dropped out during training. **Pretest 30 throws → three training days × 50 throws → posttest**, ~7 days total. **Throwing distance 2.37 m; WDF board, 34 cm diameter; bullseye at 1.73 m.** Outcomes: **quiet-eye duration (ms)** by SMI eye-tracking glasses at **60 Hz**, and **throwing accuracy as radial distance from the bullseye (cm)**.

**Table 3, verbatim from the paper:**

| Group | TA pre (cm) | TA post | QED pre (ms) | QED post |
|---|---|---|---|---|
| Internal-visual | 6.8 ± 1.2 | 6.1 ± 1.2 | 498 ± 322 | **867 ± 392** |
| External-visual | 6.6 ± 1.8 | 6.7 ± 2.0 | 499 ± 347 | **946 ± 442** |
| Internal-kinesthetic | 11.0 ± 4.4 | 11.3 ± 2.8 | 618 ± 380 | **579 ± 293** |
| External-kinesthetic | 10.8 ± 2.9 | **9.6 ± 3.6** | 686 ± 482 | **565 ± 384** |

**Results.** QE duration rose overall, **574 → 747 ms, F(1,32) = 6.93, p = 0.01, f = 0.43** — quiet eye IS trainable in a week. **Significant test × perception-focus interaction, F(1,32) = 15.31, p < 0.01, f = 0.69: the visually instructed groups went UP and the kinesthetically instructed groups went DOWN.** Accuracy: **8.7 ± 3.3 → 8.2 ± 3.2 cm, F(1,32) = 1.13, p = 0.30, f = 0.13, NS.** Group ANCOVA (needed because of a pretest imbalance): **F(1,31) = 3.35, p = 0.08, f = 0.33, NS.**

> ### 🚨 THREE THINGS THE ABSTRACT DOES NOT SAY, AND ALL THREE MATTER
>
> **(1) THE ASSOCIATION RUNS BACKWARDS.** The paper's own discussion: *"the kinesthetically instructed groups showed a lot higher improvement in throwing accuracy compared with visual or internal instructions"* and *"the kinesthetic-external group showed the highest improvement in throwing accuracy."* **Those are the two groups whose quiet-eye duration went DOWN.** The group that gained the most quiet eye (external-visual, 499 → 946 ms) **got worse** (6.6 → 6.7 cm). The group that lost the most quiet eye (external-kinesthetic, 686 → 565 ms) **improved the most** (10.8 → 9.6 cm). This is not a null. **Within this experiment, quiet-eye gain and accuracy gain are NEGATIVELY associated.**
>
> **(2) THE BASELINE IMBALANCE IS ENORMOUS AND IT CONFOUNDS (1).** Pretest accuracy differed between the perception-specific foci at **F(1,32) = 20.75, p < 0.01, f = 1.47** — visual groups at 6.6–6.8 cm, kinesthetic groups at 10.8–11.0 cm. **Randomisation with 7–10 per group produced a gap larger than any effect the study was looking for.** The kinesthetic groups had far more room to improve, so **regression to the mean alone predicts the pattern in (1).** The negative association is therefore **suggestive and confounded — it should not be registered as a finding, and it absolutely should not be reversed into "long quiet eye is bad."**
>
> **(3) 🚨 THE REPORTED POWER IS NOT ACHIEVABLE.** The paper attaches **`1 − β = 0.95`** to almost every null, alongside observed effect sizes as small as **f = 0.03**. **Recomputed for this design (2×2 ANOVA, N = 36, df = 1,32, α = .05): power at the observed f = 0.13 is 11.6%, and at f = 0.33 it is 48.8%.** Reaching 80% would need **N ≈ 465** at f = 0.13 and **N ≈ 72** at f = 0.33. **A reported 1 − β of 0.95 beside an actual 0.12 is off by a factor of eight** — it is an a-priori target reported as achieved power, and it is the exact failure F-439's n ≥ 97 rule exists to catch.

**GRADE: the accuracy null is a DETECTION FLOOR, NOT AN ABSENCE (F-439). n = 36 novices at 2.37 m.** The **trainability** result (F = 6.93, f = 0.43) is the solid part and is not in dispute. **What this study does NOT establish is that quiet-eye training improves throwing accuracy — and it is the only manipulated throwing test that exists.**

### 4.5 The registered trial with the right name is about hitters

**NCT04289376, "Quiet Eye Duration in Baseball"**, Ohio State, PI Nicklaus Fogt. **n = 20** (10 with HS-or-above baseball/softball experience, 10 without), **watching videos of a pitcher** to test for anticipatory gaze toward the release point. **This is a batter-perception study.** Recorded so that no future cycle mistakes it for pitcher-side evidence.

---

## 5. ✅ SOURCE-VERIFIED — gaze may be a TIPPING channel, not a command lever

**Bright J, Lu M, Zelek J (University of Waterloo).** *Interpretable Pre-Release Baseball Pitch Type Anticipation from Broadcast 3D Kinematics.* **arXiv 2603.04874v1 — downloaded from the arXiv bulk corpus and READ IN FULL 2026-09-23.** This closes the corpus's **highest-value unread item**, open since 2026-09-07 (`idea-scouting.md` §4).

**Design.** Monocular broadcast video → diffusion-based 3D pose backbone → 17 joints (incl. **nose and both eyes**) → automatic detection of three events (**foot plant / maximum external rotation / release**) → 154 raw-pose + 45 biomechanical + 30 temporal-delta features → **XGBoost**, 8-class pitch type. **119,561 pitches**, stratified 80/20 split (95,648 train / 23,913 test).

| Quantity | Value |
|---|---|
| Overall accuracy, **8 classes** | **80.4%** (RHP 80.6% / LHP 79.9%) |
| **Majority-class baseline** | **32.3%** (FF) — the accuracy is genuinely strong |
| Raw poses only → +biomech → +temporal deltas | 76.5% → 78.9% → **80.4%** |
| Event-based vs evenly-spaced sampling | **76.5% vs 63.2%** on the same 154 features |
| Upper body : lower body importance | **64.9% : 35.1%** (1.85:1) |
| Arms | 40.5% |
| **Head joints (both eyes + nose), COMBINED** | **19.0%** |
| **Both wrists, COMBINED** | **14.8%** |
| **Trunk** | **5.3%** |
| Importance by event | release 35.9%, others within a 5% band |
| Ceiling | FF↔FT is the dominant confusion — grip-defined variants are **not separable from pose** |

> ### ✅ THE SNIPPET'S "INTERNAL INCONSISTENCY" IS RESOLVED AT SOURCE — AND THE FLAG WAS RIGHT TO BE RAISED
> The search summary said wrist was *"the most informative joint group"* at 14.8% while giving head/eyes 19.0%. **The paper says the opposite:** head joints *"collectively contribute 19.0%, higher than any single limb group."* **The summariser inverted the ranking.** The cycle's original instruction — *use the order of magnitude, never the ranking* — was correct, and the ranking it declined to use was wrong. **This is the third documented instance of search-summary corruption in this corpus** (after the invented *"Park et al., 12.4 million pitches"* and the fabricated grip-strength r = .705).

**✅ The paper frames this itself:** it extracts pre-release features *"enabling interpretable importance rankings as **batter-visible 'tells' for anticipation training**."* The tipping reading is the authors' own, not this corpus's extrapolation.

### 5.1 🚨 WHAT THE PRIMARY READ CHANGED — three objections, one dead, two alive and sharper

**❌ DEAD — "the head share is inherited from trunk lateral tilt."** This cycle's opening objection (Dispute #38) assumed head orientation was a proxy for trunk tilt. **At source, the trunk carries 5.3% of total joint importance and head joints carry 19.0% — the head group is 3.6× the trunk group.** The trunk-inheritance story does not survive its own arithmetic. **Conceded on the record.**

**⚠️ ALIVE, AND NOW THE PRINCIPAL OBJECTION — the importance measure is XGBoost GAIN, and there is NO leave-one-joint-out ablation.** The paper's §5.6 ablations are **by feature CATEGORY** (raw pose / biomech / temporal), never by joint or region. **So the head's 19.0% is never tested by removing it.** Gain-based importance is the measure most known to distribute arbitrarily among correlated predictors, and head orientation is correlated with arm slot and shoulder position, not only with the trunk. **The 19.0% is a share of attributed gain, not a demonstrated channel, and the paper does not run the test that would make it one.** Dispute #38 survives in this amended form.

**⚠️ ALIVE, AND NOT DISCUSSED BY THE PAPER AT ALL — there is no held-out-PITCHER evaluation.** The 80/20 split is stratified over **pitches**, so the same pitcher appears in training and test. The model may be learning *"this particular man's slider looks like this."* The only generalisation check reported is across **handedness** (<1% difference), which is not the same thing. **Consequence, and it is the practically important one:** the result does **not** establish a league-wide "pitchers tip with their heads" phenomenon. It is consistent with **119,561 pitches' worth of individual, pitcher-specific tells averaged together** — which is exactly why **the check in §6.3 must be run on YOUR pitcher and cannot be replaced by reading this paper.**

**⚠️ AND A MEASUREMENT CAVEAT THE PAPER UNDERSELLS.** Automated event detection, validated on 156 pitches from 13 pitchers: **release is excellent (mean error 9.6 ms, 90.7% within ±10 ms), but foot plant is 46.9 ms (only 22.1% within ±10 ms) and MER is 46.5 ms (31.4%).** Roughly two-thirds of the importance is aggregated at two events located, on average, **~47 ms off**. Whatever noise that adds is noise **against** the finding, so the direction is conservative — but the per-event importance breakdown should not be read finely.

**⚠️ AND A CLASSIFIER IS STILL NOT A HITTER.** 229 features, full pre-release sequences, hindsight labels, a workstation. A hitter has ~150 ms and no labels. **The paper bounds what is PRESENT in the signal; nothing in it bounds what a hitter extracts.** That absence is F-461 #6 and is unchanged by the primary read.

## 6. 🧮 DETECTION — what it would cost to test any of this

Conventions follow `F-289` / `F-449`: α = .05 two-sided, power .80, $(z_{\alpha/2}+z_\beta)^2 = 7.849$; session clustering handled by a design effect $\text{DEFF} = 1 + (m-1)\rho$ with $m = 30$ pitches/bullpen.

### 6.1 Detecting a 2-inch improvement in mean radial miss

$n_{\text{per condition}} = 2 \times 7.849 \times \sigma^2 / \Delta^2$, then × DEFF.

| Within-pitcher location SD σ | Raw n / condition | × DEFF (ρ = .05, = 2.45) | **Total pitches** |
|---|---|---|---|
| 6 in | 141 | 346 | **692** |
| **8 in** | **251** | **615** | **1,230 ≈ 41 bullpens** |
| 10 in | 392 | 961 | **1,922** |

⚠️ **σ is bracketed because the corpus does not hold it.** "No measured pitch-location distribution for an 85+ arm" has been an open `INDEX.md` gap since 2026-09-11. **This is the twelfth detection table in this corpus blocked by a number that is already in every program's TrackMan log** (after F-264, F-289, F-295, F-307, F-320, F-336, F-348, F-363, F-385, F-396 and the friction SD).

### 6.2 Detecting a change in location SD itself

Two-group comparison of $\ln s$, $\mathrm{Var}(\ln s)\approx 1/2(n-1)$:

| Effect | Raw n / condition | × DEFF | **Total** |
|---|---|---|---|
| **10% SD reduction** | **708** | 1,735 | **3,470 — not affordable** |
| 20% SD reduction | 159 | 390 | **780 ≈ 26 bullpens** |

### 6.3 ⭐ Detecting a gaze/head TIPPING tell — and this one is cheap

Freeze-frame classification, blind grader, two pitch types, chance = 0.50:
$n = 7.849 \times p(1-p)/(p-0.5)^2$

| Grader accuracy to detect | **Frames needed** |
|---|---|
| 60% | **189** |
| **65%** | **80** |
| 70% | **42** |

With three pitch types (chance 0.333), detecting 50%: **71 frames**.

> **80–190 freeze-frames is two to four bullpens of phone video.** It is **15 to 45 times cheaper** than the cheapest command test in §6.1, and it tests a question with a real mechanism behind it.

### 6.4 What the detection arithmetic says, plainly

**A gaze intervention's effect on command is not detectable at the scale a college program operates at**, unless the effect is enormous (a 20%+ cut in location SD). Anyone — a coach, a vendor, a pitcher — who reports seeing a quiet-eye or target-focus effect **in a bullpen** is reading noise. One bullpen of 30 pitches has roughly **2–4% power** against a 2-inch mean shift at σ = 8.

---

## 7. What a coach actually does with this

1. **Do not run a quiet-eye block.** The mediator is measured with a criterion twice the width of the strike zone (§2), the mechanism it proposes is unavailable at 60 ft (§3), the one manipulated throwing test is negative (§4.4), and you could not detect the effect if it were there (§6.1).
2. **Do not stop telling him to look at the target either.** Nothing here says looking at the glove is *harmful*, and §2's argument cuts both ways: because the criterion is loose, the published nulls are also weak. **The defensible position is agnostic**, exactly as F-192 concluded about feedback frequency.
3. **Do run the tipping check (§6.3).** Cheap, fast, binary, and it tests the one gaze-adjacent claim with a plausible mechanism and a **source-verified** 119,561-pitch dataset behind it. **And it cannot be replaced by reading that paper**, because the paper has no held-out-pitcher evaluation (§5.1) — whatever it found is consistent with many individual tells averaged together, so the only way to know about *your* pitcher is to look at *your* pitcher.
4. **The head-position claim that survives is mechanical, not visual.** The industry line (Driveline, §8.3) — *"gaze tracking studies don't show that locking the eyes on the target has anything to do with throwing strikes, but pulling the head off line prematurely will vary the release point"* — is consistent with everything in this file. **It relocates the finding from the eyes to the neck and trunk.** Whether it is true is a separate question and is unverified.

---

## 8. Field sweep, 2026-09-23

### 8.1 ⭐ ✅ SOURCE-VERIFIED — **xCTRL**, Ludwig M, Brill RS, Wyner AJ, **arXiv 2508.19184v1** (26 Aug 2025), read in full
*Separating Intent from Execution: A Probabilistic Approach to Pitch Location Accuracy.* Brill and Wyner are Wharton statisticians; standing high.

**Method, at source.** Statcast via `pybaseball`, **every regular-season pitch 2008–2023**; analysis against Stuff+/Location+ on **2021–2023** (2020 excluded, COVID). Each pitch binned by **pitcher × pitch type × batter handedness × season**, with a **minimum of 250 pitches per bin**. Within a bin, fit a **Gaussian mixture by EM**, each component being *"a unique target the pitcher likes to aim at"*, component weights being how often he goes there. **K is not fixed:** `K = K(x)`, tuned over **K ∈ {1,…,6}** by **validation-set log-likelihood** on a random train/validation partition. Location outliers are removed by the **1.5·IQR rule before fitting**, but are still **scored** afterwards. xCTRL is then the **posterior-weighted distance from the observed location to the inferred target centres** — the posterior update using the actual location is what lets it estimate intent per pitch rather than per bin.

**✅ IT IS A REAL AND CAREFUL PIECE OF WORK, AND IT ATTACKS THE RIGHT PROBLEM.** Its stated premise is the corpus's own: *"it is impossible to directly observe where a pitcher was trying to throw a given pitch"*, and Location+/Command+ *"assume all pitchers share common location goals for each pitch type."*

> ### 🚨 THE CIRCULARITY OBJECTION SURVIVES THE PRIMARY READ — the paper's K-selection does not answer it
> This cycle raised the objection before reading: **the target is inferred FROM the pitcher's own location distribution and the deviations are then measured AGAINST that same distribution**, so a wild pitcher gets **wide components** and can score a **small** distance-to-target. The paper's answer to component count is **validation log-likelihood**, which selects the K that best **describes** the location cloud. **That is the same quantity the command score is built on, so it cannot break the loop — it optimises it.** No simulation study, and no validation against a *known* target (e.g. tagged catcher setups, or a bullpen with a declared target), was located in the paper.
> **The 1.5·IQR pre-fit outlier removal partially mitigates this** — the wildest pitches do not widen the components — and that is a point in the paper's favour that this corpus did not anticipate. **It does not close the objection**, because the IQR rule trims the tail, not the bulk.

**⚠️ AND THE NEAR-TAUTOLOGY STANDS.** xCTRL is reported as more predictive of **FIP, IP, BB/9 and WHIP** than Location+. **Predicting BB/9 from a location metric is close to definitional — a walk IS four out-of-zone pitches — and WHIP inherits it. The FIP and IP results are the ones that carry information.**

**VERDICT: PROMISING, source-verified, and the most useful measurement advance located in months. Two named checks for whoever uses it: (a) how does xCTRL behave on a simulated pitcher whose scatter is widened with intent held fixed? (b) does it beat Location+ on FIP alone, with BB/9 and WHIP set aside?**

### 8.2 ⭐ **Driveline, "The Interaction of Biomechanics and Command" (Feb 2026)** — **PROMISING, UNREAD**
`drivelinebaseball.com/2026/02/the-interaction-of-biomechanics-and-command/`. Snippet reports this is the write-up behind Driveline's **2025 SABR Dr. Mike Marshall Pitching Biomechanics Research Award**, for research into the **biomechanics of command**. **Domain is blocklisted; no methods, no sample, no numbers retrieved.** Given the corpus's standing "no bullpen-to-game command transfer study" gap, this is now a **top-three verification-queue item**.

### 8.3 **Driveline's gaze claim** — **UNPROVEN, and it is the industry's own null**
Snippet, source page unread: *"gaze tracking studies don't show that locking the eyes on the target has anything to do with throwing strikes"* — called *"another myth"* — paired with *"pulling the head off line prematurely will vary the release point and screw up a finely-tuned sense of proprioception,"* attributed to improper glove-arm deceleration pulling the cervical spine off line. **A high-standing industry source asserting a null that agrees with §2/§3, with no study cited.** Verdict: UNPROVEN as stated, and **useful mainly as evidence that the field is not actually arguing for the quiet-eye position.**

### 8.4 **"Command training balls of varying size and weight"** — **MARKETING-ADJACENT, watch**
Snippet from a 2026 industry piece: command is *"both under-researched and undervalued"* and variable size/weight balls *"fit this bill perfectly,"* with researchers planning to *"investigate further."* **A stated intention to investigate is not a result.** This is the differential-learning idea (F-~193 lineage) with a product attached. Verdict: **UNPROVEN**, and flagged because the phrasing is the shape a magnitude gets invented around.

### 8.5 **Noah Woodward, "Targets matter," The Advance Scout** — **PROMISING as a hypothesis, no data retrieved**
Argues the catcher's setup is not a formality — with examples of 3-0 setups and Willson Contreras setting up nearly on the batter's-box line to invite a fastball off the plate. **Relevant because it is the hitter-facing half of §5: if the target itself carries information, the tipping channel includes the catcher.** Substack is blocklisted; no numbers.

### 8.6 **Command+ for the 2026 Prospect League** — logged, not assessed
`cornbeltersbaseball.com`, a summer-league command metric build. Independent-league, unread, no methods. **Logged only so a later sweep does not treat it as new.**

### 8.7 Things looked for and NOT found — said plainly rather than padded
- **No gaze study of any kind on a pitcher above the n = 3 abstract.** Not in baseball, not in handball, not in cricket bowling.
- **No 2026 industry argument about pitcher gaze.** The searches returned batter-side gaze content (Driveline has three articles on *hitters'* gaze and none on pitchers'), vision-training marketing, and youth coaching pages. **The field is not debating this. That is part of why it was a gap.**
- **No bias-corrected quiet-eye meta-estimate.** Searched specifically; the critique literature that exists (a *"Say it quietly, but we still do not know how Quiet Eye training works"* comment on Vickers; a *"Quiet Eye: Origins, Controversies, and Future Directions"* review) is **mechanistic criticism, not a bias re-analysis.** The re-analysis that was run on external focus (F-189) and on OPTIMAL theory (F-190) **has not been run on quiet eye.**

---

## 9. Hazard log for this file

- **🚨 THE CYCLE'S OWN LARGEST ERROR was declaring a reading blockade without probing the object stores** `INDEX.md` §0 documents. Corrected mid-cycle; **three primary texts were then read in full.** Registered as **F-462**. *"WebFetch is blocked"* ≠ *"this cycle cannot read papers."*
- ✅ **SOURCE-VERIFIED: §4.4 (PMC7739699), §5 (arXiv 2603.04874), §8.1 (arXiv 2508.19184).**
- ⚠️ **STILL SNIPPET-ONLY: §4.1 (Kuchmaner, no PMCID/arXiv ID exists), §4.2 (ECU thesis, unidentified), §4.3 (Lebeau 2016 — NOT in the PMC OA subset), §4.5 (NCT04289376), §8.2–§8.6.**
- **§2, §3 and §6 are arithmetic and stand on their own.** They are the only content here that never depended on a source. **Note that §2's darts row (2.4 m, 34 cm board) was independently confirmed by the source read of PMC7739699 (2.37 m, 34 cm WDF board).**
- **The 1126.88 ms figure (§4.1) remains UNVERIFIED and is probably a mis-paraphrase.** Do not import it.
- **The 19.0% head/eye figure is now SOURCE-VERIFIED (§5), and the search summary's RANKING was inverted.** The paper says head joints are *higher than any single limb group*; the summary said wrist was highest. **Third documented instance of search-summary corruption in this corpus.**
- **Dispute #38's original form is DEAD** (trunk carries 5.3%, head 19.0%) and **its amended form is alive**: gain-based importance with **no leave-one-joint-out ablation**.
- **arXiv 2603.04874 has NO held-out-pitcher evaluation.** Do not read it as a league-wide phenomenon; it is consistent with many individual tells averaged.
- **§2's window÷target ratios assume the athlete fixates the target's centre and that eye-to-target distance ≈ nominal task distance.** Approximations; neither moves a ratio by more than ~15%, against a pitching-vs-putting gap of a factor of 5.
