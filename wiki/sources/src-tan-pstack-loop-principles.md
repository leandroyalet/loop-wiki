---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, principles]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/skills
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-loop-principles.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack — six loop principles (SKILL.md files)

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-loop-principles.md` · Up: [[sources]]

## Summary
The full text of six pstack principle skills that matter most for loops. Each is a short rule with a *why*, and most include a test.

## Key claims
- **Make Operations Idempotent:** *"converge to the correct state regardless of how many times they run or where they start from."* The pattern: convergent startup (scan, clean stale artifacts, adopt live sessions), content-based cleanup, self-healing PID-based locks, and idempotent scheduling. Test: what if it runs twice, or the previous run crashed at every possible point? If the answer is *"it depends on what state was left behind,"* add a reconciliation step. See [[idempotency]].
- **Never Block on the Human:** *"The human supervises asynchronously."* Proceed on reversible work and present the result. Irreversible actions (force-push, deleting prod data, sending external messages) *still require confirmation*. See [[human-in-the-loop]].
- **Prove It Works:** check the real artifact, not a proxy, self-report or "it compiles". *"When verification fails, suspect the observation method before suspecting the system."* Script the check so a reviewer can re-run it. See [[verification]].
- **Sequence Work into Verifiable Units:** take small units, each ending in a checkable state, and don't advance until green. Order the delivery so it proves itself, for example failing test first and then the fix. See [[task-sizing]].
- **Encode Lessons in Structure:** when you write an instruction for the second time, make it a lint, flag, check or script. *"The instruction is the symptom."* See [[build-the-lever]].
- **Guard the Context Window:** route bulk to subagents and keep summaries in the main thread. Size phases, cap scope and set turn budgets. The fetched file looks abridged. See [[smart-zone]].

## Pages touched
[[idempotency]], [[human-in-the-loop]], [[verification]], [[task-sizing]], [[build-the-lever]], [[smart-zone]]
