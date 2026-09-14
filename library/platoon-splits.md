# PLATOON SPLITS — WHAT A HANDEDNESS NUMBER CAN AND CANNOT TELL YOU

**Created 2026-09-14 (Cycle 13).** Findings **F-337 → F-350**.
Companion to [`FINDINGS.md`](../FINDINGS.md). Population: **elite, 85 mph floor** — showcase/D1-committed HS through pro.

> **⚠️ PROVENANCE, STATED FIRST.**
> **§2, §4, §5, §6, §7 are DERIVED IN-CYCLE** — closed-form arithmetic, re-derivable in fifteen lines, no source required.
> **§3 rests on ONE snippet-level empirical constant** (Cross's 1,670 / 570 harmonic PA). **The page was never opened**; `sabr.org` and `tht.fangraphs.com` were both refused by the egress proxy. It is corroborated by an independent plausibility screen (§3.2) and it is **queued for verification**.
> **§9 is SOURCE-VERIFIED** — the NCAA rules document was downloaded and read in full.
> **Every league constant here is MLB-derived. There is no NCAA platoon estimate anywhere in this corpus or, as far as this cycle could find, anywhere public. See Dispute #26b.**

---

## 1. Why this file exists

`platoon` appeared **14 times** in `FINDINGS.md` and **zero times** in `INDEX.md` before today. Every one of those 14 was a *modifier* on some other finding — arm slot is platoon-dependent (F-071), the sweeper's platoon table (F-157), the league dropping the sinker to lefties (F-158), stuff models not pricing platoon (F-168). **The split itself was never a topic**, and the coach's actual question had never been asked:

> *He's got a reverse split. Is that real?*

It is a near-perfect target for this program because it is the **marker-versus-lever** problem in its purest form — and because, unlike stride length and extension where the corpus had to *discover* the trap after the fact, here the trap can be **proved closed in advance, arithmetically, before anyone acts on a number.**

---

## 2. The structure: why a split is worse than what it splits

### 2.1 The principle (F-350)

A split is **a difference of two sample means**. That does two things at once, in opposite directions:

- **The noise DOUBLES.** Var(D) = σ²/n₁ + σ²/n₂ = 2σ²/H, where H is the harmonic mean of the two counts. You are not measuring one noisy thing; you are subtracting two.
- **The signal SHRINKS.** True *platoon skill* varies far less between pitchers than true *overall quality* does — **18 wOBA points against 30–50** (§3.2, §5).

Reliability is signal over signal-plus-noise. **A split attacks it from both ends simultaneously.**

This is not a fact about platoon splits. It is a fact about **every split statistic**: times-through-order, home/road, count, RISP, first-half/second-half, day/night, "since the break." **F-286's 790-season result is this principle with one set of numbers plugged in.**

The corpus has now derived the same wall **three independent ways** — F-273 (usage, 60,000+ pitches), F-286 (TTO, 790 seasons), F-337/F-340 (platoon, arithmetically unavailable). **Three independent routes converging is the strongest internal consistency check this corpus has produced.**

### 2.2 The per-PA noise floor

Recomputed independently this cycle from standard wOBA weights and an ordinary outcome distribution (BB .095 @ .70, 1B .142 @ .89, 2B .044 @ 1.27, 3B .004 @ 1.62, HR .032 @ 2.10, outs remainder):

> mean wOBA **0.3224**, per-PA SD **0.5269**

**F-286 holds 0.531 from a different weight set — agreement to 0.8%.** The corpus's number is sound. **σ_PA = 0.531 is adopted throughout below.**

### 2.3 The college starter's budget (F-337)

F-286's college weekend-starter budget: **~308 BF/season** (14 starts × ~22 BF).

| Opposite-handed share | n_opp | n_same | Harmonic PA | **SE of the observed split** |
|---|---|---|---|---|
| 40% | 123 | 185 | 148 | **61.8 pts** |
| 45% | 139 | 169 | 152 | **60.8 pts** |
| 50% | 154 | 154 | 154 | **60.5 pts** |
| 55% | 169 | 139 | 152 | **60.8 pts** |

**≈61 wOBA points of pure sampling noise on a full season's split**, near-invariant to lineup handedness — which matters practically: *you do not need to know your opponents' handedness mix to know the number is unusable.*

> **For scale: 61 points is more than twice the entire league-average platoon effect. The measurement error exceeds the phenomenon by a factor of 2.3.**

---

## 3. The one empirical input, and the screen it passed

### 3.1 The constants (F-338) — SNIPPET-ONLY

**Jared Cross, "Forecasting Pitcher Platoon Splits," The Hardball Times, 14 Aug 2015.** Two independent WebSearch retrievals returned identical figures and attribution:

> RHP observed splits should be regressed by adding **~1,670 harmonic plate appearances**; LHP, **~570**.

**"Harmonic PA" is exactly the right unit**, because Var(D) = 2σ²/H. That is not a coincidence of phrasing — it makes his constant directly comparable to a quantity derivable without him.

### 3.2 The plausibility screen — and its honest limit

c = 2σ²_PA / σ²_true. Inverting:

| | Cross's *c* | **Implied σ_true of platoon skill** |
|---|---|---|
| RHP | 1,670 | **18.4 wOBA pts** |
| LHP | 570 | **31.5 wOBA pts** |

Forward, from an independent bracket of σ_true:

| σ_true | Derived *c* |
|---|---|
| 15 pts | 2,506 |
| **18 pts** | **1,741** (vs published 1,670 → **+4.3%**) |
| 20 pts | 1,410 |
| 25 pts | 902 |
| **31 pts** | **587** (vs published 570 → **+3.0%**) |

> **⚠️ WHAT THIS IS AND IS NOT (conceded under cross-examination, Dispute #26 lineage).**
> **It is NOT a replication.** σ_true was derived *from* Cross's constant, so the forward table cannot independently confirm it. That direction is circular and the brief's own rules require saying so.
> **It IS a plausibility screen, and a real one.** The non-circular quantity is **σ²_PA = 0.531², computed from wOBA weights with no reference to Cross whatsoever and recomputed this cycle to within 0.8%.** His constants imply a true platoon-skill spread of 18 and 31 wOBA points — *physically sensible magnitudes for a real skill*. Had they implied 200 points or 0.5 points, the number would have been exposed as fabricated or as a different statistic entirely.
> **What it genuinely validates is the CORPUS's per-PA variance** (F-286, F-289), which just survived an outside check it did not know it was taking.
> **The Cross page remains in the verification queue at full priority.**

### 3.3 The LHP/RHP asymmetry (F-341)

σ_true is **1.71× larger for left-handers**.

| | Harmonic PA for r = 0.50 | **College seasons to get there** |
|---|---|---|
| RHP | 1,670 | **11.0** |
| LHP | 570 | **3.7** |

**A four-year left-hander is the only pitcher on the roster whose handedness numbers will ever say anything.** For every right-hander, at every college career length, the answer is no.

**Hypothesis, explicitly untested:** the larger lefty spread may be **arsenal variance**, not handedness. A left-hander facing a mostly right-handed world is selected on having *something* for opposite-handed hitters, and the ways of having it (changeup, cutter, high slot, crossfire) differ a lot; right-handers face a mixed diet and converge. **If that is right, the split is partly a readout of arsenal construction and becomes a development variable rather than a roster note.** Nobody has tested it. → **Tomorrow's question 2.**

---

## 4. The numbers a coach will be handed

### 4.1 Reliability (F-337)

σ_true = 18.4 pts (RHP):

| Sample | Harmonic PA | Reliability | **You keep** |
|---|---|---|---|
| 1 season | 152 | 0.084 | **8%** |
| 2 seasons | 305 | 0.154 | 15% |
| 3 seasons | 457 | 0.215 | 22% |
| **Full 4-year career** | 610 | 0.267 | **27%** |

### 4.2 One in three (F-339)

SD(observed) = 63.5 pts:

| True league split | P(observed < 0) | **On a 12-man staff** |
|---|---|---|
| 20 pts | 0.376 | **4.5 pitchers** |
| 27 pts | 0.335 | **4.0 pitchers** |
| 35 pts | 0.291 | **3.5 pitchers** |

> **Every season, ~4 of your 12 pitchers show an apparent reverse split — and it is a different 4 next year.**
> **THE TURNOVER IS THE TELL, AND IT IS FREE TO CHECK.** Pull two seasons of your own game logs, list the reverse-split names each year, compare. If the lists barely overlap, the statistic is noise and the whole room can see it in five minutes. **The cheapest demonstration in this corpus.**

### 4.3 The closing result (F-340)

r = 0.084, prior mean +27 pts, posterior SD 17.6 pts:

| Observed split | Posterior mean | **P(truly reverse-split)** |
|---|---|---|
| −100 pts | **+16.4 pts** | 0.176 |
| −150 pts | **+12.2 pts** | 0.244 |
| −200 pts | **+8.0 pts** | 0.324 |

To reach even odds you must observe **−296 points**: **5.1 SD**, p = **1.9 × 10⁻⁷** per pitcher-season, **0.00001** expected occurrences on a 12-man staff over four years.

> ### **No college right-hander will ever, in a college career, generate the evidence required to conclude he has a reverse platoon split.** Not unlikely. **Arithmetically unavailable.**

---

## 5. The doctrine (F-342)

Same pitcher, same plate appearances, two quantities:

| Quantity | σ_true | Reliability at ~250–308 PA |
|---|---|---|
| **Overall quality (q)** | 30–50 pts | **0.44 – 0.73** (~0.6) |
| **Platoon split (s)** | 18.4 pts | **0.084** |

**Seven times the reliability, from the very same events.**

> **Spend all estimation effort on q. Assign every pitcher the league-average s. Move on.**
> **Splitting a sample does not reveal hidden information — it destroys the information you had.**

---

## 6. Deployment (F-343)

Write performance as q ± s/2. Facing an opposite-handed hitter, the switch gains **(q_out − q_in) + s**.

> **DECISION RULE: make the switch unless the incoming pitcher is worse in overall quality by more than s ≈ 27 wOBA points** (bracket 20–35).

Because q is ~7× better estimated than s, **the quality gap is the term you can know and the split is the term you must assume.**

**Season price** (wOBA scale 1.25 → 27 pts = 0.0216 runs/PA):

| Decisions/season | × 1.0 PA | × 1.5 PA | × 2.0 PA |
|---|---|---|---|
| 40 | 0.86 R | 1.30 R | 1.73 R |
| 60 | 1.30 R | **1.94 R** | 2.59 R |
| 80 | 1.73 R | 2.59 R | 3.46 R |

**Central estimate ≈ 1.3 – 2.6 runs/season.**

> **FIFTH TACTICAL QUESTION THE CORPUS HAS PRICED, AND THE FOURTH TO LAND BETWEEN 1 AND 3 RUNS A SEASON** (running game F-319, times-through-order, count leverage, now this). These decisions are real, roughly equal to one another, **and none of them is where a season is won.**

**Audit the DECISIONS against the rule, never the outcomes.** 60 decisions × 0.02 runs is invisible forever (F-273). Compliance is 100% achievable and checkable in an afternoon.

---

## 7. The lever, and the compliance check (F-346, F-347)

### 7.1 What is associated with a small split — ALL CROSS-SECTIONAL

Snippet-level (Cross; FanGraphs arm-angle work):
- Small/reverse-split pitchers throw **more changeups and curveballs, fewer sliders**.
- **More VERTICAL movement → smaller/reverse splits. More LATERAL → larger.**
- **Sidearm RHP show especially large gaps**; higher slots, smaller.

### 7.2 The corpus reached the same place from different data

- **F-157** (ESTABLISHED): sweeper RV/100 RHP→RHB **−0.94**; RHP→LHB **−0.05** where the *ordinary slider* is **−0.35**. *Against opposite-handed hitters the sweeper is the worst pitch in the comparison.*
- **F-158**: RHP sinker usage to LHB collapsed **21% → 9.7%** — the league's answer to the sinker's platoon problem was to stop throwing it.
- **F-071**: lower arm angle = same-handed weapon, contraindicated opposite-handed.

**Three vault findings and one outside model, different data, same physics.**

### 7.3 ⚠️ AND IT IS STILL A MARKER

**Nobody has manipulated an arsenal and measured the resulting change in a split.** Not Cross, not Driveline, not anyone found this cycle. **This is the F-043/F-044/F-045 stride-length structure transplanted into arsenal design.**

**What rescues it from being only a marker:** the mechanism is **forward-derivable geometry** — where a pitch moves relative to a barrel path is a trajectory, not an association — a stronger footing than stride length ever had.
**What does not rescue it:** nothing. **Never attach a magnitude.**

**Safe to say:** *"your sweeper is a right-handed weapon and will never be anything else"* (a pitch-level run value, not a between-pitcher correlation); *"you need one pitch that goes toward a left-hander's hands."*
**Never say:** *"adding a changeup will shrink your split by X points."*
**Common failure mode:** the pitcher "fixes" it by dropping his slot — which per F-071 makes the platoon problem **worse** while raising elbow varus torque (F-070).

### 7.4 The measurable check — COMPLIANCE ONLY (F-347)

| | Budget |
|---|---|
| Detect a **usage** shift 9% → 22% vs opposite-handed hitters (α .05, 80% power) | **120 opposite-handed pitches ≈ 4 starts** |
| Usage precision at 22% true, n=400 | **±4.1 pts (95%)** |
| Detect the **run-value benefit** of a 20 pp usage correction (F-273) | **61,319 – 137,969 pitches** |
| A college season | **~1,600 pitches** |

> **VERIFY HE THREW IT. NEVER TRY TO VERIFY IT WORKED.** Three orders of magnitude separate the two budgets.

---

## 8. The fatigue channel — where physiology actually enters (F-348)

The anatomist's first move is to **decline the question**. There is no tissue-level account of a platoon split. Nothing adapts; no motor unit recruits differently against a left-handed hitter. **The split is geometry and perception.** Saying so is the contribution — the corpus's standing failure mode is an agent manufacturing relevance.

**But there is one real handle.** The opposite-hand weapon is almost always a **changeup or splitter** — a pitch whose entire effect depends on a *velocity and spin differential held by forearm and wrist positioning*, not gross force output. **F-127**: command and secondary-pitch finish degrade **before** velocity. Therefore:

> **The opposite-hand weapon is the first thing fatigue takes away. A starter's platoon disadvantage should widen WITHIN an outing, and widen BEFORE any velocity decline is visible on the gun.**

**Measurable consequence: FB−CH velocity separation, bucketed by pitch number.**

| Within-pitcher release-speed SD | 1.0 mph loss | 1.5 mph | 2.0 mph |
|---|---|---|---|
| 0.8 mph | 10 CH/bucket | 4 | 3 |
| **1.0 mph** (F-289 working assumption) | **16** | **7** | **4** |
| 1.2 mph | 23 | 10 | 6 |

A college starter throws ~12–18 CH/start → **~6–9 per early/late bucket.**

> **A large separation collapse (≥1.5 mph) is visible in a SINGLE START. A subtle one (0.5 mph) needs ~60/bucket ≈ eight starts pooled.**

**Third fast instrument the corpus owns**, beside F-320 (five pitches) and F-331. **And it is falsifiable inside one season:** if separation does *not* erode before velocity does, the mechanism is wrong.

⚠️ **EIGHTH INSTANCE of the recurring gap:** the corpus holds **no within-pitcher SD of FB−CH velocity separation for an 85+ arm.** It is in every program's TrackMan log. Nobody has published it. (F-264, F-289, F-307, F-295, F-320, F-336 ×2, now this.)

---

## 9. ✅ SOURCE-VERIFIED — the rules that govern the matchup (F-344, F-345)

Downloaded and read in full: **NCAA, *2025 and 2026 Baseball Rules Changes***, Baseball Rules Committee / Playing Rules Oversight Panel — `ncaaorg.s3.amazonaws.com/championships/sports/baseball/rules/2025-26PRMBA_RulesChanges.pdf` (130,493 bytes).

### 9.1 No three-batter minimum

Full-text search for `three batter`, `3 batter`, `disengage`: **zero hits.** **A college coach may change pitchers for a single batter, freely. The matchup lever is fully available to Tommy and is NOT available to his MLB counterparts.**

Snippet-level: a **three-batter minimum** is proposed as a **conference-experimental rule for 2026-27**, alongside **a two-disengagement limit per batter**. ⚠️ **That second rule is the one the running-game cycle already logged (F-322) — from the same package. The corpus logged one item and missed the other. Read rule proposals as packages.**

**If the SEC adopts it:** the matchup still buys ~27 points but commits you across **three** batters, and §6's rule must be re-derived against a mixed-handedness sequence. That will kill most one-batter moves. **Watch item.**

### 9.2 Verified clock facts, and a correction

| Rule | Verified content |
|---|---|
| Pitch clock | **20 seconds** |
| Batter alert | **8 seconds** remaining (amended down from 10) |
| **Between innings** | **120 s, UNLIMITED warm-up pitches** (Rule 9.2.i) |
| **Relief pitcher** | **150 s, unlimited warm-ups**; timer starts when he crosses the warning track |
| Mound visit | **30 s**, umpire proceeds at 9 s; on expiry the 20-second pitch clock commences |
| Between batters | 30 s (permissive by conference rule) |

> ### 🔧 CORRECTED 2026-09-14 — INDEX.md §5 and `daily/2026-09-13-report.md`
> Recorded there: the between-inning break is *"uncovered — dominates the recovery budget and **the clock does not touch it**."*
> **The final clause is WRONG.** The interval is capped at **120 seconds** (150 for a reliever), and the 2025 change converted the warm-up allowance from a **pitch COUNT** to a **TIME BUDGET**.
> **Why it was wrong, so it cannot be re-imported:** asserted in a fully-blocked cycle from the reasonable prior that a "pitch clock" governs only the interval *between pitches*. **The rulebook governs the whole dead-ball economy.**
> **Why it matters for pitching:** F-330 argued the clock removes the *cheapest* seconds. The 120 s cap is the opposite case — **a hard ceiling on the longest and most physiologically valuable recovery interval a starter gets** — and the pitcher now **chooses how to spend that fixed budget.** Unpriced anywhere. → **Tomorrow's question 3.**

---

## 10. Field-sweep verdicts

| Item | Verdict |
|---|---|
| Cross's 1,670 / 570 constants | **PROMISING — best public answer, passes an independent plausibility screen. QUEUED, NOT VERIFIED** |
| **"100 PA makes a split reliable"** (fantasy/betting pages) | **DEBUNKED (F-349).** r = 100/(100+1670) = **5.6%**. Off by **~17×** |
| Vertical→small / lateral→large splits | **PROMISING as MECHANISM, CROSS_SECTIONAL as evidence.** Never a lever |
| Arm angle vs release point asymmetry (FanGraphs) | **UNPROVEN.** Snippet-only, cross-sectional, and the source already carries a known anomaly (F-071) |
| NCAA 3-batter minimum + 2-disengagement proposal | **WATCH ITEM (F-344)** |
| NCAA ABS approved as an option for next season | **WATCH ITEM — bears on F-283 and Dispute #20b. QUEUED** |
| Driveline / Tread on platoon-specific arsenal design | **NULL RESULT.** Nothing found beyond general changeup-grip content. **The industry is not publicly working on this** (F-321 precedent) |

---

## 11. What this file does NOT cover

- **Any NCAA platoon estimate.** Every league constant here is MLB. **Dispute #26b.**
- **Hitter platoon splits** — a different (and better-behaved) problem.
- **Whether the LHP spread is arsenal variance** — §3.3's hypothesis, untested.
- **Left-on-left specialist usage patterns**, bullpen construction, or roster-building around handedness.
- **Any intervention.** Nobody has changed an arsenal and measured a split.
- **The between-inning warm-up decision** newly opened by §9.2.

## 12. New gaps this file opens

1. **No NCAA platoon-split estimate exists** — every constant in this file is imported from MLB.
2. **No within-pitcher SD of FB−CH velocity separation at 85+** — eighth instance of *already in your data, published by nobody*.
3. **No test of whether the LHP/RHP platoon-spread asymmetry is arsenal variance.**
4. **No intervention anywhere** that manipulated an arsenal and measured a split change.
5. **No pricing of the 120-second between-inning warm-up budget** — how many warm-ups actually serve an 85+ starter.
