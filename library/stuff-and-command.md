# Stuff and Command — Pitch Design and Command Development
### Elite population (85 mph floor) · Performance development, not injury prevention

**Compiled:** 2026-08-13
**Author role:** pitch-design specialist / motor-learning researcher
**Status:** living document
**Companion files:** `library/biomechanics.md`, `library/coaching-translation.md`, `library/idea-scouting.md`

---

## ⚠️ VERIFICATION STATEMENT — READ FIRST

Every citation in this document was checked against a primary source: PubMed, Crossref, a journal site, or the author's/institution's own page. Several distributional tables were **computed directly from Baseball Savant CSV endpoints** rather than repeated from secondary blogs, and are marked as such.

**Three things were explicitly rejected during research and are named here so nobody re-imports them:**

1. **Content-farm domains** returning confident, specific-sounding, untraceable numbers on pitching topics: `accio.com`, `mlbanalytic.com`, `sportsorca.com`, `mkdcbaseball.com`, `seemagnus.com`, `sportstrace.com`, `talksox.com`, `baseballscouter.com`. **The tell is unearned precision.** Standing hazard from `idea-scouting.md` §12.
2. **Any "2026 ASMI consensus statement."** No such document exists.
3. **Specific numeric claims that could not be traced** — e.g. "sweeper usage 8.4% in 2026" — are excluded rather than hedged.

**Items that remain flagged UNVERIFIED are labeled inline.** Where a literature is genuinely thin, I say so rather than padding it.

---

## Table of Contents

1. [Framing: what stuff and command are actually worth](#1-framing-what-stuff-and-command-are-actually-worth)

**TOPIC A — STUFF / PITCH DESIGN**

2. [The Physics of Pitch Flight](#2-the-physics-of-pitch-flight)
   - 2.1 [Spin: total, transverse, gyro](#21-spin-total-transverse-gyro) · 2.2 [Magnus force — and the diminishing-returns myth](#22-magnus-force--and-the-diminishing-returns-myth) · 2.3 [Seam-shifted wake](#23-seam-shifted-wake--the-honest-state-of-the-evidence) · 2.4 [Extension and perceived velocity](#24-extension-release-height-and-perceived-velocity) · 2.5 [Vertical approach angle](#25-vertical-approach-angle--the-cleanest-result-in-this-document)
3. [Designing Each Pitch](#3-designing-each-pitch)
4. [Arsenal Construction, Tunneling, and Stuff Models](#4-arsenal-construction-tunneling-and-stuff-models)

**TOPIC B — COMMAND**

5. [Command Is an Angular Problem](#5-command-is-an-angular-problem)
6. [Release-Point Variability: the numbers, and a debunking](#6-release-point-variability-the-numbers-and-a-debunking)
7. [The Mechanical Signature of Plus Command](#7-the-mechanical-signature-of-plus-command)
8. [Repeatability, Adjustability, and the Uncontrolled Manifold](#8-repeatability-adjustability-and-the-uncontrolled-manifold)
9. [Measuring Command](#9-measuring-command)
10. [Motor Learning and Skill Acquisition — the reckoning](#10-motor-learning-and-skill-acquisition--the-reckoning)
11. [Training Command Deliberately](#11-training-command-deliberately)

**Back matter**

12. [What Is Marketing](#12-what-is-marketing)
13. [Corrections Owed to the Library, and Open Questions](#13-corrections-owed-to-the-library-and-open-questions)
14. [References](#14-references)

---

## 1. Framing: what stuff and command are actually worth

**Finding 1 — On any single pitch, location outweighs shape. Across a season, shape is the more reliable asset.** FanGraphs' own summary: *"On any given pitch, the location is hugely important, more than the stuff. However, stuff is stickier season to season and start to start, so it's a safer bet."* ([FanGraphs Library](https://library.fangraphs.com/pitching/stuff-location-and-pitching-primer/)) **[ESTABLISHED]**

**Finding 2 — The measured price of command.** Ludwig, Brill & Wyner (2025): **improving fastball miss distance by one inch ≈ 0.3 FIP**, which they characterize as *"comparable in magnitude to the effect of a one-standard-deviation increase in Stuff+."* Elite fastball control ≈ **+36 IP/season.** ([arXiv:2508.19184](https://arxiv.org/abs/2508.19184)) **[EMERGING — preprint, 118 pitcher-seasons]**

A starter's Stuff+ standard deviation is 12.16 points. **Getting a pitcher from an 11-inch average miss to a 9-inch miss is worth roughly what adding 24 points of Stuff+ is worth** — which is far more than most pitch-design projects deliver.

**Finding 3 — Location+ correlates with walk rate at −0.54; Stuff+ at only −0.15. Yet Stuff+ carries roughly three times Location+'s weight in explaining xERA.** (Jack Martin, RotoGraphs, 25 Jun 2026.) **[ESTABLISHED]** The canonical case is **Eury Pérez: Stuff+ 117.8 / Location+ 93.4, 47.7% hard-hit on the fastball, xERA 4.91.** Elite shape, ordinary results.

**Finding 4 — the measurement asymmetry that explains why the industry chases stuff anyway.** Stuff+ becomes reliable at **~80 pitches**; Location+ at **~400**. Observed starter SDs: **Stuff+ 12.16, Location+ 3.34.** **[ESTABLISHED]**

> **The industry's preference for stuff is substantially an artifact of measurement convenience, not a considered judgment about value.** You can prove a pitch-design win in ten pitches. You cannot prove a command win in ten bullpens (§11.4). That asymmetry — not the underlying value — is why one industry exists and the other doesn't.

---

# TOPIC A — STUFF / PITCH DESIGN

## 2. The Physics of Pitch Flight

### 2.1 Spin: total, transverse, gyro

A spinning baseball's spin vector decomposes relative to its direction of travel:

- **Transverse (active/useful) spin** — perpendicular to the velocity vector. The only component producing Magnus force.
- **Gyro spin** — parallel to the velocity vector, like a rifle bullet. Produces **zero** Magnus force.

Verbatim from Alan Nathan: *"components of spin perpendicular to the direction of motion result in movement, whereas the component parallel to the direction of motion does not."* **Spin efficiency** = transverse ÷ total = sin(θ), where θ is the angle between spin axis and velocity vector. **Gyro degree** is the complement. **[ESTABLISHED]**

#### MLB four-seam distributions — computed directly from Statcast

*Source: Baseball Savant pitch-level CSV, all four-seam fastballs 2024-06-01 → 2024-06-05, **n = 6,113 pitches.** Five days is good for central tendency, weak for individual tails.*

| Metric | Mean | SD | p5 | p25 | Median | p75 | p95 | p99 |
|---|---|---|---|---|---|---|---|---|
| Velocity (mph) | 94.5 | 2.4 | 90.6 | 93.0 | 94.6 | 96.0 | 98.2 | 100.1 |
| Spin rate (rpm) | 2,313 | 174 | 2,030 | 2,206 | 2,317 | 2,432 | 2,584 | 2,668 |
| **Bauer Units** (rpm/mph) | **24.5** | 1.8 | 21.7 | 23.4 | 24.5 | 25.7 | 27.2 | 28.1 |
| Extension (ft) | 6.51 | 0.45 | 5.80 | 6.20 | 6.50 | 6.80 | 7.30 | 7.60 |
| Release height (ft) | 5.87 | 0.48 | 5.10 | 5.61 | 5.90 | 6.16 | 6.55 | 6.94 |
| IVB (in) | 15.7 | 2.9 | 10.2 | 14.0 | 16.1 | 17.6 | 19.8 | 21.2 |

**[ESTABLISHED — own computation.]** Two things worth flagging:

- **"24 Bauer Units is average" is empirically correct** (measured mean 24.48). Bauer Units = spin ÷ velocity, a Driveline coinage.
- **The spin distribution is much tighter than commonly implied.** SD is only 174 rpm. **2,600 rpm is roughly the 95th percentile, not exotic.** Restricting to 95+ mph pitches (n = 2,657) barely moves spin (mean 2,350) — **velocity and spin rate are nearly independent at the elite level**, which is exactly why Bauer Units exist.

#### Spin efficiency / active spin by pitch type

*Source: Statcast Active Spin leaderboard, 2024, **n = 708 pitchers.***

| Pitch | Mean | p10 | Median | p90 | Max |
|---|---|---|---|---|---|
| Four-seam | 89.4% | 77.0 | 91.5 | 98.2 | 99.6 |
| Sinker | 85.9% | 73.0 | 87.1 | 96.8 | 99.6 |
| Changeup | 90.2% | 77.3 | 93.2 | 98.9 | 99.7 |
| Splitter | 83.0% | 65.5 | 85.1 | 96.6 | 99.1 |
| Curveball | 70.8% | 49.3 | 73.5 | 88.8 | 99.6 |
| Sweeper | 50.4% | 36.4 | 50.9 | 64.5 | 81.4 |
| Cutter | 46.5% | 28.0 | 47.3 | 64.2 | 79.8 |
| Slider | **32.3%** | 17.5 | **30.9** | 46.9 | 83.0 |

**[ESTABLISHED]** Elite four-seam efficiency benchmark: **95%+ ≈ p75; 98%+ ≈ p90.** The four-seam distribution is left-skewed and compressed near the ceiling — **there is far less headroom in four-seam efficiency than the market implies.** Sliders are the opposite: **median 31% efficiency means the typical MLB slider is predominantly gyro.**

#### The two axis conventions, and the trap

- **Clock-face tilt** (hh:mm from the catcher's view). Pure backspin = 12:00; a RHP sinker typically reads ~1:30–2:00.
- **True 3D spin axis** — measured directly at release (Hawk-Eye), not inferred from trajectory. Nathan's reconciliation method: *"Determining the 3D Spin Axis from Statcast Data"* (2020).

**The trap: tilt is a 2D projection and says nothing about the gyro component.** Two pitches with identical 1:30 tilt and identical spin rate can move completely differently if one is 90% efficient and the other 55%. **Tilt without efficiency is close to uninformative.** **[ESTABLISHED]**

**Related caution on the term "active spin":** Statcast's *observed* axis from Hawk-Eye and its *inferred* axis from movement are different quantities, and their divergence is the seam-shifted-wake signal (§2.3). Active spin derived from movement inference therefore **conflates efficiency loss with seam effects.**

### 2.2 Magnus force — and the diminishing-returns myth

From **Nathan (2008), *American Journal of Physics* 76(2):119–124, DOI 10.1119/1.2805242** (verified):

- `F_D = ½ C_D ρ A v²` and `F_M = ½ C_L ρ A v²`, with ρ = 1.23 kg/m³
- C_L is mainly a function of the **spin factor S ≡ Rω/v**, and may also depend on Reynolds number
- In SI units: **Re = 2180v**, **S = 8.53ω/v**
- Experimental range covered: S = 0.090–0.595
- Verbatim: *"The lift coefficient C_L is found not to depend strongly on v at fixed values of S."*

**Lyu, Smith, Elliott & Kensrud (2022), *Proc. IMechE Part P* 239:235–241, DOI 10.1177/17543371221113914** (verified via Crossref). 416 tests, six new Rawlings ROMLB balls, pitching machine + high-speed camera:
- *"At low spin the lift of the four-seam spin axis was nearly constant and **three times larger** than the two-seam spin axis"* — due to *"a **periodic reverse Magnus effect** observed at low spin rates."*
- **C_L for the two orientations converged at S = 0.15.**

**Where MLB fastballs actually sit:** at 94.5 mph and 2,313 rpm, **S ≈ 0.21.** Elite (2,600 rpm, 95 mph): **S ≈ 0.235.**

### ⚠️ "Spin has diminishing returns because of the lift curve" is FOLKLORE

The C_L(S) curve rises steeply below S ≈ 0.10–0.15, then increases **approximately linearly** above it (Nathan 2008; transition confirmed at S = 0.15 by Lyu 2022). **Every MLB fastball lives in the linear regime.** The aerodynamic marginal return to spin is roughly constant across the elite band. **Coaches quoting the low-S part of a curve no pitcher operates in are misapplying the physics.** **[FOLKLORE — and this corrects a claim I would otherwise have repeated.]**

**The real diminishing returns are two different things, and both are ESTABLISHED:**

1. **Added raw spin usually arrives with no added efficiency.** Regressing IVB on spin and velocity across all 6,113 pitches:
   `IVB = 3.86 + 0.00315·spin + 0.048·velo` → **+0.32 in of IVB per +100 rpm, R² = 0.041.**
   Raw spin explains **~4%** of cross-sectional IVB variance. The theoretical Magnus value for a 100%-efficient pitch is roughly **+0.5 to +0.6 in per 100 rpm**. **The gap between 0.57 theoretical and 0.32 observed IS the efficiency problem.** Chasing rpm without chasing axis is where the returns actually vanish.
2. The IVB → whiff relationship saturates behaviorally. **That is a hitter-response fact, not a fluid-dynamics fact.** Do not conflate them.

**Coaching bottom line:** spin rate is largely a fixed athlete trait. **Efficiency and axis are the trainable variables**, and they are where the missing movement is. **[EMERGING for trainability — I am not aware of a good controlled intervention trial on spin-efficiency training, and that absence should bother people more than it does.]**

### 2.3 Seam-shifted wake — the honest state of the evidence

**Who actually did the work — VERIFIED.**

**Dr. Barton L. Smith, Professor of Mechanical and Aerospace Engineering, Utah State University** (confirmed on USU's own faculty directory). He is a genuine particle-image-velocimetry specialist — he authored the PIV chapter in the *Handbook of Fluid Dynamics* (2016) with an extensive PIV uncertainty-quantification record. **This is not a baseball person dabbling in fluids; it is a fluids person who turned to baseball.** That matters for how much weight the work carries.

The term was **coined in 2019 by Andrew W. Smith**, an MS student, not by Barton Smith.

**Peer-reviewed anchor:** **A. W. Smith & B. L. Smith (2021), "Using baseball seams to alter a pitch direction: The seam shifted wake," *Proc. IMechE Part P* 235(1):21–28, DOI 10.1177/1754337120961609** — title, authors, journal, volume, pages and date all confirmed via the Crossref API. Underlying thesis: A. W. Smith (2020), *Pitched Baseballs and the Seam Shifted Wake*, USU, digitalcommons.usu.edu/etd/7903.

The public-analytics anchor is **Barton Smith, Alan Nathan & Harry Pavlidis, "Not Just About Magnus Anymore," Baseball Prospectus, 5 November 2020** — described on Nathan's own index as *"the first use of Hawkeye data to find evidence for pitch movement beyond that expected due to the Magnus force."* Nathan followed with *"What Is The Hawkeye Spin Data Teaching Us?"* **I** (Jan 2021), **II** (Mar 2021), **III: Searching For The Seam-Shifted Wake** (Mar 2023).

**The mechanism [ESTABLISHED].** Seams at specific positions relative to the flow force the boundary layer to separate earlier than it otherwise would. When this happens asymmetrically, the wake is deflected and a net force results — **in a direction independent of the Magnus force.** Demonstrated with **PIV**, i.e. direct velocity-field measurement of the separation location. This is a real measurement, not a flow visualization.

**Magnitude in controlled tests [ESTABLISHED].** From Smith's SSW Timeline Part 3 (2 Nov 2023): Andrew Smith's February 2020 "Looper" test compared two zero-gyro changeup-like pitches oriented **180° apart** and measured **about 8 inches of break difference.** A January 2020 deliberate-scuff test produced movement **counter to Magnus.** These were cannon experiments at Washington State's Sports Science lab with authentic 2019 MLB balls, on a machine that could repeat trajectory, rpm and velocity — so seam orientation was genuinely isolated.

**⚠️ Correction to a claim that circulates widely:** the foundational SSW work was **cannon/field experiments and PIV, not wind-tunnel smoke visualization.** Wind-tunnel separation-mapping came later. The actual evidence chain is: **PIV separation-point measurement → cannon repeatability tests → Hawk-Eye population data.**

**Reynolds-number dependence [ESTABLISHED], and it matters for our athlete.** Seam effects scale with Re. USU's Logan, Utah altitude (4,500 ft) means **90 mph at Logan ≈ 76 mph at sea level ≈ 92 mph at Denver.** **SSW behavior is velocity- and altitude-dependent, and lab results must be Re-matched before being applied.**

**What Hawk-Eye enabled [ESTABLISHED].** From 2020, MLB's Hawk-Eye system (12 cameras, up to 300 fps) **directly observes the spin axis at release** rather than inferring it from movement. SSW is detected as the discrepancy between the **inferred** axis (back-calculated from trajectory) and the **observed** axis (measured at release). Driveline's calibration check: **park error under 2° maximum, 21 of 30 parks under 1°** — which is what makes the signal below believable.

**Quantified SSW effects, 2020 MLB season** (Driveline, "An Introduction to Seam-Shifted Wakes and their Effect on Sinkers," 1 Nov 2020; "The Impact of Seam-Shifted Wakes on Pitch Quality," 10 Mar 2021):

| Finding | Value |
|---|---|
| League-average 2D axis deviation, **sinkers** | **~17.6°** |
| Sinkers, added movement | **+3 in run, +4 in drop** |
| Cutters | +3 in glove-side, +2 in drop |
| Changeups / splitters | substantial added drop |
| Four-seamers | a fair amount of cut |
| Sliders / curveballs | **no large league-wide effect** |
| **At the extremes** | **~9 inches** of lateral and/or vertical movement |

**[ESTABLISHED at the population level.]**

### The blunt assessment

| Claim | Status |
|---|---|
| SSW exists; boundary-layer separation mechanism; measurable by PIV and by Hawk-Eye | **ESTABLISHED** |
| Worth several inches league-wide on sinkers, cutters, changeups, splitters | **ESTABLISHED** |
| Reliable *prescriptive* coaching — this grip and seam orientation, for this pitcher, at his Re, to a target effect | **NOT SOLVED** |
| SSW effects are stable pitch-to-pitch (seam orientation at release is a high-variance motor output) | **UNKNOWN** |
| **SSW is causally good** | **CONTRADICTED BY DRIVELINE'S OWN DATA** |

**That last row deserves emphasis.** Driveline found **~42% of the pitches analyzed had *lower* Stuff+ despite their actual trajectory breaks.** **SSW adds movement. Movement is not automatically value.**

**The residual problem, which almost nobody states:** the SSW signal is computed as a *residual* after removing modeled Magnus, drag, and environment. **Anything the model gets wrong lands in the "SSW" bucket, including Hawk-Eye error.** Driveline is explicit that the residual is *"either non-Magnus effects or Hawk-Eye error."* **Population averages are trustworthy; any single-pitch SSW number should be read skeptically.**

**MARKETING:** the "death ball" branding; the implication that any pitcher can be taught to throw one in a session; and the framing that SSW *replaces* Magnus rather than adding a few inches to it. The underlying pitch (heavy-drop, arm-side-fade changeup from a seam-oriented, low-efficiency spin — Barton Smith calls it a discoball changeup) is physically real. The commercial packaging is not.

**Where the frontier actually is:** SSW is now mainstream application, not frontier research. The frontier is **cheap seam-orientation measurement** — Driveline's April 2026 CNN extracting spin axis and seam orientation from ordinary video. **No published accuracy validation against Hawk-Eye exists.** If it validates, real unlock. Until then, a demo.

### 2.4 Extension, release height, and perceived velocity

**The formula, recovered empirically.** Statcast's `effective_speed` field was reverse-engineered against `release_speed` and `release_extension` across 6,109 pitches:

> **Perceived Velocity = Release Velocity × 54.17 / (60.5 − Extension)**

Implied reference distance **54.173 ft, SD only 0.216 ft** across 6,109 pitches — essentially an exact recovery. The formula's neutral extension is **60.5 − 54.17 = 6.33 ft**, which independently confirms "league average extension ≈ 6.3 ft" as the baked-in reference. **[ESTABLISHED — own computation; MLB's own glossary page returns HTTP 406 to fetchers, so this recovery is stronger evidence than the glossary would have been.]**

**Note the reference is now slightly stale:** measured 2024 four-seam mean extension is **6.51 ft.** The league has gotten longer.

**mph per foot of extension, at 94 mph:**

| Extension (ft) | Perceived velo (mph) |
|---|---|
| 5.5 | 92.59 |
| 6.0 | 93.44 |
| 6.5 | 94.30 |
| 7.0 | 95.18 |
| 7.5 | 96.08 |

**≈ 1.7 mph per foot** — matching Devan Fink (FanGraphs, 24 Jun 2021). **But it is multiplicative, not additive: the gain scales with velocity.** At 85 mph it is **~1.55 mph/ft**; at 100 mph, **~1.83 mph/ft.** Harder throwers get more from the same extension gain.

**Elite benchmarks:** MLB mean 6.51 ft, p95 = 7.30, p99 = 7.60. Documented elite ~**7.5 ft** (Bailey Falter, Devin Williams, Logan Gilbert). Extension ≈ **1.04× pitcher height** on average; Devin Williams at 1.22× is the outlier. Low end: Germán Márquez 5.3 ft.

**⚠️ 7.5 ft appears to be a practical ceiling — a handful of pitchers, not a tail you can push indefinitely.**

**Two qualifications the extension enthusiasts skip:**

1. **Extension is mostly anthropometry plus stride length, and stride length is already a velocity lever** (β = 0.334 in the professional velocity model, `biomechanics.md` §3.5). You are not adding an independent skill; you are re-describing one you already coach.
2. **Extension lowers release height and flattens VAA** (§2.5). Good for a four-seam at the top of the zone. **Bad for a curveball.** Extension is pitch-type dependent, not universally good.

### 2.5 Vertical approach angle — the cleanest result in this document

VAA computed at the front of the plate from Statcast release-frame kinematics, four-seamers, n = 6,113. Values are magnitudes (VAA is descending/negative by convention).

| Population | Mean \|VAA\| | SD | p5 | Median | p95 |
|---|---|---|---|---|---|
| All four-seams | 4.75° | 1.01 | 3.12 | 4.76 | 6.40 |
| **Top of zone (plate_z 2.8–3.6 ft), n = 2,093** | **4.40°** | 0.55 | **3.50** | 4.38 | **5.31** |

**That second row is the operative benchmark: a flat four-seamer at the top of the zone is ~3.5–4.0°; a steep one is ~5.3°+.**

**The regression — n = 6,110, R² = 0.999:**

```
|VAA| = 9.069 − 1.084·(plate height, ft) + 1.055·(release height, ft)
                − 0.0927·(IVB, in) − 0.0630·(velocity, mph)
```

Coefficients are stable when restricted to top-of-zone pitches only (n = 1,597, R² = 0.996). **[ESTABLISHED — own computation, and it independently reproduces Zahradnik (Iowa Baseball Managers, 26 Oct 2020, n = 2,350 pitchers), who predicted VAA from extension and release height at R² = 0.945.]**

**Interpretation — this is the single most actionable table in Topic A:**

| Input | Effect on VAA | Verdict |
|---|---|---|
| **Release height** | **+1.06° steeper per foot** | **By far the biggest controllable lever.** Dropping slot one foot flattens VAA by a full degree ≈ **two SDs** of the top-of-zone distribution. |
| **Pitch location** | −1.08° per foot higher | Nearly equal and opposite leverage to release height. **Location is a VAA variable.** |
| **IVB** | only −0.093° per inch | Five extra inches of ride buys 0.46° — roughly **half** what half a foot of release height buys. **Elite IVB is a worse VAA lever than slot.** |
| **Velocity** | −0.063° per mph | Essentially negligible. +5 mph buys 0.32°. |
| Extension | drops out once release height is included | Acts through geometry, not independently. |

> **VAA is geometry. It is not a "stuff" trait.** And **any VAA figure quoted without its location is meaningless** — the same pitch has a different VAA at the top of the zone than at the bottom.

**VAA and whiffs — ESTABLISHED in direction, EMERGING in magnitude.** Alex Chamberlain (FanGraphs, 1 Feb 2022) gives VAA-Above-Average benchmarks after adjusting for pitch height: **+1σ = 0.5°, +2σ = 0.9°, +3σ = 1.4°.** His earlier piece (7 Jan 2021) establishes the key **interaction**: flat VAA works high in the zone, steep VAA works low, and **VAA matters most at the edges of the zone, not in the heart.** Reported R² ≈ 0.237 for SwStr% and ≈ 0.224 for whiff rate. Also: at the **bottom** of the zone, fastballs get roughly half the whiffs-per-swing of non-fastballs; at the **top** edge they match non-fastballs.

**⚠️ Be careful with the popular framing.** "Flat VAA causes whiffs" is incomplete. **The defensible claim is the interaction: flatter four-seamers generate whiffs higher in the zone and tolerate a lower target line; steeper ones must be located down. A low-slot pitcher with a flat VAA who lives at the belt gets punished.**

**The better framework, and it supersedes league-wide VAA:** Chamberlain's May 2025 piece on Andrés Muñoz shows VAA-above-average ignores hitter *expectation* — Muñoz's four-seam is +0.59° flat yet generates groundballs. **Max Bay's Dynamic Dead Zone** models arm angle, height-scaled extension, and acceleration components as a per-pitcher multivariate normal. **What matters is distance from your OWN expected shape given your slot, not from a league-wide average.** **[EMERGING, but this is the right mental model.]**

**Horizontal approach angle (HAA): EMERGING at best.** Not on Savant, thin public evidence, **no verifiable quantitative HAA→whiff study found.** Treat confident HAA coaching claims as unsupported.

**This all connects to the arm-slot finding already in the library** (`coaching-translation.md` §5): MLB release points ~2 in lower than 2016, arm angle down 1.41° since 2020, pitchers dropping slot 2°+ gained **+2.14 run value** and **+18.3 rpm** on the four-seam at a cost of ~0.15 mph. **The regression above supplies the mechanism: a lower slot flattens VAA at ~1.06° per foot. That is very likely why the league is drifting lower, and it remains the best-evidenced pitch-design lever in this document** — the only one with published numbers on both the performance side and the stress side.

---

## 3. Designing Each Pitch

### 3.1 MLB 2025 baseline table, RHP

*Computed from Baseball Savant pitch-movement, active-spin, spin-direction, and statcast_search endpoints. Mirror clock tilts and flip HB sign for LHP. HB direction noted arm-side/glove-side.* **[ESTABLISHED]**

| Pitch | Velo | Spin (rpm) | Active spin % (mean / IQR) | IVB (in) | HB (in) | VAA (°) | Measured tilt |
|---|---|---|---|---|---|---|---|
| Four-seam (FF) | 95.1 | 2339 | 89.1 / 84.8–95.8 | +15.7 | 7.4 arm | −4.66 | 1:05 |
| Sinker (SI) | 94.2 | 2201 | 85.5 / 79.8–92.8 | +6.8 | 15.0 arm | −5.76 | 1:26 |
| Cutter (FC) | 90.7 | 2434 | 46.5 / 37.7–55.4 | +8.7 | 1.9 glove | −5.83 | 12:06 |
| Gyro slider (SL) | 86.8 | 2478 | **32.0** / 23.5–39.2 | +1.4 | 4.6 glove | −7.61 | 9:56 |
| Sweeper (ST) | 83.3 | 2641 | **50.6** / 43.4–57.4 | +0.7 | 14.0 glove | −7.68 | 8:10 |
| Slurve (SV) | 83.1 | 2387 | 54.9 | −3.7 | 12.2 glove | −8.53 | 7:41 |
| Curveball (CU) | 80.1 | 2611 | 70.8 / 61.2–82.2 | −10.2 | 9.8 glove | −9.77 | 7:25 |
| Knuckle/spike CU (KC) | 83.1 | 2599 | ~71 | −9.6 | 6.8 glove | −9.48 | 7:25 |
| Changeup (CH) | 87.1 | 1802 | 88.5 / 83.1–96.5 | +3.8 | 14.5 arm | −7.38 | 2:02 |
| Splitter (FS) | 87.0 | **1390** | 83.4 / 77.6–91.9 | +2.8 | 11.7 arm | −7.66 | 1:52 |

**Extension is nearly constant across pitch types (6.35–6.54 ft) — do not chase per-pitch extension; chase it globally.**

**The gap between Hawk-Eye *measured* tilt and movement-*inferred* tilt is the SSW / axis-deviation signal.** Largest on cutter (12:06 measured vs 11:16 inferred), slider, changeup, splitter. **This is the number to look at on a Trackman/Hawk-Eye system to answer "is this pitch getting non-Magnus help."**

### 3.2 Velocity separation norms

*Per-pitcher deltas off the athlete's own four-seam, 2025. Mean (IQR), mph.* **[ESTABLISHED]**

| CH | FS | SL | ST | CU | FC | SI |
|---|---|---|---|---|---|---|
| **7.6** (6.1–8.7) | **8.2** (6.7–9.6) | **8.5** (7.3–9.8) | **11.6** (10.3–12.9) | **14.2** (12.2–15.7) | **4.7** (3.5–5.7) | **0.4** (0.0–0.8) |

Two coaching consequences:
1. **The sinker is not a velocity-separation pitch** — it is a shape/plane pitch at the *same* speed.
2. **A sweeper costs ~3 mph more separation than a gyro slider.** That is a real timing cost you pay for the sweep.

### 3.3 Whiff and value ordering

**Whiff-per-swing, 2025:** KC 38.3 · FS 34.6 · CU 33.6 · SL 33.0 · CH 32.1 · ST 30.4 · FC 22.3 · FF 21.5 · **SI 11.9.**
**Usage share:** FF 31.9% · SL 16.5% · SI 15.1% · CH 10.3% · ST 6.8% · FC 6.8% · CU 6.5% · FS 2.8% · KC 2.3%.
**wOBA-against (min 100 pitches):** FS .263 · CH .271 · ST .276 · CU .279 · SL .284 · FF .335 · FC .335 · SI .346.

**⚠️ The min-100 pool is survivorship-biased** — every RV/100 in it is positive. **Use for relative ordering only, never absolute levels.**

### 3.4 The design method — this part is transferable

1. **Measure what he already throws.** Ten pitches, **one device**, logged. (Never mix Rapsodo and Trackman — `biomechanics.md` §7.4.)
2. **Identify the gap in the arsenal, not the deficiency in the pitch** (§4.1).
3. **Change exactly one thing: grip, seam orientation, or intent cue.** Not mechanics. Pitch design that requires a delivery change is a mechanical intervention in a costume, and it will cost command (§7.1).
4. **Five to ten pitches per variant, device on, side by side.** Judge on: did the axis move, did efficiency hold, did velocity hold within ~1 mph.
5. **Re-test cold, on a different day.** Bullpen novelty effects are large — and per §10.1, in-session performance is not learning. A grip that works the day you find it and not the following week is a mood, not a pitch.
6. **Then test whether he can *locate* it.** A designed pitch he cannot command is worse than the one it replaced.

**Step 6 matters most and gets done least.** **[EMERGING — my synthesis, not a validated protocol.]**

**Your own gym's distribution is a better benchmark than any MLB table**, because Rapsodo and Trackman disagree systematically, and MLB averages are drawn from a population your 88-mph college arm is not in.

### 3.5 Pitch-by-pitch notes

**Four-seam — two partially independent archetypes.** FF IVB percentiles, RHP 2025: p10 12.1 / p25 14.0 / **median 16.0** / p75 17.6 / p90 19.0 in.
- **Ride archetype:** ≥18" IVB, ≥90% active spin, ~1:00 tilt. True four-seam grip, fingers on the horseshoe; cue "through the top half / fingers behind the ball."
- **Flat-VAA archetype:** ordinary IVB (14–16") but **low release height + high extension.** This is how low-slot arms play at the top of the zone. Freddy Peralta (2025: 94.8 mph, 16.8" induced VB, +1.2" vs velocity/extension-matched league) is the canonical case.

Per §2.5, **the flat-VAA route is the better-leveraged one** — release height beats IVB roughly 2:1 as a VAA lever.

**Sinker / two-seam.** Target ~+6 to +8" IVB, 14–16" arm-side, ~1:30 tilt, ~85% active spin, VAA −5.5 to −6.0°. **This is the original seam-shifted-wake pitch**, and seam orientation is the whole game. **[ESTABLISHED as physics; EMERGING as a reliably coachable target.]**
**Deployment warning [ESTABLISHED]:** RHP sinker usage to LHB has collapsed from 21% a decade ago to **9.7% in 2025** — the lowest on record (Ben Clemens, FanGraphs, 1 May 2025). The league solved the mirror-image platoon problem by *dropping the pitch*, not fixing it. Read that as a warning about single-handedness arsenals generally.

**Slider family — three distinct pitches, and the vocabulary confusion is expensive.**
- **Gyro slider:** 87 mph, 2478 rpm, **32% active spin (≈68% gyro)**, +1–2" IVB, 2–6" sweep. \|HB\| p25 2.4 / med 4.3 / p75 6.4".
- **Sweeper:** 83 mph, 2641 rpm, ~51% active spin, ~0" IVB, ~14" sweep. \|HB\| p25 11.5 / med 14.2 / p75 16.8".
- **Slurve:** separated from the sweeper almost entirely by **negative IVB** (median −3.8" vs ST +0.5"), not by sweep (12.2" vs 14.0").

**The SL/ST crossover sits at ~9–11" of glove-side HB.** MLB has never published a hard cutoff (the Statcast classifier is probabilistic) — **treat any single threshold as soft.**

**A design cue that actually works [ESTABLISHED, Driveline, Oct 2021]:** the velocity↔efficiency tradeoff is **pitcher-specific for sliders** — roughly half the league *gains* efficiency as slider velocity rises and half *loses* it. **Curveballs almost universally lose efficiency with added velocity** (you are buying speed with gyro). **Cutters almost universally gain it.** So: **test the tradeoff on your athlete before prescribing "throw it harder."**

**Curveball.** 80 mph, 2611 rpm, ~71% active spin, −10.2" IVB, 9.8" glove-side, VAA −9.8°. The **knuckle/spike curve is ~3 mph harder, ~3" less sweep, same drop — and posts the highest whiff rate of any pitch class (38.3%).** **⚠️ That is very likely a selection effect** (only pitchers who get something out of the grip keep throwing it), not a mechanism. **[EMERGING]**
Arm slot determines 12-6 vs. slurve: higher release → top-down, lower slot → horizontal. Cues that work: "yank it down with the middle finger," "throw it with the back of your hand," fingers *in front* of the ball pulling down. Spiking the index finger increases middle-finger pressure without a verbal cue. Driveline's target: **~10–15 mph off the fastball, ~25" of vertical break separation.** Their own honest line: **no single curveball profile vastly outperforms others — fit it to the arsenal.**

**Changeup — and strong evidence the conventional design targets are WRONG.**
Michael Rosen, FanGraphs, 17 Jun 2025, ["Changeups Are Weird"](https://blogs.fangraphs.com/changeups-are-weird/). **[EMERGING — single-source, and weaker than the original write-up implied. See correction box.]**

> ### ⚠️ CORRECTED 2026-08-13 — READ THIS BEFORE USING THIS ENTRY
>
> **The prior version of this section INVERTED Rosen's central finding. Do not re-import the old framing.**
>
> **What the article actually argues, as its main chain:**
> **velocity differential (fastball → changeup) → hitters get out in front (attack direction) → whiffs.** Rosen characterizes that relationship as **strong.** Velocity *separation* is the engine of the pitch in his account, not a null.
>
> **What has "basically no relationship" to changeup whiff rate is the pitch's ABSOLUTE velocity** — which is why a 92 mph Griffin Jax changeup and a 78 mph Hunter Gaddis changeup both post ~57% whiff. **Absolute velocity ≠ velocity separation.** The earlier phrasing "velocity showed virtually no correlation with changeup whiff rate" collapsed those two and reversed the coaching conclusion.
>
> **⚠️ Any statement in this library or elsewhere that "velocity separation doesn't predict changeup whiffs" is a reversal of the source and is wrong.**
>
> **Second correction — downgrade the two nulls.** The spin-axis-similarity null and the arm-angle-change null are **each a single unquantified sentence in the article**, with **no coefficient, no n, no chart, and no stated method.** They are real statements by a credible analyst, and they are much weaker evidence than a "cited null" implies. **Label them [EMERGING, unquantified] — not [FOLKLORE], and never "a published null."**
>
> **Third: the variable Rosen thinks actually matters, he could not test.** **Arm-speed similarity** is not publicly measurable, and he names it as the likely reason Cole Ragans' unremarkable-looking changeup dominates. **The most important design variable in the pitch is currently unmeasured by anyone outside an org.**

**What the article establishes, restated correctly:**

| Finding | Strength |
|---|---|
| **Fastball→changeup velocity gap → hitters swing early (attack direction) → whiffs** | **The article's main, affirmatively-argued chain.** Gaddis's changeup induced a **−26.1° pull-oriented attack angle**, the most extreme in baseball |
| **Absolute changeup velocity has basically no relationship with whiff rate** | Supported by the Jax (92 mph) / Gaddis (78 mph) contrast, both ~57% whiff |
| Spin-axis similarity to the fastball showed no predictive value | **[EMERGING, unquantified]** — one sentence, no coefficient |
| Arm-angle change showed no predictive value | **[EMERGING, unquantified]** — one sentence, no coefficient |
| Arm-speed similarity is the probable hidden variable | **Untested. Not publicly measurable.** |

> **The design targets, stated so they cannot be inverted again:**
> 1. **Buy separation.** The velo gap is the mechanism that makes hitters early, and being early is what produces the whiff. **~7.6 mph off the four-seam is the MLB changeup norm** (§3.2); the splitter norm is ~8.2.
> 2. **Kill the spin** — Driveline's target is ~500–800 rpm below the fastball; the splitter class averages 1,390 rpm, the lowest of any pitch, and posts the best wOBA-against in baseball (.263).
> 3. **Preserve arm speed.** Probably the most important variable and the one you cannot buy a device for. Judge it on 240 fps video, not on a Rapsodo report.
> 4. **"Mirror your fastball's spin axis" remains unsupported — but it is unsupported by one unquantified sentence, not by a measured null.** Do not chase it; do not claim it has been disproven.

Cues: "roll over the ball," "throw it with your ring finger," "pronate sooner," "swipe the inside of the ball," "flexible wrist." Lateral finger tilt toward the thumb on a two-seam grip reduces raw spin.

**Splitter / split-change.** 87 mph, **1390 rpm** (by far the lowest of any pitch class), 83% active spin, +2.8" IVB, 11.7" arm-side, 34.6% whiff, **best wOBA-against of any pitch class (.263 in 2025).** Design goal is unambiguous: **kill spin to create vertical separation off the fastball.** ~8 mph off the fastball is the norm. Requires hand size and finger-splay tolerance not every athlete has — test before programming.

### 3.6 The sweeper — and why the alpha is gone

**Origin [ESTABLISHED].** Not a new pitch. NPB pitchers, Yu Darvish prominently, threw accentuated sweeping sliders for years. What is new is (a) the Dodgers and Yankees popularizing it as a *deliberate design target* from late 2021 into 2022, and (b) **Statcast creating "ST" as its own classification in 2023**, alongside "SV" (slurve).

**Mechanism [ESTABLISHED physics].** ~51% active spin — the axis is tilted well off the direction of travel, so this is **genuine Magnus sidespin**, unlike the gyro slider's 32%. SSW contributes additionally (the measured-vs-inferred tilt gap is material). Gyro degree is the working coaching variable. **The design tension is explicit: sweep costs velocity.**

**The platoon penalty — Ben Clemens, FanGraphs, 2 Sept 2022. These are the definitive numbers. [ESTABLISHED]**

| RHP vs **RHB** | Sweeper | Non-sweeper SL |
|---|---|---|
| Whiff% | 36.4 | 35.3 |
| wOBA on contact | **.325** | .357 |
| BABIP | **.246** | .277 |
| GB% | 33.0 | 45.6 |
| **Popup%** | **20.3** | 13.1 |
| **RV/100** | **−0.94** | −0.26 |

| RHP vs **LHB** | Sweeper | Non-sweeper SL |
|---|---|---|
| Whiff% | **28.5** | 31.8 |
| wOBA on contact | .370 | .370 |
| BABIP | .284 | .268 |
| **RV/100** | **−0.05** | **−0.35** |

> **Read that carefully. The sweeper's edge is NOT whiffs — it is popups and BABIP suppression** (+7.2 pts popup rate, −31 pts BABIP vs same-handed hitters). **And the entire effect vanishes and actually inverts against opposite-handed hitters** (−0.05 vs −0.35 RV/100 — the ordinary slider is *better*). Pitchers halve sweeper usage vs. opposite-handed batters, correctly.

**Adoption [ESTABLISHED, Clemens, 1 May 2025]:** league sweeper share **1.1% (2020) → 7.6% (2025).** Slider share fell 16.8% → 14.9%. RHP-to-RHB sweeper usage **2.6% (2021) → 10.7% (2025).**

**Has it plateaued or reversed? Yes — three independent confirmations. [EMERGING]**
1. **Driveline** (Jack Lambert, 31 May 2024, Stuff+ v4): *"Sweepers received lower ratings, reflecting hitter adaptation since their peak effectiveness in 2021."* **Their model repriced the pitch downward.**
2. **Savant arsenal stats:** sweeper whiff% **33.4 (2023) → 31.0 (2024) → 31.2 (2025)**, while the ordinary slider held at ~35.
3. **2026 usage:** Brad Johnson (RotoWire, 29 May 2026) puts the sweeper at *"about 7 percent of pitches"* — flat-to-down from 7.6% in 2025.

> **Verdict: the sweeper is a correctly-priced, same-handed, weak-contact pitch that the league has fully absorbed. The alpha is gone. Building an arsenal around it as a primary weapon in 2026 is late.**

**Skeptical footnote:** Gavin Addleman (10 Apr 2026, self-published but real analysis) argues sweepers and sliders are genuinely distinct (sweeper xwOBA .246–.275 vs slider .282–.302, 2021–25) but presents **no formal bimodality test** — the case rests on visual separation. **Treat "distinct pitch type" as a convention, not a fact.**

### 3.7 The kick-change — verified

**Real. Reporting confirmed across four independent outlets.**

- **Developer: Leif Strom, director of pitching at Tread Athletics (Charlotte, NC), 2023.** He searched Tread's archive specifically for a pitch that would let **supinators** neutralize opposite-handed hitters — supinators cannot pronate a conventional changeup. He identified, named, and built the analytical understanding of it. (ESPN 2025; Yahoo Sports, Baker & Tracy, 9 May 2025.)
- **First MLB game use: Hayden Birdsong (SF), June 2024**, after finding Strom's social-media post.
- **⚠️ Independent parallel line [VERIFIED, FanGraphs, Davis Martin & Matt Bowman interview]:** Martin learned it from **Ethan Katz and Brian Bannister** as a supinator alternative. **So the "invented by one person" framing is too clean.** Strom's claim to naming and formalizing it is solid; **sole-inventor claims are UNVERIFIED.**

**Mechanism [ESTABLISHED].** The middle finger is **spiked/raised** rather than laid flat; it is the last thing to touch the ball and "kicks" the axis forward through release. The ring finger cuts efficiency, creating tumble. Martin uses a two-seam base, traces the seam, spikes with the middle finger, targeting a **3 o'clock axis.** Bowman's framing: it sits on the same spectrum as a split-change, differentiated primarily by **rpm**.

**Measured results — small samples, early-2025 snapshots:**

| Pitcher | Result |
|---|---|
| Davis Martin | ~90 mph, **+1 to −1" vert**, 10–20" horizontal |
| Clay Holmes | **−10" vert at 88 mph**, 38.2% whiff, .182 BAA, 16.2% usage, 2.95 ERA thru 7 starts |
| Tylor Megill | **50% whiff** on 41 kick-changes, 2.50 ERA over 7 outings |
| Griffin Canning | 2.50 ERA thru 7 starts after a 5.19 prior |
| Hayden Birdsong | **46.7% whiff**, .188 BAA |

Other adopters: Jack Leiter, Pablo López, Andrés Muñoz.

**Honest assessment.** The mechanism is real and physically coherent. **The results are a small-sample, selection-biased snapshot — only the successes got written about.** No end-of-2025 league-wide kick-change evaluation exists. **Statcast does not classify it separately** (it shows up as CH or FS), so league-level public tracking is currently impossible. **Label the pitch EMERGING; label "the pitch of 2025" MARKETING.**

**Why it is still the right kind of project:** it is a **grip-and-release change, not a mechanics change** — cheap to test, low stress cost, reversible. That risk profile is rare. The library's counterweight stands and should be said out loud to any athlete adding one: **MLB pitch-tracking studies associate increased changeup velocity and increased changeup spin/movement with UCL-reconstruction odds** (§4.4). Tag it and move on.

---

## 4. Arsenal Construction, Tunneling, and Stuff Models

### 4.1 Shape gaps — the organizing principle

**The defensible framework is Max Bay's Dynamic Dead Zone:** model release characteristics (measured arm angle, height-scaled extension) and acceleration components jointly as a **per-pitcher** multivariate normal, and measure how far each pitch sits from the shape a hitter would expect *given that pitcher's slot*. This replaces the static league-wide "dead zone." Bay co-built Stuff+ and now works in Dodgers R&D.

> **Shape gaps are relative to your own release, not to the league.** **[EMERGING, but this is the right mental model.]**

**Construction rules that survive the evidence:**
1. **Cover both movement halves.** Sweeper-only right-handers get neutralized by LHB (§3.6). The 2025 collapse of RHP sinkers-to-LHB (21% → 9.7%) shows the league solving the mirror-image problem by *dropping* the pitch rather than fixing it.
2. **Separate on plane and timing, not just movement.** The velocity separation norms in §3.2 are the guardrails.
3. **The sinker/four-seam pair is a *plane* split at identical velocity** (+15.7 vs +6.8 IVB, 0.4 mph apart) — a legitimate and underrated gap.
4. **Most amateur pitch-design projects try to improve the pitcher's best breaking ball. Most of the available value is in the missing quadrant.**

### 4.2 Tunneling — be blunt: it is over-sold

**Origin [ESTABLISHED].** Jeff Long, Jonathan Judge & Harry Pavlidis, Baseball Prospectus, **25 Jan 2017**. Tunnel point originally **23.8 ft** from the plate (~175 ms); revised **31 Jan 2018** (Long, Pavlidis, Alonso) to **150 ms**, calculated from batter eye height, citing a Waseda University study that the final third of the trajectory contributes nothing because the required angular eye velocity exceeds physiological limits. Metrics: Tunnel Differential, Plate Differential, Break Differential, Flight-Time Differential, Release Differential, Break:Tunnel Ratio, Release:Tunnel Ratio. League means: tunnel diff 10.0", plate diff 18.7", break diff 2.6", release diff 2.4", break:tunnel 27.6%.

> **⚠️ Critical fact: neither the 2017 introduction nor the 2018 update reported a single correlation with outcomes.** The metric suite was published **without predictive validation** and was adopted on aesthetic appeal (the "column of milk" image). **That is the root of the over-selling.**

**What later work actually found:**

| Study | Design | Result |
|---|---|---|
| **Jon Roegele**, THT, 24 Nov 2014 (pre-dates BP) | PITCHf/x 2013–14, ≥150 sequences | Real "in-band" effect: SwStr% lift **0.7–8.2 pts** by pitcher (Hamels +6.0). But pitcher **year-over-year repeatability R² = 0.24.** **Never converted to run values.** |
| **Michael Augustine**, 2020 | 401 pitchers, ≥50 pairings, BP tunnel data | Top-15% vs bottom tunnelers: SwStr 10.1% vs 6.1%; K/BB 2.69 vs 2.26; EV ~1 mph. **Explicitly notes he cannot establish intent; confounded with overall pitcher quality.** |
| **Zack Bryant**, 27 Sept 2024 | 100 random pitchers, ≥3 pitch types, ≥200 pitches; custom Tunnel Score+ vs Savant run values | **r = 0.07.** *"Almost no relationship at all."* |

**The strongest positive evidence is a different thing entirely — and it is the actionable one.**
**Michael Rosen, FanGraphs, 13 Jun 2024, "The Kirby Corollary":** **horizontal release angle (HRA) overlap** between fastball and slider predicts swings at **59% accuracy vs Stuff+'s 54%.** Slider Stuff+ correlated with called-strike% at **r² = 0.001**; **release-angle overlap at r² = 0.12 (2023), 0.20 (2022).** Kershaw and Strider maximize HRA overlap and generate swings through visual confusion. **George Kirby's command precision comes at the cost of release-angle overlap** — a real, named trade.

**And BP itself pivoted.** Stephen Sutton-Brown, **17 Jan 2025**, replaced pairwise tunnel differentials with four **arsenal-level** metrics — Pitch Type Probability, Movement Spread, Velocity Spread, Surprise Factor — reporting that above-average values worsen batter decision rates and raise whiff probability.

**Synthesis for a coach:**

- **FOLKLORE / over-sold:** *"Tunnel your fastball and slider through a 24-foot window."* Pairwise tunnel-differential metrics have **~zero correlation with run value (r = 0.07)**. And nobody can execute a tunnel intentionally, pitch to pitch, at the inch scale those metrics measure.
- **ESTABLISHED and actionable:** early-flight **release** similarity — specifically **horizontal release angle** — measurably changes swing decisions, and does so **better than stuff models do.** This is a **static property of your delivery, trainable in a bullpen**, not a sequencing decision.
- **EMERGING:** arsenal-level unpredictability (movement spread, velocity spread, surprise factor) is a better frame than pairwise tunneling.

> **Train release consistency. Do not build sequences around tunnels.** Sequence on expected outcome, count, and hitter tendency. Note this ties Topic A directly to Topic B: **release consistency is a stuff variable AND a deception variable** — see §6, where release-point variability predicts K/9 and HR/9 but not walks.

### 4.3 Stuff models — construction

| Model | Built by | Inputs | Type | Output scale |
|---|---|---|---|---|
| **Stuff+** | Eno Sarris & Max Bay (now Sarris + Owen McGrattan) | Release point, velocity, V/H movement, spin rate, **axis differential (SSW proxy)**, pitch type; secondaries judged **relative to the pitcher's own primary fastball** | Decision-tree | 100 = avg, **10 pts = 1 SD at the pitch level** |
| **Location+** | same | **Location only** — count-adjusted, pitch-type adjusted, batter handedness. No velocity, no movement | Zone-value | same |
| **Pitching+** | same | Physical characteristics + location + count + handedness. **Not** a weighted average | Integrated | same |
| **PitchingBot** | **Cameron Grove** (ex-Durham astrophysicist, DESI; SMT/UCSAS 2022 winner; now Cleveland Guardians) | Adds **extension, spin efficiency, spin-axis deviation, plate location** as explicit inputs | XGBoost, many small event-probability sub-models split by pitch family | botStf / botCmd / botOvr on the **20–80 scouting scale**, plus botxRV100, botERA |
| **tjStuff+** | Thomas Nestico (U. Toronto) | v3: LightGBM, >1.6M pitches, RobustScaler, LHP mirrored | — | mean 100 / SD 10, built on xRV/100 (mean 0.35, SD 0.68) → **130 tjStuff+ ≈ +2 runs per 100 pitches** |
| **Driveline Stuff+** | Jack Lambert (31 May 2024) | Velocity, VB, HB, **arm angle**, extension, location-adjusted **VAA/HAA**. No locations | — | three non-comparable buckets |

**Observed starter SDs: Stuff+ 12.16, Location+ 3.34, Pitching+ 4.94.** Relievers: 17.02 / 5.87 / 6.61. **A reliever→starter transition costs ~5.5 Stuff+ points.**

**Two Driveline findings worth keeping:** velocity → Stuff+ is **exponential above ~96 mph**, not linear; and **sinkers grade above four-seams below ~97 mph.** **⚠️ Driveline disclosed no R², RMSE, or training-set size — evidentiarily weaker than it presents.**

**Pitch-type Stuff+ averages (starters):** FF 99.2 ± 18.3 · SL 110.8 ± 15.6 · KC 110.3 ± 16.4 · FS 109.6 ± 30.2 · CU 105.5 ± 16.8 · FC 102.1 ± 14.0 · SI 92.5 ± 13.6 · CH 87.2 ± 16.4.

> **⚠️ This is the single most misused table in public pitch analytics.** Sliders average 110 and changeups 87 **not because sliders are better pitches**, but because the model is scaled within pitch type and these reflect how each pitch is used and against whom. **A pitcher does not improve his arsenal by throwing more sliders because sliders "grade higher."**

### 4.4 What stuff models MISS — the section that matters most

**(a) The team-switcher test — ESTABLISHED and damning.**
Baseball Prospectus, weighted Spearman, 2021 metric → 2022 ERA; **342 same-team pitchers vs 231 who changed teams**, bootstrapped 5,000 samples (SD .05–.07):

| Metric | Same team | All | **Switched teams** |
|---|---|---|---|
| **Stuff+** | .41 | .33 | **.14** |
| Location+ | .00 | .09 | .24 |
| Pitching+ | .35 | .31 | .23 |
| DRA | .32 | .30 | .27 |

> **Stuff+'s predictive power largely vanishes for team-switchers.** It is partly measuring *the team's* pitch-design program, defense, catching, and park — **not the pitcher.** For a developing athlete who will change environments repeatedly, that r ≈ .14 is the number to remember.

**(b) Goodhart's Law / model decay — ESTABLISHED, and this is the best 2026 citation.**
Davy Andrews, FanGraphs, **20 Jan 2026**, 2,860 pitcher-seasons 2020–25, min 400 pitches: **Stuff+ standard deviation across pitchers fell 9.7 (2020) → 8.8 (2025), ~9% compression.** Below-average-stuff pitchers fell from 12% (2021–23) to 9% (2024–25). Correlation between stuff grades and wOBA declined across all four measures.

> **When everyone optimizes to the metric, the metric stops discriminating.**

**(c) Population drift.** Driveline and Nestico independently document the sweeper falling from ~115 Stuff+ (2021) to under 95 today as hitters adapted. Models get retrained and silently reprice arsenals. **Cross-vintage Stuff+ comparisons are invalid.**

**(d) Command, sequencing, and interaction.** Location+ correlates −0.54 with BB%; Stuff+ only −0.15 (§1). **No public stuff model handles sequencing, arsenal interaction, bullpen-vs-game intent, within-game usage decay, or platoon deployment.**

**(e) The injury association — EMERGING but peer-reviewed, and this one is not optional to mention.**
**Mastroianni et al., *American Journal of Sports Medicine*, May 2025** (PMID 40230317): 115 MLB pitchers with UCL reconstruction/repair vs 230 matched controls, Apr 2018 – Nov 2023. Higher fastball/changeup/sinker velocity, higher slider spin, and longer cutter extension were all associated with surgery; **changeup Stuff+ and FB/CH/SI Pitching+/Location+ showed significant differences.** Case-control → association, not causation.

> **The inputs stuff models reward overlap heavily with the inputs that predict UCL surgery.** This document is scoped to development, not injury prevention, so I state it once and move on — **but a coach optimizing an 85+ mph arm's Stuff+ should know he is optimizing toward a measured risk gradient.**

**(f) FOLKLORE alert.** Jeff Zimmerman (RotoGraphs, May 2023) reported r² = .996 (Stuff+) and .992 (PitchingBot). **These are curve-fits of bucketed group means to ERA, not pitcher-level predictive r²**, and they are routinely laundered as the latter. **If you see r² > .9 for a stuff model predicting ERA, it is this number being misquoted.**

**(g) Real predictive performance, for calibration.** tjStuff+ v1 vs ERA: same-season r = −0.38; prior-season tjStuff+ → ERA r = −0.34 (vs prior xFIP 0.29, prior ERA 0.20). **It beats prior ERA as a forward predictor — and −0.34 is a modest correlation.** Stabilization: tjStuff+ v2 median **220 pitches (~3 starts)**; meaningful wOBA prediction ~400. Stickiness: tjStuff+ v2 2022→23 R² = 0.78; v3 2023→24 r = 0.85.

### 4.5 How to use them

**Should:** as a **fast, low-sample (80–250 pitch) shape screen** — "does this new pitch grade better than the one it replaces?" A/B grips in a bullpen. Use tjStuff+/botStf **within a pitcher, within a season, within one model vintage.** Read Location+/botCmd separately and never average them mentally.

**Should not:** compare Stuff+ across years or across models. Treat a high Stuff+ as a forecast for an athlete changing environments (r ≈ .14). Chase Stuff+ by adding velocity and slider spin without weighing §4.4(e). Assume the model prices platoon, sequencing, or arsenal fit — **none of them do.**

**BP's stated doctrine is worth adopting verbatim:** include an input only if you can **articulate its causal pathway** *and* it **improves out-of-sample.**

---

# TOPIC B — COMMAND

## 5. Command Is an Angular Problem

**This is the most important finding in the document and almost nobody coaches it.**

**Kusafuka, Kobayashi, Miki, Kuwata, Kudo, Nakazawa & Wakao (2020), *Frontiers in Sports and Active Living* 2:36.** n = 7 skilled pitchers (one former NPB professional), **187 four-seam fastballs**, TrackMan plus an aerodynamic simulation varying each release parameter individually. **`[SAMPLE MISMATCH on velocity — mean ~32.6 m/s ≈ 73 mph. The physics, however, is velocity-independent.]`**

| Release parameter | Effect on location at the plate |
|---|---|
| **Elevation (vertical) release angle** | **~30 cm per 1°** |
| **Azimuth (horizontal) release angle** | **~30 cm per 1°** |
| Release speed | ~20 cm per 1 m/s (vertical) |
| Vertical release point | ~1 cm per 1 cm |
| Horizontal release point | ~1 cm per 1 cm |

Model fit: **R² = 0.97 ± 0.02 (vertical), 0.96 ± 0.04 (horizontal).** Standardized coefficients largest for elevation/azimuth angle (~0.30). Measured within-pitcher SDs: release speed ±1.0 m/s, elevation angle ±1.1°, azimuth angle ±1.09°.

✅ **VERIFIED CLEAN 2026-08-13 (PMID 33345028) — 30 cm per 1° confirmed for BOTH elevation and azimuth. Do not re-check.**

**Independent geometric check:** release is ~54.5 ft from the plate. `tan(1°) × 54.5 ft = 0.951 ft = 11.4 in = 29 cm`. **The paper's 30 cm/° is trigonometry, and therefore not sample-dependent.** **[ESTABLISHED]**

### 5.1 What this means

**Release angle is roughly 30× more consequential than release position.** A full inch of release-point wander costs one inch at the plate. **One-thirtieth of a degree of release-angle wander costs the same inch.**

Multiply through: **±1.1° × 30 cm/° ≈ 33 cm ≈ 13 inches of 1-SD location scatter from release angle alone.** That single term accounts for essentially the entire observed miss distance.

**Three coaching consequences:**

1. **Chasing "a repeatable release point" on a Rapsodo report is chasing the wrong variable by a factor of ~30.** Release point is a *proxy* for delivery consistency, not a cause of location error. §6 is the empirical confirmation.
2. **Velocity variability is a command variable.** ~20 cm of vertical location per 1 m/s → **1 mph (0.447 m/s) ≈ 9 cm ≈ 3.5 inches of vertical miss.** A pitcher whose fastball ranges 91–95 in an outing carries **~14 inches of vertical scatter from velocity alone**, before any angular error. **This is large, measurable with a radar gun you already own, and almost universally uncoached.** **[ESTABLISHED — arithmetic on a verified sensitivity.]**
3. **The authors' own conclusion matters most:** improving the reproducibility of each parameter individually is **not** the optimum. Skilled pitchers show **compensatory covariation** — different combinations of release parameters landing in the same spot. This is the uncontrolled-manifold idea (§8) arriving independently from ballistics.

**Corroboration at MLB scale, different method.** The **Kirby Index** (Rosen, FanGraphs, 3 May 2024): release *angles* plus release points predict actual pitch location at **R² = 0.92 vertical / 0.85 horizontal** across ~230,000 four-seam fastballs. A model using spin, velocity, extension, and release height/width but **excluding release angles collapses to R² = 0.06 / 0.05.** **[ESTABLISHED]**

---

## 6. Release-Point Variability: the numbers, and a debunking

**Wakamiya, Nagamoto, Yamaguchi, Okunuki, Maemichi, Liu, Ogawa, Kobayashi & Kumai (2024), *Frontiers in Sports and Active Living* 6:1447665.**

✅ **VERIFIED CLEAN 2026-08-13 (PMC11608975) — n = 344 MLB starters; BB/9 R² = 0.011, K/9 R² = 0.345, HR/9 R² = 0.072 all confirmed. Do not re-check.**

**344 MLB pitchers (300,884 four-seams, 517,530 breaking balls) and 64 MiLB pitchers (42,585 / 77,440), 2021–2023.** Inclusion: ≥1,500 pitches/season, ≥70% starts, >5% four-seam usage. Variability = 95% confidence ellipse dimensions, cm. **[POPULATION MATCH — the best command dataset in existence for our athlete.]**

| Four-seam measure | MLB | MiLB | p |
|---|---|---|---|
| RPX (horizontal), cm | **30.60 ± 12.29** | 35.21 ± 16.17 | .014 |
| RPZ (vertical, coronal), cm | **15.21 ± 2.52** | 17.48 ± 3.43 | <.001 |
| RPZ (vertical, sagittal), cm | 15.70 ± 3.06 | 17.30 ± 3.22 | <.001 |
| 95% ellipse area (coronal), cm² | **373.50 ± 184.81** | 497.06 ± 300.81 | <.001 |

Breaking balls: RPX 35.39 ± 15.24 vs 39.54 ± 16.77 (p = .002); ellipse 471.00 ± 287.70 vs 625.54 ± 352.58.

**Reading 1 — MLB pitchers are tighter, and horizontal is the discriminator.** The horizontal gap (~4.6 cm) is roughly double the vertical gap (~2.3 cm). **[ESTABLISHED]**

**Reading 2 — the debunking.**

| Outcome | Model R² | Release-point term |
|---|---|---|
| xFIP | 0.207 | RPX variability β = +0.161, p = .002 (2nd predictor after velocity, β = −0.398) |
| K/9 | 0.345 | RPX variability β = −0.122, p = .006 |
| HR/9 | 0.072 | RPX variability β = +0.168, p = .002 |
| **BB/9** | **0.011** | **Only velocity entered (β = 0.118, p = .029). Release-point variability NOT significant.** |

> **Release-point variability relates to strikeouts and home runs — deception and pitch quality — and has essentially no relationship with walk rate.**
>
> The folk model *"repeatable release point → command → doesn't walk guys"* is **not supported at the MLB level.** **[ESTABLISHED as a null result, n = 344.]**

**This is exactly what §5 predicts.** Release point moves location ~1:1 against a ~30 cm/° angular term. It cannot carry command because it is not where command lives.

**What release-point consistency IS good for: deception.** K/9 and HR/9 — the hitter's read of the ball out of the hand. That is real and valuable, and it connects directly to §4.2's Kirby Corollary finding that **horizontal release-angle overlap changes swing decisions better than stuff models do.** It is simply not command.

**Real limitations:** season-aggregated variability confounds intentional release differences across locations and pitch types; starters only; breaking balls pooled; no spin or biomechanical data; only ~20% of xFIP variance explained.

---

## 7. The Mechanical Signature of Plus Command

**Manzi, Dowling, Wang, Arzani, Chen, Nicholson & Dines (2021), *Journal of Orthopaedics* 27:28–33 (PMID 34475727).**

**n = 338 professional pitchers** (MLB and Low-A through AAA), split by location spread into high-consistency (n = 91) vs low-consistency (n = 98) at ±0.5 SD, normalized to grid width; 8–12 fastballs each, marker-based mocap at 480 Hz. **Velocity ~37.9–38.4 m/s ≈ 85–86 mph in-lab — POPULATION MATCH** (per `biomechanics.md` §0, a 90–93 mph game arm).

| Variable at ball release | High-consistency | Low-consistency | p |
|---|---|---|---|
| **Arm slot (°)** | **59.7 ± 13.5** | 54.7 ± 12.4 | .009 |
| **Trunk lateral flexion (°)** | **−27.1 ± 9.3** | −31.8 ± 9.0 | **<.001** |
| **Trunk tilt (°)** | **−33.4 ± 9.1** | −37.2 ± 8.9 | .004 |
| **Trunk flexion (°)** | **11.9 ± 10.0** | 15.9 ± 9.0 | .005 |
| Stride length (%BH) | 77.8 ± 5.5 | 79.4 ± 5.3 | .048 (n.s. at α = .01) |
| Shoulder distraction force (%BW) | 112.4 ± 15.9 | 118.3 ± 15.1 | .001 |
| Elbow distraction force (%BW) | 110.5 ± 17 | 117.0 ± 15.2 | .006 |

**Velocity did not differ (p = .055).** This is a genuine command contrast, not a velocity confound. **[ESTABLISHED — n = 338, velocity-matched.]**

### 7.1 The three-way conflict the library has not previously named

**Consistent pitchers stand taller and less tilted.** Higher arm slot, ~5° less lateral trunk flexion, ~4° less forward tilt, ~4° less trunk flexion at release.

**The mechanism is §5:** less lateral trunk tilt means the release-angle vector is less sensitive to small trunk perturbations. If the release angle is generated by a heavily tilted trunk, a 1° trunk error becomes a 1° release-angle error — **and 1° is 12 inches.**

**Now put this against the library's velocity model** (`biomechanics.md` §3.5, §6.3):

| Variable | Effect on VELOCITY | Effect on COMMAND | Effect on ELBOW TORQUE |
|---|---|---|---|
| **Trunk flexion at BR** | **↑↑** (β = 1.829) | **↓ consistency** (11.9° vs 15.9°) | — |
| **Trunk lateral tilt at BR** | ↑ (part of "get out over it") | **↓ consistency** (−27° vs −32°) | **↑** |
| **Higher arm slot** | Neutral | **↑ consistency** (59.7° vs 54.7°) | **↑** in pros |

> **The deliveries that maximize velocity are not the deliveries that maximize command.** An athlete being pushed toward more forward and lateral tilt is being pushed toward velocity and **away from** command. **Say that out loud before you push.**
>
> And note the arm-slot square: a **higher** slot predicts better command but **higher** elbow torque — while `coaching-translation.md` §5 recommends going **lower** for stress and for four-seam VAA/run-value. **[EMERGING as synthesis; the underlying findings are individually ESTABLISHED.]**

These are cross-sectional population associations, not three dials on one athlete. But the direction is clear and the trade is real.

### 7.2 Foot contact is where command is decided

A second **Manzi et al. (2021), "Kinematic Models For Pitch Location Metrics in Professional Baseball Pitchers," *Archives of Sports Medicine*.** **n = 322 professional, velocity 38.4 ± 1.7 m/s (POPULATION MATCH)**, elastic net + random forest.
**⚠️ Published in a low-profile open-access venue (Scholars.Direct) with weak indexing; location charted manually by pitching staff from behind the mound. The author group (Dines, HSS) is legitimate and the sample overlaps the *J Orthop* paper. [EMERGING, low-tier venue.]**

- **Accuracy model**, top random-forest importances: **trunk tilt at foot contact (6.6%)**, lead hip flexion at FC (4.2%), shoulder abduction at FC (4.2%), trunk tilt at BR (3.8%).
- **Consistency model (R² = 0.57):** trunk tilt at FC (3.7%), trunk flexion at BR (3.3%), lead foot rotation at FC (3.2%), back hip flexion at FC (2.6%).
- Authors: *"Four of the top six parameters in both models involved variance at the hip and trunk."*

**Three independent routes now converge on foot contact:** these professional datasets, the Driveline command study (§8.3), and the library's Rule 2 (`coaching-translation.md` §1), which was derived from phase durations alone. **[ESTABLISHED as a direction; effect sizes modest.]**

### 7.3 Command and velocity have different mechanical drivers

**Agresta, Freehill, Nakamura, Guadagnino & Cain (2022), *Sensors* 22(21):8488.** n = 10 collegiate, six APDM Opal IMUs at 512 Hz, ~35 pitches, Rapsodo 2.0.

- **COMMAND:** of all variables, **only peak forearm resultant linear acceleration** survived (β = 0.008, SE 0.003, p = .010).
- **VELOCITY:** ten variables — torso-pelvis peak separation angle (β = 0.29, p < .001), torso peak rotation rate (β = 0.03, p < .001), upper-arm orientation at foot strike (β = 0.16, p < .001), time of torso-pelvis peak separation (β = 3.82, p = .016), ball release timing (β = −66.15, p = .017).

**Authors' framing: command lives at the end-effector; velocity lives in proximal-to-distal sequencing.** Consistent with §5 — command is a release-angle problem, and the release angle is set distally.

**⚠️ Command was measured by a subjective 5-point Likert self-rating spoken aloud. n = 10. [EMERGING at best.]**

### 7.4 Off-population, flagged

*"Kinetic and kinematic comparisons in high school pitchers with low and high pitch location consistency,"* JSES 31(12), 2022 (PMID 35931332). **n = 59 high schoolers — `[SAMPLE MISMATCH]`.** High-consistency showed decreased lead hip flexion at elbow extension (40 ± 12° vs 52 ± 13°), decreased back hip extension, increased back hip internal rotation at FC; multiregression predicted **0.49** of location-consistency variance. **Directionally consistent with the pro data (hips at foot contact). Do not transfer the joint-angle values to an 85+ athlete.**

---

## 8. Repeatability, Adjustability, and the Uncontrolled Manifold

### 8.1 The method

**Scholz, J.P. & Schöner, G. (1999), *Experimental Brain Research* 126(3):289–306, PMID 10382616.** **[ESTABLISHED — verified.]**

UCM partitions trial-to-trial variance in *elemental* variables (joint angles) relative to a *performance* variable (release point/angle) into **V_UCM** (does **not** change the outcome) and **V_ORT** (does). Synergy index Δ = (V_UCM − V_ORT)/V_TOT; Δ > 0 means the joints are covarying to protect the outcome.

Antecedents: **Bernstein (1967)**, *The Co-ordination and Regulation of Movements*; **Latash's motor abundance.** **[ESTABLISHED as canonical; not independently re-verified.]**

**Why a pitching coach should care:** "Should he repeat his delivery?" is the wrong question. **The right question is: which joint variability moves the release point, and which doesn't?** Only the first kind costs command.

### 8.2 The Bloebaum UCM analysis — and a correction

**Bloebaum, A. (Driveline). SportRxiv preprint, doi 10.51224/SportRxiv.1010.** **43,650 game-speed pitches, 4,338 athlete-sessions, 2,052 pitchers**, median 9 trials/session, markerless capture; 15 throwing-side joint angles from peak knee height to ball release; release-point variance decomposed with a validated forward-kinematic model; reproduced on the public OpenBiomechanics marker-based cohort. **By an order of magnitude the largest kinematic-variability dataset in the public literature.**

> **⚠️ CORRECTION TO THE PRIOR CYCLE'S BRIEF. The synergy index partial ρ = 0.22, p < 10⁻⁴⁷ at release is an association with PITCH VELOCITY, not with command.** This is not a command paper. `idea-scouting.md` #3 and `coaching-translation.md` §6 both present it in a command context; **both should be corrected.** It remains highly relevant — as a description of how variability is *structured*, not as evidence about accuracy.

**Findings:**
- Synergy index Δ higher in **higher-velocity** pitchers (partial ρ = 0.22, p < 10⁻⁴⁷); Δ **surges at ball release**.
- **Joint-angle SD does not decline monotonically toward release.** Convergence is **segment-staggered**: trunk/pelvis reach their variability minimum **before foot plant**; the shoulder only at maximum external rotation.
- **Proportional funnel depth is invariant across skill levels.** Higher-velocity pitchers have a **lower absolute variability floor**, not a different convergence shape.
- **Trunk degrees of freedom carry only ≈5% of release-preserving variance** — the synergy is an arm-chain phenomenon over a stable proximal base.
- All velocity associations survived athlete-level mixed models.

**[EMERGING — preprint; Driveline analyzing its own athletes with its own pipeline; ρ = 0.22 is modest. But sample size and method pedigree are both strong.]**

### 8.3 The Driveline command study, stated precisely

**"The Interaction of Biomechanics and Command," Driveline Baseball, Feb 2026.** Winner of the 2025 SABR Dr. Mike Marshall Pitching Biomechanics Research Award.

**n = 27 athletes, 270 throws** (first 10 per athlete), from weekly sessions of 8–20 **middle-middle fastballs at ~90% intensity** on Velocity-phase "A Days." College → independent → affiliate → MLB. **POPULATION MATCH, but the task is a non-competitive bullpen aiming at one location at submaximal intent.** Command = **average miss distance in inches** (Intended Zone Tracker + TrackMan Mobile). Kinematics at **PKH, FP, MER, BR**.

**Reference value supplied: MLB average fastballs miss their intended spot by roughly 11 inches** (intent via InsideEdge).

**Results as actually reported:**
- Multiple features with |Pearson r| > 0.5 on raw SD; **glove-shoulder abduction at FP** and **torso lateral tilt at FP** significant (repeatability helping).
- Predominantly **negative** correlations elsewhere — *more* variability associated with *better* command — concentrated in **angular velocities at peak knee height.**
- **"Dampening scores"** — SD at an earlier chain point ÷ SD at a later one. High = **"Funnel In"**; low = **"Funnel Out."** **Dampening scores produced larger correlations than raw SD.**
- **PKH → FP: all significant dampening features negative (|r| ≳ 0.6) → Funnel In is good early.**
- **FP → MER and MER → BR: all significant features positive → Funnel Out is good late.** Variable shoulder horizontal abduction at MER is a "clean-up point"; variable pronation rate into release does the same.
- PCA: 10 components = 80% of variance. **PC3 (adjustability; 14/15 loadings angular velocities at PKH) strongest negative; PC9 (repeatability; features post-PKH) strongest positive** — though PC9's loadings were a "mixed bag."

**⚠️ Honest assessment.** No per-variable correlation table published. No sample miss-distance values published. No ANOVA (authors state n was too small, which is why they pivoted to the SD/dampening analysis). **With n = 27 and many features screened at |r| > 0.5, multiple-comparisons inflation is a real risk.** **[EMERGING, not ESTABLISHED. Watch for a follow-up with a held-out sample.]**

**Why I still take it seriously:** it is corroborated from two independent directions — Bloebaum's segment-staggered convergence is literally a funnel-in-then-out pattern at n = 2,052, and §8.4 is the behavioral version.

### 8.4 Corrective capacity — the best adjustability evidence in the peer-reviewed literature

**Kusafuka, Okegawa, Yamamoto, Miyata & Kudo (2025), *Scientific Reports* 15:12300, doi 10.1038/s41598-025-97146-5 (PMID 40210939).**

n = 14 skilled pitchers, top-level Japanese university league, **velocity 30.84 ± 2.61 m/s ≈ 69 mph — `[SAMPLE MISMATCH]`**. 30 four-seams each, 960 fps cameras, DeepLabCut. Autocorrelation + a novel transition-probability analysis on inter-trial changes in release angle.

- Maximum SDs: **elevation 1.81°, azimuth 2.81°** → via §5, ~54 cm and ~84 cm of 1-SD scatter.
- **Elevation:** no relation between lag-1 ACF and SD (r = −0.18, p = .46). **Vertical correction is near-optimal in all skilled throwers.**
- **Azimuth:** ⚠️ **LABELS CORRECTED 2026-08-13 — the two headline numbers were mis-described. The direction of the claim survives; the labels did not.**
  - **r = 0.54, p = .02 is NOT an autocorrelation value.** It is the **correlation between each pitcher's lag-1 autocorrelation coefficient (ACF1) and the SD of his azimuth release angle.** The elevation equivalent was null (**r = −0.18, p = .46**).
  - **r = 0.73, p < .01 is NOT a "staying-in-the-same-state" correlation.** It is the **correlation between the "No"-correction transition probability and the SD of azimuth release angle.**
  - Friedman χ² = 25.79, df = 15, p = .04.
  - *Sample: n = 14 × 30 balls. Do not restate these as autocorrelations or as state probabilities — they are correlations BETWEEN a per-pitcher correction statistic AND that pitcher's azimuth variability.*

> **Pitchers with poor horizontal command are the ones who fail to correct trial-to-trial in the horizontal direction.** A positive lag-1 autocorrelation means the error persists — he missed arm-side, missed arm-side again, and did not adjust.

**Genuinely new and directly coachable. [EMERGING — n = 14 × 30 balls, sub-elite velocity, bullpen task — but the correction-to-variability association is a large effect and the mechanism is clean.]** ✅ *Citation and both coefficients re-verified against PMID 40210939, 2026-08-13.*

**Translation: command training that only counts hits and misses trains the wrong thing. What separates command is the correction after the miss, and specifically the horizontal correction.** See §11.2.

### 8.5 Reconciling the apparent conflict

Bloebaum: the trunk carries only ~5% of release-preserving variance; the proximal base is *stable*. Manzi and Driveline: trunk/hip at foot contact is the top command predictor. **These are not the same claim and must never be quoted as if they were.**

- Bloebaum decomposes within-delivery variance *about the release point*, with velocity as the outcome.
- Manzi and Driveline predict *between-pitcher* command from trunk *posture* and posture variability at foot contact.

A stable proximal base is exactly what lets the arm chain do the release-preserving covariation. **Get the trunk to the same place at foot plant, then let the arm negotiate.** Same sentence, three datasets.

---

## 9. Measuring Command

### 9.1 The intended-target problem

**(a) Glove tagging / COMMANDf/x.** Baseball Prospectus explicitly calls glove-based intent inference *"flawed"*; Driveline calls manual tagging unreliable and labor-intensive. The glove moves pre-pitch, the target may be a zone rather than a point, framing motion contaminates the frame. **Deprecated.**

**(b) BP Command / CSAA** (Pavlidis & Judge, *"Prospectus Feature: Command and Control"*). Called strikes above average on **taken pitches only**, from a mixed model controlling pitcher, catcher, batter, umpire, and location. **Sidesteps intent entirely** by inferring command from outcome. 2016 leaders (min. 500 chances): Zach Davies 3.5%, Josh Tomlin 2.8%, Kyle Hendricks 2.5%, Zack Greinke 2.1%. Jered Weaver's decline: 2.1% (2014) → 0.6% (2016), WARP 0.4 → −5.3. **⚠️ BP never published formal stabilization figures** — in the comments Pavlidis offered only *"a couple weeks of games is a reasonable rule of thumb, but we should dig out the proper values."* **Label any CSAA stability claim UNVERIFIED.**

**(c) Location+ / PitchingBot Command.** Location+ is explicit: *"Location+ only looks at actual locations and implicitly assumes the intent is generally the same across the league in certain counts with certain pitches."* Defensible modeling choice, real limitation — **it cannot distinguish a missed spot from an executed pitcher's pitch.**

**(d) xCTRL — Ludwig, Brill & Wyner (2025), arXiv:2508.19184** (Wharton Sports Analytics). The best current public work on intent. Fit a **Gaussian mixture model via EM** to each pitcher's historical location tendencies (K discrete targets, ≥250 pitches/bin); for each pitch, **Bayesian-update** the posterior over which target he was aiming at given the realized location; xCTRL = posterior-weighted execution distance. Statcast 2008–2023 (primary 2021–2023), 23,831 fastball at-bats for validation, 118 pitcher-seasons.

- **Elite control pitchers average ~7.05 in miss distance** (the exemplar is **Kevin Gausman**); the worst exceed 10 in.
- **One inch of fastball xCTRL improvement ≈ 0.3 FIP**; elite fastball control ≈ **+36 IP/season.** Inter-season correlation **0.65.**
- ✅ **VERIFIED CLEAN 2026-08-13 (arXiv:2508.19184). Do not re-check.**
- **Correlation with Location+ is only r = −0.46.** They disagree meaningfully — Kevin Gausman is top-2 by xCTRL since 2021 but 13th by 2023 Location+.

**[EMERGING — preprint.]**

Also exists: **Command+** (Sarris / STATS, 2018), modeling intent as selection from **13 target zones** incorporating catcher glove placement. Proprietary; Ludwig et al. note discretization limits precision. **[EMERGING, proprietary.]**

### 9.2 The reliability gap — and why it may be an artifact

| Metric | Within-season stabilization | Year-over-year |
|---|---|---|
| **Stuff+** | **~80 pitches** | r ≈ 0.73 |
| **Location+** | **~400 pitches** (Cronbach's α ≈ 0.9) | R² = 0.39; r ≈ 0.48 |
| Pitching+ | ~250 (RP) / ~400 (SP) | — |
| tjStuff+ v2 | ~220 pitches (~3 starts) | R² = 0.78 (2022→23) |
| Kirby Index | 1–2 starts for stable vertical release angle | R² = 0.50 (2022→23) |
| **xCTRL (fastball)** | — | **r = 0.65** (53 pitcher-season pairs) |

**The 5× stabilization gap between Stuff+ (80) and Location+ (400) is the empirical core of "stuff is easy, command is noisy." [ESTABLISHED.]**

**But look at the last row.** The intent-aware metric sits at r = 0.65 — much nearer Stuff+ (0.73) than Location+ (0.48).

> **Much of the historic "command is unstable / command is luck" finding is plausibly a measurement artifact of ignoring intent, not a fact about pitchers.** **[EMERGING, and if it holds it is one of the more consequential ideas in this document.]**

### 9.3 The convergence worth trusting

Three independent methods land on the same number for how far an MLB fastball misses:

| Source | Method | Value |
|---|---|---|
| §5 physics (Kusafuka 2020) | Release-angle SD × 30 cm/° | ~13 in |
| Driveline (Feb 2026) | Intended Zone Tracker + InsideEdge | **~11 in** |
| xCTRL (Ludwig et al. 2025) | Bayesian intent inference, Statcast | **7 in elite, 10+ in poor** |

**[ESTABLISHED, order-of-magnitude.]**

**Athlete-facing anchor:** *"The best command in the major leagues misses by about 7 inches. The average major leaguer misses by about a foot. If you think you're hitting the glove, you're not — and neither is anybody else."*

**For a training environment:** declared-target-before-the-pitch is the only approach that *solves* rather than infers the intent problem. Driveline's Intended Zone Tracker is one implementation; **it does not require their hardware — it requires discipline.** The cost is ecological validity: a bullpen is not a game, and "middle-middle at 90%" is not a game task.

---

## 10. Motor Learning and Skill Acquisition — the reckoning

**Scope warning that governs this entire section.** Almost the entire experimental motor-learning literature uses **novices on lab tasks** (dart throwing, golf putting, key-pressing, balance boards) with **20–60 total participants and 1–3 sessions.** An elite 85+ mph pitcher is the extreme opposite: 10–20 years of deliberate practice on a ballistic, high-force, open-loop task with a ~150 ms execution window. **Almost nothing below was tested on that population.**

**And this field has had a genuine replication reckoning.** Median sample sizes are ~15/group, giving **~20–30% power** for realistic effects. When robust publication-bias models are applied, headline effects repeatedly collapse toward zero. **Several things baseball coaching education teaches as settled science are, as of the current evidence, falsified or unsupported.** This section says so.

### 10.1 The one methodological point that matters more than all the rest

**Performance during practice is not learning.** Conditions that raise in-session performance frequently *lower* retention and transfer, and vice versa. Canonical modern synthesis: **Soderstrom & Bjork (2015), *Perspectives on Psychological Science* 10:176–199** — repeated dissociations between acquisition curves and delayed retention/transfer across motor and verbal domains. **[ESTABLISHED — the single most defensible finding in the field.]**

Learning is only visible on (a) a **delayed test** (≥24 h, ideally days), (b) under **changed conditions** (transfer), (c) **without the feedback or support present in practice.**

> **A bullpen where a pitcher hits 80% of his targets tells you almost nothing about whether he learned anything.** Any command program evaluated by within-session hit rate is measuring the wrong variable. **This is the most common methodological error in applied baseball**, and §11.4 is its arithmetic consequence.

### 10.2 External vs. internal focus of attention

**The claim.** Wulf's **constrained action hypothesis**: internal focus (on body parts) invokes conscious control that disrupts automatic processes; external focus (on the movement's effect) promotes automaticity. Extended in **Wulf & Lewthwaite (2016), *Psychonomic Bulletin & Review* 23:1382–1414** into **OPTIMAL theory**, adding **enhanced expectancies** (EE) and **autonomy support** (AS).

**The pro-EF meta-analysis everyone quotes.** Chua, Jiménez-Díaz, Lewthwaite, Kim & Wulf (2021), *Psychological Bulletin* 147(6):618–645: 143 studies; performance **g ≈ 0.26** (73 studies, N = 1,824); retention **g ≈ 0.58** (40 studies, N = 1,274).

**The critique — and it is devastating.**
**McKay, Corson, Seedu, De Faveri, Hasan, Arnold, Adams & Carter (2024), *Psychological Bulletin* 150(11):1347–1362 (PMID 39480294).** Re-analyzed the data from **seven prior EF meta-studies** (including Chua et al.) using **robust Bayesian meta-analysis with multiple publication-bias models:**

- **Moderate-to-strong evidence of publication bias in every analysis.**
- Bias-corrected means: **g = 0.01 (performance), 0.15 (retention), 0.09 (transfer), 0.06 (EMG), −0.01 (the "farther is better" distance effect).**
- **Bayes factors favored the NULL in every analysis** (BF01 = 1.3 to 5.75).
- Large residual heterogeneity — focus effects exist but depend on unknown moderators.

> **External focus is the *best-supported* of Wulf's claims and it still is not clean.** Honest label: **EMERGING/CONTESTED, not ESTABLISHED.** The direction is plausibly positive; the bias-corrected magnitude is near-trivial (g ≈ 0.1). **The "more distal is better" rule is FOLKLORE (g = −0.01).**

**For pitching:** external cues ("drive the ball through the glove," "finish to the target") are a **low-cost default with weak average benefit**, and **individual response should be measured, not assumed.** Elite pitchers frequently self-report internal cues that work for them; **the data do not license overriding that.**

**The motivational pillars of OPTIMAL theory are essentially unsupported. [FOLKLORE as applied.]**

| Claim | Evidence |
|---|---|
| **Self-controlled practice** | McKay, Yantha, Hussien, Carter & Ste-Marie (2022), *Meta-Psychology* 6: k = 52, N = 2,061. Naïve **g = 0.44** [0.31, 0.56] → after correcting for selective reporting, **g = 0.107** [0.047, 0.18]. Published studies showed benefits; unpublished did not. p-curve indicated inadequate evidential value. Authors: **"not currently distinguishable from zero."** |
| **Enhanced expectancies + autonomy support** | McKay, Bacelar, Parma, Miller & Carter (2023), *IRSEP* 18:242–262: reporting bias plus underpowered designs **"substantially exaggerated"** both. (Secondary reporting gives bias-corrected EE d ≈ 0.26 [−0.07, 0.63] and AS d ≈ 0.034 — **PARTIALLY VERIFIED**, paywalled; the qualitative conclusion is verified.) |
| **The mechanism was never tested** | Parma, Miller & Bacelar (2024), *Psychology of Sport and Exercise* 74:102690: of **166 experiments** testing OPTIMAL predictions, only **21% (n = 35) measured motivation at all**; of those, ~23% showed group-level motivational effects; of those 8, only 5 also showed learning benefits. **The theory's causal mechanism is essentially unevidenced.** |
| **Direct high-powered failures** | McKay & Ste-Marie (2020), *Hum Mov Sci* 71:102612 — AS and reduced feedback frequency had *trivial* effects on golf putting. McKay & Ste-Marie (2022), *RQES* 93:64–76 — irrelevant-choice AS: no benefit. Yantha et al. (2022), *J Sports Sci* 40:769–782 and St. Germain et al. (2023), *Psychon Bull Rev* 30:621–633 — learner-controlled feedback schedules not advantageous. St. Germain et al. (2024), *Psychol Res* 89(1):26 — autonomy-supportive instructional language did not beat controlling language. |

> **Giving pitchers choices and telling them they're doing great may be good coaching for adherence and rapport. There is no credible evidence it accelerates motor learning.** Do not build a program around it and do not claim a learning mechanism.

**A verified, awkward, directly relevant field finding.** *"Focus of attention instructions during baseball pitching training,"* **International Journal of Sports Science & Coaching (2018), TU Delft.** Six coaches, **70 elite youth pitchers (mean 15.3 yr — `[SAMPLE MISMATCH]`)**, four weeks, **1,699 recorded instructional statements.** Of the 717 that induced a specific focus, **only 224 (31%) were external.** And on questionnaire, **the pitchers reported using an internal focus and preferring to receive internal instruction.**

**Two takeaways.** Coaches cue internally roughly 2:1 against the (weak) evidence. And **athletes prefer the cues that work less well** — an external-focus conversion is a change the athlete will initially dislike. Plan for that.

### 10.3 Contextual interference (blocked vs. random)

**Origin:** Shea & Morgan (1979), *JEP: HLM* 5:179–187. Lab barrier-knockdown task, novices. **`[SAMPLE MISMATCH]`**

**Meta-analytic history:**

| Source | Finding |
|---|---|
| Brady (2004), *Percept Mot Skills* 99:116–126 | 61 studies, 139 ES, mean ≈ 0.38. Pools fine lab and gross sport skills; no baseline-equivalence requirement. **Weak by current standards.** |
| **Czyż, Wójcik, Solarská & Kiper (2024), *Scientific Reports* 14:15974** | 54 studies, 2,068 participants, 194 ES. Overall retention **SMD = 0.63** [0.33, 0.93] (0.43 after outlier removal). **By setting: laboratory SMD = 0.92** [0.48, 1.36] vs **applied/field SMD = 0.23 [−0.16, 0.62], p = 0.24 — negligible and non-significant.** By age: young (<18) SMD = 0.02, null; adults 0.63; older adults 1.45. I² = 88–90%; **no formal publication-bias test reported.** |
| **Ammar, Trabelsi, Boujelbane, Boukhris, Glenn, Chtourou & Schöllhorn (2023), "The myth of contextual interference learning benefit in sports practice," *Educational Research Review* 39:100537** | **No CI benefit in sports settings at acquisition, retention, or transfer.** |
| Ammar et al. (2024), *Educational Psychology Review* | Multilevel meta-analysis: of 183 pooled outcomes, **only ~20% agreed with the paradoxical CI pattern.** |
| Farrow & Buszard (2017), *Prog Brain Res* 234:69–83 | Effect appears mainly in simple/moderately complex **closed** skills; applied evidence far weaker. |
| Buszard, Reid, Krause, Kovalchik & Farrow (2017), *Front Psychol* 8:1931 | Skilled youth tennis, **n = 8/group**, 10 sessions/7 weeks. Moderate CI improved the *transfer* (match-play) test more; low CI improved the *closed skill* test more. |

**There is a live published methodological exchange** (Czyż 2025 commentary; Ammar et al. 2025 reply). **The debate is not settled.**

**The famous baseball study — verified, and it is small.**
**Hall, Domingues & Cavazos (1994), "Contextual interference effects with skilled baseball players," *Perceptual and Motor Skills* 78(3 Pt 1):835–841 (PMID 8084699).** **30 collegiate players, n = 10 per group** (random, blocked, no-extra-practice control). 12 extra BP sessions over 6 weeks, 45 pitches each (15 FB / 15 CB / 15 CH). Pretest→random-transfer improvement: **random +56.7%, blocked +24.8%, control +6.2%.**

> **⚠️ This is the most-cited applied CI study in baseball and it is n = 10 per cell, one team, one coach, unblinded, no delayed retention beyond the 6-week endpoint, and no effect sizes reported.** A +56.7% vs +24.8% split on n = 10 is exactly the profile of a result that would not survive replication. **It is a hitting study being generalized to pitching** — a different task class (self-paced, no reactive component). **Cite it as suggestive, never as evidential.**

> **Verdict: CI in lab/novices = ESTABLISHED (SMD ≈ 0.92). CI in applied sport settings with skilled performers = NOT SUPPORTED (SMD 0.23, ns).** The CI effect is **least** well-supported precisely in the population this program serves.

**What survives, in a narrower form:** *practicing pitch-to-pitch variation the way it occurs in competition improves transfer to competition* — which is really the **specificity/representative-design argument (§10.6)**, not the CI-elaboration argument.

**Practical staging, honestly labeled:** blocked reps are defensible when *acquiring* a new pitch or movement pattern (goal: a stable movement solution); randomized sequencing is defensible in the *game-execution* phase. **This staging has not been tested in pitchers. [FOLKLORE-with-plausible-rationale.]**

### 10.4 Variable practice and differential learning

**Schema theory** (Schmidt, 1975, *Psychological Review* 82:225–260) predicted variable practice builds generalized motor programs with better parameter rules. **The theory is largely abandoned in its original form**; the empirical variability-of-practice effect is inconsistent and heavily confounded with CI. **[Theory FOLKLORE; effect EMERGING/inconsistent.]**

**Differential Learning (Schöllhorn)** — deliberately adding movement noise, never repeating the same movement, no corrections, no target pattern.

**Best evidence: Tassignon et al. (2021), *Frontiers in Psychology* 12:533033.** 27 articles / 31 experiments, **N = 897** (DL 453, control 446). Acquisition **d = 0.26** [0.10, 0.42]; retention **d = 0.61** [0.30, 0.91]; sport-technical retention d = 0.63 [0.34, 0.91].

**But:** **high risk of bias, I² = 77–79%, substantial publication-bias concerns, most studies from a single research group (the originator's), low power throughout.** **The authors themselves state that inferences about DL effectiveness "would be premature."** Independent critiques argue DL's claimed mechanisms are neither theoretically nor empirically founded, and that structured variation *with* corrections — which contradicts DL's core premise — outperforms DL protocols.

> **Verdict: DL = EMERGING with a serious single-lab/allegiance problem.** Effect sizes are exactly the magnitude that bias correction has repeatedly reduced to zero elsewhere in this literature. **"Differential learning improves pitching command" is FOLKLORE — no direct evidence in pitchers exists.** Given how aggressively DL is marketed in baseball (weighted and odd-shaped implements, constraint drills sold as DL), that gap should be stated plainly.

### 10.5 Constraints-led approach / ecological dynamics

Newell's constraints model (organism–task–environment, 1986) and the Davids/Renshaw/Araújo program are **frameworks, not interventions.** A framework can be conceptually productive and simultaneously have almost no direct RCT support. That is the current state.

**Best available evidence: Bromilow, Milne, Woods, Dowsett & Keogh (2025), *Sports Medicine – Open* 11:90.** Nine studies, youth→elite, **78% soccer**, ages 9–27, mean 15.8 ± 6.6 sessions.
- **Technical outcomes: 66% showed NO difference; 34% favored nonlinear.**
- Tactical outcomes: after removing high-bias studies, 66% favored nonlinear (decision-making, game sense).
- **Risk of bias: all six RCTs "some concerns" under RoB 2; two non-randomized studies "serious risk." Heterogeneity prevented meta-analysis.**

> **CLA is a framework with modest, biased, mostly team-sport, mostly *tactical*-outcome support. It is not an evidence-based intervention in the sense a clinician would mean.**

**For pitching specifically: zero RCTs.** And note the mismatch — pitching command is largely a **closed, self-paced** skill, while the tactical/decision-making outcomes where CLA looks best are the outcomes **least relevant to raw command** (they matter for sequencing and pitch selection, not location precision). **Constraint manipulation for pitchers is defensible-by-analogy, not evidenced.**

**Its real practical virtue** is that it disciplines the coach into changing the **environment** rather than adding another verbal cue — which is separately (weakly) supported by the external-focus literature. Crider's Driveline heuristics (`coaching-translation.md` §7) remain the best applied version.

### 10.6 Feedback: the guidance hypothesis is falsified

**The claim** (Salmoni, Schmidt & Walter, 1984, *Psychological Bulletin* 95:355–386): frequent KR guides performance during practice but creates dependency and degrades learning; therefore **reduce, fade, bandwidth, or summarize** feedback. **This is the most widely taught applied principle in coaching education.**

**It does not hold up.**
**McKay, Hussien, Vinh, Mir-Orefice, Brooks & Ste-Marie — meta-analysis of reduced relative feedback frequency, *Psychology of Sport and Exercise* (2022). 61 eligible papers, k = 75, N = 2,228.**
- **No significant effect of reduced feedback frequency at any time point.**
- **No significant moderators** — frequency, amount of practice, bandwidth vs. faded vs. yoked schedule all non-significant.
- **No significant change in effect from acquisition/immediate retention to delayed retention** — i.e. **the signature dissociation the guidance hypothesis predicts was absent.**
- Authors: **"The guidance hypothesis is not supported by the extant research."**

Self-controlled feedback (§10.2): g drops 0.44 → 0.107 after bias correction; direct high-powered tests null.

> **Verdict: guidance hypothesis = FOLKLORE (unsupported). Faded feedback, bandwidth KR, and self-controlled feedback as *learning accelerators* = FOLKLORE.**

**⚠️ This corrects a recommendation I would otherwise have made, and it cuts both ways.** The fashionable advice to withhold Trackman/Rapsodo data from pitchers to "avoid dependency" **has no empirical support.** Neither does the opposite claim that more data is better.

**The defensible position is agnostic:** feedback *frequency* is not a major learning lever. What matters is **feedback content and validity** — does the metric actually index command? — and whether **testing** is done without feedback. **Run no-feedback retention testing for measurement reasons (§10.1), not for guidance-hypothesis reasons.**

### 10.7 Transfer: what actually gets from the pen to the game

**Specificity of practice** (Proteau tradition): learners become tuned to the specific sensory/informational conditions of practice; changing those conditions degrades performance. **[ESTABLISHED in lab aiming tasks.]**

**Representative learning design** — Pinder, Davids, Renshaw & Araújo (2011), *JSEP* 33:146–155. The argument is about **action fidelity**: practice must preserve the information–movement couplings that exist in competition. **[EMERGING — strong conceptual grounding, weak direct experimental verification.]**

> **⚠️ Bullpen-to-game transfer in baseball: essentially no direct evidence exists. I found no peer-reviewed intervention study testing whether a bullpen-design manipulation improves in-game command. This is a genuine, glaring gap, and it should be stated rather than papered over with coaching-blog content.**

**What does exist is biomechanical evidence that bullpen ≠ game**, which supports the specificity argument indirectly: Lerch, Fleisig, Slowik & Oliver (2025), *J Biomech* 188:112775 (already in `biomechanics.md` §7.2), plus multiple reports that pitchers throw meaningfully slower in lab/no-batter conditions and that kinematics differ with a batter present and on mound vs. flat ground. *(A frequently cited "Differences between bullpen and game baseball pitching biomechanics" appears on ResearchGate only — no verifiable peer-reviewed journal version found. **UNVERIFIED — do not cite.**)*

**The defensible claim, stated precisely:** *"Representative bullpen design is theoretically indicated and biomechanically motivated; its transfer benefit in pitchers is untested."*

**Measurement corollary:** since acquisition ≠ learning, evaluation of any command intervention must use **in-game command metrics across a subsequent window**, not bullpen hit rates. **A program that cannot produce that measurement cannot know whether it works.**

### 10.8 The speed–accuracy question — a verified, counterintuitive finding

**Urbin, M.A., Stodden, D.F., Boros, R. & Shannon, D. (2012), "Examining impulse-variability in overarm throwing," *Motor Control* 16(1):19–30 (PMID 22402218).**
n = 30 (16 skilled, 14 unskilled), tennis ball, target at 30 ft, seven percentages of maximum velocity (40–100%) in random order, 9 trials per condition. **`[SAMPLE MISMATCH — tennis ball, mixed skill, short distance.]`**

1. Throwing-velocity variability rose from 40%, **peaked at 60%**, then **decreased at every higher interval** — supporting the inverted-U from impulse-variability theory.
2. **Spatial error showed no significant relationship with speed across the entire 40–100% range. The Fitts'-Law speed–accuracy trade-off was NOT supported for overarm throwing.**

A children's replication (*Motor Control* 2018, PMID 28657818) **failed to find the inverted-U**, so part 1 is contested. **Part 2 — the absence of a speed–accuracy trade-off — is the more robust half.**

> **"Take a little off and throw a strike" is not supported.** Spatial error does not systematically worsen with speed in overarm throwing — and force-output variability is *highest* around 60% of maximum, which is exactly where "take something off" lands the athlete.

This dovetails with the library's effort-level findings (`coaching-translation.md` §4): perceived effort is a badly calibrated instrument, and a pitcher who believes he is at 60% is often at 86% of velocity. **Submaximal command work may be simultaneously the least accurate and the least specific thing in the program.** **[EMERGING.]** Driveline's own protocol independently arrived at the same rule: **RPE minimum 70%, preferably higher.**

### 10.9 Dosage — reps, spacing, sleep

**Distributed > massed at the level of SESSIONS. [EMERGING/ESTABLISHED cross-domain.]**
- Donovan & Radosevich (1999), *J Applied Psychology* 84:795–805 — meta-analysis; the effect is strongly moderated by task type and interstudy interval ("now you see it, now you don't"). **Larger spacing advantages for simpler tasks; smaller or reversed for complex ones.**
- Lee & Genovese (1988), *RQES* 59:277–287 — distributed practice benefits *performance* more than *learning*. The §10.1 dissociation again.
- **Spruit, Band & Hamming (2015), *Surgical Endoscopy* 29:2235–2243** — laparoscopic training, 3×75 min in one day vs 1×75 min/week for 3 weeks. **Spaced better at end of training, at 2-week retention, and at 1-year retention; 65% of the spaced group vs 21% of massed reached proficiency.** Complex real-world motor skill, adult learners — **the closest analogue to a dosage RCT available.** Still `[SAMPLE MISMATCH — novice surgeons]`.
- **Counter-evidence at short intervals:** Dutra et al. (2026), *QJEP* 79(4):896–904 found 2-s inter-trial intervals beat 30-s for a serial key-press task. **Inter-trial spacing and inter-session spacing are different phenomena. Do not conflate them.**

**Practical inference (weak-to-moderate confidence): spreading a fixed volume of command work across more, shorter sessions per week is better supported than consolidating it into fewer long bullpens.** This also aligns with arm-health constraints. **[EMERGING — cross-domain extrapolation.]**

**Sleep.** Schmid, Erlacher, Klostermann, Kredel & Hossner (2020), *Neurosci Biobehav Rev* 118:270–281: 48 studies, 53 sleep groups (n = 829) vs 53 wake groups (n = 825). Overall relative sleep gain **g = 0.43**; finger tapping 0.47; mirror tracing 0.62.
**⚠️ The caveat matters enormously: the effect is largely demonstrated on *explicit motor sequence* tasks, not continuous/ballistic whole-body skills.** Generalizing "sleep consolidates your bullpen" to a pitching delivery is **unwarranted extrapolation.** **[ESTABLISHED for sequence tasks; UNVERIFIED for ballistic sport skills.]** Advocate sleep on other grounds — those arguments are stronger.

**Reps per session: no direct evidence exists for pitching command.** There is **no dose-response curve** in the literature for throwing-accuracy practice volume. **Anyone quoting an optimal number of command reps is extrapolating. [FOLKLORE.]**

**On dart/free-throw studies:** the literature is dominated by small single-session attentional-focus and quiet-eye studies on novices with **no retention tests** (e.g. Asadi et al. 2022, *Hum Mov Sci* 86:103015, n = 18; Hitchcock & Sherwood 2018, *Int J Exerc Sci* 11:1120–1135, n = 24). **Mechanistic hints only. Never programming guidance for pitchers.**

---

## 11. Training Command Deliberately

### 11.1 The published protocol — and what it lacks

**Driveline, "Implementing Command Training Into Team Practice" (Sept 2018)** — the most complete publicly documented command program:

- **Implements:** overload 6 oz / regulation 5 oz / underload 4 oz leather balls, **alternated within a session**, usable on mound or flat ground.
- **Not fastball-only** — secondary pitches trained for command too, ball weight customized to the specific pitch/location he struggles with.
- **Metrics:** strike %, location accuracy vs. intended target, **RPE minimum 70% and preferably higher**, radar for velocity monitoring.
- **Gamification:** competitive scoring sheets tracking strikes and categorizing misses — which the authors report *"solved the problem of effort and focus almost immediately."*
- **Progression:** 50 ft → regulation; flat ground → mound; increasing RPE; then contextual distraction (hitters, hecklers, noise, unrelated tasks).

**⚠️ The article publishes zero quantified outcomes.** No pre/post, no retention test, no control condition. **[UNPROVEN as a protocol.** Well-reasoned and built on defensible principles — which is not the same as effective.]

### 11.2 What I would actually program

Each element traced to its source. **All of this is [EMERGING] — synthesis, not a validated program.**

**1. Declare the target before every pitch.** Without declared intent you are measuring outcome, not command (§9.1). Free, and the highest-value change available.

**2. Score miss distance in inches, not strikes.** Ball/strike is a binary that discards almost all the information. Miss distance is continuous and is the quantity the whole literature is denominated in (§9.3).

**3. Score the *sign* of the miss, especially the horizontal sign.** Kusafuka 2025 (§8.4): what separates command is **horizontal corrective capacity** — the pitchers who fail to correct are the ones with the widest azimuth scatter (**"No"-correction transition probability vs SD of azimuth release angle, r = 0.73, p < .01**). **Two consecutive same-direction horizontal misses is the actionable event** — a failure to correct is a different problem from scatter and needs a different response.

**4. Have him call his own miss before he sees the number.** This converts the device from a feedback source into a **calibration test**, which builds the internal model. **Track his calling accuracy separately** — I would expect it to predict improvement better than his miss distance does.
*(Note: I am NOT justifying this via the guidance hypothesis, which is falsified — §10.6. The justification is measurement: you need a no-feedback probe to see learning.)*

**5. Feedback frequency: don't overthink it.** §10.6 found **no effect** of reduced feedback frequency at any time point across k = 75, N = 2,228. **Both "screen on every pitch" and "hide the numbers" are unsupported.** Spend the attention on whether the metric is valid instead.

**6. Train at RPE ≥ 70%, and radar-gate it.** No speed–accuracy trade-off exists in overarm throwing (§10.8); force variability is *worst* near 60% of max; perceived effort is badly calibrated. **Submaximal command work is the least specific and possibly the least accurate condition available.**

**7. Attack release-speed variability as a command variable.** ~3.5 in of vertical miss per 1 mph (§5.1). **This costs nothing — you already have the radar readings.** Compute the SD of his fastball velocity within an outing and treat it as a command metric. **I have never heard this coached.**

**8. Variable-tempo bullpens converging to one foot-plant position.** Trains the funnel-in/funnel-out structure (§8.3) and the repeatability-at-FP finding (§7.2). Five pitches: slow lift, fast lift, no lift, slide-step, exaggerated drift — all required to arrive at the same front-foot position and trunk angle at FC. Already in `coaching-translation.md` §6; §7.2 and §8 strengthen it considerably.

**9. Random/interleaved pitch selection — default it, don't oversell it.** The CI effect is **null in applied field settings with skilled performers** (SMD 0.23, ns — §10.3). Random is a sensible default. It is not a proven intervention for this population.

**10. Differential/varied implements — use, but label honestly.** Alternating ball weights within a session has a plausible rationale and is Driveline's protocol. **The evidence that it improves command is absent, and the differential-learning literature has a single-lab bias problem (§10.4).**

**11. Representative design — add the hitter EARLY, not last.** Driveline's progression adds distraction at the end. Given how little transfer evidence exists (§10.7), I would add a live hitter much sooner and treat the sanitized pen as the special case rather than the default.

**12. Spread the volume.** More, shorter command sessions per week beats fewer long ones (§10.9), on cross-domain evidence and on arm-health grounds.

### 11.3 What to measure

| Metric | Why | Frequency |
|---|---|---|
| **Miss distance (in), by pitch type** | The denominator of the whole literature | Every command session |
| **Miss *direction*, horizontal sign** | Kusafuka 2025 — correction is the skill | Every pitch |
| **Consecutive same-direction misses** | Direct index of corrective failure | Every pitch |
| **Self-called miss vs. actual** | Calibration of the internal model | Every session |
| **Within-outing fastball velocity SD (mph)** | ~3.5 in of vertical miss per mph | Every outing |
| **Trunk angle + front-foot position at FC, stacked across varied tempos** | §7.2, §8.3 | Weekly, 240 fps |
| **In-game command metric over a subsequent window** | The only valid transfer test (§10.7) | Per outing |

### 11.4 ⚠️ How long before you can believe a command change

**This should stop most command "wins" from being declared.**

Take a within-pitcher miss-distance SD of ~10 inches (consistent with a ~11-inch mean miss). To detect a **2-inch improvement** at 80% power, α = .05, paired:

`d = 2/10 = 0.2` → `n ≈ (1.96 + 0.84)² / 0.2² ≈ 196 pitches per condition`

**You need roughly 200 tracked command pitches — seven to ten bullpens — before you can claim a 2-inch improvement.** A single 30-pitch bullpen can only detect d ≈ 0.52, i.e. a **~5-inch** change. And per §10.1, **in-session improvement is not learning anyway** — the comparison must be a delayed retention test, ideally in a game.

**Consequences, plainly:**
- **Any command intervention declared successful after one bullpen is noise.** Every one of them.
- **Location+ needing ~400 pitches to stabilize is not a defect of the metric. It is the actual signal-to-noise ratio of command.** The metric is telling the truth; coaches don't want to hear it.
- **This is the whole reason pitch design has commercially outrun command training.** You can prove a spin-axis change in ten pitches. You cannot prove a command change in ten bullpens.

**[ESTABLISHED — standard power analysis on a verified SD.]**

---

## 12. What Is Marketing

| Claim | Verdict |
|---|---|
| **"Spin has diminishing returns because of the lift curve."** | C_L(S) is approximately **linear** above S ≈ 0.15, and **every MLB fastball lives at S ≈ 0.21–0.24.** Misapplying the low-S part of a curve nobody operates in. **FOLKLORE (§2.2).** |
| **"Raise your spin rate."** | Raw spin explains **~4%** of cross-sectional IVB variance (R² = 0.041); observed +0.32 in/100 rpm vs +0.57 theoretical. **The gap is efficiency.** Selling rpm gains is selling the least trainable, least effective term. **MARKETING.** |
| **"Seam-shifted wake lets us add X inches to your sinker."** | The physics is settled and the population effect is real (~17.6° axis deviation on sinkers, +3 in run / +4 in drop). **But the prescriptive coaching pathway is not solved, pitch-to-pitch stability is unknown, and Driveline's own data found ~42% of SSW-affected pitches had LOWER Stuff+.** SSW adds movement; movement is not value. **MARKETING at the service layer.** |
| **"Death ball" changeup branding.** | The pitch is real. The branding, the one-session promise, and the implication that SSW replaces Magnus are **MARKETING.** |
| **"Match your changeup's spin axis to your fastball."** | ⚠️ **REVISED 2026-08-13.** Rosen (FanGraphs, Jun 2025) reports no predictive value for spin-axis similarity — but as **a single unquantified sentence, no coefficient, no n, no method.** Downgrade from FOLKLORE to **UNSUPPORTED-BUT-UNTESTED.** Don't chase it; don't claim it's been disproven. **And note the row below — the old version of this row also mis-stated the velocity finding.** |
| **"Velocity separation doesn't matter on a changeup."** | ⚠️ **THIS IS A REVERSAL OF THE SOURCE AND WAS BRIEFLY IN THIS LIBRARY.** Rosen's main argued chain is **velo gap → hitters out front → whiffs**, and he calls it strong. What has no relationship to whiff rate is **absolute** changeup velocity. **Do not re-import.** See §3.5. |
| **Building an arsenal around the sweeper in 2026.** | RV/100 **−0.94 same-handed vs −0.05 opposite-handed** (worse than an ordinary slider). Whiff% 33.4 → 31.0 → 31.2 (2023–25). Driveline's own model **repriced it downward.** Usage flat-to-down. **The alpha is gone.** |
| **"Tunnel your fastball and slider through a 24-foot window."** | The BP metric suite was **published without any outcome validation.** Independent test: **r = 0.07 with run value.** And nobody can execute a tunnel intentionally at the inch scale. **FOLKLORE as a training target** — train *release consistency* instead. |
| **Optimizing Stuff+ as the objective.** | Scaled within pitch type; excludes location and sequencing; predicts ERA at **r ≈ .14 for team-switchers**; the metric's discriminating power is **compressing ~9% as everyone optimizes to it**; and its rewarded inputs overlap the UCL-surgery gradient. **MARKETING when sold as a development target.** |
| **"Stuff models predict ERA at r² = .99."** | Those are **curve-fits of bucketed group means**, not pitcher-level predictive r². Routinely laundered. **FOLKLORE.** |
| **"Repeat your release point and you'll command the ball."** | Release point moves location ~1 cm per 1 cm against a ~30 cm/° angular term, and **release-point variability does not predict BB/9 in 344 MLB pitchers (R² = 0.011).** **FOLKLORE, now with a published null.** |
| **"Take a little off to throw a strike."** | **No speed–accuracy trade-off found in overarm throwing across 40–100% of max**, and force variability *peaks* near 60%. **FOLKLORE.** |
| **External focus as established science.** | Bias-corrected **g = 0.01 (performance), 0.15 (retention)**; **Bayes factors favor the null** across seven meta-studies. **"Farther is better" is g = −0.01.** Use external cues as a cheap default; **do not claim they are proven.** |
| **Enhanced expectancies / autonomy support / self-controlled practice.** | Self-controlled practice **g 0.44 → 0.107** after bias correction, *"not distinguishable from zero."* **Only 21% of 166 OPTIMAL experiments measured motivation at all.** **FOLKLORE as learning levers.** |
| **Faded / bandwidth / reduced feedback ("guidance hypothesis").** | **k = 75, N = 2,228: no effect at any time point, no significant moderators, no acquisition-to-retention dissociation.** Authors: *"not supported by the extant research."* **FOLKLORE** — and so is the fashionable inverse advice to hide the Rapsodo screen. |
| **Contextual interference as settled science for elite pitchers.** | **Applied/field SMD = 0.23, ns.** The famous baseball study is **n = 10 per group**, on hitters. **Least supported precisely in our population.** |
| **Differential learning for pitching command.** | Single-lab dominance, high risk of bias, I² ≈ 78%; **the meta-analysts themselves call inferences "premature."** **No baseball pitching trial exists.** **FOLKLORE as marketed.** |
| **Constraints-led approach as an evidence-based intervention.** | **66% of technical outcomes showed no difference**; all RCTs carried risk-of-bias concerns; benefits concentrated in *tactical* outcomes, which are the least relevant to location precision. **Framework, not intervention.** |
| **Any command intervention declared a success after one bullpen.** | Underpowered by a factor of ~7. **Noise, every time.** |
| **Any "2026 ASMI consensus statement."** | **FABRICATED.** Content-farm output. |

---

## 13. Corrections Owed to the Library, and Open Questions

### Corrections

1. **`idea-scouting.md` #3 and `coaching-translation.md` §6 both frame Bloebaum's UCM synergy index (ρ = 0.22) as a command finding. It is a VELOCITY finding.** Correct in both files. The paper remains relevant to command as a description of variability *structure*, not as evidence about accuracy.
2. **`coaching-translation.md` §6's cue — "different every time on the way there, same every time when the foot lands" — survives and is now considerably better supported** (§7.2, §8.3, §8.5). Keep it.
3. **A new entry is owed to `open-disputes.md`:** the velocity-predicting delivery (more forward and lateral trunk tilt at release) is the **command-degrading** delivery in a velocity-matched sample of 338 professionals (§7.1). And the **arm-slot square**: higher slot → better command but higher torque; lower slot → better VAA and lower torque but worse command. **Nobody in the library has named either trade.**
4. **`coaching-translation.md` should retire any recommendation built on faded/reduced feedback frequency or on autonomy support.** §10.6 and §10.2 falsify both. The library does not currently lean on them heavily, but the coaching-education default does.

### Open questions

5. **Is there any published bullpen-to-game transfer evidence for command in baseball?** None found. Everything in §11 is reasoned from general principles. **The largest hole in the applied command literature.**
6. **Does within-outing release-speed SD predict vertical command in a large sample?** Physics says ~3.5 in per mph (§5.1). **Trivially computable from any Statcast or Trackman database, and I am not aware of anyone having done it. The cheapest high-value study in this document — a college program could run it this fall.**
7. **Does the Driveline adjustability finding survive a held-out sample?** n = 27 with many screened features at |r| > 0.5 is multiple-comparisons territory (§8.3).
8. **Does the contextual-interference effect hold for expert pitchers on a field task?** An 85+ mph sample has never been tested (§10.3).
9. **Is spin efficiency actually trainable in an elite arm, and by how much?** The entire pitch-design industry assumes yes. **I found no controlled intervention trial. That absence should bother people more than it does.**
10. **Does the Driveline seam-orientation CNN validate against Hawk-Eye?** If yes, cheap seam measurement is a real unlock (§2.3).
11. **Are SSW effects stable pitch-to-pitch for a given pitcher?** Seam orientation at release is a high-variance motor output and nobody has published the within-pitcher variance.
12. **Is there an end-of-2025 league-wide kick-change evaluation?** Statcast does not classify it separately, so public tracking is currently impossible (§3.7).

---

## 14. References

### Physics of flight

- **Nathan AM (2008).** *The effect of spin on the flight of a baseball.* Am J Phys 76(2):119–124. DOI 10.1119/1.2805242. [PDF](https://baseball.physics.illinois.edu/AJPFeb08.pdf)
- **Lyu B, Smith L, Elliott J, Kensrud J (2022).** *The dependence of baseball lift and drag on spin.* Proc IMechE Part P 239:235–241. DOI 10.1177/17543371221113914. [PDF](https://baseball.physics.illinois.edu/LyuDragLiftSpin.pdf)
- **Smith AW & Smith BL (2021).** *Using baseball seams to alter a pitch direction: The seam shifted wake.* Proc IMechE Part P 235(1):21–28. DOI 10.1177/1754337120961609 *(confirmed via Crossref API)*
- **Smith AW (2020).** *Pitched Baseballs and the Seam Shifted Wake.* MS thesis, Utah State University. [DigitalCommons](https://digitalcommons.usu.edu/etd/7903/)
- **Smith BL, Nathan AM, Pavlidis H (5 Nov 2020).** *Not Just About Magnus Anymore.* Baseball Prospectus.
- **Nathan AM.** Papers index: [baseball.physics.illinois.edu](https://baseball.physics.illinois.edu/nathan-papers.html) — incl. *Determining the 3D Spin Axis from Statcast Data* (2020), *The 3D Spin Axis: An Addendum* (2020), *What Is The Hawkeye Spin Data Teaching Us?* I (2021), II (2021), III: *Searching For The Seam-Shifted Wake* (2023).
- **Smith BL.** [baseballaero.com](https://baseballaero.com/) — *Seam-Shifted Wake Timeline* Parts 1–5 (Oct–Nov 2023); Part 3 contains the 8-inch Looper result. Faculty page: [USU](https://engineering.usu.edu/directory/mae/faculty/smith-barton)
- **Driveline (1 Nov 2020).** *An Introduction to Seam-Shifted Wakes and their Effect on Sinkers.* [Driveline](https://www.drivelinebaseball.com/2020/11/more-than-what-it-seams-an-introduction-to-seam-shifted-wakes-and-their-effect-on-sinkers/)
- **Driveline (10 Mar 2021).** *The Impact of Seam-Shifted Wakes on Pitch Quality.* [Driveline](https://www.drivelinebaseball.com/2021/03/the-impact-of-seam-shifted-wakes-on-pitch-quality/)
- **Clemens B (22 Jan 2021).** *The Seam-Shifted Revolution Is Headed for the Mainstream.* FanGraphs.
- **Chamberlain A (7 Jan 2021).** *Where Vertical Approach Angle Seems to Matter Most.* FanGraphs. · **(1 Feb 2022)** *A Visualized Primer on Vertical Approach Angle.* · **(7 May 2025)** *Andrés Muñoz Is an Analytical Blind Spot.*
- **Fink D (24 Jun 2021).** *When 92 Is Actually 95: Bailey Falter's Extension Adds Meaningful Velocity.* FanGraphs.
- **Zahradnik R (26 Oct 2020).** *Fastball Vertical Approach Angle.* Iowa Baseball Managers. n = 2,350 pitchers.

### Pitch design and arsenal

- **Rosen M (17 Jun 2025).** *Changeups Are Weird.* FanGraphs.
- **Rosen M (13 Jun 2024).** *The Kirby Corollary: Why Batters Don't Swing at Sliders.* FanGraphs.
- **Rosen M (3 May 2024).** *Introducing the Kirby Index.* FanGraphs. ~230,000 four-seams.
- **Clemens B (2 Sept 2022).** *The Secret Benefit and Cost of Sweeping Sliders.* FanGraphs — the platoon table.
- **Clemens B (1 May 2025).** *Let's Take a Peek at Some Early 2025 Pitch Usage Trends.* FanGraphs.
- **Driveline (Oct 2021).** *Optimizing Breaking Ball Shape Through Data-Driven Pitch Design, Part II.* · **(Jun 2020)** *How to Throw a Curveball.* · **(Jan 2022)** *Ultimate Guide to Baseball Pitch Grips.*
- **Long J, Judge J, Pavlidis H (25 Jan 2017).** *Prospectus Feature: Introducing Pitch Tunnels.* BP. · **Long, Pavlidis, Alonso (31 Jan 2018)** *Updating Pitch Tunnels.*
- **Roegele J (24 Nov 2014).** *The Effects of Pitch Sequencing.* The Hardball Times.
- **Bryant Z (27 Sept 2024).** *Does Pitch Tunnelling Actually Work?* tdabaseball.com — **r = 0.07.**
- **Augustine M (2020).** *Searching for Pitch Tunneling Benefits.*
- **Sutton-Brown S (17 Jan 2025).** *Introducing New Arsenal Metrics.* BP.
- **Kick-change reporting:** ESPN (2025); Yahoo Sports, Baker & Tracy (9 May 2025); FanGraphs, *Davis Martin and Matt Bowman Break Down the Kick-Change.* *(Baseball America and Lookout Landing both block automated fetching; their reporting is corroborated only through ESPN/Yahoo/FanGraphs — **UNVERIFIED by direct fetch**.)*
- **Addleman G (10 Apr 2026).** *Sweepers vs Sliders.* Self-published; no bimodality test.
- **Johnson B (29 May 2026).** *Mound Musings.* RotoWire — 2026 sweeper usage ~7%.

### Stuff models

- **FanGraphs Library.** *Stuff+, Location+, and Pitching+ Primer.* · *PitchingBot Pitch Modeling Primer.*
- **Andrews D (20 Jan 2026).** *They Don't Make Pitch Models Like They Used To.* FanGraphs. 2,860 pitcher-seasons.
- **Martin J (25 Jun 2026).** *Stuff and Location, Ceiling and Floor.* RotoGraphs.
- **Baseball Prospectus.** *An Updated Evaluation of Hitting and Pitching, Including Stuff Metrics* — the team-switcher table. · *StuffPro / PitchPro.*
- **Nestico T.** tjStuff+ v1/v2/v3 modelling writeups.
- **Lambert J (31 May 2024).** *Revisiting Stuff+.* Driveline.
- **Zimmerman J (5 May 2023).** *Referencing Pitch Quality Models to More Traditional Stats.* RotoGraphs — **the misquoted r² = .996.**
- **Grove C.** [pitchingbot.com](https://pitchingbot.com/)
- **Mastroianni et al. (May 2025).** *AJSM.* 115 UCL cases vs 230 matched controls. [PubMed 40230317](https://pubmed.ncbi.nlm.nih.gov/40230317/)

### Command — peer-reviewed

- **Kusafuka A, Kobayashi H, Miki T, Kuwata M, Kudo K, Nakazawa K, Wakao S (2020).** *Influence of Release Parameters on Pitch Location in Skilled Baseball Pitching.* Front Sports Act Living 2:36. [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2020.00036/full) | [PubMed 33345028](https://pubmed.ncbi.nlm.nih.gov/33345028/) — **the 30 cm/° result.**
- **Kusafuka A, Okegawa T, Yamamoto R, Miyata K, Kudo K (2025).** *Two-dimensional trial-by-trial error correction for accurate baseball pitching.* Sci Rep 15:12300. [PMC11985933](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985933/) | [PubMed 40210939](https://pubmed.ncbi.nlm.nih.gov/40210939/)
- **Wakamiya K, et al. (2024).** *Relationship between ball release point variability and pitching performance in Major League Baseball.* Front Sports Act Living 6:1447665. [Frontiers](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2024.1447665/full) | [PMC11608975](https://pmc.ncbi.nlm.nih.gov/articles/PMC11608975/)
- **Manzi JE, Dowling B, Wang Z, Arzani A, Chen A, Nicholson K, Dines JS (2021).** *Kinematic and kinetic findings in high vs. low consistency professional baseball pitchers.* J Orthop 27:28–33. [PubMed 34475727](https://pubmed.ncbi.nlm.nih.gov/34475727/)
- **Agresta C, Freehill MT, Nakamura B, Guadagnino S, Cain SM (2022).** *Using Sensors for Player Development.* Sensors 22(21):8488. [PMC9655623](https://pmc.ncbi.nlm.nih.gov/articles/PMC9655623/)
- **Scholz JP, Schöner G (1999).** *The uncontrolled manifold concept.* Exp Brain Res 126(3):289–306. [PubMed 10382616](https://pubmed.ncbi.nlm.nih.gov/10382616/)
- *Kinetic and kinematic comparisons in high school pitchers with low and high pitch location consistency.* JSES 31(12), 2022. `[SAMPLE MISMATCH]` [PubMed 35931332](https://pubmed.ncbi.nlm.nih.gov/35931332/)

### Command — preprints and industry

- **Bloebaum A (Driveline).** *Skilled pitching is not less joint variability but better-structured joint variability.* SportRxiv, doi 10.51224/SportRxiv.1010. **⚠️ ρ = 0.22 is a VELOCITY association.** [SportRxiv](https://sportrxiv.org/index.php/server/preprint/view/1010)
- **Ludwig M, Brill RS, Wyner AJ (2025).** *Separating Intent from Execution.* arXiv:2508.19184. [arXiv](https://arxiv.org/abs/2508.19184) | [Wharton](https://wsb.wharton.upenn.edu/introducing-xctrl-a-probabilistic-approach-to-pitch-location-accuracy/)
- **Driveline (Feb 2026).** *The Interaction of Biomechanics and Command.* [Driveline](https://www.drivelinebaseball.com/2026/02/the-interaction-of-biomechanics-and-command/)
- **Driveline (Sept 2018).** *Implementing Command Training Into Team Practice.* · *Command Training and a Closer Look at the Speed-Accuracy Trade-Off.*
- **Pavlidis H, Judge J.** *Prospectus Feature: Command and Control.* BP.
- **Manzi JE, Krichevsky S, Roberts A, Rauck R, Dines JS (2021).** *Kinematic Models For Pitch Location Metrics.* Archives of Sports Medicine. **⚠️ Scholars.Direct — low-profile venue, manual location charting.**

### Motor learning — all verified via PubMed/Crossref/DOI

- **Soderstrom NC, Bjork RA (2015).** *Learning versus performance: An integrative review.* Perspect Psychol Sci 10:176–199.
- **McKay B, Corson AE, Seedu J, De Faveri CS, Hasan H, Arnold K, Adams FC, Carter MJ (2024).** *Reporting bias, not external focus.* Psychol Bull 150(11):1347–1362. [PubMed 39480294](https://pubmed.ncbi.nlm.nih.gov/39480294/)
- **Chua LK, Jiménez-Díaz J, Lewthwaite R, Kim T, Wulf G (2021).** *Superiority of external attentional focus.* Psychol Bull 147(6):618–645. [PubMed 34843301](https://pubmed.ncbi.nlm.nih.gov/34843301/)
- **Wulf G, Lewthwaite R (2016).** *OPTIMAL theory of motor learning.* Psychon Bull Rev 23:1382–1414. DOI 10.3758/s13423-015-0999-9
- **McKay B, Yantha ZD, Hussien J, Carter MJ, Ste-Marie DM (2022).** *Meta-analytic findings of the self-controlled motor learning literature.* Meta-Psychology 6. DOI 10.15626/MP.2021.2803
- **McKay B, Bacelar MFB, Parma JO, Miller MW, Carter MJ (2023).** *The combination of reporting bias and underpowered study designs…* IRSEP 18:242–262. DOI 10.1080/1750984X.2023.2207255
- **Parma JO, Miller MW, Bacelar MFB (2024).** *OPTIMAL theory's claims about motivation lack evidence.* Psychol Sport Exerc 74:102690. [PubMed 38908415](https://pubmed.ncbi.nlm.nih.gov/38908415/)
- **Bacelar MFB, Parma JO, Murrah WM, Miller MW (2022).** *Meta-analyzing enhanced expectancies on motor learning.* IRSEP 17:587–616.
- **McKay B, Ste-Marie DM (2020).** Hum Mov Sci 71:102612. [PubMed 32452429](https://pubmed.ncbi.nlm.nih.gov/32452429/) · **(2022)** RQES 93:64–76. [PubMed 32854605](https://pubmed.ncbi.nlm.nih.gov/32854605/)
- **Yantha ZD, McKay B, Ste-Marie DM (2022).** J Sports Sci 40:769–782. [PubMed 34963413](https://pubmed.ncbi.nlm.nih.gov/34963413/)
- **St. Germain L, McKay B, et al. (2023).** Psychon Bull Rev 30:621–633. [PubMed 36163607](https://pubmed.ncbi.nlm.nih.gov/36163607/) · **(2024)** Psychol Res 89(1):26. [PubMed 39589568](https://pubmed.ncbi.nlm.nih.gov/39589568/)
- **McKay B, Hussien J, Vinh M-A, Mir-Orefice A, Brooks H, Ste-Marie DM (2022).** *Meta-analysis of the reduced relative feedback frequency effect.* Psychol Sport Exerc. Preprint DOI 10.31234/osf.io/v2cp7 — **k = 75, N = 2,228, null.**
- **Salmoni AW, Schmidt RA, Walter CB (1984).** *Knowledge of results and motor learning.* Psychol Bull 95:355–386.
- **Shea JB, Morgan RL (1979).** *Contextual interference effects.* JEP:HLM 5:179–187.
- **Czyż SH, Wójcik AM, Solarská P, Kiper P (2024).** *High contextual interference improves retention in motor learning.* Sci Rep 14:15974. [PubMed 38987617](https://pubmed.ncbi.nlm.nih.gov/38987617/)
- **Ammar A, Trabelsi K, Boujelbane MA, Boukhris O, Glenn JM, Chtourou H, Schöllhorn WI (2023).** *The myth of contextual interference learning benefit in sports practice.* Educ Res Rev 39:100537. · **Ammar et al. (2024)** Educ Psychol Rev, DOI 10.1007/s10648-024-09892-z.
- **Brady F (2004).** *Contextual interference: A meta-analytic study.* Percept Mot Skills 99:116–126.
- **Farrow D, Buszard T (2017).** Prog Brain Res 234:69–83. [PubMed 29031473](https://pubmed.ncbi.nlm.nih.gov/29031473/)
- **Buszard T, Reid M, Krause L, Kovalchik S, Farrow D (2017).** Front Psychol 8:1931.
- **Hall KG, Domingues DA, Cavazos R (1994).** *Contextual interference effects with skilled baseball players.* Percept Mot Skills 78(3 Pt 1):835–841. **n = 10/group.** [PubMed 8084699](https://pubmed.ncbi.nlm.nih.gov/8084699/)
- **Tassignon B, et al. (2021).** *An exploratory meta-analytic review… differential learning.* Front Psychol 12:533033. [PMC8138164](https://pmc.ncbi.nlm.nih.gov/articles/PMC8138164/)
- **Schmidt RA (1975).** *A schema theory of discrete motor skill learning.* Psychol Rev 82:225–260.
- **Newell KM (1986).** *Constraints on the development of coordination.*
- **Bromilow L, Milne N, Woods CT, Dowsett CK, Keogh JWL (2025).** *The effectiveness of linear and nonlinear pedagogical approaches in team-invasion ball sports.* Sports Med Open 11:90. DOI 10.1186/s40798-025-00893-y
- **Pinder RA, Davids K, Renshaw I, Araújo D (2011).** *Representative learning design.* JSEP 33:146–155.
- **Urbin MA, Stodden DF, Boros R, Shannon D (2012).** *Examining impulse-variability in overarm throwing.* Motor Control 16(1):19–30. `[SAMPLE MISMATCH]` [PubMed 22402218](https://pubmed.ncbi.nlm.nih.gov/22402218/)
- *Examining Impulse-Variability Theory… in Children's Overarm Throwing.* Motor Control (2018). `[OFF-POPULATION]` [PubMed 28657818](https://pubmed.ncbi.nlm.nih.gov/28657818/)
- *Focus of attention instructions during baseball pitching training.* Int J Sports Sci Coach (2018), TU Delft. `[SAMPLE MISMATCH]` [TU Delft](https://research.tudelft.nl/en/publications/focus-of-attention-instructions-during-baseball-pitching-training/)
- **Donovan JJ, Radosevich DJ (1999).** J Appl Psychol 84:795–805. · **Lee TD, Genovese ED (1988).** RQES 59:277–287.
- **Spruit EN, Band GPH, Hamming JF (2015).** Surg Endosc 29:2235–2243. [PubMed 25318372](https://pubmed.ncbi.nlm.nih.gov/25318372/)
- **Schmid D, Erlacher D, Klostermann A, Kredel R, Hossner E-J (2020).** Neurosci Biobehav Rev 118:270–281. [PubMed 32730847](https://pubmed.ncbi.nlm.nih.gov/32730847/)
- **Bernstein NA (1967).** *The Co-ordination and Regulation of Movements.* Pergamon. **[canonical; not re-verified]**

### Data endpoints used for own computations

- `baseballsavant.mlb.com/statcast_search/csv` — four-seams 2024-06-01→06-05, n = 6,113; the only source with `release_extension` and vy0/vz0/ay/az for VAA
- `baseballsavant.mlb.com/leaderboard/active-spin` (2024, n = 708 pitchers; 2025)
- `baseballsavant.mlb.com/leaderboard/pitch-movement`, `/pitch-arsenal-stats`, `/pitch-arsenals`, `/spin-direction-pitches`

### Rejected as unverifiable / AI-generated

`accio.com` · `mlbanalytic.com` · `sportsorca.com` · `mkdcbaseball.com` · `seemagnus.com` · `sportstrace.com` · `talksox.com` · `baseballscouter.com`

### Circulating with no traceable source

- *"For every millisecond off optimal release there's ~2 feet of accuracy error at 80% speed."* — **FOLKLORE.** Roughly consistent with §5's angular arithmetic, so possibly a garbled restatement. **Do not cite.**
- *"2026 ASMI consensus statement"* on anything — **FABRICATED.**
- Nathan's fitted C_L(S) constants circulating online ("C_L = 0.09 + 0.6S"; "C_L,0 = 0.583, C_L,1 = 2.333, C_L,2 = 1.120") appeared only in a search-engine summary, not in an openable source. **UNVERIFIED.**
- MLB.com glossary pages for Perceived Velocity, Extension, and the sweeper/slurve thresholds return HTTP 406 to fetchers. The perceived-velocity formula in §2.4 is an empirical recovery from Statcast data, which is stronger evidence than the glossary would have been.

---

*Cross-references: `library/biomechanics.md`, `library/coaching-translation.md`, `library/idea-scouting.md`, `library/anatomy-physiology.md`, `library/open-disputes.md`.*
