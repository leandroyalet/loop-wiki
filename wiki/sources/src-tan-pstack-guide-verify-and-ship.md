---
type: source
branch: sources
tags: [loop-engineering, tan, pstack, verification, guide]
sources: []
url: https://github.com/cursor/plugins/blob/997ffc7fe26b/pstack/docs/guide/06-verify-and-ship.md
author: Lauren Tan
published: unknown (repo HEAD 2026-10-12)
raw: raw/2026-10-12-tan-pstack-guide-verify-and-ship.md
created: 2026-10-12
updated: 2026-10-12
status: solid
---
# pstack guide 6 — "Verify the result and open a PR"

**Author:** [[lauren-tan]] · **Raw:** `raw/2026-10-12-tan-pstack-guide-verify-and-ship.md` · Up: [[sources]]

## Summary
*"'It compiles' is not evidence."* *"Verification is the slowest step in most agent work, because it's the step that usually waits on a human. Make the agent able to do it, and you stop being the bottleneck. Skip it, and running more agents only gets you more unchecked work to review."*

## Key claims
- **State the finish condition up front** as checks that can run. *"treat a confident reply without evidence as a red flag."* An inconclusive check should be *reported* as inconclusive. See [[goal-spec]].
- **Match the check to the change:**
  - a CLI change runs the real command
  - a UI change walks the flow, or diffs against a frozen visual baseline
  - a parser replays saved input
  - a perf change compares profiles
  - a storage change reads the value back

  See [[verification]].
- **`/benchmark-checklist`** asks seven questions before you trust a number: limiter, tuned like production, physical limits, errors, reproducible median and range, end-to-end relevance, and whether the work actually happened in the timed region. The verdicts are faster, slower, no difference, or inconclusive. See [[failure-modes]].
- **The verification skill:** `/create-verification-skill` interviews the *repository*, not you, and writes Launch, Doctor, Drive, Evidence and Cleanup sections plus a Feature Map. It must prove itself once end to end before you use it. `/maintain-verification-skill` runs daily from an automation and ends in `clean`, `changed` (one PR, confined to the skill) or `blocked`. It never edits product code. See [[verification-skill]].
- **Build the lever:** a small control CLI instead of throwaway click scripts. Also make the dev setup repeatable. See [[build-the-lever]].
- **The Babysit playbook:** handle conflicts, then review threads, then CI. Batch fixes into one push. Triage comments skeptically and post the disproof on threads you dismiss. **It stops at merge-ready and never merges**, *"because merging is a different decision."* See [[babysitter-loop]].
- **The Shipping playbook:** one fresh agent per PR verifies live, and *"the agent that judges a change is never the one that wrote it."* It lands only the contiguous verified run from the bottom of the stack. See [[evaluator-optimizer]].
- *"Five narrow PRs beat one fat one."* See [[task-sizing]].

## Pages touched
[[verification]], [[verification-skill]], [[goal-spec]], [[babysitter-loop]], [[evaluator-optimizer]], [[build-the-lever]], [[failure-modes]], [[task-sizing]], [[scheduled-loop]]
