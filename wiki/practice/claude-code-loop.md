---
type: practice
branch: practice
tags: [loop-engineering, practice, claude-code, scheduling]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-pocock-ralph-plugin]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: solid
---
# Claude Code `/loop`

`/loop` is a bundled skill that re-runs a prompt while a [[claude-code]] session stays open. It is *"the quickest way to run a prompt on repeat"* ([[src-claude-code-scheduled-tasks]]). Up: [[practice]].

## Three modes
| You provide | Example | Behaviour | Pattern |
|---|---|---|---|
| interval + prompt | `/loop 5m check the deploy` | fixed cron. Units are `s`/`m`/`h`/`d`, rounded to clean cron steps. | [[scheduled-loop]] |
| prompt only | `/loop check whether CI passed and address any review comments` | Claude picks a delay of 1 min–1 h after each iteration | [[self-paced-loop]] |
| nothing (or interval only) | `/loop`, `/loop 15m` | built-in maintenance prompt, or your `loop.md` | [[babysitter-loop]] |

You can pass a skill as the prompt (`/loop 20m /review-pr 1234`), but only skills Claude may invoke on its own will execute ([[src-claude-code-scheduled-tasks]]).

## `loop.md`
- `.claude/loop.md` (project) takes precedence over `~/.claude/loop.md` (user). It replaces the built-in prompt for a bare `/loop` only.
- Plain markdown, written as if you were typing the prompt. **Edits apply on the next iteration**, so you can tune a running loop. Content beyond 25,000 bytes is truncated.

All from [[src-claude-code-scheduled-tasks]]. See [[writing-a-loop-prompt]].

## Stopping
- `Esc` clears the pending self-paced wakeup.
- Claude can stop the loop itself (`ScheduleWakeup(stop: true)`).
- Silent iterations get one fallback wakeup about 20 min later, then the loop ends.
- Fixed-interval loops run until cancelled or until the **7-day** expiry.

All from [[src-claude-code-scheduled-tasks]]. See [[termination]].

## Limits
- It is session-scoped and only fires while Claude Code is running and idle. Backgrounding the session carries tasks over.
- No catch-up for missed fires.
- A self-paced loop isn't restored on `--resume`.

All from [[src-claude-code-scheduled-tasks]]. For durable schedules, see [[claude-code-scheduling]].

## Contradictions & open questions
- **Context build-up.** `/loop` iterations run inside the same session, as scheduled prompts that fire *between your turns* ([[src-claude-code-scheduled-tasks]]). Pocock's critique of in-session Ralph is that context accumulates into the [[smart-zone|dumb zone]] ([[src-pocock-ralph-plugin]]). If it holds, it would apply here too *(synthesis)*. The docs don't say whether `/loop` clears or compacts between iterations. Short polling prompts, like babysitting a PR, are probably less affected than build loops. Cursor's `/loop` is the closest analogue: Tan runs overnight loops with it in one session and keeps them lean with subagents ([[src-tan-pstack-guide-overnight]]). See [[open-questions]].

## Related
[[claude-code-goal]] · [[loop-primitives]] · [[building-a-ralph-loop]]
