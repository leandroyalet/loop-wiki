---
type: entity
branch: entities
tags: [loop-engineering, product, codex]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]"]
created: 2026-10-11
updated: 2026-10-11
status: stub
---
# OpenAI Codex

OpenAI's coding agent app. It has the same [[loop-primitives]] as [[claude-code]] under different names ([[src-osmani-loop-engineering]]). Up: [[entities]].

## Loop surfaces
All second-hand, from [[src-osmani-loop-engineering]] and [[src-tns-loop-engineering]]:
- **Automations tab:** pick the project, prompt, cadence and environment (local checkout or background worktree). Runs that find something go to a **Triage inbox**, and empty runs archive themselves. OpenAI uses them internally for issue triage, CI-failure summaries, commit briefings and bug hunts. See [[scheduled-loop]].
- **`/goal`:** run until a verifiable stop condition holds, with pause, resume and clear. See [[goal-loop]].
- A built-in worktree per thread ([[isolation]]), `SKILL.md` skills invoked with `$name`, MCP connectors and plugins, and subagents defined as TOML in `.codex/agents/`.
- Memory via `AGENTS.md`, the Memories feature, or Linear.

## Contradictions & open questions
- There are no first-party Codex docs in `raw/` yet. See [[open-questions]].
