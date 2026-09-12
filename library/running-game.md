# The Running Game — holding runners, time to plate, and the one lever this corpus can actually measure

**Created 2026-09-12.** Cycle 11. **EIGHTH consecutive fully egress-blocked cycle** — `WebFetch` returns an explicit `{"error_type":"EGRESS_BLOCKED"}` for every host including `en.wikipedia.org` as a control, and raw `curl` fails CONNECT with a 403 from the gateway. **No primary source was opened.** Everything below marked DERIVED is closed-form arithmetic computed in-cycle; everything marked REPORTED is snippet-level and is a lead, not a finding.

Findings registered from this file: **F-315 → F-325.**

> ## WHY THIS TOPIC, AND WHY IT IS DIFFERENT FROM EVERY OTHER TOPIC IN THE CORPUS
>
> Eight cycles have now produced the same shape of answer: the effect is real, it is worth about a run, and **you will never be able to prove you changed it.** F-273 (60,000 pitches), F-282 (17 seasons), F-286 (790 seasons), F-295 (3,832–245,277 pitches), F-310 (2.4 starter-seasons). The corpus has a detection wall and every topic runs into it.
>
> **The running game is the first topic that does not.** A pitcher's time to the plate is detectable at **five stopwatch readings** (§5). The reason is structural and worth stating in general form: every other quantity in this corpus is an **outcome** — run value, wOBA, a called strike — whose variance is dominated by hitters, umpires, fielders and luck. **Time to plate is not an outcome. It is the lever itself, measured directly, in the units it is changed in.** That is the whole reason the wall disappears, and it is a template for what a blocked cycle should hunt for.
>
> ⚠️ **And the sting in the tail: the wall does not disappear for the topic, only for the lever.** The attempt rate against him needs ~121 opportunities (2–3 seasons) and the success rate against him needs ~400 attempts (13–40 seasons). **Everything downstream of the stopwatch is as unmeasurable as ever** (§5.3).

---

## 1. The margin model — the whole topic is one subtraction

A steal of second is decided by a single quantity:

**M = T_runner − ( T_plate + T_pop )**

- **T_runner** — from the runner's first movement to his hand on the bag.
- **T_plate** — from the pitcher's first movement to the ball in the catcher's mitt.
- **T_pop** — from the ball hitting the mitt to the ball reaching the fielder's glove at second.

M > 0 is safe. Everything anyone says about holding runners is a claim about one of those three terms, and **the pitcher owns exactly one of them.**

### 1.1 The table (DERIVED; inputs REPORTED and bracketed)

Benchmark inputs, **snippet-level from coaching grey literature and not verified at any source**: average T_plate 1.3–1.5 s, a quick pitcher 1.1–1.29 s; runners look to go against 1.35 s and above; a runner reaching second in 3.2–3.8 s "has a good shot." Catcher pop times ~1.90 (plus) / 2.00 (average) / 2.10 (below), reconstructed, not read.

Margin in seconds, against an **average 2.00 pop time**:

| T_plate → | 1.20 (slide) | 1.30 (quick) | 1.40 (average) | 1.50 (slow) |
|---|---|---|---|---|
| **Elite runner 3.30** | +0.10 | 0.00 | −0.10 | −0.20 |
| **Good runner 3.45** | +0.25 | +0.15 | +0.05 | −0.05 |
| **Average runner 3.60** | +0.40 | +0.30 | +0.20 | +0.10 |

**Read the row, not the cell.** The entire operating range of the topic — elite runner to average runner, slide step to slow delivery — spans **0.60 seconds**, and the pitcher controls **half of it**.

### 1.2 The conversion that makes it coachable: seconds ↔ feet of lead

A runner arrives at second at roughly 25–28 ft/s. The marginal foot of lead is a foot he does not have to cover at that speed:

**1 foot of lead ≈ 0.036–0.040 s. 0.10 s of delivery time ≈ 2.5–2.8 feet of lead.**

This is pure kinematics and depends on nothing but his top speed. Two consequences:

1. **The gap between a 1.45 and a 1.25 delivery is worth about 5.4 feet of lead.** No quantity of pickoff throws takes five feet off a good baserunner.
2. It gives the pitcher a unit he can feel. "Two tenths" is abstract. "You are giving him five feet before he moves" is not.

---

## 2. Margin → probability, and why the slope is so steep

P(safe) = Φ(M / σ_M), where σ_M is the SD of the margin: jump quality, throw accuracy, tag, footwork, and the pitcher's own pitch-to-pitch variation. σ_M is **not known** — bracketed 0.15–0.30 s.

**Points of safe-rate per 0.1 s of delivery time (DERIVED):**

| σ_M | at the 50% point | at a realistic 78% operating point |
|---|---|---|
| 0.15 s | 26.6 pts | 19.7 pts |
| 0.20 s | 19.9 pts | 14.8 pts |
| 0.25 s | 16.0 pts | 11.8 pts |
| 0.30 s | 13.3 pts | 9.9 pts |

**A tenth of a second is worth roughly 10–20 points of stolen-base success rate.** That is a very large number by this corpus's standards, and it is the reason the topic *feels* enormous in a dugout.

⚠️ **BUT SEE §4. It is not what actually happens, because the runner chooses.**

---

## 3. What a stolen base is worth — and the ratio that survives not knowing

### 3.1 Run values (ONE UNVERIFIED EMPIRICAL INPUT, bracketed)

A caught stealing is built from this corpus's own F-270 table — an in-play out is **−0.270 runs** — plus the value of removing a runner from first, reconstructed at **0.15–0.20 runs**. So CS ≈ **−0.42 to −0.47**. A stolen base ≈ **+0.15 to +0.20**. Neither was read from a page; both are bracketed everywhere they are used, exactly as F-280 handled the walk-minus-strikeout gap.

### 3.2 The break-even success rate — an F-307-class result

**Break-even p\* = |CS| / (|CS| + SB).**

Across the **entire** input bracket — every combination of SB ∈ {0.15, 0.175, 0.20} and CS ∈ {0.42, 0.44, 0.47} — p\* lands between **67.7% and 75.8%**, and at the centre of the bracket it is **71.5%**.

This is the same species of result as F-307's σ_u cancellation: **a ratio that survives not knowing either of its inputs well.** Both run values are unverified, both are bracketed ±15%, and the answer moves by eight points. **Say "about seventy percent." Never quote a decimal.**

### 3.3 The consequence nobody says out loud

Because league success rates sit *just above* the break-even, **an individual stolen-base attempt is worth almost nothing to anybody.** EV to the offence, per attempt, at SB = +0.175 / CS = −0.44:

| Success rate | EV per attempt |
|---|---|
| 0.65 | **−0.040 R** |
| 0.70 | −0.010 R |
| 0.72 | +0.003 R |
| 0.78 | +0.040 R |
| 0.85 | +0.083 R |
| 0.90 | +0.114 R |

**At league-average success an attempt is worth four hundredths of a run.** The running game is loud, it is emotional, it is the thing a dugout yells about — and one attempt is worth less than a tenth of what a single walk costs.

---

## 4. ⚠️ THE ENDOGENEITY — the value of a quick delivery is invisible in the column everyone reads

The table in §2 assumes the runner goes regardless. He does not. **He goes when the margin is favourable**, which means a pitcher who takes 0.2 s off his delivery does not mostly produce *failed* steals — he produces *unattempted* ones. The runners who would have been thrown out never leave first base.

**So the improvement shows up in the ATTEMPT column, not the SUCCESS column, and a pitcher who fixes his delivery may see his stolen-base success rate against barely move — or rise, because only the fastest runners still try.**

This is the fifth appearance of the same structure in this corpus, and by now it should be a standing expectation rather than a surprise:

- F-094 — between-athlete vs within-athlete associations diverge.
- F-269 / F-299 — at an optimum the *more used* option looks *better*, not worse.
- Dispute #20b — strike probability is a move in a game, not a coin.
- F-309 — the catcher's contribution is bias, not noise, because assignment is not random.
- **Here — the success rate against a pitcher is conditioned on a decision the opponent makes after observing him.**

**A pitcher's stolen-base success-rate-against is a selected statistic and must never be used to evaluate him.** Use the stopwatch.

---

## 5. What the season is actually worth, and the trade against velocity

### 5.1 Season price (DERIVED; inputs bracketed)

Scenario: the same pitcher, same catcher, slow delivery (~1.45 s) versus quick (~1.25 s). Attempts against and success rate both fall.

| Attempts / success BEFORE | AFTER | Runs allowed to the running game | **Saved** |
|---|---|---|---|
| 30 @ .82 | 15 @ .74 | +1.93 → +0.23 | **1.70 R** |
| 22 @ .80 | 12 @ .72 | +1.14 → +0.03 | **1.11 R** |
| 15 @ .78 | 9 @ .71 | +0.60 → −0.03 | **0.63 R** |
| 10 @ .78 | 6 @ .71 | +0.40 → −0.02 | **0.42 R** |

**The entire running game against one college starter, fixed from slow to quick, is worth roughly 0.4 to 1.7 runs a season.**

**Where that sits on this corpus's own ladder, per college season:**

| Item | Runs |
|---|---|
| 0-2 waste-pitch argument (F-280) | ~0.2 |
| Times through the order, whole question (F-288) | ~1.0 |
| **Holding runners, slow → quick (this file)** | **~0.4–1.7** |
| Exploited sequencing tendency (F-296) | 0.8–6.4 |
| Half an inch of catcher framing (F-308) | ~8 |

⚠️ **The attempts-against figures are ASSUMED, not measured.** The corpus holds no NCAA stolen-base rate. The ordering is the output; the cells are not — the same discipline as F-269, F-278, F-296 and F-308.

### 5.2 The velocity trade, and why it cannot be settled in general but CAN be settled for one athlete

The quick delivery is only free if it costs no velocity. Break-even velocity cost, given that the slide step is used **only** with a runner on first (12–25% of plate appearances) over a ~90-inning season:

| Share of PA affected | Runs per mph per 9 IP | Prize 0.5 R | Prize 1.0 R | Prize 1.5 R |
|---|---|---|---|---|
| 0.12 | 0.15 | 2.78 mph | 5.56 | 8.33 |
| 0.12 | 0.25 | 1.67 | 3.33 | 5.00 |
| 0.18 | 0.25 | 1.11 | 2.22 | 3.33 |
| 0.18 | 0.40 | 0.69 | 1.39 | 2.08 |
| 0.25 | 0.25 | 0.80 | 1.60 | 2.40 |
| 0.25 | 0.40 | **0.50** | 1.00 | 1.50 |

**The break-even sits between 0.5 and 5.6 mph, centred near 2 mph.** At the optimistic end the slide step is nearly free money; at the pessimistic end a half-mph cost already loses. **The general question has no general answer**, and anyone who tells you the slide step is always worth it, or never worth it, is quoting a corner of this table.

**But the individual question has an individual answer, and it takes one bullpen — see §5.4.**

### 5.3 The detection ladder, with the new entries in place

n required, α = .05, 80% power:

| What | Requirement |
|---|---|
| **Time to plate, 0.15 s change, stopwatch (σ = 0.08 s)** | **5 pitches per condition** |
| **Slide-step velocity cost, 1.0 mph (σ = 1.2 mph)** | **~23 fastballs per condition** |
| Sequence tendency, 20 points (F-295) | ~47 observations |
| **Attempt-rate drop .30 → .15 (this file)** | **~121 opportunities ≈ 2–3 seasons** |
| Command gain 4.52 pts via zone rate (F-310) | ~3,700 pitches ≈ 2.4 seasons |
| **Success-rate drop .80 → .72 (this file)** | **~400 attempts ≈ 13–40 seasons** |
| Sequencing FIX (F-295) | 3,832–245,277 pitches |
| Mix-change outcome (F-273) | 60,000+ pitches |
| Count-targeted 3-2 gain (F-282) | ~17 seasons |
| One pitcher's own TTOP (F-286) | ~790 seasons |

**Five pitches against 3,700 (F-310) is a factor of 740. Against 60,000 (F-273) it is a factor of 12,000.**

**The general principle, stated plainly:** detectability is set by the ratio of the effect to the variance of the quantity you measure. This corpus keeps hitting a wall because it keeps measuring **outcomes** whose variance is dominated by other people. The stopwatch measures the **lever**. Where the lever and the measurement are the same physical quantity, the wall is not there.

### 5.4 THE ONE THING TO RUN THIS WEEK

**One bullpen. Two blocks. Both sides of the trade, with real confidence intervals, in forty minutes.**

- **25 fastballs from his normal stretch**, radar on, two hand-timers on every pitch (first movement → mitt).
- **25 fastballs from the quick delivery** he would actually use, same conditions.
- Compare. **5 timings settles the delivery-time question; 23 fastballs settles the 1-mph velocity question.** You have 25 of each, so both are powered.
- Decision rule, straight from §5.2: **if the quick delivery costs under ~1 mph, take it. If it costs more than ~2 mph, do not — buy the run somewhere else.** Between 1 and 2, it is a genuine judgement call and the table above tells you which way your own park, catcher and opponents push it.

⚠️ **Two hand-timers, not one.** Hand timing carries ~0.03–0.05 s of its own error, which is a meaningful fraction of a 0.15 s effect. Average two operators, or use the video frame count at 240 fps (F-204, F-205).

⚠️ **Velocity is not the only cost.** Command may also move, and §5.2 prices only mph. Track strike rate as a flag, but do **not** try to conclude anything from it — F-310 says a real command change needs 2.4 seasons, and one bullpen tells you nothing.

---

## 6. The pickoff, and the rule that goes on the card

### 6.1 The third disengagement is a 14–28× losing play (DERIVED)

Under a two-disengagement limit — proposed as an NCAA conference experiment, and live in MLB since 2023 — **the third disengagement is a balk unless the pickoff records an out.** The EV is then a straight comparison:

- Pickoff records an out → worth the value of a caught stealing, ≈ **+0.44 R** to the defence.
- Anything else → balk, runner to second, ≈ **+0.175 R** to the offence.

**Break-even P(pickoff out) = 0.175 / (0.44 + 0.175) = 28.5%** (27.3–29.4% across the whole run-value bracket).

Pickoff throws record an out on the order of **1–2%**. The third disengagement therefore **loses by a factor of 14 to 28.**

> ### THE CARD RULE
> **Never make the third disengagement unless the pickoff is essentially certain — a broken-down runner, a busted double-steal, a man who has already fallen.** Not "rarely." Not "think about it." The required success rate is twenty times what a pickoff throw actually achieves.

This is the same genre as F-283 ("never burn a challenge on 0-2"), and its margin — 14–28× — is comparable to F-313's 9.8×. It is a derived rule whose inputs would have to be wrong by more than an order of magnitude to reverse.

### 6.2 The ordinary pickoff throw is close to worthless, and its whole case is unmeasured

Ignoring the disengagement limit: a pickoff throw is P(out) ≈ 1–2% × 0.44 R ≈ **+0.007 R**, minus a throwing-error risk of similar order. **The direct EV is approximately zero.**

The entire argument for throwing over is the **deterrence channel** — that it shortens the lead and slows the jump. §1.2 prices that: **1 foot of lead is 0.037 s**, so a throw that takes a foot off buys the same as 0.037 s of delivery time. Plausible. **And completely unmeasured — nobody has published a lead-length response to pickoff attempts for any population.** Registered as a gap (F-324) and as Dispute #24.

---

## 7. What the literature actually contains — and the sample it comes from

**There is essentially one peer-reviewed slide-step velocity comparison in circulation, and it is 9 mph below this program's floor.**

**Vasiliadis / Escamilla-lineage, "Shoulder kinematics during pitching: comparing the slide step and traditional stretch deliveries," PMID 22487194, ScienceDirect S0167945712000097 (2012).** Reported: **88 pitches, 10 pitchers (6 collegiate, 4 high school), mean age 17.60 ± 2.63 years**, ball velocity **76.2 ± 5.3 mph** (traditional stretch) versus **74.5 ± 4.7 mph** (slide step).

Four things follow, and they matter more than the number:

1. **SAMPLE MISMATCH — directional only.** Mean age 17.6 and mean velocity 76 mph. This is not an 85+ population; it is not even close. **"The science says the slide step costs 1.7 mph" is a statement about a sample of ten teenagers.**
2. **It is nonetheless one of the rare MANIPULATED comparisons in this corpus.** Same pitchers, both deliveries, within-subject. Unlike stride length (F-043/F-044/F-045) or open pelvis (F-049), delivery style was actually *changed* and the result *measured*. **Delivery time is a lever, not a marker** — but the magnitude of its cost is established only in a sample that does not apply.
3. **We do not know whether the 1.7 mph difference was tested, or what the paired SD was.** The snippet reports two descriptive means. At n = 10 with between-subject SD ≈ 5 mph, an unpaired test of 1.7 mph is nowhere near significance; a paired test might be. **This is a descriptive difference of unknown reliability and must not be quoted as "the slide step costs 1.7 mph."**
4. **The study's own reported result argues against its own headline.** It reports **no differences between deliveries at front foot contact or at ball release** — differences appeared only at maximum external rotation. **F-088 is explicit that foot contact is where the delivery is decided.** If the two deliveries are kinematically indistinguishable at the landmark that decides the pitch, the corpus's own framework predicts the velocity cost should be small.

**And the strongest prior we have points the same way: F-069.** Wind-up and stretch produce statistically similar velocity and kinematics in professionals, replicated (Fleisig 2024; Escamilla 2026 dirt-mound replication). Removing the entire wind-up — a far larger kinematic subtraction than shortening a leg lift — costs professionals nothing. **The prior on "the slide step costs an elite arm 2–4 mph" should therefore be low, and the folklore figure should be treated as folklore.**

⚠️ **The counter-argument, which is real (Dispute #24).** Wind-up → stretch changes what happens *before* the leg lift. Slide step → changes the leg lift *itself* and compresses the time into foot contact. Those are different operations and the F-069 prior may not transfer. **Nobody has measured it at 85+. The pitcher in front of you can, in one bullpen (§5.4), which is more than the literature offers.**

**Grey-literature claims, recorded as FOLKLORE:** "most lose 1–2 mph, and if you lose 4 the issue is sequencing"; "2–4 mph versus a full leg kick"; "the slide step reduces delivery time by 0.2–0.4 s." **No sample size appears with any of them.** The 0.2–0.4 s figure is consistent with §1.1 and is the only one worth carrying, as a range.

---

## 8. Rules — what is actually in force (REPORTED, SNIPPET-ONLY)

⚠️ **Verify every line of this with compliance before acting on it. No page was opened.** Same posture as F-311.

- **In force in NCAA since 2023:** with runners on, the pitcher must begin the motion of a pitch or a pickoff to avoid an action-clock violation, and is **allowed one step-off or fake throw per batter to reset the clock.**
- **Proposed, as a conference-level experiment across all three divisions:** **two disengagements per batter, with a third disengagement a balk unless the pickoff records an out.** Reported as approved for experimentation in the 2026-27 academic year — **the "approved" framing is summary-level, not quoted, and falls under the F-284/F-293 rule.**
- **MLB, since 2023:** two disengagements per plate appearance, third is a balk unless it records an out.
- **MiLB, new for 2026:** **Double-A cuts the limit from two disengagements to one.** Reported as expected to increase stolen bases sharply, because a pitcher who has spent his single disengagement cannot contest the lead at all.

**Why this section belongs in a pitching file rather than a rulebook:** the disengagement limit converts holding runners from a *skill the pitcher exercises during the plate appearance* into a *resource he spends*. §6.1 prices the last unit of that resource at 14–28× against. **If the one-disengagement rule moves upward from Double-A, the pickoff throw is finished as a tactic and the delivery clock becomes the only instrument the pitcher has left.** That is the direction the whole topic is moving.

---

## 9. Who actually owns the running game — pitcher or catcher?

**REPORTED:** Baseball Savant now publishes a **pitcher running-game-prevention** leaderboard (first-to-second attempts with no other runners), and the accompanying write-up states that **a pitcher's quickness to the plate is more influential than a catcher's arm.** Snippet-only; the page was not opened.

**DERIVED, by a wholly different route.** Both terms enter the margin in §1 additively and with equal weight, so their relative importance is just the relative spread across players:

| SD(T_plate) | SD(T_pop) | SD ratio | Pitcher's share of controllable variance |
|---|---|---|---|
| 0.08 | 0.06 | 1.33× | 64% |
| 0.10 | 0.07 | 1.43× | 67% |
| 0.12 | 0.08 | 1.50× | 69% |
| 0.12 | 0.06 | 2.00× | 80% |

**The pitcher owns roughly two-thirds to four-fifths of it.** The reason is not that his term matters more per second — the terms are interchangeable, second for second — but that **pitchers vary more than catchers do.**

⚠️ **STATED AGAINST INTEREST, per F-314.** Both SDs above are reconstructed from memory in a cycle that read nothing. The apparent agreement between this derivation and the Savant claim is **two unverified things agreeing**, which is precisely the F-274 pattern. **It is recorded as suggestive and nothing more.** What makes it worth recording at all is that the two routes are genuinely different — a fitted probability model against a spread decomposition — and that the derivation's conclusion is insensitive to the inputs: the pitcher's share exceeds 50% for *any* SD ratio above 1.0.

**And the cross-topic ordering is the useful part.** F-308 prices half an inch of catcher framing at ~8 runs a college season. This file prices the entire running game against a starter at ~0.4–1.7 runs. **For the catcher as well as for the pitcher, framing outranks throwing by roughly an order of magnitude.** A program choosing between receiving work and pop-time work is not choosing between two comparable things.

---

## 10. What is not in here

- **The lead-length response to pickoff attempts** — the entire justification for throwing over, unmeasured for any population (F-324, Dispute #24).
- **The distraction channel.** Whether a runner on first degrades pitch selection, command or velocity by more than the steal itself costs. Frequently asserted, never quantified, and if real it could exceed everything in §5 (Dispute #24b).
- **Holding at second and third**, delayed steals, first-and-third plays, the pitchout.
- **Left-handers**, whose pickoff move is a different object with different rules and a different deterrence curve.
- **Any NCAA baserunning data at all.** Every attempt-rate figure in §5.1 is assumed. One query against any program's own game log fixes it.
- **Whether the quick delivery costs COMMAND**, which §5.2 does not price and F-310 says takes 2.4 seasons to see.
