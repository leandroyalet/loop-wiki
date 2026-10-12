---
type: source
branch: sources
tags: [loop-engineering, pocock, architecture, ax]
sources: []
url: https://www.aihero.dev/how-to-make-codebases-ai-agents-love
author: Matt Pocock
published: 2026-02-26
raw: raw/2026-10-12-pocock-codebases-agents-love.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "How To Make Codebases AI Agents Love" (2026-02-26)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-codebases-agents-love.md` · Up: [[sources]]

## Summary
*"AI is not a super-powered developer. It's a new starter with no memory"*, like the man in *Memento*, and *"You're spawning 20+ new starters a day."* The codebase, *"way more than your prompt or your AGENTS.md file"*, decides the output. The prescription is **deep modules** (*A Philosophy of Software Design*) used as **grey-box modules**: you own the interface, AI owns the implementation, and tests keep it honest.

## Key claims
- A badly designed codebase costs you in three ways: poor feedback loops, hard navigation, and cognitive burnout.
- Folders per module with clear public interfaces give **progressive disclosure** of complexity.
- You keep *"seven or eight chunks"* in your head, not hundreds. You still apply taste at the boundaries.
- In TypeScript, Effect helps enforce module boundaries.

## Pages touched
[[agent-experience]], [[context-and-state]], [[operator-debts]]
