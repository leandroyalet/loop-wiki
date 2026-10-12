---
type: source
branch: sources
tags: [loop-engineering, meta, memory]
sources: []
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
author: Andrej Karpathy
published: unknown
raw: raw/2026-10-11-karpathy-llm-wiki.md
created: 2026-10-11
updated: 2026-10-11
status: solid
---
# Karpathy — "LLM Wiki" (gist)

**Author:** [[andrej-karpathy]] · **Raw:** `raw/2026-10-11-karpathy-llm-wiki.md` · Up: [[sources]]

## Summary
An "idea file" describing the pattern this wiki is built on. An LLM incrementally builds and maintains a persistent, interlinked markdown wiki that sits between the human and the raw sources. *"The knowledge is compiled once and then kept current, not re-derived on every query."* It is only tangentially about agent loops. It is ingested here because it is the schema's origin, and because it is a worked example of **persistent external memory**, which every long-running loop needs. See [[llm-wiki-pattern]].

## Key claims
- There are three layers: immutable raw sources, an LLM-owned wiki, and a schema file (`CLAUDE.md` / `AGENTS.md`).
- There are three operations: **ingest**, **query** (file good answers back as pages), and **lint** (contradictions, orphans, stale claims).
- `index.md` is a catalogue and `log.md` is an append-only timeline. The index is enough to navigate a wiki of about 100 sources without RAG.
- *"Humans abandon wikis because the maintenance burden grows faster than the value."* LLMs make maintenance close to free.
- (synthesis) Ingest/lint is itself a small loop: a human-triggered [[agent-loop]] that writes durable state ([[context-and-state]]) and runs a periodic self-check ([[verification]]).

## Pages touched
[[llm-wiki-pattern]], [[context-and-state]], [[andrej-karpathy]]
