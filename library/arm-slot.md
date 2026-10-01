# THE ARM SLOT — marker, lever, and the identity underneath it

**Opened 2026-10-01.** Findings **F-533 → F-546**. Disputes **#51, #52**. Companion to `biomechanics.md` §3, `stuff-and-command.md` §7, `coaching-translation.md`.

> **RUN CONDITION: this file was written on a FULLY EGRESS-BLOCKED day (F-546).** Every literature claim is **snippet-only**. Every *derived* section (§2, §3, §6) is **source-independent arithmetic** and survives the blockage. Read §1 before anything else, because it changes what the rest of the topic's numbers mean.

---

## §0 — Why this topic needed a cycle

Arm slot has been in this corpus since day one (F-070, F-071) and **Dispute #10 — "lower arm slot: universal recommendation or individual?" — has been open, 🟡 NARROWED, longer than almost anything else here.** It has never had a dedicated cycle. Meanwhile it became the single most active mechanical intervention in professional baseball: pitchers have lowered slots in **8 of the last 10 seasons**, and whole organizations now run coordinated slot-change programs (F-544).

So the topic is simultaneously: the industry's most-used lever, and a variable with **zero manipulation studies** (F-541).

---

## §1 — What "arm angle" actually measures (F-533)

**Statcast arm angle is the inclination of the straight line from the throwing shoulder to the ball at release.** 0° = horizontal (sidearm), 90° = over the top.

It is therefore a **composite of three anatomically independent things**:

| Contributor | What moves it | Cost profile |
|---|---|---|
| **Trunk lateral tilt** (toward glove side) | more tilt → LOWER arm angle | **expensive** — costs command (F-176), raises varus torque (F-070 failure mode) |
| **Shoulder abduction** | less abduction → lower arm angle | the "real" arm change; cheap on velocity (F-538) |
| **Elbow flexion at release** | more flexion → shortens the vector | small, largely not consciously controlled |

**Consequence: "raise your arm slot" is not an instruction, it is three different instructions with opposite price tags.** The industry's independent read agrees — one widely-circulated coaching source: *"most of the time, arm slot is much more about the amount and direction of trunk tilt than it is about specific shoulder positioning."*

**This is also the structural reason Dispute #51 exists** (is slot a lever at all, or an output of the trunk wearing the arm's clothes?), and it is the *exact* shape of Dispute #47 about the glove arm. Two consecutive topics have now turned out to be trunk variables in a limb's costume.

---

## §2 — 🔢 THE IDENTITY (F-534) — the core of this file

Because the shoulder-to-ball distance at release is nearly fixed for a given athlete:

> ### **z_ball = z_shoulder + L · sin θ**

- `z_ball` = release height (public on Savant, every pitch)
- `θ` = arm angle (public on Savant since 2020)
- `L` = shoulder-to-ball distance ≈ **0.82 m / 32.3 in** for professional anthropometry
- `z_shoulder` = **shoulder height at release — published by nobody (F-543)**

**Derivation of L** (ASMI cohort height 189.7 cm, F-151): upper arm 0.186·H = 0.353 m; forearm 0.146·H = 0.277 m; hand 0.108·H = 0.205 m; elbow→ball ≈ 0.482 m; elbow flexion at release ≈ 22° (ASMI norm 20–25°).
L = √(a² + b² + 2ab·cos φ) = √(0.1246 + 0.2323 + 0.3403 × 0.9272) = **0.820 m**.

### The exchange rate

**dz/dθ = L · cos θ · (π/180) = 0.564 · cos θ inches per degree**

| arm angle θ | inches of release height per 1° of slot |
|---|---|
| 20° | 0.53 |
| 30° | 0.49 |
| 40° | 0.43 |
| **50° (≈ MLB average)** | **0.36** |
| 60° | 0.28 |
| 70° | 0.19 |

**Finite-difference check (50° → 45°):** 32.3 × (0.7660 − 0.7071) = **1.90 in**, i.e. 0.38 in/deg — agrees with the derivative to 5%. ✅
**Robustness:** at 185 cm, L = 0.80 m and the 50° figure becomes 0.35 in/deg. **±5 cm of height moves the table ±4%. The slot angle matters far more than the body.**

### Two things follow immediately

1. **Release height and arm angle are NOT independent variables.** Any model using both is fitting a near-collinear pair whose residual is shoulder height. Check #4 territory: a high R² between them is substantially identity, not discovery.
2. **The residual IS the interesting variable**, and it is the one nobody reports (§5).

---

## §3 — 🚨 What the identity does to the sport's headline number (F-535)

The corpus holds both of these, inside F-070, presented as one trend:

- "MLB release points ~2 in lower than 2016"
- "arm angle down 1.41 deg since 2020"

**Arithmetic:** 1.41° × 0.362 in/deg = **0.51 in**. Observed: **2.0 in**. → **arm angle accounts for ~25%.**

⚠️ **Baseline mismatch stated honestly:** the 2 in runs from 2016, the 1.41° from 2020. This is the *generous* case for the arm-angle story, and it cannot be made cleaner because Statcast arm angle does not exist before 2020.

**Independent route to the same place:** F-536's validation study finds Δvertical release vs Δarm angle at **r = 0.74 → R² = 0.55**, i.e. **45% of year-over-year release-height variance is not arm angle.** Two routes — one derived, one empirical — converge on "half to three-quarters of release-height movement is a non-slot channel."

> **"The league is dropping its arm slot" is at most a quarter true. What the league is mostly doing is releasing from a lower shoulder.**

**Why this is not pedantry:** the two channels have opposite cost profiles (§1). The sport has been recommending the cheap channel using the expensive channel's data.

---

## §4 — The velocity question, answered properly (F-538)

This is the corpus's cleanest example of a **between-subject null and a within-athlete effect coexisting without contradiction.**

| Question | Design | Answer |
|---|---|---|
| Do sidearmers throw softer than over-the-top guys? | between-group, n = 207 pro (30/156/21), 240 Hz | **No. n.s., avg 86.3 mph** ⚠️ attribution snippet-level |
| — replicated? | between-group, 49 pitches (18/10/10/11) | **Yes. Only UNDERHAND was slower; OH/¾/SA did not differ** |
| What does it cost a pitcher who *moves* his slot? | within-athlete, season-over-season, self-selected | **−0.15 mph** (Driveline Mar 2026, no n, blocked) |

**Reading the 0.15 mph correctly:** it is ~1/10th of the between-outing SD and far below F-024's ~1.6 mph detection floor. **As a population mean it is real and negligible. As an individual prescription it is undetectable.** Offsetting registered gains (F-070): **+2.14 run value, +18.3 rpm** for ≥2° droppers.

**Do NOT convert the between-subject null into permission.** "Sidearmers throw just as hard" answers a different question than "what happens if *you* drop down." Dispute #52 attacks the 0.15 mph on survivorship grounds and that attack is not answered.

---

## §5 — ❌ The three absences

1. **F-541 — no prospective arm-slot manipulation exists, in any population, with any performance outcome.** The causal ledger is **5+ variables, 0 manipulations.** The only three "intervention studies" the searches returned were **fabricated** (F-539).
2. **F-543 — shoulder height at release is published by nobody**, despite being the term that decomposes the entire topic and despite MLB necessarily holding it (Statcast computes arm angle *from* the shoulder position). **It is back-computable from public data to ±1.5 in** by rearranging §2's identity. The decomposition of the 2020–2026 league decline into its arm-angle and shoulder-height terms is **free to run and appears unrun.**
3. **F-544 — the reversion denominator is unpublished.** Coverage names ~5 successes and 2 reversions (Gilbert, Skenes) and **no attempt rate, no abandonment rate, and not one named pitcher who tried it and got worse.**

---

## §6 — 🎯 COACHING: the one protocol this file produces

### "Did he change his ARM, or did he just get LOWER?"

The question to ask after any slot change, and until now there was no way to answer it.

**What you need:** release height (any tracking system), arm angle, and his height.

**The rule of thumb, at a normal slot:**
> ## 1° of arm angle ≈ 0.35 in of release height.
> ## Anything beyond that is his shoulder, not his arm.

**Worked example.** A pitcher at 50° drops to 45° (−5°).
- Expected release-height drop from the arm alone: 32.3 × (sin 50° − sin 45°) = **1.9 in**
- Observed release-height drop: **4.0 in**
- Residual: **2.1 in of shoulder drop** → he executed the change by **adding trunk tilt / getting lower in his posture**, not by changing his arm.

**Why you care which one it was:**

| He changed it at the... | Velocity | Command | Elbow |
|---|---|---|---|
| **arm** (abduction) | ~free, −0.15 mph (F-538) | unknown — nobody has measured it | probably down (F-070, **direction flagged — F-540**) |
| **trunk** (added tilt) | ~free | **this is the expensive channel** (F-176: plus-command arms sit 5° higher with less lateral tilt) | **up**, per F-070's own stated failure mode |

**On video, the failure looks like:** the slot number moved but the arm looks the same relative to the torso, and the whole torso is leaning further toward the glove side at release. He didn't lower his arm; he tipped over.

**How you'd know it's working:** release height and arm angle tracked together across **≥200 pitches** (F-186's minimum to detect a ~2 in command change) — not one bullpen. **Honest limit: the shoulder-height back-calculation has a ±1.5 in error bar. This detects inches, not tenths of inches.** A 2 in residual is real; a 0.5 in residual is noise.

### What to say to an 85+ arm who asks to drop down

> *"The velocity is not the issue — it'll cost you a tenth or two of a mile an hour and neither of us will be able to see it. The thing we're actually spending is command, and the price depends on how you do it: with your arm, or by tipping your torso over. We're going to measure which one you did."*

**Three caveats that belong in the same breath:**
- **F-176 is cross-sectional.** The 5° command gap describes who commands well; it is not a dial. Price the risk, don't promise the mechanism.
- **Nobody has run the experiment** (F-541). Everything above is observation.
- **Expect a soreness window** (F-545) — offseason or early-season, reduced volume for 2–3 weeks. This is a reasoned precaution, graded WEAK, not a protocol.

---

## §7 — ⚠️ Hazards specific to this topic

1. **TWO INVERTED SIGN CONVENTIONS (F-540).** Statcast: larger = more overhand. The ASMI/Escamilla papers as rendered in F-070: larger = more sidearm. **Any figure moved between them flips sign**, and F-070 appears to contain both, contradicting itself. The torque *direction* of the corpus's load-bearing arm-slot finding is currently supported 2-to-1, not unanimously.
2. **RELEASE-POINT PROXIES (F-536).** Any arm-slot claim older than 2024 built on release point is measuring arm angle at **R² ≈ 0.55.**
3. **HORIZONTAL RELEASE IS NOT A SLOT NUMBER (F-537).** Geometry says it *should* be the better proxy (0.43 vs 0.36 in/deg at 50°); it measured far worse (r = −0.38 vs 0.74) because it carries rubber position and stride direction. **Falsifiable prediction: control for those two and it becomes a good proxy.**
4. **🚨 FABRICATION LAUNDERING (F-539).** accio.com, already blacklisted at F-266, resurfaced on this topic and **the search layer restated its fabricated numbers as findings of the Journal of Applied Biomechanics, the NCAA and the University of Florida, with no byline.** F-266's rule is insufficient. **New protocol: read the URL list, not just the prose; and re-query any number lacking author/title/DOI — a real finding returns the same number, a generated one returns a new number or vanishes.** This test caught it today.
5. **SNIPPET-LEVEL DISCREPANCIES, registered unresolved:** Hancock's start point (27° vs the corpus's 23°); the Savant leaderboard launch date (2022 vs 2020 vs Aug 2024). **Do not register any of them.**

---

## §8 — Verification queue opened by this file

| Item | Why it matters | Cost |
|---|---|---|
| **PMID 39744973** (Sports Biomech 24(8), n = 66) — slot variable sign + stated convention | **Settles F-540 and the stress half of F-070.** The cheapest open item in the corpus. | one table |
| **PMC10601404** (Escamilla/Fleisig 2023) — convention + torque direction | the other side of F-540 | one table |
| **"Direct arm angle versus release-based proxies…"** (SUNY Buffalo/Columbia/Wake Forest) — journal, year, authors, DOI | F-536 is currently an **incomplete citation**; existence likely (3 institutional repositories) but **UNREAD** | one page |
| **"Differences Among Overhand, Three-Quarter, and Sidearm…"** — confirm the **86.3 mph** belongs to the n = 207 sample | would make this one of the corpus's few true ≥85 mph samples | one table |
| **PMC13519161** — "Sidearm Deliveries… 927 Pitchers (2020–2025)" | the **"favorable performance profile"** half is on-mission and entirely unread | one abstract |
| **PMID 42661912** — "Segmental Momentum Sequencing… Different Arm Slots" (collegiate) | sequencing×slot interaction; snippet says sidearm relationships weaker — **likely just subgroup power** | one abstract |
| **Driveline (Mar 2026)**, "Pitchers are going low…" — the **n** behind −0.15 mph | the best within-athlete number in the topic has no sample size | blocked domain |
