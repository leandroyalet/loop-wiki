---
type: source
branch: sources
tags: [loop-engineering, primary, ralph]
sources: []
url: https://ghuntley.com/ralph/
author: Geoffrey Huntley
published: 2025-07-14
raw: raw/2026-10-11-huntley-ralph.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Huntley — "Ralph Wiggum as a 'software engineer'" (2025-07-14)

**Author:** [[geoffrey-huntley]] · **Raw:** `raw/2026-10-11-huntley-ralph.md` (diagrams not captured) · Up: [[sources]]

## Summary
This is the origin write-up of the **Ralph** technique, which predates the "loop engineering" name by almost a year. *"In its purest form, Ralph is a Bash loop: `while :; do cat PROMPT.md | claude-code ; done`."* Huntley used it to build CURSED, a new esoteric programming language. It is the most hands-on source in the wiki about tuning a loop by observation. See [[ralph-loop]].

## Key claims
- *"Deterministically bad in an undeterministic world."* Failures are identifiable and fixable through prompts. The operator **tunes Ralph like a guitar** by adding "signs." See [[writing-a-loop-prompt]].
- **Monolithic, not multi-agent:** a single process in a single repo doing one task per loop. Agent-to-agent multiplexing is "a red hot mess." See [[orchestrator-workers]].
- **One item per loop.** With about 170k tokens of context, *"The more you use the context window, the worse the outcomes."* See [[context-and-state]].
- **Deterministically allocate the stack the same way every loop:** load the plan (`fix_plan.md`) and the specs every time. See [[context-and-state]] and [[goal-spec]].
- The **main context acts as a scheduler.** Expensive work goes to subagents. Parallelism is fanned out for search and writes but limited to **one subagent for build and test**, to avoid "bad form back pressure." See [[orchestrator-workers]].
- **"Don't assume it's not implemented."** Non-deterministic code search is *"the Achilles' heel of Ralph."* See [[failure-modes]].
- **Backpressure:** tests, type systems, static analysers and security scanners reject bad generations. *"the wheel has got to turn fast."* See [[backpressure]].
- **Leave notes for future loops:** document *why* each test exists, because future iterations lack the reasoning. See [[context-and-state]].
- **No cheating:** models drift toward placeholder implementations because *"the reward function is compiling code."* The fix is to run more Ralphs that hunt for placeholders. See [[failure-modes]].
- **Loop back is everything:** design so output feeds back for evaluation (logging, inspecting IR). See [[observation]].
- **Self-improvement:** Ralph updates `AGENT.md` with how to build and run the project. See [[context-and-state]].
- **You will wake up to a broken codebase.** Then it is a judgment call: `git reset --hard` and restart, or write rescue prompts. See [[human-in-the-loop]].
- *"There's no way in heck would I use Ralph in an existing code base."* It is best for greenfield work and gets about 90% done. See [[ralph-loop]].
- *"Engineers are still needed … Anyone claiming [otherwise] is peddling horseshit."* The same post also says Ralph can *"displace a large majority of SWEs … for Greenfield projects."* See [[operator-debts]].

## Pages touched
[[ralph-loop]], [[context-and-state]], [[goal-spec]], [[backpressure]], [[verification]], [[observation]], [[failure-modes]], [[orchestrator-workers]], [[writing-a-loop-prompt]], [[human-in-the-loop]], [[operator-debts]], [[geoffrey-huntley]]
