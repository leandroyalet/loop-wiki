---
type: source
branch: sources
tags: [loop-engineering, secondary, industry]
sources: []
url: https://thenewstack.io/loop-engineering/
author: Janakiram MSV (The New Stack)
published: 2026-06-10
raw: raw/2026-10-11-tns-loop-engineering.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# The New Stack — "…he ditched prompting — now he just writes loops" (2026-06-10)

**Author:** Janakiram MSV · **Raw:** `raw/2026-10-11-tns-loop-engineering.md` · Up: [[sources]]

## Summary
Industry coverage published three days after [[src-osmani-loop-engineering]]. It retells the Cherny/Steinberger/Osmani origin story and adds framing of its own. Loop engineering is called *"an orchestration pattern that combines scheduled execution, isolated workspaces, verifier agents, and persistent memory."*

## Key claims
- **Cron vs loop:** *"a cron job runs a fixed script, while a loop runs a model that reads the current state and chooses its next action."* This is the cleanest one-line distinction in the wiki. See [[decision-step]] and [[scheduled-loop]].
- **Lineage:** prompt engineering → context engineering → harness engineering → loop engineering, *"in fewer than 18 months."* See [[loop-vs-prompt-engineering]].
- Before loops, *"the human [was] both scheduler and quality gate."* A loop takes over both roles. See [[human-in-the-loop]].
- It counts **six** building blocks, where Osmani's text says "five things and then one place to remember stuff." See [[loop-primitives]].
- **The verifier is the part that earns trust.** It cites Anthropic's harness work for long-running agents. See [[verification]].
- Ramp's *Inspect* built the same closed-loop shape as bespoke infrastructure about six months earlier. Its arrival as a first-party feature suggests that *"closed-loop operation is becoming the default."*
- On cost, it says you can start with **one scheduled triage automation and one verifier sub-agent** to capture most of the value cheaply. See [[budgets-and-cost]].
- **Portability prediction:** *"the vendor that makes loop definitions portable will take pole position."* Cursor, Antigravity and the Copilot app orchestrate agents, but none names a loop as its unit of work. See [[open-questions]].

## Pages touched
[[loop-engineering]], [[loop-primitives]], [[decision-step]], [[scheduled-loop]], [[verification]], [[budgets-and-cost]], [[human-in-the-loop]], [[loop-vs-prompt-engineering]], [[boris-cherny]], [[open-questions]]
