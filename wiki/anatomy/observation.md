---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, feedback]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Observation

**Observation** is how the loop learns what its action actually did. Agents must *"gain 'ground truth' from the environment at each step (such as tool call results or code execution) to assess its progress"* ([[src-anthropic-building-effective-agents]]). Up: [[anatomy]].

## Where it sits in the loop
It comes after [[action]]. Its output feeds the next [[decision-step]] in the inner loop, and [[verification]] in the outer loop.

## Guidance
- **"Loop back is everything."** Design work so its output can be fed back to the model: add logging, compile and inspect the IR, run the unit's tests ([[src-huntley-ralph]]).
- **Watch the context cost.** Every tool result is *"an allocation"* in the context window. Have subagents summarize large outputs, such as whether a test suite passed ([[src-huntley-ralph]]). See [[context-and-state]].
- **Error output is the observation.** In the self-correction loop, a failing check puts *"a type error with a file and line, a failing assertion with expected and actual values"* into the context, which is enough to fix and re-run with no human involved. **Determinism matters**: *"A flaky check poisons this"*, because the agent "fixes" code that was fine or retries past real failures ([[src-pocock-ai-coding-dictionary]]).
- **Observe the real artifact, not a proxy.** Run the feature and read the actual value, not file mtimes, self-reports or "it compiles". *"When verification fails, suspect the observation method before suspecting the system"* ([[src-tan-pstack-loop-principles]]).
- **Agents need your instruments.** Give them the debugger, profiler, heap snapshots and screen recording you'd use yourself (Tan's `/control-glass` over CDP, [[src-tan-loops-you-can-trust]]). See [[verification-skill]].
- **Push beats poll.** Streaming events through Monitor, or Channels, is often cheaper and more responsive than re-running a prompt to check ([[src-claude-code-scheduled-tasks]]). See [[event-driven-loop]].

## Related
[[backpressure]] · [[observability]]
