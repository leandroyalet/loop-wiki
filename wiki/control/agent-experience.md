---
type: concept
branch: control
tags: [loop-engineering, control, ax, architecture]
sources: ["[[src-pocock-codebases-agents-love]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-tdd-skill]]", "[[src-tan-x-short-posts]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-agentos-docs]]", "[[src-omp]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-12
updated: 2026-10-27
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

## Design the tool surface for the weakest agent (AgentOS)
[[agentos]] carries AX from the codebase to the **tool surface**. *"The customer is the smallest model"*: a 1B-parameter model with a 4K context should be able to read the readme and finish the task on the first try. The reasoning is *"Error Rate = f(Dependency Depth)"*, because every round-trip compounds error ([[src-agentos-docs]]). The practice, called *agent empathy*:
- **Observe first.** Watch an agent use the tool, and notice where it *"misinterpret[s] silence as absence"* or wastes a round-trip.
- **Teach the domain, not the syntax:** mental model first, reference card second.
- **One call, not two.** *"If the server knows something the agent will need, include it in the response."*
- **Dynamic beats static.** A readme that reports live counts *"orients"*. One that says "use list" *"assigns homework"*.
- **Inline, not tabular.** One entity per line with its ID in parentheses, plus a self-teaching footer listing the fields the agent could ask for.
- **Absent is not false.** Explain why a query got zero results, or the agent *"confidently report[s] that nothing exists."*

*(synthesis)* This is the Anthropic ACI and poka-yoke advice ([[src-anthropic-building-effective-agents]]), applied with a concrete test: could the weakest caller succeed after one read? See [[action]].

## Tool surfaces that scale (Anthropic)
- **Intent-level tools.** Group tools by what the user wants, not one per API; tool choice degrades past ~30–50 definitions ([[src-anthropic-fold-subagents]]).
- **Actionable failures.** A tool whose precondition isn't met, or whose user lacks permission, returns an instruction or plain refusal the model can act on ([[src-anthropic-fold-subagents]]).
- **Don't paste reference material.** Put it behind a lookup tool or in skill reference files instead of having code paste it into prompts ([[src-anthropic-fold-subagents]]). See [[progressive-disclosure]].

## The harness is the variable (omp)
Can Bölük: *"the model is but a parameter. The real variable is the harness"*. Tool schemas, error messages and state management are *"where most failures happen in practice."* omp tunes prompts per model and treats GitHub PRs and issues as paths for its `read` tool (`read pr://1428`), so the agent learns *"One interface"* instead of a set of separate GitHub tools ([[src-omp]]). *(synthesis)* This is AgentOS's "design for the weakest caller" rule backed by numbers: the weakest models gained the most from a better edit format.

## Where it sits in the loop
AX shapes [[context-and-state]] (what the agent can find cheaply), [[observation]] (how fast feedback arrives), and [[verification]] (whether checks are trustworthy). *"AX matters most in AFK runs"* ([[src-pocock-ai-coding-dictionary]]). See [[afk]].

## Contradictions & open questions
- **Who is the agent?** AgentOS designs for a 1B local model ([[src-agentos-docs]]). Pocock says local models aren't good enough for coding loops, so *"you have to pay to play"* ([[src-pocock-ralph-tips]]). Tan's version: *"even the dumbest agent (and pilot)"* should be able to contribute ([[src-tan-x-short-posts]]). *(synthesis)* Designing interfaces for the weakest caller and choosing a strong driver model are not in conflict.
- Huntley would not run Ralph on an existing codebase at all ([[src-huntley-ralph]]). Pocock's answer is to make the codebase ready first. These may be compatible: a messy existing repo is exactly the bad-AX case.

## Related
[[operator-debts]] · [[task-sizing]] · [[progressive-disclosure]]
