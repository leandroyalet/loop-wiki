---
type: concept
branch: control
tags: [loop-engineering, control, context, skills, tools]
sources: ["[[src-anthropic-fold-subagents]]", "[[src-omp]]", "[[src-pocock-codebases-agents-love]]", "[[src-agentos-docs]]", "[[src-huntley-ralph]]", "[[src-tan-pstack-loop-principles]]"]
created: 2026-10-27
updated: 2026-10-27
status: draft
---
# Progressive disclosure

**Progressive disclosure** keeps the agent's window small by showing it only *short descriptions* of skills, tools and reference material, and loading the full content when the agent decides it needs it. Anthropic presents it as the main alternative to splitting work across subagents: it *"removes the main reason teams previously split work across subagents"* ([[src-anthropic-fold-subagents]]). Up: [[control]].

## Where it sits in the loop
It governs what enters [[context-and-state|context]] at each [[decision-step]], and which [[action|tools]] are visible. It is a control on context rot ([[smart-zone]]) that works inside one session, not across iterations.

## Mechanisms
- **Skills** carry procedure: the steps, rules and judgment calls of a domain. Only the description sits in context until the skill is loaded ([[src-anthropic-fold-subagents]]).
- **Tool search with deferred loading.** Tool definitions are loaded on demand. Group tools **by user intent rather than one per API**, because past **30–50 tool definitions** in the system prompt, tool choice tends to degrade ([[src-anthropic-fold-subagents]]). *(synthesis)* [[agentos]] reaches the same place from the other side: one MCP surface brokering many services by capability ([[src-agentos-docs]]).
- **Knowledge bases** hold reference material needed only sometimes (policies, metric definitions, specs), behind a lookup tool or as reference files inside a skill. Code should not fetch it and paste it into the prompt ([[src-anthropic-fold-subagents]]).
- **Rules on trigger.** omp's time-traveling stream rules stay out of context until the model goes off-script, so there is no *"context tax on every turn"* ([[src-omp]]).
- **In the codebase.** Deep modules with a clear public interface give *"progressive disclosure"* to an agent exploring the repo ([[src-pocock-codebases-agents-love]]). See [[agent-experience]].

## Evidence and limits
- Anthropic says it cut Claude Code's system prompt for advanced models by **over 80%**, partly by progressively disclosing skills and tools ([[src-anthropic-fold-subagents]]). The underlying post has not been ingested.
- It needs discipline: skill and tool descriptions have to *trigger at the right times*, and the system prompt needs an owner ([[src-anthropic-fold-subagents]]).
- Skills sprawl like agents do. Per-team DRIs, plus tooling that shows each skill's cost and usage (`/skill-doctor`), keep the library pruned ([[src-anthropic-fold-subagents]]).

## Contradictions & open questions
- **Disclosure or offloading?** Huntley and Tan protect the main window by sending bulk reads to subagents ([[src-huntley-ralph]], [[src-tan-pstack-loop-principles]]). Anthropic protects it by loading less in the first place, and keeps subagents for *measured* bloat ([[src-anthropic-fold-subagents]]). The two can be combined; no source compares them.
- Pocock's dictionary has a **progressive disclosure** entry that is not yet ingested. See [[open-questions]].

## Related
[[folding-subagents]] · [[smart-zone]] · [[context-and-state]] · [[agent-experience]]
