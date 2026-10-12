---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, principles, guide]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/docs/guide/08-principles.md
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-guide-principles.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack guide 8 — "Steer with principle names"

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-guide-principles.md` · Up: [[sources]]

## Summary
pstack ships **24 principles** as individual skills. `/poteto-mode` reads their index at the start of every multi-step task and must *name each applied principle and the decision it changed*. *"A principle citation with no decision behind it is the tell that it name-dropped instead of applying."* Humans use the names as one-line steering commands. See [[writing-a-loop-prompt]].

## Key claims
- **Core:** Laziness Protocol, Foundational Thinking, Redesign from First Principles, Attack the Premise, Subtract Before You Add, Minimize Reader Load, Outcome-Oriented Execution, Experience First, Exhaust the Design Space, **Build the Lever** (*"If a script can do a step the same way every time, use the script, and save agents for the judgment calls"*). See [[build-the-lever]].
- **Architecture:** Model the Domain, Boundary Discipline, Type System Discipline, **Make Operations Idempotent**, Migrate Callers Then Delete Legacy APIs, Separate Before Serializing Shared State. See [[idempotency]].
- **Verification:** **Prove It Works**, Fix Root Causes, **Sequence Work into Verifiable Units**, Test Behavior Not Implementation, Explain the Number. See [[verification]].
- **Delegation:** **Guard the Context Window** and **Never Block on the Human**. See [[smart-zone]] and [[human-in-the-loop]].
- **Meta:** **Encode Lessons in Structure**, applied repo-wide by `/correct`.

## Pages touched
[[build-the-lever]], [[idempotency]], [[verification]], [[writing-a-loop-prompt]], [[pstack]]
