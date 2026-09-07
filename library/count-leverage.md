# Count Leverage — where a pitch is actually worth something

**Created 2026-09-07.** Companion to `pitch-mix-sequencing.md` (which covers WHAT MIX) and `stuff-and-command.md` §5 (command as an angular problem). This file covers **WHICH PITCHES MATTER**, by ball-strike count.

> ## ⚠️ RUN CONDITION — READ BEFORE USING ANY NUMBER HERE
> This file was produced in the **FOURTH CONSECUTIVE fully egress-blocked cycle** (F-259, F-266, F-267, **F-277**). `WebFetch` returned `EGRESS_BLOCKED` on every host attempted; raw `curl` got HTTP `000` with the agent proxy logging `403 to CONNECT` — a **policy denial at the gateway**, including on `en.wikipedia.org` as a control. **No primary source was opened. Nothing in this file is source-verified.**
>
> **What that means for how to read it:** everything in §1–§4 is **closed-form arithmetic on a Markov chain** and depends on no citation — it is either right or wrong on its own terms, and you can re-derive it in twenty lines of Python. §5 carries **one unverified empirical input** (the walk-minus-strikeout run gap), bracketed. §6 is a **field item that is snippet-only**. Per the standing rule (F-259): *a cycle that cannot read papers must not write table rows* — so the tables here are **derived**, not **reported**, and they are labelled as such throughout.

---

## 0. The one-paragraph version

Per pitch, leverage is highest deep in the count — a full count is roughly **4.7×** a 0-0 pitch and roughly **an order of magnitude** above 0-2. But **total** leverage over a season is dominated by **0-0**, because 0-0 happens once per plate appearance and 3-2 happens once every eight or nine. Under the honest model (balls in play included), 0-0 carries ~24% of a pitcher's entire ball-strike leverage budget and 3-2 carries ~12%. **0-2 is the lowest-leverage count in baseball** — ~10% of pitches carrying ~2% of the leverage — which means the entire "waste pitch vs. put-away pitch" argument is a fight over about a fifth of a run per season. And **"pitcher-ahead" counts are 34% of pitches and 15% of leverage**: getting ahead pays *at the moment you get ahead*, not in the counts you then occupy.

---

## 1. The identity that makes this computable without any data

Treat the plate appearance, for the moment, as a pure ball/strike lattice: every pitch is a **ball** (probability $1-q$) or a **strike** (probability $q$, fouls included). Absorbing states are the walk at $b=4$ and the strikeout at $s=3$.

Let $u(b,s)$ be the probability of reaching a **walk before a strikeout** from count $(b,s)$. With $B = 4-b$ balls still needed and $S = 3-s$ strikes still needed, this is the standard negative-binomial race:

$$u(b,s) \;=\; \sum_{j=0}^{S-1} \binom{B-1+j}{\,j\,}\,(1-q)^{B} q^{\,j}$$

Let $W$ be the run value of a walk and $K$ the run value of a strikeout. Then the count's value is $V(b,s) = K + u(b,s)\,(W-K)$, and the **leverage** of a pitch — the swing in plate-appearance value between the ball outcome and the strike outcome — is

$$L(b,s) \;=\; V(b+1,s) - V(b,s+1) \;=\; \bigl[\,u(b+1,s) - u(b,s+1)\,\bigr]\cdot (W-K)$$

**The point:** in the *ratio* $\lambda(b,s) = L(b,s)/L(0,0)$, the factor $(W-K)$ **cancels completely.** The relative leverage of every count in baseball is determined by **one number, $q$** — and by nothing else. No run-expectancy table, no Statcast query, no citation. This is why this topic was chosen for a blocked cycle.

### The relative-leverage table (derived, F-278)

| Count | $q=0.55$ | $q=0.62$ | $q=0.70$ |
|---|---|---|---|
| **3-2** | 3.63 | **4.74** | 7.56 |
| 3-1 | 2.00 | 2.94 | 5.29 |
| 2-1 | 1.80 | 2.23 | 3.17 |
| 2-0 | 1.48 | 2.08 | 3.33 |
| 3-0 | 1.10 | 1.82 | 3.70 |
| 2-2 | 1.63 | 1.80 | 2.27 |
| 1-0 | 1.33 | 1.58 | 2.00 |
| 1-1 | 1.21 | 1.27 | 1.43 |
| **0-0** | 1.00 | **1.00** | 1.00 |
| 1-2 | 0.73 | 0.68 | 0.68 |
| 0-1 | 0.73 | 0.65 | 0.57 |
| **0-2** | 0.33 | **0.26** | 0.20 |

---

## 2. How hard I tried to break it — and what broke

**This is the part that matters more than the table.** Three separate specifications were run against the base model.

**(a) Count-varying strike probability.** The i.i.d.-$q$ assumption is plainly false: pitchers fill up the zone when behind (~.78 at 3-0) and nibble when ahead (~.48 at 0-2). Re-solving the chain with a count-specific $q$ vector: **the order changes, but no count moves more than 2 places**, 3-2 stays top, 0-2 stays bottom, and the 3-2/0-2 ratio falls from 18.2× to 11.7×.

**(b) Balls in play.** Adding a third per-pitch outcome (in play, with value $C$) and sweeping the BIP rate 0.10–0.24 and $C$ from $-0.10$ to $+0.10$: **3-2 and 3-1 are the top two in every specification and 0-2 is last in every specification**, but the middle of the table reshuffles freely, and the 3-2/0-2 ratio ranges **4.9× to 18.2×** across specifications.

**(c) Fouls.** Modelling the 2-strike foul as a return to the same state lengthens 2-strike counts and raises their share of pitches thrown, but does not touch $L$ itself (leverage is the ball-vs-strike swing, and a foul is neither).

> ### The honest claim, therefore (F-278)
> **Robust:** 3-2 is the highest-leverage count and 0-2 the lowest, in every specification tried. The gap between them is **an order of magnitude, not a number** — call it 5–18×, and never quote a single figure.
> **NOT robust:** the cell values, and the rank order through the middle of the table. **Say the ordering of the extremes; never quote a middle cell.** This is the F-269 lesson applied to the author's own new model on the day it was built.

---

## 3. Where the leverage actually lives — and the error this caught

The first pass computed pitch shares from the **ball/strike-only** lattice and produced a headline that 3-2 carries ~20% of all leverage while being 5.8% of pitches. **That was an artifact.** A tree with no balls in play cannot end a plate appearance early, so it produced **4.92 pitches per PA** against a real-world ~3.9, systematically over-weighting deep counts.

Re-derived with balls in play at 17% per pitch (**3.47 pitches/PA** — now slightly *short*, so the true answer is bracketed by the two runs):

| Count | $\lambda$ | % of pitches | % of total leverage |
|---|---|---|---|
| **0-0** | 1.00 | **28.8%** | **23.7%** |
| 3-2 | 4.74 | 3.1% | 11.9% |
| 1-0 | 1.58 | 9.1% | 11.8% |
| 1-1 | 1.27 | 9.4% | 9.8% |
| 2-2 | 1.80 | 5.8% | 8.6% |
| 2-1 | 2.23 | 4.4% | 8.1% |
| 0-1 | 0.65 | 14.8% | 7.9% |
| 1-2 | 0.68 | 9.2% | 5.2% |
| 2-0 | 2.08 | 2.9% | 4.9% |
| 3-1 | 2.94 | 1.9% | 4.5% |
| **0-2** | 0.26 | **9.7%** | **2.1%** |
| 3-0 | 1.82 | 0.9% | 1.4% |

| Group | % of pitches | % of leverage |
|---|---|---|
| 2-strike counts | 27.8% | 27.8% |
| 3-ball counts | 5.8% | 17.8% |
| **Pitcher ahead (0-1, 0-2, 1-2)** | **33.8%** | **15.2%** |

**Three readings fall out of this table.**

1. **0-0 is the highest-total-leverage count in baseball (F-279)** — not because any single first pitch matters much, but because there are so many of them. The deep-count story is *per-pitch* true and *aggregate* misleading. A coach optimising for total runs should care about the first pitch more than the full count, and about the full count more than any other single count.
2. **0-2 is arithmetically negligible (F-280).** 9.7% of pitches, 2.1% of leverage, $\lambda = 0.26$. The reason is structural: at 0-2 both outcomes are cheap — a strike ends it in your favour, a ball merely moves you to 1-2, which is still a good count. **The waste-pitch argument is a real argument about a very small number.**
3. **"Get ahead" pays at the transition, not in the destination (F-281).** Ahead counts are a third of all pitches and a seventh of all leverage. The value of 0-1 over 1-0 is banked the instant the first pitch is a strike — which is why $\lambda(0,0)$ is high and $\lambda(0,1)$ is low. Nothing here argues against getting ahead; it argues against the idea that being ahead is where the work happens.

---

## 4. What a strike-rate gain is worth, by count

**⚠️ This section introduces the file's ONE unverified empirical input:** $(W-K)$, the run-value gap between a walk and a strikeout, reconstructed from memory with no page open and bracketed at **0.55–0.62 runs**. Every absolute run figure below scales linearly with it. The *ratios* in §1–§3 do not depend on it at all. **Verify against a run-expectancy table when egress returns and issue a dated correction if it lands outside that bracket.**

For a 1,400-pitch D1 starter season, with $(W-K) = 0.58$:

| Where the gain lands | Pitches/season | Value of **+5 strike-rate points** |
|---|---|---|
| 3-2 only | ~43 | **1.24 runs** |
| 0-2 only | ~136 | **0.22 runs** |
| **Everywhere** | 1,400 | **10.4 runs** |

**The dominant term is breadth, not targeting.** A general command gain is worth roughly **eight times** the best available count-specific gain, because the count-specific gain is throttled by how few pitches occur in that count. Count-targeted work is worth doing only when the gain is genuinely *count-specific* — something he does badly in that count and not elsewhere.

---

## 5. Detection — and why this cannot be checked in games (F-282)

Two-proportion test, $\alpha = .05$, 80% power, $n$ **per group, per arm**:

$$n \;=\; 15.70\;\frac{\bar p(1-\bar p)}{\delta^{2}}$$

| Gain to detect | $\bar p = .62$ (3-2 strike rate) | $\bar p = .50$ (0-2 chase rate) |
|---|---|---|
| +3.0 pts | 4,110 | 4,361 |
| +5.0 pts | 1,480 | 1,570 |
| +7.5 pts | 658 | 698 |
| +10.0 pts | 370 | 392 |
| +15.0 pts | 164 | 174 |

A D1 starter throws about **43 full-count pitches all season.** Detecting even a **+10-point** 3-2 strike-rate improvement in game data would take **≈17 seasons.**

> **The conclusion, and it generalises: a count-specific training effect is not observable in one athlete's competition data, ever.** This is the same structure as F-273 (mix) and F-257 (deception): the quantity you want to change is real, and the athlete you want to change it in cannot supply enough events to see it. **The count must be manufactured to be measured.**
>
> **The affordable version:** 25 manufactured full counts per bullpen × 3 bullpens/week × 12 weeks = 900 pitches, split into two 450-pitch halves, detects **δ ≈ 9 points**. That is a real, runnable, single-athlete study — and it is the only design in this file that a college program can actually execute.

---

## 6. ABS challenge as a leverage-allocation problem — **FIELD ITEM, SNIPPET-ONLY** (F-283)

MLB's 2026 Automated Ball-Strike **challenge** system gives each team two challenges per game; only the batter, catcher and pitcher may challenge. Reported success rates (multiple outlets, **none opened — snippet-level only**): catchers ~59–60% overturn, batters ~46%, and **almost no pitcher challenges at all** — one report names a single reliever as the only pitcher in MLB with more than two challenges on the season.

**The derivation applies directly and needs no new machinery.** A challenge is a discrete, scarce resource; the expected value of spending one in count $(b,s)$ is

$$\text{EV} \;=\; P(\text{overturn})\cdot L(b,s) \;-\; \text{option value of holding it}$$

Because $L$ varies **5–18×** across counts and $P(\text{overturn})$ varies far less than that, **the count term dominates the challenge decision.** A challenge on a 3-2 pitch is worth roughly an order of magnitude more than the same challenge, at the same overturn probability, on 0-2. Burning a challenge on an 0-2 borderline call is close to free money handed back.

**Standing of this item:** the arithmetic is the same arithmetic as §1 and is sound. The *empirical inputs* (challenge counts, overturn rates, the pitcher-participation gap) are **snippet-only and unverified** — treat them as the reason to look, not as measurements. **Applicability to Ole Miss depends on whether the SEC operates an ABS challenge system in the relevant season, which this cycle could not verify.**

---

## 7. What this file does NOT establish

- **Nobody has manipulated practice allocation by count and measured anything.** There is no intervention here of any kind. Every claim in this file is **MECHANISM / DERIVATION**. Do not phrase any of it as an instruction backed by evidence.
- **It says nothing about pitch selection within a count** — only about how much a ball-versus-strike outcome is worth there. What to *throw* in 3-2 is a different question, and `pitch-mix-sequencing.md` shows the outcome-side of that question is unanswerable at the individual level.
- **It assumes the pitcher is indifferent to contact quality.** Collapsing balls in play into a single count-independent value $C$ is the model's weakest joint — in reality hitters do more damage in hitter's counts, which would push *further* in the direction of §2's conclusion, not against it.
- **It has no hitter model.** A hitter's swing decisions change by count, and the whole tree is derived as if the pitcher faces a fixed opponent.
- **Times-through-the-order, sequence order and specific-hitter attack remain entirely uncovered** in this corpus (F-258 is quarantined).
