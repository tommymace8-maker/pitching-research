# Pitching Research Program

A standing three-agent research team studying the body and the pitching motion, so I can become a better pitching coach.

## Population scope — 85 MPH floor

This program is built for **elite throwers only**: top high-school prospect (showcase circuit, D1-committed, draft-followed) through college and professional. The athlete already throws **85+ mph** and is chasing 90-95+.

Nothing in this library is written for youth or average high-school pitchers. Growth-plate injuries, youth pitch counts, and beginner mechanics are out of scope. Studies sampling youth or unselected HS pitchers are either excluded or flagged *"sample does not match our population — directionally suggestive only."*

## Mission — make pitchers better

This is a **performance development** program, not an injury-prevention one. The question driving every cycle is *how does this athlete get better*: more velocity, sharper stuff, better command, more competitive outs.

Research effort goes to:
- **Velocity** — what actually adds mph to an arm already at 85+, and how to train it
- **Stuff** — pitch design, spin efficiency, seam-shifted wake, movement profiles, tunneling, arsenal construction
- **Command** — the biggest lever most 90+ arms leave on the table
- **Training transfer** — strength, plyos, weighted balls, med ball, sprint/jump: what shows up on the gun and what doesn't
- **Skill acquisition** — motor learning, cue design, constraints, variability, what transfers from pen to mound
- **Pitchability** — sequencing, usage, attacking hitters; what separates stuff from outs

Injury material is a **supporting constraint, not a research topic.** No cycles on injury mechanisms, rehab, or risk modeling. When a development method carries a real stress cost, it gets tagged in a line and the work moves on.

## The team

| Agent | Role | What it owns |
|---|---|---|
| `anatomy-physiology` | Doctoral-level anatomy / physiology / exercise science expert | Structures, tissue behavior, energy systems, injury mechanisms, recovery |
| `biomechanist` | PhD sports biomechanist | Phases, kinematics, kinetics, kinematic sequence, motion-capture data |
| `pitching-coach` | Certified pitching coach | Interrogates the other two about each position in the delivery, then translates science → cue → drill |

Agent definitions live in [.claude/agents/](../.claude/agents/). Edit those files to change how an agent thinks.

## How a research day works

1. **Deep pass** — Anatomy and Biomechanics each research their assigned topic and update their library file.
2. **Field sweep** — the Coach scouts public social sources (X, YouTube, blogs, Substacks, podcasts, forums) for genuinely new ideas circulating in the industry right now, and labels each PROMISING / UNPROVEN / DEBUNKED / MARKETING.
3. **Interrogation** — the Coach asks the other two pointed questions about a specific position in the delivery ("at foot plant, what's actually resisting valgus torque, and in what order?"), and routes every scouted idea through them for evaluation.
4. **Cross-examination** — all three read each other's output and each issues at least two challenges. Every challenge gets answered: conceded or defended with evidence. Nothing unchallenged makes it into the library.
5. **Translation** — the Coach converts surviving findings into: **science → cue → drill → what failure looks like on video.**
6. **Write-up** — reports land in `daily/YYYY-MM-DD-*.md`; durable knowledge folds into `library/`; unresolved arguments go to `library/open-disputes.md`.

### On disagreement
Manufactured consensus is a failure state. When the three can't agree, that argument gets logged with the strongest evidence on each side and what would settle it — an honest open dispute is more useful than a fake answer.

## Structure

- `library/` — the growing permanent reference documents
  - `anatomy-physiology.md`
  - `biomechanics.md`
  - `coaching-translation.md` — the science-to-cue playbook
  - `open-disputes.md` — arguments the three agents haven't resolved
  - `idea-scouting.md` — new ideas from the field, with verdicts
- `daily/` — one dated report per research day
- `README.md` — this file

## Running a day

In Claude Code from the project root:

```
Run today's pitching research cycle — see research/README.md
```

Or set it up to run automatically with `/schedule` (a daily cloud agent) or `/loop`.

## Ground rules for all three agents

- Every claim gets labeled: **ESTABLISHED** / **EMERGING** / **FOLKLORE**.
- Real citations only — author, year, link. Never invent a source.
- Numbers get units, ranges, and the population/level they were measured on.
- Correlation is not causation, and most pitching-injury literature is cross-sectional.
- Anything medical gets flagged for a physician, PT, or ATC. This is education, not treatment.
