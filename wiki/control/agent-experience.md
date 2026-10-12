---
type: concept
branch: control
tags: [loop-engineering, control, ax, architecture]
sources: ["[[src-pocock-codebases-agents-love]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tdd-skill]]", "[[src-tan-x-short-posts]]", "[[src-tan-complete-guide-pstack-pt1]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Agent experience (AX) and codebase design

**AX** is *"how well the environment is set up for an agent to do good work — checks, architecture, and free context"* ([[src-pocock-ai-coding-dictionary]]). For loops, the codebase is the strongest influence on output, *"way more than your prompt or your AGENTS.md file"* ([[src-pocock-codebases-agents-love]]). Up: [[control]].

## The repo wins
Instructions compete with the codebase. *"You can write 'never use any types' in your prompt. But if Ralph sees any throughout your existing code, it will follow the codebase."* *"Agents amplify what they see."* Ralph can add dozens of commits in hours, so **software entropy compounds fast** ([[src-pocock-ralph-tips]]). The fixes:
- Clean up before letting the loop loose.
- Enforce standards with checks. See [[backpressure]].
- State the quality bar explicitly: prototype, production or library ([[src-pocock-ralph-tips]]).

## Deep, grey-box modules
- An agent is *"a new starter with no memory"*, and you spawn *"20+ new starters a day"* ([[src-pocock-codebases-agents-love]]).
- **Deep modules** have a small interface over a lot of implementation. A folder per module with a clear public interface gives **progressive disclosure** ([[src-pocock-codebases-agents-love]]).
- **Grey box:** *"You own the interface. AI owns the implementation. Tests keep it honest"* ([[src-pocock-codebases-agents-love]]). This is why QA code review *"may not always be necessary (especially with gray box architectures)"* ([[src-pocock-seven-phases]]).
- Design for testability: inject dependencies and return results ([[src-pocock-tdd-skill]]).

## Hard constraints beat instructions
Tan: *"codebases designed for agents need hard constraints so that even the dumbest agent (and pilot) can contribute meaningfully … refactoring your codebase and choosing a tech stack with strong type systems/compiler diagnostics has far greater impact than AGENTS.md and tweaking your skills. the best rules are in your code"* ([[src-tan-x-short-posts]]). Pick a debuggable stack, because *"The harder your tech stack is to debug and control, the more difficult it will be to use agents productively"* ([[src-tan-complete-guide-pstack-pt1]]). Keep a **gardener** who turns each smell into a rule ([[src-tan-x-short-posts]]). See [[build-the-lever]].

## Where it sits in the loop
AX shapes [[context-and-state]] (what the agent can find cheaply), [[observation]] (how fast feedback arrives), and [[verification]] (whether checks are trustworthy). *"AX matters most in AFK runs"* ([[src-pocock-ai-coding-dictionary]]). See [[afk]].

## Contradictions & open questions
- Huntley would not run Ralph on an existing codebase at all ([[src-huntley-ralph]]). Pocock's answer is to make the codebase ready first. These may be compatible: a messy existing repo is exactly the bad-AX case.

## Related
[[operator-debts]] · [[task-sizing]]
