---
type: source
branch: sources
tags: [loop-engineering, pocock, ralph, how-to]
sources: []
url: https://www.aihero.dev/getting-started-with-ralph
author: Matt Pocock
published: 2026-01-08
raw: raw/2026-10-12-pocock-getting-started-with-ralph.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "Getting Started With Ralph" (2026-01-08)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-getting-started-with-ralph.md` · Up: [[sources]]

## Summary
A step-by-step guide to a first [[ralph-loop]]. *"You run the same prompt repeatedly. The AI picks its own tasks from a PRD. It commits after each feature. You come back later to working code."* It turns Huntley's bare `while` loop into two scripts, a HITL `ralph-once.sh` and a capped AFK `afk-ralph.sh`, run inside a Docker sandbox. See [[building-a-ralph-loop]].

## Key claims
- **Setup:** Claude Code plus Docker Desktop 4.50+ (`docker sandbox run claude`). The working directory is mounted at the same path, git config is injected, and there is one sandbox per workspace. See [[isolation]].
- **State:** a `PRD.md` written with plan mode defines the end state, and an empty `progress.txt` tracks what is done. *"Claude reads both on each loop iteration."* See [[context-and-state]] and [[goal-spec]].
- **`ralph-once.sh`:** `--permission-mode acceptEdits` so the loop doesn't stall, plus the instruction *"ONLY DO ONE TASK AT A TIME."* Run it, watch it, run it again. See [[human-in-the-loop]].
- **`afk-ralph.sh <iterations>`:** wraps the call in a `for` loop with `set -e`, an **iteration cap** (*"prevent runaway costs"*), print mode (`-p`), and a **completion sigil** `<promise>COMPLETE</promise>` that exits early. See [[termination]].
- **Make it your own:** swap the task source (GitHub Issues, Linear, beads), change the output (a branch and PR per iteration), or run other loop types (coverage, lint, duplication, entropy). *"Any task that fits 'look at repo, improve something, commit' works with Ralph."* See [[improvement-loops]].

## Pages touched
[[building-a-ralph-loop]], [[ralph-loop]], [[termination]], [[isolation]], [[context-and-state]], [[goal-spec]], [[human-in-the-loop]], [[afk]], [[improvement-loops]], [[matt-pocock]]
