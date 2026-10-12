---
type: practice
branch: practice
tags: [loop-engineering, practice, afk, overnight]
sources: ["[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-recipes]]", "[[src-tan-pstack-guide-poteto-mode]]", "[[src-pocock-getting-started-with-ralph]]"]
created: 2026-10-12
updated: 2026-10-12
status: draft
---
# The overnight contract

What to hand a loop before you walk away. Tan: *"A good handoff has the goal, the finish condition, permissions, and an escape hatch. It doesn't need to be long"* ([[src-tan-pstack-guide-overnight]]). Up: [[practice]].

## The four parts
```text
/poteto-mode im going to bed. migrate every caller to the new parser in a fresh worktree off <base>.
done means zero old callers, all parser fixtures pass, old api deleted.
keep a decision log. don't ask me before committing.
/loop until done. if you're truly stuck after a few hours, stop and write up why.
```

| Part | In the example | Anatomy slot | Why |
|---|---|---|---|
| **Goal** and session override | "im going to bed … migrate every caller" | [[goal-spec]] | The agent stops asking and keeps going. |
| **Finish condition** | "done means zero old callers, all fixtures pass, old api deleted" | [[goal-spec]], [[termination]] | *"turns the goal into checks every iteration can run"* |
| **Isolation** | "fresh worktree off `<base>`" | [[isolation]] | no collisions with your other work |
| **Permissions** | "don't ask me before committing" | [[guardrails-and-permissions]] | pre-answers the question it would otherwise block on |
| **Audit trail** | "keep a decision log" | [[observability]] | a morning audit of decisions, not the transcript |
| **Escape hatch** | "if you're truly stuck after a few hours, stop and write up why" | [[termination]] | *"beats eight hours of creative goal reinterpretation"* |

Source: [[src-tan-pstack-guide-overnight]].

## What each iteration does
1. Check the finish condition.
2. Make the smallest justified change.
3. Verify it against the real artifact.
4. **Commit** if it made progress, **discard** it if not.
5. Log one decision row.

*"A plateau means pivot, not stop, and the finish condition never quietly relaxes to declare victory"* ([[src-tan-pstack-guide-overnight]]).

## Pitfalls
- **A duration is not a finish condition.** *"'work on this for 4 hours' gives the agent nothing to check"* ([[src-tan-pstack-guide-overnight]]).
- A vague finish condition such as "make it better" ([[src-tan-pstack-guide-recipes]]).
- Looping before the loop has earned trust. See [[earned-autonomy]].

## In the morning
`/show-me-your-work catch me up on what you did last night`. A reviewer from a different model family reads the decision log and the transcript. Read the **Attention** section first ([[src-tan-pstack-guide-overnight]]). See [[observability]].

## Compared with Pocock's AFK Ralph *(synthesis)*
| | Tan's overnight contract | Pocock's `afk-ralph.sh` ([[src-pocock-getting-started-with-ralph]]) |
|---|---|---|
| Repetition | Cursor `/loop` (events or heartbeat), in-session | a bash `for` loop, a fresh process per iteration |
| Stop | finish-condition predicate, plus an escape-hatch write-up | `<promise>COMPLETE</promise>` sigil, plus an iteration cap |
| Non-progress | discard the change and pivot | not specified. The next iteration picks a task. |
| Audit | decision-log TSV plus a cross-model reviewer | `progress.txt` plus git log |

## Related
[[afk]] · [[building-a-ralph-loop]] · [[writing-a-loop-prompt]]
