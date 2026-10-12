---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, primary, trust]
sources: []
url: https://x.com/poteto/status/2069824386283319343
author: Lauren Tan
published: 2026-06-24
raw: raw/2026-10-12-tan-loops-you-can-trust.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Tan — "Loops You Can Trust" (X article, 2026-06-24)

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-loops-you-can-trust.md` · Up: [[sources]]

## Summary
Tan's core essay on loops, built on Andy Grove's *High Output Management*. A breakfast factory is scheduled around its slowest step, the three-minute egg. Likewise, **verification is the limiting step** of agentic software development: *"the stage that constrains the output of the whole loop."* So you must teach agents to verify **before** you think about loops. Otherwise *"running loops naively just creates compounding slop."* The essay traces how this developed: `/control-glass` (a CDP-driven app control skill), then worktrees for parallel agents, then pstack (every recurring failure mode turned into a skill), then Cursor Automations, which let *"the pstack loop … finally start without me."*

## Key claims
- **Limiting step.** Making the toast and coffee faster doesn't deliver breakfast sooner. Repro and verification take longest because they wait on humans. Hand them to agents and you free *"the most precious resource"* to run several loops. See [[verification]] and [[earned-autonomy]].
- **Agents need your tools.** *"agents should get the same signals human engineers use … Agents need to be able to see what I see, and use the tools I use."* See [[verification-skill]].
- **Parallelism without quality is rework.** With worktrees she could run many agents, but *"Parallelization just gave me more to review and discard."* See [[operator-debts]].
- **Managerial leverage.** Do the work once as a reusable skill or tool and every future run inherits it. *"The agents improved because their instructions carried the scars from previous runs."* See [[build-the-lever]].
- **A self-starting maintenance line:** Slack report → triage (attachments, version, duplicates, code and history) → repro twice in a real cloud build, with screenshots and video → fix (test when possible, smallest provable fix, before/after, draft PR). The thread stays open for humans to reject the repro. See [[stage-gated-pipeline]].
- **Every stage can stop the line.** A "not a bug", "can't repro" or "too risky" verdict is a *useful* outcome, because it keeps bad work from reaching costlier stages. *"Slack has become the control room."*
- **Trust but verify.** *"'I fixed it' isn't good enough."* Artifacts (failing→passing test, before/after video, trace, heap snapshot) *"beat a plausible sounding explanation."* See [[observation]].
- **Scripts for deterministic steps, agents for fuzzy ones:** *"If a script can do it deterministically, use the script."* See [[build-the-lever]].
- **The decision log:** `/show-me-your-work` keeps an append-only log, checks it against the transcript, and has a different model family review it. See [[observability]].
- **StyleX lesson:** a ~400K-line migration PR was pixel-perfect yet still hid z-index and specificity bugs. It became an automation that migrates **one leaf component per day** with before/after computed styles across themes and states. *"catch defects at the lowest value stage."* See [[task-sizing]] and [[improvement-loops]].
- **Five steps:**
  1. Do the work by hand first.
  2. Give agents your tools.
  3. Make every stage prove its work and stop when it misses the bar.
  4. Read transcripts and turn failures into tools, skills or evals.
  5. Make the loop autonomous only after it earns trust.

  See [[earned-autonomy]].

## Pages touched
[[verification]], [[earned-autonomy]], [[verification-skill]], [[build-the-lever]], [[stage-gated-pipeline]], [[observability]], [[observation]], [[task-sizing]], [[improvement-loops]], [[operator-debts]], [[isolation]], [[software-factory]], [[event-driven-loop]], [[lauren-tan]], [[cursor]], [[pstack]]
