---
type: concept
branch: control
tags: [loop-engineering, control, safety, permissions]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-git-guardrails-hook]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-benny-automation]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Guardrails and permissions

**Guardrails** limit what a loop may do without a human. Because autonomous agents carry *"the potential for compounding errors"*, Anthropic recommends *"extensive testing in sandboxed environments, along with the appropriate guardrails"* ([[src-anthropic-building-effective-agents]]). Up: [[control]].

## Examples from Claude Code
All from [[src-claude-code-scheduled-tasks]]:
- **Scope fence.** The built-in maintenance prompt *"does not start new initiatives outside that scope"*.
- **Authorization carry-over.** Irreversible actions such as pushing or deleting *"only proceed when they continue something the transcript already authorized."*
- **Permission inheritance.** `/loop` inherits the session's permissions, Desktop tasks are configurable per task, and cloud Routines run autonomously with no prompts. Choose the surface with that in mind. See [[claude-code-scheduling]].
- **Invocation limits.** A scheduled fire only runs skills Claude may invoke on its own. Built-in commands and skills with `disable-model-invocation` arrive as plain text.
- **Kill switch.** `CLAUDE_CODE_DISABLE_CRON=1`.

## Where vs what
A sandbox limits **where** commands run. It does not limit **what** they do. *"your git history lives inside that sandboxed folder"*, so `git reset --hard` or `git push --force` can still wipe out weeks of work ([[src-pocock-git-guardrails-hook]]). You need both layers. See [[isolation]].

## Hard guardrails via hooks
A `PreToolUse` hook reads each Bash command, matches it against dangerous patterns (`git push`, `reset --hard`, `clean -f`, `branch -D`, `checkout .`, `restore .`), and exits 2 with `BLOCKED: … The user has prevented you from doing this.` *"It's a hard guardrail, not a suggestion buried in prose."* These are *"safe by default"* rules that you can loosen per workflow ([[src-pocock-git-guardrails-hook]]).

## Permission modes for loops
- `--permission-mode acceptEdits` auto-accepts edits *"so the loop doesn't stall"* ([[src-pocock-getting-started-with-ralph]]).
- AFK *"Usually requires a permissive permission mode plus sandboxing to be safe"* ([[src-pocock-ai-coding-dictionary]]). See [[afk]].
- End AFK runs in *"a PR, not changes already merged"* ([[src-pocock-ai-coding-dictionary]]).

## Reversible vs irreversible
*"Irreversible actions (force-push, delete production data, send external messages) still require confirmation. Reversible actions (write code, edit notes, split tasks) should proceed without blocking"* ([[src-tan-pstack-loop-principles]]).

## Automation guardrails (benny)
From [[src-tan-benny-automation]]:
- draft PRs only, *"do not merge or deploy"*
- **fail closed** when channel coordinates, tracker access, the control adapter or the feature map are missing or uncertain
- subagents *"cannot post to slack or receive slack credentials"*
- never post a root channel message
- secrets kept out of the copied pack
- no automation created until the human explicitly asks

## Contradictions & open questions
- Still wanted: sources on network egress and credential scoping for unattended loops. See [[open-questions]].

## Related
[[isolation]] · [[action]] · [[human-in-the-loop]]
