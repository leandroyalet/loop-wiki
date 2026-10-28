---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, tools]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tracer-bullets]]", "[[src-tan-pstack-guide-overnight]]", "[[src-agentos-docs]]", "[[src-omp]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Action

**Action** is how an iteration changes the world: tool calls, file edits, PRs, messages. *"A loop that can only see the filesystem is a tiny loop"* ([[src-osmani-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
It comes after the [[decision-step]] and produces the raw material for [[observation]].

## Guidance
- **Connectors widen the reach.** MCP connectors let the loop read the tracker, query a DB, hit staging, post to Slack, and open the PR and link the ticket itself ([[src-osmani-loop-engineering]]). See [[loop-primitives]].
- **Design the agent-computer interface (ACI).** Tool definitions deserve as much prompt engineering as the main prompt. Pick formats the model writes easily. *"Poka-yoke"* the tools: requiring absolute paths eliminated a whole class of errors ([[src-anthropic-building-effective-agents]]).
- **The edit format is part of the model's skill.** omp's hashline tags each read line with a 2–3 character content hash, so edits point at anchors instead of retyping old text. Across 16 models it beat `apply_patch` by 15 points on average, and took Grok Code Fast 1 from 6.7% to 68.3%. *"Often the model isn't flaky at understanding the task. It's flaky at expressing itself"* ([[src-omp]]).
- **Collapse round-trips.** *"Error Rate = f(Dependency Depth)"*: every extra call is another chance to compound an error, so the tool should return what the agent will need next. [[agentos]] puts this into practice as one MCP surface brokering many services by *capability* rather than by name ([[src-agentos-docs]]). See [[agent-experience]].
- **Scope each iteration to one item.** Smaller actions keep context small and failures local ([[src-huntley-ralph]]). Build tracer bullets, thin end-to-end slices, rather than whole layers ([[src-pocock-tracer-bullets]]). See [[task-sizing]].
- **The harness executes.** A tool call is *"just structured text"*. The harness runs it and returns the result. Hooks, permissions and sandboxes live in the harness, not the model ([[src-pocock-ai-coding-dictionary]]).
- **Make the smallest justified change** per iteration, and discard changes that didn't help: *"not left to ride"* ([[src-tan-pstack-guide-overnight]]).
- **Group tools by user intent, not one per API.** Past roughly **30–50 tool definitions** in the system prompt, tool choice tends to degrade. Load the rest through tool search with deferred loading ([[src-anthropic-fold-subagents]]). See [[progressive-disclosure]].
- **Put preconditions inside the tool.** If Y needs X's output, Y's tool checks for it and returns an instruction the model can act on, instead of a fixed pipeline enforcing the order ([[src-anthropic-fold-subagents]]).
- **Batch and run in parallel.** In Anthropic's single loop the model emits a batch of tool calls per turn and the harness runs them in parallel, returning raw results ([[src-anthropic-fold-subagents]]). See [[agent-loop]].
- **Isolate parallel actions** in separate worktrees or cloud agents. See [[isolation]].
- **Gate irreversible actions.** See [[guardrails-and-permissions]].

## Related
[[observation]] · [[agent-loop]]
