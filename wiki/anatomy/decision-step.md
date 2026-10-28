---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, planning]
sources: ["[[src-tns-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ralph-tips]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-loop-principles]]", "[[src-openprose]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Decision step

The **decision step** is where the model reads the current state and chooses what to do next. It is what separates a loop from a cron job: *"a cron job runs a fixed script, while a loop runs a model that reads the current state and chooses its next action"* ([[src-tns-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
It comes after [[context-and-state]] is loaded and before [[action]]. In workflows the code makes this choice. In agents the LLM makes it ([[src-anthropic-building-effective-agents]]).

## Examples
- **What to work on.** *"Follow the @fix_plan.md and choose the most important thing."* Huntley says *"LLMs are surprisingly good at reasoning about what is important to implement"* ([[src-huntley-ralph]]). Pocock agrees that *"the agent chooses the task, not you"* is the key improvement over multi-phase plans ([[src-pocock-ralph-tips]]).
- **How to prioritise.** Left alone, Ralph picks *"the first item in the list or whatever seems easiest."* Tell it to go risk-first: architecture → integration points → unknown unknowns → standard features → polish ([[src-pocock-ralph-tips]]). See [[task-sizing]].
- **Which procedure to follow.** `/poteto-mode` routes the goal to one of 23 playbooks and copies its steps into a todo list. Skipped steps stay visible as `skip: <reason>` ([[src-tan-pstack-guide-poteto-mode]]).
- **Keep or discard.** After verifying, *commit* a change that made progress and *discard* one that didn't. *"A plateau means pivot, not stop"* ([[src-tan-pstack-guide-overnight]]).
- **Ask or proceed.** *"Never block on the human"*: proceed on reversible work and present the result, but confirm irreversible actions ([[src-tan-pstack-loop-principles]]). See [[human-in-the-loop]].
- **When to run next.** A self-paced `/loop` picks its own delay after each iteration and prints the delay and the reason: short while a build is finishing, long when idle ([[src-claude-code-scheduled-tasks]]). See [[self-paced-loop]].
- **Whether to escalate.** Findings the loop can't handle go to a triage inbox for a human. See [[human-in-the-loop]].
- **Whether to stop.** See [[termination]].
- **How to revise the plan.** In Anthropic's single loop the model writes its plan in context on turn one and revises it as tool results arrive. Because the planner is the executor, *"it can change the plan mid-turn"*. A code step that rewrites the plan from a rule catalog is no longer needed ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].

## Contradictions & open questions
- Huntley trusts the model's sense of what is "most important" ([[src-huntley-ralph]]). Pocock finds the model drifts to easy wins unless told otherwise ([[src-pocock-ralph-tips]]).
- How much decision power should the loop have? Anthropic says to prefer workflows (code decides) unless flexibility is needed ([[src-anthropic-building-effective-agents]]). Ralph gives the model full say over priorities ([[src-huntley-ralph]]).
- **Take the model out of the outer decision?** OpenProse makes the wake/commit decision deterministic: *"The harness never asks an LLM 'did this change.'"* The model decides once, at compile time, what counts as a material change, and it decides again inside each bounded render ([[src-openprose]]). *(synthesis)* For the outer loop this reverses TNS's defining contrast with cron, while keeping it for the inner loop. See [[reconciler-loop]].
- **Move decisions into the model, or out of it?** Anthropic: *"Each new model lets you move more of the decision-making out of the harness and into the model itself,"* and rigid multi-agent structures often stopped a new model doing more of the work ([[src-anthropic-fold-subagents]]). OpenProse moves the outer wake/commit decision the other way, into deterministic code ([[src-openprose]]). *(synthesis)* Anthropic still puts hard limits in the harness and tools, so both agree that judgment goes to the model and invariants go to code. See [[build-the-lever]].

## Related
[[agent-loop]] · [[goal-spec]]
