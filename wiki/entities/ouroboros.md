---
type: entity
branch: entities
tags: [loop-engineering, product, open-source, spec-first, evaluation]
sources: ["[[src-ouroboros]]"]
created: 2026-10-19
updated: 2026-10-19
status: stub
---
# Ouroboros

**Ouroboros** (`ouroboros.page`, GitHub `Q00/ouroboros`, Ouro Labs) is an MIT-licensed, local-first, spec-first management layer for AI coding work. It is a Python core that exposes an MCP server and `ooo` skills inside 14 host agents, including Claude Code, Codex CLI, OpenCode, Kiro, Gemini, Pi and [[omp]]. It doesn't write code: *"Your coding agent writes the code. Ouroboros verifies the result."* Its GitHub repo carries the `loop-engineering` topic ([[src-ouroboros]]). Up: [[entities]].

## The workflow
| Command | Step | Anatomy slot |
|---|---|---|
| `ooo interview` | Socratic questions until the ambiguity score is ≤ 0.2 | [[goal-spec]] |
| `ooo seed` | an immutable YAML spec, graded A/B/C | [[goal-spec]] |
| `ooo run` | hands off to the runtime: Discover → Define → Design → Deliver | [[action]] |
| `ooo evaluate` | Mechanical (the only stage that can grant) → Semantic → Consensus (both can only withhold) | [[verification]] |
| `ooo evolve` / `ooo ralph` | Wonder → Reflect → next-generation Seed, until convergence, stagnation, oscillation or the 30-generation cap | [[evolutionary-loop]], [[termination]] |
| `ooo auto` | interview → grade-A Seed → run, with bounded loops and a resume ID | [[goal-loop]] |
| `ooo unstuck` | 5 lateral-thinking personas when the same failure repeats | [[failure-modes]] |
| `ooo publish` | Seed → GitHub issues for a team | [[backlog-triage]] |

All from [[src-ouroboros]].

## Distinctive design choices *(synthesis)*
- **Graders hidden from the doer.** Verify commands and assertions never reach workers. See [[verification]].
- **No model can grant acceptance.** Only executed mechanical checks can.
- **The spec is versioned, not fixed.** It is immutable within a run and evolved across generations as a *lineage*.

## Contradictions & open questions
- Its site guide (v0.51.5) and repo docs (v0.59) disagree on whether consensus can approve ([[src-ouroboros]]).
- It calls itself an "Agent OS", which has nothing to do with [[agentos]].
- There is no published field evidence. Its roadmap gates expansion on a pilot that hasn't happened yet ([[src-ouroboros]]).

## Related
[[omp]] · [[openprose]] · [[claude-code]] · [[openai-codex]]
