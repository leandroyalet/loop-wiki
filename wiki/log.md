# Log

Append-only. Recent entries: `grep "^## \[" wiki/log.md | tail -5`

## [2026-10-11] scaffold | Wiki structure and schema
- Created `CLAUDE.md` (schema), `raw/`, `wiki/` with 7 branch folders, `.obsidian/app.json`, `tools/wikilint.py`.
- Root concept: [[loop-engineering]]. Scope: AI agent loops only.

## [2026-10-11] ingest | Karpathy — LLM Wiki
- Created [[src-karpathy-llm-wiki]], [[llm-wiki-pattern]], [[andrej-karpathy]].

## [2026-10-11] ingest | Osmani — Loop Engineering
- Created [[src-osmani-loop-engineering]], [[loop-primitives]], [[operator-debts]], [[addy-osmani]], [[peter-steinberger]], [[boris-cherny]], [[openai-codex]], [[claude-code]].
- Seeded [[context-and-state]], [[verification]], [[scheduled-loop]], [[goal-loop]], [[isolation]], [[evaluator-optimizer]].

## [2026-10-11] ingest | Anthropic — Building Effective AI Agents
- Created [[src-anthropic-building-effective-agents]], [[agent-loop]], [[orchestrator-workers]], [[anthropic]].
- Updated [[observation]], [[action]], [[termination]], [[evaluator-optimizer]], [[guardrails-and-permissions]], [[human-in-the-loop]].

## [2026-10-11] ingest | Huntley — Ralph
- Created [[src-huntley-ralph]], [[ralph-loop]], [[backpressure]], [[writing-a-loop-prompt]], [[geoffrey-huntley]].
- Updated [[context-and-state]], [[failure-modes]], [[orchestrator-workers]], [[goal-spec]], [[operator-debts]].
- Contradictions flagged: monolithic vs multi-agent; greenfield-only vs daily loops on existing repos; maintainability "by whom?" vs comprehension debt.

## [2026-10-11] ingest | Claude Code docs — Run prompts on a schedule
- Created [[src-claude-code-scheduled-tasks]], [[claude-code-loop]], [[claude-code-scheduling]], [[self-paced-loop]], [[event-driven-loop]], [[babysitter-loop]].
- Updated [[trigger]], [[termination]], [[guardrails-and-permissions]], [[observability]].

## [2026-10-11] ingest | The New Stack — loop engineering
- Created [[src-tns-loop-engineering]], [[loop-vs-prompt-engineering]].
- Updated [[decision-step]] with the cron-vs-loop distinction, [[loop-primitives]] (five vs six), [[budgets-and-cost]], [[claude-code-goal]].
- Not ingested: dassum (Medium) returned 403. Logged in [[open-questions]].

## [2026-10-11] query | Syntheses from the seed set
- Created [[loop-pattern-comparison]], [[loop-design-checklist]], [[open-questions]].

## [2026-10-11] lint | First pass
- `tools/wikilint.py`: 59 pages, 0 problems. Lint self-test confirmed it flags broken links, orphans, unindexed pages and bad frontmatter.
- Provenance check: every non-hub page cites at least one existing `src-*` page.
- Semantic gaps carried to [[open-questions]]: idempotency, budget-based stops, `/goal` limits, observability, first-party Codex docs.

## [2026-10-12] ingest | Matt Pocock / AI Hero (12 sources)
- Found via the aihero.dev sitemap (196 URLs). Selected the 11 articles about loops plus the AI Coding Dictionary (index + 9 entries). Skipped AI SDK/MCP tutorials and per-skill pages.
- Created 12 `src-pocock-*` pages, plus [[matt-pocock]], [[software-factory]], [[afk]], [[improvement-loops]], [[smart-zone]], [[agent-experience]], [[building-a-ralph-loop]], [[task-sizing]], [[seven-phases-of-ai-development]], [[backlog-triage]].
- Updated 30+ pages, including [[loop-engineering]], every anatomy page, [[ralph-loop]], [[human-in-the-loop]], [[verification]], [[backpressure]], [[guardrails-and-permissions]] (stub→draft), [[failure-modes]] (+12 rows), [[observability]] and [[loop-design-checklist]].
- Contradictions flagged:
  - in-session vs fresh-context loops (may affect `/loop` and `/goal`)
  - dumb-zone threshold: 40% vs 125–150K tokens
  - "backpressure" terminology
  - Huntley's greenfield-only vs Pocock on existing repos
  - dark-factory acceptability
- Raised in priority: Anthropic's "Effective harnesses for long-running agents", now cited by two sources.

## [2026-10-12] ingest | Lauren Tan / pstack (11 sources)
- Found via the GitHub API (`cursor/plugins/pstack` @ 997ffc7fe26b) and api.fxtwitter.com (X articles). The no.lol blog (2014–2020) was skipped as off-topic.
- Created 11 `src-tan-*` pages, plus [[lauren-tan]], [[pstack]], [[cursor]], [[earned-autonomy]], [[idempotency]], [[stage-gated-pipeline]], [[overnight-contract]], [[verification-skill]], [[build-the-lever]].
- Updated ~35 pages. Big changes: [[verification]] (limiting step, proof not claims), [[termination]], [[human-in-the-loop]] (never block on the human), [[event-driven-loop]] (stub→draft, worked example), [[failure-modes]] (+8 rows), [[isolation]], [[loop-design-checklist]] and [[open-questions]].
- Gap closed (partly): idempotency (open question #4).
- Contradictions flagged:
  - human merge gate (Autopilot-full vs Pocock and Osmani)
  - dark factory as goal vs hazard
  - worktrees vs cloud agents
  - cap vs pivot
  - ask vs proceed (Anthropic / Pocock / Tan)
  - in-session lean loop vs fresh process
  - source bias (Cursor employee, self-reported throughput)
