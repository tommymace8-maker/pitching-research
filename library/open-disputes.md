# Open Disputes
### Arguments among the biomechanist, the anatomist, and the coach that are NOT resolved

**Started:** 2026-08-12 · **Status:** living. Disputes get added, escalated, or **RESOLVED/CONCEDED** with a date and a reason. Nothing gets quietly deleted.

> **Ground rule (from `README.md`):** manufactured consensus is a failure state. An honest open dispute is more useful than a fake answer. Each entry states what each side claims, the strongest evidence each way, and **what would settle it.**

**Status key:** 🔴 OPEN · 🟡 NARROWED · ✅ RESOLVED · ⬜ CONCEDED (one side yielded)

---

## Index

| # | Dispute | Parties | Status |
|---|---|---|---|
| 1 | Are the four "free" torque reductions actually modifiable? | Biomech vs Coach | 🟡 NARROWED |
| 2 | Is elbow flexion at FC an independent variable or just "arm path"? | Coach vs Biomech | 🔴 OPEN |
| 3 | Can mechanics decouple velocity from varus torque *within* an individual? | Anatomy vs Biomech vs Coach | 🔴 OPEN — the central question of the program |
| 4 | Force plates vs. modeled torque — what should we buy and what should we believe? | Biomech vs Coach | 🟡 NARROWED |
| 5 | Is there a dugout-measurable posterior-cuff activation marker? | Anatomy vs Coach | 🔴 OPEN |
| 6 | Does "vary your effort" actually reduce load, or just reduce velocity? | Coach vs the 2026 literature | 🔴 OPEN |
| 7 | Is the lead-leg block worth coaching given that it *raises* torque? | Coach vs Biomech | 🔴 OPEN |
| 8 | Weighted implements in a mature 85+ arm | Anatomy vs the field | 🔴 OPEN |
| 9 | Does the "block whips the hips" model deserve full retirement? | Coach vs Biomech | 🟡 NARROWED |
| 10 | Lower arm slot — universal recommendation or individual? | Coach vs Biomech | 🟡 NARROWED |
| 11 | The kinematic sequence | Coach vs Biomech | ⬜ **CONCEDED by the coach, 2026-08-12** |
| 12 | **Does the velocity-optimal delivery cost command?** | Command data vs Velocity data | 🔴 **OPEN — added 2026-08-13; revisited same day** |
| 13 | **Is stride length a velocity LEVER, or only a CORRELATE?** | Coach vs velocity report | 🔴 **OPEN — added 2026-08-13. Two failed manipulations** |
| 14 | **Is "keep lifting = floor protection" a real asymmetry or a design artifact?** | Coach vs velocity report | ⬜ **LARGELY RESOLVED, coach's favour, 2026-08-13 — Gdovin is an UNCONTROLLED pre-post, not a removal trial.** Underlying physiology still open |
| 15 | **Is spin efficiency trainable, and does the industry price the cost honestly?** | Coach vs the pitch-design industry | 🔴 **OPEN — added 2026-08-13** |
| 16 | **Does release-angle precision have any coachable channel?** | Coach vs stuff/command report | 🔴 **OPEN — added 2026-08-13** |

---

## 1. 🟡 Are the four "free" torque reductions actually modifiable in an 85+ arm without velocity loss?

**Biomechanist's position.** Four variables raise normalized elbow varus torque without contributing to velocity in the two elite regressions: shoulder abduction at FC (too high), elbow flexion at FC (too high), shoulder abduction at BR (too low), and an early pelvis peak. These are the closest thing the literature offers to free lunch. *(biomechanics.md §6.4)* He asked the coach which one is actually modifiable.

**Coach's answer, ranked by real-world modifiability:**

| Variable | Modifiable? | Why |
|---|---|---|
| **Shoulder abduction at FC** | **Most modifiable.** | It is a *position at a landmark I can freeze on video*, it lives in the stride phase (Rule 2 — enough time to organize), and I have a felt cue and a constraint for it. This is my answer to the biomechanist: **start here.** |
| **Later pelvis peak** | Modifiable indirectly | Not as a timing instruction — nobody can feel 15 ms. Modifiable only through its upstream causes: lead-hip IR availability, thoracic rotation, front-foot landing angle. |
| **Shoulder abduction at BR** | Barely | BR is inside the 30–50 ms acceleration window. I can only change it by changing trunk lateral tilt, which is itself a *positive* torque contributor. **Likely a wash.** |
| **Elbow flexion at FC** | Least — see Dispute #2 | |

**Coach's standing objection.** All four come from a model explaining **40% of normalized-torque variance**, cross-sectionally, with **zero intervention trials**. "Free" is a property of a regression coefficient, not of a bullpen. In a real athlete these variables covary — you cannot move one and hold the others.

**What would settle it.** A within-subject intervention: 20–30 pitchers at 85+, baseline mocap, 8–12 weeks of targeted coaching on shoulder abduction at FC only, re-test kinetics and velocity. Nobody has run it. **This is the single highest-value study that could be run in this field and it is cheap.**

---

## 2. 🔴 Is elbow flexion at FC an independent variable, or is it just "arm path" wearing a number?

**Biomechanist's position.** It's a listed positive contributor to normalized elbow varus torque with no velocity benefit. Pro norm 93–101° at FC.

**Coach's position.** It is not a dial. Elbow flexion at FC is downstream of arm path, hand position, forearm alignment, and pitch grip. Cue it directly and you change slot and pitch shape as collateral damage. **I will not cue it**, and I suspect the regression coefficient is partly capturing "long arm action vs short arm action" — a construct nobody has cleanly operationalized.

**Strongest evidence for the biomechanist.** It survived as an independent contributor in a multivariate model alongside shoulder abduction at FC, so the model at least nominally separates them.

**Strongest evidence for the coach.** Max elbow flexion at MER in pros is 89–90° and elbow flexion at FC is 93–101° — the elbow arrives at FC essentially at its peak-load position and barely moves. That says the FC value is a *consequence* of how the arm got up, not an independent choice.

**What would settle it.** Partial-correlation or mediation analysis in the ASMI dataset: does elbow flexion at FC predict torque after controlling for arm slot, arm-path length, and shoulder abduction at FC? If the coefficient survives, I'm wrong.

---

## 3. 🔴 Can mechanics decouple velocity from varus torque *within* an individual? — **the central question of the program**

**Anatomist's framing** (his Open Question #1): the population-level velocity–torque correlation is strong, but the residual — pitchers who throw 95 at below-expected torque — is where all coaching leverage lives, and it is poorly characterized.

**Biomechanist's data, which cuts both ways.**
- *Against decoupling:* within a single pitcher, velocity and elbow varus torque are locked at **R² = 0.957** (Slowik 2019, n=64 pro). When *you* throw harder, *your* elbow load rises, near-linearly.
- *For decoupling:* across elite arms, the high-torque and low-torque groups differed **28% in normalized torque for a 1% difference in ball velocity** (Fleisig 2025, n=523). And Crotin et al. (2022, n=545) formalized "biomechanical efficiency" = velocity per unit normalized torque as a real, measurable, varying quantity.

**Coach's answer, which is the one I'll defend to an athlete:**
> These two findings are not in conflict, and the reconciliation is the whole job. **R² = 0.957 describes a fixed delivery.** Along *this* delivery's curve, more velocity costs more torque, always. **The 28% gap describes different curves.** Coaching does not move you along your curve for free — it moves you to a different curve, and *then* you re-apply effort along the new one.

**Why it stays OPEN.** Nobody has demonstrated a within-athlete *curve shift.* Every piece of evidence for the 28% gap is between-subject and cross-sectional. It is entirely possible the gap is anthropometry, tissue quality, and humeral torsion — things you cannot coach — rather than mechanics. **60% of normalized torque variance is unexplained by kinematics**, and I would not bet that the unexplained 60% is coachable.

**What would settle it.** Longitudinal tracking of individual efficiency (velocity ÷ normalized torque) across a development block, in the same lab with the same filter settings, in athletes who gained velocity. Does anyone's efficiency ratio actually improve, or does everyone just slide up their own fixed curve? Driveline and every MLB org have the data to answer this. It is not public.

---

## 4. 🟡 Force plates vs. modeled torque

**Biomechanist asks:** can we get force plates, since GRF is directly measured while torque is always modeled?

**Coach's answer: yes, buy them — and I'll go further than you did.** Two reasons beyond your own:
1. **Dowling, Slowik & Fleisig (2026)** now demonstrate that sample and filter frequency choices materially change computed pitching data (published studies span 240–500 Hz sampling; 13.4 and 18.0 Hz are the common filter cutoffs). Inverse-dynamics torque depends on the second derivative of position, so filter choice is a large fraction of the answer. **This is the mechanism behind our unresolved 64 vs 100 vs 120 N·m spread, and it means the whole torque literature is less comparable than it looks.** GRF has no such problem.
2. Force plates measure the thing I can actually train — lower-half force production and braking — and they measure it *in the athlete's own units*, which is what §Rule 3 says is the only defensible use of measurement anyway.

**Where I push back.** GRF being directly measured does not make it *relevant*. After controlling for bodyweight, lead-leg GRF explains **~4–6% of between-pitcher velocity variance** (r = 0.23 vertical, 0.19 A-P). A directly measured variable that explains 5% of the outcome is not obviously better than a modeled variable that predicts UCL surgery (HR 1.26 per 10 N·m). **Precision and importance are different things**, and force plates are frequently sold as if they were the same.

**Remaining dispute.** The biomechanist's own file flags that **braking impulse in %BW·s — the mechanically meaningful quantity — has no published elite norms.** So we would be buying an instrument to measure a variable for which no reference values exist. That's fine for within-athlete tracking and useless for evaluation. Say so when you write the purchase order.

**What would settle it.** Published elite braking-impulse norms in %BW·s, and a within-athlete study showing that improving braking impulse improves velocity or efficiency.

---

## 5. 🔴 Is there a dugout-measurable marker of posterior-cuff activation deficit that fires before command drifts?

**Anatomist asks this** (his Open Question #3). His own evidence: pitching-induced fatigue produces a **voluntary activation deficit of the infraspinatus** measured by interpolated twitch — a neural inhibition, not a muscle-condition problem — and the coach-observable fatigue hierarchy runs **command drift → breaking-ball finish → slot drop → longer between pitches → velocity last.**

**Coach's honest answer: no, not one that's validated. Here are the three candidates and why each is inadequate.**

| Candidate | Case for | Why it isn't the answer |
|---|---|---|
| **Handheld dynamometry ER strength between innings** | HHD is reliable for shoulder ER; preseason ER weakness is associated with in-season injury and subsequent velocity loss; post-game ER strength drops ~11% | Nobody has established a *between-innings* protocol, a minimal detectable change for this use, or shown it moves before command does. And the act of a maximal ER contraction between innings is itself a load |
| **Grip dynamometry** | $60, 5 seconds, and it indexes the flexor-pronator load-sharing that the anatomist says is the whole UCL safety margin | It's a *forearm* marker, not a posterior-cuff marker. Answers a different question — a good one, but not his |
| **Slot drop on video** | Free, already happening, and it *is* in the fatigue hierarchy | It fires **after** command drift, which is exactly what he asked us to beat |

**Where the coach pushes back on the anatomist.** The request may be malformed. If the deficit is **central/neural voluntary activation**, then any field test requiring a maximal voluntary contraction is measuring the same inhibited system with a cruder instrument — it will be noisier than the pitcher's own performance, which is a 100-repetition-per-outing readout. **The best available marker of a pitcher's arm may just be the pitcher.** I would rather formalize the observation ladder (ATC charts arm-side miss rate and breaking-ball finish by inning) than chase a number.

**What would settle it.** A study measuring interpolated-twitch infraspinatus activation and a candidate field test (HHD ER, or a rate-of-force-development ER test) at innings 1/3/5/7 in collegiate starters, with per-pitch command tracking. Does the field test cross a threshold *before* command degrades? That study is feasible today and does not exist.

---

## 6. 🔴 Does "vary your effort" reduce load, or mostly reduce velocity?

**Fleisig's 2026 position** (*Sports Biomechanics*): varying effort instead of maximum effort on every pitch may both reduce UCL damage and improve performance by disrupting hitter timing.

**The three primary datasets disagree with each other.**
- Fiegen 2023 (n=10 HS `[OFF-POPULATION]`): 75% effort → 81% of stress, 90% of velocity. **−13% stress per 25% effort reduction.**
- Wolf 2025 (n=19 collegiate): 100% vs 60% → 92.5 vs 73.2 N·m; **kinematics unchanged** at all levels.
- Hyeamang 2026 (n=38 HS + 24 pro): at 50% RPE, HS threw **86% of velocity and 75% of max torque**. Pros far more consistent.

**Coach's position.** The strategy is defensible; the *load-reduction* arithmetic is poor. Half effort buys roughly a quarter less torque. There is no dosing here that yields a big stress cut at a small velocity cost, and in the amateur half of this population the perception is so badly calibrated that "throw easier" can expose healing tissue to more load than the rehab plan assumed.

**Where all three of us disagree.** Wolf says kinematics are *preserved* at 60%; Hyeamang says HS pitchers are *highly variable* at submaximal effort. If Wolf is right, submaximal work is a clean training stimulus. If Hyeamang is right, submaximal work in a young arm is a different, sloppier movement — which is a motor-learning problem on top of a load problem.

**What would settle it.** The Wolf protocol (five effort levels, full kinetics *and* kinematic variability) run on a strictly 85+ sample with n > 50, reporting within-subject variability at each effort level. Note the levels differ too — Wolf found significance only at 100 vs 60, i.e. the intermediate steps did nothing measurable.

---

## 7. 🔴 Is the lead-leg block worth coaching, given that it raises torque?

**The conflict, stated plainly from the biomechanist's own conflict table:** max knee extension velocity during arm acceleration is a **positive** contributor to normalized elbow varus torque, *and* front-knee extension correlates with velocity (r = 0.25–0.29). It is a direct trade, not a free lunch.

**Coach's position.** Coach it, and name the price out loud. My reasoning: the block is one of the few velocity levers that is genuinely trainable in the weight room (eccentric quad strength, RFD) rather than requiring a mechanics change; and block quality is one of the first things to degrade under fatigue, so training it also buys durability of *everything upstream* late in outings.

**Biomechanist's likely counter, which I can't fully answer.** The bodyweight-controlled correlations are r = 0.23 vertical / 0.19 A-P — **4–6% of velocity variance.** I am asking an athlete to accept a measured torque increase to chase 5% of the between-pitcher velocity variance.

**Coach's counter-counter.** Between-pitcher variance is the wrong denominator. Within an athlete, "does his block hold at pitch 75" is a much bigger swing than 5%.

**What would settle it.** Within-athlete: does a training block that measurably improves braking impulse and knee-extension velocity produce (a) more velocity, (b) more torque, and (c) what's the ratio? Force plates plus a sleeve could get a usable answer at a private facility inside one off-season. **This is the most tractable open dispute on this list.**

---

## 8. 🔴 Weighted implements in a mature 85+ arm

**Anatomist's position.** Reinold 2018: 6-week weighted-ball program, **24% injury rate vs 0% control**, with olecranon stress fractures and UCL injuries — and the 3.3° ER "gain" is best read as acquired laxity, not mobility. ⚑ HS-aged sample. He notes professional survey data (IJSPT 2025) has not reproduced the signal, and calls the divergence an open question.

**The field's position** (circulating widely in 2026): O'Connell et al. 2022, n=26 collegiate/pro, five ball weights — elbow varus torque and shoulder IR moment statistically unchanged across implement weights.

**Coach's position: the field is quoting a concentric-phase study to settle a deceleration-phase and cumulative-load question.** O'Connell measured the acceleration phase. The injuries in Reinold were olecranon stress fractures (cumulative bone loading) and UCL tears (cumulative ligament loading). **A single-session acceleration-phase study cannot speak to either.** The paper also doesn't specify plyoball vs hard leather — a distinction that changes both the deceleration demand and the grip.

**Where I side with the field.** The 24% figure indicts *that protocol in that population* — HS-aged arms, six weeks, fixed progression. It does not indict a supervised, individualized implement block in a mature 85+ arm. But the burden of proof sits with the intervention.

**What would settle it.** A prospective study in a strictly 85+ population, randomized, with *deceleration-phase* kinetics and cumulative workload tracked (sleeve or equivalent), 12+ weeks, injury outcomes. It has not been run and probably won't be, because nobody wants to be the arm in the control group or the arm in the injury group.

---

## 9. 🟡 Does "the block whips the hips" deserve full retirement?

**Biomechanist:** yes. Pelvis rotation change FP→BR and pelvis rotational velocity gain both correlate **r = −0.07** with velocity across 800+ force-plate sessions. The block works by decelerating the COM and extending the knee.

**Coach:** I've retired the cue, and I'm keeping it retired. But I want to narrow the claim before it hardens into library dogma, because a null correlation is not a null mechanism:

1. **A between-subject correlation of −0.07 does not mean pelvis rotation is unimportant.** It may mean pelvis rotation *gain after foot plant* is uniformly present in a population where everyone already blocks — a restricted-range problem. Every athlete in that dataset was a trained thrower.
2. **The bodyweight-controlled value is 0.10, and the raw is −0.07.** Two nominally different signs on a variable this weak means the honest reading is "indistinguishable from zero," not "negative."
3. This is **one industry R&D dataset, not peer-reviewed.** It's a good one and it's the biggest force-plate sample in public, but a single unreplicated source retiring a century-old coaching model deserves a second look.

**Agreed between us:** the *cue* is dead, because it describes a mechanism that isn't doing the work. **Not agreed:** whether pelvis rotation after foot plant is genuinely irrelevant or merely uniform in this population.

**What would settle it.** Replication in a second independent force-plate dataset, and — better — a within-athlete analysis: on a given pitcher's harder pitches, does pelvis rotation gain rise?

---

## 10. 🟡 Lower arm slot — universal or individual?

**Biomechanist:** in professionals, +10° of slot (lower/more sidearm) associates with −0.1 %BW×BH in both elbow varus and shoulder IR torque; pros sit lower than high schoolers (58 ± 14° vs 50 ± 11°). Now corroborated: ~4.23 N·m less varus torque per 10° at consistent velocity in 66 elite college pitchers (*Sports Biomechanics* 2024/25), and MLB field data showing ~4% torque reduction per 10°, +2.14 run value and +18.3 rpm for slot-droppers, at a cost of ~0.15 mph.

**Coach: I accept the direction and dispute the universality.** Three specific limits:
1. **It inverts at the HS level** — in high schoolers, lower slots associated with *higher* elbow flexion torque. Our population's floor (85 mph HS prospect) sits astride that inversion and we do not know which side of it he's on.
2. **It requires wrist radial-deviation mobility** to hold spin efficiency at the new slot. Skenes tried it and reverted.
3. **The most common way a coach "lowers a slot" is by adding trunk lateral tilt** — which is itself a *positive* contributor to elbow varus torque. Executed wrong, the intervention costs torque instead of saving it. **This is the failure mode that would make a good finding harmful in the field.**

**What would settle it.** A within-athlete intervention: 15–20 elite pitchers coached to drop slot 5–10°, with pre/post kinetics *and* trunk lateral tilt at BR measured, so we can separate "changed arm path" from "leaned over."

### 🔄 REVISITED 2026-08-13 — moved further toward "individual." Two new inputs.

**(a) The effect is PLATOON-DEPENDENT.** Davy Andrews, FanGraphs, 27 Nov 2024, ["An Arm Angle Update That Ends With a Mystery"](https://blogs.fangraphs.com/an-arm-angle-update-that-ends-with-a-mystery/): **lower arm angles perform better against same-handed batters; HIGHER arm angles perform better against opposite-handed batters.** Same-sided correlations: arm angle→wOBA .13, →xwOBA .23; velocity −.18. Andrews flags an anomaly he cannot explain — every metric correlated better with xwOBA than with actual wOBA — and says so in print, which is worth crediting.

**(b) Slot changes propagate into SPIN EFFICIENCY and PRONATION TENDENCY, not just VAA and torque.** Michael Rosen, FanGraphs, 13 Apr 2026: Emerson Hancock dropped arm angle **23° → 13°** and moved his landing crossbody; Driveline's Spenser Davis: the crossbody landing *"cut off his tendency to pronate."* His four-seam spin efficiency fell from 99% — **and that was good for him**, because it unlocked a glove-side breaking ball (2.38 FIP, 30.6% K%). Connor White: *"The arm is not one fixed lever."*

**(c) And the command cell filled in.** `stuff-and-command.md` §7 — Manzi et al. 2021, n = 338 professionals, **velocity-matched (p = .055): the plus-command group sat at a HIGHER arm slot** (59.7° vs 54.7°, p = .009). **The lower-slot arms are the ones with worse command.**

**Narrowed conclusion (coach and biomechanist now agree on this wording):**
> **Lower slot is a same-handed weapon that reshapes the entire arsenal — not a universal upgrade.** It is contraindicated for a pitcher facing predominantly opposite-handed hitters, and possibly for a pitcher whose value is command. **Slot is not a dial. It is a package, and the package includes his pronation tendency and his platoon splits.**

**Status: still 🟡 NARROWED.** The within-athlete intervention above is still what would settle it — **and it now needs two more outcome measures: spin efficiency and split-by-batter-handedness run value.**

---

## 11. ⬜ CONCEDED — the kinematic sequence (coach yields, 2026-08-12)

**Coach's intended attack:** the biomechanist's claim that the textbook proximal-to-distal sequence was never observed on a single pitch rests on **n = 14** (4 HS, 8 collegiate, 2 pro). Too small to retire a century of coaching.

**What I found on the field sweep, against my own position:**
- **Scarborough et al. (2020), *Sports Biomechanics* 19(5):** n = 22 pitchers, **208 pitches, 14 distinct sequence patterns, not one fully proximal-to-distal.** Fewer than 10% of pitchers used a single pattern. **Sequence variability was similar in high-school pitchers and professionals** — so it is not a skill marker.
- A further sample: 30 pitchers, 249 fastballs, **17 patterns.**

**Concession.** Three independent samples, ~50 pitchers, 600+ pitches, three different labs, same result. **"Fix your kinematic sequence" as a discrete binary intervention is retired.** It is in `coaching-translation.md` §9.

**What survives the concession, and I want this on the record:** the *proximal end* is still real. Trunk-reaching-peak-velocity-before-pelvis increases shoulder and elbow torques (Aguinaldo & Escamilla 2019), and later pelvis peak associates with lower normalized torque. **The disorder is distal — arm, forearm, hand ordering.** So the coachable claim narrows from "sequence your delivery" to **"don't let your chest beat your hips to foot strike"** — one specific, upstream, screenable failure. That claim stands.

---

## 12. 🔴 Does the velocity-optimal delivery cost command? — **added 2026-08-13**

**This is the sharpest direct contradiction in the library, and until now nobody had put the two datasets on the same page.**

### The two positions

**The velocity literature says: get out over the front side.**
In the professional velocity model (n = 337 pro, 3,627 fastballs, adj. R² = 0.536), **trunk flexion at ball release is the single strongest kinematic predictor of velocity — β = 1.829**, with a stated effect of **+10° ≈ +3.71 m/s (+8.3 mph)**. Trunk lateral tilt at BR is part of the same "get out over it" complex and is a positive contributor to elbow varus torque. *(`biomechanics.md` §3.5, §6.2)*

**The command literature says: stand taller and stop leaning.**
**Manzi, Dowling, Wang, Arzani, Chen, Nicholson & Dines (2021), *J Orthop* 27:28–33 (PMID 34475727).** **n = 338 professional pitchers** (MLB and Low-A→AAA), split into high-consistency (n = 91) and low-consistency (n = 98) by location spread at ±0.5 SD, normalized to grid width; 8–12 fastballs each; marker-based mocap at 480 Hz.

| At ball release | Plus command | Wild | p |
|---|---|---|---|
| **Trunk flexion** | **11.9 ± 10.0°** | 15.9 ± 9.0° | .005 |
| **Trunk lateral flexion** | **−27.1 ± 9.3°** | −31.8 ± 9.0° | **<.001** |
| **Trunk tilt** | **−33.4 ± 9.1°** | −37.2 ± 8.9° | .004 |
| **Arm slot** | **59.7 ± 13.5°** | 54.7 ± 12.4° | .009 |
| Shoulder distraction force | 112.4 ± 15.9 %BW | 118.3 ± 15.1 %BW | .001 |

**The critical design feature: velocity did NOT differ between groups (p = .055).** This is a genuine command contrast, **not** a velocity confound — which is exactly what makes it hard to dismiss.

**So the conflict, stated without hedging:** every degree of forward and lateral trunk tilt that the velocity model rewards is a degree the command data penalizes, **in the same population, at the same velocity, at the same landmark.**

### And it is worse than two-way — the arm slot squares off against itself

| Variable | VELOCITY | COMMAND | ELBOW TORQUE |
|---|---|---|---|
| Trunk flexion at BR | **↑↑** (β = 1.829) | **↓** (11.9° vs 15.9°) | — |
| Trunk lateral tilt at BR | ↑ | **↓** (−27° vs −32°) | **↑** |
| **Higher arm slot** | Neutral | **↑** (59.7° vs 54.7°) | **↑** in pros |

**The arm-slot cell is a direct collision with Dispute #10.** That dispute concluded lower slot is favorable — ~4.23 N·m less varus torque per 10°, +2.14 run value and +18.3 rpm on the four-seam, at ~0.15 mph. **This new data says the lower-slot arms are the ones with worse command.** Both cannot be costless.

### Mechanism — why the command finding is probably not a fluke

This is not just a correlation; there is a clean physical reason, and it comes from `stuff-and-command.md` §5:

> **1° of release angle = ~30 cm (12 in) of location at the plate.** *(Kusafuka et al. 2020, Front Sports Act Living 2:36 — and the number is pure trigonometry: tan 1° × 54.5 ft = 11.4 in, so it is not sample-dependent.)*

If the release angle is generated by a heavily tilted trunk, then **a small trunk error transmits almost 1:1 into a release-angle error — and 1° is a foot.** The taller, less-tilted delivery is *geometrically less sensitive* to the same perturbation. **That mechanism predicts exactly what Manzi measured**, which is the strongest thing going for the command side.

### Strongest evidence for the velocity side

The β = 1.829 coefficient comes from a larger fastball sample (3,627 pitches) with a real R² (0.536), and the direction replicates across the velocity literature.

**But `biomechanics.md` §3.5 already flagged this coefficient as suspect on its own terms:** +8.3 mph per 10° of forward tilt is an enormous, almost certainly non-causal effect, and forward tilt at release is plausibly a *downstream consequence* of a good lead-leg block and a fast trunk rather than a cause of anything. The library's own verdict was **"a marker of a good delivery, not a lever."**

**If that verdict is right, the conflict partly dissolves** — you were never supposed to coach forward tilt anyway, and the command data is simply a second, independent reason not to.

### Strongest evidence for the command side

Velocity-matched groups (p = .055), n = 338 professionals, a mechanism with exact geometric backing, four trunk variables all pointing the same direction at p ≤ .005, and **independent convergence from a second Manzi paper** (n = 322 pro) in which **trunk tilt at foot contact was the top random-forest predictor in both the accuracy model (6.6%) and the consistency model** — *"four of the top six parameters in both models involved variance at the hip and trunk."* ⚑ That second paper is in a low-tier venue (*Archives of Sports Medicine*, Scholars.Direct) with manually charted locations, so it is corroboration, not proof.

### Weaknesses on the command side, stated honestly

1. **Cross-sectional and between-subject.** Two populations, not one athlete moved.
2. **Command was operationalized as location *spread* around a target grid** — dispersion, not accuracy, and with no intent inference (the §9.1 problem in `stuff-and-command.md`).
3. **The differences are small in absolute terms** — ~4–5° on SDs of 9–10°. **The distributions overlap heavily.** This is a population signal, not an individual diagnostic.
4. **Reverse causation is live.** Pitchers who already command the ball may throw with less effort, and less effort produces less tilt. **The tilt could be a symptom of a controlled delivery rather than a cause of one.** Nothing in the data separates these.

### What would settle it

**The within-athlete study nobody has run.** Take 20–30 pitchers at 85+. Measure trunk flexion and lateral tilt at BR, velocity, **and command with declared intent** (miss distance in inches, not grid spread) at baseline. Coach a targeted reduction in trunk lateral tilt at BR over 8–12 weeks. Re-test all three.

**Three outcomes, three different worlds:**
- Command improves and velocity holds → **tilt is a genuine command tax and the velocity coefficient was never causal.** Coach it out.
- Velocity drops proportionally → **it is a real trade** and every athlete needs an explicit decision about which he is buying.
- Nothing moves → **tilt was a marker of an already-organized delivery**, both literatures were reading a symptom, and the whole dispute was a mirage.

**Power note (from `stuff-and-command.md` §11.4):** with a within-pitcher miss-distance SD of ~10 in, detecting a 2-inch command change needs **~196 tracked pitches per condition** — seven to ten bullpens. **Any version of this study that evaluates command on a single post-test bullpen is uninterpretable**, and so is any coach who declares this trade resolved after one session.

### What the coach should do in the meantime

**Say the trade out loud.** An athlete being pushed toward "get out over the front side" is being pushed toward velocity and **away from** command, and possibly toward more elbow torque. That may still be the right call for a 19-year-old who needs 4 more mph to get drafted. **It is not the right call by default, and it is currently being made by default, silently.**

### 🔄 REVISITED 2026-08-13 — moved slightly toward the "mirage" reading. Still 🔴 OPEN.

Nothing published today tests this dispute directly. Two things nudge it:

**(a) The stride-length collapse weakens the whole "velocity-optimal delivery" construct.** Dispute #13 establishes that the **best-evidenced mechanical velocity lever in the library** — cross-sectional, n = 315 professionals, per-unit mph coefficient, no torque cost — **produced nothing when two independent groups experimentally moved it, and made pitchers slower in one.** If that coefficient was a marker rather than a lever, **confidence that ANY of the cross-sectional kinematic coefficients are causal should drop.** That includes **trunk flexion at BR, β = 1.829 — which IS the velocity side of this dispute**, and which `biomechanics.md` §3.5 had already flagged as implausible at +8.3 mph per 10°. **Same error, one variable over.**

**(b) A fourth axis.** Andrews' platoon finding (Dispute #10) means arm slot has **velocity, torque, command, AND platoon** consequences pointing in different directions depending on who is in the box. The "arm-slot square" is at least a pentagon.

**The coach's answer to "pick one for a real athlete," since somebody has to:**

| Athlete | Pick | Reasoning |
|---|---|---|
| **18–21, needs velocity to be seen at all** | **Velocity-optimal** | A 21-year-old at 88 with plus command is org-filler. At 94 with 12-inch command he gets drafted and then gets three years of professional instruction. **The market prices velocity as an option on future command, and it is right to** |
| **22–25, already 93+, in pro ball, not getting outs** | **Command-optimal** | He is past the window — expected year-over-year change is negative above 93. And 1 inch of miss ≈ 0.3 FIP ≈ a full SD of Stuff+, more than any pitch-design project delivers |
| **88–90 college arm, average command** | **Neither** | **Buy extension, buy slot, buy the missing pitch.** All three are cheaper than either horn of the dilemma and **none requires resolving this dispute.** This is the honest answer and it is the one nobody sells |

**And the coach's caveat, on the record: this dispute may be a mirage.** If β = 1.829 is non-causal — and today's evidence makes that *more* likely — then nobody should have been coaching forward tilt in the first place, and the command data is simply a second independent reason not to. **What certainly exists is a bad cue that two literatures independently flag. Whether a real trade sits underneath it is unproven, and the third outcome in "what would settle it" above — "nothing moves, both literatures were reading a symptom" — has become the most likely of the three.**

---

## 13. 🔴 Is stride length a velocity LEVER, or only a CORRELATE? — **added 2026-08-13**

**The velocity report's position** (`velocity-development.md` §4.4, §7 as originally written): stride length toward ≥80% of body height is **recommendation #2, "the best mechanical lever"** — **+2.0 mph per 10% BH, no elbow-torque cost, n = 315 professional pitchers** (**Manzi JE**, Dowling B, et al. 2021, *J Sports Sci* 39(23):2658–2664, PMID 34240663 — ⚠️ *first author is Manzi, not Dowling; corrected 2026-08-13*. B = 0.089, β = 0.25, p < .001; varus torque n.s. across quartiles, p = 0.072. **Cross-sectional/observational**). Its Open Question #8 asserted that *"nobody has lengthened a professional's stride and measured what happened."*

**The coach's position: the second half is false, and the first half does not survive it.**

### The evidence the library did not have

| Study | n / level | Manipulation | Ball velocity |
|---|---|---|---|
| **Ramsey DK, Crotin RL, White S (2014), *Hum Mov Sci* 38:185–196** ([PMID 25457417](https://pubmed.ncbi.nlm.nih.gov/25457417/)) | 19 (15 collegiate, 4 elite HS) ⚑ | **±25%** of self-selected stride; randomized crossover, 8-camera mocap 240 Hz + 2 force plates, two 80-pitch simulated games, 72 h washout; stride differed **p ≤ .001** | **Hand and ball velocity EQUIVALENT across conditions** |
| **Matsuda T, Hirano A, Umakoshi Y, Kimura A (2025), *Front Sports Act Living*** ([PMID 40264933](https://pubmed.ncbi.nlm.nih.gov/40264933/)) | 20 college ⚑ | **±20%** instructed | **Under 72.7 · NORMAL 75.8 · Over 72.7 mph. His own stride was significantly FASTER than both. Lengthening REDUCED velocity** |

**And the %-body-height normalization is contradicted twice — by critiques that disagree with each other:**
- **Solomito, Cohen & Garibay (2023), *Sports Biomech* 22(11):1460–1469** ([PMID 32912079](https://pubmed.ncbi.nlm.nih.gov/32912079/)), n = 99 collegiate: **no significant association between normalized stride length and ball velocity.** Proposes 131–137% of *leg length*.
- **Yanagisawa & Taniguchi (2020), *J Phys Ther Sci* 32(9):578–583** ([PMID 32982054](https://pubmed.ncbi.nlm.nih.gov/32982054/)), n = 18 collegiate: **absolute** stride length r = 0.55, p = .02 — but **as % body height, r = 0.36, p = .15, NOT significant.** Also null against lower-extremity length and hip-abduction width.

> **⚠️ COUNT THE BUFFALO DATASET ONCE.** The 19-athlete Ramsey/Crotin cohort appears across **at least seven papers** — PMIDs 25457417, 26707678, 23917472, 25804970, 29578381, 37109515, plus *Life* 15(9):1440 (PMID 41010383). **One experiment, not seven trials.** Canonical velocity citation: PMID 25457417.

### Strongest evidence for the velocity report

1. **n = 315 professionals** is a far better population match than n = 19–20 at 73–81 mph. Both manipulations are **below the 85 mph floor.**
2. **Both manipulations are ACUTE and INSTRUCTED**, at ±20–25% — a disruption of a habituated movement, not a trained adaptation. Forcing an over-stride tests whether a man can absorb an insult.
3. **Manzi 2024 retained stride length in BOTH the HS and professional models.**
4. **Stride length has the best cross-system measurement agreement of any kinematic variable** (CCC > 0.85), so the cross-sectional finding is not a measurement artifact.

### Strongest evidence for the coach

1. **Two independent groups, two countries, two methods, two nulls — and one that goes backwards.** Matsuda is the damaging one: it did not merely fail to find a gain, it found **the pitcher's own self-selected stride was significantly faster than a lengthened one.**
2. **The normalization the recommendation is denominated in fails in two independent samples**, and the two failures propose different replacements. **You cannot prescribe a threshold in units whose validity is disputed.**
3. **The mechanism runs the wrong way.** Ramsey/Crotin's own kinematics show that shortening the stride *delayed* peak pelvis–trunk separation and *raised* the trunk's angular-velocity contribution — i.e. the body compensates and preserves the outcome. That is a **motor-redundancy** finding, and it is exactly what the uncontrolled-manifold literature predicts: **the system protects ball velocity against a perturbation of one parameter.**
4. **Measurement error exceeds the effect.** Single-camera markerless stride error is **5.75% of body height**; the change worth 2 mph is **10%.**

### Where the coach lands

> **A long stride is a MARKER of a pitcher who throws hard, not a LEVER that makes one.** Pitchers who generate more momentum stride further as a *consequence*. That is why it correlates at n = 315 and does nothing when you move it.

**Action taken 2026-08-13:** demoted in `velocity-development.md` §4.4 and §7; Open Question #8 rewritten; the §6.7 line *"there is ~1–1.5 mph sitting there before you touch anything else"* **deleted**; cue retired in `coaching-translation.md` §9 and §12.

### What would settle it

**The trial nobody has run: a LONGITUDINAL, CONSTRAINT-REMOVAL block — not a cue.**
20–30 pitchers at 85+, 8–12 weeks, targeting the plausible constraints on stride (drive-leg ankle dorsiflexion, incoming momentum / "body drift," trail-leg eccentric strength, lead-hip abduction capacity) **without ever instructing the athlete to stride further** — because instructing him is precisely the experiment that has already failed twice.

**Outcome: RELEASE velocity, never perceived/effective velocity** — extension is baked into perceived velocity by construction, and a longer stride raises extension, so evaluating on PV would manufacture a false gain. Track stride %BH, release velocity, extension, and release height simultaneously, from a fixed calibrated camera, **after establishing the athlete's own test-retest error.** ~8 separately-dated sessions of ≥25 fastballs per condition to detect 1 mph.

**Half of this study already exists and is unpublished:** an MS thesis by **Zack Buck** (advisor **Phil Pavilionis**), Univ. of Nevada, Reno, defended spring 2026 — D1 pitchers, 4-week resistance-band ankle-mobility + balance block, **pre/post stride length, no velocity outcome, no control group.** **Somebody should request it.**

---

## 14. ⬜ Is "keep lifting = floor protection" a real asymmetry, or a study-design artifact? — **added AND largely resolved 2026-08-13**

> ### ✅ SUBSTANTIALLY RESOLVED IN THE COACH'S FAVOUR, 2026-08-13 — same day it was opened.
>
> **The coach argued this asymmetry was probably a dose/design artifact BEFORE the design was known.** Verification then returned the design.
>
> **Gdovin et al.'s actual title is *"Limiting Access to Resistance Training Equipment During the Off-Season: The Impact on Collegiate Pitching Metrics,"* and the design is an UNCONTROLLED 8-WEEK PRE-POST OBSERVATIONAL STUDY WITH NO CONTROL GROUP.** It is not a removal trial, not a natural experiment, and not a designed subtraction. Nobody assigned, withheld, or compared anything.
>
> **The coach's objection #1 below — "this is not adding vs removing, it is a large dose change vs a small one" — turns out to have understated the problem. There is no comparison at all on the removal side.** PMID, n = 12, and p < .001 are correct; **the mph magnitude is paywalled and was never obtained**, so the library does not know how large the decline was.
>
> **Status: the DISPUTE is largely settled — the asymmetry does not have the evidentiary basis claimed. What remains OPEN is the underlying physiological question**, restated at the bottom of this entry.

**The velocity report's position as originally written** (`velocity-development.md` §5.5, §7 #1): *"Adding strength training to an 85+ arm has never been shown to add velocity in a controlled trial. Removing it demonstrably costs velocity."* Basis: **Gdovin JR, Hogan B, Williams CC (2025), *JSCR* 39(3):347–351** ([PMID 39495235](https://pubmed.ncbi.nlm.nih.gov/39495235/)) — n = 12 NCAA D1, 8 weeks, **ball velocity decreased p < .001.** Framed as **floor protection**, and named the document's **#1 highest-confidence recommendation.**

**The coach's position: the asymmetry is exactly what you would get from three mundane design differences, none of which requires a threshold effect to exist.**

1. **This is not "adding vs removing." It is a large dose change vs a small one.** ⚠️ **CONFIRMED AND WORSE, 2026-08-13: it is not even a dose comparison. There is no comparison group.** The study is an uncontrolled pre-post in which equipment access was *limited* during an off-season. The addition studies at least have control arms; **the "removal" arm has none.** The asymmetry the library built its #1 recommendation on is an asymmetry between *underpowered controlled trials* and *one uncontrolled observation*.
2. **Gdovin's own data contains no mechanism.** Peak arm slot angle, peak arm velocity, and peak elbow varus torque were **all unchanged (p > .05).** **A velocity decline with no kinematic correlate, in n = 12, is at least as consistent with accumulated fatigue, schedule, or measurement drift as with detraining.**
3. **The counterfactual is missing, and the library supplies it elsewhere.** ⚠️ **CONFIRMED 2026-08-13 — there is literally no control group.** League fastball velocity **RISES ~0.6 mph across a season** (Podhorzer, FanGraphs), and MiLB velocity rose linearly across the first 8 games (**R = 0.91**, Crotin et al. 2013). **A fall-season decline in n = 12 against no baseline trajectory is not evidence of causation** — and the library's own §5.4 says the expected direction is *up*.
4. **Expectancy.** Athletes told they have lost gym access, tested before and after, are not blind to the manipulation.

**Strongest evidence for the velocity report — much thinner than it looked.** ~~It is a removal/natural-experiment design, which is genuinely harder to confound than a between-groups addition trial.~~ **Struck: it is not.** What survives on the report's side: **Lambert 2023 independently documents that a D1 control group LOST rotator-cuff strength across just 8 offseason weeks doing their normal program** — so *"maintenance is not the default state"* has support from a second and better-designed direction, albeit on a strength outcome rather than velocity. And the **correlational case for mass and absolute power is the strongest in the entire document** (body mass r = 0.58, lean mass r = 0.52, CMJ concentric impulse r = 0.71, absolute cycle power r ≈ 0.44 replicated in D1 and MiLB, drop-jump RSI R² = 0.30 in 53 pros). **That case is real and it is what should have been carrying recommendation #1 all along.**

**Where the coach does NOT dispute:** he lifts the athlete anyway, year-round, at absolute loads. **The dispute is about the warrant and the wording, not the practice.**

**A framing objection that stands regardless of who is right:**
> **"Floor protection" is not a coachable sentence and the coach will not use it.** *"This won't make you better, it'll stop you getting worse"* is the least compelling thing available to say to a 20-year-old at 6 a.m. **The translation is "lifting doesn't buy mph — lifting is what lets everything else buy mph."** Substrate, not intervention. Then give him the correlational case with its honesty label attached, which makes him a participant in an open question rather than the recipient of a hedge. (`coaching-translation.md` §11.9.)

### What remains open, restated

**The dispute over the EVIDENCE is settled. The physiological question is not:** *does resistance training have any demonstrable velocity effect at 85+, in either direction?* **Nothing in the literature answers it.** Every addition study is underpowered and off-population; the one removal-flavoured observation has no control group and an unretrieved effect size.

**What would settle it.** A **dose-response trial** at 85+: three arms — maintenance / +30% volume / +60% volume — 16 weeks, radar at full intent, ≥8 dated post-test sessions (`coaching-translation.md` §11.13).

**Two cheap steps first, before anyone runs anything:**
1. **Obtain the Gdovin full text** and recover the actual mph values. The library currently cites a p-value with no effect size, which is exactly the failure mode it criticises elsewhere.
2. **Pull the cohort's prior-year fall trajectories.** If those pitchers also declined in a fall when they *did* have gym access, the finding is a schedule artifact outright.

**Action taken 2026-08-13:** `velocity-development.md` §3.4, §5.5, §7 #1 and §9 OQ7 all corrected; "removal experiment / removal design" struck throughout; recommendation #1 re-justified on the correlational case and **demoted below #2b**; the label moved **[EMERGING] → [WEAK]**.

**What does NOT change: the athlete still lifts, year-round, at absolute loads.** The dispute was always about the warrant and the wording, never the practice — and the coach's framing objection stands independently:
> **"Floor protection" is not a coachable sentence.** The translation is **"lifting doesn't buy mph — lifting is what lets everything else buy mph."** Substrate, not intervention. (`coaching-translation.md` §11.9.)

---

## 15. 🔴 Is spin efficiency trainable — and does the pitch-design industry price the cost honestly? — **added 2026-08-13**

**The industry's position** (implicit in every pitch-design service sold): spin efficiency is a trainable variable addressed through **grips, seam orientation, and intent cues** — a cheap, low-risk, reversible project. `stuff-and-command.md` §3.4 explicitly builds its design method on *"change exactly one thing: grip, seam orientation, or intent cue. Not mechanics."*

**The new data.** Michael Rosen, FanGraphs, 13 Apr 2026: **185 pitchers with ≥25 fastballs in both 2023 and 2026 — three-year spin-efficiency r² = 0.65.** Roughly **two-thirds fixed** across three seasons of professional coaching, at a level where every athlete has access to a pitch-design department.

**And the one documented mover bought a delivery change.** Emerson Hancock: **arm angle 23° → 13°**, landing moved crossbody, which per Driveline's Spenser Davis *"cut off his tendency to pronate."* Efficiency fell from 99%, which **helped** him. Connor White: *"the arm is not one fixed lever."* Field consensus quoted in the same piece: *"once you go supinator, it's hard to go back."*

**The coach's charge:**
> **If the one-third of spin efficiency that moves, moves via arm slot and landing position, then efficiency work is a MECHANICS project in a grip's costume — and it carries every cost in Disputes #10 and #12: platoon consequences, a possible command tax, and a torque change. Nobody is quoting that price.**

**Strongest evidence for the industry.** r² = 0.65 leaves **35% of variance moving**, which is not small; some of that is certainly grip and seam orientation, and grip changes genuinely are cheap and reversible. **And the headroom argument cuts the other way for four-seams specifically** — four-seam efficiency is compressed near its ceiling (p75 ≈ 95%, p90 ≈ 98%), so there was never much to win there. **The real efficiency room is in the breaking balls** (slider median 31%, sweeper 51%, cutter 47%), and nobody has shown *those* require a delivery change.

**Strongest evidence for the coach.** The only publicly documented large efficiency change in the modern era came with a 10° slot change and a landing-position change. **And there is still no controlled spin-efficiency intervention trial with a delayed retention test, anywhere** — `stuff-and-command.md` Open Question #9, which its own author flags as an absence that *"should bother people more than it does."*

**What would settle it.** A controlled trial: 20–30 elite arms, randomized to (a) grip/seam-only intervention or (b) no intervention, 8–12 weeks, **spin efficiency measured on one device with a cold retest ≥1 week later**, plus arm slot and release height tracked to detect whether the delivery moved without anyone intending it. **Report effect size separately for four-seams and breaking balls** — the coach predicts the four-seam arm shows almost nothing and the breaking-ball arm shows a real effect.

---

## 16. 🔴 Does release-angle precision have any coachable channel? — **added 2026-08-13**

**The stuff/command report's position** (`stuff-and-command.md` §5): *"This is the most important finding in the document and almost nobody coaches it."* **~30 cm of plate location per 1° of release angle**, vertically and horizontally (Kusafuka 2020, R² = 0.97/0.96) — and the number is **pure trigonometry** (`tan 1° × 54.5 ft = 11.4 in`), therefore not sample-dependent. Release angle is **~30× more consequential than release position.** Within-pitcher SD ±1.1° ≈ **13 inches of scatter**, essentially the entire observed miss.

**The coach's position: it is true, it is geometric, and it is inert as a coaching instruction.**

There is **no cue, no drill, no feedback channel, and no device in a college program** that returns a pitcher's release angle in a form he can act on inside the ~150 ms he has. **You cannot feel a thirtieth of a degree, and there is no external-focus surrogate for one.**

**And the report's own source agrees.** §5.1 conclusion 3 reports that Kusafuka et al. found improving the reproducibility of each release parameter individually is **NOT the optimum**, because skilled pitchers show **compensatory covariation** — different combinations of release parameters landing in the same spot. **So the coachable implication of 30 cm/° is NEGATIVE: it tells you what not to chase.** As currently written, a coach reads "30 cm per degree," concludes he has found the master variable, and goes and buys something.

**Where the coach agrees completely — and thinks the ordering is wrong.** Two things in that same section *are* immediately actionable, and both sit beneath the 30 cm/° headline:
1. **Release-speed variability as a command variable** — ~3.5 in of vertical miss per mph. **Free; the data is already in every radar log.** It appears as a numbered corollary.
2. **Horizontal corrective capacity** (Kusafuka 2025, PMID 40210939: the **"No"-correction transition probability correlates with SD of azimuth release angle at r = 0.73, p < .01**; the elevation equivalent is null at r = −0.18, p = .46). Also free, also actionable, and it is in §8.4.

**Both should be promoted above the geometric result.**

**Strongest evidence for the report.** The number is *true* and it correctly demolishes the release-point-repeatability industry (§6, and the BB/9 null at n = 344). **A finding whose main value is destructive is still valuable** — knowing which twenty years of coaching to stop is worth more than most new drills.

**What would settle it.** **Name a device.** Does any system — Trackman, Hawk-Eye, Rapsodo, or a research rig — report **per-pitch release angle** to a pitcher in a college bullpen at a latency he can use? If yes, the coach is wrong and this becomes the most important number in the document. **If no, it is a beautiful fact about geometry and it should be labeled as one.**

---

## Standing methodological disputes (not attributable to one agent)

- **Torque values are not comparable across labs.** 64 vs 100 vs 120 N·m for the same population. Now partly explained by sampling/filter frequency (Dowling, Slowik & Fleisig 2026). **Operating rule adopted: a torque number without its sampling rate and filter cutoff is not a number.**
- **Lab velocity ≠ game velocity.** Published kinetics likely *under*-represent competitive load, so every torque figure in this library is probably a floor.
- **60% of normalized elbow torque variance is unexplained by kinematics.** Nobody knows what's in there. Until somebody does, every mechanics-based stress claim in this library is a claim about the minority of the problem.
- **Survivorship.** Every "professional norms" table is drawn from arms that survived to be tested.
- **⚠️ ADDED 2026-08-13 — verifying a citation is not verifying a claim, and this program has been treating them as one operation.** **Six** library corrections landed on 2026-08-13 and **not one was a fabrication.** Each was a real source, correctly identified, read slightly wrong: a **cross-sectional finding read as a causal lever** (stride length); **two adjacent quantities collapsed** (absolute changeup velocity vs velocity separation — which *inverted* the conclusion); a **summary figure taken over the underlying table** (+1.35 vs +0.65 mph); a **sampling unit misread** ("pitcher-seasons" vs pitcher × pitch-type × season pairs); **an absolutism nobody checked because it was a negative claim** ("not one study at 85+"); and **a STUDY DESIGN assumed from a result** — Gdovin's p < .001 was read as a "removal experiment" when the paper is an **uncontrolled pre-post with no control group.** **Every one of them would have survived a PubMed check, because in every case the citation, the n, and the p-value were correct.**
  **The sixth is the sharpest illustration: a correct PMID, a correct n, and a correct p-value, attached to a design that does not exist.** Two further label errors landed the same day (first-authorship on PMID 34240663 — Manzi, not Dowling; and two Kusafuka 2025 coefficients described as an autocorrelation and a state probability when both are correlations *between* a correction statistic and azimuth variability). **A number can be right, its citation can be right, and the sentence around it can still be false.**
  **Operating rules adopted:** (a) the verification pass asks a second question — *does the source support this sentence, or a weaker one?* — **and a third: *what was the actual design, and is there a control group?*** Never infer a design from a p-value; (b) **any claim promoted to a numbered recommendation gets re-read against the primary source before it ships**, because those are the ones quoted to an athlete; (c) **sample sizes are verified on the paper's own page**, never from a search summary — an ordinary search summary was observed manufacturing a phantom sample size with no bad actor in the chain; (d) **the same scrutiny applies to disconfirming evidence** — the coach presented one 19-athlete cohort as multiple independent studies, in the direction he was already arguing, on the same day he accused colleagues of the same error. Full analysis in `daily/2026-08-13-coach.md` §11.
- **⚠️ ADDED 2026-08-13 — "one experiment, many papers."** The Ramsey/Crotin Buffalo stride cohort (n = 19) is reported across at least **seven** papers. Before treating multiple citations by one group as independent replication, **check whether it is one dataset.**
