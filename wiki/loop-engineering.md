---
type: hub
branch: root
tags: [loop-engineering, hub, root]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-ralph-tips]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Loop Engineering

**Loop engineering** is the practice of *"replacing yourself as the person who prompts the agent"*. Instead of prompting, you design the system that does the prompting ([[src-osmani-loop-engineering]]). A loop **finds the work, hands it out, checks it, writes down what is done, and decides the next thing**, and it keeps going until a goal is met or a stop condition fires. The term was coined in June 2026 by [[addy-osmani]], after [[boris-cherny]] said *"My job is to write loops"* and [[peter-steinberger]] urged developers to *"design loops that prompt your agents"* ([[src-tns-loop-engineering]]).

> The one-line distinction: *"a cron job runs a fixed script, while a loop runs a model that reads the current state and chooses its next action."* ([[src-tns-loop-engineering]])

> **Synonym:** [[matt-pocock]] calls the same idea a **[[software-factory]]**: *"agent sessions are started by triggers … rather than by a human"* ([[src-pocock-ai-coding-dictionary]]).

## Mental model: two nested loops *(synthesis)*

```
 OUTER LOOP: what you engineer
 ┌─────────────────────────────────────────────────────────────────────────┐
 │ trigger ──► load state ──► decide ──► INNER LOOP ──► verify ──► write   │
 │    ▲          (memory)      (what     (agent: act ⇄    (separate  state │
 │    │                         next?)    observe)         checker)    │   │
 │    └──────────── wait / reschedule ◄── done? ──► stop ◄─────────────┘   │
 └─────────────────────────────────────────────────────────────────────────┘
```

- **Inner loop:** the [[agent-loop]]. An LLM uses tools based on environmental feedback, turn after turn ([[src-anthropic-building-effective-agents]]). The model vendors mostly provide this.
- **Outer loop:** what loop engineering designs. It decides *when* the agent runs ([[trigger]]), *what it remembers* ([[context-and-state]]), *what counts as done* ([[goal-spec]] and [[verification]]), and *when to stop* ([[termination]]).

## Branches

| Branch | Question it answers | Hub |
|---|---|---|
| Anatomy | What are the parts of one loop? | [[anatomy]] |
| Patterns | What kinds of loops are there? | [[patterns]] |
| Control | How do I keep a loop bounded, safe and correct? | [[control]] |
| Practice | How do I build one in real tools today? | [[practice]] |
| Entities | Who and what shapes the field? | [[entities]] |
| Sources | What has been read? | [[sources]] |
| Syntheses | Comparisons, checklists, open questions | [[syntheses]] |

## Core claims so far
1. **The building blocks now ship in the products.** You no longer maintain a pile of bash. Automations, worktrees, skills, connectors, sub-agents and memory exist in both [[claude-code]] and [[openai-codex]] ([[src-osmani-loop-engineering]]). See [[loop-primitives]].
2. **Memory lives on disk, not in context:** *"The agent forgets, the repo doesnt."* ([[src-osmani-loop-engineering]]). Ralph reloads the same plan and specs every iteration ([[src-huntley-ralph]]). See [[context-and-state]].
3. **Verification is the limiting step.** Loops are only as fast as their slowest stage, and that stage is verification, which usually waits on a human. Teach agents to verify first, then loop ([[src-tan-loops-you-can-trust]]). See [[verification-skill]] and [[earned-autonomy]].
4. **Separate the maker from the checker.** *"A verifier you actually trust is the only reason you can walk away."* ([[src-osmani-loop-engineering]], [[src-tns-loop-engineering]]). See [[verification]] and [[backpressure]].
5. **Bound every loop.** Use iteration caps ([[src-anthropic-building-effective-agents]]), goal conditions, and expiry: Claude Code recurring tasks die after 7 days so *"a forgotten loop"* can't run forever ([[src-claude-code-scheduled-tasks]]). See [[termination]] and [[budgets-and-cost]].
6. **Fresh context per iteration.** Each iteration should start in the model's [[smart-zone]]. Restart the process instead of accumulating one long session ([[src-pocock-ralph-plugin]], [[src-huntley-ralph]]). Size tasks accordingly. See [[task-sizing]].
7. **Earn autonomy.** Start [[human-in-the-loop]], go [[afk]] once the loop is trusted, and always cap iterations or give a pass/fail finish condition ([[src-pocock-ralph-tips]], [[src-tan-pstack-guide-overnight]]). End runs in a reviewable PR, not a merge ([[src-pocock-ai-coding-dictionary]]). Let any stage stop the line ([[src-tan-loops-you-can-trust]]). See [[earned-autonomy]].
8. **Loops raise the stakes on human judgment.** Comprehension debt and cognitive surrender grow faster with a smooth loop ([[src-osmani-loop-engineering]]). See [[operator-debts]].

## Lineage (one line, by design)
Prompt engineering → context engineering → harness engineering → loop engineering, *"in fewer than 18 months"* ([[src-tns-loop-engineering]]). The practitioner version is vibe coding → planning → multi-phase plans → Ralph ([[src-pocock-ralph-tips]]). Ralph ([[src-huntley-ralph]], 2025) is the pre-name ancestor. See [[loop-vs-prompt-engineering]].

## Known gaps
- **Idempotency** now has a principle-level source ([[src-tan-pstack-loop-principles]]) but no worked failure case. See [[idempotency]].
- **Observability** has some practitioner tactics now, such as streaming and notifications, but no systematic source. See [[observability]].
- **In-session vs fresh-context loops.** It is unresolved whether Claude Code's `/loop` and `/goal`, or Cursor's `/loop`, suffer the context build-up Pocock describes. Tan's overnight loops run in-session and lean on subagents. See [[smart-zone]].
- **Human merge gate.** Tan's Autopilot-full merges on verifier verdicts alone. Pocock and Osmani keep humans on PRs. See [[software-factory]].
- **Codex** is described only second-hand. See [[openai-codex]].
- Full list: [[open-questions]].

## Navigation
[[index]] · [[log]] · [[loop-design-checklist]]
