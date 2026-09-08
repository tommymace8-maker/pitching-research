# Times Through the Order, and the Within-Outing Decline

**Created 2026-09-08.** Closes half of the flagged gap "times-through-the-order, sequence/order effects" (INDEX §5).
Companion to [`pitch-mix-sequencing.md`](pitch-mix-sequencing.md) and [`count-leverage.md`](count-leverage.md).

> ### ⚠️ RUN CONDITION — FIFTH CONSECUTIVE FULLY EGRESS-BLOCKED CYCLE
> Every outbound host returned **403 at the CONNECT stage**, including `en.wikipedia.org` as a control. `WebFetch` returned `EGRESS_BLOCKED` at tool level. **No primary source was opened.** (F-277, now F-285.)
> **Everything in §2, §3, §4 and §6 of this file is arithmetic computed in-cycle and depends on no source.** It is re-derivable in thirty lines of Python.
> **§1 and §5 rest on snippet-level reports and are flagged inline.** The one empirical magnitude imported from a snippet — the ~10 wOBA points per time through the order — is bracketed everywhere it is used, and **every ratio and every detection result in this file is independent of it except where explicitly stated.**

---

## 0. The question, stated so it can be answered

A coach asks one of three different questions and usually does not notice which:

1. **"Do hitters do better the third time they see him?"** — a *league* question about a *population*.
2. **"Does *my* guy fall off the third time through?"** — an *individual* question.
3. **"Should I pull him right now?"** — a *decision* question, which is neither of the above.

This file's central result is that these three have wildly different answers, and that **the answer to (2) is: you will never know, and it does not matter, because (3) does not depend on it.**

---

## 1. What the literature reports — SNIPPET-ONLY, NOT VERIFIED

**The paper.** Brill, Deshpande & Wyner, *"A Bayesian analysis of the time through the order penalty in baseball,"* **Journal of Quantitative Analysis in Sports**, 2023. DOI `10.1515/jqas-2022-0116`. arXiv preprint `2210.06724` (2022). Also hosted at `wsb.wharton.upenn.edu/wp-content/uploads/2023/08/Ryan-Brill_Research-Paper.pdf` and on Deshpande's page `skdeshpande91.github.io/publications/2023-05-17-TTOP`.

> **⚠️ CORRECTION TO THE CORPUS — `CORRECTED 2026-09-08`.**
> **F-258 records this work as "Brill & Wyner 2022."** Two independent snippets this cycle, one of them the second author's own publications page, give the author list as **Brill, Deshpande & Wyner** and the journal year as **2023** (arXiv preprint 2022). **Deshpande was omitted.** The finding's *substance* was already quarantined as unverified and is unchanged; **the citation was wrong and is corrected here.** Do not re-import "Brill & Wyner 2022."

**What the snippets say it found**, consistently across three separate searches:

| Reported | Status |
|---|---|
| Batters improve relative to the pitcher by **~10 wOBA points per time through the order** | **SNIPPET-ONLY.** Used in this file as a bracketed input, never as a verified number |
| Expected wOBA rises **steadily and continuously** across the game | **SNIPPET-ONLY** |
| The **discontinuity** parameters at the TTO boundaries have posteriors "covering both positive and negative values, mostly centred around 0" — **no evidence of a sharp step** | **SNIPPET-ONLY** |
| Design: games where the starter was pulled before the 3rd time through were **removed**, so results are conditional on surviving the 2nd time through — done to balance the sample on pitcher quality | **SNIPPET-ONLY**, but a specific and checkable methodological description |

**⚠️ THE DISTINCTION THAT MATTERS, AND WHY F-258'S ONE-LINE SUMMARY WAS MISLEADING.** F-258 records this as "little evidence of a strong batter learning effect," which reads as *the TTOP is not real*. That is **not** what the snippets describe. They describe a **decline that is real and roughly 10 wOBA points per cycle, but CONTINUOUS in batters faced rather than STEPPED at the lineup turn.**

Those two readings give **opposite** managerial instructions:

- **Stepped** → the lineup turning over is the event. Pull him *before* the third time through, regardless of pitch count.
- **Continuous** → the lineup turning over is a *clock*, not a cause. The decision variable is **cumulative exposure** (batters faced / pitch count), and "third time through" is merely the label that happens to sit near it.

**The corpus should hold the continuous reading as the live hypothesis and the stepped reading as the folk one — but neither is verified, because no page was opened.** See §5 for what separates them.

---

## 2. The arithmetic that kills question (2): one pitcher's own TTOP is unmeasurable

### 2.1 The noise floor of a plate appearance

wOBA per PA is a lottery ticket. Using standard weights and an ordinary outcome distribution (BB .085, HBP .012, 1B .145, 2B .045, 3B .004, HR .033, outs .676):

- mean wOBA = **0.329**
- **per-PA SD = 0.531**

Sensitivity: the SD is driven almost entirely by the home-run share. At HR = 2.0% the SD is 0.492; at 5.0% it is 0.576. **Every result below is stable across that range**, because n scales with σ² and the σ² range is ±17%.

### 2.2 How many plate appearances to see it

Two-sample, α = .05 two-sided, 80% power, σ = 0.531:

| True individual TTO penalty | PA needed **per group** | College seasons of 3rd-time PA |
|---|---|---|
| 0.010 wOBA (the reported league value) | **44,200** | **790** |
| 0.020 wOBA (2× league) | 11,100 | 197 |
| 0.030 wOBA (3× league) | 4,900 | 88 |
| 0.050 wOBA (**5× league** — implausibly large) | 1,800 | **32** |
| 0.100 wOBA (10× league — absurd) | 440 | 8 |

**The season budget.** A college Friday starter: ~14 starts × ~22 batters faced = **~308 BF/season**. He faces the lineup once (9), twice (9), and gets ~4 batters into the third pass — so **~56 third-time PA per season.**

> **A pitcher would need roughly 790 college seasons to detect his own league-average times-through-the-order penalty. A penalty FIVE TIMES the league average would take 32 seasons.**
> This is not a small-sample caution. It is a statement that the quantity does not exist as a measurable individual property at any career length.

**This is the same wall as F-273 (pitch mix: 60,000 pitches) and F-282 (full counts: 17 seasons), and it is the most extreme instance yet.** Add it to the pattern: *the things a coach most wants to know about one athlete are precisely the things one athlete cannot generate enough events to answer.*

---

## 3. The bias that manufactures the penalty in a coach's own scorebook

This is the finding of the cycle, and it is pure composition.

**The mechanism.** A starter's first and second times through the order are **complete passes** — he faces all nine lineup slots. His third time through is **truncated**: he faces slots 1, 2, 3, … up to wherever he is pulled. **Lineup slots 1–4 are the best hitters on the roster.** So the third-time sample is drawn disproportionately from the *top* of the order while the first- and second-time samples are drawn from the *whole* order.

**The size of it.** Take a plausible college lineup talent profile (wOBA by slot: .345 .350 .355 .350 .330 .315 .300 .290 .275; full-lineup mean **.3233**):

| Pulled after *k* batters in the 3rd pass | Talent of the TTO3 sample | **Composition bias** |
|---|---|---|
| k = 1 | .3450 | **+.0217** |
| k = 2 | .3475 | **+.0242** |
| k = 3 | .3500 | **+.0267** |
| k = 4 | .3500 | **+.0267** |
| k = 5 | .3460 | **+.0227** |
| k = 6 | .3408 | +.0175 |
| k = 7 | .3350 | +.0117 |
| k = 8 | .3294 | +.0060 |
| k = 9 (complete pass) | .3233 | **0** |

**Typical k = 3–5 → composition bias ≈ +0.025 wOBA.**

> ### The reported league-wide TTOP is ~0.010 wOBA per cycle. The composition bias in the naive calculation is **+0.025 wOBA**. The artefact is roughly **2.5× the entire real effect**, and it points in the direction that creates it.

**What the coach actually observes.** If the true within-pitcher effect across two cycles is 0.020 wOBA, and the composition bias adds 0.025:

- observed naive gap = **0.045 wOBA**
- **56% of what he sees is lineup slot, not his pitcher.**

**Two things this does and does not say.**

- **It does not accuse the published literature.** Brill/Deshpande/Wyner adjust for batter quality explicitly (per the snippet), and any competent analysis does. **This is an indictment of the calculation a coach, a broadcaster or a front-office intern performs on a scorebook or a season split** — which is the version that actually reaches a dugout decision.
- **It is bias-in-expectation, not noise.** It does not average out with more starts. Fourteen starts of it produce the same +0.025, more precisely estimated. **More data makes this error more confident, not less.**

**The fix costs nothing:** compare the third time through **only against the same lineup slots** the first and second times through — slots 1–4 vs slots 1–4. That removes the entire bias. It also removes most of the sample, which returns you to §2.

---

## 4. The decision (question 3), which does not need either answer

The pull decision is not "is there a TTOP." It is a **comparison of two arms.**

Let the tired starter's penalty at this moment be Δ wOBA relative to his own fresh self, and let the fresh reliever be *G* wOBA points worse in true talent than the fresh starter. **Leaving the starter in is correct whenever Δ < G.**

Using the reported league magnitude, Δ at the third time through ≈ **0.020 wOBA** (two cycles × 10 points).

> **The break-even is a 20-wOBA-point talent gap.** If your bullpen arm is more than about 20 points of wOBA worse than your starter — and in a college program, arm #6 out of the pen usually is, by far more than that — **leaving the starter in is the correct decision even granting the penalty in full.**

**What the whole decision is worth.** Converting at the standard ~1.15 runs per PA per unit wOBA:

- 10 wOBA points per cycle = **0.87 runs per 100 PA per exposure**
- The cost of letting an **equal-talent** starter face 4 batters a third time rather than a fresh **equal-talent** arm: **0.070 runs per start**
- Over a 14-start college season: **≈ 1.0 run.**

> **The entire third-time-through question is worth about one run a season to a college starter, and only if you have an equally good fresh arm — which is the condition that is almost never true.**
> Compare F-280: 0-2 count optimisation is worth ~0.2 runs a season. This is the same order of magnitude. **Both are real, both are arithmetically confirmed, and both are too small to spend a coaching week on.**

**Where the real money is:** the talent gap *G*, not the penalty Δ. A college program's third-time-through problem is a **bullpen-depth** problem wearing a pitching-mechanics costume.

---

## 5. What separates "continuous" from "stepped" — a design, not a finding

**The identification problem.** Times through the order and pitch count are near-collinear: the third time through arrives at roughly pitch 70–85 in almost every start. **But not perfectly.** Efficiency varies: a pitcher who works quickly reaches the third time through at pitch 62; one who nibbles reaches it at pitch 95.

**The design.** Regress per-PA outcome on **pitch count** and **times-through-the-order indicator** simultaneously, exploiting that off-diagonal variation. If the TTO indicator carries signal after conditioning on pitch count, the effect is **familiarity**. If pitch count absorbs it, the effect is **fatigue**, and the lineup turn is a coincidence of timing.

**Status: I could not verify whether this has been done.** It is the obvious design, the snippets describe a Bayesian model doing something adjacent (discontinuity parameters at TTO boundaries, which is a *stepped-vs-smooth* test rather than a *fatigue-vs-familiarity* test), and **no page was opened.** Treat this as a design handed forward, not a gap claim — the corpus has been burned before by asserting an absence it had not searched properly (Known Correction #4).

**Why it matters to a development program and not just to a manager.** The two mechanisms have **different training answers**:

- **Familiarity** → the answer is *arsenal*: a fourth pitch, a held-back look, a shape the hitter has not seen. Bought in February.
- **Fatigue** → the answer is *capacity*: conditioning, pitch efficiency, the strength base. Bought in the fall.

**A program that guesses wrong spends a whole off-season on the wrong problem.** This is the single highest-value unresolved question in this file.

---

## 6. What IS measurable within an outing — and the asymmetry that follows

Outcomes are unmeasurable (§2). Inputs are not.

**Fastballs needed per bucket to detect a within-outing velocity drop** (two-sample, α = .05, 80% power):

| within-outing FB SD | 0.5 mph drop | 1.0 mph | 1.5 mph | 2.0 mph |
|---|---|---|---|---|
| 0.8 mph | 40 | **10** | 5 | 3 |
| **1.0 mph** (corpus working assumption) | 63 | **16** | 7 | 4 |
| 1.2 mph | 90 | **23** | 10 | 6 |

> ### THE ASYMMETRY, STATED PLAINLY
> **A 1.0 mph velocity decline is detectable inside a SINGLE OUTING (~16 fastballs at each end).**
> **A 10-wOBA-point outcome decline is not detectable in 790 SEASONS.**
> The ratio between those two is about **10,000 starts**. You must make the third-time decision on **inputs** — velocity, slot, shape, command drift — and never on **outcomes**.

This is the general form of **F-257** (the detection asymmetry: cheap input check, unaffordable outcome check) and **F-273**, and it is now the third independent domain in which the corpus has derived it. It should probably be promoted to a standing rule rather than restated a fourth time.

**Caveat, and it is real:** F-127 says velocity goes **LAST** in the fatigue hierarchy — command drift, then breaking-ball finish, then slot, *then* velocity. So velocity is the **most measurable** signal and the **latest-arriving** one. The cheap instrument watches the wrong end of the sequence. The earlier signals (command drift, slot) are exactly the ones the corpus cannot yet quantify a detection threshold for, because **F-173's within-outing release-speed-SD study still has not been run by anybody.**

---

## 7. Reading the field's fatigue-detection claims against this arithmetic

A currently-indexed article (`sportsnaut.com`, "Predicting Pitcher Fatigue: Why Velocity Drops Are Flawed", **snippet-only, page not opened**) reports that *"pulling a pitcher just because their velocity has dropped 1.5 mph triggers a false alarm 41% of the time,"* using Statcast 2023–2026 and requiring ≥15 pitches in an inning.

**The arithmetic objection, which needs no page.** With a within-inning fastball SD of 1.0 mph and 15 pitches per inning, the SE of an inning-to-inning mean difference is **0.365 mph**. A 1.5 mph observed drop is therefore **4.1 standard errors** — probability under pure measurement noise ≈ **2 × 10⁻⁵**. Across the plausible SD range (0.8–1.2 mph) it is **3.4 to 5.9 SD**.

> **A 41% false-alarm rate CANNOT be measurement noise. Noise produces that drop roughly once in fifty thousand innings.**

So if the 41% figure is real, it is measuring one of two things, and the article's framing fits neither:

1. **Strategic pacing** — the velocity genuinely fell and genuinely came back, because the pitcher was managing effort. That is a *real* and interesting finding, and it is an argument about **intent**, not about the instrument.
2. **A circular label.** "False alarm" requires a ground truth for *fatigue*. **There is no ground-truth fatigue label in Statcast.** If "fatigued" is defined by subsequent performance, the metric is being validated against the very outcome §2 shows is unmeasurable at any relevant sample size.

**Verdict: UNPROVEN, and the headline ("velocity drops are flawed") does not follow from the arithmetic.** The instrument is fine — 1.5 mph is a 4-sigma signal. What is unproven is the *interpretation* of the signal. **Do not repeat the 41%.**

---

## 8. The connection to the corpus's cheapest unanswered question

`pitch-mix-sequencing.md` §6 and F-276 name the **anticipation slope $D$** — how much a pitch's effectiveness decays per point of usage share — as *"currently the cheapest unanswered question in the corpus,"* unmeasured anywhere.

**The TTO decline is a within-game measurement of exactly that quantity**, with exposure counted in *looks* rather than *usage share*. If batters improve ~10 wOBA points (**≈0.87 runs per 100 PA**) per additional look at a pitcher, that is a direct empirical handle on the decay of a *pitcher*, and the same panel design that estimates it per-pitch estimates $D$.

**This does not close the gap** — a look at a *pitcher* is not a look at a *pitch*, and the aggregation is not obvious. But it means the TTO literature is the nearest existing measurement of the corpus's most-wanted missing parameter, and **the estimation design in `pitch-mix-sequencing.md` §6 should be re-read with the TTO papers in hand once egress returns.** That is now the top item in the verification queue.

---

## 9. Summary table

| Question | Answer | Basis |
|---|---|---|
| Is there a league-level TTOP? | Reportedly ~10 wOBA pts per cycle, **continuous not stepped** | **SNIPPET-ONLY** |
| Can I measure my own guy's? | **No. ~790 seasons.** Not at 5× the effect either (32 seasons) | Arithmetic |
| What does my scorebook show me? | **56% lineup-slot composition**, +.025 wOBA of pure artefact | Arithmetic |
| Should I pull him the third time through? | Only if the fresh arm is within **~20 wOBA points**. Usually he is not | Arithmetic + snippet input |
| What is the whole question worth? | **~1 run per college season**, and only against an equal fresh arm | Arithmetic + snippet input |
| What can I actually see in an outing? | A **1.0 mph** velocity drop, in ~16 fastballs per bucket | Arithmetic |
| Familiarity or fatigue? | **UNKNOWN, and the training answers are opposite** | Open |
