# Motor imagery and mental practice — does rehearsing a pitch build anything?

**Opened 2026-09-25.** Companion to `FINDINGS.md` F-473→F-482.

⚠️ **THIS FILE WAS BUILT IN A FULLY EGRESS-BLOCKED CYCLE. NOT ONE CLAIM BELOW WAS VERIFIED AT A PRIMARY SOURCE.** Every empirical number is **SNIPPET-ONLY** (a search summariser's paraphrase). Per the standing rule, a snippet-level claim is a **lead, not a finding**. The *derivations* in §2–§4 are source-independent arithmetic and do not depend on the snippets except where a number is explicitly imported — and §2 exists precisely to show that importing one of those numbers is illegitimate.

**Egress note, for the record:** every domain the operating brief lists as WORKING (nature.com, frontiersin.org, sportrxiv.org, ncbi.nlm.nih.gov/pmc, jstage, ijspt.scholasticahq.com, tandfonline.com, journals.sagepub.com) returned `EGRESS_BLOCKED` on 2026-09-25, as did plos.org, semanticscholar.org, europepmc.org, crossref, scispace and thesportjournal.org. `curl` through the agent proxy returned `CONNECT tunnel failed, response 403` for every host tried. **The brief's egress map is stale. WebSearch was the only channel.** Cf. F-462 — the probe was run rather than assumed, and this time the probe came back negative.

---

## 1. Why this topic, and what makes it structurally unusual

This corpus runs roughly **30:1 cross-sectional to intervention**. Its recurring failure mode is a *marker* — an observed association — being sold to a pitcher as a *lever*. Stride length and extension both died this way.

**Motor imagery is the mirror-image case, and that is the reason to open it.** The imagery literature is overwhelmingly made of **randomised intervention designs with control groups**. Nobody is correlating imagery vividness against velocity in 149 pros and calling it a cue. People assigned athletes to imagine things, kept a control group, and measured. On the corpus's own marker/lever axis, **imagery is a lever.**

And yet the corpus should not adopt a single magnitude from it. §2 is why.

---

## 2. ⭐ THE STANDARDIZED-EFFECT IMPORT FALLACY

### 2.1 The naive import, run to its conclusion

Take the pooled effect the imagery literature actually reports (SNIPPET-ONLY):

> Simonsmeier, Androniea, Buecker & Frank (2020), *International Review of Sport and Exercise Psychology* 14(1) — imagery interventions in sport, **d = 0.431, 95% CI [0.298, 0.563]**.

Now take this corpus's own registered command scale:

- **F-186** — within-pitcher miss-distance SD ≈ **10 inches**.
- **F-170** — one inch of miss distance ≈ **0.3 FIP**.

Import the standardized effect the obvious way:

```
Δ_command = d × σ_command = 0.431 × 10 in = 4.31 inches
ΔFIP      = 4.31 in × 0.3 FIP/in         = 1.29 FIP
```

**A pitcher sits in a chair for fifteen minutes, three times a week, and takes 1.29 off his FIP.**

### 2.2 The reductio

That number is not merely large. It is, by a wide margin, **the largest effect in a 472-finding registry.** For scale:

| Intervention | Corpus finding | Magnitude |
|---|---|---|
| **Imagery, naive d-import** | this file | **4.31 in ≈ 1.29 FIP** |
| Throwing off a mound vs flat ground | F-464 | ~2.0 mph (in a 76.5 mph sample) |
| One full season of command development | F-309 | 4.52 pts |
| Catcher-framing contamination of that gain | F-309 | 3.69 pts |
| A 1-SD increase in Stuff+ | F-170 | ≈ 0.3 FIP |

The import says imagery is worth **more than four times a one-SD Stuff+ gain**, for free, with no arm cost, using a technique every mental-skills coach in professional baseball has been selling since the 1980s.

**Second reductio, from the detection side.** An effect of 4.31 inches would need only **42 tracked pitches** to establish at 80% power (§3). Forty-two pitches is two bullpens. An effect that size would have been obvious to every pitching coach who ever lived, and it would have been rediscovered independently a thousand times. **It has not been.** The import is wrong.

### 2.3 Where exactly the import breaks

A standardized effect is a **ratio**, not a quantity:

```
d = Δ / σ
```

Importing `d` from population A into population B and computing `Δ_B = d̂ · σ_B` is valid **if and only if**

```
Δ_A / σ_A  =  Δ_B / σ_B
```

— that is, only if **the raw benefit is proportional to the receiving population's scatter.** Nothing licenses that. The samples underneath these meta-analyses are largely undergraduates and novices, who have *both* a larger σ *and* far more headroom. The assumption embedded in the naive import is that a group with three times the scatter gets three times the raw benefit, which is an empirical claim nobody has made, let alone tested.

The honest alternative anchor is the **raw import**, `Δ_B = Δ_A` — keep the effect in inches, not in SDs. But:

> ### 🚨 **META-ANALYSES DISCARD THE RAW UNITS. STANDARDIZATION DESTROYS EXACTLY THE NUMBER YOU NEED.**

`d = 0.431` is unrecoverable back into inches, centimetres, or degrees without going to each primary study — which in this cycle was impossible, and in general is the whole reason the pooled figure gets quoted instead.

### 2.4 The rule this produces

**A pooled `d` tells you a DIRECTION and a CONFIDENCE. It does not tell you a SIZE in another population, and multiplying it by the receiving population's SD is not a conversion — it is an assumption wearing a conversion's clothes.**

This is a **new hazard class** for the corpus, and it is general: it applies to every meta-analytic `d` this corpus will ever meet, in any topic. It sits beside:

- **F-465** — the unit-mislabelled table (a real paper printing mph under an `m/s` header).
- **F-382** — peer-reviewed laundering.
- **F-373** — an abstract contradicted by its own table.
- **F-013 / extension** — a marker sold as a lever.

**F-473 registers it.** Its operating instruction: **when you meet a pooled `d`, ask what the raw units were before standardization. If you cannot recover them, you have a direction and not a magnitude — say so, and never multiply.**

---

## 3. What a program could actually detect

F-186's power form (paired / one-sample against a within-pitcher baseline, α = .05 two-sided, 80% power):

```
n = (z_.975 + z_.80)² · σ² / Δ²  =  7.849 · σ² / Δ²
```

With σ = 10 in (F-186):

| Effect Δ | Pitches per condition | Reality |
|---|---|---|
| 4.31 in (the naive import) | **42** | two bullpens — and it would already be famous |
| 2.0 in | **196** | ✅ reproduces F-186's ~200 exactly |
| 1.0 in | **785** | a full fall, one condition |
| 0.5 in | **3,140** | not available to any college program |

### 3.1 The clustering correction nobody applies

Pitches within a bullpen are **not independent**. With cluster size `m` and intraclass correlation ρ, the design effect is `1 + (m−1)ρ`. A 25-pitch bullpen at a modest ρ = 0.10:

```
DE = 1 + 24(0.10) = 3.4
```

So the 785 pitches needed for one inch become **~2,670**. ⚠️ **ρ for pitch location within a bullpen has never been published for any population** — 0.10 is an assumption, stated as one.

### 3.2 The affordability threshold — the number to actually carry

Invert it. Given a realistic budget of **400 tracked declared pitches per condition** across a fall, the **minimum detectable effect** is:

```
MDE = σ · √(7.849 / n) = 10 · √(7.849/400) = 1.40 inches          (independence assumed)
MDE = 10 · √(7.849/117.6) = 2.58 inches                            (at DE = 3.4)
```

> ### **A COLLEGE PROGRAM CANNOT DETECT AN IMAGERY EFFECT ON COMMAND SMALLER THAN ABOUT 1.4 INCHES — AND REALISTICALLY NOT SMALLER THAN ~2.6 INCHES.**

This is the cycle's hardest result and it **cuts against running the experiment at all.** F-476 registers it.

---

## 4. The decision rule that survives the arithmetic

If the effect cannot be priced (§2) and cannot be measured (§3), the usual question — *"is it proven?"* — has no answer available, and waiting for one is waiting forever.

**So ask the other question: what does it cost?**

| Cost channel | Imagery |
|---|---|
| Arm / throw count | **zero** |
| Money | **zero** |
| Practice-plan time | 15 min, displaceable to travel, treatment table, pre-sleep |
| Opportunity cost vs. another block | **near-zero — it does not compete for throws** |
| Downside risk | one plausible channel only: **negative rehearsal** (§6) |

**This is a free-rider decision, not an evidence decision.** An intervention with a verified direction, an unknown magnitude, and a near-zero cost is worth adopting *even if you will never be able to prove it worked in your own program* — and the honest coaching sentence says exactly that, rather than manufacturing a confidence the arithmetic does not support. **F-481.**

⚠️ **THE TRAP TO AVOID:** "free" is not "large." Adopt it on cost, and then **do not count it as a development win**, because §3 says you will never be entitled to. A program that adopts imagery and then attributes a good fall to it has learned nothing and will carry a false lever forward.

---

## 5. The cognitive-task moderator, and where the headroom probably is

SNIPPET-ONLY, from the founding meta-analysis:

> Driskell, Copper & Moran (1994), *Journal of Applied Psychology* 79(4):481–492 — k = 35, **overall d = 0.53**. Mental practice was **more effective the more the task involved cognitive components** (reported **r = 0.44**).

Applied to an 85+ arm, this points somewhere specific. His delivery is **automatized** — that is what "mechanics already good" means, and it is the population constraint this corpus runs under. The execution layer is exactly the low-cognitive-load case where Driskell's moderator predicts the *smallest* return.

What is **not** automatized for a college arm:

- pitch selection and sequencing (F-294→F-303)
- count strategy (F-278→F-283)
- the runner-on-first decision set (F-316→F-325)
- times-through-the-order adjustments (F-286→F-292)
- the pre-pitch routine and its restart after a disruption

**Mechanism-consistent prediction: imagery's headroom in this population is in the DECISION layer, not the EXECUTION layer.** F-478.

> ### ⚠️ AND THE BIOMECHANIST'S OBJECTION TO §5 IS CORRECT AND IS RECORDED AS SUCH
> Driskell's moderator is measured **ACROSS TASKS** (a card-sort versus a dart throw), not **ACROSS LAYERS WITHIN ONE TASK**. Applying a between-task moderator to the within-task decomposition of pitching is **structurally the same move §2 just condemned.** The coach does not get to condemn the standardized-effect import at the top of the file and then perform an analogous extrapolation at the bottom.
>
> **The coach concedes the structure and keeps the recommendation on COST, not on evidence** (§4). §5 is graded **WEAK**, and it is a hypothesis about where to look, **not a finding**. See Dispute #42.

---

## 6. Mechanism — what the brain work does and does not show

SNIPPET-ONLY: *Pitching-specific facilitation of upper-limb corticospinal excitability during motor imagery of sports motor skills*, **Experimental Brain Research (2026), PMID 41557017**. TMS over M1, motor-evoked potential amplitudes. Baseball motor imagery facilitated corticospinal excitability in **abductor pollicis brevis (APB)**; imagery **with a model video** additionally facilitated **flexor carpi radialis (FCR)**; other recorded muscles not facilitated versus rest.

**THE ANATOMIST'S READ, and it is deflationary:**

1. **This is an ACUTE STATE MEASURE TAKEN DURING IMAGERY, NOT A TRAINING ADAPTATION.** MEP facilitation during motor imagery is among the most reproducible findings in motor neuroscience and has been known for thirty years. **It has never, by itself, predicted a performance gain.** The step from "the corticospinal tract is more excitable while he imagines" to "imagining builds the skill" is unearned.
2. **APB is a THUMB muscle.** Abductor pollicis brevis contributes essentially nothing to ball velocity. Its only plausible pitching relevance is at the **ball–hand interface** (`library/ball-hand-friction.md`, 2026-09-21) — finger force and release. That is an interesting lead and it is not a velocity result.
3. **The muscles that actually make a pitch were not shown to be facilitated** — lats, pecs, subscapularis, and the entire hip/trunk chain. TMS reaches distal hand and forearm representations easily and proximal/trunk representations poorly, so this is at least partly a **measurement-accessibility artefact rather than a physiological ranking** — but the paper cannot be used to claim the delivery's prime movers were engaged, because they were not measured.

**Verdict: the mechanism paper establishes that imagery engages the motor system in a pitching-specific, muscle-specific way. It establishes nothing about velocity, and nothing about training.** F-477.

**Downside channel.** The same mechanism is the one honest argument for imagery having a *negative* branch: if imagery drives task-specific corticospinal facilitation, then vividly rehearsing a pitch sailing to the backstop is the nervous system rehearsing that. ⚠️ **This is an inference, not a result — nobody has run negative imagery against a throwing outcome.** It is the field's most-repeated coaching claim and it is UNPROVEN.

---

## 7. The baseball-specific evidence base, stated plainly

**One study. n = 6.**

> *The Effects of Video and Cognitive Imagery on Throwing Performance of Baseball Pitchers: A Single Subject Design* — Georgia Southern University ETD #100, also in *The Sport Journal*. 30 pitchers screened on the Movement Imagery Questionnaire–Revised; participants drawn from the **highest and lowest 20%**; **4 in the intervention conditions, 2 constituting the control**; 3-week video-imagery and imagery program; high-school and college pitchers in southeastern Georgia.

- **No velocity reported anywhere.** No 85 mph floor. **SAMPLE MISMATCH — directional only.**
- **Single-subject design, n = 6 total.** By this program's own standing rule — *a conference abstract with no retrievable sample is not evidence for a magnitude* — **this is not evidence for a magnitude either.**
- **Not readable at source** (thesportjournal.org blocked, 2026-09-25). The reported result ("both intervention groups had significantly higher throwing accuracy than the control") is **snippet-only and its inferential basis at n = 6 is unknown.**
- Directionally consistent with §1. Worth nothing as a number. **F-475.**

---

## 8. Dose — what the dose-response literature says, and one import to refuse

SNIPPET-ONLY throughout:

| Source | Population & outcome | Reported optimum |
|---|---|---|
| Paravlic et al. (2018), *Sports Medicine* 48, PMID 29541965 | healthy adults, **muscle strength** | 4 weeks, 3×/week, 2–3 sets, 25 reps, **15 min/session** |
| Driskell, Copper & Moran (1994) | mixed motor + cognitive tasks | optimum session ≈ **20.8 min** |
| Van Kuiken (2004), *J Holistic Nursing* | **guided imagery, health outcomes** | effect rises over **5–7 weeks**, **decreased at 18 weeks** |

**The three converge on 15–21 minutes per session, and that is the only part worth carrying.**

> ### ⚠️ REFUSE THE DECAY CURVE
> The 5–7 week rise / 18-week decay is from a **holistic-nursing meta-analysis of guided imagery on health outcomes.** It is not athletes, not a motor skill, and not a performance outcome. Importing it as "the pitching imagery decay curve" would be a cross-domain transfer of precisely the kind this corpus exists to catch. **The retention profile of an imagery effect on a throwing task is UNKNOWN. F-479.**

Note also that the Paravlic dose is optimised for **muscle strength**, an outcome this corpus's own transfer nulls (F-004, F-358, F-359) say does not reach pitch velocity anyway. **Do not quote the 4-week/25-rep protocol as a pitching protocol.**

---

## 9. What does not exist (searched for, not found) — F-482

1. **No imagery intervention on any pitcher above 85 mph, anywhere.** The population this corpus serves has never been studied on this topic.
2. **No imagery study in baseball with a pitch-location outcome in inches.** Accuracy was scored on a target grid in the one existing study; miss distance in inches — the corpus's own command currency (F-170, F-186) — has never been the outcome.
3. **No imagery study reporting a VELOCITY outcome in pitchers.** Not one.
4. **No test of the "mental bullpen" as a workload substitute.** The trade-press claim is that mental reps are throws without arm cost. Nobody has measured whether they carry any of the training benefit of a throw. **This is the single most testable and most commercially loaded claim in the topic.**
5. **No dose-response curve for imagery on any throwing accuracy outcome.** §8's doses are borrowed from strength and from health.
6. **No study of negative/failure imagery against a throwing outcome**, despite it being the field's most repeated coaching claim (§6).
7. **No published intraclass correlation for pitch location within a bullpen** — which §3.1 shows is load-bearing for every command power calculation this corpus has ever run, including F-186's own ~200.

**Item 7 is the one with reach beyond this topic.** F-186's ~200-pitch figure — quoted throughout the corpus — assumes independent pitches. If ρ > 0 it is an **underestimate**, and every command detection threshold in the registry is optimistic.

---

## 10. Unread queue (blocked 2026-09-25)

| Source | Why it matters |
|---|---|
| Simonsmeier et al. (2020), *IRSEP* 14(1), DOI 10.1080/1750984X.2020.1780627 | the pooled d = 0.431 and **its expertise moderator**; §2's whole premise |
| Toth et al. (2020), *Psychology of Sport and Exercise* 48:101672 | the 24-year replication of Driskell. ⚠️ **This cycle initially mis-recalled its journal as *J Sports Sci*. It is *Psych Sport Exerc*.** |
| Driskell, Copper & Moran (1994), *JAP* 79(4):481–492 | d = 0.53, the cognitive moderator r = 0.44, and **the retention/decay data §8 refused to import from nursing** |
| *Exp Brain Res* (2026), PMID 41557017 | §6 — which muscles, what stimulus intensity, what n |
| *Motor imagery ability in baseball players with throwing yips*, PMC10688651 | direct cross-link to the 2026-09-16 yips cycle |
| Frontiers *Psychology* (2026) 10.3389/fpsyg.2026.1888190 | Bayesian meta-analysis, imagery on basketball skills — a **closed-skill accuracy** analogue |
| Georgia Southern ETD #100 | §7 — the only baseball text |
