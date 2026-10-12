---
type: practice
branch: practice
tags: [loop-engineering, practice, tooling, encode-lessons]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-principles]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-pstack-guide-recipes]]", "[[src-tan-x-short-posts]]", "[[src-huntley-ralph]]", "[[src-pocock-git-guardrails-hook]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Build the lever / encode lessons in structure

Two related pstack principles about **moving work and knowledge out of prompts and into durable tools**. They are how a loop gets better over time. Up: [[practice]].

## Build the lever
*"If a script can do a step the same way every time, use the script, and save agents for the judgment calls"* ([[src-tan-pstack-guide-principles]]). Agents are for *"the fuzzy parts: choosing hypotheses, interpreting evidence, and deciding when something needs human judgment"* ([[src-tan-loops-you-can-trust]]).
- **Migration example:** do the first unit by hand to learn the recipe, then have the agent write a **codemod** for the mechanical parts and a **checker** that proves the output. A reviewer can read and re-run both ([[src-tan-loops-you-can-trust]]).
- **Self-made levers:** *"When I see one repeatedly doing something by hand, I have it write the tool or skill it wishes it had. Every future run inherits it"* ([[src-tan-loops-you-can-trust]]).
- **Managerial leverage** (Grove): human work done once as reusable skills multiplies the output of the whole agent team ([[src-tan-loops-you-can-trust]]).
- An example lever is the [[verification-skill]] control CLI.

## Encode lessons in structure
*"Apply when you catch yourself writing the same instruction a second time … Encode the rule as a lint, metadata flag, runtime check, or script instead of more text."* *"The instruction is the symptom"* ([[src-tan-pstack-loop-principles]]). `/correct` lands repeated corrections as architecture, types, lints or tests, *"so the next agent can't make the mistake"* ([[src-tan-pstack-guide-recipes]]). The gardener: *"every weed you pull becomes a rule, so it can't grow back"* ([[src-tan-x-short-posts]]).

## Compared with tuning by signs *(synthesis)*
| Approach | Where the lesson lives | Source |
|---|---|---|
| Huntley's "signs" | more instructions in `PROMPT.md` | [[src-huntley-ralph]] |
| Pocock's git hook | a hard `PreToolUse` guardrail, *"not a suggestion buried in prose"* | [[src-pocock-git-guardrails-hook]] |
| Tan's encode-in-structure | lints, types, checks, scripts and architecture | [[src-tan-pstack-loop-principles]] |

Prompt signs are the quickest fix. Structural encodings are the ones that last. Tan's rule: *"If the fix is structural, only use the structural fix."*

## Related
[[agent-experience]] · [[backpressure]] · [[writing-a-loop-prompt]]
