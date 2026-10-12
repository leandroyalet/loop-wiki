---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, automation, event-driven]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/automations/benny
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-benny-automation.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack — benny automation pack (README + FOR_AGENTS)

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-benny-automation.md` · Up: [[sources]]

## Summary
A dormant, open-sourced pack of two **Cursor Automations** for a Slack issue channel. It is written as a statement of intent ("what i want to automate") that an agent reads in order to set the pack up. It is the reference implementation of the [[stage-gated-pipeline]].

## Key claims
- **Automation 1, triage.** Trigger: a new top-level Slack report. It classifies the report (bug/perf, feature request, question/feedback, reroute), traces the owning layer, searches the tracker for duplicates, and creates a ticket **only for a clear net-new bug**. Outcome: *exactly one* thread reply with a `[benny:bug|performance|other]` marker.
- **Automation 2, repro and fix.** It waits for the trusted triage marker. **Gates:** it stops if someone clearly owns the fix, and if a PR may already fix it, it verifies that PR instead of competing with it. It must **reproduce the exact symptom twice through the real UI**, with screenshots, video and a read-only state cross-check. After that it may attempt **one bounded root-cause fix** (TDD when cheap, check the blast radius), and opens a draft PR *only when before/after proof passes*.
- **Shared rules:**
  - never post a root message in the channel
  - thread coordinates stay immutable
  - subagents may help but get **no Slack credentials**
  - **fail closed** if config is missing or uncertain
  - **draft PRs only, never merge or deploy**
  - configured **budgets** for polling, verdict waits, repro and fix

  See [[guardrails-and-permissions]].
- **Setup:** never overwrite user-owned config. Verify with a *fresh agent* that dependencies resolve at project scope. Don't create an automation until the human explicitly asks. See [[human-in-the-loop]].

## Pages touched
[[stage-gated-pipeline]], [[event-driven-loop]], [[guardrails-and-permissions]], [[backlog-triage]], [[budgets-and-cost]], [[human-in-the-loop]], [[cursor]]
