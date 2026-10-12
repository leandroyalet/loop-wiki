---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, memory, context]
sources: ["[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-tns-loop-engineering]]", "[[src-karpathy-llm-wiki]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-seven-phases]]", "[[src-pocock-ralph-plugin]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-overnight]]"]
created: 2026-10-11
updated: 2026-10-12
status: solid
---
# Context and state

**State** is what survives between iterations. **Context** is what one iteration loads into the model's window. The model forgets everything between runs, *"so the memory has to be on disk and not in the context. The agent forgets, the repo doesnt."* ([[src-osmani-loop-engineering]]). Up: [[anatomy]].

## Where it sits in the loop
State is read at the start of each iteration and written back at the end. Osmani calls the state file *"the spine of the whole thing"* ([[src-osmani-loop-engineering]]).

## What lives where
| Kind | Examples | Sources |
|---|---|---|
| Progress / plan | `fix_plan.md`, a progress markdown file, a Linear board | [[src-huntley-ralph]], [[src-osmani-loop-engineering]] |
| Session log | `progress.txt`: tasks, decisions, blockers, files. Committed, and **deleted after the sprint**. | [[src-pocock-ralph-tips]] |
| Git history | one commit per feature gives a log, a diff and a rollback point. *"full context without burning tokens on exploration"* | [[src-pocock-ralph-tips]] |
| Research cache | `RESEARCH.md` for hard-to-reach docs. Sprint-scoped, because *"Research can go out of date"* | [[src-pocock-seven-phases]] |
| How-to-run knowledge | `AGENT.md` / `AGENTS.md` / `CLAUDE.md`, which the loop updates as it learns | [[src-huntley-ralph]], [[src-tns-loop-engineering]] |
| Project conventions | Skills (`SKILL.md`), *"intent written down on the outside"* | [[src-osmani-loop-engineering]] |
| Why-notes | Doc comments that explain *why* a test exists, written for future iterations | [[src-huntley-ralph]] |
| Accumulated knowledge | A persistent LLM-maintained wiki | [[src-karpathy-llm-wiki]] |

## Context discipline (from Ralph)
These come from [[src-huntley-ralph]]:
- **Allocate the same way every loop:** always load the plan and the specs.
- **Keep the window small.** With about 170k tokens, *"the more you use the context window, the worse the outcomes."* This is why Ralph does **one item per loop**.
- **Main context is a scheduler.** Expensive reads such as test output go to subagents, so they don't fill the primary window. See [[orchestrator-workers]].

## Handoff artifacts
Specs, tickets, plans and progress files are **handoff artifacts**: *"written to the environment by one session to be read by another."* Write them for a reader with zero context, using concrete paths, decisions with their reasons, and what's done and what's left. They are **secondary sources**, *"an account of the session's work, not the work itself"*, so a later session should verify important claims against the code and tests. Unlike in-memory compaction, they can be read, corrected and reused, and *"the same spec can brief five parallel sessions"* ([[src-pocock-ai-coding-dictionary]]).

## The codebase as memory
Tan: *"I think your codebase is the ultimate form of memory. Code is a projection of the decision making you and your team have made."* A **Feature Map** is a compact, token-saving projection of the code, i.e. *"materialized memory"*, shared by everyone because it lives in a skill ([[src-tan-complete-guide-pstack-pt1]]). See [[verification-skill]]. Pause and resume work through a WIP commit plus a **resume note** that a fresh chat picks up ([[src-tan-pstack-guide-overnight]]).

## Fresh context vs accumulated context
Pocock: a bash loop gives *"each iteration … a fresh context window"*, and state survives only through files and git. An in-session loop drags all of its history forward into the dumb zone ([[src-pocock-ralph-plugin]]). See [[smart-zone]].

## Contradictions & open questions
- Osmani says that without skills the loop *"re-derives your whole project from zero every cycle"*, and with them it compounds. Huntley *chooses* to re-load specs every loop and accepts the waste as the price of consistency. These are not strictly contradictory, but the two sources weigh the trade-off differently.
- TNS lists `CLAUDE.md` and auto memory as Claude Code's memory. Osmani lists `AGENTS.md` and progress files. These look like different emphases rather than a conflict.

## Related
[[loop-primitives]] · [[llm-wiki-pattern]] · [[failure-modes]] · [[smart-zone]] · [[agent-experience]]
