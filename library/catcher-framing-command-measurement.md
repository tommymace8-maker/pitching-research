# Catcher Framing, the Zone Edge, and What Contaminates a Command Number

**Created 2026-09-11 (cycle 10).** Findings **F-305 → F-314**.

> ### ⚠️ RUN CONDITION — read before using anything here
> This file was written in the **SEVENTH consecutive fully egress-blocked cycle** (F-304). **No primary source was opened.** Every quantity below is either (a) **derived in-cycle** from rule geometry, flight geometry or probability, and depends on no source, or (b) **explicitly flagged as an unverified empirical input**. There are exactly **three** inputs of type (b) and each is bracketed where it is used:
> 1. the **per-pitch run-value table** (inherited from F-270, already flagged there);
> 2. the **±15–20 runs/season MLB framing spread**, reconstructed from memory;
> 3. the **catch distance** `d = 1.5–2.0 ft` from plate to glove, an assumed bracket.
>
> **The ORDERINGS and the STRUCTURAL results are the output. The cell values are not.** Same discipline as F-269, F-278, F-296.
>
> **This topic was nominated by the corpus itself.** F-265's coaching note (2026-09-05) listed "the geometry of catcher framing and receiving angles" as a remaining gap a blocked cycle could close. This is that cycle.

---

## 0. Why this belongs in a pitching-development corpus at all

Framing is a catcher skill. This program develops pitchers. The reason it is here is **F-182**: the corpus already recorded that framing contaminates command measurement, and then never sized the contamination.

That is the whole point of the file. The question is not *how good is my catcher*. The question is:

> **When I say a pitcher's command improved this year, how much of that number is the pitcher?**

The answer, derived below, is uncomfortable: **at the scale of a real one-season command gain, roughly half of it can be the catcher** — and because catcher assignment is not random, it does not average out.

---

## 1. The called zone is a BALL-CENTRE zone (F-305)

Any part of the ball over any part of the plate is a strike. So the region in which a **ball centre** produces a strike is one ball-radius larger than the rulebook zone on every side.

| Quantity | Value |
|---|---|
| Ball diameter | 2.90 in (circumference 9.00–9.25 in) |
| Plate width | 17.0 in |
| Vertical rulebook zone (conventional) | 1.60 → 3.40 ft = 21.6 in |
| **Ball-centre strike zone** | **19.90 in wide × 24.50 in tall** |
| Rulebook area | 367 in² |
| **Ball-centre area** | **488 in² (+33%)** |
| **Perimeter of the ball-centre zone** | **88.8 in** |

The horizontal geometry is exact and rule-derived. The vertical band uses conventional Statcast averages and is batter-dependent.

**The 88.8-inch perimeter is where this entire file takes place.** Framing operates there; called-strike-based command metrics are contaminated there; nowhere else.

⚠️ **Do not make this a cue.** "Use the extra inch and a half" is the stride-length error (F-043/F-044/F-045) waiting to happen. Nobody has manipulated edge-targeting in an 85+ arm and measured the result.

---

## 2. The physical framing lever: plate-to-glove travel (F-306)

**The umpire does not judge the ball where it crosses the plate. He judges it where it is caught** — roughly 1.5–2.0 ft further on. Over that gap the ball keeps descending.

drop = v_vert · t + ½·g_eff·t² , where v_vert = tan(|VAA|)·v , t = d/v , g_eff ≈ 20 ft/s²

At **d = 1.75 ft**:

| Pitch | mph | VAA | drop, d=1.5 ft | **d=1.75 ft** | d=2.0 ft |
|---|---|---|---|---|---|
| 4-seam (elite) | 94 | −5.0° | 1.59″ | **1.86″** | 2.12″ |
| 4-seam (typical) | 92 | −5.5° | 1.75″ | **2.04″** | 2.34″ |
| Sinker | 91 | −6.5° | 2.07″ | **2.41″** | 2.76″ |
| Slider | 85 | −7.5° | 2.39″ | **2.79″** | 3.19″ |
| Curveball | 78 | −10.0° | 3.19″ | **3.73″** | 4.27″ |

**Horizontal equivalent** (92 mph, HAA 2.5°, d = 1.75 ft): **0.92 in**.

The g_eff term contributes under 0.03 in over these times — the result is essentially `v_vert · t`.

### Two predictions, reached from geometry alone

1. **The vertical lever is 2–4× the horizontal one.**
2. **The lever scales with tan(VAA), so it is largest for the steepest pitches — the low ones.**

The industry believes framing value is vertical-dominant and bottom-of-zone-dominant. **This cycle reached both from flight geometry without reading anyone**, which is worth more than one more person asserting them.

⚠️ **This is a bound on what is geometrically available, not a demonstration that anything is coachable.** Nobody has manipulated catch distance and measured called strikes. **MARKER, NOT LEVER.** Anything a receiving coach claims *beyond* ~2 in on a fastball is not a claim about where the ball is — it is a claim about umpire perception, which is a different and far less supported thing.

---

## 3. The shift-times-density result (F-307)

Model the umpire as calling a strike with probability `Φ(−d/σ_u)` for a pitch at signed distance `d` from the zone line. **σ_u is unknown and this corpus has no verified value for it.**

A catcher who shifts the **presented** location by `δ` converts

∫ f(d) · [ Φ(−(d−δ)/σ_u) − Φ(−d/σ_u) ] dd

Where the pitch density `f` is locally flat across the band, **this integral equals exactly `δ · f₀`** — where `f₀` is the density of taken pitches at the line.

> ### **IT DOES NOT DEPEND ON σ_u.**

A sloppier umpire converts *more* pitches near the line and *fewer* far from it, and the two effects cancel. **The eternal dugout argument about whether tonight's umpire is tight or wide is, for framing purposes, second-order.**

### Numerical value of f₀

Calibration: 2-D Gaussian pitch locations, σ_p = 10 in/axis (giving a ~53% zone rate); swing model fitted to **47% swing / 68% in-zone / 28% chase** (achieved: 48.4 / 66.6 / 27.8; taken rate 51.6%).

| Band ±b of the line | Share of TAKEN pitches |
|---|---|
| 0.5 in | 7.4% |
| 1.0 in | 14.6% |
| 1.5 in | 21.9% |
| 2.0 in | 28.6% |
| 3.0 in | 41.3% |
| 6.0 in | 69.9% |

**f₀ = 7.38% of taken pitches per inch.** Cross-checks agree: 7.28%/in at b=1.0, 7.29%/in at b=1.5.

> **The portable form: every inch of presentation is worth about 7 calls per 100 taken pitches.**

⚠️ **Say "about 7 per 100 per inch," never "7.38."** f₀ is a model output that scales with the assumed location scatter — a pitcher who lives on the edges has a higher f₀ than one who works the middle. ⚠️ The flatness assumption fails at the **corners** of the zone, where the rectangle model is weakest; the correction is second-order and was not computed.

---

## 4. What it is worth — and the backward check (F-308)

Using **this corpus's own F-270 table** (ball +0.055 R, called strike −0.045 R), one flipped call = **0.100 R**.

| δ (in) | flips / 1000 taken | runs / 1000 taken |
|---|---|---|
| 0.25 | 18.5 | 1.85 |
| 0.50 | 36.9 | 3.69 |
| 1.00 | 73.8 | 7.38 |
| 2.00 | 147.6 | 14.76 |

**Full season** (taken rate 51.6%):

| | taken | δ=0.5 in | δ=1.0 in |
|---|---|---|---|
| College catcher (4,200 pitches) | 2,168 | **8.0 R** | 16.0 R |
| MLB catcher (7,500 pitches) | 3,872 | 14.3 R | 28.6 R |

### The backward check — and it is the real finding

Run the reported MLB framing spread **backward** through the same model:

| reported season framing value | **implied δ vs the average catcher** |
|---|---|
| +10 R | **0.35 in** |
| +15 R | **0.52 in** |
| +20 R | **0.70 in** |

⚠️ *The ±15–20 R anchor is reconstructed from memory, no page opened, NOT verified.*

> **The physical lever available is ~2 inches (§2). The observed spread between the best and worst catchers in the world is about HALF AN INCH — a quarter of it.**

The honest reading: **nearly every professional catcher already captures most of the available geometry.** What separates them is the residual. Which also means the headroom for a college receiving program is *the part nobody has measured* — so do not promise a catcher two inches.

### Ordering against the corpus (per college season)

| Item | Value |
|---|---|
| F-280 — the 0-2 waste-pitch argument | ~0.2 R |
| F-288 — times through the order | ~1 R |
| F-296 — an exploited sequencing tendency | 0.8–6.4 R |
| **This — a 0.5-in catcher difference** | **~8 R** |

**The corpus has spent four cycles on questions worth about a run apiece. This one is worth eight** — and it is a roster and playing-time argument, not a bullpen one. Hand it to whoever makes those decisions.

⚠️ **Do not quote the run cells.** They scale linearly with an unverified framing anchor *and* with F-270's own bracketed SD. **The ordering is the output.**

---

## 5. ⚠️ The contamination — called-strike rate is a two-person statistic (F-309)

Pitcher command modelled as **execution scatter** (F-182: elite xCTRL miss ~7.05 in, worst >10 in). **Zone rate** is a fact about where the ball went:

| execution SD | zone rate | local slope |
|---|---|---|
| 6.00 in | 0.865 | — |
| 7.00 in | 0.777 | −9.01 pts/in |
| 7.05 in | 0.772 | −9.07 pts/in |
| 8.50 in | 0.644 | −8.54 pts/in |
| 10.00 in | 0.530 | −7.40 pts/in |

**Sensitivity near elite command ≈ 9.0 points of zone rate per inch of execution SD.**

### Head to head, in the same units

| Source of movement in observed called-strike rate | pts |
|---|---|
| A realistic **one-season command gain** (exec SD 7.5 → 7.0 in) | **4.52** |
| **Changing catchers**, presentation δ = 0.5 in | **3.69** |
| Changing catchers, δ = 1.0 in | 7.38 |

> ### **RATIO = 0.82. The catcher term is the same size as the thing you are trying to measure.**

Against the **large cross-sectional** gap (7.05 vs 10.0 in = 24.2 pts) the catcher is only **15%** — ignorable.

**It is the small, within-athlete, year-over-year change — the only kind a development program ever produces — where the contamination equals the signal.** That is the **F-094** pattern (between vs within) arriving in a new place.

### And it is BIAS, not noise

Catcher assignment **is not random**. Your Friday starter throws to your best receiver. So this does **not** average out:

> **More pitches shrink the noise and do not shrink the bias. Every instinct to "wait for a bigger sample" makes the error MORE confident.**

This is precisely **F-287**'s structure (the lineup-slot composition bias), and it is the corpus's **second** worked example of a bias that does not shrink.

**The practical damage:** a pitcher who caught the backup as a freshman and the starter as a sophomore is handed a command improvement he did not earn. One who moves the other way is blamed for a decline that is not his.

---

## 6. The fix — and this time it is free (F-310)

| Option | Framing-immune? | Sample cost |
|---|---|---|
| **1. Zone rate / edge rate / miss distance from TRACKED LOCATION** | **Yes, by construction** | **None — 100% of the sample** |
| 2. Called strikes, contaminated band (±2 in) removed | Yes | discards 28.6%, variance ×1.40 |
| 3. Within-catcher comparison only | Yes | at a 70/30 split, variance ×1.43 |

> **CONTRAST F-298**, where the unconfounded sequencing estimator cost 3–6× and **failed the season budget outright**. Here the clean estimator is **free**. That is a genuinely different situation and it should be taken advantage of.

### Detection cost (α=.05, 80% power, two-sample, 4.52-pt effect)

| Metric | taken / group | ≈ pitches | college starter-seasons |
|---|---|---|---|
| Called-strike rate (contaminated) | 1,639 | 3,177 | 2.0 |
| **Zone rate (clean)** | 1,909 | 3,700 | **2.4** |

⚠️ **Read this before celebrating.** Zone rate is **clean but not fast**. Two-plus starter-seasons to confirm a realistic one-season command gain means **you still cannot prove the gain inside the season you produced it.** The fix removes the **bias** and leaves the **noise wall** exactly where F-273, F-282, F-286 and F-295 left it.

**What you have bought is an honest number, not a fast one.**

⚠️ **Zone rate is not command.** A pitcher deliberately working off the plate has a low zone rate and may have excellent command. Use it to compare a pitcher **to himself over time at similar usage** — never to rank two pitchers.

---

## 7. ABS, and the stress test F-283 survived (F-311, F-312, F-313)

**F-283's conditional is resolved.** The SEC ran an ABS challenge system for every game of the 2026 conference tournament; the NCAA has approved one for all three divisions from 2027, optional, regular season and postseason (F-311 — corroborated across multiple independent outlets, **but no page was opened and every specific is snippet-only**).

**The pitcher is one of the three people who may challenge**, which makes this a pitcher-development item.

### The strongest objection to F-283, and why it loses

A findable 2026 arXiv paper (**2609.03786**, KBO/ABS transition — F-312) reportedly finds human umpires shrink the zone **−17.17 pp on 0-2** and expand it **+6.61 pp on 3-0**, with both vanishing under ABS. **Snippet-only; do not quote either number.**

If true, the umpire is *most wrong exactly on 0-2* — the best available argument for challenging there. Put both terms in one expression:

EV(challenge) ∝ λ(count) × P(overturn | count)

λ(3-2)/λ(0-2) = 4.74 / 0.26 = **18.2×**. So 0-2 wins only if its overturn probability exceeds 3-2's by **more than 18.2×**.

| baseline pitcher-favourable error rate in band | 0-2 rate after −17.17 pp | ratio |
|---|---|---|
| 20% | 37.2% | **1.86×** |
| 30% | 47.2% | 1.57× |
| 40% | 57.2% | 1.43× |

**Largest ratio available 1.86×. Required 18.2×. Margin ≈ 9.8×.**

> **F-283 SURVIVES. Do not burn a challenge on 0-2.**

The input would have to be wrong by a factor of ~9 *in the pitcher's favour* to reverse this; wrong by 3× changes nothing. **And the comparison is made between (0-2, 3-2) — the only two cells F-278 says are safe to quote.**

**A recommendation that has survived its best counterargument is a different object from one that has merely gone unchallenged.**

### What ABS does to the rest of this file

A **challenge** system removes framing only on **challenged** pitches — nearly all pitches are unchallenged, so §2–§6 remain fully live. **Full ABS would zero the contamination in §5 and make called-strike rate an honest pitcher statistic for the first time.** A challenge system does not.

---

## 8. What to actually do

1. **Change the column, not the equipment.** Report pitcher command as **tracked zone rate / edge rate / miss distance**, never as a called-strike statistic. You already own the data (F-310).
2. **Before believing any year-over-year command change, ask who was catching.** If the battery changed, the number is uninterpretable until you re-cut it within catcher (F-309).
3. **Put F-283's rule on a card:** never challenge on 0-2 (F-313).
4. **Hand the catcher valuation to the people who set the lineup.** ~8 runs a college season is the largest single item this corpus has priced, and it is not a pitching-coach decision (F-308).

---

## 9. The three things that would settle this

| Question | What it needs |
|---|---|
| Is f₀ right for an 85+ college arm? | One query against the program's own TrackMan: the share of taken pitches within ±1 in of the zone line. **Nobody has published this for any population.** |
| Is the catcher term really ~0.5 in? | Same log: called-strike rate on boundary-band pitches, split by catcher. **~2,500 taken pitches per catcher detects a 0.5-in difference** (F-310's arithmetic). |
| Is count composition a *larger* confound than the catcher? | **Read arXiv 2609.03786.** If −17.17 pp is real it is ~4× everything in this file (F-312). |

---

*Findings F-305 → F-314. Written 2026-09-11 in a fully blocked cycle; nothing here was verified at source.*
