---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, inner-loop, foundations]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Agent loop (inner loop)

The **agent loop** is the basic unit everything else wraps. Agents are *"typically just LLMs using tools based on environmental feedback in a loop"* ([[src-anthropic-building-effective-agents]]). Huntley describes the same thing: agentic loops work *"by executing a tool and then evaluating the result of that tool"* ([[src-huntley-ralph]]). Up: [[patterns]].

## Where it sits in the loop
It covers [[decision-step]] → [[action]] → [[observation]], repeated within one session or turn. Loop engineering wraps this in an outer loop. See [[loop-engineering|the two-loop model]].

## Who runs it
*"The agent loop — model proposes, harness executes, repeat — is run by the harness."* The model only turns text into text. The harness assembles context, executes tool calls, feeds results back, stores the session, asks permission, and decides when to compact ([[src-pocock-ai-coding-dictionary]]). When behaviour changes, *"the model is often not the variable — the harness is."*

## Workflows vs agents
- **Workflows:** *"LLMs and tools are orchestrated through predefined code paths."* They are predictable and suit well-defined tasks.
- **Agents:** *"LLMs dynamically direct their own processes and tool usage."* They suit open-ended problems where *"you can't hardcode a fixed path"*.

Anthropic's advice is to start with the simplest option. Often that is a single call, then a workflow, and only then an agent ([[src-anthropic-building-effective-agents]]).

## The single-loop design (Anthropic, 2026)
Anthropic's current reference shape for an enterprise agent ([[src-anthropic-fold-subagents]]):
- One model, one context window, an open-ended tool loop. The harness sets turn and cost budgets and write gates.
- Each turn the model emits a **batch** of tool calls. The harness runs them in parallel and returns raw results, and the model picks another batch, a question for the user, or an answer.
- It stops on the answer or a budget. A goal or verifier check can optionally follow.
- The plan lives **in context**, written on turn one and revised as results arrive.
- Skills hold procedure and tools hold live data and hard limits, both loaded through [[progressive-disclosure]].

Over-built alternatives (intent classifier, fixed reasoning pipeline, segment buckets, branches, orchestrator) often do *"work the model no longer needed done for it"*. One clear system prompt, 4–5 thin data tools and firm output guardrails cover most cases ([[src-anthropic-fold-subagents]]). *(synthesis)* This updates Anthropic's own 2024 advice to start simple: the bar for "simple" has moved as models improved. See [[folding-subagents]].

## Risks
Higher cost and *"the potential for compounding errors"*. The advice is to test in sandboxes and add guardrails ([[src-anthropic-building-effective-agents]]). See [[failure-modes]] and [[guardrails-and-permissions]].

## Related
[[orchestrator-workers]] · [[evaluator-optimizer]] · [[action]] · [[folding-subagents]]
