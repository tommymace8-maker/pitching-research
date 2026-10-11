# HEAT, THERMAL STRAIN AND HYPOHYDRATION — the pitcher, not the ball

**Opened 2026-10-11.** Findings **F-657 → F-668**. Disputes **#69, #70**.
⚠️ **Written in a fully egress-blocked cycle (the twelfth consecutive — F-657). NOT ONE primary text in this file was opened. Every magnitude is snippet-level, several at two removes. Treat the whole file as a map of leads with the derivations marked.**

**Scope note.** The corpus already covers heat acting on the **ball** (`environment-air-density.md`, F-260→F-265) and muscle temperature across the **inning break** (`between-inning-break.md`, F-354→F-358). This file covers heat acting on the **pitcher**: thermal strain, hypohydration, cooling, acclimatization, and the task-class question.

---

## 1. The one-paragraph version

There is no evidence base. Not weak evidence — **none**, and the gap is six-fold (F-666). What exists is three adjacent literatures, each measuring an outcome this corpus has already ruled untransferable: cooling measures endurance and lower-body peak power, which **F-004 forbids converting into mph**; heat acclimation measures aerobic and thermoregulatory adaptation and has **never improved peak anaerobic power**; hypohydration measures cognition and paced visuomotor accuracy. Meanwhile the two numbers everyone quotes for temperature and velocity are **both confounded by the calendar in the direction of the claimed effect**.

The useful output of the cycle is therefore not a recommendation. It is **three designs and one measurement**:

| | What | Cost | Who can run it |
|---|---|---|---|
| **Design 1** | Within-pitcher, **within-calendar-month** temperature contrast (F-659) | 22–50 starts for ~1 mph; 80–181 for 0.5 mph. Free public data. | **MLB data only.** A college staff is short by 3–10×. |
| **Design 2** | **Heat × pitch-tempo-pressure interaction** on late-inning command (F-663) | Two public datasets, no new instruments | MLB data only |
| **Design 3** | **Home/away split inside one hot venue** as an acclimatization test (F-668) | One Statcast query | MLB data only |
| **Measurement** | **Weigh the starter in and out, log bottles** (F-665) | A scale and a clipboard | **Any program, this week** |

---

## 2. The calendar confound — why both published temperature numbers are unusable

**F-658.** Two bodies of evidence, opposite directions, same disease.

- **Cold end:** ≤40 °F starts run **~0.95 mph** below the same pitchers' other games (FanGraphs, PITCHf/x 2008–2015). But ≤40 °F games in MLB are **April** games, and the comparison set is May–September. The estimate contains the **season's velocity ramp**, which has the same sign as the cold penalty. A pitcher fixed effect does not remove a within-pitcher time trend.
- **Warm end:** season-start to season-end velocity rises **~0.6 mph**, largest step March/April → May, **peak in August–September**. FanGraphs names three causes and declines to choose: ramp, weather, **survivorship**. ⭐ **The tell is the peak: the curve tops out in September, when it is cooling.**

**The screen, for any future claim:** *did you hold the calendar month fixed?* If not, they measured the season.

**One channel survives and must not be shadowed by this entry.** Cold **finger and hand sensation** is a different mechanism, is not calendar-confounded, and attaches to **F-431/F-432** (friction, finger normal force, spin) rather than to velocity.

**Cross-era caveat.** Statcast reads peak velocity near the hand; PITCHf/x measured near 55 ft, so Statcast runs **~1 mph higher**. The cold study is PITCHf/x-era and is not directly comparable to current figures.

---

## 3. The threshold ladder, and the exposure-dose mismatch

**F-664.** All snippet-only, all from continuous passive or exertional heating:

| Core temperature | What begins to happen |
|---|---|
| ~37.8 °C | voluntary force production falls |
| ~38.3 °C | motor cortical excitability drops |
| ~38.5 °C | cortical motor drive suppressed in high-intensity tasks |
| ~38.8 °C | complex cognitive performance declines with neuromuscular function |

**The dose does not match.** A starter throws **15–20 minutes of actual work across two hours**, with a passive half-inning between every work bout. **Within a baseball team he is the lowest thermal-strain position on the field** — the catcher is the highest, a corner outfielder is higher than the pitcher.

⭐ **This is the F-631/F-650 rule in a third form: ask what the sample's actual EXPOSURE DOSE was before importing its magnitude.** Thermal strain is a dose. Continuous-exercise magnitudes do not port to intermittent work with long passive recovery.

**It is a prior, not a dismissal, and it is cheap to overturn: one ingestible pill, one pitcher, one 92 °F game.** Until then the whole ladder is unusable, because nobody knows which rung he is on.

---

## 4. ⭐⭐ The task-class argument — the cycle's new idea

**F-662 / F-663, and Dispute #69.**

**Step 1 — heat is NOT another "zero accuracy outcomes" venue.** For six weeks this corpus has tallied topics with no accuracy outcome at all (Dispute #27; the tally reached its **TWELFTH** venue on 2026-10-10 and read *"holds without exception"*). Heat supplies the counterexample, and a large one:

> **Wittbrodt et al. 2018, *Physiological Reports*, doi 10.14814/phy2.13805.** n = **13**, counterbalanced 150-min trials at **45 °C / 15% RH**. Visuomotor accuracy **69.7 ± 13.5%** (heat + ~2.8–3.0% dehydration) vs **85.1 ± 7.0%** (seated control), **P < 0.01**; response time 6–8% slower.
> ⚠️ Snippet-only at **two removes**. A review table lists n = 12 vs the abstract's 13 — unresolved. **Unblinded to hydration status.**

**Step 2 — the task was PACED.** Twenty-two minutes, externally timed. The participant responds when the machine says.

**Step 3 — the dissociation.** A **~1.5 °C** core rise did **not** change brain activity during **self-initiated** movement but **did** during **externally triggered** movement (PMC12321350); a companion review states self-paced voluntary movements are unaffected while externally triggered movements needing prefrontal control are impaired (PMC13232702). ⚠️ **Both outcomes are brain activity, not performance.**

**Step 4 — a pitch is the most self-initiated movement in sport.** Nothing cues it. He comes set and goes when he decides to go.

**What is defensible (narrowed after Challenge 1):** not *"heat spares pitching"* but a property of the measurement — **the single largest accuracy decrement in the heat literature was collected on a paced task, and the pacing may be the thing that produced it.**

**Step 5 — ⭐⭐ and the pitch clock breaks it.** Under a timer, a pitcher at 0.5 seconds remaining is **externally cued**, under time pressure, with a called-strike penalty for failing. If the dissociation is real, the clock **selectively** moves exactly those pitchers into the heat-vulnerable class.

**The prediction, pre-registered 2026-10-11:**
- split pitchers by **tempo pressure** (Statcast Pitch Tempo leaderboard — with **F-334's** caveat that its definition excludes most of a pitcher's pitches);
- split games by **temperature**;
- outcome: late-inning **location SD** or called-strike rate;
- **predicted:** interaction concentrated in the high-tempo-pressure group, ≈ 0 in the fast-working group;
- **falsified by:** a main effect of heat with no tempo interaction.

⚠️ **The test is observational and three alternatives would produce the same interaction** (faster fatigue in heat, hurried mechanics under clock pressure independent of temperature, dehydration). **A positive result is suggestive; only the absence is decisive.** ⚠️ **And it is not yet priced — it needs ρ, the within-bullpen location ICC, still unpublished, now blocking a FIFTH topic.**

---

## 5. The three channels that land in forbidden outcome classes

| Channel | Best evidence | Why it does not reach a fastball |
|---|---|---|
| **Cooling** (pre/per) | Bongers 2015 *BJSM*, 28 studies: **+6.7 ± 0.9%, ES 0.43**. Hohenauer 2018, 29 studies: external pre-cooling on **peak power**, **g = 0.49 [0.33, 0.64]**. A third meta found **no** power difference (p > 0.05). | **F-004:** jump height vs velocity **r = 0.07, NS**. Lower-body power % **cannot** be converted to mph. Zero throwing outcomes in the entire literature. **(F-661)** |
| **Heat acclimation** | Chalmers 2014 *Sports Med*, PMID 24817609, 8 studies: ***"peak anaerobic power efforts have not been demonstrated to improve."*** Peak power unchanged in cool conditions; 15 m sprint unaffected; one study **+~2%** after 10 days. | The adaptations are **plasma volume, earlier/higher sweat rate, lower core temperature at a given workload** — all cardiovascular and thermoregulatory. **Not one is a rate-of-force-development adaptation.** It is a **tolerance** intervention. **(F-660)** |
| **Hypohydration** | ~2.4% loss, n = 30 randomised: **motor learning NOT impaired**. n = 10 crossover: no cognitive decline bar one subtest. GSSI: decrements *"more likely > 2%… significant inter-individual variability."* The clear decrement needed **2.8–3.0% + 45 °C** (§4). | The 2% threshold is **borrowed from team sports**, the cleanest motor test at 2.4% came back **null**, and **F-395** already established no primary hydration-and-pitching study exists at all. **(F-665)** |

⚠️ **The 2019 *Frontiers in Physiology* heat-acclimation meta-analysis and meta-regression exists and its sprint/anaerobic effect sizes were not retrievable. That is the cheapest verification item from this cycle.**

---

## 6. The 2% arithmetic — F-665

**90 kg arm; 2% = 1.80 L; exposure 2.5 h (≈25 min pre-game bullpen + ≈2.0 h outing and dugout).** Net deficit as % body mass:

| sweat rate | drink 0.5 L | 1.0 L | 1.5 L | 2.0 L |
|---|---|---|---|---|
| 0.59 L/h *(vendor)* | 1.08% | 0.53% | −0.03% | −0.58% |
| 0.83 L/h *(GSSI pooled baseball, n = 1,303)* | 1.75% | 1.19% | 0.64% | 0.08% |
| 1.20 L/h *(heat bracket)* | **2.78%** | **2.22%** | 1.67% | 1.11% |
| 1.50 L/h *(heat bracket)* | **3.61%** | **3.06%** | **2.50%** | 1.94% |
| 2.00 L/h *(upper bracket)* | **5.00%** | **4.44%** | **3.89%** | **3.33%** |

⚠️⚠️ **The sweat-rate column is the weakest thing in this file.** 0.83 L/h is a **commercial blog's summary** of a GSSI pooled dataset; 0.59 L/h is a **sensor vendor's marketing page**. Neither was measured in heat; neither separates pitchers from position players. The 1.2–2.0 rows are a **bracket imported from intermittent team sport**.

**Four conclusions, robust across the bracket:**
1. At pooled rates, **half a litre keeps him under 2%**.
2. **In real heat he exceeds it drinking two litres** — and that row is the unmeasured one.
3. **The binding variable is drinking behaviour, not sweat rate.** He is the one athlete on the field with a private, unobserved two-hour window and a cooler ten feet away.
4. ⭐ **The within-game risk is largely an artifact of attention. The real exposure is cumulative** — a pitcher arriving at a Friday start already 1% down from Thursday's lift starts at the top of the table.

---

## 7. The six-fold gap — F-666

Established at the **corpus level** after a six-angle sweep; a reading cycle must confirm literature-wide.

1. **No cooling intervention has ever been applied to a pitcher**, in any population.
2. **No core-temperature measurement of a pitcher exists**, in any game, at any level.
3. **No sweat rate has been measured in a pitcher in heat.**
4. **No in-game fluid intake has been published for a pitcher** at any level.
5. **No study relates WBGT or any heat metric to pitch velocity or command.**
6. **Zero throwing or throwing-accuracy outcomes in the entire pre-cooling/per-cooling literature.**

**The one baseball thermal study in existence used intermittent vest cooling on CATCHERS, in a SIMULATION** — sample size, level and core-temperature method all unknown to this corpus. ⭐ **Note the direction: the catcher is the highest-strain position and the pitcher the lowest, so its magnitudes are an UPPER BOUND on anything a pitcher could show.**

**The one procurement decision this cycle supports: if the program buys cooling vests, they belong behind the plate.**

---

## 8. What to do, and what not to

### Do: weigh the starter in and out, and log what he drinks

- Same-clothing weight 20 min before the pre-game bullpen; same scale, same protocol, within 10 min of coming out. Every bottle logged in millilitres.
- **Cost:** the scale F-630 already put in the pitchers' locker room, and one manager with a clipboard.
- **What it buys:** his **sweat rate in his actual conditions** and his **actual deficit** — two numbers that do not exist in the published literature for any pitcher at any level, and which §6 had to bracket across a **3.4-fold range** because of it.
- **Decision rule, stated in advance:** >2% → behavioural fix (more bottles, start earlier). <1% → the hydration conversation is over for the season.
- **Reliability, not power:** **6–8 outings** for a stable per-athlete sweat rate. ⚠️ **This is a MEASUREMENT, not an intervention — it owes reliability, not a powered outcome. DO NOT regress velocity on it:** at a per-start SD near 1 mph you would need F-659's start counts, which a program does not have.

### Do not
- **Buy cooling vests for pitchers** (F-661 — no measured channel; F-666 — wrong position).
- **Run a heat-acclimation block for performance** (F-660 — no anaerobic-power adaptation, no RFD mechanism). Run one for competitive comfort if you like, and do not attach mph to it.
- **Change anything based on the thermometer** (F-658 — no clean estimate exists).
- **Test weather effects on your own staff** (F-659 — short by 3–10×).
- **Tell a pitcher heat will fog his command** (F-662 — no mechanism in a self-paced task), *unless* F-663 turns out to be right, which nobody knows yet.

---

## 9. Standing distinction added by this cycle

**Two kinds of recommendation, and this corpus had only formalised one** (Challenge 3, 2026-10-11).

- An **INTERVENTION** changes the athlete and owes a **powered outcome** with the sample size to detect it.
- A **MEASUREMENT** changes what the coach knows and owes only **reliability** — how many observations until the number is stable.

The hazard is real and accepted: **a measurement with no outcome becomes an intervention the moment somebody acts on it.** That is why §8 states its decision rule *in advance* and explicitly forbids regressing performance on the result.

---

## 10. Open items handed forward

1. **Run F-663's heat × tempo test.** Cheapest unrun test in the corpus; decides whether §4 is a finding or a story.
2. **One ingestible pill, one pitcher, one 92 °F game.** The entire §3 ladder is unusable without it.
3. **What does a starter actually drink?** §6 pivots on it; unpublished at every level. It is a clipboard.
4. **The 2019 Frontiers heat-acclimation meta-analysis magnitudes** — one table, closes F-660's only soft edge.
5. **ρ, the within-bullpen location ICC** — still unpublished, now blocking a fifth topic.
6. **Wittbrodt's n: 12 or 13?** Unresolved until egress returns.
