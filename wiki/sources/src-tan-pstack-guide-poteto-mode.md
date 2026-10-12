---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, routing, guide]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/docs/guide/02-poteto-mode.md
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-guide-poteto-mode.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack guide 2 — "Route work through /poteto-mode"

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-guide-poteto-mode.md` · Up: [[sources]]

## Summary
`/poteto-mode` reads the principles, matches the task to one of **23 playbooks**, copies that playbook's steps into the todo list, and calls the other skills as each step needs them. *"Your words carry the intent, and the skill carries the rigor."* See [[pstack]].

## Key claims
- Routes include Investigation, Bug fix, Feature, Refactoring, Perf issue and figure-it-out, plus hillclimb, babysit, autopilot, orchestrate, session pickup, pause safely and others. A skipped step stays visible as `skip: <reason>`. See [[decision-step]].
- **A prompt has five things:**
  1. the goal
  2. a **done check that can pass or fail**
  3. the proof you want to see
  4. what you already know
  5. real constraints

  Leave out *the how* and, at first, *your theory of the cause*. See [[writing-a-loop-prompt]].
- **Restate before acting:** for noisy reports, make the first step a plain-English restatement, *"don't change any code yet."*
- **"new task"** makes it re-match a playbook rather than continue the previous one, so context from the last task doesn't steer the new one. See [[smart-zone]].
- **Isolation:** prefer cloud subagents, each with its own VM and branch. Locally, use one worktree per task. Worktrees pile up, and the Worktree cleanup playbook deletes only what the evidence clears. See [[isolation]].
- **Pitfall:** don't list skills in the prompt, because the playbook already sequences them.

## Pages touched
[[pstack]], [[writing-a-loop-prompt]], [[decision-step]], [[isolation]], [[smart-zone]]
