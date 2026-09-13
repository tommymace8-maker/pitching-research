# The Pitch Clock, Inter-Pitch Tempo, and the Recovery Interval

**Created 2026-09-13 (cycle 12).** Population: **elite, 85 mph floor** — showcase/D1-committed HS through college and pro. Mission: **performance development.** Injury is a supporting constraint and gets one line.

> ## ⚠️ RUN CONDITION — READ BEFORE USING ANY NUMBER IN THIS FILE
> This file was written in the **NINTH consecutive fully egress-blocked cycle** (F-326). **No primary source was opened.** `WebFetch` and raw `curl` were both refused — `EGRESS_BLOCKED` and `CONNECT tunnel failed, response 403` — for `en.wikipedia.org` as a control and for `pmc.ncbi.nlm.nih.gov` directly. `WebSearch` was the only working channel, and it returns summaries rather than pages.
>
> **What that means for this file, precisely:**
> - **§2, §3.1, §3.3, §4, §5.2 and §7 are DERIVATION.** Closed-form recovery modelling, difference-in-differences arithmetic, censoring logic and power calculations. They depend on no source and are re-derivable in about forty lines. **These are safe.**
> - **§3.2, §5.1 and §6 are SNIPPET-ONLY.** Rule text, reported league velocity changes, a leaderboard definition. **Every one is a lead, not a magnitude** (F-284 rule).
> - **§3.4 (Yang 2016) is the important one and carries TWO flags at once:** snippet-only substance, **and a SAMPLE MISMATCH** — n = 7 Taiwanese intercollegiate pitchers whose mean velocity is not reported anywhere and has no reason to clear 85 mph.
> - **Every magnitude in §2 is a multiple of `d`, the per-pitch phosphagen depletion, WHICH NOBODY HAS MEASURED.** The **ratios** are the output. There is no cell value in §2 to quote to anybody.

---

## 1. Why this topic, and what it is not

The corpus had **zero** entries for "pitch clock" across 325 findings before this cycle. That is a real hole: the clock is not an optional training variable a coach may take or leave — it is a **binding rule constraint on every pitch every athlete in this program throws**, and it has been one for several seasons.

The topic was also chosen against **F-320's search criterion**, which the corpus adopted one cycle ago: *hunt for topics where the lever and the measurement are the same physical quantity, because that is where the detection wall is not.* Tempo is seconds. A stopwatch measures seconds. The lever and the instrument are the same thing, and §4 shows the detection arithmetic behaves accordingly.

**What this file is not.** It is not an injury file. Two papers on the clock and UCL surgery surfaced in the sweep (PMC12569362, PMC12858762) plus a 2026 *Arthroscopy* editorial commentary (PMID 42001115, Cossell). **All three are unread, all three are injury-side, and an editorial commentary is precisely the third-party-paraphrase hazard class this program has already been burned by once.** They are logged to the queue and the file moves on.

---

## 2. The recovery model — and why the industry's mechanism is the wrong shape

### 2.1 The standing story

The universally repeated mechanism is: *less time between pitches → less recovery → cumulative fatigue → lost velocity late in outings.* It is stated by broadcasters, by players, and in the journalism the sweep returned. **It is the wrong shape, and the corpus can show that with its own existing physiology.**

### 2.2 The steady state

From F-132, phosphagen resynthesis has a fast phase restoring roughly half of PCr in **20–30 s**, near-complete in 3–5 min. Model each pitch as depleting a fraction `d` and each inter-pitch interval `T` as recovering exponentially with time constant `τ`:

> **D_{n+1} = (D_n + d)·e^(−T/τ)**

which has the closed-form fixed point

> **D\* = d / (e^(T/τ) − 1)**

**Two results fall straight out, and the second one is the finding.**

**(a) The deficit PLATEAUS, and does so almost immediately.** Convergence is geometric with ratio e^(−T/τ), so the deficit reaches 95% of its steady state within:

| Interval T | 95% of steady state by pitch (τ = 28.9–43.3 s) |
|---|---|
| 25 s | **3.5 – 5.2** |
| 20 s (NCAA) | **4.3 – 6.5** |
| 15 s (MLB, bases empty) | **5.8 – 8.6** |
| 12 s | **7.2 – 10.8** |
| 8 s | **10.8 – 16.2** |

**Always inside the first inning or two.** Whatever the clock costs metabolically, it is paid in the first inning and is flat thereafter. **It cannot produce a progressive late-outing decline, because there is nothing left accumulating by the fourth inning** (F-327).

**(b) The RATIOS survive not knowing τ.** Steady-state deficit relative to an unclocked 25-second interval:

| Interval | τ=28.9 s | τ=36.1 s | τ=43.3 s | **Spread** |
|---|---|---|---|---|
| 20 s (NCAA) | 1.38× | 1.35× | 1.33× | **1.33–1.38** |
| 15 s (MLB empty) | 2.02× | 1.94× | 1.89× | **1.89–2.02** |
| 12 s | 2.67× | 2.53× | 2.45× | **2.45–2.67** |
| 8 s | 4.31× | 4.03× | 3.85× | **3.85–4.31** |

Across the **entire** plausible half-time bracket the NCAA figure moves only from 1.33 to 1.38. **This is an F-307/F-317-class result: the comparison survives not knowing the quantity nobody knows.** It is also the third time this program has found one, and the pattern is worth naming — *ratios of a common unknown are the natural output of a blocked cycle.*

**And the threshold shape matters.** The penalty is convex: 25→20 s costs +35%, 20→15 s costs another +44%, 20→12 s costs +88%. **There is no linear "seconds of rest" currency here.** Twenty seconds is a materially different place on the curve from twelve.

### 2.3 A clock removes the cheapest seconds

Because dF/dt = (1/τ)e^(−t/τ) is decreasing, the marginal value of a second of rest falls monotonically (F-330). At τ = 36.1 s:

| t | marginal value |
|---|---|
| 0 s | 2.77 pts/s |
| 10 s | 2.10 pts/s |
| 17 s | 1.73 pts/s |
| 20 s | 1.59 pts/s |
| 25 s | 1.39 pts/s |

**The last 3 seconds of a 20-second interval buy 5.0 points of fast-phase recovery; the first 3 buy 8.0 — a ratio of 1.60×.** A clock truncates the *end* of the interval. **It is therefore the least damaging available way to remove a given quantity of rest**, which is an argument *for* the rule that nobody in the sweep made.

Over a full outing, cutting mean tempo by 2/3/5 s removes 200/300/500 s of in-inning rest — **6.7% / 10.1% / 16.8%** of the ~50-minute total in-game recovery budget (100 pitches, ~6.5 inning breaks at ~150 s). **Note what dominates that budget: the between-inning breaks, which the pitch clock does not touch at all.** If inter-effort recovery were genuinely the binding constraint on late-outing performance, the intervention with leverage would be the inning break, not the pitch interval.

### 2.4 The anatomist's bound on `d`

Everything above is a multiple of `d`, and `d` is unmeasured (F-336). **But the corpus bounds it as small, using its own findings.** F-127 records that velocity **holds through roughly pitch 60 and declines LAST**, after command drift, secondary-pitch quality and slot. If `d` were large enough that a 3–5 second interval difference mattered materially, the standing deficit would be large and would arrive by pitch 6 — producing an early velocity collapse nobody observes.

**The observed within-outing velocity stability is itself evidence that per-pitch phosphagen depletion is small.** And this points the blame elsewhere for the real late-outing decline: F-127 already names posterior-cuff voluntary activation loss at 60–90 pitches, which is neural, cumulative, and has nothing to do with the inter-pitch interval.

---

## 3. What the empirical record actually says

### 3.1 The rule supplies its own natural experiment

**Nobody in the sweep used the best instrument available, which the rule itself creates.** MLB's 2023 clock ran **15 s bases empty / 20 s runners on**. The same pitchers, in the same season, faced a **5-second rule-imposed difference**. Differencing removes everything common to the season — ball construction, weather, schedule, aging, league-wide training trends.

Reported 2022→2023 change: **−0.3 mph bases empty, −0.2 mph runners on.**

> **Diff-in-diff = −0.10 mph per 5 s → ≈ 0.020 mph per second of rest** (F-328)

Applied forward: **NCAA 20 s versus an unclocked 25 s ≈ 0.10 mph.** That is inside the day-to-day noise of a single radar gun.

**And it is an UPPER bound, because the confound shares its sign.** Pitchers throw with higher intent with runners on base, inflating the runners-on arm. F-069 (wind-up ≈ stretch in pros, replicated twice) bounds the *delivery-type* confound as small but says nothing about intent. **A confound that pushes the same direction as the effect means the true clock effect is smaller than 0.02 mph/s, not larger.**

### 3.2 The headline claim does not survive (F-333)

The most-shared pitch-clock statistic: *of the **26** pitchers who improved tempo by **5+ seconds**, **22 (85%)** lost velocity, versus **65%** of everyone else.*

Checked in-cycle against H₀ = 0.65: SE = 0.0935, **z = 2.10, p ≈ 0.036.** Marginal — and then three objections:

1. **Forking paths.** "Five or more seconds" is a cutpoint chosen after seeing the data. **F-297** demonstrates that scanning a modest number of candidate cuts produces an apparently significant cell on a population with *no* true effect. A p of .036 survives that scan poorly.
2. **Selection on the prior variable.** Pitchers who cut 5+ seconds are *by construction* the slowest workers of 2022 — plausibly older, further along the aging curve where F-073/F-078 make velocity loss expected anyway. The contrast is one selected group against everybody else, not tempo-change against tempo-stable.
3. **The baseline is also treated.** 65% of the "others" lost velocity too, in a season when every pitcher was clocked. **There is no untreated comparison group anywhere in the design.**

**Verdict: UNPROVEN. Do not repeat 85% vs 65%.** It will be quoted at this program, because it is the most shareable number in the topic.

### 3.3 What the raw before-after is worth

The −0.3 mph itself is an **uncontrolled pre-post across a league-wide treatment**. Note the trap: with hundreds of thousands of pitches the league mean has a standard error of roughly **0.004 mph**, so the decline is statistically certain — **and statistical certainty about a descriptive change says nothing about what caused it.** *Precision is not identification.* This is Known Correction #6 (the Gdovin "removal experiment" that was an uncontrolled pre-post) arriving in a new venue.

### 3.4 The one manipulated study — and where its arms actually sit (F-329)

**Yang SC, Wang CC, Lee SD, et al., "Impact of 12-s Rule on Performance and Muscle Damage of Baseball Pitchers," *Med Sci Sports Exerc*, 2016, PMID 27434082** (University of Taipei).

**Design: n = 7 intercollegiate pitchers, randomized counterbalanced, three rest conditions — 8 s / 12 s / 20 s — over a 7-inning simulated game at 15 pitches per inning (105 pitches per condition).** Reported: dropping from 20 s to **12 s or less** produced **early-onset performance loss within the game** and elevated muscle-damage and inflammation markers for **more than 2 days** after.

**This is a genuine INTERVENTION on the exact variable, which is rare — the corpus runs roughly 30:1 cross-sectional to intervention.** And the mapping to real rules is the finding:

| Study arm | Corresponds to |
|---|---|
| **20 s — the safe arm** | **The NCAA clock, exactly** |
| *(untested gap)* | **MLB 15 s empty / 18 s on — TESTED BY NOBODY** |
| **12 s — harm** | The proposed "12-second rule" that was the study's premise. **Never adopted in this form.** |
| **8 s — harm** | No rule anywhere |

**So the only experiment anyone has run found no harm at the interval college baseball actually plays under.** That is a reassurance, not a licence.

**Three flags.** ⚠️ **n = 7.** ⚠️ **SAMPLE MISMATCH — DIRECTIONAL ONLY:** Taiwanese intercollegiate pitchers, mean velocity not reported in any snippet, no reason to believe it clears 85 mph. Second instance this month after F-323 (76 mph, 17.6 years old). ⚠️ **Substance is snippet-only** — existence is corroborated across two independent queries returning a matching PubMed title/journal/year, but **no page was opened**, and no marker, value or effect size is retrievable. **Do not repeat the 2-day muscle-damage result as a magnitude.**

**And one thing recorded AGAINST INTEREST, per F-314.** §2.2's model independently predicts an **early-onset, threshold-shaped** loss worsening sharply below ~15 s, and the snippet describes exactly that. **Two things agreeing when one of them is unread is the F-274 pattern and is NOT corroboration.** It is recorded only because the two routes are genuinely different — a closed-form recovery model versus a randomized crossover — and because the prediction was derived *before* the study was found.

---

## 4. The clock censors the cheapest fatigue tell — and what to use instead (F-331)

**This is the file's one executable recommendation.**

F-127 lists the coach-observable fatigue sequence: **command drift → loss of breaking-ball depth → visible slot drop → LONGER TIME BETWEEN PITCHES → velocity decline last.** Sign #4 is tempo. **A pitch clock caps sign #4.**

The signal is **right-censored**, and worst for the pitcher it binds hardest:

| Baseline tempo | Fatigue would push | Coach can observe | Share of signal |
|---|---|---|---|
| 18 s | +6 s | **+2 s** | **33%** |
| 16 s | +6 s | +4 s | 67% |
| 15 s | +8 s | +5 s | 62% |

**The fast worker keeps most of the tell. The slow worker — the one the clock actually binds, and the one whose fatigue you most want to catch — loses two-thirds of it.**

**The uncensored substitute: SECONDS REMAINING ON THE CLOCK AT FIRST MOVEMENT.** Same underlying drift, inverted observable — un-clocked fatigue made a pitcher slower *between* pitches; under a cap it makes him arrive at the buzzer with *less margin*.

**And it is cheap.** Detecting a **3-second drop in margin** (two-sample, α = .05 two-sided, 80% power, n = 15.7σ²/δ²):

| σ(margin) | n per bucket | total |
|---|---|---|
| 2 s | **7** | **14 pitches** |
| 3 s | **16** | **31 pitches** |
| 4 s | **28** | **56 pitches** |

**All three fit inside a single start** (first 30 pitches vs last 30). Against the corpus's usual walls — 60,000 pitches for a mix change (F-273), 17 seasons for a count effect (F-282), 790 seasons for a TTOP effect (F-286), 2.4 starter-seasons for a clean command read (F-310) — **this is the second quantity the corpus has found that answers the same night** (after F-320's five stopwatch readings). **Both are levers measured directly, not outcomes.** F-320's lesson generalises.

⚠️ **The instrument is UNVALIDATED.** F-127's ordering is itself only EMERGING as a formal hierarchy, and nobody has tested clock margin as a fatigue proxy in any population. It is cheap, uncensored, and unproven — and it should be charted for a season before it is allowed to remove anyone from a game.

---

## 5. The disengagement card is shared with the running game (F-332)

### 5.1 The rule (SNIPPET-ONLY — verify before coaching)

NCAA reportedly runs a **20-second action clock** with a **ball added to the count** on expiry, and permits **one step-off or fake throw per batter** to reset it. MLB permits **two disengagements per plate appearance**. ⚠️ **Neither NCAA PDF was opened** (the January 2026 Clock Operation Guide and the 2025–26 Rules Changes document both surfaced in search and neither is fetchable). ⚠️ **And one specific caution:** the search summary asserted the 20-second limit applies *both* with bases empty and with runners on **without a quoted snippet supporting the both-situations claim** — which is exactly the F-293 texture. **Verify with compliance and umpiring contacts.**

### 5.2 The derivation, which survives any card count

**The step-off that resets the clock and the step-off that permits a pickoff are the same card.** F-322 priced the pickoff against the running game *alone*: a third-disengagement attempt needs a **28.5%** pickoff success rate against an actual **1–2%**, losing by **14–28×**, and ordinary pickoff EV is approximately zero with the whole case resting on an unmeasured deterrence channel (F-324).

**The clock now gives that same card a second, concrete, immediate use — stopping a count from becoming a ball.** Under a one-card college rule, **every pickoff throw spends that batter's only clock reset**, leaving no mechanism to stop the clock for the remainder of the at-bat.

**This cannot move F-322's answer in the favourable direction.** Adding a competing claim on a scarce resource can only raise the price of spending it. **The structural point holds under any card count; the count itself is snippet-only.**

---

## 6. Measuring tempo — and a definition that matters (F-334)

Baseball Savant publishes a public **Pitch Tempo** leaderboard: **median seconds release-to-release**, split **bases empty / runners on**, with display buckets **"Fast" ≤ 15 s** and **"Slow" > 30 s**.

**The inclusion rule is the finding: only pitches following a TAKE (called strike or called ball) to the SAME batter.**

Since roughly half of all pitches are swung at, fouled, or end the plate appearance, **the metric is computed on a minority of pitches — and the excluded ones are precisely those following contact, where tempo is most disrupted.** It is also conditioned on takes, and take rates vary strongly by count (F-312), so it inherits a count-composition tilt of the kind F-287 and F-298 document.

**⚠️ SNIPPET-ONLY — the page was never opened. Queued.** Do not benchmark a college pitcher against an MLB median until someone confirms the definition, and if you chart tempo yourself, **decide and write down your inclusion rule first** — the same discipline F-310 required of command metrics. A college stopwatch figure that includes everything is not the same quantity as a Savant median that does not.

---

## 7. What is unmeasured, and which parts are cheap (F-336)

| # | Missing quantity | Blocks | Cost to obtain |
|---|---|---|---|
| **1** | **Per-pitch phosphagen depletion `d`** in the throwing musculature | **Every magnitude in §2** | ⚠️ **NOT CHEAP.** Needs ³¹P-MRS or biopsy; may be undoable on a mound. **This is the one that actually blocks the mechanism.** |
| **2** | **Within-pitcher SD of inter-pitch tempo at 85+** | §4 and §6 detection tables (bracketed σ = 2/3/4 s) | **One stopwatch, one start** |
| **3** | **Within-pitcher SD of clock margin at 85+** | §4 — the file's only executable recommendation | **One person, one scoreboard, one outing** |

Items 2 and 3 are the **sixth and seventh** entries in a pattern the corpus keeps rediscovering — after F-264 (within-pitcher IVB SD), F-289 (within-outing velocity SD), F-307 (location scatter at the zone edge), F-295 (the transition matrix) and F-320 (SD of time to plate):

> **A quantity already sitting in every program's own data, costing an afternoon to compute, gating a whole topic's detection arithmetic — and published by nobody.**

Seven instances is no longer a coincidence about baseball. **It is a fact about publishing: within-athlete variance is what a practitioner needs and what a journal has no venue for.** Item 1 is the opposite case and should not be lumped in with them.

---

## 8. Verification queue added this cycle

1. **PMID 27434082** (Yang 2016) — the only manipulated study. **Get the sample's mean velocity first**; if it does not clear 85 mph the whole thing is directional only. Then the performance outcome (velocity? accuracy? both?) and the markers.
2. **Baseball Savant Pitch Tempo leaderboard** — confirm the definition in §6, and pull actual median tempo values so the corpus has a norm.
3. **NCAA Clock Operation Guide (January 2026) + 2025–26 Rules Changes PDF** — settle the clock length by base state and the step-off allowance (§5.1).
4. **Baseball America "Do Pitch Clocks Reduce Velocity?" / Pitcher List 2023 tempo analysis** — the −0.3/−0.2 split that §3.1's entire bound rests on.
5. *(Injury-side, low priority for this program)* PMC12569362, PMC12858762, PMID 42001115.

---

## 9. The one-paragraph version

**The pitch clock is not a velocity problem for a college arm.** The differenced estimate off the rule's own natural experiment bounds the cost at **≈0.02 mph per second — about a tenth of a mile per hour for the whole NCAA-versus-unclocked difference** — and it is an upper bound because the confound shares its sign. The recovery model says the metabolic cost, whatever its size, **plateaus inside the first inning and cannot accumulate**, and that a clock removes the **cheapest** seconds available. The only manipulated study ever run found harm at 12 s and below and **used 20 s — the NCAA clock — as its safe arm**, though in n = 7 pitchers who probably throw well below 85. **What the clock does cost is an instrument:** it censors the corpus's own cheapest fatigue tell, and the replacement — **seconds remaining at first movement** — is worth charting, costs one volunteer, and answers inside a single start.
