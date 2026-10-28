---
type: hub
branch: practice
tags: [loop-engineering, hub, practice]
sources: []
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Practice: building loops with today's tools

Concrete tools and how-tos. Osmani argues that the shapes are now the same across vendors, so you should *"design a loop that still works no matter which one you happen to be sitting in"* ([[src-osmani-loop-engineering]]). Up: [[loop-engineering]].

**Cross-tool**
- [[loop-primitives]]: the five building blocks plus memory, mapped to Claude Code and Codex.
- [[writing-a-loop-prompt]]: how to write the prompt a loop re-runs.
- [[task-sizing]]: one thing per iteration, tracer bullets, vertical TDD, risk first.
- [[folding-subagents]]: when to collapse an orchestrator and specialists into one loop with skills and tools, and how to migrate one subagent at a time against an eval.

**Ralph and workflow (Pocock)**
- [[building-a-ralph-loop]]: HITL `ralph-once.sh` → capped AFK `afk-ralph.sh`, sandbox, streaming, guardrails.
- [[seven-phases-of-ai-development]]: idea → research → prototype → PRD → kanban → execution → QA.
- [[backlog-triage]]: turning inbound issues into `ready-for-agent` briefs.

**Verification and trust (Tan / pstack)**
- [[verification-skill]]: app control CLI + Feature Map, created once and maintained daily.
- [[overnight-contract]]: goal, finish predicate, isolation, permissions, decision log, escape hatch.
- [[build-the-lever]]: scripts for deterministic steps, and lessons encoded in structure, not prose.

**Claude Code**
- [[claude-code-loop]]: `/loop` modes, `loop.md`, stopping.
- [[claude-code-goal]]: `/goal` run-until-condition.
- [[claude-code-scheduling]]: choosing between `/loop`, Desktop tasks, cloud Routines and GitHub Actions.
- [[layered-code-review]]: how the Claude Code team reviews agent-written code: six layers over fast rollback, risk-tiered approval, a reviewer that must converge.

**omp**
- [[omp-loop-surfaces]]: `/goal` (self-audited, token budget), `/loop --until '<cmd>'`, `/ratchet` hill-climb, the advisor, stream rules, `orchestrate`/`vibe`.

**Codex:** see [[openai-codex]], which is covered only second-hand so far.

**Adjacent**
- [[llm-wiki-pattern]]: how this wiki works, as a loop over a knowledge base.
