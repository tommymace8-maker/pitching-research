# THE MOUND — slope, height, surface, and the flat-ground-to-mound transfer

**Opened 2026-09-24 · Cycle 25 · Findings F-464 → F-472 · Dispute #40**
**TWO PRIMARY TEXTS READ IN FULL** (PMC7734513 Dowling 2020; PMC3806183 Nissen 2013). Eighth reading cycle in ten.

> **WHY THIS TOPIC EARNED A CYCLE.** `mound height`, `cleat`, `shoe` and `mound slope` return **0 hits** in `FINDINGS.md`; `traction` returns 23 and every one is the substring inside *distraction*. The corpus holds 470 findings and nothing on the surface every pitch is thrown from.
>
> **AND IT IS THE RARE INVERSION OF THIS CORPUS'S CENTRAL PROBLEM.** The vault runs ~30:1 cross-sectional to intervention. The mound has been **randomised within athlete** — twice. You cannot randomise a man into a stride length; you can absolutely move him onto flat ground and back. **§2 is a real lever test.**

---

## 1. What the mound actually is, as a number

Regulation geometry, from the rule:

- Top of the rubber sits **10 in (25.4 cm)** above home plate.
- Starting **6 in in front of** the rubber, the mound falls **1 in per foot for 6 ft**.
- So a lead foot landing `s` feet in front of the rubber sits at **`10 − (s − 0.5)` inches** above plate level.

| Stride, ft from rubber | Lead foot sits, in above plate | **Net downhill vs flat ground** |
|---|---|---|
| 4.90 | 5.60 | **4.40 in** |
| 5.25 | 5.25 | **4.75 in** |
| 5.50 | 5.00 | **5.00 in** |
| 6.00 | 4.50 | **5.50 in** |
| 6.50 | 4.00 | **6.00 in** |

**The mound is not "ten inches." To the pitcher it is a four-to-six-inch downhill and a release point four-and-a-half inches higher.** Those are the two numbers that do work in §4 and §5.

---

## 2. The lever test — mound vs flat ground, randomised within athlete

**Dowling B, McElheny KD, Camp CL, Ling DI, Dines JS (2020), *Orthop J Sports Med* 8(12), PMID 33354584, PMC7734513 — READ IN FULL 2026-09-24.**

**Design, quoted at source:** 21 HS varsity pitchers, 5 fastballs at each of 4 conditions (mound/flat × 60.5/50.5 ft), regulation 10-in mound, motusBASEBALL sleeve, radar gun. *"The order of the throwing conditions was randomized for each pitcher, to eliminate any bias related to testing order."* Each pitcher is his own control.

**Table 1 raw means (ball velocity, m/s):**

| | 50.5 ft | 60.5 ft |
|---|---|---|
| Mound | 33.9 (1.9) | **34.2 (1.9)** |
| Flat ground | 33.2 (1.9) | **33.3 (1.8)** |

**MOUND OVER FLAT AT REGULATION DISTANCE: +0.9 m/s = +2.0 mph.** At 50.5 ft, +0.7 m/s = +1.6 mph.

Also source-verified: **arm slot +3.0° higher on the mound** (95% CI 0.4–5.5, P = .02). **No effect** of mound vs flat on elbow varus torque, arm speed or arm rotation.

### 🚨 2.1 — THE SAMPLE

**34.2 m/s = 76.5 mph.** "High school varsity pitchers" here means a **76 mph** fastball — nine below this corpus's floor. Check #1, run, failed. **Everything in §2 is DIRECTIONAL ONLY for an 85+ arm.** Whether the effect survives to this population is **Dispute #40**.

### 🚨 2.2 — THE UNITS ARE WRONG IN THE PAPER, AND THE ABSTRACT COMPOUNDS IT (F-465)

Table 2's model coefficients should be the Table 1 cell differences. Differencing the cells:

| Row | Raw Δ @50.5 | Table 2 | Raw Δ @60.5 | Table 2 | Verdict |
|---|---|---|---|---|---|
| Arm slot, deg | +1.0 | +1.0 | +2.9 | +3.0 | ✅ matches |
| Arm rotation, deg | −0.5 | −0.5 | −1.4 | −1.4 | ✅ matches |
| Elbow torque, N·m | +0.3 | +0.3 | −1.0 | −0.9 | ✅ matches |
| Arm speed, "deg/s" | +30.6 | +5.2 | +80.4 | +14.2 | ❌ **raw ÷ 6 = RPM** |
| Ball speed, "m/s" | +0.70 | +1.6 | +0.90 | +2.0 | ❌ **raw × 2.2369 = MPH** |

Three rows reproduce exactly. The two that do not are **exact unit conversions to the printed digit**: 0.70 × 2.23694 = 1.57 → "1.6"; 0.90 × 2.23694 = 2.01 → "2.0"; 30.6 ÷ 6 = 5.1 → "5.2"; −38.4 ÷ 6 = −6.4 → "−6.4".

**Consequences.** The printed CIs (1.2–1.9 and 1.7–2.3 "m/s") **exclude the paper's own Table 1 differences**. Read as printed the mound is worth 3.6–4.5 mph; read correctly, **1.6–2.0 mph** — a factor of 2.24.

And the abstract: *"...with pitches at 60.5 ft having higher velocity (+0.7 m/s)."* That **+0.7 is the 60.5-vs-50.5 contrast within the mound condition**, and in corrected units it is **0.7 mph (0.31 m/s)**. A WebSearch summariser this cycle reported it as the mound-over-flat effect in m/s: **wrong contrast and wrong unit, a 4.5× error, off a correctly-cited open-access paper.**

> **NEW HAZARD CLASS — THE UNIT-MISLABELLED TABLE.** Journal real, DOI resolves, open access, three of five rows internally consistent. Every fabrication defence passes. **The only thing that caught it was differencing the paper's own Table 1.**
> **OPERATING RULE: when a paper prints both cell means and model contrasts, difference the cells and check. One minute.**

---

## 3. The paper that measured velocity and did not print it (F-466)

**Nissen CW et al. (2013), *Sports Health* 5(6):530–536, PMC3806183 — READ IN FULL 2026-09-24.**

Methods, quoted: *"Two markers were placed on the ball to calculate the ball velocity..."* **A full-text search for "ball velocity", "ball speed", "m/s" and "mph" returns that sentence and nothing else.** Not in the abstract, not in Tables 1–4, not in Results, not in Discussion.

What it did report, both favouring the mound:

| | Mound | Flat | P |
|---|---|---|---|
| Max GH internal-rotation velocity, deg/s | 3560 ± 500 | 3396 ± 400 | .05 |
| Max elbow-extension velocity, deg/s | 1808 ± 192 | 1742 ± 206 | .01 |

+4.8% and +3.8% — the two angular velocities most proximate to ball speed.

⚠️ **Population: mean age 12.7 ± 1.3 y, inclusion 9–14, mean mass 54 kg.** Its 33.6 / 31.7 N·m joint-moment numbers are circulating in search summaries **without the age attached**; they are nine-to-fourteen-year-olds and must never be quoted for an 85+ arm. Also at source: *"A power analysis was not performed at the start of the investigation."* n = 15, **3 trials each**.

**Why this matters beyond the one paper:** Dowling explains its disagreement with Nissen by age and experience. **But Nissen reported no ball velocity to disagree with.** Part of what looks like a contested literature is a missing table row.

---

## 4. The energy accounting — ~100 J in, ~5 J out (F-468)

Pure arithmetic. Ball mass 0.145 kg; `g` = 9.81; masses from Dowling's participants.

**FREE POTENTIAL ENERGY the downhill supplies, `mgΔh`:**

| Mass | Extra drop | Free PE |
|---|---|---|
| 73.6 kg (Dowling's sample) | 4.4 in | **80.7 J** |
| 73.6 kg | 6.0 in | **110.0 J** |
| 90 kg (an 85+ college arm) | 4.75 in | **106.5 J** |
| 90 kg | 6.0 in | **134.6 J** |

**BALL KINETIC ENERGY:** 117.4 J at 90 mph. 84.8 J at 34.2 m/s.

**WHAT THE BALL KEEPS.** Dowling's measured gain is 84.8 − 80.4 = **4.40 J** against 80.7–110.0 J available → **4.0–5.5%**. For a 90 kg arm, **+2 mph from 90 costs 5.27 J** against 89.7–134.6 J → **3.9–5.9%**.

**The two efficiencies coincide at populations fourteen miles an hour apart.** That is a consistency check, not a proof.

### What this licenses, and what it does not

✅ **An energy argument cannot dismiss the mound.** The downhill supplies **more joules than the ball ever carries at 90 mph**. "Ten inches can't matter" is wrong on the physics.

✅ **An energy argument also cannot sell it.** ~95% goes to eccentric absorption at the lead leg, braking and heat. It is not sitting there waiting for a cue.

🚨 **NO DRILL FOLLOWS FROM THIS SECTION.** "Use the mound," "fall down the hill," "get more out of the slope" all propose to raise a transfer efficiency **nobody has ever measured within an athlete**. F-063 already retired *"get down the mound faster."* Filed as **MECHANISM**, generating no prescription — the F-392 posture, adopted deliberately.

---

## 5. What the mound does to the pitch: plane, not speed (F-469)

Release happens ~0.5–1 ft beyond the lead foot, where residual mound height is **4.0–5.5 in**. Two independent routes:

- **Trigonometry**, over the 16.8 m release-to-plate path: **0.35° / 0.39° / 0.48°** for 4.0 / 4.5 / 5.5 in.
- **F-151's regression** (|VAA| = 9.069 − 1.084·plate_ht + 1.055·rel_ht − 0.0927·IVB − 0.0630·velo; n = 6,110, R² = 0.999): 1.055 × (4.5/12) = **0.396°**.

**They agree.** Call it **0.40°**.

**Translations:**
- Via **F-152** (+1 SD of VAA-above-average = 0.5°): the mound ≈ **0.79 SD**.
- Via **F-151's** own exchange rate (half a foot of release height = 0.53° = 5.7 in of IVB): the mound ≈ **4.3 inches of IVB-equivalent**.

⚠️ **This is a GEOMETRIC IDENTITY, not a discovered effect** — check #4, declared. It is registered as mechanism.

⚠️ **But one term in it was measured, not assumed:** Dowling's **arm slot +3.0° on the mound**. Posture moves in the same direction as the geometry, so 0.40° is a floor, not a ceiling.

### 🚨 5.1 — THE MEASUREMENT WARNING, which is the part coaches break

**Never grade a four-seamer's VAA, ride or "flatness" from flat-ground data.** On flat ground the identical delivery produces an approach angle **~0.4° flatter** — nearly a full SD of "flat fastball," for free, **from the floor**. A pitcher who looks like a ride-and-flat guy on flat ground and ordinary off the mound has not changed.

Same in reverse for a steep sinker.

**What to say: *"flat ground tells you about your arm, not about your pitch."***

---

## 6. The bullpen mound as a command contaminant (F-470)

With launch angle unchanged, a release-height error `δ` translates **one-for-one** into vertical arrival error. The trajectory translates; it does not rotate.

| Bullpen mound off by | Pitch arrives off by |
|---|---|
| 0.5 in | 0.5 in |
| 1.0 in | 1.0 in |
| 2.0 in | 2.0 in |

**Scale against this corpus's own command work.** F-309: a realistic one-season command gain is **4.52 points** of zone rate; the catcher-contamination term at δ = 0.5 in of glove movement is **3.69 points**. A mound-height discrepancy is **the same order of magnitude as both** — and unlike catcher assignment it is **constant, unidirectional and free to remove.**

Per F-309's own framing this is **BIAS, NOT NOISE**: more bullpens make you *more* confident in a contaminated number.

⚠️ **THE HONEST LIMIT, and it is the open half.** This bounds what is geometrically **available**. It says nothing about whether the pitcher's own adaptation already absorbs it — a man who has thrown 300 pens on a low mound has adapted, and **the adaptation is exactly the thing that fails to transfer.** That is **Dispute #40b**, and it is the same shape as F-306's harvest question.

---

## 7. Gaps (F-471)

- 🚨 **NO MOUND MANIPULATION ANYWHERE HAS USED A COMMAND OUTCOME.** Height manipulated → velocity/spin/break. Mound vs flat → velocity, arm slot, torque. **Zero accuracy outcomes.** Dowling's pitchers were told to *"aim down the middle of the strike zone"* — **a target was declared and the miss was never scored.** Thirteenth entry in the F-264/F-289/F-295/F-307/F-320/F-336/F-348/F-363/F-374/F-385/F-396/F-457 pattern.
  **And the arithmetic says why:** 5 pitches per condition detects nothing about location. Against σ = 6/8/10 in (F-457), separating a 1-inch shift needs **hundreds** per condition. **It is unmeasured because it is expensive, not because nobody thought of it.**
- **THE MOUND-SURFACE LITERATURE IS NOT A LITERATURE.** A sweep for firmness, clay composition, landing-area stability and cleat traction returns groundskeeping vendors and a **subjective 1-to-10 daily rating sheet**. No instrumented traction measurement, no performance outcome, in any population.
- **NO PUBLISHED DISTRIBUTION OF MOUND-TO-MOUND HEIGHT AND SLOPE VARIATION** in any conference or organisation. F-470's whole magnitude is unbracketed for this reason. **It is a level, a tape and an afternoon.**
- **THE SAMPLE VELOCITY OF THE MOUND-HEIGHT MANIPULATION IS UNKNOWN** (F-467) — check #1 cannot be run on the topic's most important paper.

## 8. Verification queue for this topic

1. 🚨 **Diffendaffer/Fleisig 2019, *J Sci Med Sport*, PMID 30733141** — the 15/20/25/30 cm randomised manipulation in 20 collegiate pitchers. **Needed for: the sample's mean velocity; whether the null had power; the actual kinematic magnitudes.** `jsams.org`, ScienceDirect, `doi.org` and a `foreonline.org` PDF mirror **all HTTP 000 on 2026-09-24; not in the PMC OA bucket.**
2. **Fleisig, Diffendaffer, Ivey, Oi (2018), AJSM — youth mound height and distance.** Youth, so low value, but it is the third randomised manipulation.
3. **Fleisig et al., the 17 college-aged mound-vs-long-toss comparison** cited by Nissen as ref 5. Cf. F-137.
4. **The claim that MLB slope-gauges game and bullpen mounds ~monthly** — vendor-sourced, unverified, one league document would settle it.

## 9. Retrieval notes, 2026-09-24

**Pre-topic probe run as F-351/F-462 require, against BUCKETS not journals. SERVED (200):** `pmc-oa-opendata.s3.amazonaws.com`, `storage.googleapis.com/arxiv-dataset`, `openalex.s3.amazonaws.com`, `ncaaorg.s3.amazonaws.com`. **403 (bucket answers):** `biorxiv-src-monthly`. **REFUSED (000):** `en.wikipedia.org` (control), `pmc.ncbi.nlm.nih.gov`, `jsams.org`, `cir.nii.ac.jp`, `jstage.jst.go.jp`, `doi.org`, `foreonline.org`.

**The standing brief's WORKING-domain list was wrong for the FOURTEENTH time.** It names `pubmed` as blocked and `nature.com`/`frontiersin.org`/`jstage` as working; the only things that served were the four object stores. **Both texts today came through `?list-type=2&prefix=PMC<id>.` then a GET of the `.txt`, in under three minutes.**
