# HITTER PERCEPTION AND THE TIMING BUDGET

**Created 2026-09-01.** The opponent-side reference: what the hitter can see, when he commits, and how to price a pitcher's stuff in the hitter's own units.

**Scope note.** Every other file in this library describes the athlete we are developing. **This one describes the person he is throwing at.** The population rules therefore invert: the 85 mph floor governs the *pitchers* in a study, but the *hitters* are the subject, and a high-school hitter sample is a sample-mismatch problem in exactly the same way — flagged individually.

> ## ⚠️ VERIFICATION STATE OF THIS FILE
> **Created during a cycle in which all external fetch was blocked** (WebFetch and curl alike, proxy 403 on every domain tried — see F-259). **Every empirical magnitude below is snippet-level and has not been read at source.** Paper existence is corroborated by PMID/DOI recurring across independent search result sets; magnitudes are not.
> **§3 is the exception** — it is arithmetic computed in-house with the model stated, and is independent of that failure.
> **Nothing in §1, §2 or §5 may be promoted to a numbered recommendation until read at source.** Backlog and priority order in F-259.

---

## 1. The timing budget — the hitter's error allowance

### 1.1 The numbers

| Source | Sample | Finding |
|---|---|---|
| Human Movement Science 2019 (PMID 31254808) | n = 26 **high-school** batters, machine, optical mocap of ball/bat/pelvis | Acceptable timing error at ball-bat impact: **fastball ±7.9 ms**, curveball ±10.7 ms, "slowball" ±10.7 ms. Optimal timing for **outside** pitches ~**10 ms later** than inside. |
| Front. Sports Act. Living 2025 (PMID 40225202, PMC11985794) | 18 ball trajectories from **10 collegiate pitchers** × 145 swings from **29 collegiate batters**, recombined computationally. **Max ball speed 39.6 m/s = 88.6 mph** | Mean acceptable range **9.36 ± 6.25 ms** (and 0.227 ± 0.163 m). **Across-hitter range 2.48 – 30.40 ms.** Width set by swing trajectory viewed from the side *and* from above, plus bat angle at impact. |

**Working figure: ~±8 ms on a fastball (≈16 ms wide), with an across-hitter range of roughly 2.5 – 30 ms.**

### 1.2 The headline is the spread, not the mean

A **twelve-fold** range across collegiate hitters. The width is a property of **the hitter's swing path**, not of the pitch. Therefore **a millisecond taken from a hitter is not worth a constant amount.** It is large against a steep, short-window swing and close to irrelevant against a flat, long-window one.

This is the first quantity in the corpus that prices a pitcher's stuff **against a named opponent** rather than against a league average. Everything else in `stuff-and-command.md` is league-relative.

### 1.3 The ambiguity that has to be resolved before any of this is quoted

The 2025 paper's own two headline numbers do not reconcile: **0.227 m ÷ 9.36 ms = 24.3 m/s = 54 mph**, against a stated maximum ball speed of 39.6 m/s. Possible explanations — one is a half-width and the other a full width; they are measured along different axes; the distance is bat-sweet-spot travel rather than ball travel. **Cannot be resolved without the paper. This is a factor of two on everything in §3.4.**

**RULE ADOPTED: use only conclusions that survive both readings.** The ordering statement — *a few mph of unexpected speed exhausts the window* — survives. Any statement needing the exact value waits.

### 1.4 Useful conversions

At a plate speed of ~87 mph (127.7 ft/s = 1,532 in/s):

- **1 ms of timing error ≈ 1.5 inches of ball travel.**
- A ±8 ms window ≈ ±12 inches of ball travel, ~24 in total.
- The 2019 outside-vs-inside result (+10 ms) is the *timing* statement of a spatial fact the corpus already holds.

---

## 2. When he commits

### 2.1 Two constraints the industry fuses, and which is load-bearing

| | **Oculomotor limit** | **Visuomotor limit** |
|---|---|---|
| Question | Can the eye still follow the ball? | Can new information still change the swing? |
| Evidence | Bahill & LaRitz (1984), *Am. Scientist* 72:249–253 — a professional, combining ~120 deg/s smooth pursuit with head rotation, tracked the ball **to within ~5.5 ft** of the plate (≈ the last **43 ms**). Batters also saccade to a predicted contact point and let the ball catch up. | Higuchi et al. (2016), *PLoS ONE* 11(2):e0148498 — occlusion experiment, below. |
| Binds at | Very late, and weakly | **~150 ms out** |
| **Load-bearing?** | No | **Yes** |

**Baseball Prospectus's revision of the tunnel point to 150 ms cites the *first* constraint** (F-163: "required angular eye velocity exceeds physiological limits"). **That rationale is wrong, and is contradicted by the very source it traces to** — Bahill's professional tracked to 5.5 ft, which is the last ~43 ms, not the last 150.

**But the 150 ms number itself is fine, and F-163 under-credited it** — see §2.2. *This is a correction in the direction of more confidence, which is the opposite direction from all six corrections in F-240, and should be re-checked rather than gratefully accepted.*

**Why the distinction changes pitch design:** if the limit were oculomotor, "see it longer" would be trainable and worth attacking. Because it is **visuomotor delay**, **late movement does not beat the hitter by hiding from his eyes — it beats him by arriving after his swing is committed.**

### 2.2 The occlusion experiment

**Higuchi et al. (2016), PLoS ONE 11(2):e0148498** (PMID 26848742 / PMC4743964). n = **10 college** position players, machine-launched ball. *Machine ball speed not stated in any available summary — outstanding.*

| Condition | What he sees |
|---|---|
| **R+150** | Only the **first** 150 ms after release |
| **A−150** | Everything **except** the last 150 ms |
| **NO** | Everything |

Results: occlusion did **not** shift the **mean** contact location in any axis. Standardized **variability** fell from R+150 to A−150 in the bat's **short axis** only — and **A−150 did not differ from NO**. Authors: the limitation on useful visual information is the later part of the trajectory, "likely due to visuo-motor delay."

**Read carefully: this is not "vision doesn't matter after 150 ms of flight."** It is "vision in the **final** 150 ms adds nothing detectable, while vision between 150 ms after release and 150 ms before arrival **does**." The middle of the flight is where the hitter's remaining information comes from.

### 2.3 The order the hitter solves the problem in

**Saijo, Fukuda & Kashino (2025), Front. Psychol. 16:1514301** (PMC11822940), NTT Communication Science Laboratories. **n = 23 batters from a Japanese professional team** — the only genuinely elite hitter sample in this file.

| Process | Effect of occluding late flight |
|---|---|
| Swing **timing** adjustment (to pitch speed) | **Unaffected** |
| Swing **decision** (strike/ball) | Minor decline |
| Swing **trajectory** adjustment (to plate location) | **Significant decline** |

Inference: **timing first, then the swing/take decision, then trajectory.**

**Independent corroboration from a different lab and method** — Ranganathan & Carlton (2007), *J. Motor Behav.* 39(5):369–380 (PMID 17827114), 10 expert + 10 novice batters, VE fastball/changeup discrimination, 6 visual conditions: skilled batters' **stepping** patterns tracked **the pitcher's kinematics**, while their **swing time** tracked **ball speed**. Same early-body / late-ball dissociation.

**The anatomist's mechanism, which is why the ordering is plausible at all:** timing a whole-body interceptive action requires a single **scalar** (time-to-contact, extracted early and cheaply from optical expansion); trajectory adjustment requires a continuously updated **effector vector** against a moving target, which is expensive and revisable until the mechanical point of no return. *Cheap scalar first, expensive vector last.*

**What is NOT established:** the boundaries. Whether the decision closes at 150, 180 or 220 ms depends on conduction delay + electromechanical delay + swing duration, which vary 40–80 ms across athletes. **Nobody has measured a commit point in an individual hitter.** Higuchi's 150 ms is an experimenter-chosen occlusion boundary, not a measurement.

### 2.4 A methodological warning for anyone buying a "pitch recognition" score

Ranganathan & Carlton also found batters were **more accurate at naming the pitch when they did not have to swing** than when they did. **Any recognition test that asks a hitter to call the pitch overstates what he can do while swinging.** Applies directly to recognition products sold to hitters — and to any claim about how well hitters "pick up" a pitch.

---

## 3. The arithmetic — the verified part

Model: `v(x) = v0·exp(−kx)`, calibrated so a 95 mph release arrives ~87 mph over 54.0 ft → **k = 0.001629 /ft (8.4% loss)**. Distance = 60.5 − extension. Computed in-house 2026-09-01.

### 3.1 Flight time, release to front of plate (ms)

| Extension | 88 mph | 90 | 92 | 95 | 98 |
|---|---|---|---|---|---|
| 6.00 ft | 441.6 | 431.8 | 422.4 | 409.0 | 396.5 |
| 6.25 ft | 439.5 | 429.7 | 420.4 | 407.1 | 394.6 |
| 6.50 ft | 437.3 | 427.6 | 418.3 | 405.1 | 392.7 |
| 7.00 ft | 433.1 | 423.5 | 414.3 | 401.2 | 388.9 |
| 7.50 ft | 428.9 | 419.4 | 410.2 | 397.3 | 385.1 |

### 3.2 Sensitivities

| Lever | At 95 mph / 6.5 ft | At 90 mph / 6.3 ft |
|---|---|---|
| **+1 mph** | −4.31 ms | −4.82 ms |
| **+1 ft extension** | −7.83 ms | −8.27 ms |
| +1 inch extension | −0.65 ms | −0.69 ms |

**Exchange rate: 1 mph ≈ 1.8 inches of extension.** At F-250's realistic individual extension change of 0.1–0.3 ft, **extension is worth 0.8–2.4 ms — about a fifth of a mph.** Extension is not a substitute for velocity at any achievable magnitude.

**Note the direction:** per-mph timing return is **larger at 90 than at 95** (flight time goes as 1/v), while per-mph *training* return **shrinks** as baseline rises (F-025). **The two curves run opposite ways and nobody has priced them against each other.**

### 3.3 The correction to F-250

F-250 gives **7.18 ms/ft** (1 ft ÷ release speed) and suggests ~7.5 ms with drag at a flight-average speed. **Both are the wrong quantity.** Moving the release point 1 ft closer removes the **final** foot of the flight — covered at the ball's **slowest** speed, ~87 mph. **Correct: 1 ÷ 127.7 ft/s = 7.83 ms/ft.** +9%, changes no conclusion. Logged because the reasoning error (pricing a marginal change at an average rate when it is removed from one tail) recurs — cf. F-072, F-248.

### 3.4 Velocity separation, priced in the window

Off a 92 mph fastball, same extension:

| Gap | Arrives late by | ≈ half-windows (±8 ms) |
|---|---|---|
| 2 mph | 9.3 ms | 1.2 |
| **3 mph** | **14.1 ms** | **1.8** |
| 4 mph | 19.0 ms | 2.4 |
| 5 mph | 24.0 ms | 3.0 |
| 6 mph | 29.2 ms | 3.6 |
| 8 mph | 39.8 ms | 5.0 |
| 10 mph | 51.0 ms | 6.4 |
| 12 mph | 62.7 ms | 7.8 |

**READ THIS TABLE CORRECTLY OR NOT AT ALL.** It is **not** "the effect of a velocity gap." It is **the penalty for a given arrival-time estimation error.** A hitter who correctly identifies the changeup **re-times it** and the table is irrelevant. **The table is the cost of being wrong, not the cost of the pitch** — and the distribution of hitters' estimation error by pitch type is **unmeasured** (searched for 2026-09-01, not found).

**With that read, the conclusion holds: beyond ~4 mph, additional velocity separation buys no further timing disruption.** The margin is saturated several times over, and separation past that point is *paid for* in recognisability — the kinematics that remove 10 mph are visible; the ones that remove 6 are not. Consistent with, and a pricing of, the corrected changeup chain in F-232.

---

## 4. The two classes of pitching edge

The most portable output of this file. From Gray (2017) — see §5.1 — pitch recognition is **trainable in the opponent**.

| Class | Works because… | Erodes as hitters train? | Examples |
|---|---|---|---|
| **A — Erodible** | the hitter cannot tell what is coming | **Yes** | tunnels, grip disguise, arm-speed matching |
| **B — Not erodible** | the pitch is physically hard to intercept **once correctly identified** | **No** | velocity, late movement, location |

**Priority order that follows: velocity capacity first, then late shape, then disguise.**

Caveat: Gray's group were high-school hitters with room to improve; expect a smaller effect in a lineup that already recognises well.

**And the timing/trajectory split (§2.3) says "deception" is two attacks, not one:**

| Attack | Lives | Measured by |
|---|---|---|
| **Timing** | before and immediately after release — delivery, release consistency between pitch types, anything making speed unpredictable at release | HRA overlap from Trackman, ~100 pitches of each type (F-164's existing protocol) |
| **Trajectory** | in **late movement** — the part of flight the hitter is still using and least able to | pitch-shape metrics already in `stuff-and-command.md` |

---

## 5. The hitter-side intervention literature — better than ours

### 5.1 Gray (2017) — a four-arm RCT with a real transfer test

**Gray R (2017), "Transfer of Training from Virtual to Real Baseball Batting," Front. Psychol. 8:2183** (PMC5733365). **n = 80** competitive **high-school** batters, randomised to four groups:

1. **Adaptive** VR batting training (staircased pitch speed, location, spin rate)
2. Extra VR batting practice
3. Extra on-field real batting practice
4. No-training control

Reported: the **adaptive** group improved significantly more than all three others, had superior in-league batting statistics, and **a significantly greater proportion reached a level of competition above high school.** Proposed mechanism: greater sensitivity to ball-flight information, and improved use of **lace rotation** to identify pitch type. *No effect sizes available from any summary.*

**Say this plainly: this is a randomised four-arm trial with a real-world transfer test, and the pitching-development literature this corpus covers contains nothing of that design at any level** (F-023, F-038). The opponent's side of the sport has better methodology than ours does.

### 5.2 What was searched for and not found (2026-09-01)

- **No study manipulating release extension and measuring hitter outcomes.** Confirms F-249/F-250's absence claim from the hitter side too.
- **No public analysis pairing bat-tracking swing length or swing path with per-hitter timing-window width.**
- **No ABS-era peer-reviewed analysis of pitch-location strategy.**
- **No collegiate or professional replication of the ±7.9 ms fastball window** with batters actually facing pitchers (the 2025 paper recombines separately collected pitches and swings).
- **No measured commit point in an individual hitter, at any level.**
- **No distribution of hitters' arrival-time estimation error by pitch type** — the quantity §3.4 actually needs.

---

## 6. What a coach does with this file

1. **Do not put ±8 ms on a whiteboard.** Use the ordering, not the value (§1.3).
2. **Stop chasing changeup separation past ~4 mph.** Chart arm-speed match, not velo gap. Check with ≥ 200 charted changeups in live at-bats (8–12 outings) scored for swing rate and contact timing — **a bullpen cannot test this, because there is no hitter in it.**
3. **Stop calling two different things "deception."** Timing attack ≠ trajectory attack (§4).
4. **Priority order: velocity, then late shape, then disguise** — because the first two do not erode and the third does (§4).
5. **Say the honest thing about the ms framing:** it re-denominates velocity, it does not create a lever. Its value is that it makes velocity, extension and separation comparable on one axis.

---

## Bibliography

- **Higuchi T, et al. (2016).** *Contribution of Visual Information about Ball Trajectory to Baseball Hitting Accuracy.* PLoS ONE 11(2):e0148498. PMID 26848742 / PMC4743964. `SNIPPET-LEVEL`
- **Bahill AT, LaRitz T (1984).** *Why can't batters keep their eyes on the ball?* American Scientist 72:249–253. `SNIPPET-LEVEL`
- **Saijo N, Fukuda S, Kashino M (2025).** *The temporal structure of multiple visuomotor processes in baseball batting: insights from a virtual reality system.* Front Psychol 16:1514301. PMC11822940. `SNIPPET-LEVEL`
- **Ranganathan R, Carlton LG (2007).** *Perception-Action Coupling and Anticipatory Performance in Baseball Batting.* J Mot Behav 39(5):369–380. PMID 17827114. `SNIPPET-LEVEL`
- **(2019).** *Acceptable timing error at ball-bat impact for different pitches and its implications for baseball skills.* Human Movement Science. PMID 31254808, DOI 10.1016/j.humov.2019.06.011. Shibaura Institute of Technology. `SNIPPET-LEVEL — first author not confirmed`
- **(2025).** *Acceptable range of timing error at bat-ball impact in baseball depends on the bat swing path.* Front Sports Act Living. PMID 40225202 / PMC11985794. `SNIPPET-LEVEL — first author not confirmed`
- **Gray R (2017).** *Transfer of Training from Virtual to Real Baseball Batting.* Front Psychol 8:2183. PMC5733365. `SNIPPET-LEVEL`
- **MLB (2025–2026).** ABS Challenge System announcements and 2026 in-season coverage; Baseball-Reference ABS challenge tracker. `SECONDARY — effect sizes unreliable, see F-257`
- **Driveline / SABR Analytics 2025.** Intended Zone Tracker + markerless biomechanics, n = 16. `SNIPPET-LEVEL — underpowered, see F-258`
