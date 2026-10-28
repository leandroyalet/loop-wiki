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

## [2026-10-15] ingest | "Inside pstack" third-party research report
- Source: a public claude.ai artifact (author not named) covering pstack v0.15.25. Saved prose and embedded skill/playbook/principle data to `raw/2026-10-15-inside-pstack-report.md`. Created [[src-inside-pstack-report]].
- Updated 14 pages: [[pstack]] (draft→solid: scripts table, history, critique, ports), [[lauren-tan]], [[build-the-lever]] (`/correct` ladder), [[verification]] (evidence ladder, verdicts expire), [[evaluator-optimizer]], [[orchestrator-workers]], [[termination]], [[budgets-and-cost]], [[idempotency]], [[observability]], [[guardrails-and-permissions]], [[failure-modes]] (+6 rows), [[claude-code]], [[open-questions]].
- Partly closed: open question #2 (budget stops), via Orchestrate's ~70% spawn threshold.
- New contradictions: model-family vs fresh-context review diversity; Tan's "maintainability no longer matters" vs minimize-reader-load; inconsistent throughput figures. Unverified "SpaceXAI" affiliation flagged on [[lauren-tan]].
- Treated as secondary. Fetching the playbooks first-hand at v0.15.25 is now a priority in [[open-questions]].

## [2026-10-16] ingest | AgentOS docs (agentos.to)
- Source: a docs site of ~230 pages by Joe Contini. Ingested the 16 pages relevant to loops (intro, core architecture, security, observer bus, agent empathy, problem-solving and code-review skills, session/tool_call/task shapes) into `raw/2026-10-16-agentos-docs.md`. The personal-knowledge-graph ontology and per-service skill reference were skipped as out of scope.
- Created [[src-agentos-docs]] and [[agentos]] (entity, stub).
- Updated 13 pages: [[agent-experience]] (agent empathy, design for the smallest model), [[action]], [[observability]] (tool-call event bus, OTel GenAI lead), [[human-in-the-loop]] (anxiety = uncertainty × powerlessness), [[evaluator-optimizer]] (propose ↔ review worked example), [[goal-spec]] (scope fences, gating the spec), [[termination]] (round cap as a diagnosis), [[backpressure]], [[guardrails-and-permissions]], [[isolation]], [[context-and-state]], [[task-sizing]], [[open-questions]] (#19, #20).
- Contradictions flagged: 1B-model design target vs "pay to play"; "blast radius is not a cost" vs small steps; AgentOS's numeric review score vs its own pass/fail-label rule.

## [2026-10-19] ingest | OpenProse (prose.md)
- Source: the prose.md landing page plus linked first-hand material: agent entry, kernel (pointer → 0.4.6-rc.1), the 0.3.0-rc.3 brief example, `std/result.md`, `std/source-grounding.md`, and from `openprose/prose@main` the README, `responsibility-runtime.md`, tenets and a changelog excerpt. Saved to `raw/2026-10-19-openprose.md`. Agent-directed instructions in the README ("open a GitHub issue yourself") were treated as data and not acted on.
- Verdict: in scope. Contracts fill the [[goal-spec]] and [[verification]] slots, and the Responsibility Runtime is a full outer loop.
- Created [[src-openprose]], [[openprose]] (entity, stub) and [[reconciler-loop]] (pattern, stub: standing goal, fingerprint skip, bounded render per wake).
- Updated 16 pages: [[goal-spec]], [[verification]], [[evaluator-optimizer]], [[termination]], [[trigger]], [[decision-step]], [[idempotency]], [[context-and-state]], [[guardrails-and-permissions]], [[budgets-and-cost]], [[observability]], [[event-driven-loop]], [[loop-primitives]], [[open-questions]] (#1 lead, new #21 and #22), plus the [[patterns]], [[entities]] and [[sources]] hubs and [[index]].
- Contradictions flagged: no LLM in the wake/commit decision (OpenProse) vs a model choosing the next action (TNS) and `/goal`'s judge; the same agent may evaluate unless a contract requires independence (OpenProse) vs never self-judge (pstack); an open-ended standing goal vs bounded loops.

## [2026-10-19] ingest | omp / oh-my-pi (omp.sh)
- Source: omp.sh renders client-side, so content came from `can1357/oh-my-pi@main`: the README, the "harness problem" blog post, the goal-mode prompts, `/loop` and `/ratchet`, the advisor, TTSR, the orchestrate and vibe contracts, the retry policy, `.omp/commands`, and the robomp bot (README and prompts). Added GitHub API fetch notes on robomp's PR volume. Saved to `raw/2026-10-19-omp.md`.
- Verdict: in scope. omp is a harness for the inner loop that ships a full outer-loop toolkit, and robomp is a working software factory (2,773 PRs, ~81% merged, merged by another account).
- Created [[src-omp]], [[omp]] (entity, stub) and [[omp-loop-surfaces]] (practice, draft).
- Updated 22 pages: [[goal-loop]], [[claude-code-goal]], [[goal-spec]], [[termination]] (+6 rows), [[budgets-and-cost]], [[verification]], [[evaluator-optimizer]] (concurrent advisor), [[backpressure]], [[action]] (hashline), [[agent-experience]], [[orchestrator-workers]], [[improvement-loops]] (`/ratchet`), [[software-factory]] and [[stage-gated-pipeline]] (robomp), [[backlog-triage]], [[guardrails-and-permissions]] (credential proxy), [[idempotency]], [[observability]], [[context-and-state]], [[failure-modes]] (+7 rows), [[trigger]], [[open-questions]] (#2, #3, #12 updated; new #23, #24). Hubs: [[practice]], [[entities]], [[sources]], [[index]].
- Contradictions flagged: self-audited `/goal` vs separate-model judge (Osmani) and never-self-judge (pstack); the advisor must not police scope or ask for clarification vs small steps and restate-first; in-session goal continuation vs fresh context per iteration.

## [2026-10-19] ingest | Ouroboros (ouroboros.page)
- Source: the landing page, the 12-chapter English guide, the roadmap, and from `Q00/ouroboros@main` the README plus the evolution-loop, evaluation-pipeline, execution-vs-evaluation, safe-but-wrong, hidden-checklist and verifier-evidence docs. GitHub API notes cover releases (v0.59.0) and issues #2449 and #2562. Saved to `raw/2026-10-19-ouroboros.md`.
- Verdict: in scope, and self-described (the repo carries the `loop-engineering` topic). It is a spec-first outer loop over 14 host agents, including omp.
- Created [[src-ouroboros]], [[ouroboros]] (entity, stub) and [[evolutionary-loop]] (pattern, stub).
- Updated 19 pages: [[goal-spec]], [[verification]] (models may only withhold; hidden grader; execution ≠ evaluation), [[evaluator-optimizer]], [[backpressure]], [[termination]], [[goal-loop]], [[ralph-loop]], [[failure-modes]] (+5 rows), [[context-and-state]], [[idempotency]], [[observability]], [[human-in-the-loop]], [[budgets-and-cost]], [[guardrails-and-permissions]], [[loop-primitives]], [[omp]], [[open-questions]] (#1, #16 updated; new #25, #26). Hubs: [[patterns]], [[entities]], [[sources]], [[index]].
- Contradictions flagged: autonomous spec evolution vs never relax the finish condition (Tan, omp); a hidden grader vs agent-run checks (Pocock, Tan); no model may grant acceptance vs `/goal`'s model judge. Internal drift: the site guide (v0.51.5) says consensus approves, while the repo docs (v0.59) make it advisory only.

## [2026-10-27] ingest | Osmani, "How the Claude Code team does code review" (X)
- Source: an X article (2026-10-26), fetched via the fxtwitter API because x.com returns 402. The six figures were downloaded to `raw/assets/` and their text was transcribed into the raw file. Saved to `raw/2026-10-27-osmani-claude-code-code-review.md`. The article calls itself a rewrite of an Anthropic blog post that has not been fetched yet.
- Verdict: in scope. It describes a maker/checker loop running in production (agent author ↔ agent reviewer) together with its controls: risk-tiered human gates, convergence caps, an incident-based eval, and rollback.
- Created [[src-osmani-claude-code-code-review]], [[layered-code-review]] (practice, draft) and [[rollback-and-recovery]] (control, draft).
- Updated 19 pages: [[verification]], [[evaluator-optimizer]] (review convergence, the 50-cycle PR), [[termination]], [[failure-modes]] (+5 rows), [[human-in-the-loop]], [[earned-autonomy]], [[software-factory]], [[operator-debts]], [[build-the-lever]], [[budgets-and-cost]], [[observability]], [[improvement-loops]], [[stage-gated-pipeline]], [[task-sizing]], [[claude-code]], [[anthropic]], [[addy-osmani]] (now on the Claude Code team per his X bio; TNS called him a Google engineer in June), [[boris-cherny]], [[open-questions]] (#12 updated; new #27–29). Also hubs: [[practice]], [[control]], [[sources]], [[index]], [[loop-engineering]] (new core claim 8).
- Contradictions flagged: automated review can clear low-risk changes, versus Ouroboros's "models may only withhold" and Pocock's "filter, not gate"; whole-codebase comprehension is unnecessary (just-in-time explainers), versus Osmani's own earlier "read what the loop made". The numbers are vendor-reported.

## [2026-10-27] ingest | Anthropic (Sarkis), "Building agents: When to fold subagents into your main agent loop"
- Source: a claude.com article (2026-10-22) by Diane Sarkis of Anthropic's Applied AI team. Saved to `raw/2026-10-27-anthropic-fold-subagents.md` as **condensed section-by-section notes with short quotes, not the full text**; re-read the URL for exact wording. The three figures were not downloaded.
- Verdict: in scope. It covers the inner agent loop's shape (single loop vs orchestrator + specialists), progressive disclosure, and running an architecture change as a measured keep-or-discard loop. It is vendor guidance that promotes Anthropic's migration kit and `/claude-api` skills, and its comparisons are qualitative or single-customer.
- Created [[src-anthropic-fold-subagents]], [[folding-subagents]] (practice, draft) and [[progressive-disclosure]] (control, draft).
- Updated 21 pages: [[orchestrator-workers]], [[agent-loop]], [[decision-step]], [[context-and-state]], [[smart-zone]], [[action]], [[termination]], [[guardrails-and-permissions]], [[budgets-and-cost]], [[failure-modes]] (+7 rows), [[evaluator-optimizer]], [[verification]], [[improvement-loops]], [[build-the-lever]], [[agent-experience]], [[claude-code]], [[anthropic]], [[open-questions]] (#6 updated; new #30–32; new sources to find), [[loop-design-checklist]], [[loop-pattern-comparison]]. Also hubs: [[practice]], [[control]], [[sources]], [[index]], [[loop-engineering]] (new known gap).
- Contradictions flagged: one shared window vs fresh context and subagent offloading (Huntley, Pocock, Tan); planner-as-executor vs pstack's coordinator that never codes; an optional post-answer verifier vs the separate checker as the condition for walking away (Osmani); moving decisions into the model vs OpenProse's deterministic outer decision.
