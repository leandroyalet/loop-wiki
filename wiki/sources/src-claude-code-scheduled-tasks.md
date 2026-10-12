---
type: source
branch: sources
tags: [loop-engineering, docs, claude-code]
sources: []
url: https://code.claude.com/docs/en/scheduled-tasks
author: Anthropic (Claude Code docs)
published: unknown
raw: raw/2026-10-11-claude-code-scheduled-tasks.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Claude Code docs — "Run prompts on a schedule"

**Author:** [[anthropic]] · **Raw:** `raw/2026-10-11-claude-code-scheduled-tasks.md` (fetched 2026-10-11) · Up: [[sources]]

## Summary
The official reference for the `/loop` bundled skill and the session-scoped cron tools (`CronCreate`, `CronList`, `CronDelete`) in [[claude-code]]. It is the most precise source in the wiki on how a production loop is triggered, paced and stopped.

## Key claims
- There are **three scheduling surfaces**: cloud Routines (minimum interval 1 h, no machine needed), Desktop scheduled tasks, and `/loop`, which is session-scoped and runs at 1 min minimum. See [[claude-code-scheduling]].
- `/loop` has **three modes**:
  1. interval + prompt gives a fixed cron
  2. prompt only makes it **self-paced**: Claude picks a delay between 1 min and 1 h after each iteration
  3. nothing runs the **built-in maintenance prompt** or `loop.md`

  See [[claude-code-loop]] and [[self-paced-loop]].
- The **built-in maintenance prompt** works in this order: continue unfinished work, tend the PR (comments, CI, conflicts), then clean up. It does not start new initiatives. Irreversible actions run only if the transcript already authorized them. See [[guardrails-and-permissions]] and [[babysitter-loop]].
- **`loop.md`** (in `.claude/` or `~/.claude/`) replaces the default prompt. Edits take effect on the next iteration. It is truncated above 25,000 bytes. See [[writing-a-loop-prompt]].
- **Stopping:**
  - `Esc` clears a pending self-paced wakeup.
  - Claude can stop the loop itself with `ScheduleWakeup(stop: true)`.
  - An iteration that neither reschedules nor stops gets one fallback wakeup about 20 minutes later and then ends.

  See [[termination]].
- **Seven-day expiry** for recurring tasks: *"This bounds how long a forgotten loop can run."* See [[termination]] and [[failure-modes]].
- **Jitter:** recurring tasks run late by a fixed offset derived from the task ID, up to 30 min. One-shots set for :00 or :30 run up to 90 s early. **No catch-up** for missed fires. See [[trigger]].
- For **event-driven** work, it points to Channels (CI pushes failures into the session) and the **Monitor** tool, which streams script output and is *"often more token-efficient and responsive"* than polling. See [[event-driven-loop]].
- Use `/goal` to work "turn after turn toward a condition rather than on an interval." See [[claude-code-goal]].
- A session holds at most 50 scheduled tasks. `CLAUDE_CODE_DISABLE_CRON=1` disables scheduling entirely.

## Pages touched
[[claude-code-loop]], [[claude-code-scheduling]], [[claude-code-goal]], [[self-paced-loop]], [[scheduled-loop]], [[event-driven-loop]], [[babysitter-loop]], [[trigger]], [[termination]], [[guardrails-and-permissions]], [[failure-modes]], [[writing-a-loop-prompt]], [[claude-code]]
