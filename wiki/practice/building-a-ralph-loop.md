---
type: practice
branch: practice
tags: [loop-engineering, practice, ralph, how-to]
sources: ["[[src-pocock-getting-started-with-ralph]]", "[[src-pocock-ralph-tips]]", "[[src-pocock-afk-ralph-streaming]]", "[[src-pocock-ralph-plugin]]", "[[src-pocock-git-guardrails-hook]]", "[[src-huntley-ralph]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# Building a Ralph loop (Pocock's recipe)

A concrete, current recipe for a [[ralph-loop]], mostly from [[matt-pocock]]. Huntley's original is a bare `while :` loop ([[src-huntley-ralph]]). Pocock's version adds a cap, a completion sigil, a sandbox, streaming and guardrails. Up: [[practice]].

## 1. State files
- `PRD.md` or `prd.json` defines the **end state**. Write it in plan mode. JSON items with `passes: false` make the PRD both scope and tracker ([[src-pocock-ralph-tips]]). See [[goal-spec]].
- `progress.txt` holds tasks, decisions, blockers and files changed. It is committed, and deleted after the sprint ([[src-pocock-ralph-tips]]). See [[context-and-state]].

## 2. HITL first: `ralph-once.sh`
`claude --permission-mode acceptEdits "@PRD.md @progress.txt …find the next incomplete task… commit… update progress.txt… ONLY DO ONE TASK AT A TIME."` Run it, watch it, run it again ([[src-pocock-getting-started-with-ralph]]).

## 3. AFK: `afk-ralph.sh <iterations>`
From [[src-pocock-getting-started-with-ralph]]:
- `for ((i=1; i<=$1; i++))` with `set -e`. **The iteration cap is mandatory**: 5–10 for small jobs, 30–50 for large ones ([[src-pocock-ralph-tips]]).
- `docker sandbox run claude --permission-mode acceptEdits -p "<prompt>"`
- The prompt says: pick the highest-priority task, run tests and type checks, update the PRD and progress, commit, *"ONLY WORK ON A SINGLE TASK"*, and output `<promise>COMPLETE</promise>` if the PRD is complete.
- The script checks the result for the sigil and exits early. See [[termination]].

## 4. See what it's doing
`--print` shows a blank screen. Use `--verbose --output-format stream-json | grep --line-buffered '^{' | tee $tmp | jq` to stream assistant text, then read the final `result` from `$tmp` to check for the sigil ([[src-pocock-afk-ralph-streaming]]). Add a notification when it ends (Pocock uses WhatsApp, [[src-pocock-ralph-tips]]). See [[observability]].

## 5. Safety
- A **Docker sandbox** isolates *where* the agent acts ([[src-pocock-ralph-tips]]). See [[isolation]].
- A **`PreToolUse` git hook** restricts *what* it does: it blocks `push`, `reset --hard`, `clean -f` and `branch -D` ([[src-pocock-git-guardrails-hook]]). See [[guardrails-and-permissions]].

## 6. Keep it a bash loop
Run **one process per iteration**, so each iteration starts with a fresh context window. Pocock rejects Anthropic's in-session Ralph plugin because it accumulates context into the dumb zone ([[src-pocock-ralph-plugin]]). See [[smart-zone]].

## 7. Prompt add-ons
Feedback-loop gate (*"Do NOT commit if any feedback loop fails"*), step size, risk-first prioritisation, quality bar, and tracer bullets ([[src-pocock-ralph-tips]], [[src-pocock-tracer-bullets]]). See [[writing-a-loop-prompt]] and [[task-sizing]].

## Related
[[afk]] · [[improvement-loops]] · [[claude-code-loop]]
