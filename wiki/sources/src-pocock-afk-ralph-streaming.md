---
type: source
branch: sources
tags: [loop-engineering, pocock, ralph, observability]
sources: []
url: https://www.aihero.dev/heres-how-to-stream-claude-code-with-afk-ralph
author: Matt Pocock
published: 2026-01-22
raw: raw/2026-10-12-pocock-afk-ralph-streaming.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# Pocock — "Here's How To Stream Claude Code With AFK Ralph" (2026-01-22)

**Author:** [[matt-pocock]] · **Raw:** `raw/2026-10-12-pocock-afk-ralph-streaming.md` · Up: [[sources]]

## Summary
AFK Ralph in `--print` mode shows **a blank screen**: *"Is Claude working? Is it stuck?"* The fix is `--output-format stream-json --verbose`, piped through `grep --line-buffered '^{'` (to drop non-JSON noise) and `tee` (to keep a temp file), then `jq` to print only assistant text live. The final `result` is read back from the temp file to check for `<promise>COMPLETE</promise>`.

## Key claims
- You want both *"real-time visibility … but you also want to leave it running."* See [[observability]].
- The jq filter selects `type == "assistant"` text blocks and fixes line endings (`\n` → `\r\n`).
- At the time of writing, OpenCode streams natively. Pocock hopes Claude Code will ship this so the article can be deleted.

## Pages touched
[[observability]], [[building-a-ralph-loop]], [[afk]]
