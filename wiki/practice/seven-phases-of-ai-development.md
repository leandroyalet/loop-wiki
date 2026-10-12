---
type: practice
branch: practice
tags: [loop-engineering, practice, workflow]
sources: ["[[src-pocock-seven-phases]]", "[[src-pocock-triage-skill]]", "[[src-pocock-ai-coding-dictionary]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Seven phases of AI development

[[matt-pocock]]'s workflow *around* an execution loop. The loop itself is phase 6. The other phases make AFK execution possible and check what it produced ([[src-pocock-seven-phases]]). Up: [[practice]].

| # | Phase | Deliverable | Loop-anatomy role *(synthesis)* |
|---|---|---|---|
| 1 | Idea, refined with `/grill-me` | problem statement | resolve ambiguity *before* AFK. See [[afk]]. |
| 2 | Research (optional) | `RESEARCH.md` | cached [[context-and-state]] for fresh windows, deleted after the sprint |
| 3 | Prototype (optional) | throwaway variations, winner committed | concrete patterns the agent can copy. See [[agent-experience]]. |
| 4 | PRD | end state, *"not the journey"* | [[goal-spec]] |
| 5 | Kanban board | tickets with blocking relationships | work queue. Non-blocking tickets can run in parallel. See [[orchestrator-workers]]. |
| 6 | **Execution** | code, via Ralph loops, possibly AFK | the loop: [[ralph-loop]] |
| 7 | QA | an agent-written QA plan, human testing, code review | human [[verification]]. It produces new tickets, so the cycle returns to 5. |

## The outer cycle
Phases 5 → 6 → 7 → 5 repeat *"multiple times until you reach a polished product"* ([[src-pocock-seven-phases]]). In wiki terms, QA is a [[human-in-the-loop]] outer loop wrapped around an AFK inner execution loop *(synthesis)*.

## Variants
- Inbound work from others enters through [[backlog-triage]] instead of phases 1–4. Both lanes meet at `ready-for-agent` ([[src-pocock-triage-skill]]).
- With triggers starting the execution sessions, this becomes a [[software-factory]] ([[src-pocock-ai-coding-dictionary]]).

## Related
[[loop-design-checklist]] · [[building-a-ralph-loop]]
