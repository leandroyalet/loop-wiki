---
type: synthesis
branch: syntheses
tags: [loop-engineering, synthesis, lineage]
sources: ["[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-anthropic-building-effective-agents]]", "[[src-huntley-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-loops-you-can-trust]]", "[[src-tan-how-i-use-cursor]]"]
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Loop engineering vs prompt engineering

Up: [[syntheses]].

## The shift
| | Prompt engineering | Loop engineering |
|---|---|---|
| Who prompts the agent | you, turn by turn | a system you designed ([[src-osmani-loop-engineering]]) |
| Human role | *"both scheduler and quality gate"* ([[src-tns-loop-engineering]]) | designer, reviewer, tuner. See [[human-in-the-loop]]. |
| Unit of work | a prompt + context | a loop: trigger, state, verifier, stop condition. See [[anatomy]]. |
| Memory | the conversation | files and boards on disk. See [[context-and-state]]. |
| Quality check | you read the reply | a checker agent plus backpressure. See [[verification]]. |
| Main risk | a bad answer | unattended mistakes, cost, comprehension debt. See [[failure-modes]] and [[operator-debts]]. |

## Lineage
*"Developers went from prompt engineering to context engineering to harness engineering to loop engineering in fewer than 18 months"* ([[src-tns-loop-engineering]]). Osmani places loop engineering *"one floor above the harness. The harness but it runs on a timer, it spawns little helpers, and it feeds itself"* ([[src-osmani-loop-engineering]]). Ralph (2025) did it before the name existed, with nothing but bash ([[src-huntley-ralph]]).

The practitioner's lineage is different ([[src-pocock-ralph-tips]]):
1. **Vibe coding:** accept without checking.
2. **Planning:** plan mode, but still one context window.
3. **Multi-phase plans:** a separate window per phase, but *"requires constant human involvement to write each prompt."*
4. **Ralph:** the same prompt in a loop, and *"the agent chooses the task, not you."*

The next step is the **[[software-factory]]**, where triggers, not humans, start the sessions ([[src-pocock-ai-coding-dictionary]]).

## Tan: it's management
Tan frames loop engineering as **management** (Grove's *High Output Management*), not prompting. You find the limiting step, decide what runs in parallel, choose where to inspect quality, and spend your attention where it has the most leverage. Agents are *"brilliant new hires with amnesia"*, and the engineer's job is now *"observing where agents struggle and building systems that help them succeed"* ([[src-tan-loops-you-can-trust]]). She also argues that *"using a cli just makes you, the human, the orchestrator"* ([[src-tan-how-i-use-cursor]]).

## Is it harder or easier? *(synthesis)*
- Osmani: *"loop design [is] harder than prompt engineering, not easier … the leverage point moved."* Prompting directly is *"also effective. It's all about finding the right balance."* ([[src-osmani-loop-engineering]])
- Anthropic's older advice still applies as a brake. Prefer the simplest system that works and add agentic complexity *"only when it demonstrably improves outcomes"* ([[src-anthropic-building-effective-agents]]). Not every task deserves a loop.
- Pocock: *"Every tip in this article works for human developers too … Ralph makes them non-negotiable"* ([[src-pocock-ralph-tips]]). Loops don't add new engineering. They remove the option to skip the old engineering.
- Huntley: prompts are still central. A loop is a prompt that gets tuned over and over ([[src-huntley-ralph]]). See [[writing-a-loop-prompt]].

## Related
[[loop-engineering]] · [[loop-primitives]]
