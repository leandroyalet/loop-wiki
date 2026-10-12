---
type: source
branch: sources
tags: [loop-engineering, primary, agent-loop, foundations]
sources: []
url: https://www.anthropic.com/engineering/building-effective-agents
author: Erik Schluntz, Barry Zhang (Anthropic)
published: 2024-12-19
raw: raw/2026-10-11-anthropic-building-effective-agents.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Anthropic — "Building Effective AI Agents" (2024-12-19)

**Author:** [[anthropic]] (Erik Schluntz, Barry Zhang) · **Raw:** `raw/2026-10-11-anthropic-building-effective-agents.md` · Up: [[sources]]

## Summary
This is the foundational text for the **inner** loop. Agents are *"typically just LLMs using tools based on environmental feedback in a loop."* It separates **workflows** (predefined code paths) from **agents** (where the LLM directs its own process). It catalogues composable patterns and strongly advises building the simplest thing that works. The page now carries a note that its tooling landscape has changed since December 2024.

## Key claims
- **Workflows vs agents:** *"Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents … dynamically direct their own processes and tool usage."* See [[agent-loop]].
- **Start simple.** Add complexity *only* when it demonstrably improves outcomes, and often a single LLM call is enough. See [[loop-vs-prompt-engineering]].
- The building block is the **augmented LLM**: retrieval, tools and memory.
- The workflow patterns are prompt chaining (with gates), routing, parallelization, **orchestrator-workers**, and **evaluator-optimizer**. See [[orchestrator-workers]] and [[evaluator-optimizer]].
- Evaluator-optimizer fits when there are *"clear evaluation criteria"* and iteration gives measurable value. See [[verification]].
- Agents must gain **"ground truth" from the environment at each step** (tool results, code execution). See [[observation]].
- **Stopping conditions** such as a maximum number of iterations *"maintain control."* Agents may pause for human feedback at checkpoints or blockers. See [[termination]] and [[human-in-the-loop]].
- Autonomy means **higher costs and compounding errors**. The advice is to test in sandboxes and add guardrails. See [[budgets-and-cost]], [[guardrails-and-permissions]] and [[failure-modes]].
- Three principles:
  1. simplicity
  2. transparency, by showing planning steps
  3. a carefully crafted **agent-computer interface (ACI)**

  See [[action]] and [[observability]].
- Tool design matters as much as the prompt. For example, requiring absolute file paths removed a whole class of errors. See [[action]].
- Agents fit best where tasks have *"clear success criteria, enable feedback loops, and integrate meaningful human oversight."* See [[goal-spec]].

## Pages touched
[[agent-loop]], [[orchestrator-workers]], [[evaluator-optimizer]], [[observation]], [[action]], [[termination]], [[goal-spec]], [[verification]], [[human-in-the-loop]], [[guardrails-and-permissions]], [[budgets-and-cost]], [[failure-modes]], [[observability]], [[loop-vs-prompt-engineering]], [[anthropic]]
