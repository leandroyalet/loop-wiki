---
type: concept
branch: control
tags: [loop-engineering, control, context, context-rot]
sources: ["[[src-pocock-ralph-plugin]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-tips]]", "[[src-huntley-ralph]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-how-i-use-cursor]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-12
updated: 2026-10-27
status: draft
---
# Smart zone and dumb zone (context rot)

*"Early in a session the agent is in a 'smart zone' — sharp, focused, recall is good. As the session grows it drifts into a 'dumb zone': sloppier, forgetful, more mistakes"*. It is the same model, just with more context ([[src-pocock-ai-coding-dictionary]]). Huntley says the same thing in other words: *"The more you use the context window, the worse the outcomes"* ([[src-huntley-ralph]]). Pocock also cites this as **context rot** ([[src-pocock-ralph-tips]]). Up: [[control]].

## Why
Attention relationships grow with the square of the context length (N tokens give about N² pairs). Each token's attention budget is spread thinner, so the signal degrades ([[src-pocock-ralph-plugin]], [[src-pocock-ai-coding-dictionary]]).

## Design consequences for loops
- **Fresh context per iteration.** A bash loop restarts the agent with an empty window each time, while an in-session loop accumulates (20% → 35% → 50%…). *"the plugin guarantees that you're going to fill up the smart zone"* ([[src-pocock-ralph-plugin]]). See [[ralph-loop]] and [[claude-code-loop]].
- **One task per session.** *"The smart zone is a budget, and unrelated work spends it"* ([[src-pocock-ai-coding-dictionary]]). See [[task-sizing]].
- **Plan around the smart zone, not the window.** Quality drops long before the hard limit ([[src-pocock-ai-coding-dictionary]]).
- **Hand off or compact at natural boundaries.** Don't push through, because re-explaining adds more context ([[src-pocock-ai-coding-dictionary]]). See [[context-and-state]].
- **Offload expensive reads to subagents** ([[src-huntley-ralph]]). Tan's version is *Guard the Context Window*: route bulk to subagents, keep summaries in the main thread, size phases, and cap scope and turns ([[src-tan-pstack-loop-principles]]). See [[orchestrator-workers]].
- **Load less instead of offloading.** Anthropic's alternative to subagents is [[progressive-disclosure]]: skills and tools show only short descriptions until needed. Subagents are kept for *measurable* degradation from context bloat ([[src-anthropic-fold-subagents]]).
- **Say "new task"** when switching subjects, so the agent re-routes instead of carrying the last task's context ([[src-tan-pstack-guide-poteto-mode]]).

## Contradictions & open questions
- **Where is the boundary?** About **40%** of the context window ([[src-pocock-ralph-plugin]]), about **125K–150K tokens** on frontier models (*"debated"*, [[src-pocock-ai-coding-dictionary]]), or simply "use as little of ~170k as possible" ([[src-huntley-ralph]]). All agree that a boundary exists.
- **Fresh process or lean session?** Pocock restarts the process every iteration ([[src-pocock-ralph-plugin]]). Tan runs long overnight loops in one Cursor session with `/loop` and keeps the main thread lean through subagents ([[src-tan-pstack-guide-overnight]], [[src-tan-pstack-loop-principles]]). She also reports that compaction quality varies by harness, anecdotally ([[src-tan-how-i-use-cursor]]).
- Do Claude Code's in-session `/loop` and `/goal` reset or compact context between iterations? Not documented in the ingested sources. See [[open-questions]].
- **Offload or keep together?** Huntley and Tan send bulk work to subagents to protect the main window ([[src-huntley-ralph]], [[src-tan-pstack-loop-principles]]). Anthropic says shared context in one window produces better answers and that progressive disclosure removes most of the reason to split ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].

## Related
[[failure-modes]] · [[budgets-and-cost]]
