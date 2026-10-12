---
type: source
branch: sources
tags: [loop-engineering, pocock, guardrails, hooks]
sources: []
url: https://www.aihero.dev/this-hook-stops-claude-code-running-dangerous-git-commands
author: Matt Pocock
published: 2026-02-10
raw: raw/2026-10-12-pocock-git-guardrails-hook.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "This Hook Stops Claude Code Running Dangerous Git Commands" (2026-02-10)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-git-guardrails-hook.md` · Up: [[sources]]

## Summary
A Docker sandbox lets Claude run "YOLO" safely because it *"isolates where"* commands run, but it *"doesn't restrict what commands Claude can run."* Your git history lives **inside** the sandbox, so `git reset --hard` or `git push --force` can still destroy weeks of work. The fix is a **`PreToolUse` hook** that pattern-matches Bash commands and exits 2 with a `BLOCKED:` message.

## Key claims
- Blocked by default: `git push` (all variants), `reset --hard`, `clean -f`/`-fd`, `branch -D`, `checkout .` and `restore .`. These are *"safe by default"* rules, not "never allow".
- *"It's a hard guardrail, not a suggestion buried in prose."* Claude sees the message and adapts.
- To verify, clear the context, ask for `git push`, and watch it get blocked.

## Pages touched
[[guardrails-and-permissions]], [[isolation]], [[loop-primitives]]
