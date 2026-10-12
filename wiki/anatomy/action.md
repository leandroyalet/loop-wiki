---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, tools]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tracer-bullets]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Action

**Action** is how an iteration changes the world: tool calls, file edits, PRs, messages. *"A loop that can only see the filesystem is a tiny loop"* ([[src-osmani-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
It comes after the [[decision-step]] and produces the raw material for [[observation]].

## Guidance
- **Connectors widen the reach.** MCP connectors let the loop read the tracker, query a DB, hit staging, post to Slack, and open the PR and link the ticket itself ([[src-osmani-loop-engineering]]). See [[loop-primitives]].
- **Design the agent-computer interface (ACI).** Tool definitions deserve as much prompt engineering as the main prompt. Pick formats the model writes easily. *"Poka-yoke"* the tools: requiring absolute paths eliminated a whole class of errors ([[src-anthropic-building-effective-agents]]).
- **Scope each iteration to one item.** Smaller actions keep context small and failures local ([[src-huntley-ralph]]). Build tracer bullets, thin end-to-end slices, rather than whole layers ([[src-pocock-tracer-bullets]]). See [[task-sizing]].
- **The harness executes.** A tool call is *"just structured text"*. The harness runs it and returns the result. Hooks, permissions and sandboxes live in the harness, not the model ([[src-pocock-ai-coding-dictionary]]).
- **Make the smallest justified change** per iteration, and discard changes that didn't help: *"not left to ride"* ([[src-tan-pstack-guide-overnight]]).
- **Isolate parallel actions** in separate worktrees or cloud agents. See [[isolation]].
- **Gate irreversible actions.** See [[guardrails-and-permissions]].

## Related
[[observation]] · [[agent-loop]]
