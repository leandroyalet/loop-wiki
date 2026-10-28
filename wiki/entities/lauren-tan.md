---
type: entity
branch: entities
tags: [loop-engineering, person, pstack]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-how-i-use-cursor]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-tan-pstack-guide-overnight]]", "[[src-inside-pstack-report]]"]
created: 2026-10-12
updated: 2026-10-15
status: draft
---
# Lauren Tan (@poteto)

Engineer, formerly an engineering manager, and on the React Compiler core team. She moved from Meta to [[cursor]] in March 2026 ([[src-tan-how-i-use-cursor]]), and her GitHub profile now lists xAI, where she works on Grok Bot ([[src-tan-complete-guide-pstack-pt1]]). She created **[[pstack]]**. Up: [[entities]].

## Contributions
- **Verification is the limiting step.** She applies Andy Grove's *High Output Management* to agent loops ([[src-tan-loops-you-can-trust]]). See [[verification]].
- **Earned autonomy / depth before breadth:** *"Trying to parallelize agents you don't trust yet is a huge waste of tokens"* ([[src-tan-how-i-use-cursor]]). See [[earned-autonomy]].
- **The overnight contract**, the commit-or-discard iteration and the audited decision log ([[src-tan-pstack-guide-overnight]]). See [[overnight-contract]].
- **The stage-gated maintenance line (benny)** ([[src-tan-benny-automation]]). See [[stage-gated-pipeline]].
- **Verification skills:** a control CLI plus a Feature Map ([[src-tan-complete-guide-pstack-pt1]]). See [[verification-skill]].
- **Build the lever and encode lessons in structure** ([[src-tan-pstack-guide-principles]]). See [[build-the-lever]].
- **Idempotency as a design principle** for loops ([[src-tan-pstack-loop-principles]]). See [[idempotency]].

## Positions
- She is pro-volume once trust exists, and says she ships 2,000 PRs a month (self-reported, [[src-tan-complete-guide-pstack-pt1]]). A third-party report finds her figures **inconsistent across posts**: ~1,000/month (29 Jul), 221 in 2 days (7 Aug), 2,500/month (21 Sep talk). She herself told Pocock *"They're not obviously like 2,500 features"* ([[src-inside-pstack-report]]).
- *"a low trust loop is just a waste of tokens"* (X, 8 Jun 2026, quoted in [[src-inside-pstack-report]]).
- **Correction ladder** (X, 16 Aug 2026), which later became `/correct`: eliminate the problem through architecture, then a lint or test, then a skill or rule, and only last human review (*"ngmi"*) ([[src-inside-pstack-report]]). See [[build-the-lever]].
- **Maintainability.** On 11 Oct 2026 she argued that maintainability and clean code still mattering is *"no longer true"*, and defined good code as *"correct, bug free, fast and cost efficient to run"*. The report notes the tension with pstack's own *minimize-reader-load* principle ([[src-inside-pstack-report]]). See [[software-factory]].

## Affiliation (unverified)
The third-party report says she has worked on Grok Bot at "SpaceXAI" since 17 Aug 2026, *"after SpaceX acquired Cursor"* ([[src-inside-pstack-report]]). The wiki's primary source only shows xAI on her GitHub ([[src-tan-complete-guide-pstack-pt1]]). This is not confirmed by a first-party source.
- She treats a dark factory as a possible destination, not a hazard: *"true agent parallelism, like in a dark factory for software, might be possible"* ([[src-tan-how-i-use-cursor]]). See [[software-factory]].
- She manages agents the way she managed people: *"brilliant new hires with amnesia"* ([[src-tan-loops-you-can-trust]]).
