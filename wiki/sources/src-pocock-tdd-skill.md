---
type: source
branch: sources
tags: [loop-engineering, pocock, tdd, verification]
sources: []
url: https://www.aihero.dev/skill-test-driven-development-claude-code
author: Matt Pocock
published: 2026-02-10
raw: raw/2026-10-12-pocock-tdd-skill.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "My Skill Makes Claude Code GREAT At TDD" (2026-02-10)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-tdd-skill.md` · Up: [[sources]]

## Summary
LLMs work in **horizontal slices**: all the tests, then all the code. *"Tests written in bulk test imagined behavior, not observed behavior."* The TDD skill forces **vertical red-green-refactor slices**: ONE test → ONE implementation → repeat. *"If a test fails first, the LLM can't fake it."*

## Key claims
- Failure modes of bulk tests: they verify mocks, they short-circuit, and *"When the LLM's context is running low, it might just rewrite the test to make it pass."* See [[failure-modes]].
- Good tests go through **public interfaces** and describe *what*, not *how*. They survive refactors. Bad tests mock internals or check through the DB or call counts.
- A planning phase comes first: interface changes, the behaviours that matter most, deep modules, and testability (inject dependencies, return results). See [[agent-experience]].
- *"honest tests through forced constraints"*: *"when you can trust the tests, you can trust the code."* See [[verification]].

## Pages touched
[[backpressure]], [[verification]], [[task-sizing]], [[failure-modes]], [[agent-experience]]
