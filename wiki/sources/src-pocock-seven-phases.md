---
type: source
branch: sources
tags: [loop-engineering, pocock, workflow]
sources: []
url: https://www.aihero.dev/my-7-phases-of-ai-development
author: Matt Pocock
published: 2026-03-16
raw: raw/2026-10-12-pocock-seven-phases.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "My 7 Phases Of AI Development" (2026-03-16)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-seven-phases.md` · Up: [[sources]]

## Summary
The phases around the loop. In order:
1. Idea, refined with `/grill-me`
2. Research (optional), cached as `RESEARCH.md`
3. Prototype (optional), to impose taste
4. PRD, describing the end state
5. Kanban board of tickets with blocking relationships
6. **Execution with Ralph loops**, possibly AFK and parallel on non-blocking tickets
7. QA: an agent-written QA plan plus human review, which feeds new tickets back into phase 5

See [[seven-phases-of-ai-development]].

## Key claims
- Research assets save repeated exploration in fresh context windows, but they *"can go out of date"*, so delete them after the sprint. See [[context-and-state]].
- AFK execution works when the agents have research, prototype code, a clear PRD, and tickets with acceptance criteria. See [[afk]].
- Phases 5–7 repeat *"multiple times"*. QA is the outer loop around execution. See [[human-in-the-loop]].
- Code review *"may not always be necessary (especially with gray box architectures)"*. See [[agent-experience]].

## Pages touched
[[seven-phases-of-ai-development]], [[goal-spec]], [[afk]], [[human-in-the-loop]], [[orchestrator-workers]], [[context-and-state]]
