# Pitch Mix, Sequencing and Usage

**Opened 2026-09-06.** Findings F-268 → F-273, F-276. Companion daily brief: `daily/2026-09-06-report.md`.

**Population:** elite, 85 mph floor. Nothing here depends on level — the arithmetic is level-independent — but the sample-size anchors are NCAA (~1,600 pitches/season) and MLB (~3,000/season) starters.

> ⚠️ **Provenance warning.** This file was written in a **fully egress-blocked cycle** (F-267, the third consecutive). **Every quantitative result in §1–§4 is derived in-cycle from stated assumptions and requires no source.** The two external references (§5) are **search-snippet level and were never opened.** One empirical input — the per-pitch run-value distribution — is **approximate and unverified**, and every conclusion drawn from it is bracketed across ±40% and shown to survive.

---

## Why this file exists

INDEX.md §5 opened its list of never-researched topics with *"Pitchability, sequencing and in-game usage."* Before today the corpus held exactly two adjacent things, both negative: **F-166** (pitch tunnelling retired as a training target) and **F-172** (no public stuff model prices sequencing). Nothing told a coach how to set a mix.

The mix problem is a **constrained optimisation, not an experiment** — which is why it could be opened in a cycle with no source access, and why the results below are unusually durable for this corpus. What could *not* be derived is the single empirical parameter everything depends on, and that gap is §6.

---

## 1. The optimality condition — and why the industry's test is the wrong one

A pitcher picks usage shares $p_i$ over pitch types, $\sum p_i = 1$. Let $v_i(p_i)$ be run value per pitch **expressed to the hitter** (lower is better for the pitcher). One assumption: a pitch degrades as it is thrown more often, because the hitter's prior on seeing it rises — $v_i' > 0$.

Minimise $V(p) = \sum_i p_i v_i(p_i)$ subject to $\sum p_i = 1$:

$$\boxed{\;v_i(p_i) + p_i\,v_i'(p_i) = \lambda \quad \text{for every pitch used}\;}$$

**What is equal at the optimum is the MARGINAL run value** — the pitch's value *plus the damage one more of it does to all the others of its type*. **Average run values $v_i$ are equal only if the wedge terms $p_i v_i'$ happen to be equal.**

**Why the assumption is not optional.** If $v_i' = 0$ everywhere, $V$ is linear in $p$ and the optimum is a **corner** — throw the best pitch 100% of the time. The fact that every real pitcher throws an interior mix *is itself the evidence* that $v_i' > 0$. Anticipation is not a refinement of the model; it is the only reason a mix exists.

**→ F-268.**

---

## 2. At a true optimum the more-used pitch should look BETTER

Linear anticipation, $v_i = a_i + b_i p_i$ with $b_i > 0$. The FOC $a_i + 2b_i p_i = \lambda$ substitutes back to:

$$v_i = \lambda - b_i p_i$$

So with comparable slopes, **the pitch thrown more often sits at a lower (better) average run value**, by $b(p_i - p_j)$.

Let $D$ = anticipation penalty in R/100 across a full 0→100% usage swing ($b = D/100$). **$D$ is unmeasured** — bracketed:

| $D$ (R/100 per full usage swing) | 60/40 | 55/45 | 70/30 | 50/30 |
|---|---|---|---|---|
| 1.0 | 0.20 | 0.10 | 0.40 | 0.20 |
| 2.0 | 0.40 | 0.20 | 0.80 | 0.40 |
| 4.0 | 0.80 | 0.40 | 1.60 | 0.80 |
| 8.0 | 1.60 | 0.80 | 3.20 | 1.60 |

*(R/100 by which the MORE-USED pitch should look BETTER at the optimum.)*

**Worked example** — FB intrinsically 1.0 R/100 worse than SL, equal slopes $D = 4$:

| FB usage | FB avg | SL avg | Total |
|---|---|---|---|
| 30% | +2.20 | +2.80 | +2.620 |
| 40% | +2.60 | +2.40 | +2.480 |
| **43.8% (opt)** | **+2.75** | **+2.25** | **+2.469** |
| 50% | +3.00 | +2.00 | +2.500 |
| 70% | +3.80 | +1.20 | +3.020 |

**At the optimum the fastball is the "worse" pitch and is thrown less. Both are correct.** A leaderboard reading would flag this pitcher as under-using his slider; he is not.

⚠️ **Quote the direction, never the numbers.** $D$ is unmeasured, the linear form was chosen for tractability, and equal slopes across pitches is almost certainly false — a sweeper and a four-seam do not decay at the same rate. What survives: for **any** smooth $v_i$, averages differ by $p_j v_j' - p_i v_i'$, and the more-used pitch is better whenever slopes are comparable. **→ F-269.**

> **This is the stride-length error transplanted into analytics.** "His slider grades out better, so throw more sliders" reads a between-pitch leaderboard gap as a within-pitcher lever. It is F-043/F-044/F-045 in a different costume, made by people who would never make it about stride length.

---

## 3. The noise floor — why an individual's own numbers can never decide this

Per-pitch run value is a lottery: ~90% of pitches move run expectancy by hundredths of a run; a small tail moves it by more than a full run.

**Outcome model** (⚠️ approximate, reconstructed from memory, **unverified — on the queue**):

| Outcome | freq | ΔRE (hitter) | | Outcome | freq | ΔRE |
|---|---|---|---|---|---|---|
| ball | .360 | +0.055 | | in-play out | .118 | −0.270 |
| called strike | .170 | −0.045 | | single | .038 | +0.450 |
| swinging strike | .105 | −0.045 | | double | .013 | +0.750 |
| foul | .185 | −0.025 | | triple | .001 | +1.050 |
| | | | | home run | .010 | +1.400 |

**→ SD ≈ 0.214 runs per pitch.** Bracketed at **0.20 / 0.25 / 0.30** throughout.

### 3a. SE of an observed "run value per 100"

| n pitches of that type | SD .20 | SD .25 | SD .30 |
|---|---|---|---|
| 100 | 2.00 | 2.50 | 3.00 |
| 300 | 1.15 | **1.44** | 1.73 |
| 500 | 0.89 | 1.12 | 1.34 |
| 1,000 | 0.63 | **0.79** | 0.95 |
| 3,000 | 0.37 | 0.46 | 0.55 |
| 5,000 | 0.28 | 0.35 | 0.42 |

**Anchors.** College starter ≈ **1,400–1,700 pitches per season across the whole arsenal**; MLB qualified starter ≈ 3,000. So a college primary fastball (~700) carries SE ≈ **0.95 R/100**; a third pitch (~200) carries **1.77**; an MLB ace's full season of fastballs (~1,200) carries **0.72**.

### 3b. Two-sample n per pitch type to detect a real gap (α=.05, 80% power)

| Gap (R/100) | SD .20 | SD .25 | SD .30 |
|---|---|---|---|
| 0.2 | 156,978 | 245,277 | 353,200 |
| 0.5 | 25,116 | 39,244 | 56,512 |
| 1.0 | 6,279 | 9,811 | 14,128 |
| 2.0 | 1,570 | **2,453** | 3,532 |
| 5.0 | 251 | 392 | 565 |

**A 2 R/100 difference between a pitcher's own two pitches — arsenal-defining — needs ~2,450 of each.** More than a full college season spent on one pitch type. **→ F-270.**

**The robustness argument, which is the point:** the tables span a ±40% band on the SD and move by less than 2.25×, while the gap between *what a season contains* and *what detection requires* is 1,000× or more. **To overturn the conclusion the true SD would have to be wrong by a factor of ~30, not 40%.**

---

## 4. What a wrong mix actually costs, and whether you can ever see the fix

### 4a. The objective is quadratically flat

$V(p) - V(p^*) = (b_F + b_S)(p-p^*)^2$. **This follows from stationarity, not linearity** — it survives any smooth value function.

**Runs over a 1,600-pitch college season:**

| Usage error | D=1 | D=2 | D=4 | D=8 |
|---|---|---|---|---|
| 5 pp | 0.08 | 0.16 | 0.32 | 0.64 |
| 10 pp | 0.32 | 0.64 | 1.28 | 2.56 |
| 15 pp | 0.72 | 1.44 | 2.88 | 5.76 |
| 20 pp | 1.28 | 2.56 | 5.12 | 10.24 |
| 30 pp | 2.88 | 5.76 | 11.52 | **23.04** |

**The actionable regime is large errors only; the middle does not exist.** Below ~10 points off, the whole-season cost is less than one blown call — spend no bullpen time on it. At 30 points off (a four-seam at 65% that should be 35% — ordinary in college baseball) the top of the range is a full win. **→ F-272.**

### 4b. And you can never verify the fix on your own athlete

Pitches needed to **detect the benefit** of fixing a usage error (one-sample vs baseline):

| Usage error | D | Gain R/100 | SD .20 | SD .25 | SD .30 |
|---|---|---|---|---|---|
| 10 pp | 2 | 0.040 | 3,924,440 | 6,131,937 | 8,829,990 |
| 10 pp | 4 | 0.080 | 981,110 | 1,532,984 | 2,207,497 |
| 20 pp | 4 | 0.320 | 61,319 | 95,812 | 137,969 |
| 20 pp | 8 | 0.640 | 15,330 | 23,953 | 34,492 |
| **30 pp** | **8** | **1.440** | **3,028** | 4,731 | 6,813 |

**The single most favourable cell — largest error, strongest anticipation, tightest noise — still needs 3,028 pitches, i.e. two college seasons.** A 15-year MLB career is ~45,000 pitches; the realistic cells need 60,000 to millions.

### 4c. So the inference belongs at the population level

**Unmeasurable-on-an-individual ≠ unreal.** 245,277 pitches ≈ **80 MLB pitcher-seasons**; 15,330 ≈ **5**. Statcast holds millions.

> **The architecture this forces: estimate the anticipation slope ONCE from the league, apply it to the individual as a prior, and never try to learn it from him. A pitcher's own run-value line should have no vote in his own mix.**

**What you verify instead is compliance, not outcome.** Did the usage actually change? **400 tracked pitches pin a usage share to about ±2.5 points.** That is a proportion, and proportions are cheap. **→ F-273.**

---

## 5. The two-sign slope — "commit or cut"

**The anatomist's objection, and the most usable result in the file.** Everything above assumed $v_i' > 0$. That is one of two effects:

$$b_i = b_i^{\text{ant}} - b_i^{\text{dose}}$$

$b^{\text{ant}} > 0$ is the hitter's anticipation penalty. $b^{\text{dose}} > 0$ is the pitcher's own execution improvement from throwing it more. **A pitch used 6% of the time is ~70 competitive reps a season.** Nobody sits on a pitch thrown 6% of the time — so at low usage the dose term plausibly dominates and **$b_i < 0$**.

**And that inverts the optimisation.** With $b_i < 0$, the contribution $a_i p_i + b_i p_i^2$ is **concave**, so there is no interior minimum and the solution is pushed to a **corner**:

> **In any usage region where execution-dose outruns anticipation, optimal usage is either zero or substantially higher. There is no optimal small dose.**

**The fourth-pitch decision is therefore "commit or cut," not "how much."** Sprinkling at 5–8% is the one usage level the model says is provably wrong — under-practised *and* insufficiently threatening, collecting the costs of both regimes and the benefits of neither.

⚠️ **The crossover usage $p_c$ is completely unmeasured.** The structure is derivable; the threshold is not. **Never tell a pitcher that 6% is below a known line.**

⚠️ **Timing.** A college pitching coach does not have the authority over in-game calling to move a pitch 12 points mid-season — catcher calls it, scouting report drives it, and a 2-2 count with the tying run on second is not where anyone experiments. **This is a February decision. The reps get built in the offseason.**

### The affordable check — and it is NOT run value

Compare the candidate pitch's **within-pitcher vertical release-angle SD** against his fastball's (the command channel of F-171 / F-186). Variance ratio, α=.05, 80% power, **pitches of EACH type**:

| Candidate's release SD is this much worse | n per pitch type |
|---|---|
| 2.00× | 34 |
| 1.75× | 51 |
| **1.50×** | **96** |
| 1.40× | 140 |
| **1.30×** | **229** |
| 1.20× | 473 |
| 1.15× | 805 |

**~100 of each — three or four bullpens — tells you whether he executes that pitch 50% worse than his fastball.** If he does, it is a dose problem and the commit path is live. If his release consistency on it is already near his fastball's, the commit argument loses its main support.

⚠️ The classic *"slowed arm gives the changeup away"* tell is **F-256 — FOLKLORE with a plausible mechanism**, universally repeated, never measured. Legitimate to look at on video; not legitimate to claim as known. **→ F-276.**

---

## 6. THE MISSING PARAMETER — and how to get it from data that already exists

**Everything in §2, §4 and §5 scales with one number that nobody has published: $D$, the anticipation slope.** Every sequencing metric in public use implicitly assumes a value for it and none of them state one.

**The estimation design, requiring no new instrumentation:**

> Within pitcher, within season, regress each pitch type's outcome on that pitch type's **trailing usage share**, using natural variation in usage across starts and across times-through-the-order. Fixed effects for pitcher × pitch type. The slope is $b_i$.
>
> **Use whiff-per-swing as the outcome, not run value** — §3 is the reason. Whiff-per-swing is binomial and far less noisy; F-257 gives its own detection table.
>
> Pooled across ~80 pitcher-seasons the parameter is well-determined (§4c). **This has almost certainly been done inside at least one front office and appears not to be published.**

**Second missing quantity:** the crossover $p_c$ where $b^{\text{dose}}$ stops dominating $b^{\text{ant}}$ (§5). The release-angle SD test above is a cheap first probe at the individual level; the population version needs the same panel regression run separately by usage decile, looking for a sign change at the low end.

**Third, unpriced:** does a mix shift change tissue load at constant pitch count? INDEX §5 lists **non-fastball workload accounting** as entirely uncovered. Every mix recommendation in this file is made with the injury constraint unpriced — permitted by the brief, but it should be said each time rather than assumed away.

---

## 7. External references — SNIPPET-ONLY, NONE OPENED

| Source | Relevance | Status |
|---|---|---|
| ESPN (2025), *"Which MLB pitchers are throwing their best stuff most often, and who shouldn't be?"* — the **Nash Score**. [link](https://www.espn.com/mlb/story/_/id/45539286/) | The industry's operationalisation of equalisation. Reported criterion: pitches within **0.2 R/100** of the average of the others = at equilibrium. Exemplar Jake Irvin; Skubal 11th at 0.37. | **UNVERIFIED — SNIPPET-ONLY.** Two objections stand (F-271): it equalises **average** where the optimum equalises **marginal**; and **0.2 R/100 is 4–9× smaller than the SE of its own inputs** (§3a). The second needs no model — only a square root. |
| arXiv **2609.03810**, *Unified Pitch Graphs for Diagnosing Pitching Strategy* | 3.94M Statcast pitches 2021→Jul 2026; 300 highest-workload 2025 pitchers. Authors' own words: *"increasing state detail or path length can recover specificity at the cost of rapidly decreasing statistical support."* | **UNVERIFIED — SNIPPET-ONLY. Priority read** — that sentence is §3 restated by an independent group. |
| arXiv **2606.17345**, *Counterfactual Optimization of Baseball Pitch Sequences…* | Only known attempt to price a mix change in season-level runs. | **UNVERIFIED — SNIPPET-ONLY.** On the queue since 2026-09-04, still unread. |
| arXiv **2601.11904**, *Structure of Pitch-Pattern Motifs in MLB* | Sequence motifs. | **UNVERIFIED — SNIPPET-ONLY.** |
| Driveline, *"The Interaction of Biomechanics and Command"* (Feb 2026) | Adjacent. | **Blocked at source per standing brief.** Queued. |

⚠️ Two pitch-count figures (3.94M and 12.4M) appear in search summaries of these papers and are **mutually inconsistent** — they probably belong to different papers. **Quote neither.**

---

## 8. Reproducibility

- Optimum: $v_i + p_i v_i' = \lambda$; linear case $p_i = (\lambda - a_i)/2b_i$, $v_i = \lambda - b_i p_i$.
- Loss from usage error: $(b_F + b_S)(p - p^*)^2$ runs per pitch.
- Two-sample n per group: $n = 2(z_{\alpha/2}+z_\beta)^2\sigma^2/\delta^2$, $z_{.025}+z_{.20} = 2.8016$.
- SE of run value per 100: $100\sigma/\sqrt n$.
- Variance ratio n per group: $n \approx 1 + 2(z_{\alpha/2}+z_\beta)^2/(\ln r)^2$.

Scripts as run: `daily/2026-09-06-report.md` §8.
