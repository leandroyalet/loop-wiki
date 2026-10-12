---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, sub-agents, multi-agent]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-osmani-loop-engineering]]", "[[src-pocock-seven-phases]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-recipes]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Orchestrator–workers

In **orchestrator-workers**, *"a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results"*. Unlike fixed parallelisation, the subtasks are decided at runtime ([[src-anthropic-building-effective-agents]]). Up: [[patterns]].

## In loops
- **Context offloading (Ralph).** The primary context *"should operate as a scheduler"* that spawns subagents for expensive work, so their output doesn't bloat the main window ([[src-huntley-ralph]]).
- **Controlled fan-out (Ralph).** Use up to hundreds of subagents for search and writing, but **only one for build and test**, because fanning validation out creates *"bad form back pressure"* ([[src-huntley-ralph]]). See [[backpressure]].
- **Role split (Osmani).** The usual split is *"one agent explores, one implements, one verifies against the spec."* In Codex, agents are defined as TOML in `.codex/agents/`, each with its own model and effort. In Claude Code they live in `.claude/agents/` and agent teams ([[src-osmani-loop-engineering]]).
- **Kanban parallelism (Pocock).** Break the PRD into tickets with blocking relationships, then *"Find all non-blocking tickets and spin up an agent for each one"*. Often a single sequential agent is enough ([[src-pocock-seven-phases]]). See [[seven-phases-of-ai-development]].
- **Coordinator that never codes (Tan).** pstack's *Orchestrate* playbook has a standing coordinator that authors briefs, collects results, keeps the lowest unmerged PR green, and *"never writes code itself"*. It is *"deliberately heavy machinery"* and routes single-session work back to the [[overnight-contract]] ([[src-tan-pstack-guide-overnight]]). Bots spawn cloud agents so their own context *"stays clean"* ([[src-tan-complete-guide-pstack-pt1]]).
- **Owner per PR (Tan).** *Autopilot-full* and *Autopilot-stack* give each PR one owner agent from build to merge-ready ([[src-tan-pstack-guide-overnight]]).
- **Swarm.** `/swarm` partitions slices across workers and returns one `PASS` / `ISSUES` / `BLOCKED` report instead of raw dumps ([[src-tan-pstack-guide-recipes]]).
- **Isolation.** Each worker gets its own worktree or cloud agent. See [[isolation]].

## Contradictions & open questions
- Huntley dismisses peer **agent-to-agent** communication as *"a red hot mess"* (non-deterministic microservices) but relies heavily on hierarchical subagents ([[src-huntley-ralph]]). Osmani mentions agent teams that *"pass work between them"* without flagging that risk ([[src-osmani-loop-engineering]]).

## Related
[[evaluator-optimizer]] · [[loop-primitives]] · [[budgets-and-cost]]
