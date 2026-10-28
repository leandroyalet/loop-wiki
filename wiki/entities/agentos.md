---
type: entity
branch: entities
tags: [loop-engineering, product, tool-surface, mcp, local-first]
sources: ["[[src-agentos-docs]]"]
created: 2026-10-16
updated: 2026-10-16
status: stub
---
# AgentOS

A local, agent-first *"operating system for human-AI collaboration"* by Joe Contini (`agentos.to`, GitHub org `agentos-to`). It is pre-launch, and the engine source is not public ([[src-agentos-docs]]). Up: [[entities]].

## What it is
- **Engine:** a Rust daemon, one per machine. It owns a personal knowledge graph (the "memex", a single SQLite file at `~/.agentos/data/agentos.db`), runs skills, resolves auth, and speaks **MCP**. Any MCP client (Claude Code, Cursor) can use it as a tool surface.
- **Skills:** Python adapters to outside services (Gmail, GitHub, Linear, Cursor, browsers and others) that declare capabilities with `@provides(...)`. The engine matches each request to a provider. Skills run as fresh per-call subprocesses.
- **Shapes:** a YAML ontology of entity types. Agent activity is part of it: `session`, `tool_call`, `task`, `agent`, `skill`.
- **Apps:** an optional React GUI. The CLI and engine work without it.

All of the above is from [[src-agentos-docs]].

## Where it fits in a loop *(synthesis)*
AgentOS does not drive a loop. It is infrastructure the loop calls into:
- **[[action]]:** one MCP tool surface over many services, designed to need *"one call, not two."*
- **[[context-and-state]]:** the graph as durable, queryable memory shared across sessions and clients. Its design principles list *"agent memory"* among the things that belong on the graph.
- **[[observability]]:** the observer bus streams every tool call, and tool calls, sessions and changes are stored as attributable entities.
- **[[human-in-the-loop]]:** the GUI exists to keep the human *"seeing everything and in control of everything."*

The `problem-solving` agent skill is a loop in its own right: a pain gate, then propose ↔ adversarial review for up to 5 rounds, then implement, then closeout. See [[evaluator-optimizer]].

## Contradictions & open questions
- It has no public engine code and *"zero users"*. Its claims are design intent, and the docs' own "Honest caveats" list gaps between principle and enforcement ([[src-agentos-docs]]).
- Is a single shared memory graph good for loops, or does it bring back the stale-context problems that fresh-context loops avoid? See [[smart-zone]] and [[open-questions]].

## Related
[[agent-experience]] · [[claude-code]] · [[cursor]]
