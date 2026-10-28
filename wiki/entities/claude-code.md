---
type: entity
branch: entities
tags: [loop-engineering, product, claude-code]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-afk-ralph-streaming]]", "[[src-pocock-git-guardrails-hook]]", "[[src-tan-how-i-use-cursor]]", "[[src-inside-pstack-report]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
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

- **Porting [[pstack]].** A third-party report maps the pieces as follows ([[src-inside-pstack-report]]):

  | pstack piece | Claude Code equivalent |
  |---|---|
  | SKILL.md files | carry over unchanged |
  | agent files | `.claude/agents/` |
  | Task tool with a model per role | Agent tool with `subagent_type` and `model` |
  | worktrees and cloud agents | `isolation: "worktree"` or `"remote"` |
  | `/loop` | `/loop` |

  It keeps the same `/loop` rule: *"loop on a check that can pass or fail, never on a duration."* The main loss is cross-family review, because model choice is limited to Claude tiers. Ports either shell out to another vendor's CLI or accept reviewers that differ only by context. There is also no exact equivalent to an always-on Custom Mode.

- **How the team reviews its own code** ([[src-osmani-claude-code-code-review]]). Claude writes about 90% of Claude Code. Review runs in layers: pre-PR verification with a fresh-context subagent, an AI reviewer on every PR, a blocking security review, CI, risk-tiered human approval, a merge queue, flags and staged rollout (*latest* before *stable*), and fast rollback. Related product surfaces: **Code Review for Claude Code** (Team and Enterprise; Quick, Standard and Deep levels), local `/code-review` and `/security-review`, the security-review GitHub Action, and `REVIEW.md` files that tell the reviewer what matters per area. See [[layered-code-review]].

- **System prompt cut for newer models.** Anthropic says it reduced Claude Code's system prompt for more advanced models by over 80%, partly by progressively disclosing skills and tools ([[src-anthropic-fold-subagents]]). See [[progressive-disclosure]]. The `/skill-creator` and `/skill-doctor` skills author, audit and prune skill libraries by cost and usage ([[src-anthropic-fold-subagents]]).

Full mapping: [[loop-primitives]].
