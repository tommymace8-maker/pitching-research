# Environment: Air Density, Altitude, Temperature and Humidity

**Created 2026-09-05** (Cycle 5). Companion to `FINDINGS.md` F-260 → F-266.
Closes the `INDEX.md` §5 gap *"Environmental effects beyond the Reynolds-number note (altitude, temperature, humidity, ball construction year to year)."*

> ### ⚠️ PROVENANCE — read before quoting anything here
> This file was written in a **fully egress-blocked cycle**, the second consecutive one (F-266). **No primary source was opened.** Everything below is **computed in-cycle from stated equations with stated constants** — which is the one kind of content a blocked cycle can honestly produce (F-259).
>
> **The ratios are the result. The absolute inch values are calibration-dependent and are not claimed.** No Statcast validation was possible. An independent snippet-level corroboration exists (Alan Nathan's Denver page) and is **unread** — it is item 1 in the verification queue.
>
> **Ball construction year-to-year remains uncovered.** This file closes three of the four named sub-topics.

---

## 1. The model

Continuous with F-251, using its exact constants: m = 0.145 kg, r = 0.0366 m, A = 4.2078e-3 m², Cd = 0.33.

**Air density is computed, not assumed:**

```
ρ = p_d/(R_d·T) + p_v/(R_v·T)          R_d = 287.058, R_v = 461.495 J/(kg·K)
p_sat = 610.94·exp(17.625·T_c/(T_c+243.04))   Pa      (Buck)
p_v = RH · p_sat ;  p_d = p − p_v
p = p₀·(1 − 2.25577e-5·h)^5.25588       (ISA station pressure, h in m)
```

**Trajectory:** RK4, dt = 1e-4 s, vertical plane, with gravity, quadratic drag, and Magnus force perpendicular to velocity (F_M = ½·ρ·A·C_L·v²).

**Induced vertical break (IVB)** = Magnus trajectory − the same trajectory with spin removed. Gravity and drag cancel out of the difference.

**Continuity check.** At 0 ft / 68 °F / 50% RH → **ρ = 1.1988**; F-251 used **1.196**. Agreement to 0.2%. Dry air at the same conditions is 1.2041, which reveals F-251's "sea level, 20 °C" figure to have been implicitly humid.

### 1.1 The C_L problem and why the ratios survive it

No lift-coefficient model could be verified with egress down. So C_L is **not asserted** — it is calibrated so the sea-level case returns a league-typical 16.0 in IVB for a 95 mph four-seam, then **held fixed while only the air changes.**

This makes the absolute inches an assumption and the **ratios the result** — and §3 shows the ratios do not care what the calibration was.

---

## 2. Reference tables

### 2.1 Density by venue (game-typical temperature, 50% RH)

| Venue | alt (ft) | °F | ρ (kg/m³) | % of sea level |
|---|---|---|---|---|
| Sea-level reference | 0 | 70 | 1.1939 | 100.0% |
| **Swayze Field, Oxford MS** | 500 | 80 | 1.1485 | **96.2%** |
| Hoover AL (SEC tournament) | 560 | 85 | 1.1342 | 95.0% |
| Omaha (CWS) | 1,050 | 80 | 1.1257 | 94.3% |
| Tempe AZ | 1,150 | 90 | 1.0983 | 92.0% |
| Tucson AZ | 2,400 | 90 | 1.0487 | 87.8% |
| Logan UT (Utah State) | 4,500 | 70 | 1.0113 | 84.7% |
| BYU, Provo | 4,550 | 70 | 1.0094 | 84.5% |
| Albuquerque (UNM) | 5,050 | 80 | 0.9701 | 81.3% |
| Coors Field, Denver | 5,200 | 75 | 0.9748 | 81.6% |
| **Air Force Academy** | 6,600 | 65 | 0.9439 | **79.1%** |

### 2.2 A 95 mph four-seam, 6.5 ft extension

| Venue | flight (ms) | plate mph | IVB (in) | % of SL |
|---|---|---|---|---|
| Sea level | 406.1 | 86.8 | 16.00 | 100.0% |
| Swayze Field | 405.4 | 87.1 | 15.39 | 96.2% |
| Omaha | 405.0 | 87.3 | 15.09 | 94.3% |
| Tucson | 403.8 | 87.8 | 14.06 | 87.9% |
| Logan | 403.2 | 88.1 | 13.56 | 84.7% |
| Albuquerque | 402.5 | 88.4 | 13.01 | 81.3% |
| Coors | 402.6 | 88.3 | 13.07 | 81.7% |
| Air Force Academy | 402.1 | 88.6 | 12.66 | 79.1% |

### 2.3 Temperature (Oxford, 500 ft, 50% RH, 95 mph)

| °F | ρ | flight (ms) | IVB (in) |
|---|---|---|---|
| 40 | 1.2468 | 407.0 | 16.71 |
| 60 | 1.1967 | 406.2 | 16.04 |
| 80 | 1.1485 | 405.4 | 15.39 |
| 100 | 1.1010 | 404.6 | 14.76 |

≈ **0.033 in of IVB per °F.**

### 2.4 Humidity (Oxford, 85 °F, 95 mph)

| RH | ρ | IVB (in) |
|---|---|---|
| 0% | 1.1456 | 15.35 |
| 50% | 1.1367 | 15.23 |
| 100% | 1.1277 | 15.11 |

Total dry→saturated swing: **0.24 in.**

### 2.5 Breaking ball (curveball-scale C_L, 80 mph, total Magnus deflection)

| Venue | deflection (in) |
|---|---|
| Sea level | 32.00 |
| Coors | 26.16 |
| Air Force Academy | 25.33 |

---

## 3. The three results worth carrying

### 3.1 Movement scales with density, and the ratio is parameter-free

IVB % equals density % at every venue **to within 0.1 percentage point.**

| Sea-level calibration | C_L | AFA IVB % of SL | ρ ratio |
|---|---|---|---|
| 12.0 in | 0.1293 | 79.09% | 79.06% |
| 16.0 in | 0.1725 | 79.10% | 79.06% |
| 20.0 in | 0.2158 | 79.11% | 79.06% |

| Cd | AFA IVB % of SL |
|---|---|
| 0.30 | 79.10% |
| 0.33 | 79.10% |
| 0.36 | 79.10% |

**Invariant to both free parameters across their full plausible ranges.** That is what licenses using the bare density ratio in the field with no simulation.

**Is this a geometric identity restated?** *Partly, and it is flagged against the corpus's own check #4.* F_Magnus ∝ ρ by definition, so first-order proportionality is the force law, not a discovery. **The non-trivial part is that the second-order drag couplings cancel to <0.1%:** thinner air means less Magnus force *and* a shorter flight (less deflection time) *but* a higher retained velocity (F_M ∝ v²). The net was expected to fall below the density ratio. It does not.

### 3.2 Altitude is nearly all downside

Sea level → Air Force Academy, 95 mph four-seam:

| Quantity | Change |
|---|---|
| **IVB** | **−3.34 in (−20.9%)** |
| Flight time | −4.0 ms (−0.98%) |
| Plate speed | +1.76 mph |

The "thin air makes it play faster" consolation is **4 ms**. F-252's commit-instant band is 130–175 ms — a **45 ms uncertainty band on a single unverified input, eleven times the entire altitude effect on the clock.** The gain is not small; it is unmeasurable against the noise in our own model of the hitter.

**And it compounds badly with F-254.** Air density degrades the **movement** channel and leaves **velocity separation** untouched (that is a timing quantity). F-254 already establishes the movement channel as the *quadratic, back-loaded* one that has delivered under half its separation at the commit instant. **So thin air weakens the channel that was already the weaker one.**

### 3.3 Invisible to the pitcher, obvious to the sensor

**Perception** (via F-171: ±1.1° elevation release-angle SD × 30 cm/° = **13.0 in of vertical scatter at 1 SD**):

| Shift | IVB loss | as fraction of his own 1 SD |
|---|---|---|
| AFA vs sea level | 3.34 in | **0.26 SD** |
| Coors vs sea level | 2.93 in | 0.23 SD |
| Oxford Feb vs Jun | 1.99 in | 0.15 SD |

**Detection** (α = .05, 80% power, pitches of that type per group):

| IVB shift | SD 1.0 | SD 1.5 | SD 2.0 |
|---|---|---|---|
| 3.34 in | 1.4 | 3.2 | **5.6** |
| 2.93 in | 1.8 | 4.1 | **7.3** |
| 1.99 in | 4.0 | 8.9 | 15.9 |
| 1.00 in | 15.7 | 35.3 | 62.8 |

**Six to eight tracked pitches settle it. No amount of feel does.** When an effect is smaller than the athlete's own noise but larger than the sensor's, the sensor is the only honest witness and the athlete's feel is actively misleading.

---

## 4. Coaching

### 4.1 What to say, once, in the pre-series meeting

> "The air here is about four-fifths as thick as at home. Everything you throw is going to move about four-fifths as much — that's the air, it's not you, and it's happening to their pitchers too. Don't try to get it back. If you try to make the slider bite, you'll wrap it, and you'll take that home with you."

**Use the density RATIO, never the inch count.** The inch figures were computed on *vertical* break of a *four-seam* and do not transfer to a slider. (The coach was one sentence from making exactly that error; see `open-disputes.md` and the 2026-09-05 cross-examination.)

### 4.2 There is no drill

**The intervention is a prohibition, not an addition.** The only active change is a **usage** decision, made by the coach before the game: de-emphasise the biggest-breaking pitch (most absolute movement to lose), lean on pitches that never depended on Magnus — cutter, firm slider, anything living off velocity and location.

### 4.3 On video, the failure looks like

- a longer, more deliberate arm action on the breaking ball
- visible extra effort on a pitch previously thrown casually
- **the breaking ball's release point drifting from the fastball's** — the reliable tell, because adding break almost always means getting around the ball, which moves the hand

### 4.4 How you know it worked

- **Cheap check:** 6–8 tracked fastballs vs *his own* season baseline (never a staff average).
- **The check that matters:** movement returns to baseline **on the first outing back at sea level.** If it does, the air did it. **If it doesn't, he changed the pitch on the road and brought it home** — the actual failure this exists to prevent, detectable within one start.
- **Do not measure:** whether it bought outs. Per F-257, that needs thousands of swings; a road trip supplies dozens.

### 4.5 Humidity: say only that it does not matter

The folklore is wrong twice — **backwards in sign** (humid air is *less* dense; more humidity means slightly *less* break) and **negligible in size** (0.24 in dry-to-saturated, one-eighth of a seasonal temperature swing). If a pitcher raises it, the honest answer is that a muggy night affects his **grip and sweat**, which are real, not the aerodynamics, which are not.

### 4.6 Temperature is a measurement-hygiene problem

Most of a season's IVB drift at a sea-level program is **weather, not development.** A fastball that "lost an inch of ride" between February and May has most likely lost nothing. **Temperature-match any cross-month movement comparison**, and be most suspicious in the flattering direction: apparent *gains* in the fall are usually just colder air. Carry ≈ **0.03 in per °F**.

---

## 5. Stated limits

1. **No SSW term.** The model has none. Seam-shifted wake is a separation-point phenomenon, **Reynolds-dependent rather than simply density-dependent**, and potentially non-monotonic near the drag crisis. The ratio holds for clean Magnus pitches; **for sinkers, sweepers and seam-effect pitches it is an approximation of unknown quality that could err in either direction.** → `open-disputes.md` #18.
2. **Constant C_L.** Real C_L varies with spin factor S = rω/v; S at the plate is slightly lower in thin air, which would push real movement marginally *below* these numbers. Estimated sub-0.1 in; does not touch the ratio.
3. **2-D model.** Adequate for IVB; horizontal break is treated by symmetry, not simulated.
4. **Venue temperatures are assumptions**, not measurements.
5. **No empirical validation.** Model, not measurement. Nathan's page agrees at snippet level and is unread.
6. **The athlete is not in this model.** Altitude has real physiological effects (arterial O₂ saturation, ventilatory demand, disturbed sleep in the first 48 h). For a phosphagen task with 20+ s between efforts these should be near-irrelevant *within* an outing, but **between-outing recovery on a Colorado trip is a separate question this file does not address.** Read §3 as "altitude affects the pitch," not "altitude affects only the ball."

---

## 6. Queue

1. **Alan Nathan, `baseball.physics.illinois.edu/Denver.html`** — snippet reports ~4 in less curveball drop and ~4 in *more* fastball drop at Coors, matching this file's sign and order of magnitude. **The highest-value unopened item in the corpus**, because it independently checks work already done.
2. **Purple Row, *Pitching at Altitude* Parts 1–5** (2023) — snippet matches §2.5 directionally.
3. **Within-pitcher pitch-to-pitch IVB SD for an 85+ arm** — the corpus does not hold it, which is why §3.3's detection table is bracketed rather than exact. Computable from any program's own TrackMan in an afternoon.
4. **Does SSW movement scale with density or non-monotonically with Re?** → Dispute #18.
5. **Ball construction year-to-year** — the fourth sub-topic of the INDEX gap, still uncovered.
