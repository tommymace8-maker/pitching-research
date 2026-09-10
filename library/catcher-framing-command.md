# The Catcher — framing as a contaminant of command measurement

**Created 2026-09-10.** Companion to `stuff-and-command.md` §5 (command) and `coaching-translation.md`.
Findings **F-305 → F-310**, **F-313**, **F-314**.

> **⚠️ RUN CONDITION. This file was written in the SEVENTH consecutive fully egress-blocked cycle
> (F-304). NO PAGE WAS OPENED. Everything in §1–§4 is closed-form geometry or power arithmetic and
> depends on no source. §5 is a field sweep and is SNIPPET-LEVEL THROUGHOUT — treat every magnitude
> in it as a lead, never a measurement.**

**Scope note.** This is a pitching corpus and the mission is performance development. The catcher
enters it for one reason: **the metric most programs use to evaluate a pitcher's command is a
called-strike rate, and a called-strike rate is not a measurement of the pitcher.** F-182 conceded
this in one clause — *"framing motion contaminates the frame"* — and moved on. This file asks how
large the contamination is. The answer turns out to be less interesting than the second answer:
**the metric fails on variance grounds before the catcher is even considered.**

---

## 1. The geometry of the framable band

A pitch is a strike if any part of the ball overlaps the zone. So in **ball-centre coordinates**
the target is wider than the plate:

```
half-width = 17.0/2 + 2.9/2 = 9.95 in        effective strike width = 19.90 in
```

Statcast's **Shadow Zone** is defined as one ball width inside the edge to one ball width outside —
a band **5.8 in** wide straddling the boundary in ball-centre coordinates.

| Rulebook zone height | Effective strike area | Shadow annulus | Shadow ÷ zone |
|---|---|---|---|
| 17.0 in | 396 in² | 462 in² | **1.17** |
| 19.5 in | 446 in² | 491 in² | **1.10** |
| 22.0 in | 496 in² | 520 in² | **1.05** |

**F-305: the shadow annulus is larger in area than the strike zone it borders, by 5–17%, at every
plausible zone height.** The borderline region is not a thin correction band at the margin of the
target. It is a region bigger than the target, inside which the call is a decision rather than a
fact, and inside which someone other than the pitcher has a vote.

> **⚠️ Area is not probability.** Pitch density is not uniform, so the *share of actual pitches*
> landing in the shadow is **not** 50%. That empirical share is unpublished (F-314) and is
> bracketed at **12–20% of all pitches** everywhere it is used below. Every conclusion in §3 is
> shown to survive the whole bracket.

---

## 2. Framing, converted into inches

Called-strike probability runs from near-1 at the inner edge of the shadow to near-0 at the outer
edge, across those 5.8 inches. Taking the transition as roughly linear:

| Assumed transition | Gradient |
|---|---|
| 0.10 → 0.90 across 5.8 in | 13.8 pp/inch |
| 0.15 → 0.85 across 5.8 in | 12.1 pp/inch |
| 0.05 → 0.95 across 5.8 in | 15.5 pp/inch |

> **F-306. The conversion is ~12–16 percentage points of shadow-strike rate per inch of location.
> Divide any framing gap in pp by ~14 to read it in inches.**

**The finding is stated as a conversion rate on purpose**, so that it does not depend on any
unverified framing magnitude. Applied *illustratively* to §5's unverified 18.7 pp best-to-worst gap:
**≈ 1.2–1.6 inches.**

**Set that against the pitcher's own error bar.** F-183: the best command in Major League Baseball
misses by **~7 inches**; the average major leaguer by **~11–13**.

> **The entire best-to-worst spread in major-league catcher framing is worth roughly one-fifth of a
> single average pitcher's miss.**

Framing is a **large number in runs** because it is applied to ~1,600 pitches a year. It is a
**tiny number in inches**. Both are true and they point opposite ways:

- **For the catcher**, an inch applied 1,600 times a season is a real job.
- **For the pitcher**, the whole framing industry is fighting over a fifth of his own error bar.
  **There is no version of this in which a pitcher's development plan contains a framing term.**

---

## 3. Why a called-strike rate cannot measure a college pitcher's command

### 3.1 The variance wall

Shadow pitches are near coin flips by construction — that is what makes them the shadow. Two-
proportion test, p ≈ 0.5, 80% power, α = .05 two-sided:

| Detect | Shadow takes per group | Total |
|---|---|---|
| 2 pp | 9,811 | 19,622 |
| 3 pp | 4,360 | 8,721 |
| **5 pp** | **1,570** | **3,140** |
| 7 pp | 801 | 1,602 |
| 10 pp | 392 | 785 |

And the supply. A college starter throws ~1,200–1,800 pitches a season:

| | 12% shadow-take | 15% | 20% |
|---|---|---|---|
| 1,200 pitches | 144 | 180 | 240 |
| 1,500 pitches | 180 | **225** | 300 |
| 1,800 pitches | 216 | 270 | 360 |

> **F-307. A college starter generates roughly 150–360 framable taken pitches a season. Detecting a
> 5-percentage-point command change requires ~3,140 of them — about fourteen seasons. Detecting
> 7 pp requires about seven.**

**Nothing rescues it.** The most generous cell (360/season) against the most forgiving effect
(7 pp) still needs 4.5 seasons. Push the shadow share to 25% and the pitch count to 2,000 and it is
still over three seasons, for an effect larger than the best framer in baseball is worth.

**And restriction of range makes it worse, not better.** Elite command populations cluster more
tightly, so the gaps you are trying to detect shrink while the shadow-take supply does not grow.
**The 85+ population is the hardest one in which to measure command by called strikes.**

### 3.2 The catcher-assignment artifact, underneath the noise

A measured called-strike rate is jointly produced by location, catcher, umpire, batter and count.
BP's CSAA handles this with a mixed model controlling all five (F-182) — **and that model is
identifiable in MLB because catcher assignment rotates.**

**A college staff has two catchers**, often with one catching 70–90% of innings and personal-catcher
pairings. The difference between two pitchers arising **from the catcher alone**:

```
artifact = (s_i - s_j) x delta_catcher
```

| Δ between your catchers | share diff 0.2 | 0.5 | 0.8 |
|---|---|---|---|
| 3 pp | 0.60 pp | 1.50 pp | 2.40 pp |
| **5 pp** | 1.00 pp | **2.50 pp** | 4.00 pp |
| 8 pp | 1.60 pp | 4.00 pp | **6.40 pp** |

**The comparison that matters** (F-182, BP 2016 CSAA leaders): Zach Davies **+3.5%**, Josh Tomlin
+2.8%, Kyle Hendricks +2.5%, Zack Greinke +2.1%. That is the top of Major League Baseball. **A
2.5 pp artifact on a college staff is ~70% of the best command season in MLB, manufactured entirely
by who was squatting.**

> **F-308. On a two-catcher college staff the catcher-assignment artifact is the same order of
> magnitude as the entire real signal — AND IT IS BIAS, NOT NOISE. It does not shrink with more
> innings.**

The run cost is trivial (0.28–1.50 runs a season at Statcast's stated 0.125 runs/strike) **and that
is the point. The damage is not runs. It is that the artifact corrupts the ranking you allocate
development time against.** You do not lose a run; you spend a winter on the wrong pitcher.

**This is the second member of the family F-287 opened** (the lineup-slot composition bias in
times-through-order splits). Both are systematic, both are larger than the effect they contaminate,
and both defeat the one instinct every coach has about a bad number — *wait for a bigger sample*.
**Here, waiting is the error: a staff that pools three seasons to fix the sample-size problem
increases the artifact while believing it has solved the problem.**

**The standard fix is unavailable.** Co-estimating catcher and pitcher effects requires variation in
the pairing. With two catchers and near-constant shares the terms are near-collinear; the model does
not fail loudly, it returns wide unstable pitcher estimates that look like numbers. Randomising
catcher assignment would identify it, and **no program should trade a season of battery chemistry
for a cleaner spreadsheet column.**

---

## 4. What to measure instead — the declared-target miss log

### 4.1 The detection case

| Route | Pitches needed |
|---|---|
| Miss distance, 2 in gain (SD 5 in) | **~196** |
| Miss distance, 1.5 in gain | ~349 |
| Miss distance, 1 in gain | ~785 |
| Shadow called-strike rate, 5 pp | **~20,930** |

> **F-310. The input route needs several-fold fewer pitches than the outcome route, and the outcome
> route needs more than a career.**

> **⚠️ SAY THE ORDERING, NOT THE RATIO.** The naive 107× compares a continuous t-test against a
> binomial and its exact value is an artefact of pairing 2 inches with 5 pp. Converting to one unit
> via F-306 (~14 pp/inch), 5 pp *is* ~0.36 in, which needs ~6,000 pitches by the input route —
> still ~3.5× fewer than ~21,000, because a binomial at p = 0.5 discards nearly all the information
> in a continuous location. **This is the standing rule generalised from Dispute #22.**

### 4.2 The protocol

**Cost: a notebook and a camera you already own.** F-182 is explicit that declared-target-before-
the-pitch is the **only** approach that *solves* rather than infers the intent problem — glove
tagging is deprecated precisely because the glove moves and framing motion contaminates the frame,
which is the same contamination §3.2 quantifies, arriving from the other direction.

1. Before each pitch in a charted bullpen the pitcher **declares the target out loud** — a 9-zone
   call plus in/out of zone. **Not the glove.** The glove may be there; it is not the record.
2. The catcher sets up and **holds** until release. A drifting or late glove voids the pitch for
   charting (not for throwing).
3. Log actual location from any tracking unit, or a fixed 240 fps camera behind the plate with a
   taped scale (F-204).
4. Record **signed miss in inches**, horizontal and vertical, then the scalar radial miss.
5. **Never record whether it was called a strike.** That is the corrupted variable.

**The check, with the sample size to detect it:** ~200 charted pitches pre and post detects a
2-inch improvement in mean radial miss at 80% power. At ~50 charted pitches a week, four weeks each
side. Want 1 inch? ~785 pitches — budget for it or do not claim it.

**Calibrate the athlete before showing him a number** (F-183's anchor): *"The best command in the
big leagues misses by about seven inches. Average misses by a foot. If you think you're hitting the
glove, you're not, and neither is anybody else."* A college arm logging 12–14 in is normal.

### 4.3 ⚠️ The load-bearing limitation

**F-197: no bullpen-to-game command transfer study exists in baseball.** This protocol measures a
**bullpen** quantity, and it is justified **because it is measurable, not because transfer is
established.** The biomechanist's objection was conceded in full (Dispute #20a, escalated
2026-09-10): a held static target is not a game target, so this buys internal validity by spending
ecological validity. **The protocol stands only because the alternative is not a better measurement
but no measurement.**

---

## 5. ABS, and what it does to all of this — ⚠️ SNIPPET-LEVEL THROUGHOUT

### 5.1 The timeline (structural fact — corroborated across four outlets, safe to plan around)

- The **SEC used the ABS challenge system for every game of the 2026 SEC Tournament** (May 19–24,
  Hoover), accelerating a timeline previously pegged to 2027. Three challenges per game; pitcher,
  catcher or batter at the plate may challenge.
- The **NCAA approved ABS as an experimental rule for all divisions in 2027**, team-optional subject
  to technology availability.

**Consequence: any framing-dependent investment now has a depreciation schedule.** Recruiting a
catcher for his receiving, or spending bullpen time on presentation, is buying an asset with a
known write-down date. **How steep is unknown** — the challenge system preserves framing on
*unchallenged* pitches, which is most of them, so the value decays rather than vanishing.

### 5.2 The challenge-success selection effect

> **F-309. Challenge success rate is mechanically anti-correlated with framing skill.**

Let *T* be borderline pitches that are truly strikes under the ABS zone. A **good** framer converts
a high fraction of *T*, leaving a **small** residual of challengeable-and-winnable calls; a **bad**
framer leaves a **large** one. Second term, same direction: the good framer's residual is adversely
selected — what he failed to convert is what the umpire was most confident about, so even his
residual overturns at a lower rate. **Both terms push the same way.**

**Therefore: do not evaluate, recruit or play a catcher on challenge success rate.** A catcher
leading the league in it is displaying a larger supply of umpire mistakes against him.

**The pitcher version is why this belongs here.** A pitcher with poor command generates more
genuinely-missed calls, so *his* success rate is inflated too. **Don't let your pitcher spend the
challenge:** he is the party furthest from the pitch, with the strongest motivated reasoning about
it, and the least information. The catcher has the best view.

**The general rule, which is the durable part: before reading any success rate, ask who chose the
denominator.**

### 5.3 What must not be repeated

| Figure | Status |
|---|---|
| Top-30 framers 0.704 → 0.565 runs/100 innings (~20% decline) | **UNVERIFIED — `calledthird.com`, unknown standing** |
| 18.7 pp best-to-worst framer gap | **UNVERIFIED — same** |
| SEC tournament "56.2% conversion rate" | **UNVERIFIED, and ambiguous as stated** |
| Challenge success: catchers 56–59%, batters 48–50%, pitchers 41% | **UNVERIFIED — and the two readings disagreed (F-312)** |
| Carson Kelly 21-4 / 24-28 | **UNVERIFIED, and withdrawn as evidence (F-312, §6.4)** |
| Bailey +25 runs / Quero −13 runs, 2025 | **UNVERIFIED — summary-level** |
| **Statcast conversion: 0.125 runs per strike** | **Documented methodology figure — the one framing input treated as safe** |

**One coherence check that costs nothing.** Using 0.125 runs/strike: +25 runs → +200 strikes;
−13 → −104; gap 304 strikes; 304 ÷ 0.187 ≈ **1,626 shadow chances per full-time catcher-season.**
Three independently-reported summary numbers cohere only near ~1,600. **That raises the odds they
are real. It does not make them verified**, and it is used only as the bracketed anchor for §3.1's
denominator.

**Blocklist candidates added (unknown standing, content-farm profile, unverifiable):**
`calledthird.com`, `mlbanalytic.com`, `pitching.dev`.

---

## 6. What this file does not know

- **The shadow-take share for a college pitcher** — bracketed 12–20%, unpublished (F-314).
- **The miss-distance SD for an 85+ arm** — bracketed 4–6 in from F-183's MLB anchor, unpublished
  (F-314). **A month of charted bullpens produces it.**
- **Any college catcher framing gap.** §3.2's Δ bracket (3–8 pp) is illustrative. No college framing
  data exists publicly at all.
- **Whether bullpen command transfers to games** (F-197). This is the single largest hole under §4.
- **The shape of the called-strike probability transition.** §2's gradient assumes rough linearity
  across the shadow band; the true curve is a logistic whose slope varies with count, handedness,
  umpire and pitch type.
- **Whether framing decays or collapses under a challenge system.** §5.1 argues decay from the
  structure of the rule; the only public magnitude is unverified.

---

## 7. The one-page version

1. **The borderline band is bigger than the strike zone** (F-305).
2. **Framing converts at ~14 pp per inch. The whole best-to-worst MLB framing spread is about a
   fifth of one average pitcher's miss** (F-306, F-183).
3. **Your college starter throws ~225 framable takes a year. Seeing a 5 pp command change needs
   ~3,140 of them — fourteen seasons** (F-307).
4. **Underneath that noise is a catcher artifact the size of the entire real signal, and it is bias:
   more innings makes the wrong ranking more confident** (F-308).
5. **So delete the called-strike column. Measure inches from a declared target instead — ~200
   pitches, not 21,000** (F-310) **— and say the ordering, not the ratio.**
6. **ABS is coming to college in 2027, SEC first. Don't let the pitcher spend the challenge, and
   don't buy framing on a long horizon** (F-309, F-313).
