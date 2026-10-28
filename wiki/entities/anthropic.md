---
type: entity
branch: entities
tags: [loop-engineering, org]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-claude-code-scheduled-tasks]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-ralph-tips]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: stub
---
# Anthropic

AI lab and maker of [[claude-code]]. Up: [[entities]].

- Wrote the foundational inner-loop reference, "Building Effective AI Agents" (2024), covering workflows vs agents, evaluator-optimizer and the ACI ([[src-anthropic-building-effective-agents]]). See [[agent-loop]].
- TNS also cites the harness work for the maker/checker separation ([[src-tns-loop-engineering]]). See [[open-questions]].
- Shipped an **official Ralph plugin** for Claude Code (`/ralph-loop … --completion-promise … --max-iterations`). It loops inside one session via a stop hook, and Pocock criticises that design ([[src-pocock-ralph-plugin]]). See [[ralph-loop]].
- Its article *"Effective harnesses for long-running agents"* is the origin of the `passes`-flag PRD and the progress-file practice ([[src-pocock-ralph-tips]]). It is cited by both TNS and Pocock but not yet ingested.
- **Change volume.** Its monorepo went from about 2,500 merged changes a day in May 2026 to over 30,000 in September, which made line-by-line human review impossible. The Claude Code team's answer is [[layered-code-review]] ([[src-osmani-claude-code-code-review]]).
- Sells **Code Review for Claude Code**, an automated PR reviewer, so its review numbers are vendor-reported ([[src-osmani-claude-code-code-review]]).
- **Applied AI guidance on multi-agent systems** (Diane Sarkis, 2026-10-22): many enterprise agents improve by folding routers, planners and domain subagents into one loop with skills, tools and progressive disclosure. It ships the `single-agent-loop-kit` migration kit and `/claude-api` skills (`build-eval`, `prompt-audit`, `hillclimb`, `cost-optimize`), so treat its comparisons as vendor-reported ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].
- Launched **Routines** (cloud-scheduled Claude Code) in April 2026 ([[src-tns-loop-engineering]]). See [[claude-code-scheduling]].
