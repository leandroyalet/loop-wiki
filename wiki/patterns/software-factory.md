---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, factory, triggers]
sources: ["[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-triage-skill]]", "[[src-osmani-loop-engineering]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-loops-you-can-trust]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Software factory (and dark factory)

A **software factory** is *"a system of work where agent sessions are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human"* ([[src-pocock-ai-coding-dictionary]]). It is the same idea as [[loop-engineering]] from another angle *(synthesis)*. Osmani: *"replacing yourself as the person who prompts the agent"* ([[src-osmani-loop-engineering]]). Pocock: *"A factory takes the human out of starting sessions, and not necessarily out of anything else."* Up: [[patterns]].

## Where it sits in the loop
A factory is a set of [[trigger]]s wired to sessions. Everything else is a design choice about where [[human-in-the-loop|humans]] remain.

## Triggers → sessions
From [[src-pocock-ai-coding-dictionary]]:

| Trigger | Session | Example |
|---|---|---|
| Issue created or labelled | explore, fix, implement | `ready-for-agent` label → a session that opens a PR. See [[backlog-triage]]. |
| Schedule (cron) | recurring maintenance | *"One lint rule fixed per night."* See [[scheduled-loop]] and [[improvement-loops]]. |
| CI failure or alert | diagnose and attempt a fix | a broken build on main → find the breaking commit and propose a fix. See [[event-driven-loop]]. |
| Another session finishing | follow-on work | a PR → automated review → a fix-up session. See [[evaluator-optimizer]]. |

## Start small
*"One cron job that runs one kind of session and opens one reviewable PR is a factory."* Narrow loops produce small, similar PRs, and *"reviewing them shows how far the loop can be trusted before it's widened"* ([[src-pocock-ai-coding-dictionary]]). This matches TNS's "one triage automation and one verifier" advice. See [[budgets-and-cost]].

## Dark factory
A factory whose output **no human reads**. It is *"vibe coding for an area of code, not for one change."* Automated checks and automated review become the only gates. When something breaks, *"You must debug code that nobody on the team has read"* ([[src-pocock-ai-coding-dictionary]]). It is **not** dark just because it runs AFK: if a human reviews the PRs, it is an ordinary factory. See [[operator-debts]].

## Tan: trust is the prerequisite
*"the key for building your own software factory is trust. Unless you can trust an agent to own a problem end-to-end, including verification, you cannot automate your processes"* ([[src-tan-how-i-use-cursor]]). Her factory is a [[stage-gated-pipeline]] in which *"one automation can feed the next without waiting for me to carry the context between them"* ([[src-tan-loops-you-can-trust]]).

## Contradictions & open questions
- **Is a dark factory a goal or a hazard?** Pocock: a hazard, where *"You must debug code that nobody on the team has read"* ([[src-pocock-ai-coding-dictionary]]). Tan: *"true agent parallelism, like in a dark factory for software, might be possible"* once trust is earned ([[src-tan-how-i-use-cursor]]). Her **Autopilot-full** merges PRs on a fresh verifier swarm's clean verdict without human review ([[src-tan-pstack-guide-overnight]]). Her benny automations, though, are **draft-PR only** ([[src-tan-benny-automation]]).
- Huntley asks *"Why are humans the frame for maintainability?"* ([[src-huntley-ralph]]). That position effectively endorses dark factories for greenfield work. Pocock and Osmani treat human review as the main safeguard.

## Related
[[afk]] · [[loop-primitives]] · [[loop-pattern-comparison]]
