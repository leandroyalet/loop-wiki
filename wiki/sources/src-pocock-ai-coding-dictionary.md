---
type: source
branch: sources
tags: [loop-engineering, pocock, vocabulary]
sources: []
url: https://www.aihero.dev/ai-coding-dictionary
author: Matt Pocock
published: 2026-09-24
raw: raw/2026-10-12-pocock-ai-coding-dictionary.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "AI Coding Dictionary" (index + 9 entries, 2026-09-24)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-ai-coding-dictionary.md` · Up: [[sources]]

## Summary
A plain-English glossary of agentic coding. The raw file holds the full index plus nine full entries: software factory, dark factory, AFK, human-in-the-loop, smart zone, automated check, automated review, handoff artifact and harness. It is the closest thing in the wiki to a **controlled vocabulary**, and its *software factory* is essentially loop engineering under another name. See [[software-factory]].

## Key claims
- **Software factory:** *"agent sessions are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human."* *"One cron job that runs one kind of session and opens one reviewable PR is a factory."* *"Deciding which of those decisions stay human is the main design question."* See [[software-factory]] and [[trigger]].
- **Dark factory:** a factory whose output no human reads. It is *"vibe coding for an area of code."* When something breaks, you debug code nobody has read. See [[operator-debts]].
- **AFK:** the characteristic failure is *"hours of finished, confident work built on a wrong call made in the first ten minutes."* Give input before (grilling, a spec), during (checks and review), and after (*"a PR, not changes already merged"*). See [[afk]].
- **Human-in-the-loop:** choose it by asking *"how expensive is a wrong turn, and how late would you catch it?"* See [[human-in-the-loop]].
- **Smart zone:** the dumb zone begins *"around 125K-150K tokens — though this is debated"*. *"Plan around the smart zone, not the window."* Use one task per session. See [[smart-zone]].
- **Automated check vs automated review vs human review.** Checks are deterministic, and *"A flaky check poisons"* the self-correction loop. Review is a judgement by an agent with a fresh context. *"treat it as a filter … not a gate."* See [[verification]].
- **Terminology:** *"Avoid: 'feedback loop' / 'backpressure' — both lump checks together with review."* See [[backpressure]].
- **Handoff artifact:** specs, tickets and plans written for a zero-context reader. They are secondary sources, so verify claims against the code. See [[context-and-state]].
- **Harness:** everything around the model, including tools, prompt, context management, permissions and hooks. *"The agent loop — model proposes, harness executes, repeat — is run by the harness."* See [[agent-loop]].

## Pages touched
[[software-factory]], [[afk]], [[human-in-the-loop]], [[smart-zone]], [[verification]], [[backpressure]], [[context-and-state]], [[agent-loop]], [[operator-debts]], [[trigger]], [[agent-experience]], [[loop-engineering]]
