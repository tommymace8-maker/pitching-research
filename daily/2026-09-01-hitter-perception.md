# 2026-09-01 — HITTER PERCEPTION AND THE TIMING BUDGET

**Topic:** what the hitter can actually see, when he commits, and what a pitcher's velocity and extension are worth *denominated in the hitter's own error budget*.

**Why this topic.** INDEX.md §5 lists "Hitter perception and reaction" under *Topics the corpus has not researched at all* — "referenced obliquely (attack angle, deception, the 150 ms tunnel-point argument) but never studied directly." This cycle studies it directly. It also lets us test a claim the corpus currently carries second-hand: F-163 records that Baseball Prospectus revised the tunnel point to **150 ms** "citing a study that the final third of the trajectory contributes nothing because required angular eye velocity exceeds physiological limits." Nobody in this program had read that study.

**Population note.** The pitchers are ours (85+ floor). **The hitters in this literature are not.** Two of the four core studies use high-school batters and one uses Japanese professionals. Where a number is a property of *bat-ball geometry* it transports reasonably; where it is a property of *skill* it does not. Flagged individually below.

---

## ⚠️ VERIFICATION STATUS OF THIS BRIEF — READ BEFORE USING ANY NUMBER

**All external fetch was blocked today.** Both WebFetch and `curl` returned proxy 403 for every domain tried, including every domain the run instructions list as working: `pmc.ncbi.nlm.nih.gov`, `frontiersin.org`, `sportrxiv.org`, `jstage.jst.go.jp`, `journals.plos.org`, `nature.com`, `tandfonline.com`, `journals.sagepub.com`, `arxiv.org`, `doi.org`, `europepmc.org`. WebSearch was the only working channel.

Under this program's own rule (`F-240 (E)`: *sample sizes are verified on the paper's own page, never from a search summary*), that means:

| Class | Status |
|---|---|
| Every empirical number attributed to a published study below | **SNIPPET-LEVEL ONLY. LEAD, NOT FINDING.** Existence of the paper is corroborated by PMID/DOI appearing across independent result sets; the *magnitudes* were not read at source. |
| The flight-time arithmetic in §3 | **COMPUTED IN-HOUSE.** Script at `/tmp/flight.py`, model and calibration stated in full. Independent of egress. This is the only fully verified content in the brief. |
| The one correction to an existing finding (§3.3, F-250) | **DERIVED, NOT CITED.** It is a reasoning correction on arithmetic already in the vault, checkable by hand. |

**Nothing in §1, §2 or §4 may be promoted to a numbered recommendation until it is read at source.** Registered as a verification backlog item in F-259.

---

## 1. THE HITTER'S TIMING BUDGET — how much error he is allowed

This is the number the corpus was missing, and it reframes everything the vault says about velocity.

**Katsumata-lineage work, Human Movement Science 2019** (PMID 31254808, DOI 10.1016/j.humov.2019.06.011; Shibaura Institute of Technology). n = 26 **high-school** batters, pitching machine, three pitch types, optical mocap of ball, bat and pelvis. Reported acceptable timing error at ball-bat impact:

| Pitch | Acceptable timing error |
|---|---|
| Fastball | **± 7.9 ms** |
| Curveball | ± 10.7 ms |
| "Slowball" | ± 10.7 ms |

Plus: optimal impact timing for **outside** pitches is ~**10 ms later** than for inside pitches.

**Frontiers in Sports and Active Living 2025** (PMID 40225202, PMC11985794) — the follow-up, and the one whose population is closest to ours. **18 pitched-ball trajectories from 10 collegiate pitchers; 145 swings from 29 collegiate batters**, combined computationally. Max ball speed **39.6 m/s = 88.6 mph** — i.e. this study sits essentially at our floor.

> Mean acceptable range of timing error **9.36 ± 6.25 ms**, and 0.227 ± 0.163 m in distance.
> **Across-hitter range: 2.48 ms to 30.40 ms** (distance 0.056–0.614 m).
> Determined by the interplay of swing trajectory from the side and from above, and bat angle at impact.

**THE HEADLINE IS NOT THE MEAN. IT IS THE SPREAD.** A twelve-fold range across collegiate hitters. Some hitters' swing paths give them a 2.5 ms window; some give them 30 ms. That is a property of *the hitter's swing path*, not of the pitch — and it means the value of a millisecond you take away from a hitter is not a constant. It is enormous against a steep, short-window swing and close to irrelevant against a flat, long-window one.

**⚠️ AN UNRESOLVED INTERNAL INCONSISTENCY I COULD NOT CHECK.** The 2025 paper's own two numbers do not reconcile at any plausible pitch speed: 0.227 m ÷ 9.36 ms = 24.3 m/s = 54 mph, but the study's max ball speed is 39.6 m/s. Either 9.36 ms is a half-width and 0.227 m a full width (or vice versa), or the two are computed along different axes, or the distance is bat-sweet-spot travel rather than ball travel. **This factor-of-two ambiguity propagates into every calculation below**, which is why §3 reports ratios against *both* readings. Resolving it requires the paper. `UNRESOLVED — REQUIRES SOURCE ACCESS.`

**Working figure adopted, provisionally: the hitter's fastball timing budget is ~±8 ms (≈16 ms wide), with an across-hitter range of roughly 2.5–30 ms.**

---

## 2. WHEN HE COMMITS — three findings that agree

### 2.1 The last 150 ms of flight is not usable — and the corpus's reason for believing it was the wrong reason

**Higuchi et al. (2016), "Contribution of Visual Information about Ball Trajectory to Baseball Hitting Accuracy," PLoS ONE 11(2):e0148498** (PMID 26848742, PMC4743964). n = 10 **college** position players, machine-launched ball, three conditions:

- **R+150** — vision occluded from 150 ms *after release* (he sees only the first 150 ms)
- **A−150** — vision occluded from 150 ms *before arrival* (he sees everything **except** the last 150 ms)
- **NO** — no occlusion

Result as reported: occlusion did **not** shift the *mean* contact location in any axis. Standardized *variability* fell from R+150 to A−150 in the bat's **short-axis** direction only — and **A−150 and NO did not differ.** Authors' conclusion: the limitation on useful visual information is the **later part of the trajectory**, "likely due to visuo-motor delay."

**This matters for the vault in two ways.**

1. **The 150 ms commit point has direct experimental support, and F-163 did not credit it.** F-163 logged the 150 ms figure as a Baseball Prospectus assertion resting on a citation. It also has an occlusion experiment behind it, from a different lab, using a different method. **The number survives; the corpus's confidence in it was too low, not too high** — a rare direction for this program.
2. **But the *mechanism* BP cited is the wrong one, and it is contradicted by its own source.** BP's stated rationale is an **angular eye-velocity limit**. That traces to **Bahill & LaRitz (1984), "Why can't batters keep their eyes on the ball?", American Scientist 72:249–253** — where the reported result is that a professional batter, combining ~120 deg/s smooth pursuit with head rotation, **tracked the ball to within about 5.5 feet of the plate.** 5.5 ft is roughly the last **30 ms**, not the last 150 ms. **The eye-tracking limit and the commit point are two different constraints and BP fused them.** The load-bearing constraint is **visuomotor delay** — the swing is already unalterable — **not** whether the eyes can follow the ball. `⚠ Both Higuchi and Bahill are SNIPPET-LEVEL today.`

**Coaching consequence of the distinction:** if the binding limit were oculomotor, "see it longer" would be trainable and worth training against. Because it is visuomotor delay, **late movement does not beat the hitter by hiding from his eyes; it beats him by arriving after his swing is committed.** Those imply different pitch-design priorities.

### 2.2 The order in which the hitter solves the problem

**Saijo, Fukuda & Kashino (2025), "The temporal structure of multiple visuomotor processes in baseball batting: insights from a virtual reality system," Frontiers in Psychology 16:1514301** (PMC11822940). NTT Communication Science Laboratories. **n = 23 batters from a Japanese professional team** — the only genuinely elite hitter sample found this cycle.

Three processes were dissociated under occlusion:

| Process | Effect of occluding late flight |
|---|---|
| **Swing timing** adjustment (to pitch speed) | **Unaffected** |
| **Swing decision** (strike/ball) | Minor decline |
| **Swing trajectory** adjustment (to plate location) | **Significant decline** |

Authors' inference: the brain computes **timing first, then the swing/take decision, then trajectory.**

**This is the most directly actionable result of the cycle.** It says the hitter's *timing solution is locked early* — from the delivery and the first part of flight — and his *spatial solution stays open latest.* Therefore:

- **A pitcher's leverage on the hitter's TIMING lives before and immediately after release.** Delivery, release consistency, and whatever makes speed unpredictable at the moment of release. Late velocity is not a thing; late *arrival relative to an early estimate* is.
- **A pitcher's leverage on the hitter's TRAJECTORY solution lives in late movement** — the part of the flight the hitter is still trying to use and least able to.
- These are **two separate attacks** and the corpus has been treating "deception" as one thing.

This is a mechanism claim from one VR study with n = 23. `EMERGING at best. Do not build a program on it this month.`

### 2.3 Perception-action coupling — a caution about how anyone tests this

**Ranganathan & Carlton (2007), Journal of Motor Behavior 39(5):369–380** (PMID 17827114). 10 expert, 10 novice batters; fastball/changeup discrimination in a virtual environment; verbal (uncoupled) vs. swinging (coupled) response, 6 visual conditions.

Reported: batters were **more accurate at naming the pitch when they did not have to swing.** In the coupled condition, experts used **the first 100 ms of ball flight** independently of pitcher kinematics; skilled batters' **stepping** tracked pitcher kinematics while their **swing time** tracked ball speed.

Two consequences. (a) **Any "pitch recognition" test that asks a hitter to call the pitch overstates what he can do while swinging** — a warning for any facility selling recognition scores. (b) The step/swing dissociation independently supports §2.2: the *early* body solution is driven by the pitcher's body, the *later* one by the ball.

---

## 3. THE ARITHMETIC — the only fully verified section

Everything here is computed in-house. Model: exponential speed decay `v(x) = v0·exp(−kx)`, calibrated so a 95 mph release arrives at ~87 mph over 54.0 ft, giving **k = 0.001629 /ft (8.4% loss)**. Distance travelled = 60.5 − extension. Script: `/tmp/flight.py`.

### 3.1 Flight time, release to front of plate (ms)

| Extension | 88 mph | 90 | 92 | 95 | 98 |
|---|---|---|---|---|---|
| 6.00 ft | 441.6 | 431.8 | 422.4 | 409.0 | 396.5 |
| 6.25 ft | 439.5 | 429.7 | 420.4 | 407.1 | 394.6 |
| 6.50 ft | 437.3 | 427.6 | 418.3 | 405.1 | 392.7 |
| 7.00 ft | 433.1 | 423.5 | 414.3 | 401.2 | 388.9 |
| 7.50 ft | 428.9 | 419.4 | 410.2 | 397.3 | 385.1 |

### 3.2 What a pitcher buys, in milliseconds

| Lever | At 95 mph / 6.5 ft | At 90 mph / 6.3 ft |
|---|---|---|
| **+1 mph** | **−4.3 ms** | **−4.8 ms** |
| **+1 ft extension** | **−7.8 ms** | **−8.3 ms** |
| +1 inch extension | −0.65 ms | −0.69 ms |

**Against a ±8 ms window: one mph is roughly half of the hitter's entire allowance on one side.** Against the *tightest* hitters (2.5 ms) a single mph is three windows. Against the widest (30 ms) it is a seventh of one.

**Note the direction of the velocity sensitivity: it is LARGER at 90 mph than at 95** (4.8 vs 4.3 ms per mph), because flight time goes as 1/v. Slower pitchers get *more* timing return per mph than faster ones. This is the opposite of the shape of the *training* return, which shrinks toward zero as baseline rises (F-025). **The two curves run opposite ways, and nobody has priced them against each other.**

### 3.3 ⚠️ REFINEMENT TO F-250 — the extension-per-foot figure comes off the wrong end of the flight

F-250 records **7.18 ms per foot** of extension at 95 mph (computed as 1 ft ÷ release speed, 139.33 ft/s), and notes that "with in-flight drag at a ~91 mph flight average the true figure is ~7.5 ms."

**Both are the wrong quantity, and the second is wrong for an instructive reason.** Releasing one foot closer to the plate does not slow the whole trajectory down by a foot's worth of *average* speed. The ball leaves the hand at the same speed and follows the same speed-vs-distance profile; what disappears is the **final** foot of the flight — the foot the ball would have covered **at its slowest, ~87 mph.**

**Correct figure: 1 ft ÷ 127.7 ft/s = 7.83 ms per foot at a 95 mph release.** The in-house model returns 7.83 ms independently.

Magnitude of the change is small (7.18 → 7.83, +9%) and **it does not alter F-250's conclusion in any way** — the scale-bar argument (1 ft ≈ 2.2 SD ≈ the whole major-league range) and the total absence of any extension intervention both stand untouched. It is logged because the *reasoning* error — pricing a change at the average rate when the change is removed from one end of the distribution — is the kind that recurs. `CORRECTED 2026-09-01. Annotated, not overwritten.`

### 3.4 Velocity separation, priced in the hitter's window

Off a 92 mph fastball at the same extension, an offspeed pitch arrives late by:

| Velocity gap | Arrives late by | ≈ half-windows (±8 ms) |
|---|---|---|
| 2 mph | 9.3 ms | 1.2 |
| **3 mph** | **14.1 ms** | **1.8** |
| 4 mph | 19.0 ms | 2.4 |
| 5 mph | 24.0 ms | 3.0 |
| 6 mph | 29.2 ms | 3.6 |
| 8 mph | 39.8 ms | 5.0 |
| 10 mph | 51.0 ms | 6.4 |
| 12 mph | 62.7 ms | 7.8 |

**THE FINDING: a 3 mph velocity gap already exceeds the average hitter's entire timing budget.** By 8 mph the ball arrives five windows late; by 12 mph, nearly eight. **Beyond roughly 4 mph, additional velocity separation is not buying timing disruption — the pitch was already unhittable-on-time, several times over.**

So what is the changeup's remaining variable? **Whether he recognises it.** Every mph of separation past ~4 is spent on a margin that is already saturated, and is *paid for* in recognisability (bigger gap = more arm-speed and shape difference to hide). **The binding constraint on an offspeed pitch is disguise, not separation.** That is consistent with the vault's corrected changeup entry (F-159/F-232), where the argued chain is velocity-gap → hitters out front → whiffs, but it prices the chain and shows where it saturates.

**Caveat the biomechanist insisted on, below.** This arithmetic assumes the hitter times the *fastball*. A hitter who correctly identifies the changeup re-times it and the entire table becomes irrelevant. **The table is the cost of being wrong, not the cost of the pitch.**

---

## 4. FIELD SWEEP — 2026-09-01

Five items. Two are genuinely new to this corpus. Sources reachable only by search this cycle, so standing is assessed but content is not source-verified.

### 4.1 ABS challenge system, live in MLB for 2026 — **PROMISING (as a signal), UNVERIFIED (as numbers)**

MLB adopted the Automated Ball-Strike **challenge** system for the 2026 season (announced Sept 2025; mlb.com press release, plus AP/NPR/CBS/Baseball America coverage). Zone: 2-D rectangle at the middle of the plate, 17 in wide, **top 53.5% and bottom 27% of batter height.**

Reported consequences, all secondary: the umpire-called zone was **more rounded and more pitcher-lenient** (top ~55.6%, bottom ~24.2%); at 2-2 the umpire zone measured **449 sq in vs 443 sq in** for ABS; edge-dependent pitchers and elite-framing batteries lost value.

**Why Tommy cares even though it is an MLB rule:** the NCAA has been trialling ABS, and *the direction of the incentive change is what matters.* If the corners stop being negotiable, the value of a pitch that "just misses" drops and the value of an in-zone pitch that misses bats rises. **That is a re-weighting of stuff over nibbling, and it is the first thing in two years that argues a pitching program should shift its command target from the black to the shadow-in.**

**⚠️ ONE CIRCULATING NUMBER IS NOT CREDIBLE AND SHOULD NOT BE REPEATED.** A fantasy-baseball piece claims hitters are "offering at pitches out of the zone 40.2 percent this season, way up from 28.2 percent a season ago." A league-wide chase rate jumping 12 points in one season is not a plausible magnitude; MLB chase has sat in the high-20s/low-30s for a decade. Most likely a mis-scoped or mislabelled split. **DO NOT IMPORT.** Verdict on the rule change: **PROMISING**. Verdict on the published effect sizes: **UNVERIFIED, and at least one is wrong.**

### 4.2 Driveline "Intended Zone Tracker" + markerless biomech, presented at 2025 SABR Analytics — **UNPROVEN (underpowered)**

Driveline projects an intended target zone onto the plate and pairs each pitch's **miss distance** with markerless-mocap biomechanics. Reported correlations with miss distance:

- Lead knee extension velocity at foot plant: **r = −0.37**
- Maximal shoulder external rotation: **r = +0.44**
- **n = 16 pitchers.**

**THE BIOMECHANIST'S KILL SHOT: at n = 16 (df = 14), the two-tailed critical r at α = .05 is 0.497. NEITHER CORRELATION REACHES SIGNIFICANCE.** r = 0.44 → p ≈ .09; r = −0.37 → p ≈ .16. These are hypothesis generators, and the 95% CI on r = 0.44 at n = 16 runs from roughly −0.07 to +0.77 — it does not exclude zero and it does not exclude "enormous."

Also unresolved from the available description: whether "maximal shoulder external rotation" here is a **mean** or a **within-pitcher variability** measure. The summary says "greater variability in this motion may lead to less accurate outcomes" while the coefficient is described against MER itself. Those are different claims. `UNRESOLVED.`

**Standing is real** — Driveline's IZT is already in the vault bibliography (`library/stuff-and-command.md`, Driveline Feb 2026, *The Interaction of Biomechanics and Command*), and IZT is the best objective command instrument in the industry. **The instrument is more valuable than this result.** Verdict: **UNPROVEN.**

### 4.3 Statcast bat tracking, second full season — **PROMISING for pitchers, largely unexploited**

League baseline: average swing **71.5 mph**, average swing length **7.3 ft**. Whiff rate on **longer-than-average swings 30%** vs **19%** on shorter-than-average.

**The connection nobody in the public space has made yet, and it is today's topic:** swing length is a proxy for the *time* the swing occupies, and §1's 2025 paper says the acceptable timing window is set by **swing path**. Bat tracking therefore exposes, per hitter and publicly, an estimate of *how wide that hitter's timing window is.* **A pitcher's velocity is worth several times more against a long-swing hitter than a short-swing one, and this is now measurable from public data.** Nobody appears to be doing it. Registered as tomorrow's question #1.

### 4.4 Adaptive VR training for hitters — **PROMISING, and it cuts against us**

**Gray, R. (2017), "Transfer of Training from Virtual to Real Baseball Batting," Frontiers in Psychology 8:2183** (PMC5733365). **n = 80 competitive high-school batters, randomised to four groups**: adaptive VR training (staircased pitch speed, location, spin), extra VR batting practice, extra real on-field BP, and no-training control.

Reported: the **adaptive** group improved significantly more than all three others, had superior in-league batting statistics, and **a significantly greater proportion reached a level of competition above high school.** Mechanism proposed: greater sensitivity to ball-flight information and improved use of **lace rotation** to identify pitch type.

**This is a randomised controlled trial with a real transfer test, and there is nothing of comparable design anywhere on the pitching side of this corpus.** The hitter-perception field has better methodology than the pitching-development field does. That is embarrassing and worth saying plainly.

**And the result is bad news for us.** **Pitch recognition is trainable in the opponent.** Deception is a depreciating asset: any edge built on the hitter failing to identify a pitch erodes as recognition training spreads. An edge built on *arrival time being unrecoverable once identified* does not. Population is HS batters — `SAMPLE MISMATCH — directional only` — and one 2017 RCT is not a literature.

### 4.5 What was searched for and NOT found

- **No study manipulating release extension and measuring hitter outcomes.** Confirms F-249/F-250's absence claim from a second direction: the gap is not just an intervention gap on the pitcher's side, it is a gap on the hitter's side too.
- **No public analysis pairing bat-tracking swing length with per-hitter timing-window width.** (§4.3.)
- **No ABS-era peer-reviewed analysis of pitch-location strategy.** Everything is 2026 in-season blogging.
- **No collegiate/professional replication of the ±7.9 ms fastball window.** The 2025 collegiate paper is a computational recombination of separately-collected pitches and swings, not batters facing pitchers.

---

## 5. THE COACH'S FOUR QUESTIONS

### Q1 (to the biomechanist): "You just told me one mph is half the hitter's error budget. Velocity is the hardest thing on earth to add. Is this a reason to chase velocity, or did you just re-describe why velocity is good?"

**Biomechanist:** Mostly the second, and I will not pretend otherwise. **The ms framing does not create a new lever; it re-denominates one we already had.** What it *does* add that the mph framing cannot: it puts velocity, extension and velocity-separation on **one axis**, so they can be traded off. That produces three things the corpus did not have — (a) 1 mph ≈ 1.8 inches of extension in timing terms, which tells you extension is nearly worthless as a substitute for velocity at any realistic magnitude (F-250's 0.1–0.3 ft ≈ 0.8–2.4 ms ≈ **a fifth of a mph**); (b) the saturation point on velocity separation at ~4 mph (§3.4); and (c) the discovery in §3.2 that per-mph timing return is *larger* at 90 than at 95 while per-mph training return is *smaller*. That third one is a genuinely open question about where in a roster a mph is worth most.

**Translation:** *So what I tell the pitcher is* — "your fastball is worth what it makes him be early or late by, and the whole window he's allowed is about the blink of one-sixtieth of a second. One mph is half of it." *The drill is* — none. This is a framing for the athlete, not a training input. *On video the failure looks like* — nothing; there is no video failure mode for a unit change. *Here's how we know it's working* — **we don't, and I am not going to pretend a re-denomination is a result.**

### Q2 (to both): "Do I stop trying to add separation to the changeup at 4 mph?"

**Biomechanist:** You stop trying to add it *for timing reasons* at about 4 mph. §3.4 is arithmetic, not an estimate: at 4 mph the ball is 19 ms late against a ±8 ms allowance. There is nothing left to win there. Past that point, separation is being bought for a **different** reason — it may still change the pitch's shape or its perceived plane — and those must be argued on their own evidence.

**Anatomist:** And the way pitchers *get* separation past 4 mph is by taking speed off the arm, which is the recognisable thing. The forearm and hand kinematics that kill 10 mph are visible; the grip-and-throw-it-hard changeup that kills 6 is not.

**Coach:** *So what I tell the pitcher is* — "stop trying to make the changeup slower. Make it look the same." *The drill is* — same-intent throws, radar hidden, alternating FB/CH in a 2:1 pattern, and I chart **arm-speed match**, not velo gap. *On video the failure looks like* — the deceleration pattern of the throwing arm after release differing between the two pitches at 240 fps, and the front side opening earlier on the changeup. *Here's how we know it's working* — this is the honest part: **I cannot measure recognition without a hitter.** The only real check is live at-bats charted for **swing rate and contact timing** (early/on/late) across **≥ 200 charted changeups**, which is 8–12 outings. A bullpen proves nothing here, because there is no hitter in it.

### Q3 (to the anatomist): "Saijo says timing is solved early and location late. Is there a physiological reason to believe that ordering, or is it one VR study?"

**Anatomist:** There is a mechanistic reason to expect *something like* it, and it is not strong enough to carry the specific ordering. **Timing a whole-body interceptive action requires a single scalar — time-to-contact — and the visual system extracts optical expansion very early and cheaply.** Spatial adjustment of a swing requires continuously updating an effector trajectory against a moving target, which is a costlier computation and one whose output can be revised until the mechanical point of no return. **So "cheap scalar first, expensive vector last" is the prediction the physiology makes,** and Saijo's ordering is consistent with it.

What I will not concede: the *timing* of the boundaries. Whether the decision closes at 150, 180 or 220 ms is a claim about **conduction plus muscle electromechanical delay plus swing duration**, and those three vary by 40–80 ms across athletes. Higuchi's ±150 ms is an occlusion boundary chosen by experimenters, not a measured commit point. **Nobody has measured a commit point in an individual hitter.**

**Coach:** *So what I tell the pitcher is* — "he's decided how fast before he's decided where. What beats him early is speed he didn't expect; what beats him late is movement." *The drill is* — nothing new; it re-prioritises what we already do, putting **release consistency between pitch types** (F-164) on the timing side and **late-breaking shape** on the trajectory side, and stopping me from calling both "deception." *On video the failure looks like* — a visibly different arm slot or release height between his fastball and his breaking ball on overlaid 240 fps frames at the release instant. *Here's how we know it's working* — **HRA overlap from Trackman across ~100 pitches of each type** (F-164's protocol, already in the vault), not a hitter outcome.

### Q4 (to both): "Gray 2017 says hitters can train recognition and it transfers. Does that make anything we do obsolete?"

**Biomechanist:** It makes one class of edge obsolete on a slow clock, and it is worth naming which. **Anything that works because the hitter cannot tell which pitch is coming is erodible.** Anything that works because the pitch is *physically difficult to intercept once correctly identified* is not. Velocity, late movement and location live in the second class. Tunnels, grip disguise and arm-speed matching live in the first.

**Anatomist:** With the caveat that Gray's group was high-school hitters with room to improve, and I would expect a much smaller effect in an SEC lineup that already recognises well.

**Coach:** I will take that trade every time, and it is a genuinely clarifying rule. *So what I tell the pitcher is* — "you can't out-hide a good hitter forever. You can out-run him." *The drill is* — a priority order, not a drill: velocity capacity first, then late shape, then disguise. *On video the failure looks like* — a pitcher whose whole plan is trickery having his third time through the order collapse. *Here's how we know it's working* — **third-time-through performance in the same season, ≥ 150 batters faced in the third pass**, which for a Friday starter is most of a year. This is a slow check and I will say so.

---

## 6. CROSS-EXAMINATION

### Challenge 1 — Biomechanist → Coach. "You are about to teach the ±8 ms number to athletes, and it comes from 26 high-school hitters."

**Claim challenged:** that ±8 ms is a usable working constant for our hitters.
**Why I doubt it:** the population is wrong twice over — high-school hitters in 2019, and a computational recombination of collegiate pitches and swings in 2025. And **the 2025 paper's own two headline numbers do not reconcile** (§1). Every one of those numbers is snippet-level today.
**What would settle it:** reading both papers at source, and specifically establishing whether the reported figure is a half-width or a full width.

**COACH CONCEDES, with a boundary.** I will not put a number on a whiteboard. What I *will* use is the **ordering** — that the window is small enough that a few mph of unexpected speed exhausts it — because that survives the factor-of-two ambiguity. Any conclusion that survives both readings is safe; any that needs the exact value waits.

### Challenge 2 — Coach → Biomechanist. "Your §3.4 table assumes the hitter times the fastball. Real hitters sit on pitches."

**Claim challenged:** that a 3 mph gap "exceeds the hitter's entire budget."
**Why I doubt it:** it is only true for a hitter whose timing estimate was formed on the faster pitch. Saijo's own result says timing is computed from *early* information — which includes the arm and the ball's first 100 ms (Ranganathan & Carlton). **If he can estimate speed early, he re-times and the table collapses.** The table's real subject is not the pitch, it is **the hitter's estimation error.**
**What would settle it:** a study measuring the *distribution of hitters' arrival-time estimation error* by pitch type. I could not find one.

**BIOMECHANIST CONCEDES — and the concession improves the finding.** The table should be read as **"the penalty for a given estimation error,"** not "the effect of a velocity gap." It is a **conversion factor**, and the thing it converts is unmeasured. §3.4 is rewritten in `library/hitter-perception.md` on those terms and F-253 is worded accordingly.

### Challenge 3 — Anatomist → Biomechanist. "Your 7.83 ms correction is a rounding argument dressed as a finding."

**Claim challenged:** that F-250's 7.18 ms is worth correcting.
**Why I doubt it:** 0.65 ms. Against a window whose across-hitter range spans 28 ms. **This changes no decision anywhere.**
**What would settle it:** nothing empirical — it is a question of whether the corpus logs sub-decision-threshold reasoning errors.

**BIOMECHANIST DEFENDS, and the coach sides with him.** The magnitude is trivial and the entry says so twice. The *reasoning* error is not trivial: **pricing a marginal change at an average rate when the change is removed from one tail.** That exact error is why the corpus once had 1.35 instead of 0.65 mph (F-072) and why F-248 exists. Per F-240(B), the corruption happens in our own compression, and the cheapest place to catch it is on arithmetic we can check by hand.

### Challenge 4 — Anatomist → Coach. "You gave Q3 a coaching translation off one VR study with n = 23."

**Claim challenged:** the timing-vs-trajectory split as a basis for prioritising anything.
**Why I doubt it:** one study, one lab, VR, n = 23, no replication. The corpus has retired cues built on more.
**What would settle it:** replication, ideally with real pitchers rather than VR.

**COACH CONCEDES that it is not a basis for a new drill — and notes that it is not being used as one.** The Q3 translation changes **no** activity. It re-labels two things already being done and stops me from calling both "deception." **A taxonomy is a much cheaper thing to be wrong about than a drill.** If Saijo fails to replicate, I have lost a vocabulary, not a training block. This is registered as an open dispute anyway (#17), because the anatomist is right that the corpus has been burned by exactly this pattern.

### Revisiting a carried-forward dispute

**Dispute #12 — "Does the velocity-optimal delivery cost command?"** — was drifting toward "the trade may be a mirage" as of 2026-08-13.

**Did today move it? Slightly, and toward the mirage reading, from a new direction.** The vault holds that velocity *variability* costs command at **~3.5 inches of vertical miss per mph** (Kusafuka sensitivity; `stuff-and-command.md` §600). Today adds that the same mph is worth **~4.3–4.8 ms** against a hitter budget of ~±8 ms. So **the same variable is a command liability and a timing weapon simultaneously**, in units that can now be compared. That does not resolve #12 — but it means the question "should he throw at a controlled velocity or an uncontrolled one" is now answerable in principle rather than only rhetorically. **Logged as new dispute #17.** No change to #12's status: still 🔴 OPEN.

---

## 7. WHAT THIS CYCLE ACTUALLY ADDS

1. **A second currency for velocity** — milliseconds of the hitter's error budget — verified by in-house arithmetic and directly comparable to the vault's existing inches-of-miss currency.
2. **A saturation point on velocity separation** at ~4 mph, with the honest caveat that the table's subject is estimation error, not the gap.
3. **The 150 ms commit point is better supported than F-163 recorded, and BP's stated mechanism for it is wrong.** A rare correction in the direction of *more* confidence.
4. **A taxonomy**: the hitter solves timing early and location late, so "deception" is two attacks, not one.
5. **A refinement to F-250** (7.18 → 7.83 ms/ft) that changes no decision and logs a recurring reasoning error.
6. **The methodological embarrassment**: the hitter-perception literature contains a 4-arm RCT with a real-world transfer test (Gray 2017, n = 80). The pitching-development literature this corpus covers contains nothing of that design at any level.

## 8. WHAT THIS CYCLE DOES NOT ADD

**No source was read today.** Everything in §1, §2 and §4 is a lead. If exactly one thing is carried forward, carry §3, because it is the only part that does not depend on a network I could not reach.

---

## TOMORROW — three questions handed forward

1. **Can per-hitter timing-window width be estimated from public bat-tracking data (swing length, swing path, attack angle), and does a pitcher's velocity actually produce larger outcome gains against long-swing hitters?** The 2025 paper says the window is set by swing path; Statcast now publishes swing path. This is computable from public data and nobody appears to have done it.
2. **Where is a mph worth most?** Per-mph *timing* return rises as velocity falls (4.8 ms at 90 vs 4.3 at 95); per-mph *training* return falls as baseline rises (F-025). Those curves cross. Where?
3. **Read the two timing-error papers at source and resolve the half-width/full-width ambiguity** (PMID 31254808 and 40225202), which is a factor of two on every number in §3.4. Also read Higuchi 2016 for the machine ball speed, which was never stated in any summary.
