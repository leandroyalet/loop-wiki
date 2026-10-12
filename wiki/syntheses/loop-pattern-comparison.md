---
type: synthesis
branch: syntheses
tags: [loop-engineering, synthesis, comparison]
sources: ["[[src-huntley-ralph]]", "[[src-claude-code-scheduled-tasks]]", "[[src-osmani-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-benny-automation]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Loop pattern comparison

The outer-loop patterns compared slot by slot. See the pattern pages for citations. Up: [[syntheses]].

| Pattern | [[trigger]] | [[goal-spec]] | [[verification]] | [[termination]] | Best for | Watch out for |
|---|---|---|---|---|---|---|
| [[ralph-loop]] | immediate re-run | specs + `fix_plan.md` | backpressure (tests, types) | none built in, a human watches | greenfield builds | placeholders, drift, broken mornings |
| Ralph, Pocock variant ([[building-a-ralph-loop]]) | capped `for` loop, fresh process per iteration | PRD (JSON `passes`) + `progress.txt` | pre-commit checks block commits | sigil or cap | features from a PRD, HITL → AFK | vague scope, premature victory |
| Overnight contract ([[overnight-contract]]) | Cursor `/loop` on events or heartbeat, in-session | pass/fail finish predicate | real-artifact check each iteration; commit or discard | predicate passes, or escape hatch with a write-up | one hard task overnight | goal reinterpretation, durations as goals |
| [[stage-gated-pipeline]] | event (Slack report), then the previous stage's verdict | per stage (triage verdict, repro twice, proof) | evidence handed forward; any stage can stop | stage verdict; draft PR | maintenance: bug reports → fixes | fail-closed config, duplicate work ([[idempotency]]) |
| [[improvement-loops]] | re-run or nightly cron | a metric target (coverage %, zero lint errors) | the metric tool itself | target reached | coverage, lint, duplication, entropy | gaming the metric |
| [[scheduled-loop]] | cron or interval | the triage skill's criteria | checker sub-agent | expiry or cancel | recurring discovery and triage | jitter, no catch-up, cost of empty runs |
| [[self-paced-loop]] | model-chosen delay | the prompt | model judgment | self-stop or fallback | polling things with variable timing | not restored on resume |
| [[goal-loop]] | next turn, immediately | an explicit, checkable condition | separate grader model | condition true | bounded tasks with a test oracle | unreachable conditions (undocumented caps) |
| [[event-driven-loop]] | pushed event | the prompt | varies | varies | CI/deploy reactions | thin documentation so far |
| [[babysitter-loop]] | self-paced or interval | a health state (green, no comments) | CI itself | goal met or cancel | PRs, deploys, release branches | irreversible actions without authorization |

## Choosing *(synthesis)*
- **Do you have a machine-checkable definition of done?** If yes, use a [[goal-loop]]. If no, use a [[scheduled-loop]] with a human triage inbox.
- **Is the work discovered or assigned?** Discovered work suits a scheduled or event-driven loop. Assigned work suits a goal or Ralph loop.
- **Is it greenfield or an existing codebase?** Huntley limits Ralph to greenfield ([[src-huntley-ralph]]). Osmani's daily triage loop runs on existing repos ([[src-osmani-loop-engineering]]).
- **Can the agent verify its own work yet?** If not, build a [[verification-skill]] before any loop ([[src-tan-loops-you-can-trust]]). See [[earned-autonomy]].
- **Can a human review every output?** If not, you are building a dark factory. Decide that on purpose ([[src-pocock-ai-coding-dictionary]]). See [[software-factory]].
- **Does the loop accumulate context?** Prefer a fresh process per iteration for build work ([[src-pocock-ralph-tips]]). See [[smart-zone]].
- **Does timing vary?** If so, prefer self-paced or event-driven over a fixed cron ([[src-claude-code-scheduled-tasks]]).

## Related
[[patterns]] · [[loop-design-checklist]]
