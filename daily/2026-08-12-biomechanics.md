# Daily Research — 2026-08-12 — Biomechanics of the Pitching Motion (Day 1)

**Scope: ELITE ONLY. 85 mph hard floor.** Elite HS (PG/showcase, D1-committed) → D1 → MiLB → MLB. Target 90–95+.
**Full report:** `research/library/biomechanics.md`

---

## The one thing to know today

**Velocity is not the injury risk factor. Torque is — and the exchange rate between them varies ~28% across elite arms.**

In 305 professional pitchers followed ~4.5 years (Fleisig et al., 2025, OJSM — the only strong prospective study in this literature):
- Fastball velocity: **85.0 mph (later UCL surgery) vs 84.7 mph (healthy), p = .604 — no difference.**
- Elbow varus torque: **100.8 ± 18.1 vs 94.3 ± 16.1 N·m, p = .049. HR 1.26 per 10 N·m (95% CI 1.01–1.56).**

And in 523 elite pitchers (425 pro, 98 D1), the high-torque group produced **28% more normalized elbow torque for 1% more ball velocity** (6.37 vs 4.61 %BW×BH; 38.0 vs 37.1 m/s). **That gap is the entire coaching opportunity.**

## The trap: between-pitcher ≠ within-pitcher

Slowik et al. 2019 (n=64 pro): velocity↔elbow torque was **R² = 0.076 between pitchers** but **R² = 0.957 within a pitcher.**
→ Comparing two pros tells you nothing. **Your athlete cannot add velocity to his current delivery for free.** The lever is changing what kind of delivery it is, not "throwing harder with less stress."

## Elite reference numbers (ASMI, n = 288 pro; lab velo 38.1 m/s)

| At FC | | At MER | | At BR | | Peaks | |
|---|---|---|---|---|---|---|---|
| Stride length | 75–76 %ht | Max shoulder ER | 165–168° | Trunk lateral tilt | 24–34° | Shoulder IR vel | 5,456–6,149 °/s |
| Lead knee flex | 44–49° | Max elbow flex | 89–90° | Shoulder abd | 84–95° | Elbow ext vel | 2,191–2,403 °/s |
| Shoulder abd | 82–85° | Horiz add | 7–11° | Elbow flex | 30–35° | Trunk ang vel | 711–742 °/s |
| Elbow flex | 93–101° | | | Arm slot | 44–75° | Pelvis ang vel | 622–717 °/s |

**Kinetics (pro):** elbow varus **4.8–5.1 %BW×BH ≈ 90–100 N·m** · shoulder IR torque **4.9–5.2 %BW×BH** · shoulder distraction **~114 %BW ≈ 1,060 N** for a 95 kg athlete.
**Caution:** published elbow torque ranges 64→120 N·m across labs. Never compare across systems. Also: **lab velo ≈ 5–8 mph below game velo**, so these kinetics likely UNDER-state game load.

## Phase timing — why the stride is the only coachable phase

FC→MER ≈ **100–150 ms** · MER→BR ≈ **30–50 ms** · BR→MIR ≈ **30–50 ms**.
Everything downstream of foot contact is too fast to alter in real time. **Foot contact is where the delivery is decided.**

## The UCL margin (most important for the coach)

~95–100 N·m varus torque × ~54% UCL restraint share (Morrey & An) ≈ **51 N·m through the UCL**, vs cadaveric failure **~32–34 N·m** (Dillman; younger cadavers 34 N·m).
**The naive arithmetic says every pitch should tear it. It doesn't, because (a) inverse dynamics gives NET joint torque, not ligament load; (b) the flexor-pronator mass actively shares valgus restraint, which cadaveric testing cannot capture; (c) cadaver tissue ≠ adapted 22-yr-old tissue.**
→ **Real takeaway: the UCL runs with essentially no safety margin, bridged by active muscular load-sharing. Fatigue removes the bridge.** (Mechanistic inference, not a directly measured finding.)

## Four "free" torque reductions — raise torque, don't raise velocity

From two regressions on 523 and 337 elite pitchers:
1. Shoulder abduction at FC — lower it (pro norm 82–85°)
2. Elbow flexion at FC — lower it (pro norm 93–101°)
3. Shoulder abduction at BR — raise it (pro norm 84–95°)
4. Pelvis peak velocity later relative to trunk (proper sequencing)

**These are cross-sectional associations. No intervention trial exists. Model explains only 40% of torque variance.**

**Direct conflicts (buy velo, cost torque):** elbow extension velocity · lead-knee extension velocity · trunk lateral tilt at release.
**Clean win:** stride length (β = 0.334 for velocity, not a torque contributor).

## Three claims to stop making

- **"The block whips the hips."** Driveline, 800+ force-plate sessions: pelvis rotation gain after foot plant vs velocity **r = −0.07**. The block works via COG deceleration and lead-knee extension, not pelvis spin. After controlling bodyweight, lead-leg GRF explains only ~4–6% of velocity variance.
- **"Get on top of the ball."** Professionals throw from a **lower** average slot than high schoolers (58 ± 14° vs 50 ± 11°), and in pros a lower slot associates with **less** elbow varus AND shoulder IR torque (−0.1 %BW×BH per 10°).
- **"Fix your kinematic sequence."** In the one study that looked (n=14), the textbook pelvis→trunk→arm→forearm→hand sequence was **never observed on any pitch**; each pitcher averaged **2.7 different sequences across 5–6 throws.** The proximal (pelvis→trunk) order holds up; the distal order does not. What IS supported: **trunk peaking before pelvis raises torque** (Aguinaldo & Escamilla).

## Measurement — what's real

- **Motus/PULSE "Stress" is NOT torque.** It runs **~41 N·m (39%) below lab elbow torque** (Boddy et al., PeerJ 2019) while correlating strongly. Use for **within-athlete longitudinal load only.** Never compare to published torque or to the 32 N·m failure figure. Never compare between athletes.
- **Markerless:** Hawk-Eye MPJPE 56.6 ± 9.4 mm, Theia3D 52.0 ± 12.3 mm vs marker-based (n=18 D1). Kinematics good; **kinetics treat with caution.** KinaTrax = 8 cameras @ 300 Hz, in-game. In-game variability ≈ lab variability (Lerch, J Biomech 2025) — markerless is capturing real movement.
- **Trackman vs Rapsodo are NOT interchangeable** (Rapsodo reads velocity lower). Pick one system and never mix.
- **Video: 240 fps minimum, 1/1000 s shutter.** At 30 fps you get ~1 frame in the entire acceleration phase. Cameras: open side (stride, tilt, knee, timing), closed side (separation, elbow), straight-on (lateral tilt, foot placement/angle).
- **Force plates are the best value-per-dollar addition** — GRF is directly measured, unlike torque.

## Tomorrow's hooks
Fatigue → flexor-pronator load-sharing. Deceleration-phase training. Elite braking-impulse norms (unpublished gap).
