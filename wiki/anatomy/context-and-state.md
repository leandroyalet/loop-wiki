---
type: concept
branch: anatomy
tags: [loop-engineering, anatomy, memory, context]
sources: ["[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-tns-loop-engineering]]", "[[src-karpathy-llm-wiki]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-seven-phases]]", "[[src-pocock-ralph-plugin]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-overnight]]", "[[src-agentos-docs]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
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

## A shared memory graph
[[agentos]] puts state outside any one repo. A personal knowledge graph (one SQLite file) holds entities and their relationships, and *"agent memory"* is listed among the things that must live on it rather than in side stores. Any MCP client can query it, and agents should prefer an entity query over a live skill call. *"Computed, not stored"*: derived properties like a task's status are worked out at query time rather than cached ([[src-agentos-docs]]). *(synthesis)* This is cross-session, cross-tool state, a step beyond the per-repo files above. No source yet shows a loop using it.

## Rules loaded on demand (omp TTSR)
[[omp]] keeps some rules *out* of context until they are needed. A time-traveling stream rule *"sit[s] dormant until the model goes off-script"*. On a match it is injected as a system interrupt, so there is no *"context tax on every turn,"* and *"Injections survive compaction."* In goal mode, persisted todos are injected as *"live progress state for current goal, not old transcript decoration"* ([[src-omp]]).

## Spec, ledger and event store (Ouroboros)
[[ouroboros]] splits durable state three ways ([[src-ouroboros]]):
- the **Seed** (what to build), as YAML
- the **Ledger** (assumptions, non-goals, the grounds for decisions)
- an **EventStore** (every execution event, in SQLite)

Ralph's generations are *"stateless: the EventStore reconstructs the full lineage,"* so a restart picks up where the loop left off. *(synthesis)* This is "memory on disk, not in context" turned into event sourcing.

## Fresh context vs accumulated context
Pocock: a bash loop gives *"each iteration … a fresh context window"*, and state survives only through files and git. An in-session loop drags all of its history forward into the dumb zone ([[src-pocock-ralph-plugin]]). See [[smart-zone]].

[[openprose]] makes the same choice a tenet: *"Continuity lives in the trail, not a session. Every unit of work is bounded; nothing depends on a process that runs forever."* Its durable state is each node's world-model plus a signed, append-only receipt ledger. A render's scratch workspace reaches the published state only through an explicit commit. *"SQL, vector stores, and dashboards are derived projections, never the truth"* ([[src-openprose]]).

## Shared context vs handed-back summaries
Anthropic argues that, within one task, results should stay in **one window**: an agent that has seen each earlier step can connect them, which beats *"a set of summaries handed back by subagents"*, and every handoff is lossy. It keeps the window manageable with [[progressive-disclosure]] instead of splitting ([[src-anthropic-fold-subagents]]). The design still *"requires discipline"*: deliberate handling of context windows, memory and note-taking. See [[folding-subagents]].

## Contradictions & open questions
- Osmani says that without skills the loop *"re-derives your whole project from zero every cycle"*, and with them it compounds. Huntley *chooses* to re-load specs every loop and accepts the waste as the price of consistency. These are not strictly contradictory, but the two sources weigh the trade-off differently.
- TNS lists `CLAUDE.md` and auto memory as Claude Code's memory. Osmani lists `AGENTS.md` and progress files. These look like different emphases rather than a conflict.
- **One window vs fresh windows.** Anthropic's shared-context argument ([[src-anthropic-fold-subagents]]) pulls against Ralph's fresh context per iteration and the main thread kept lean by subagents ([[src-pocock-ralph-plugin]], [[src-huntley-ralph]]). *(synthesis)* The first is about one task or conversation, the second about iterations of an outer loop. See [[smart-zone]].

## Related
[[loop-primitives]] · [[llm-wiki-pattern]] · [[failure-modes]] · [[smart-zone]] · [[agent-experience]]
