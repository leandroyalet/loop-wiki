---
type: source
branch: sources
tags: [loop-engineering, pocock, ralph, practice]
sources: []
url: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
author: Matt Pocock
published: 2026-01-08
raw: raw/2026-10-12-pocock-ralph-tips.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "11 Tips For AI Coding With Ralph Wiggum" (2026-01-08)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-ralph-tips.md` · Up: [[sources]]

## Summary
The longest practitioner guide in the wiki on running [[ralph-loop|Ralph]] well. It frames Ralph as the next step after vibe coding, planning, and multi-phase plans, because *"the agent chooses the task, not you."* Most of the tips are classic engineering discipline that *"Ralph makes … non-negotiable."*

## Key claims
1. **Lineage:** vibe coding → planning → multi-phase plans (a new prompt per phase) → Ralph (the same prompt in a loop). See [[loop-vs-prompt-engineering]].
2. **HITL first, then AFK.** *"always cap your iterations. Infinite loops are dangerous with stochastic systems."* Typical caps are 5–10 for small tasks and 30–50 for large ones. Loops take 30–45 min, sometimes hours, and a WhatsApp ping signals the end. See [[afk]] and [[termination]].
3. **Define the scope.** The vaguer the task, the more Ralph *"might loop forever"* or *"declar[e] victory"* early. Example: it skipped "internal" commands and excluded them from coverage. Specify the files, the stop condition and the edge cases. Use **PRD items as JSON with `passes: false`** (from Anthropic's long-running-harness article). Then the PRD is both scope and tracker and can be edited mid-flight. See [[goal-spec]].
4. **Track progress.** Keep a committed `progress.txt` with tasks, decisions, blockers and files. Commit after each feature (log, diff, rollback). Delete the progress file after the sprint. See [[context-and-state]].
5. **Feedback loops:** types, unit tests, Playwright MCP, linting and pre-commit hooks. *"The best setup blocks commits unless everything passes."* See [[backpressure]].
6. **Small steps.** *"The rate at which you can get feedback is your speed limit."* Watch for context rot. There is a trade-off against per-iteration startup cost. See [[task-sizing]].
7. **Prioritise risky tasks:** architecture, integration and unknowns first, polish last. Use HITL for the risky ones. See [[decision-step]] and [[task-sizing]].
8. **Define quality explicitly.** *"The repo wins"*: agents follow the codebase over the prompt. Ralph accelerates software entropy. See [[agent-experience]].
9. **Docker sandboxes** are *"essential insurance"* for AFK and overnight runs. The trade-off is that global `AGENTS.md` and user skills aren't loaded. See [[isolation]].
10. **Pay to play.** HITL Ralph is still worth it. He runs it on the Anthropic 5x Max plan (about £90/month), and local models are *"not good enough"*. See [[budgets-and-cost]].
11. **Make it your own:** other task sources, PR outputs, and coverage, duplication (jscpd), lint and entropy loops. Coverage went from 16% to 100% on the AI Hero CLI. See [[improvement-loops]].

## Pages touched
[[ralph-loop]], [[afk]], [[goal-spec]], [[context-and-state]], [[backpressure]], [[task-sizing]], [[decision-step]], [[agent-experience]], [[isolation]], [[budgets-and-cost]], [[termination]], [[improvement-loops]], [[failure-modes]], [[loop-vs-prompt-engineering]], [[building-a-ralph-loop]]
