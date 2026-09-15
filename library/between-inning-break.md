# The Between-Inning Break — the 120-second budget, the warm-up decision, and the long half-inning

**Created 2026-09-15.** Cycle 14. Companion to [`pitch-clock-tempo.md`](pitch-clock-tempo.md), which covers the *inter-pitch* interval; this file covers the *between-inning* one.

> ### ✅ RUN CONDITION — THE READING BLOCKADE ENDED THIS CYCLE
> Unlike every library file created between 2026-09-04 and 2026-09-14, **this one was written with primary sources open.** Six full texts were downloaded and read: four through the NIH PMC Open Access bucket on S3, one through the arXiv bulk corpus on Google Cloud Storage, and one confirmed NCAA rules PDF. See **F-351**.
> **What that changes for this file:** §2's thermal inputs, §6's intervention table and §7's population audit are **source-verified**. §3, §4 and §5 are derivation, as usual, and are labelled.
> **What it does NOT change:** every derivation in §3–§4 still scales with `d`, the per-pitch phosphagen depletion, which remains unmeasured in any population (F-336). **The fractional-recovery table in §3 is the exception and is invariant to `d`.**

---

## 0. The question, and why it is new

The 2025 NCAA rule change converted the between-innings warm-up allowance **from a pitch count to a time budget**: 120 seconds between innings, 150 for a relief pitcher, **unlimited warm-up pitches inside it** (Rule 9.2.i; source-verified 2026-09-14, F-345). A pitcher now makes a genuine allocation decision eight times a night — how many warm-ups, and when — and nobody has priced it.

This file prices it, and the answer is mostly **"it is small, stop arguing about it"** — with one exception that is not small and is not the routine break at all (§5).

---

## 1. Two channels, opposite signs

Sitting between innings does two things to a pitcher:

| Channel | Direction | Speed | Status |
|---|---|---|---|
| **Phosphagen resynthesis** | longer rest is **better** | fast — half-time 20–30 s (F-132) | saturates |
| **Muscle temperature / neuromuscular readiness** | longer rest is **worse** | slow — time constant of order 300–1800 s | does not saturate inside the break |

Everything in this file follows from the fact that **the good channel is roughly an order of magnitude faster than the bad one.**

---

## 2. The thermal channel — what the half-time literature actually measures (F-356)

**SOURCE-VERIFIED INPUTS.** From González Fernández et al. (2023), *Biology of Sport* 40(2):335–344 (PMC10108754), read in full:

- A passive **15-minute** half-time induces a muscle-temperature drop of **~1.5 °C**.
- And from PMC10535876, read in full: **~3% reduction in lower-body power output per 1 °C** of muscle-temperature reduction.

**DERIVED.** Calibrating an exponential decay so that ΔT(900 s) = 1.5 °C, and reading it at 120 s:

| Thermal time constant τ_T | Asymptote | **ΔT at 120 s** | share of the half-time drop | power cost at 3%/°C |
|---|---|---|---|---|
| 300 s | 1.58 °C | **0.52 °C** | 34.7% | 1.56% |
| 600 s | 1.93 °C | **0.35 °C** | 23.3% | 1.05% |
| 1800 s | 3.81 °C | **0.25 °C** | 16.4% | 0.74% |
| linear limit | — | **0.20 °C** | 13.3% | 0.60% |

**Range 0.20–0.52 °C; best estimate ~0.30–0.35 °C; cost ~0.6–1.6% of lower-body power, best estimate ~1%.**
For the relief pitcher's 150 s: **0.28–0.62 °C.**

> ⚠️ **F-004 FORBIDS THE OBVIOUS NEXT STEP.** Bilateral vertical jump height has *no* significant relationship with fastball velocity (r = 0.07 NS), and power per kilogram is also a null (F-005, r = 0.19 NS). **There is no published conversion from "percent of lower-body power" to "mph," and this corpus will not invent one.** Anyone who hands you a mph figure derived this way has done arithmetic the literature does not support.

> ⚠️ **AND THE INPUTS ARE FROM SOCCER PLAYERS' LEGS.** No muscle-temperature measurement of a pitching arm between innings exists in any population. **New gap.**

---

## 3. The metabolic channel — and why the 120-second cap is nearly free (F-357)

**DERIVED**, using this corpus's own F-132 fast-phase half-time of 20–30 s (τ = 28.9–43.3 s), the same bracket F-327 used.

| Elapsed break time | fast-phase recovery (τ = 28.9 s) | (τ = 43.3 s) |
|---|---|---|
| 30 s | 64.6% | 50.0% |
| 60 s | 87.5% | 75.0% |
| 90 s | 95.6% | 87.5% |
| **120 s (NCAA cap)** | **98.4%** | **93.7%** |
| 150 s (reliever) | 99.4% | 96.9% |
| 180 s | 99.8% | 98.4% |

> ⚠️ **THIS TABLE IS INVARIANT TO `d`.** The unmeasured per-pitch depletion scales the *absolute* deficit but **cancels out of the fraction recovered**. That makes this the one table in the recovery work with quotable cells — an F-307-class invariance, and the reason §3 is usable where F-327's §2 is not.

**Marginal value, the F-330 result carried to a longer interval:**

- The **first 30 seconds** of the break buy **50.0–64.6** points of recovery.
- The **last 30 seconds** (90 → 120 s) buy **2.9–6.3** points.
- **Ratio 8.0×–22.5×** — against F-330's inter-pitch ratio of only **1.60×**.

95% recovery is reached at **86–130 seconds**, which brackets the NCAA cap almost exactly.

**So: "is the 120-second cap costing him?" — No, on this channel, and not close.**

---

## 4. The warm-up-pitch decision, priced (F-362)

**DERIVED.** A warm-up pitch thrown at time *t* leaves (120 − *t*) seconds to repay its own depletion `d`:

| Last warm-up at | time left | share of that pitch's `d` repaid |
|---|---|---|
| 40 s | 80 s | 84–94% |
| 60 s | 60 s | 75–87% |
| 80 s | 40 s | 60–75% |
| 100 s | 20 s | 37–50% |
| 110 s | 10 s | 21–29% |

Worst case — moving the last warm-up from t = 40 s to t = 110 s — leaves roughly **0.6 of ONE pitch's depletion** unpaid. Against the steady-state inter-pitch deficit he already carries on *every* pitch at 20-second tempo (**1.0–1.7 × d**, F-327), the entire timing decision is worth **35–60% of a deficit that is present all outing anyway.**

The thermal benefit of that same 70-second shift is **0.1–0.3 °C ≈ 0.3–0.9% of lower-body power** (§2), which §2 forbids converting.

**Both channels are small and they partly cancel.**

### The one asymmetry worth keeping

Past the first minute he is already 94%+ recovered, so a late warm-up pitch costs almost nothing metabolically, while the thermal benefit of throwing late is monotone. **If a pitcher wants a rule: take the break, then warm up at the end of it — not throw early and sit.** That is a tiebreaker, not a lever, and it should be presented as one. Coach the warm-up *count* for rhythm and the catcher's throw-down, which is what it is actually for.

---

## 5. ⚠️ THE LONG HALF-INNING — where the half-time literature actually applies (F-363)

**This is the part of the topic that is not small.**

The soccer re-warm-up evidence is calibrated to **15 minutes**. The routine inning break is **two**. The 15-minute interval in a baseball game is not the break — **it is the half-inning in which your own offence bats around.** That is where §2's 1.5 °C is in range rather than being scaled down by a factor of five, and it is the only case in this topic where a re-warm-up could plausibly matter.

It is also, unusually for this corpus, **checkable**.

**Outcome:** first-fastball velocity of each half-inning, split by the duration of the preceding offensive half-inning.

| Within-pitcher release-speed SD | detect 0.3 mph | 0.5 mph | 0.8 mph | 1.0 mph |
|---|---|---|---|---|
| 0.8 mph | 112/group | 41 | 16 | 11 |
| **1.0 mph (F-289 working value)** | **175** | **63** | **25** | **16** |
| 1.2 mph | 252 | 91 | 36 | 23 |

**Supply:**
- **One starter:** ~6 innings × 12 starts = **72 first-pitches a season**; ~15–20% follow a long half-inning = **11–14**. Five seasons short.
- **The whole staff:** ~55 games × ~9 half-innings = **~495 first-pitches**; **74–99** follow a long half-inning. **Enough for 0.5 mph in one season.**
- **The bullpen A/B, cheaper still:** paired within-pitcher, 120 s sit vs 120 s sit + re-warm-up — **0.8 mph in 8–18 pitch-pairs, 0.5 mph in 21–46.** One to two sessions.

> The pattern this corpus keeps finding, arriving again: **unanswerable about one pitcher, answerable about the staff** (F-273, F-286, F-342), and **the lever is far cheaper to measure than the outcome** (F-320, F-321).
> ⚠️ **Prefer the bullpen.** The observational version is confounded — long half-innings mean your team is scoring, which moves score margin, leverage and who is at the plate.

---

## 6. ⚠️ THE TRANSFER IS BROKEN AT BOTH ENDS (F-358, F-359)

This is the cycle's sharpest result, and it cuts **against** the intervention.

**End one — what re-warm-up moves.** González Fernández et al. 2023 (PMC10108754, read in full), 892 records screened, **4 studies reviewed, 3 meta-analysed**:

| Outcome | Effect size | p | I² |
|---|---|---|---|
| **Vertical jump height** | **0.66** | **0.001** | 0.0% |
| **Linear sprint time** | 0.19 | 0.440 | 38.4% |

Risk of bias: one study "some concerns," two "high," one "some concerns." **No study rated low.**

**The one quality it reliably improves — jump — is a registered NULL for pitch velocity in this corpus (F-004, r = 0.07 NS).** The quality that did *not* move — a horizontal, cyclic, whole-body sprint, the closer analogue to a delivery — is the one you would have wanted.

**End two — what pitching does to jump.** PMC6028199 (read in full): 18 collegiate pitchers, **117 maximal pitches over 9 innings**. Ball velocity fell 130.3 → 127.8 km/h (**1.55 mph**, P = 0.001). Isometric hip abduction and adduction fell (P = 0.009, P = 0.001). **Every squat-jump variable was unchanged** — height, mean power, peak power, mean velocity, peak velocity, all NS, two of them in the wrong direction.

**So: the re-warm-up literature moves jump, and jump does not respond to pitching. Both links in the chain are broken independently.**

> **The warning to carry.** This argument will arrive in your program wearing the strongest credential in sports science — *randomised, controlled, meta-analysed*. **A real intervention on the wrong outcome is not weaker evidence than a cross-sectional study on the right one. It is a different error, and it is harder to see, because the design looks impeccable.**

---

## 7. ⚠️ THE POPULATION AUDIT — every manipulated study here fails the floor (F-361)

| Study | Design | Mean velocity |
|---|---|---|
| F-323 — slide step (PMID 22487194) | within-subject | **76 mph**, age 17.6 |
| F-329 — Yang 2016 inter-pitch interval (PMID 27434082) | randomised, counterbalanced, n = 7 | **not reported anywhere** |
| F-359 — simulated 9 innings (PMC6028199) | repeated measures, n = 18 | **80.96 mph** |
| F-360(b) — Bishop 2016 cooling (JSCR 30(4)) | crossover, n = 8 | **~69.8 mph** |
| F-360(a) — palm cooling (PMC12360938) | crossover, n = 22 | **~67.0 mph**, and *throws*, not pitches |
| F-358 — re-warm-up meta-analysis | RCTs, k = 3 | **soccer; no throwing outcome at all** |

**Median pitching sample: n = 13. Not one clears 85 mph. The closest is four mph short.**

> **The operating rule this forces:** on this topic the **causality** tag and the **population** tag point in opposite directions, **and the population tag wins.** An INTERVENTION at 67 mph is not better evidence for an 88 mph starter than a CROSS_SECTIONAL study at 92 — it is differently wrong, and the strong design makes it *more* persuasive than it deserves to be.
> This is the mirror image of the corpus's founding error. F-043/F-044/F-045 was a cross-sectional finding sold as a lever. **This is a lever, correctly identified as a lever, measured on somebody else's arm.**

---

## 8. Cooling — the only thing anyone has actually manipulated on a pitcher between innings (F-360)

Two crossover studies have manipulated the between-innings interval for throwers, and **both cooled rather than re-warmed** — the opposite of the industry's instinct.

- **PMC12360938** (*J Hum Kinet* 2025, read in full), n = 22 D-II baseball athletes, 5 × 10 max throws, 3-min recovery, palm immersion in 10 °C water vs none:
  - **No-pain subgroup (n = 10): +0.62 mph mean, +0.81 mph max**, better accuracy and arousal.
  - **Pain subgroup (n = 12): −2.61 mph mean, −2.30 mph max.** Both p < 0.05. RPE lower under cooling in both.
  - ⚠️ **The responder split is POST HOC, on a variable measured after treatment, at n = 10 and n = 12** — the design that manufactures subgroup differences.
  - ⚠️ **The harm arm is four times larger than the benefit arm.**
- **Bishop SH et al. (2016)**, *JSCR* 30(4):1027–1032 — **existence verified, substance snippet-only, article not opened** (paywalled, not in PMC). Reported n = 8, 4 min of local cooling to deltoid and forearm in a 6-min recovery, reported +0.6 m/s (**+1.34 mph**) overall with significance in innings 4–5.

**Do not act on this.** It is 67–70 mph, n = 8–22, and one of the two is unread. It is in this file because **an industry Substack is currently circulating the Bishop result as "four minutes of ice might save your sixth inning," with the magnitude stated and the 70 mph sample not** — so it will arrive in your clubhouse whether or not this corpus invites it.

---

## 9. What to actually do

1. **Stop arguing about warm-up count and timing on the routine break.** §4: worth a fraction of one pitch. If you want a default, *take the break and warm up at the end of it* (§4).
2. **The 120-second cap is not hurting him.** §3: 94–98% recovered, and the seconds the rule removes are worth a twentieth of the seconds it leaves.
3. **Treat the long half-inning as a different situation, and test it.** §5: one bullpen, 8–18 pitch-pairs for 0.8 mph, or pool the staff for one season.
4. **Do not monitor between-innings readiness with a jump test.** §6, end two: 117 max-effort pitches did not move a single squat-jump variable.
5. **Do not ice.** §8: 67 mph samples, post-hoc subgroups, and a harm arm four times the benefit arm.

---

## 10. Gaps this file opens

- **No muscle-temperature measurement of a throwing arm between innings, in any population.** Every number in §2 is a leg measurement from soccer, scaled.
- **No manipulation of the between-innings interval LENGTH, for throwers, anywhere.** Every study in §7 manipulated what happens *inside* a fixed interval; nobody has varied the interval.
- **No pricing of the warm-up-pitch count itself** — how many actually serve an 85+ starter. The rule change created the decision in 2025 and no one has studied it.
- **`d`, the per-pitch phosphagen depletion — now blocking TWO topics** (F-336, and §3–§4 here).
- **The hip abduction/adduction fatigue result in PMC6028199** (d = 0.41 / 0.47, correlated r = 0.583 with 9th-inning velocity loss) is live, source-verified, and **not this topic.** Flagged for a future cycle.
