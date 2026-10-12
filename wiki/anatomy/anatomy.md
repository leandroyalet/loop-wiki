---
type: hub
branch: anatomy
tags: [loop-engineering, hub, anatomy]
sources: []
created: 2026-10-11
updated: 2026-10-11
status: draft
---
# Anatomy of a loop

The parts of one loop iteration, in execution order. Every [[patterns|pattern]] is a particular choice for each slot. Up: [[loop-engineering]].

| # | Part | Question | Typical implementations |
|---|---|---|---|
| 1 | [[trigger]] | When does an iteration start? | cron, interval, self-paced wakeup, event, human |
| 2 | [[goal-spec]] | What does "done" mean? | specs, `/goal` condition, acceptance tests |
| 3 | [[context-and-state]] | What does the iteration know? | plan file, `AGENTS.md`, Linear board, skills |
| 4 | [[decision-step]] | What should happen next? | the model picks the "most important thing" |
| 5 | [[action]] | How does it change the world? | tools, connectors (MCP), sub-agents |
| 6 | [[observation]] | What happened? | tool results, logs, CI output |
| 7 | [[verification]] | Is it actually right? | tests, type checks, a separate checker agent |
| 8 | [[termination]] | Stop, or go round again? | goal met, iteration cap, expiry, human |

Parts 4–6 make up the inner [[agent-loop]]. Parts 1–3, 7 and 8 are what loop engineering adds around it *(synthesis)*.
