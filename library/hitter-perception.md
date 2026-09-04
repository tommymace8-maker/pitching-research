# Hitter Perception and the Deception Budget
### Elite population (85 mph floor) · Performance development, not injury prevention

**Compiled:** 2026-09-04
**Author role:** biomechanist (arithmetic) / pitch-design specialist (implications)
**Status:** living document — **opened in a degraded cycle, see the verification statement**
**Companion files:** `library/stuff-and-command.md` (§2 pitch physics, §4 arsenal construction), `library/biomechanics.md`, `library/open-disputes.md` (Dispute 17)

---

## ⚠️ VERIFICATION STATEMENT — READ FIRST. THIS FILE IS NOT LIKE THE OTHERS.

Every other library file in this corpus opens by stating that its citations were checked against primary sources. **This one cannot.**

The 2026-09-04 cycle ran with **all outbound HTTPS denied at the egress gateway (403 CONNECT on every host attempted, including all eight domains the standing brief lists as working, and including generic controls).** Search worked; fetching did not. **No primary source was opened.**

Therefore this file is split hard in two, and the split is the point:

- **§1–§4 are ARITHMETIC.** They depend on no source. They are closed-form integrations of a standard drag model plus standard power calculations, computed in-cycle and reproducible. **These are the durable content.**
- **§5 is a QUARANTINED QUEUE.** Every literature item is snippet-only, labelled `UNVERIFIED`, and **must not be promoted, quoted to an athlete, or compressed into a recommendation until someone reads the paper.**

Do not merge the two halves. The corpus's founding lesson (F-240) is that six corrections landed in one day, none a fabrication, all in the direction of more confidence than the source supported — because the corruption happens in the compression from paper → table row → recommendation. **A blocked cycle is that compression with the paper removed.**

---

## 1. Why this file exists

`INDEX.md` §5 listed **"Hitter perception and reaction"** as a topic the corpus had never researched, "referenced obliquely (attack angle, deception, the 150 ms tunnel-point argument) but never studied directly."

That gap sat directly underneath three findings the corpus held and could not reconcile:

| Finding | What it says |
|---|---|
| **F-163** | Tunneling is over-sold. Bryant (2024, 100 pitchers) found `r = 0.07` between tunnel score and run value — "almost no relationship at all." Retired as a training target. |
| **F-164** | But release-angle (HRA) overlap **is** a real, static, trainable deception property. |
| **F-159 / F-232** | The changeup's argued causal chain is **velocity GAP → hitters out front → whiffs**, called strong. What has *no* relationship is **absolute** changeup velocity. |

Deception through the tunnel is worth nothing; deception through velocity separation is worth a lot; deception through release-angle overlap is worth something. **Nobody had asked why.** The answer turns out not to need a single citation — it needs a clock.

---

## 2. The clock

### 2.1 The model, stated so it can be attacked

One-dimensional flight along the release-to-plate line. `m = 0.145 kg`, `r = 0.0366 m`, `A = πr² = 4.208e-3 m²`, `Cd = 0.33`, `ρ = 1.196 kg/m³` (sea level, 20 °C). Quadratic drag gives `k = ρ·Cd·A/(2m) = 0.005727 m⁻¹` and the closed forms:

```
v(x) = v₀·exp(−kx)          plate speed
t(L) = (exp(kL) − 1)/(k·v₀)  flight time over travel L
x(t) = ln(1 + k·v₀·t)/k      distance covered by time t
```

Gravity and Magnus are omitted from the **timing** term — they act transverse to flight and change path length by well under 1%. Travel distance is `60.5 ft − extension`.

### 2.2 Flight time and plate speed

| Extension | Travel | 90 mph | 95 mph | 100 mph |
|---|---|---|---|---|
| 6.0 ft | 54.5 ft | 433.2 ms | 410.4 ms | 389.8 ms |
| **6.5 ft** (MLB 4-seam mean, F-153) | 54.0 ft | 429.0 ms | **406.4 ms** | 386.1 ms |
| 7.0 ft | 53.5 ft | 424.8 ms | 402.5 ms | 382.3 ms |
| 7.5 ft | 53.0 ft | 420.7 ms | 398.5 ms | 378.6 ms |

**Plate speed is 91.0% of release speed** throughout (range 90.9–91.2%).

**Sensitivity:** across `Cd = 0.30–0.36` and `ρ = 1.06–1.196` (sea level 20 °C through roughly 3,000 ft or a hot day), the 95 mph / 54.0 ft figure spans **402.7–408.2 ms**. Robust to ±3 ms.

> **The naive no-drag figure is 387.6 ms. Drag adds 18.8 ms — about 5%, and it is 5% of the hitter's entire budget.** Anyone computing flight time as distance ÷ release speed is running ~19 ms fast.
>
> **This REFINES F-250, it does not correct it.** F-250 flagged the drag issue for the per-foot extension delta and gave ~7.5 ms (conservative 7.2). This cycle's integration gives **7.88 ms per foot** at 95 mph. The difference is entirely the assumed `Cd`, and both are the same number to the precision either can support. No correction notice is warranted.

### 2.3 The commit instant

Take the swing itself as ~150 ms from initiation to contact. **This input is snippet-only and unverified** — it is the one load-bearing external number in this file, and §5 queue item 2 exists to replace it with a measurement.

| Swing duration | Commit at | Ball has travelled | **Still to go** |
|---|---|---|---|
| 130 ms | 276 ms after release | 37.3 ft | **16.7 ft** |
| **150 ms** | **256 ms after release** | **34.7 ft** | **19.3 ft** |
| 175 ms | 231 ms after release | 31.4 ft | **22.6 ft** |

And the front of the flight, which is where the anticipation literature says the expert advantage lives:

| Time after release | Ball has gone | Remaining to plate |
|---|---|---|
| 100 ms | **13.8 ft** | 306 ms |
| 150 ms | 20.5 ft | 256 ms |
| 200 ms | 27.2 ft | 206 ms |
| 250 ms | 33.8 ft | 156 ms |

**In the first tenth of a second the ball covers under fourteen feet.** Whatever a hitter extracts early, he extracts from a ball that has barely left the pitcher's hand — which is the geometric reason release-instant properties (F-164, HRA overlap) can matter at all.

> **The sentence to say out loud, because it is true across the whole 130–175 ms band and requires defending no unverified number:** *"He has decided about a quarter-second after the ball leaves my hand, with it still fifteen to twenty-five feet away from him."*

---

## 3. The central result — two deception channels with different exponents

### 3.1 The velocity channel is linear; the movement channel is quadratic

A **velocity difference** produces a positional discrepancy that grows essentially **linearly** in `t`. A **movement difference** is, to first order, a constant transverse acceleration, so its separation grows as **`t²`**.

The decision falls at `t/T = 256.4/406.4 = 0.631`. Therefore **`(t/T)² = 39.8%`** of the eventual plate-level movement separation has appeared by the time the hitter commits — while the velocity channel has delivered essentially all of its own.

**Movement channel at the commit instant:**

| Total plate separation | Visible at commit |
|---|---|
| 6 in | 2.4 in |
| 12 in | 4.8 in |
| 18 in | 7.2 in |
| 24 in | 9.6 in |

**Velocity channel at the commit instant** — positional gap between two pitches released identically at different speeds:

| Pair | Gap at commit |
|---|---|
| 95 vs 92 mph | 12.8 in |
| 95 vs 88 mph | 29.8 in |
| 95 vs 85 mph | 42.6 in |
| 95 vs 80 mph | 64.0 in |

**Sensitivity, and it runs the safe way:** over swing durations of 130–175 ms the movement fraction spans **46% down to 32%**. A *longer* swing means an *earlier* commit and makes the movement channel **worse**. Every conclusion here holds a fortiori at the unfavourable end of the band.

### 3.2 What is claimed, and what was withdrawn

> **⚠️ A draft of this section said velocity beats movement "by a factor of six." THAT RATIO IS WITHDRAWN.** It compares feet of positional discrepancy, and the visual system reads optical expansion and time-to-contact, not absolute position. The anatomist raised this in-cycle and the biomechanist conceded it. See **Dispute 17**.

**What survives translation into any units is the exponent.** Velocity separation is linear in `t`; movement separation is quadratic in `t`; the decision falls at `t/T ≈ 0.63`. **The movement channel is back-loaded past the decision and the velocity channel is not.** That ordering is a property of the exponents, not of the units.

### 3.3 What this buys the corpus

**It reconciles F-163 with F-159/F-232, and it does so without needing the tunnel window to be imaginary.**

- The tunnel window is real geometry. BP's revised 150 ms point lands at **19.3 ft from the plate**, which §2.3 reproduces independently.
- But **tunnel metrics score the movement channel, at the point in flight where that channel has delivered least** — under 40% of its eventual separation.
- A metric aimed at the weaker channel, measured at the moment that channel is weakest, correlating at `r = 0.07` with run value, is **exactly what the geometry predicts.**

**F-163's coaching line therefore stands unchanged — *train release consistency, do not build sequences around tunnels* — and now has a mechanism attached rather than just a null.** That is an upgrade to a finding, not a reversal of one.

**It also reconciles F-163 with F-164.** They are not in conflict: **HRA overlap is a release-instant property, available in the first milliseconds when the ball has moved a few feet; tunnel metrics are a mid-flight property in the back-loaded channel.** Same window, different channels, and the early one is the one that matters.

### 3.4 A computed inconsistency in the tunneling literature

F-163 records both BP tunnel-point definitions: **"23.8 ft from the plate (~175 ms)"**, later **"revised to 150 ms."** Through the clock at 95 mph:

| Point | Distance from plate | Time remaining |
|---|---|---|
| BP original | 23.8 ft | **183.9 ms** (BP glossed "~175 ms" — close; the gap is `Cd` and assumed velocity, not material) |
| BP revised | **19.3 ft** | 150 ms |

**The revision moved the tunnel point 4.5 feet closer to the plate, and the 23.8 ft figure kept circulating alongside the 150 ms justification.** Anyone drawing a "24-foot tunnel window" while citing the angular-eye-velocity argument for 150 ms is drawing the window in the wrong place.

Small in outcome terms — §3.1 says the whole channel is the weak one. Registered because **it needed no source at all**: it was caught by arithmetic on numbers the corpus already held.

---

## 4. What a coach does with this

### 4.1 The recommendation, priced at what the evidence can pay for

**Measure the fastball–changeup velocity gap and its stability — mean and SD — and treat the SD as the target, not the mean.**

- **What the pitcher hears:** *"Your changeup's job is the gap, not the movement. He commits with the ball still twenty feet away — by then he has seen almost none of your movement, and he has seen all of your speed."*
- **The drill:** FB/CH pairs off the mound, reading **only** the velocity delta off Trackman/Rapsodo. Do not show movement plots during this block; they are the distractor. A/B two changeup grips against the same fastball.
- **The failure on video:** the gap arriving from a **slowed arm** rather than the grip. At 240 fps, compare apparent arm speed and the foot-contact→release interval between fastball and changeup. If the changeup's interval is longer, he bought the gap with a tell. **See §4.3 — this check is legitimate; the claim behind it is not established.**

### 4.2 The detection asymmetry — state it before the block starts

α = 0.05, 80% power:

| Question | Change to detect | Sample needed |
|---|---|---|
| Did the mean gap move? | 1.0 mph (within-pitcher SD 0.8/1.0/1.2) | **10 / 16 / 23 pitches of each type** |
| Did the mean gap move? | 0.5 mph | 40 / 63 / 90 of each type |
| Did the mean gap move? | 1.5 mph | 4 / 7 / 10 of each type |
| **Did whiff rate improve?** | 30% → 33% | **3,760 swings per arm per batter-side** |
| Did whiff rate improve? | 30% → 35% | **1,374 swings** |
| Did whiff rate improve? | 30% → 40% | 353 swings |

> **Two bullpens settle whether the input moved. Nothing a college program can collect settles whether it bought whiffs on one arm.** Say that to the pitcher in advance. It pre-empts both failure modes that follow every training block: reading a good weekend as proof, and reading a bad one as refutation.

**This generalises.** It is the same shape as the ~200 tracked pitches needed to detect a 2-inch command gain (F-186, F-243): **release-side mechanical quantities are cheap because their within-pitcher SD is small; plate-side outcome rates are expensive because binomial noise at 40 innings swamps any realistic effect.** Coach the input on the mechanism; never promise the outcome and then go looking for it in a sample that cannot contain it.

### 4.3 Marker, lever, or neither — the honest classification

Three separate claims with three different evidence grades. **They are routinely stated as one sentence, and that sentence is where corpora go wrong.**

1. **The geometry (§3.1) is `MECHANISM`.** Arithmetic. It cannot collapse the way stride length collapsed.
2. **The link from that discrepancy to whiffs is `CROSS_SECTIONAL`.** F-159/F-232 record the velocity-gap→whiff chain as the source's *argued* chain. **Nobody has assigned pitchers to a bigger gap and measured outcomes.**
3. **Manipulability — the thing that killed stride length — is the one part that is unambiguously fine here.** Stride length collapsed because two independent groups moved it and got nothing or worse (F-043/F-044/F-045), and because a pitcher cannot decide mid-delivery to stride 8% further. A pitcher **can** decide which pitch to throw, and can change a grip in a bullpen and watch the velocity move that afternoon.

**So: mechanism established, outcome link not established, manipulability fine.** That is a genuinely different evidentiary shape from stride length — and it still does not license writing *"science says throw a bigger changeup gap."*

**And the constraint the anatomist attaches:** the gap must come from the **ball**, not the **arm**. A changeup thrown with a decelerated arm is a different motor pattern and removes the release-kinematics congruence that makes the gap deceptive at all. **The pitcher is not trying to throw slower; he is trying to throw a slower ball at the same effort.** That is a grip-and-pressure problem, not an intent problem. **This is `FOLKLORE` with a plausible mechanism (F-256) — universally repeated, never measured. Keep it in the drill as *what to look at*; drop it from the claims.**

---

## 5. ⚠️ QUARANTINED VERIFICATION QUEUE — snippet-only, nothing here is usable

**Not one of these was opened. All are `EVIDENCE: UNVERIFIED`. Do not quote, do not compress, do not promote.** Priority order for the next cycle with working egress.

| # | Source | Snippet claim | Why it is the priority it is |
|---|---|---|---|
| **1** | **Higuchi, Nagami et al. (2016), PLOS ONE 11(2):e0148498, PMID 26848742, PMC4743964** — "Contribution of Visual Information about Ball Trajectory to Baseball Hitting Accuracy" | n = 10 college position players. Conditions: no occlusion; occluded from 150 ms **after release**; occluded from 150 ms **before arrival**. Reportedly **no effect on mean ball-bat contact location in bat long axis, short axis, or pitcher-catcher direction**; extra visible time reduced standardised variability **only in the bat's short axis**. | **The single most important item in this queue.** If it survives, it says **late flight information is used for vertical adjustment, not for timing** — §3.1's conclusion arriving from a real experiment by a wholly independent method. If it does not, §3 stands on arithmetic alone: still enough for the coaching line, not enough for the mechanism claim. **Caveat regardless: n = 10 college position players is small, and they are hitters, not an 85+ pitching sample.** (F-255) |
| **2** | Frontiers in Psychology 2025, `10.3389/fpsyg.2025.1514301`, PMC11822940 — VR decomposition of batting into timed visuomotor sub-processes | Temporal structure of the batting decision | **Would replace §2.3's unverified ~150 ms swing-duration input with a measurement.** That input is load-bearing for every timing number in §3. |
| **3** | Brill R & Wyner A (2022), JQAS, `10.1515/jqas-2022-0116`, arXiv:2210.06724 | After adjusting for batter/pitcher quality, handedness and home field, **little evidence of strong discontinuity between times through the order** | Every third-time-through decision a college staff makes is priced off a penalty this reportedly weakens. **Same Brill whose xCTRL work this corpus has already verified clean (INDEX §4) — a reason to read it first, not a reason to believe it unread.** (F-258) |
| **4** | Prasad A, MIT Sloan Sports Analytics — "Decoding MLB Pitch Sequencing Strategies via Directed Graph Embeddings" | ~3.6 M pitches, 2015–2019; claims pitchers build sequences from "setup" and "knockout" components | Would be the first large-N structural evidence that sequencing is even non-random |
| **5** | arXiv 2606.17345 (2026) — counterfactual sequence optimisation, Transformer on Statcast | Claims **>1.0 K/9** from optimising final and setup pitches | **Extraordinary magnitude from unvalidated counterfactuals. Read adversarially. Do not import the K/9 figure.** |
| **6** | Creally M, Medium — pitch-level swing shape data | "Attack angle above expected" identifies soft-throwing pitchers who still get hitters late (Trevor Williams, Heaney, Tim Hill, Lively) | **The most promising genuinely new idea of the sweep** — a public, pitcher-level, outcome-anchored deception metric, a direct successor to what F-163 retired. Medium is a blocklisted domain; extra care. |
| **7** | *J Motor Learning and Development* 6(2):197 (2018) — "Use of Pitcher Game Footage to Measure Visual Anticipation and Its Relationship to Baseball Batting Statistics" | Professional batters, video occlusion at release, +80 ms, +200 ms | Would give occlusion timings **in professionals**, and would test the pre-release-kinematics premise that §4.3's arm-speed constraint rests on |

### Effective Velocity (Perry Husband) — recorded here so the verdict is findable
Search returns a consistent statement that **no thorough third-party public validation of EV theory exists**, despite MLB Network / FanGraphs / SBNation coverage. Coherent with F-249, where Driveline's 2019 Aucoin test found perceived velocity beat release speed on swinging strikes but lost on xwOBACON and projected RA9 — **with no sample size and no coefficients published.** A widely circulated *"~50% of home runs come from back-to-back pitches within 6 EV mph"* figure surfaced with no retrievable methodology. **Verdict: UNPROVEN. Do not quote the 50% figure.**

### Absences noted (searched, not found — and the search itself ran degraded)
- Any occlusion or VR study manipulating **release extension** at fixed velocity. Still absent, as F-250 recorded.
- Any study of **within-pitcher velocity-gap SD** (the SD of the FB−CH delta) against outcomes. **This looks like a genuine hole and a cheap one to fill** — computable from Statcast in an afternoon, and directly coachable. Companion to F-173, the corpus's other cheapest-unrun-study.
- Any bullpen-to-game transfer study for sequencing decisions.
- Any test of whether a pitcher can deliberately change his velocity gap **without** an arm-speed tell (F-256).

---

## 6. Hazard log for this file

**The search-summary conflation class fired again this cycle, and would have imported a 3× error.** A summary asserted *"The major league average attack angle is 32°, ranging from about 20° to near 50°"* — **32° is league-mean swing path TILT; mean attack angle is roughly 10°.** The same summary then stated two sentences later that "the most productive contact typically happens at attack angles between 5° and 20°," **contradicting its own figure inside one paragraph.** Nothing from it was imported. This is the hazard already logged as `idea-scouting.md` Sweep 2 #13, and it required no AI content farm — only a search engine compressing two adjacent metrics.

**Standing rule this file adds:** when a summary states a number and a range that are mutually inconsistent within the same paragraph, **the paragraph is the evidence of the error** — no source access is needed to reject it.
