---
type: practice
branch: practice
tags: [loop-engineering, practice, tooling, encode-lessons]
sources: ["[[src-tan-loops-you-can-trust]]", "[[src-tan-pstack-guide-principles]]", "[[src-tan-pstack-loop-principles]]", "[[src-tan-pstack-guide-recipes]]", "[[src-tan-x-short-posts]]", "[[src-huntley-ralph]]", "[[src-pocock-git-guardrails-hook]]", "[[src-inside-pstack-report]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-12
updated: 2026-10-27
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

### The `/correct` ladder
pstack's `/correct` makes this a procedure. A mistake counts as a **class** once it has happened twice. Fix it at the highest level that works:
1. architecture (one owner, one way, hide internals)
2. types, or a lint *whose error names the fix*
3. behaviour tests
4. docs, and only for judgment calls, because *"Nothing fails when an agent skips them"*

Each new check must fail on a real past mistake. The agent instruction file keeps a **rule → enforcer table**. *"If the rule was already there and nothing enforces it, that's a repeat"* ([[src-inside-pstack-report]]). The ladder started as a post: *"every time you intervene and correct your agent, you should think about how to eliminate it entirely"*, with human review last (*"ngmi"*) ([[src-inside-pstack-report]]).

### pstack applies it to itself
About 7k lines of scripts enforce the rules the prose would otherwise only ask for. The report's summary: *"Written prose only guides. Only the scripts actually enforce anything"* ([[src-inside-pstack-report]]). Two loop-relevant examples:
- `watch-pr` turns "is this PR ready?" into a typed exit code.
- `orch` keeps the orchestration ledger in files rather than in a model's memory.

The full table is on [[pstack]].

### The reviewer's misses become context (Claude Code team)
If the automated reviewer *"is consistently flagging the same issue, we fix it at the source -- via the skill itself, a lint rule, or updating documentation files"* such as `CLAUDE.md` and `REVIEW.md`. In the other direction, *"whenever our reviewers miss something, we ask ourselves what wasn't in the model's context, and turn that into a CLAUDE.md file, a skill or a new check"* ([[src-osmani-claude-code-code-review]]). See [[layered-code-review]].

### Code for the mechanical, model for the judgment (Anthropic)
In Anthropic's single agent loop, code still loads cheap, almost-always-relevant context (such as entity resolution) and does the mechanical work (payload construction, stream parsing, resuming a clarification) inside the tools the loop calls. Domain procedure goes into skills, and hard limits into tools ([[src-anthropic-fold-subagents]]). See [[folding-subagents]].

## Compared with tuning by signs *(synthesis)*
| Approach | Where the lesson lives | Source |
|---|---|---|
| Huntley's "signs" | more instructions in `PROMPT.md` | [[src-huntley-ralph]] |
| Pocock's git hook | a hard `PreToolUse` guardrail, *"not a suggestion buried in prose"* | [[src-pocock-git-guardrails-hook]] |
| Claude Code team | skills, lint rules, `CLAUDE.md` and `REVIEW.md`, plus incident cases in the reviewer's eval set | [[src-osmani-claude-code-code-review]] |
| Tan's encode-in-structure | lints, types, checks, scripts and architecture | [[src-tan-pstack-loop-principles]] |

Prompt signs are the quickest fix. Structural encodings are the ones that last. Tan's rule: *"If the fix is structural, only use the structural fix."*

## Related
[[agent-experience]] · [[backpressure]] · [[writing-a-loop-prompt]]
