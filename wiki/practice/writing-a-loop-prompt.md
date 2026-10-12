---
type: practice
branch: practice
tags: [loop-engineering, practice, prompting]
sources: ["[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-tracer-bullets]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-tan-pstack-guide-principles]]", "[[src-tan-pstack-guide-recipes]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Writing a loop prompt

A loop prompt runs many times with no one watching, so it is written differently from a chat prompt. *"There is no such thing as a perfect prompt"*. A good one *"has evolved through continual tuning based on observation"* ([[src-huntley-ralph]]). Up: [[practice]].

## Structure (distilled from Ralph's CURSED prompt)
From [[src-huntley-ralph]]:
1. **Load the stack.** Study the specs, the source layout and the plan (`fix_plan.md`, which *"may be incorrect"*).
2. **Pick one thing.** *"choose the most important thing"*. Search first, and *"don't assume not implemented"*.
3. **Do it with bounded parallelism.** Many subagents for search and writes, **one** for build and test.
4. **Apply backpressure.** Run the tests for the unit you changed, and implement whatever is missing *"as per the application specifications"*.
5. **Write back state.** Update the plan with findings. Update `AGENT.md` with build learnings, briefly and with no status reports.
6. **Commit on green.** Commit and push, and tag when the build and tests are clean.
7. **Add guard signs** for observed misbehaviour, such as *"DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS."*

## Pocock's prompt blocks
These are copy-ready sections to add to a Ralph prompt ([[src-pocock-ralph-tips]], [[src-pocock-getting-started-with-ralph]], [[src-pocock-tracer-bullets]]):

| Block | Gist |
|---|---|
| Core | `@PRD.md @progress.txt`. Pick the highest-priority task, check feedback loops, append progress, commit. *"ONLY WORK ON A SINGLE FEATURE."* |
| Completion | *"If … all work is complete, output `<promise>COMPLETE</promise>`."* See [[termination]]. |
| Progress | Append the task, PRD reference, decisions with reasons, files and blockers. *"Sacrifice grammar for the sake of concision."* |
| Feedback gate | Run typecheck, tests and lint. *"Do NOT commit if any feedback loop fails."* See [[backpressure]]. |
| Step size | One logical change per commit. Split large tasks. Run checks after each change. See [[task-sizing]]. |
| Priority | Architecture → integration → unknowns → standard features → polish. *"Fail fast on risky work."* |
| Quality bar | *"This codebase will outlive you … Fight entropy."* See [[agent-experience]]. |
| Tracer bullets | Build a tiny end-to-end slice first, get feedback, then expand. |

## Tan's five-part prompt
A useful prompt carries up to five things, each fitting in a sentence ([[src-tan-pstack-guide-poteto-mode]]):
1. **The goal.**
2. **A done check that can pass or fail.**
3. **The proof you want to see**, such as command output, a video, the stored value, or before/after numbers.
4. **What you already know**, such as a symptom, a job id or a log line.
5. **Real constraints**: "repro first", "don't change any code yet", "zero behavior change".

Leave out *the how* and, at first, *your theory of the cause*. Don't list skills, because the playbook sequences them. **Steer with principle names** in one line, e.g. *"apply prove it works. show me the real output, not the build log"*. The agent must state which decision each principle changed ([[src-tan-pstack-guide-principles]], [[src-tan-pstack-guide-recipes]]). For an unattended run, use the [[overnight-contract]].

## Principles
- **Tune by observation**, but encode durable lessons in structure: lints, types, checks, scripts. *"The instruction is the symptom"* ([[src-tan-pstack-loop-principles]]). See [[build-the-lever]]. Huntley's version is that every bad behaviour gets a sign. *"Each time Ralph does something bad, Ralph gets tuned - like a guitar"* ([[src-huntley-ralph]]).
- **Stay in scope.** Model it on Claude Code's maintenance prompt: continue unfinished work, then tend the PR, then clean up, and *"not start new initiatives"* ([[src-claude-code-scheduled-tasks]]).
- **Make "nothing to do" cheap.** *"If everything is green and quiet, say so in one line"* ([[src-claude-code-scheduled-tasks]]).
- **Call a skill, don't paste a wall.** Keep the scheduled prompt short and the knowledge in a maintained skill ([[src-osmani-loop-engineering]]).
- **Make the stop condition checkable.** See [[goal-spec]].
- **Treat tool docs as prompts too.** Give them the same care as the ACI ([[src-anthropic-building-effective-agents]]).

## Contradictions & open questions
- Huntley says copying his prompt verbatim *"won't make sense unless you know how to wield it"* ([[src-huntley-ralph]]). Prompts are local to an operator and a codebase, which is an argument *against* portable loop definitions. See [[open-questions]].

## Related
[[claude-code-loop]] · [[ralph-loop]] · [[loop-design-checklist]]
