---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, sub-agents, multi-agent]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-osmani-loop-engineering]]", "[[src-pocock-seven-phases]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-recipes]]", "[[src-inside-pstack-report]]", "[[src-omp]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
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
- **Fresh workers by default (pstack 0.15.24).** A fix round, retry or next queue item goes to a *new* agent with a consolidated brief. Resume an old agent only when it holds state that is costly to move, such as a checkout or a running dev server, because *"Interrupt-chained resumes silently drop directives"* ([[src-inside-pstack-report]]). See [[smart-zone]].
- **Rolling window, not batches.** Orchestrate pilots one unit end to end first, to falsify the brief template. It then keeps about 10 workers in flight, drains completions at fixed points, and *"never review[s] inline"*. It stops spawning at ~70% of the budget ([[src-inside-pstack-report]]).
- **The brief is the product.** *"A vague brief fails quietly, because a worker cannot ask you a question"* ([[src-inside-pstack-report]]). See [[goal-spec]].
- **The orchestrator owns the output.** *"Review the diff and write your own summary instead of passing theirs along"* ([[src-inside-pstack-report]]).
- **Delegates inherit the rules.** A thin `poteto-agent` definition makes every subagent load the router first. *"Substituting generalPurpose skips that read and drifts"* ([[src-inside-pstack-report]]).

## The orchestrate contract (omp)
[[omp]]'s `orchestrate` keyword injects a coordinator contract ([[src-omp]]):
- *"NEVER yield before closure. Phase completion is not a yield point."*
- Expand every referenced list into flat todos, because *"'Most'/'important' items is failure."*
- Dispatch independent work as parallel, self-contained subagents (≤3–5 explicit paths each), and never a lone one.
- *"Subagents NEVER verify, lint, or format."* The orchestrator runs the gates once per phase over the union of changed files and dispatches fix-ups on red. This matches Huntley's single validator.
- Never relabel unfinished work as *"follow-up", "v1", or "MVP"*.

`/vibe` takes this further: a director limited to `read` steers persistent `fast` and `good` workers, and *"worker completion means the turn settled, not that its claims are correct"* ([[src-omp]]).

## When to fold workers back in (Anthropic)
Anthropic's Applied AI team reports that many enterprise multi-agent systems did better once routers, planners and domain subagents were folded into **one loop with skills and tools** ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].
- **Keep a subagent only for** measured context bloat, parallel work in fresh throwaway windows, or tool-choice and instruction conflicts ([[src-anthropic-fold-subagents]]).
- **Divide by context, not by problem type.** Good workers need little from the rest of the system and return a compact result (research paths, clean-interface components, black-box verification). Splitting by problem type is a *"telephone game"* where each handoff loses fidelity ([[src-anthropic-fold-subagents]]).
- **Conway's law.** One subagent per team turns the architecture into *"a copy of their org chart"*, with sprawl, a Frankenprompt and evals nobody owns end to end ([[src-anthropic-fold-subagents]]). See [[failure-modes]].
- **Workers as tools.** If you keep a worker, the main agent should call it as a tool and keep the conversation. Full handoff is only for a worker that must talk to the user directly ([[src-anthropic-fold-subagents]]).

## Contradictions & open questions
- Huntley dismisses peer **agent-to-agent** communication as *"a red hot mess"* (non-deterministic microservices) but relies heavily on hierarchical subagents ([[src-huntley-ralph]]). Osmani mentions agent teams that *"pass work between them"* without flagging that risk ([[src-osmani-loop-engineering]]).
- **Planner as executor or a coordinator that never codes?** Anthropic's single loop has *"the model that writes the plan … also … carrying it out"* ([[src-anthropic-fold-subagents]]). pstack's coordinator *"never writes code itself"* ([[src-tan-pstack-guide-overnight]]). *(synthesis)* Orchestrate's parallel coding in fresh windows is exactly Anthropic's second keep-condition, so the two may not conflict.
- **Role split vs divide by context.** Osmani's explore / implement / verify split ([[src-osmani-loop-engineering]]) is partly a split by problem type, which Anthropic warns against, though its *verify* role matches Anthropic's black-box verification exception ([[src-anthropic-fold-subagents]]).

## Related
[[evaluator-optimizer]] · [[loop-primitives]] · [[budgets-and-cost]]
