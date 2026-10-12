---
type: hub
branch: sources
tags: [loop-engineering, hub]
sources: []
created: 2026-10-11
updated: 2026-10-12
status: draft
---
# Sources

One summary page per file in `raw/`. Each page links to the raw file, lists key claims, and names the wiki pages it feeds. Up: [[loop-engineering]].

| Source | Author | Published | What it contributes |
|---|---|---|---|
| [[src-osmani-loop-engineering]] | [[addy-osmani]] | 2026-06-07 | Names the practice. Gives the five building blocks plus memory, the maker/checker split, and the human debts. |
| [[src-tns-loop-engineering]] | Janakiram MSV | 2026-06-10 | Industry framing: cron vs loop, the lineage from prompt engineering to loop engineering, portability. |
| [[src-claude-code-scheduled-tasks]] | [[anthropic]] | — | Reference behaviour of `/loop`, cron tools, self-pacing, jitter and expiry. |
| [[src-huntley-ralph]] | [[geoffrey-huntley]] | 2025-07-14 | The Ralph loop: a bash while-loop, one item per loop, backpressure, signs and tuning. |
| [[src-anthropic-building-effective-agents]] | [[anthropic]] | 2024-12-19 | The inner agent loop, workflow patterns, stopping conditions and the ACI. |
| [[src-karpathy-llm-wiki]] | [[andrej-karpathy]] | — | The pattern this wiki is built on: a persistent, compounding memory maintained by an LLM. |

### Matt Pocock / AI Hero (ingested 2026-10-12)
| Source | Published | What it contributes |
|---|---|---|
| [[src-pocock-getting-started-with-ralph]] | 2026-01-08 | `ralph-once.sh` → `afk-ralph.sh`, Docker sandbox, PRD + progress, completion sigil |
| [[src-pocock-ralph-tips]] | 2026-01-08 | 11 tips: HITL→AFK, scope, progress, feedback loops, small steps, risk-first, "the repo wins", cost |
| [[src-pocock-feedback-loops-typescript]] | 2026-01-16 | tsc + Vitest + Husky pre-commit + lint-staged |
| [[src-pocock-ralph-plugin]] | 2026-01-22 | Smart/dumb zone, and why loops need a fresh context per iteration |
| [[src-pocock-afk-ralph-streaming]] | 2026-01-22 | Streaming AFK output with stream-json + jq |
| [[src-pocock-tracer-bullets]] | 2026-01-22 | Thin end-to-end slices against slop |
| [[src-pocock-tdd-skill]] | 2026-02-10 | Vertical red-green TDD for honest tests |
| [[src-pocock-git-guardrails-hook]] | 2026-02-10 | A `PreToolUse` hook that blocks destructive git; sandbox = where, not what |
| [[src-pocock-codebases-agents-love]] | 2026-02-26 | Deep, grey-box modules; the codebase beats the prompt |
| [[src-pocock-seven-phases]] | 2026-03-16 | The workflow around the execution loop |
| [[src-pocock-triage-skill]] | 2026-05-05 | A triage state machine ending in `ready-for-agent` |
| [[src-pocock-ai-coding-dictionary]] | 2026-09-24 | Vocabulary: software and dark factory, AFK, HITL, smart zone, check vs review, handoff, harness |

### Lauren Tan / pstack (ingested 2026-10-12)
| Source | Published | What it contributes |
|---|---|---|
| [[src-tan-how-i-use-cursor]] | 2026-05-25 | pstack launch. Verification is the bottleneck. Depth before breadth. Trust is the key to a factory. |
| [[src-tan-loops-you-can-trust]] | 2026-06-24 | Grove's limiting step. Earn trust. Stop-the-line maintenance automations. The 5-step ladder. |
| [[src-tan-complete-guide-pstack-pt1]] | 2026-08-31 | Verification skill: control CLI, Feature Map, cloud agents over worktrees |
| [[src-tan-pstack-guide-poteto-mode]] | repo | Routing to 23 playbooks. The five-part prompt. Restate first. |
| [[src-tan-pstack-guide-verify-and-ship]] | repo | Prove it works. Benchmark checklist. Babysit and Shipping playbooks. |
| [[src-tan-pstack-guide-overnight]] | repo | The overnight contract. Commit-or-discard iteration. Decision-log audit. Autopilot and Orchestrate. |
| [[src-tan-pstack-guide-principles]] | repo | The 24 principles as steering vocabulary |
| [[src-tan-pstack-guide-recipes]] | repo | Recipes and pitfalls, including "looping before you trust the loop" |
| [[src-tan-benny-automation]] | repo | Slack triage → repro → fix automations. Draft-only, fail closed. |
| [[src-tan-pstack-loop-principles]] | repo | Idempotency, never block on the human, prove it works, verifiable units, encode lessons, guard context |
| [[src-tan-x-short-posts]] | 2026-05 to 10 | Token cost, organic architecture, gardener, pstack slimming |

**Wanted:** see [[open-questions#Sources to find]].
