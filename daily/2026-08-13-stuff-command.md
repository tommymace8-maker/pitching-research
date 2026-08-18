# Daily Brief — 2026-08-13
## Stuff / Pitch Design and Command

**Full report:** `library/stuff-and-command.md`
**Population:** elite, 85 mph floor · **Scope:** performance development only

---

## The one-paragraph version

Command is an **angular** problem, not a positional one — **1° of release angle = 30 cm (12 in) at the plate**, while 1 cm of release-point wander = 1 cm. That single fact reorganizes the whole subject: it explains why release-point variability predicts strikeouts and home runs but **does not predict walks** in 344 MLB pitchers (R² = 0.011), why velocity variability is a hidden command variable (**~3.5 in of vertical miss per 1 mph**), and why the industry's favorite command drill targets the wrong number. On the stuff side, the two best-leveraged findings are that **release height beats induced vertical break roughly 2:1 as a VAA lever** (+1.06°/ft vs −0.093°/in) and that **raw spin explains only ~4% of cross-sectional IVB variance** — the missing movement is in efficiency and axis, not rpm. And the motor-learning literature that underwrites most modern coaching pedagogy has been through a replication reckoning that baseball has not noticed.

---

## Five things that change practice tomorrow

**1. Stop coaching "repeatable release point." Start coaching release angle and release *speed*.**
Kusafuka 2020 (n = 7, 187 pitches, TrackMan + simulation, R² = 0.97): **~30 cm of location per 1° of release angle; ~1 cm per 1 cm of release point.** Confirmed independently by trigonometry (tan 1° × 54.5 ft = 11.4 in) and at MLB scale by the Kirby Index (release angles predict location at R² = 0.92 vertical; drop them and the model collapses to R² = 0.06). **Release point is ~30× less consequential than release angle.**

**2. Within-outing fastball velocity SD is an uncoached command metric you already measure.**
~20 cm of vertical location per 1 m/s → **1 mph ≈ 3.5 inches of vertical miss.** A pitcher ranging 91–95 in an outing carries ~14 inches of vertical scatter from velocity alone. Compute the SD off your radar log. Free.

**3. Score the *direction* of the miss, and specifically the horizontal sign.**
Kusafuka 2025 (*Sci Rep*, n = 14): pitchers with poor horizontal command are the ones who **fail to correct trial-to-trial** in that direction (r = 0.73 between "no correction" and azimuth variability). Vertical correction is near-universal among skilled throwers; horizontal correction is what separates. **Two consecutive same-direction horizontal misses is the actionable event.** Counting strikes cannot see this.

**4. Lower the slot to flatten VAA — the numbers are now on both sides of the ledger.**
Own Statcast regression (n = 6,110, R² = 0.999): **release height +1.06° steeper per foot; IVB only −0.093° per inch; velocity −0.063° per mph.** Slot beats ride roughly 2:1 as a VAA lever, and location has nearly equal and opposite leverage (−1.08°/ft). Pairs with the library's existing arm-slot finding (+2.14 run value, +18.3 rpm, −0.15 mph for a 2°+ drop). **Caveat: a higher slot predicted *better* command in 338 velocity-matched pros — see the conflict below.**

**5. Nobody can prove a command win in one bullpen. Say so before you start.**
With a within-pitcher miss-distance SD of ~10 in, detecting a **2-inch** improvement at 80% power needs **~196 tracked pitches** — seven to ten bullpens. A 30-pitch pen can only detect a ~5-inch change. And per the acquisition-vs-learning literature, **in-session improvement is not learning at all.** This is precisely why pitch design commercially outran command training: you can prove a spin-axis change in ten pitches.

---

## The conflict nobody in the library has named

Manzi et al. 2021 (*J Orthop*, **n = 338 professionals, velocity-matched, p = .055**) split high- vs low-command arms:

| At ball release | Plus command | Wild | vs. velocity model |
|---|---|---|---|
| Trunk flexion | **11.9°** | 15.9° | velocity β = **1.829** (more is faster) |
| Trunk lateral flexion | **−27.1°** | −31.8° | more is faster, **and** more elbow torque |
| Arm slot | **59.7°** | 54.7° | higher = more torque in pros |

**The delivery that maximizes velocity is not the delivery that maximizes command.** And the arm slot squares off against itself: **higher slot → better command, worse torque; lower slot → better VAA and lower torque, worse command.** Say this out loud before pushing an athlete toward "getting out over the front side." → new entry owed to `open-disputes.md`.

---

## ⚠️ Correction owed to two existing library files

**Bloebaum's uncontrolled-manifold synergy index (ρ = 0.22, p < 10⁻⁴⁷, 43,650 pitches / 2,052 pitchers) is an association with PITCH VELOCITY, not with command.** `idea-scouting.md` #3 and `coaching-translation.md` §6 both present it in a command context. **Both need correcting.** The paper is still valuable — for *how variability is structured* (segment-staggered convergence; trunk/pelvis minimum before foot plant; trunk carries only ~5% of release-preserving variance) — but it is not accuracy evidence.

The Driveline "adjustability ≥ repeatability" claim survives, but weakened: **n = 27, no published correlation table, no ANOVA (authors say n too small), features screened at |r| > 0.5.** It is corroborated from two independent directions, so keep the cue — but stop calling it settled.

---

## The motor-learning reckoning — this is the big one

Baseball coaching education teaches several of these as settled. **They are not.**

| Principle | Status |
|---|---|
| **Acquisition ≠ learning** (test delayed, changed, unaided) | **ESTABLISHED** — and the most-violated rule in applied baseball |
| **External focus** | Bias-corrected **g = 0.01 (perf), 0.15 (retention)**; Bayes factors favor the **null** across 7 meta-studies (McKay 2024, *Psych Bull*). Use as a cheap default; don't call it proven. **"Farther is better" is g = −0.01 — FOLKLORE** |
| **Enhanced expectancies / autonomy support / self-controlled practice** | Self-controlled practice **g 0.44 → 0.107** after bias correction, "not distinguishable from zero." Only **21% of 166 OPTIMAL experiments measured motivation at all. FOLKLORE as learning levers** |
| **Guidance hypothesis** (faded / bandwidth / reduced feedback) | **k = 75, N = 2,228: no effect at any time point, no moderators, no acquisition-to-retention dissociation. FALSIFIED.** So is the fashionable inverse — hiding the Rapsodo screen is equally unsupported |
| **Contextual interference (random > blocked)** | **Lab SMD 0.92; applied/field SMD 0.23, ns.** The famous baseball study (Hall 1994) is **n = 10 per group, on hitters.** Least supported precisely in our population |
| **Differential learning** | Single-lab dominance, I² ≈ 78%, high bias; the meta-analysts call inferences "premature." **No baseball pitching trial exists** |
| **Constraints-led approach** | **66% of technical outcomes showed no difference**; benefits concentrated in *tactical* outcomes, least relevant to location precision. **Framework, not intervention** |
| **"Take a little off to throw a strike"** | **No speed–accuracy trade-off found in overarm throwing across 40–100% of max**; force variability *peaks* near 60%. **FOLKLORE** |
| **Bullpen-to-game transfer of command** | **No study exists.** Genuine literature gap |

---

## Marketing, named

- **"Spin has diminishing returns because of the lift curve"** — C_L(S) is linear above S ≈ 0.15 and every MLB fastball sits at S ≈ 0.21–0.24. **Misapplying a curve nobody operates in.**
- **"Raise your spin rate"** — raw spin explains **~4%** of IVB variance (+0.32 in/100 rpm observed vs +0.57 theoretical). **The gap is efficiency.**
- **SSW as a service** — the physics is settled (Smith & Smith 2021; ~17.6° axis deviation on sinkers; +3 in run / +4 in drop league-wide; ~9 in at the extremes). But the prescriptive pathway is unsolved, pitch-to-pitch stability unknown, and **Driveline's own data found ~42% of SSW-affected pitches had LOWER Stuff+.** Movement ≠ value.
- **"Match your changeup's spin axis to your fastball"** — spin-axis similarity showed **no predictive value** for changeup whiff rate (Rosen 2025). Neither did velocity or arm-angle change. **Kill the spin, preserve arm speed, make him early.**
- **Building around the sweeper in 2026** — RV/100 **−0.94 same-handed vs −0.05 opposite-handed** (worse than an ordinary slider). Whiff% 33.4 → 31.0 → 31.2. Driveline **repriced it downward** in Stuff+ v4. The alpha is gone.
- **Tunneling** — BP's metric suite was **published with zero outcome validation**; independent test gives **r = 0.07** with run value. What *does* work is **horizontal release-angle overlap** (59% swing prediction vs Stuff+'s 54%; r² = 0.12–0.20 vs 0.001) — a static, trainable property of the delivery, not a sequencing decision.
- **Optimizing Stuff+** — predicts ERA at **r ≈ .14 for team-switchers** (vs .41 same-team); its discriminating power has compressed **~9% since 2020** as everyone optimizes to it; and the "r² = .996" figure circulating is a curve-fit of bucketed group means, not pitcher-level prediction.

---

## Three open questions

1. **Does within-outing release-speed SD predict vertical command in a large sample?** Physics says ~3.5 in per mph. Trivially computable from any Statcast or Trackman database, and apparently nobody has done it. **Cheapest high-value study in the whole report — a college program could run it this fall.**
2. **Is spin efficiency actually trainable in an elite arm, and by how much?** The entire pitch-design industry assumes yes. **No controlled intervention trial found.** That absence should bother people more than it does.
3. **Does anything measurably transfer from the pen to the game for command?** No study exists in baseball. Everything in the training protocol is reasoned from general principles — and the general principles just lost their two most-cited pillars (guidance hypothesis, applied CI).
