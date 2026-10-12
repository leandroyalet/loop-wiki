---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, scheduling, claude-code]
sources: ["[[src-claude-code-scheduled-tasks]]"]
created: 2026-10-11
updated: 2026-10-11
status: stub
---
# Self-paced loop

In a **self-paced loop** the model chooses its own interval. After each iteration, Claude picks a delay between 1 minute and 1 hour *"based on what it observed: short waits while a build is finishing or a PR is active, longer waits when nothing is pending,"* and prints the delay with its reason ([[src-claude-code-scheduled-tasks]]). Up: [[patterns]].

## Where it sits in the loop
The [[decision-step]] controls the [[trigger]]. The model can also trigger [[termination]] itself (`ScheduleWakeup(stop: true)`). A fallback wakeup about 20 minutes later catches iterations that forget to reschedule.

## How to invoke
`/loop <prompt>` with no interval. See [[claude-code-loop]].

## Notes
- Jitter doesn't apply, but the 7-day expiry does. A self-paced loop is **not** restored on `--resume` ([[src-claude-code-scheduled-tasks]]).
- Where available, Claude may use the Monitor tool instead of polling. See [[event-driven-loop]].

## Related
[[scheduled-loop]] · [[babysitter-loop]]
