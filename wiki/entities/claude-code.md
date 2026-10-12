---
type: entity
branch: entities
tags: [loop-engineering, product, claude-code]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-afk-ralph-streaming]]", "[[src-pocock-git-guardrails-hook]]", "[[src-tan-how-i-use-cursor]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Claude Code

[[anthropic]]'s coding agent. Its head, [[boris-cherny]], says he now *"writes loops."* Up: [[entities]].

## Loop surfaces
- [[claude-code-loop]]: `/loop` in three modes, plus `loop.md`
- [[claude-code-goal]]: `/goal`, run until a condition holds, with a separate grader model
- [[claude-code-scheduling]]: cloud Routines, Desktop tasks, session cron, GitHub Actions
- Hooks, worktrees (`--worktree`, `isolation: worktree`), skills, MCP and plugins, subagents and agent teams, `CLAUDE.md` and auto memory ([[src-osmani-loop-engineering]], [[src-tns-loop-engineering]])

- Scriptable for outer loops: `-p`/`--print`, `--output-format stream-json`, `--permission-mode acceptEdits`, and `docker sandbox run claude` ([[src-pocock-getting-started-with-ralph]], [[src-pocock-afk-ralph-streaming]]). See [[building-a-ralph-loop]].
- `PreToolUse` hooks for hard guardrails ([[src-pocock-git-guardrails-hook]])
- The official Ralph plugin, which loops in-session and is criticised in [[src-pocock-ralph-plugin]]

- Tan, a former heavy user, notes that its simplicity drove people to build their own orchestrators on top: *"a new internal orchestrator tool built on top of cc announced every week"*. She reads this as latent demand ([[src-tan-how-i-use-cursor]]).

Full mapping: [[loop-primitives]].
