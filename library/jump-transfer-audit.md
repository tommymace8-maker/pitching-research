# The Jump-Transfer Audit — what an underpowered null can and cannot license

**Opened 2026-09-22 (Cycle 20).** Companion to `library/strength-training-velocity.md`, which covers *what the jump literature says*. This file covers *how much of it is knowable at the sample sizes it was measured at*.

⚠️ **OPENED IN A FULLY EGRESS-BLOCKED CYCLE. ZERO PRIMARY TEXTS READ.** Everything here is arithmetic on numbers already registered in `FINDINGS.md`, and is reproducible from them in one script. External citations new on 2026-09-22 are **SNIPPET-ONLY** and are leads, not magnitudes.

Findings: **F-438 → F-449**. Correction notice: **F-004**. Dispute: **#37**.

---

## 1. The interval nobody computed

**F-004:** r = 0.07, NS, n = 33 NCAA D1 (King BW, Snow TK, Millard-Stafford M 2025, *JSCR*, PMID 39446825).

Fisher z = arctanh(0.07) = 0.0701 · SE = 1/√(33−3) = 0.18257 · 95% CI in z = 0.0701 ± 1.96(0.18257)

| | r | R² |
|---|---|---|
| Lower | **−0.280** | 7.8% |
| Point | 0.070 | 0.5% |
| **Upper** | **+0.404** | **16.3%** |

In the same 33 pitchers, King reports **absolute CMJ peak power r = 0.43** and **Wingate absolute peak power r = 0.44** as significant (F-005, F-007). F-004's upper bound is **0.404**.

**0.404 < 0.43, so the interval does not literally contain them.** The defensible claim is that the two are **indistinguishable at this n**, not that they are equal. A Steiger test on dependent correlations needs r(jump height, CMJ peak power), which this corpus does not hold.

---

## 2. The n ≥ 97 rule (F-439)

**Detection floor at n = 33** (α = .05, two-tailed, df = 31, t_crit = 2.0395): **r_crit = 0.344**, i.e. **11.8% of variance**. Below that, "NS" was guaranteed in advance.

**Power at n = 33**

| True r | 0.15 | 0.20 | 0.25 | 0.30 | 0.344 | 0.40 | 0.43 |
|---|---|---|---|---|---|---|---|
| Power | 13% | **20%** | 29% | **40%** | 50% | 64% | 71% |

**n required to bound the population r at 95%**

| ±0.25 | ±0.20 | ±0.15 | ±0.10 |
|---|---|---|---|
| 62 | **97** | 172 | **385** |

> **THE RULE: a registered NULL is usable only when n ≥ ~97.** Below that it reports a detection floor, not an absence.

**Applied to this corpus — and note that it discriminates, which is what makes it a rule rather than a solvent:**

| Finding | n / N | Verdict |
|---|---|---|
| F-004 jump height | n = 33 | ❌ **FAILS** |
| F-359 squat jump under fatigue | n = 18 | ❌ **FAILS** |
| F-196 speed–accuracy in throwing | n = 30 | ❌ **FAILS — flagged for regrade** |
| F-192 guidance hypothesis | k = 75, N = 2,228 | ✅ passes |
| F-190 OPTIMAL-theory nulls | k = 52, N = 2,061 | ✅ passes |

The ±0.20 threshold is a stated convention, not a fact of nature. A program may set it tighter; it may not set it at 33.

---

## 3. The structural error (F-441)

This program enforces one rule:

> **You may not read a cross-sectional ASSOCIATION as a within-athlete LEVER.**

It has never written down the mirror:

> **You may not read a cross-sectional NULL as the ABSENCE of a within-athlete lever.**

**The four channels closed with F-004, with the design of each closed effect:**

| Cycle | Finding | Channel | Design of the effect being dismissed |
|---|---|---|---|
| 09-15 | F-358 | re-warm-up raises CMJ, ES = 0.66 | within-athlete, constant mass, acute |
| 09-15 | F-359 | 117 pitches move no jump variable | within-athlete, constant mass, acute |
| 09-19 | F-406 | sleep loss costs −6.26% power | within-athlete, constant mass, acute |
| 09-20 | F-419 | pre-game cooling costs 0.3–0.9% power | within-athlete, constant mass, acute |

**F-004 is between-athlete, mass-varying, single-session.** It is least applicable exactly where the corpus has leaned on it hardest.

**Outcome: all four move from FALSIFIED to UNMEASURED.** That is a different instruction — *falsified* means stop; *unmeasured* means nobody looked. **No magnitude is licensed for any of the four, and this file produces none.**

### 3.1 The second pillar (F-443)

F-359 (n = 18, source-verified 09-15) has an argument independent of F-004 — the pitching stimulus itself did not move squat jump. Audit it:

- **MDE, paired t, n = 18, 80% power: d = 0.660.**
- Largest observed jump effect: **d = 0.25** (~15% power). Peak power d = 0.19 (~10%).
- Built to detect a large effect; reported the absence of a large effect.

**Scale problem:** F-359's velocity decline is **d = 0.32, P = 0.026** and **d = 0.38, P = 0.001**, but d = 0.38 at n = 18 paired carries only ~31% power. Those p-values are not reachable from those d's on a common SD. Near-certain explanation: the **velocity d uses the between-subject SD (±6.2 km/h)** while significance comes from a within-subject test, whereas the jump d's are pre/post pairs. **The two effect sizes are not comparable, so the contrast cannot establish a dissociation.** ⚠️ Inference, not a read — the within-subject SDs are not in the vault.

---

## 4. The mechanism (F-442) — jump height is mass divided out of impulse

Net vertical CMJ impulse **J = m·v_takeoff**; **h = v²/2g** ⇒ **v = √(2gh)** ⇒

> **J = m·√(2gh)**

**Jump height is the mass-free half of impulse.**

**The suppression.** In King's same n = 33: **body mass r = 0.58** (F-001), **lean mass r = 0.52** (F-002) — the two strongest correlates of velocity in the study. A between-subject jump-height comparison therefore **removes the strongest predictor from itself**. Jump height's null is not a weak relationship; it is a strong one with the signal divided out.

**Within an athlete, m is ~constant across a block, so J ∝ √h:**

| Vertical | Impulse gain |
|---|---|
| 24 → 26 in | **+4.1%** |
| 28 → 30 in | +3.5% |
| 30 → 32 in | +3.3% |
| 32 → 34 in | +3.1% |
| 24 → 26 in **and** 200 → 205 lb | **+6.7%** |

And **concentric impulse is the highest jump-test correlate of velocity in the literature, r = 0.71** (F-003, Sakurai 2024, n = 19 D1, PMID 38900174).

⚠️ **THE CHAIN HAS ONE MEASURED LINK AND ONE UNMEASURED LINK.** Height→impulse within an athlete is arithmetic. **Impulse→velocity within an athlete has never been measured.** F-003's r = 0.71 is between-subject and itself mass-loaded (F-003 reports lean/body mass vs concentric impulse at r = 0.71/0.81). **This file upgrades a broken chain to a chain with one open link. That is a negative result, not a positive one.**

### 4.1 The replacement cue — both clauses mandatory

> *"Two inches on your vertical at the same body weight is about four percent more impulse into the ground — that's the number that tracks velocity across pitchers. What nobody has measured, us included, is what four percent of impulse is worth in mph."*

**If the second clause is dropped the cue is worse than the sentence it replaced**, because "r = 0.07" at least erred toward doing nothing.

**The failure to watch for:** a vertical that rises while body weight falls. **That is the one case where F-004's between-subject frame is the correct one.**

---

## 5. What a program can measure this fall (F-449)

**Design.** Pair every CMJ session with a radar-logged bullpen. Regress **within-athlete deviations** — each man's session value minus his own season mean. That deletes body mass and between-athlete talent in one step, and is precisely the step F-004 does not take. Record **body mass at every session** so the normalisation is tested rather than assumed. Use **concentric impulse**, not height, as the predictor.

**Sample size, 80% power, α = .05 two-tailed**

| Within-athlete r | Paired observations | With 12 arms |
|---|---|---|
| 0.40 | **47** | ~4 sessions each |
| 0.30 | **85** | ~7 sessions each |
| 0.20 | **194** | ~16 sessions each |

⚠️ **Floors, not budgets.** Repeated measures within athletes are clustered; treating them as independent inflates significance. **Budget ~1.5–2×, or fit a mixed model with athlete as a random effect.**

⚠️ **Noise floor.** Session-to-session fastball SD is bracketed at **0.8–1.2 mph** (F-289) and is itself unmeasured for this population. **One session proves nothing.**

⚠️ **This yields a longitudinal within-athlete observation, NOT a lever.** For a lever you must manipulate the training load and randomise or counterbalance it. The observational version is a large improvement on F-004 and is still not a lever.

---

## 6. The number that does not exist (F-448)

**King 2025 and Sakurai 2024 both report r without b, and neither reports the fastball-velocity SD.** So do F-006 (R² only) and F-007.

> **Δmph per unit of impulse, per watt, or per inch of vertical is NOT COMPUTABLE from any source in this registry.**

This is distinct from the missing *within-athlete* slope: **even the cross-sectional conversion is unavailable.** F-004's original coaching line was right to forbid the conversion and **wrong about the reason** — it is **unavailable**, not **zero**.

It compounds F-289 (no published fastball-velocity SD for an 85+ arm, open since 2026-09-08), which is the same missing quantity from the other side. **Seventh entry in the pattern of F-264, F-289, F-295, F-307, F-320 and F-374: already in every program's own data, and nobody has published it.**

---

## 7. The 2026-09-22 field sweep — four leads, all SNIPPET-ONLY

| # | Source | Claim | Verdict |
|---|---|---|---|
| 1 | JSCR 2026, **PMID 42423608** | Longitudinal weekly CMJ vs velocity, **n = 8**, 15 wk / 53 games. CMJ → velocity **stability**, not mean. JH γ = −0.060 p = 0.001; RSImod γ = +3.800 p < 0.001 | **PROMISING DESIGN, UNTRUSTWORTHY MAGNITUDE.** 8 clusters cannot carry a scale parameter; two metrics with opposite signs; **Dispute #36 in print.** Top of the queue (F-444) |
| 2 | SCJ 46(5) Oct 2024 | Bilateral **broad** jump vs FB velocity **r = 0.589 / 0.587** in D1 pitchers | **PROMISING** — locates the null in the *metric*. But it is a **MARKER**; nobody has trained broad jump and measured mph (F-446) |
| 3 | J Human Kinetics, **PMID 42211802** | Braking force + body height = **43.3%** of velocity variance, n = 32 **junior high** | ⚑ **SAMPLE MISMATCH, DIRECTIONAL ONLY.** Absolute force + height in a maturing sample is a **body-size model** — corroborates the size confound (F-445) |
| 4 | Driveline 2021 vs `pitching.dev` | Vendor: **R² = 0.54, MAE 2.7 mph.** Aggregator: "margin for error **1–1.5 mph**" | Vendor **honest but useless individually** (error > a season's gain). Aggregator **DEBUNKED — ~2× understatement** (F-447) |

**Nothing new on the Driveline-vs-Tread axis.** The 2026 "data-driven vs movement-first" content is the 2021 argument with new URLs. Said rather than padded.

---

## 8. What this file does NOT claim

- **That jump height should be trained.** It should not. Train absolute impulse; use height as a readout at constant mass.
- **That the four channels are supported.** They are **unmeasured**. No magnitude is licensed for any of them.
- **That impulse causes velocity within an athlete.** Never measured. §4 is explicit that this is the open link.
- **That King 2025 is wrong.** Its number, test and reporting are not impugned. The error is this corpus's reading of it.
- **Any mph figure whatsoever.** See §6.

---

## 9. Open items handed forward

1. **Read PMID 42423608 at source.** Is the location-scale model fit with athlete as a random effect, and does the paper report a mean-velocity effect it *could* have detected? If it had ~15% power on the mean, its conclusion is Dispute #36 in print.
2. **Mat or force plate?** Was King 2025's jump height flight-time (mat) or impulse-derived (plate)? The SCJ review flags instrumentation as a moderator; a mat adds landing-posture error on top of an already-wide interval.
3. **Trace the r = 0.589 broad-jump figure to its primary study** — n and sample mean velocity both unknown.
4. **Run the n ≥ 97 rule across the entire registry.** How many registered NULLs come from samples that could never have detected a moderate effect? Two found in one topic today. **One grep and an afternoon; the highest-yield structural check available.**
5. **Steiger test on r = 0.07 vs r = 0.43** — needs r(jump height, CMJ peak power) from King 2025's correlation matrix.
