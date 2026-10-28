---
type: concept
branch: control
tags: [loop-engineering, control, human-factors]
sources: ["[[src-osmani-loop-engineering]]", "[[src-huntley-ralph]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-pocock-codebases-agents-love]]", "[[src-pocock-tracer-bullets]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-complete-guide-pstack-pt1]]", "[[src-osmani-claude-code-code-review]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Operator debts

Osmani names three problems that *"actually get sharper as the loop gets better, not easier"*, plus two related debts from his earlier writing ([[src-osmani-loop-engineering]]). They are failures of the **human running the loop**, not of the loop. Up: [[control]].

| Debt | Meaning | Counter |
|---|---|---|
| **Verification is still on you** | *"'done' is a claim and not a proof."* | A trusted checker, plus your own review. See [[verification]]. |
| **Comprehension debt** | *"The faster the loop ships code you did not write, the bigger the gap between what exists and what you actually get."* | Read what the loop made. |
| **Cognitive surrender** | It is *"tempting to stop having an opinion and just take whatever it gives back."* | Design and run the loop *with judgement*. |
| **Intent debt** | The agent *"will fill any hole in your intent with a confident guess."* | Write intent down as skills or specs. See [[goal-spec]]. |
| **Orchestration tax** | Your review bandwidth caps how many parallel agents you can run | Size the loop to what you can review. See [[isolation]]. |
| **Review burden from slop** | Big all-at-once output leaves *"a huge review burden on the developer"* ([[src-pocock-tracer-bullets]]) | Tracer bullets and small PRs. See [[task-sizing]]. |
| **Cognitive burnout** | You try to *"hold together AI and your codebase, patching it all up manually"* ([[src-pocock-codebases-agents-love]]) | Deep modules: keep 7–8 chunks in your head. See [[agent-experience]]. |
| **Dark factory** | Comprehension debt chosen once for a whole area: *"debug code that nobody on the team has read"* ([[src-pocock-ai-coding-dictionary]]) | Keep human review on the PRs. See [[software-factory]]. |

> "Two people can build the exact same loop and get completely opposite results … The loop doesn't know the difference. You do." ([[src-osmani-loop-engineering]]). TNS repeats this ([[src-tns-loop-engineering]]).

## Contradictions & open questions
- **Does volume matter?** Tan once thought PR counts were *"a vanity metric"*. Now *"volume does matter, especially when you are able to maintain or even increase the level of quality"* (2,000 PRs/month, self-reported, [[src-tan-complete-guide-pstack-pt1]]). She also concedes that *"a hundred agents waiting for prompts and dumping slop PRs into your lap is keeping us busier than ever"* ([[src-tan-loops-you-can-trust]]). Her answer to the orchestration tax is **evidence artifacts that make review cheaper**, not fewer agents.
- **Must someone hold the whole model?** Osmani's loop-engineering essay counters comprehension debt with *read what the loop made* ([[src-osmani-loop-engineering]]). His later write-up of the Claude Code team says the opposite about the whole: *"No member of the team has a full mental model of Claude Code in their head, nor do we think anyone needs to."* Instead people ask Claude for an explainer, or a small visual artifact, on the exact slice they're about to change: *"Creating an explainer about the module you're going to change teaches you a lot,"* while reading a one-line copy diff teaches almost nothing ([[src-osmani-claude-code-code-review]]). *(synthesis)* Comprehension becomes just-in-time and scoped to the change, not continuous.
- **Huntley disagrees on maintainability.** *"Why are humans the frame for maintainability? … you can just run loops to resolve/adapt."* Yet he also says *"engineers are still needed … senior expertise guiding Ralph"* ([[src-huntley-ralph]]). Osmani: *"Build it like someone who intends to stay the engineer."*

## Related
[[human-in-the-loop]] · [[loop-vs-prompt-engineering]]
