# Range of Motion and Mobility as a Velocity Constraint

**Opened 2026-10-03.** Companion to `anatomy-physiology.md` (osseous ceilings), `strength-training-velocity.md` (the capacity channel) and `null-audit.md` (the power rules applied below). Findings **F-562 → F-573**. Disputes **#55, #56**.

⚠️ **EVERY LITERATURE CLAIM IN THIS FILE IS SNIPPET-ONLY.** The cycle that produced it was the fourth consecutive fully egress-blocked run and the block was total (F-572). Nothing here was read at source. The source-independent arithmetic — §3, §4, §6 — is the part that does not depend on that.

---

## 1. The one-paragraph answer

**A pitcher's hip rotation number is mostly the shape of his femur, the velocity figure everyone quotes was measured on a different construct, and the only trial that ever increased an 85-population pitcher's range of motion and then measured his pitching found no velocity gain.** Range of motion almost certainly matters — but as a constraint that decides which delivery he can hold and decelerate, not as a dial that produces miles per hour. **Measure it once. Do not program toward a norm.**

---

## 2. What the literature actually contains

| Study | n | Population | Design | Outcome | What it shows |
|---|---|---|---|---|---|
| J Appl Biomech 40(5):399, 2024 | **99** | collegiate, velocity unknown | CROSS_SECTIONAL | ball velocity + elbow moment | +10° in-pitch lead hip IR at MER → **+1.34 mph**, r² = .26; elbow varus moment +5 N·m, r² = .33. ✅ passes n ≥ 97 |
| Robb et al. 2010, AJSM 38(12):2487 | 19 | professional, velocity unknown | CROSS_SECTIONAL | ball velocity | nondominant-hip total arc **r ≈ .50** — against r_crit = .456 at n = 19 |
| Takeuchi et al. 2020, OJSM | 149 | elite (64 P, 85 PP), age 20.0 | CROSS_SECTIONAL | femoral torsion ↔ hip ROM | FTA lead **20.5 ± 9.2°**, trail **19.6 ± 9.8°**, symmetric (P = .276) |
| McCulloch et al. 2014, OJSM | — | professional | CROSS_SECTIONAL | hip rotation | hip rotation ROM is **asymmetric** |
| J Sport Rehabil 34(7):691, 2025 | review | pooled HS/college/pro | REVIEW | normative ROM | trail IR at 0° flex **49.4 ± 12.6°**; "+7° pro vs college" ⚠️ **Type D** |
| Bullock et al. 2018, JSCR (F-015) | 30 | NCAA D1 | CROSS_SECTIONAL | FB velocity | trunk rotation ROM **r = 0.131, p = .491** — under-powered (r_crit = .361) |
| n = 11 IMU study (unidentified) | 11 | collegiate | CROSS_SECTIONAL | in-pitch vs passive | pitchers **approach their passive extremes** when throwing |
| Williams 2013, J Sports Med | 27 | throwers, 61-mph-class unknown | **MANIPULATED_NULL** (crossover) | throwing velocity | acute static/PNF IR stretching — **no stretching × velocity interaction** |
| **J Osteopath Med 2025, PMID 41588695** | **11** | collegiate, velocity unknown | **INTERVENTION** (RCT) | ROM **and pitching** | ROM moved (+7.16° sh IR; +6.76→12.87° hip flexion). **Only significant performance result: −0.74 mph "effective velocity," p = .048, not sustained** |
| 4-wk stretching RCT | 24 | college | **INTERVENTION** | **ROM only** | ROM increased. No pitching outcome. |
| GIRD stretching RCT (PMC8091767) | 42 | overhead athletes | **INTERVENTION** | **ROM only** | ROM increased. No pitching outcome. |

**Read the right-hand column downward.** The interventions exist and work. They were all pointed at range of motion. **That is F-571, and it is the defining feature of this literature.**

---

## 3. The scale bar (F-565) — always state it

`SD_x = r · SD_y / b`, from the published `b = 0.1342 mph/deg` and `r = .510`:

| Assumed collegiate FB velocity SD | Implied SD of lead hip IR | Mean → +2 SD worth |
|---|---|---|
| 2.0 mph | 7.6° | **2.0 mph** |
| 2.6 mph | 9.9° | 2.7 mph |
| 3.5 mph | 13.3° | **3.6 mph** |

**The whole dial has 20–26° of travel across the entire college population, and crossing all of it is worth 2–3.6 mph between different men.** That is not an amount available to an individual. Quoting "1.3 mph per 10°" without this table is the same error as "+1.8 mph per foot of extension."

---

## 4. The osseous share (F-566) — why the number is mostly structure

Femoral torsion SD ≈ 9.5°. Passive hip IR ROM SD ≈ 12.6°.

- 1:1 mapping → osseous variance share `9.5²/12.6² = **57%**`
- 0.7 attenuation → `(6.65)²/12.6² = **28%**`

⚠️ **Both brackets are soft and they push opposite ways:** the 12.6° is pooled across studies with different raters, so it carries method variance and *deflates* the share; ultrasound FTA error *inflates* it. **Read it as "a large but unquantified share." The real coefficient is printed in Takeuchi 2020 and is verification queue item 1.**

**The claim survives without the arithmetic.** Measured contrasts: increased-anteversion populations average **68.33 ± 6.34°** of maximum hip IR vs **38.95 ± 13.66°** in controls — **~29° from bone**. Modeled bony impingement limits IR at a mean of **63° (range 30–85°)**, intraoperatively **49° (range 20–70°)**. **Four-week stretching programs yield 5–10°.**

→ **This is F-115 at a second joint.** The corpus retired *"stretch out his GIRD"* because humeral retrotorsion is osseous and locked at maturity. **The identical argument applies to hip internal rotation.** And F-115's warning about cost transfers: the tissue that yields to aggressive rotational stretching is the anterior capsule you did not want to lengthen — at the hip, that implicates the labrum.

---

## 5. The three competing models (Dispute #55)

| | **LEVER** | **PERMISSIVE CEILING** | **MECHANICS SELECTOR** |
|---|---|---|---|
| Claim | more ROM → more mph | binds below threshold, inert above | decides which delivery he can hold |
| Shape | linear | threshold + plateau | not a velocity relationship at all |
| Best evidence | r² = .26, n = 99 | in-pitch ≈ passive max; 28–57% osseous | mechanism; two independent practitioner groups |
| Fatal problem | construct swap; never manipulated | n = 11, snippet-only, shape never fitted | **zero trials, any population** |
| Training implication | run a mobility block | find his threshold, then stop | measure once, pick the delivery |

**Nobody has fitted a threshold, spline or segmented model to hip ROM against velocity. Every published analysis is Pearson r or OLS.**

---

## 6. The protocol, if you measure it at all (§ this is the usable output)

**Measure once. One rater. Three reps averaged. Same time of day. Record it as his own baseline, never against a norm.**

Minimal detectable change, from same-rater baseball reliability (ICC 0.95–0.98; **SEM 2.2° IR, 3.2° ER**), `MDC₉₅ = 2.77 × SEM`:

| | Single measurement | **Mean of 3 reps** |
|---|---|---|
| Hip IR | **6.1°** | **3.5°** |
| Hip ER | **8.9°** | **5.1°** |

⚠️ **The SEMs come from a YOUTH sample — SAMPLE MISMATCH, directional only, and probably optimistic for a 95 kg college arm.**

> **A single-rater re-measure must move more than ~6° of internal rotation before you may call it a change — and ~6° is roughly the entire yield of a four-week program.** Three reps averaged cuts that to 3.5° and is the difference between a protocol that can detect its own effect and one that cannot. **Most mobility programs are audited at single-measurement precision and are therefore unfalsifiable on their own terms.**

**And the velocity side, for contrast.** If he genuinely gained 6° *and* the (wrongly imported) 0.134 mph/deg transfer were real, that is **0.8 mph**. Paired detection at 80% power, α = .05:

| His within-athlete FB velocity SD | Pitches per condition |
|---|---|
| 1.0 mph | **13** |
| 1.5 mph | **28** |
| 2.0 mph | **50** |

⚠️ **Cannot be narrowed: no within-outing fastball velocity SD has ever been published for an 85+ arm** (a gap `INDEX.md` already carries). **Note the asymmetry — the velocity check is one or two bullpens. The ROM check, at MDC 6°, is the hard half.** That is the opposite of how these programs are usually audited.

---

## 7. What to say to a pitcher

- **"That number is mostly the shape of your hip, not the state of your hip, and we're not chasing somebody else's number."**
- **"We're going to measure your hips once, and then pick the delivery your hips can actually hold."**
- **"If your hips fall apart in the fifth, that's strength, not tightness"** (F-570).

**On video the failure looks like:** a closed-off landing in a pitcher with limited internal rotation, who dumps deceleration into his lumbar spine, loses the hip as a brake, and drifts his release point late in outings.
**The check is not velocity:** late-outing release-point consistency, and his own hip-rotation strength-endurance trend across a bullpen.

---

## 8. RETIRED AND FOLKLORE

- **RETIRED CUE 2026-10-03 — "get more front hip internal rotation and you'll throw harder."** Imports an in-pitch mocap angle onto a passive mobility measure, from a cross-section nobody manipulated (F-564).
- **FOLKLORE — "every pitcher needs X degrees of hip internal rotation."** No validated threshold at any level (F-566).
- **DO NOT QUOTE — "pros have 7° more hip IR than college players."** Pooled across studies and across a competition-level gap; Type D (F-569).
- **DO NOT QUOTE — the OMT trial's 0.74 mph, in either direction.** n = 11, derived metric (F-562, F-563).
- **DO NOT CITE — the Crimson Publishers ankle-dorsiflexion/varus-torque item.** Predatory-adjacent publisher, and the outcome is torque.
- **MARKETING — "Mobility Is Crucial To The High Velocity Pitcher," "Unlocking Pitching Velocity With Hip Mobility," free "Hip & T-Spine" PDFs.** The recurring move is to cite an *adolescent* hip-flexibility correlation (PMC9528701) and assert a causal training claim at the college level.

---

## 9. Total gaps

1. **No study, in any population, relates ankle dorsiflexion ROM to ball velocity.** (`ankle dorsiflexion` had 0 hits in this corpus before today.) The Nevada Reno 4-week ankle-mobility intervention remains unpublished and its outcome is stride length.
2. **No passive-hip-ROM-vs-velocity study in a confirmed 85+ sample.** Robb 2010 (n = 19 pro) is the only candidate and its mean velocity is unretrievable.
3. **No threshold/spline model of ROM against velocity, ever.**
4. **No study has measured passive ROM and in-pitch ROM in the same athletes** — the premise of the permissive-ceiling model is unverified.
5. **No stratification of pitchers by hip ROM or femoral version against any mechanical or performance outcome.** F-573 is untested in its entirety.
6. **No bullpen-fatigue decomposition of hip ROM against hip strength.** Cheap, and it would settle F-570's channel question.
7. **No thoracic-rotation mobility study with a velocity outcome.** The 2025 Cureus college study measured elbow valgus torque.
