# Velocity-Based Training — load–velocity profiling, bar-velocity autoregulation, and the precision claim

**Opened 2026-10-05.** Findings **F-588 → F-600**. Population: elite HS showcase / D1 / MiLB / MLB, **85 mph floor**.

⚠️ **PROVENANCE WARNING: this file was built in the SIXTH consecutive fully egress-blocked cycle (F-588). No primary text was opened. Every literature number is a search-result snippet; every author/year/DOI resolves to a real record, but no CLAIM is source-verified. The DERIVED arithmetic (§3, §4) is source-independent in its logic but not in its inputs.**

---

## 0. What question this file answers, and what it does not

`library/strength-training-velocity.md` answers **"does lifting add mph?"** — untested at 85+, nobody has run it.

**This file answers the next question down: given that he is going to lift anyway, does prescribing load off bar speed beat prescribing it off percentages, and can the device see what it claims to see?**

**The short answer, in one line: use the device to decide when a set ends, never to decide what the load is.**

---

## 1. The comparison literature (F-589, F-591)

| Review | Scope | Result |
|---|---|---|
| Soslu et al. 2026, doi 10.1177/17479541261452541 | 16 controlled trials, **N = 330** | VBT > traditional: **strength ES 0.26** (p=.03), **power ES 0.30** (p=.02), **jumping ES 0.36** (p=.01) |
| BMC 2025, doi 10.1186/s13102-025-01504-9 | trained individuals | **max strength SMD 0.21 [−0.01, 0.43], p=.064 NS; sprint NS**; small advantages jump + COD |

✅ **UNUSUAL FOR THIS CORPUS: `CAUSALITY: INTERVENTION`, and the F-439 n ≥ 97 rule PASSES at the meta level. The VBT null is not an underpowered null, and the marker/lever complaint does not arise.**

🚨 **AND YET — AMSTAR 2 (F-591):** *PLOS One* 2026, doi 10.1371/journal.pone.0342992. **17 VBT reviews, 2019–2025, 8,222 participants. 16/17 (94%) 'Critically low' confidence; 1 'Low'; none moderate or high. Only 4/17 (24%) used any certainty-of-evidence system.**

**Hold both at once: adequately powered, and formally rated near-worthless at the review layer. The direction is probably right (two independent reviews agree); no single number has a quality warrant.**

---

## 2. ⭐ The outcome it wins cannot be converted to mph (F-590)

VBT's biggest, most replicated advantage is **CMJ height (ES = 0.36)**. Price it in mph — you can't.

- **F-004 / F-438, CORRECTED 2026-09-22:** jump height vs fastball velocity, n = 33 D1, **r = 0.07**, 95% CI on the population r = **[−0.280, +0.404]** → upper bound **16.3% of velocity variance**. Not a null; an **uninformative interval**.
- **Wong 2023, n = 53 pros:** CMJ **R² = 0.10 (p=.28)**; squat jump **R² = 0.07 (p=.44)**; **drop jump R² = 0.30**.

🚨 **THE SHARP VERSION: the one jump variable that DOES track velocity is the reactive one (drop jump, R² = 0.30), and no VBT review reports drop jump or RSI at all. VBT's measured benefit sits on the jump variable that does not track and is silent on the one that does.** F-006 (no RSI-training intervention with a velocity outcome, anywhere) is the live branch off this dead end.

**This is Check 3, not a power complaint: the number is real, adequately powered, and does not measure what "VBT improves athletic performance" implies for a pitcher.**

---

## 3. ⭐⭐ The precision claim, inverted — two error routes, both ≈ ±10% of 1RM

### Route A — prediction error (F-592)

- **Individualised load–velocity profile: pooled SEE ≈ 9.8% of 1RM** (*Sports Medicine* 2023, doi 10.1007/s40279-023-01854-9, **434 participants, 20 studies**).
- **A TESTED 1RM's between-trial variation: −5.6% to +4.8%.** The best predicted method's individual variation: **−5.5% to +27.8%.**
- Best case (5 warm-up sets to 90% 1RM): ICC 0.92, SEM 8.6 kg, CV 5.7%.

> **DERIVED: the velocity-predicted 1RM is ≈ 2× as imprecise as testing the lift. On a 400 lb squat, ±9.8% = ±39 lb; a 5% increment is 20 lb. The prediction error is ~2 load steps wide — the entire resolution the method exists to provide.**

### 3a. Why — the anchor is the weakest number (F-593)

**V₁RM = 0.24 ± 0.06 m/s, ICC = 0.42, SEM = 0.05 m/s, CV = 22.5%.** Meanwhile submaximal mean/peak velocity: **ICC ≥ 0.801, CV ≤ 2.36%.**

**The device is reliable; its anchor is not — and the anchor's unreliability is a property of the ATHLETE.** Bar velocity at fixed load = strength **+** arousal, caffeine, sleep, warm-up completeness, intent, bar-path skill, shoe friction. **CV = 22.5% is those confounds in the data.** Every extrapolation to 1RM passes through this point, which is the mechanism under Route A's 9.8%.

### Route B — single-set detection limit (F-594)

- **Device mean-velocity typical error = 0.070 m/s** in use (ICC 0.91, CV 7%).
- **Published SWC = 0.05 m/s** mean velocity (0.10 m/s peak), free-weight back squat. **The error EXCEEDS the SWC.**

> **MDC₉₅ = 1.96 × √2 × 0.070 = 0.194 m/s — ~4× the SWC.**
> Scale: usable squat range ~40–90% 1RM ≈ 0.4–1.2 m/s (~0.8 m/s wide); zones ~0.1 m/s per 5% 1RM. **So 0.194 m/s ≈ 2 zones ≈ ~10% of 1RM.**
> **Averaging: MDC ∝ 1/√k — 3 observations → 0.112 m/s; 8 → 0.069 m/s.**

### 3b. ⚠️ The convergence, stated at its correct strength (Dispute #59)

Route A ≈ 9.8% of 1RM; Route B ≈ 10% of 1RM. **But they are NOT fully independent** — device noise propagates into the profile fit, so part of A is B in different clothes. **What is defensible: both land near ±10%, they share an unknown fraction of their error, and the fraction cannot be partitioned without opening the papers.** Route A does contain two error sources B does not (V₁RM's *biological* unreliability; model-form error from extrapolating to a load nobody lifted).

**The action is robust to the dispute: ±10% and ±7% both exceed a 5% load step.**

### 3c. ⚠️ UNRESOLVED MEASUREMENT FLAG — a 7× discrepancy

The searches returned **two** mean-velocity error figures for the same device: **0.070 m/s** ("typical error") and **0.01 m/s** ("controlled testing"). **Vendor-facing material quotes the small one.** Almost certainly bench-rig accuracy vs in-use reliability with a human lifting free weights — **unconfirmed, no text openable.** This file uses the larger figure because **CV = 7% independently corroborates it** (7% × 0.7 m/s ≈ 0.049 m/s). **If 0.01 m/s is the correct in-use figure, F-594 is WITHDRAWN. Top of the verification queue.**

---

## 4. Velocity loss — where the topic actually has an answer

| Source | Finding |
|---|---|
| *Sports Medicine* 2022, doi 10.1007/s40279-022-01754-4 | VL choice **does not affect** strength or muscle endurance. **Higher VL → hypertrophy. Lower VL → jump, sprint, velocity vs submaximal loads.** |
| *IJSSC* 2024, doi 10.1177/17479541241244581 | **VL ≤ 25% > VL > 25% for strength**, primarily with additional exercises alongside |
| Proximity-to-failure meta | **VL > 25% likely > hypertrophy than < 20%**; similar to 20–25% |
| Rodiles-Guerrero et al., 8 wk, trained men 22.7 ± 1.9 yr, squat 69–85% 1RM | **> 20% VL maximised hypertrophy; 10% and 20% gave the greatest CMJ gains; 30% and 40% considerably less** |

### 4a. ⚠️ Count two benefits, not three (F-598)

**"Low VL improves velocity against submaximal loads" is the test being the training.** Low VL means spending reps at high bar velocities; the outcome is bar velocity at submaximal load. **Not a geometric identity in the F-534 sense, but the same class: an outcome that cannot easily fail to move with the assignment.** Strip it and low VL is carrying CMJ height (unpriceable) and sprint (no registered velocity link).

### 4b. ⭐⭐ The trade-off inverts for a pitcher (F-597)

| Threshold | Buys | This corpus's mph link |
|---|---|---|
| **Low (10–20%)** | CMJ height, sprint | **UNPRICEABLE** — CI [−0.280, +0.404]; sprint has no registered link at all |
| **High (20–40%)** | hypertrophy → body + lean mass | **r = 0.58 (p=.0004) and r = 0.52**, n = 33 D1 — the strongest physical correlates in the literature (F-001, F-002) |

🚨 **NOT "CHASE HYPERTROPHY AND YOU WILL THROW HARDER."** **F-504: there is no within-athlete mass-change → velocity-change slope of any kind, in any population, at any level.** The mass correlation has never been manipulated.

✅ **WHAT IS CLAIMED IS NARROWER AND NEGATIVE: the standard reason for paying the cost of a LOW threshold is not a reason for a pitcher. A VL threshold must take some value — there is no null option to default to.** → **Dispute #60.**

### 4c. The one defensible use (F-599)

**Set and session termination.** The only use where the lever and the measurement are the same physical quantity inside one session — no 1RM extrapolation, no V₁RM, no overnight stability needed.

**Detection: at 0.7 m/s first-rep velocity, 20% VL = 0.14 m/s. Below the single-measure MDC (0.194). ABOVE the three-rep MDC (0.112). Three-rep averaging is what makes this readable; one rep does not.**

⭐ **F-086 UPDATED, NOT OVERWRITTEN.** Driveline's 4–6% / 6–10% session-termination and ~6% weekly figures are **across-session**; the research thresholds that change adaptations are **10–40% within-set** — an order of magnitude apart and **different quantities that must never be compared directly.** Grade unchanged (EMERGING); the "no validation study" clause narrows to **"no validation study in a pitcher."**

---

## 5. Mechanism (anatomy-physiology pass)

**The VL trade-off survives.** Reps deep in a set accumulate metabolic stress and tension at low velocities — the stimulus profile associated with cross-sectional-area change. Reps terminated early keep discharge rates high and fatigue low — the RFD profile. **Two adaptations genuinely competing for the same sets.** Downgraded claim after cross-examination: **"the only dose-response relationship in this file with a consistent direction across more than two independent samples"** — *not* "the least speculative mechanism here." **The acute GH observation is WITHDRAWN as supporting evidence** (a hormonal marker, not a pathway; acute GH has repeatedly failed to predict hypertrophy in better-controlled work).

**The precision claim's mechanism runs AGAINST VBT** — see §3a.

⚠️ **RULE 1, one line:** no VBT or VL study measured arm kinetics. These are barbell variables. **The injury constraint is neutral here**, which is unusual and is noted rather than dressed up as a caution.

---

## 6. Field standing (2026)

**The field has already turned.** The interesting development is a reversal, not a new claim, and the sceptics are now better supported than the advocates.

- **SimpliFaster, "Is It Time for Coaches to Rethink Velocity-Based Training?"** — mainstream practitioner outlet. **PROMISING as a read on sentiment; no new data.**
- **tntstrength.com, "Velocity-Based Training: Emperor's New Clothes"** — single-coach blog, low standing. **UNPROVEN as evidence; informative as sentiment.**
- **"Bar velocity is near-useless on Olympic lifts"** — **PROMISING and mechanically sound**: the lift's technical floor compresses the velocity range, so a light and a heavy clean barely differ.
- **Driveline, "Velocity Based Training for Baseball Athletes" (2017)** — ⚠️ **NINE YEARS OLD**, source of F-086, domain blocked. **Notable by absence: the sport's most research-active private lab has not revisited VBT publicly in nine years.**
- **Tread Athletics "deep barbell periodization"** — **MARKETING as stated**; no public protocol or data located.
- **"VBT = deadlifts while hitting a minimum speed threshold"** — **DEBUNKED as a description**: that is one zone of one implementation, and the minimum-velocity anchor is the method's least reliable number (F-593, ICC 0.42).

🚨 **IN-CYCLE HAZARD, F-539 PATTERN.** The field-sweep query returned, unattributed, a crisp sentence that was **a paraphrase of this cycle's own earlier framing from the same session**, presented as retrieved content. **The underlying 22.5% traces to a real study; the framing traces to nothing.** Cleanest instance yet of the summarisation layer laundering in-session reasoning into apparent external corroboration. **The defence that worked: notice when a source agrees with you in your own words.**

✅ **No fabrications detected. Count stands at 17.** ⚠️ **"Resolves to a real record" is not verification of a claim (Check 3) — and under a total block it was all that was available.**

---

## 7. What to do with an 85+ arm

**Change the VL threshold on the main lower-body lift from 10–15% to 20–25% for the accumulation block, and read it off a three-rep average.**

- **Load:** test or estimate the max as you already do and **program percentages**. Do not prescribe load off a predicted 1RM (§3).
- **Device:** within-session fatigue only. First-three-rep average vs last-three-rep average; terminate at the assigned VL.
- **The check is a scale and a DEXA/BodPod, not a radar gun.** Body and lean mass are the proximal outcomes with evidence behind them.
- **Detection honesty:** **you cannot evaluate this in mph.** F-586 — at an assumed between-session fastball SD of ~1.0 mph, 0.5 mph needs **≈ 32 paired starts**; a college starter makes 15–17.
- **Free and first:** log the **actual** VL at which sets currently end. **If it scatters 8–35%, you do not have a threshold — you have a rep scheme with a device next to it.**

---

## 8. Gaps (F-600)

- **No VBT or velocity-loss study in baseball players, at any level.** Not weak — none.
- **The only throwing-outcome trial in the topic is handball, n = 22, no control group, mislabelled** (F-595, F-596).
- **No bridge from CMJ height to mph.** This, not the missing experiment, is what blocks reading the existing VBT literature across to pitching (F-590).
- **No drop-jump/RSI training intervention with a velocity outcome, anywhere** (F-006) — the one live branch, since drop jump is the only jump variable that tracks velocity.
- **No within-athlete, day-to-day SD of mean bar velocity at a fixed load for a pitcher. SEVENTEENTH entry in the F-264 / F-289 / F-320 / F-504 pattern** — in every program's data, gating the whole readiness use case, published by nobody. **Four weeks of logging one lift.**
- **The 7× device-error discrepancy (§3c) is one page of one paper and swings every number in §3.**

---

## References — ALL SNIPPET-ONLY, ZERO OPENED

- Soslu R, Çuvalcıoğlu IC, Uysal HŞ, Uysal A, Thapa RK, Akgül MŞ, García-Ramos A (2026). *Int J Sports Sci Coach.* doi:10.1177/17479541261452541
- (2025) *BMC Sports Sci Med Rehabil.* doi:10.1186/s13102-025-01504-9 — PMC12870409
- (2026) *PLOS One.* doi:10.1371/journal.pone.0342992 — PMC12915968
- (2023) *Sports Medicine.* doi:10.1007/s40279-023-01854-9 — load–velocity IPD meta-analysis, 434 participants / 20 studies
- (2022) *Sports Medicine.* doi:10.1007/s40279-022-01754-4 — velocity-loss thresholds
- Chen BY et al. (2024). *Int J Sports Sci Coach.* doi:10.1177/17479541241244581
- Abuajwa O, Hamlin M, Hafiz E, Razman R (2022). *PeerJ* 10:e14049. PMID 36193438 — PMC9526411
- Rodiles-Guerrero L et al. — VL-threshold trials, squat and bench (*Biology of Sport*; *JSCR*)
- PMID 27669192; PMC8309813 — load–velocity 1RM prediction and reliability
- PMC6316460; kinetic.com.au/pdf/GA-Report2.pdf — GymAware validity/reliability
- (2024) *PLOS One.* doi:10.1371/journal.pone.0312348 — Vitruve LPT validity
- PMC7558277 — VL thresholds and kinetic/kinematic control; PMC7739360 — VBT in periodization
- Driveline Baseball (2017), "Velocity Based Training for Baseball Athletes" ⚠️ domain blocked, title/date from search index only
