---
type: practice
branch: practice
tags: [loop-engineering, practice, claude-code, scheduling]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]"]
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Claude Code scheduling options

[[claude-code]] offers three ways to schedule recurring or one-off work, plus GitHub Actions ([[src-claude-code-scheduled-tasks]]). Choosing among them is a [[trigger]] and [[guardrails-and-permissions]] decision. Up: [[practice]].

| | Cloud Routines | Desktop scheduled tasks | `/loop` (session) |
|---|---|---|---|
| Runs on | Anthropic cloud | your machine | your machine |
| Machine must be on | no | yes | yes |
| Open session needed | no | no | yes |
| Survives restarts | yes | yes | restored on `--resume`, with exceptions |
| Local files | no (fresh clone) | yes | yes |
| MCP | connectors per task | config files and connectors | inherits from session |
| Permission prompts | none, runs autonomously | configurable per task | inherits from session |
| Minimum interval | **1 hour** | 1 minute | 1 minute |

Source: [[src-claude-code-scheduled-tasks]].

> Rule of thumb from the docs: cloud for reliability without your machine, Desktop for local files and tools, `/loop` for quick polling during a session.

## Session cron tools
`CronCreate` (5-field cron, recurring or one-shot), `CronList` and `CronDelete` (by 8-character ID). Up to 50 tasks per session. Times are in local timezone. There is no `L`, `W`, `?` or name aliases. One-shot reminders can be given in natural language (*"in 45 minutes, check whether the integration tests passed"*) ([[src-claude-code-scheduled-tasks]]).

## Beyond the session
- **GitHub Actions** with a `schedule` trigger keeps the loop running *"after you close the laptop"* ([[src-osmani-loop-engineering]]).
- **Hooks** fire shell commands at lifecycle points ([[src-osmani-loop-engineering]]).

## Related
[[claude-code-loop]] · [[scheduled-loop]] · [[trigger]]
