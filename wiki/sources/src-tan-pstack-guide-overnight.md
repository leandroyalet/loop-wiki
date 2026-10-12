---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, overnight, guide]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/docs/guide/07-overnight.md
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-guide-overnight.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack guide 7 — "Run work while you sleep"

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-guide-overnight.md` · Up: [[sources]]

## Summary
The operational chapter on unattended loops. What makes them safe *"isn't hope. It's a checkable finish condition, an isolated worktree or cloud agent, and a decision log you audit in the morning."* See [[overnight-contract]].

## Key claims
- **Earn the trust before the loop.** All four must hold before a loop runs unattended:
  1. you've done the task once by hand
  2. the agent has your tools and signals
  3. every stage proves its work and can stop the line
  4. you've turned repeated failures into tools, skills or checks

  *"Until then, run it while you watch."* See [[earned-autonomy]].
- **The overnight contract** has four parts: the goal, the finish condition, permissions, and an escape hatch. Example: *"done means zero old callers, all parser fixtures pass, old api deleted … don't ask me before committing … /loop until done. if you're truly stuck after a few hours, stop and write up why."* See [[overnight-contract]].
- **One iteration:**
  1. check the finish condition
  2. make the smallest justified change
  3. verify it against the real artifact
  4. commit if it made progress, otherwise discard it
  5. log one decision row

  *"Changes that didn't help get discarded, not left to ride. A plateau means pivot, not stop, and the finish condition never quietly relaxes to declare victory."* See [[termination]].
- **Pause safely:** finish or back out of the step, commit a WIP checkpoint, and write a resume note. A fresh chat resumes from the note. See [[context-and-state]].
- **Morning audit:** `/show-me-your-work` keeps a `decisions.tsv` with time, phase, decision, reason, evidence pointer and result. A reviewer from a **different model family** reads the trail and the transcript, and the reply ends with an **Attention** section. *"You're auditing decisions, not re-reading the whole night."* See [[observability]].
- **Queues and programs:**
  - **Autopilot-full** takes independent PRs all the way to merged. One owner agent carries each PR, *"no owner merges on its own verdict"*, a swarm of fresh verifiers checks every push, and *"Only a clean verdict on the patch that merges authorizes the merge."*
  - **Autopilot-stack** does the same but ships nothing. You land the stack yourself.
  - **Orchestrate** is for multi-day programs. A coordinator *"never writes code itself."* It is deliberately heavy and sends simple work back to the overnight contract.

  See [[orchestrator-workers]].
- **Cursor Projects:** a persistent coordinator thread with cloud subagents, so work continues with the laptop closed.
- **Let loops start themselves:** scheduled or event-driven automations. Two rules: *"Every stage can stop the line"* and *"Every stage hands over evidence."* The benny pack is the reference. See [[stage-gated-pipeline]].
- **Pitfall:** *"a duration is not a finish condition."* "work on this for 4 hours" gets you *"four hours of motion instead of a result. Give /loop a predicate that can pass or fail."* See [[goal-spec]].

## Pages touched
[[overnight-contract]], [[earned-autonomy]], [[termination]], [[goal-spec]], [[observability]], [[orchestrator-workers]], [[stage-gated-pipeline]], [[context-and-state]], [[afk]], [[software-factory]], [[cursor]], [[failure-modes]]
