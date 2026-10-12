---
type: practice
branch: practice
tags: [loop-engineering, practice, memory, meta]
sources: ["[[src-karpathy-llm-wiki]]"]
created: 2026-10-11
updated: 2026-10-11
status: draft
---
# LLM Wiki pattern

The pattern this wiki is built on ([[src-karpathy-llm-wiki]]). An LLM incrementally builds and maintains a persistent, interlinked markdown wiki between you and your raw sources. *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."* Up: [[practice]].

## As a loop *(synthesis)*
| Anatomy slot | In the LLM Wiki |
|---|---|
| [[trigger]] | the human drops in a source or asks a question |
| [[context-and-state]] | `index.md` is read first, `log.md` gives recency, and the wiki itself is long-term memory |
| [[action]] | ingest: write a source summary and update 10–15 pages |
| [[verification]] | lint: contradictions, orphans, stale claims, missing pages |
| [[human-in-the-loop]] | the human curates sources and directs emphasis |

It is the [[context-and-state]] principle taken to its limit. Knowledge is *"compiled once and then kept current, not re-derived on every query"* ([[src-karpathy-llm-wiki]]).

## This wiki's implementation
`CLAUDE.md` (schema), `raw/` (immutable), `wiki/` (LLM-owned), `tools/wikilint.py` (mechanical lint).

## Related
[[andrej-karpathy]] · [[loop-engineering]]
