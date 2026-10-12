---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, scheduling, triage]
sources: ["[[src-osmani-loop-engineering]]", "[[src-claude-code-scheduled-tasks]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-loops-you-can-trust]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Scheduled loop

A **scheduled loop** fires on a fixed cadence (cron or interval), usually to do *discovery and triage*: it surfaces work so a human doesn't have to go looking ([[src-osmani-loop-engineering]]). The scheduling layer is ordinary cron. What makes it a loop is that *"a loop runs a model that reads the current state and chooses its next action"* ([[src-tns-loop-engineering]]). Up: [[patterns]].

## Canonical example: the morning triage loop
From [[src-osmani-loop-engineering]]:
1. An automation runs every morning and calls a triage **skill**.
2. The skill reads yesterday's CI failures, open issues and recent commits, and writes the findings to a markdown file or a Linear board.
3. For each finding worth doing, it opens an isolated **worktree**, where one sub-agent drafts a fix and another reviews it against the skills and tests.
4. **Connectors** open the PR and update the ticket. Anything unhandled goes to the triage inbox.
5. The state file records what was tried, passed or is open, so *"tomorrow morning the run picks up where today stopped."*

TNS suggests starting with just one triage automation and one verifier sub-agent, which captures most of the value cheaply ([[src-tns-loop-engineering]]).

## Smallest useful version
*"One cron job that runs one kind of session and opens one reviewable PR is a factory."* For example, *"Cron job picks one lint rule a night, opens a PR. I just review it in the morning"* ([[src-pocock-ai-coding-dictionary]]). See [[software-factory]] and [[improvement-loops]].

**Loops that maintain other loops.** Run `/maintain-verification-skill` daily from a scheduled automation, so the verification skill every other loop depends on doesn't rot ([[src-tan-pstack-guide-verify-and-ship]]). See [[verification-skill]]. Tan's StyleX automation migrates **one component per day** ([[src-tan-loops-you-can-trust]]). See [[improvement-loops]].

## Implementations
- [[claude-code-scheduling]]: `/loop 30m …`, cron tools, Desktop tasks, cloud Routines, GitHub Actions
- [[openai-codex]]: the Automations tab (project, prompt, cadence, environment), with a Triage inbox, and empty runs archive themselves ([[src-osmani-loop-engineering]])

## Gotchas
Jitter, no catch-up for missed fires, and the 7-day expiry. See [[trigger]] and [[termination]].

## Related
[[self-paced-loop]] · [[event-driven-loop]] · [[loop-primitives]]
