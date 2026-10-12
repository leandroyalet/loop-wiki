---
type: practice
branch: practice
tags: [loop-engineering, practice, verification, tooling]
sources: ["[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-loops-you-can-trust]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Verification skill (app control CLI + Feature Map)

A per-app skill that lets any agent **launch, drive, inspect and prove** the real application. Tan calls it *"critical infrastructure rather than 'just' a skill"* and the foundation every other loop builds on ([[src-tan-complete-guide-pstack-pt1]]). Up: [[practice]].

## Where it sits in the loop
It is what makes [[verification]] and [[observation]] possible without a human. It is therefore the precondition for [[earned-autonomy]].

## Origin
At Cursor, Tan's `/control-glass` launched a dev build with the Chrome DevTools Protocol, so agents could click, type, read the accessibility tree, take screenshots, record video, throttle, profile and take heap snapshots. *"Every future agent got those capabilities for free"* ([[src-tan-loops-you-can-trust]]).

## Parts
- **Control CLI** (a "lever"). From [[src-tan-complete-guide-pstack-pt1]]:
  - composable deep-module commands
  - `--dry-run` on anything destructive
  - subcommands for progressive disclosure
  - errors that say what to do instead
  - rich `--help`
  - JSON output

  See [[build-the-lever]].
- **Skill sections:** Launch, Doctor, Drive, Evidence, Cleanup ([[src-tan-pstack-guide-verify-and-ship]]).
- **Feature Map:** a README index plus one file per feature, covering what it does, how to reach it, and *what result proves it works*. It is *"materialized memory"* that saves tokens ([[src-tan-complete-guide-pstack-pt1]]). See [[context-and-state]].
- **Repeatable dev environment:** seeded data, test users, one command to bring it up ([[src-tan-complete-guide-pstack-pt1]]).

## Lifecycle
- **Create:** `/create-verification-skill` *"interviews the repository, not you."* It must pass one end-to-end proof (launch → doctor → drive one feature → capture evidence → clean up). *"If that proof fails, don't use the output"* ([[src-tan-pstack-guide-verify-and-ship]]).
- **Maintain:** `/maintain-verification-skill` **daily, from a scheduled automation**. It ends in `clean`, `changed` or `blocked`, never edits product code, and reports product regressions rather than papering over them ([[src-tan-pstack-guide-verify-and-ship]]). This is a [[scheduled-loop]] that keeps the other loops honest *(synthesis)*.
- **Scale:** `/swarm` fans out cloud agents across Feature Map entries, perf samples or fuzzing runs ([[src-tan-complete-guide-pstack-pt1]]).

## Contradictions & open questions
- Tan's results come from Electron and web apps with CDP. She says hard-to-debug stacks make agents much less productive, and would even switch stacks ([[src-tan-complete-guide-pstack-pt1]]). Sources on backends, mobile or embedded systems are still missing. See [[open-questions]].

## Related
[[backpressure]] · [[agent-experience]] · [[stage-gated-pipeline]]
