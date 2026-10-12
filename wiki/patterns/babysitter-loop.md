---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, ci, pr]
sources: ["[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-tan-pstack-guide-verify-and-ship]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Babysitter loop (PR / CI until green)

A **babysitter loop** tends one artefact, such as a PR, deploy or release branch, until it reaches a healthy state. The Claude Code docs list *"poll a deployment, babysit a PR, check back on a long-running build"* as core uses ([[src-claude-code-scheduled-tasks]]). Up: [[patterns]].

## Examples
- `/loop check whether CI passed and address any review comments`. This is self-paced, and it waits longer once the PR goes quiet ([[src-claude-code-scheduled-tasks]]).
- A `loop.md` that keeps `release/next` healthy: if CI is red, pull the log, diagnose and push a minimal fix; address new review comments; *"If everything is green and quiet, say so in one line"* ([[src-claude-code-scheduled-tasks]]).
- A bare `/loop` uses the built-in maintenance prompt, which tends the current branch's PR (comments, failed CI, merge conflicts) after finishing any unfinished work ([[src-claude-code-scheduled-tasks]]).
- A connector-driven variant opens the PR, links the ticket and *"pings the channel once CI is green by itself"* ([[src-osmani-loop-engineering]]).

- pstack's **Babysit** playbook handles blockers in order: conflicts → review threads → CI. It batches every known fix into one push, so checks restart once. It triages comments skeptically and posts the disproof when it dismisses one. It **stops at merge-ready and never merges**, *"because merging is a different decision"* ([[src-tan-pstack-guide-verify-and-ship]]).

## Where it sits in the loop
Its [[goal-spec]] is a health state (green CI, no unresolved comments). It usually runs as a [[self-paced-loop]].

## Related
[[claude-code-loop]] · [[guardrails-and-permissions]]
