---
type: practice
branch: practice
tags: [loop-engineering, practice, sub-agents, multi-agent, evals, migration]
sources: ["[[src-anthropic-fold-subagents]]", "[[src-huntley-ralph]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-pstack-guide-overnight]]", "[[src-osmani-loop-engineering]]"]
created: 2026-10-27
updated: 2026-10-27
status: draft
---
# Folding subagents into one loop

**Folding** means turning a multi-agent system (an orchestrator plus specialist subagents) back into a **single agent loop**. Each subagent's prompt becomes a skill, its API calls become tools, and everything loads through [[progressive-disclosure]]. Anthropic's Applied AI team found that this often improved enterprise agents on quality, and often on cost and latency too ([[src-anthropic-fold-subagents]]). It is the reverse of [[orchestrator-workers]], and the migration is run as a measured, one-change-at-a-time loop of its own. Up: [[practice]].

## Where it sits in the loop
It reshapes the inner [[agent-loop]]. Planning moves into the [[decision-step]] of the same model that acts, procedure and live data move into [[action]] (skills and tools), and results stay in one window ([[context-and-state]]). The migration itself is an [[improvement-loops|improvement loop]] graded by an eval ([[verification]]).

## Keep a subagent only when
These are Anthropic's three conditions ([[src-anthropic-fold-subagents]]):
1. The single loop shows **measurable** degradation from context bloat. See [[smart-zone]].
2. Several tasks need to run **in parallel** with fresh windows that are thrown away afterwards.
3. One agent struggles to **choose tools**, or the system prompt holds **conflicting instructions**.

When you do split, **divide by context, not by problem type**. Good candidates need little from the rest of the system and return a compact result: independent research paths, components with clean interfaces, black-box verification. Splitting by problem type creates a *"telephone game"* ([[src-anthropic-fold-subagents]]). *(synthesis)* Huntley's subagents for expensive reads and Tan's *Guard the Context Window* are divide-by-context splits, so they fall under condition 1 ([[src-huntley-ralph]], [[src-tan-pstack-loop-principles]]).

## The target loop
- One model and one window run an open-ended tool loop. The **harness** owns the limits: turn and cost budgets, write gates.
- Each turn the model emits a **batch** of tool calls. The harness runs them in parallel and returns raw results. The model chooses: another batch, a question for the user, or an answer.
- It stops on the answer or a budget. A goal or verifier check *may* run after the answer. See [[termination]].
- The plan is written **in context** on turn one and revised as results arrive. The planner is the executor.
- Procedure → skills. Hard limits and mid-conversation lookups → tools. Cheap, almost-always-relevant context and mechanical steps → code inside tools. See [[build-the-lever]].

All of this is from [[src-anthropic-fold-subagents]].

## Migration recipe
1. **Build a task-completion eval first.** One end-to-end set owned by a small central team, plus small sets each team ships with its skills. Ten golden examples are enough to start. Grade the final answer against a rubric, track routing accuracy while the orchestrator exists, then track whether the right skill or tool was used. Where replay is hard, timestamp important events so they can be replayed later.
2. **Merge tightly coupled specialists.** Start with the most-used. Pairs that chain on each other's output, share data or are called together (most traffic goes A then B) become one domain agent.
3. **Call the remaining subagents as tools.** The main agent keeps the conversation, and you get a shared response schema, a chance to check conclusions against real data, and a **baseline** without rewriting anything. Hand the conversation over fully only when a subagent must talk to the user directly. This step leaves some costs in place: separate prompts, owners and evals, lossy summaries, and nested loops that add latency.
4. **Fold one subagent at a time.** Its prompts become skills and its API calls become MCP tools. Re-run the eval with and without it.
5. **Read the flips, not the score.** In one test the folded agent got faster but broke a passing flow: it answered with the order-lookup tool alone and never asked the shipping specialist for the delivery date. Cover every agent chain that runs together in production and every rule that must not break, and **run each task more than once**, because that break appeared in only one of two runs.
6. **Keep the subagent only if the folded version scores worse.** Then repeat.

All steps are from [[src-anthropic-fold-subagents]]. Accelerators: `/claude-api build-eval`, `prompt-audit`, `hillclimb` and `cost-optimize`, chained by the `single-agent-loop-kit` migration kit (vendor tooling, not evaluated here).

## Ownership after folding
Teams stop owning *agents* and start owning **skills and tools**, each with a DRI and its own evals. One **small central team** owns the system prompt and end-to-end quality and vets every new skill, tool and eval before it ships. That is the answer to subagent sprawl, the Frankenprompt and over-localized evals ([[src-anthropic-fold-subagents]]). See [[failure-modes]].

## Contradictions & open questions
- **One window or fresh windows?** Folding keeps every step's results in one context because *"shared context produces better answers"* ([[src-anthropic-fold-subagents]]). Loop builders push the other way: a fresh context per iteration and subagents to keep the main thread lean ([[src-huntley-ralph]], [[src-tan-pstack-loop-principles]]). *(synthesis)* The two mostly apply at different levels. Folding is about one task or conversation (the inner loop), while fresh context is about outer-loop iterations. The article's own condition 1 is where they meet. See [[smart-zone]].
- **Planner = executor vs a coordinator that never codes.** pstack's Orchestrate keeps a coordinator that *"never writes code itself"* ([[src-tan-pstack-guide-overnight]]). Anthropic calls the planner doing the work the main improvement. *(synthesis)* Orchestrate fans out parallel coding tasks in fresh windows, which is condition 2.
- **Is verification optional?** The target loop makes a post-answer verifier optional. Loop engineering sources treat a separate checker as the thing that lets you walk away ([[src-osmani-loop-engineering]]). *(synthesis)* The article is mostly about interactive agents with a user in the conversation. See [[evaluator-optimizer]].
- **Vendor evidence.** The quality, cost and latency claims are qualitative or from a single customer (about 2× faster), and the article promotes Anthropic's own tooling.

## Related
[[orchestrator-workers]] · [[progressive-disclosure]] · [[agent-loop]] · [[improvement-loops]] · [[budgets-and-cost]]
