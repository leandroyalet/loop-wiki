---
type: pattern
branch: patterns
tags: [loop-engineering, pattern, maker-checker, verification]
sources: ["[[src-anthropic-building-effective-agents]]", "[[src-osmani-loop-engineering]]", "[[src-tns-loop-engineering]]", "[[src-pocock-ai-coding-dictionary]]", "[[src-tan-pstack-guide-overnight]]", "[[src-tan-pstack-guide-verify-and-ship]]", "[[src-tan-how-i-use-cursor]]", "[[src-inside-pstack-report]]", "[[src-agentos-docs]]", "[[src-openprose]]", "[[src-omp]]", "[[src-ouroboros]]", "[[src-osmani-claude-code-code-review]]", "[[src-anthropic-fold-subagents]]"]
created: 2026-10-11
updated: 2026-10-27
status: draft
---
# Evaluator–optimizer (maker / checker)

In the **evaluator-optimizer** pattern, *"one LLM call generates a response while another provides evaluation and feedback in a loop"* ([[src-anthropic-building-effective-agents]]). Loop-engineering sources call this the **maker/checker split** and treat it as the most important structural decision in a loop ([[src-osmani-loop-engineering]], [[src-tns-loop-engineering]]). Up: [[patterns]].

## When it fits
From [[src-anthropic-building-effective-agents]]:
- There are clear evaluation criteria, and iterating improves results measurably.
- A human's feedback would demonstrably improve the output, *and* an LLM can give that kind of feedback.

## Making the checker independent
- Give it different instructions, and sometimes a **different model** ([[src-osmani-loop-engineering]]).
- Check against **project skills and existing tests**, not just the maker's own claims ([[src-osmani-loop-engineering]]).
- Give it a **fresh context**. The authoring session *"reads its own conclusions back as confirmation"*, while a fresh reviewer *"sees the diff the way a stranger would"* ([[src-pocock-ai-coding-dictionary]]).
- **Scope** its system prompt to what you actually care about (security, API contracts, performance), not *"a vague 'look for problems'"* ([[src-pocock-ai-coding-dictionary]]).
- Use a **different model family**. Tan uses multi-model adversarial review (`/interrogate`), and her overnight audit reviewer is from another model family ([[src-tan-how-i-use-cursor]], [[src-tan-pstack-guide-overnight]]).
- Use **fresh verifier swarms**: *"no owner merges on its own verdict"*, and verification re-runs at every push that changes the patch ([[src-tan-pstack-guide-overnight]]). *"the agent that judges a change is never the one that wrote it"* ([[src-tan-pstack-guide-verify-and-ship]]).
- **Diversity from models, not personas.** In `/interrogate`, *"The adversarial signal comes from model diversity, not assigned personas."* A finding raised independently by two models is the strongest signal. Agreement across families is *"high-signal"* ([[src-inside-pstack-report]]).
- **A blind judge with a hidden rubric.** In `/arena`, N runners attempt one brief. A 3–6 criterion rubric is written for the picker only, and a judge from another family scores candidates by path label. Then the best parts of the losers are grafted onto the base. If the candidates *wildly diverge*, the brief was underspecified, so reframe it rather than average the results ([[src-inside-pstack-report]]).
- **A dedicated critic agent.** `comment-sicko` only reports and never writes code, because *"An author defends its comments the way you'd defend yours"* ([[src-inside-pstack-report]]).
- **The checker reports; it doesn't fix.** In [[openprose]] the checker *"assesses the supplied result and returns findings"*. *"Supplying the subject for assessment does not ask the checker to run it or rewrite the document"* ([[src-openprose]]).
- Treat it as a **filter, not a gate**. It is non-deterministic, so it misses things and flags non-issues ([[src-pocock-ai-coding-dictionary]]).
- Apply the same split to the stop decision: `/goal` uses a fresh model to judge completion. See [[goal-loop]].

## Worked example: propose ↔ review (AgentOS)
From [[src-agentos-docs]]. [[agentos]]'s `problem-solving` skill runs the pattern on *designs*, not code:
1. A **problem gate** runs before any proposal. `evaluate_problem` grades `pain.md` and, on fail, returns clarifying questions that the agent puts to the human.
2. A proposal agent writes `proposal.md`, including files, diff sketches, edge cases and a gate-test plan.
3. An adversarial reviewer returns *implement / revise / rethink*. Earlier rounds move to `_drafts/`.
4. The loop stops at **5 rounds**. Failing to converge is read as a bad *problem*, not a bad proposal, so the agent goes back to the human.
5. *"the reviewer starts fresh with no bias from proposal writing, which is the key property."* When the engine is down, the same loop runs with general-purpose subagents, and the reviewer is told to verify every claim against `file:line`.
6. A `closeout.md` records what actually shipped compared with the proposal, and it *"feeds into future proposals as prior-art references"*.

## A checker running alongside the agent (omp advisor)
From [[src-omp]]. [[omp]]'s advisor does not grade the finished output. It **reads every turn** of the primary agent, reasoning included, on its own model and context, and it has read-only tools by default.
- **Notes, not verdicts.** `nit` is an aside at the next boundary. `concern` may interrupt. `blocker` stops even partial work.
- **Its job:** *"Challenge premature 'done', thin verification, skipped reasoning"*, and block when the agent *"Yields before explicit convergence condition … is met"* or *"Substitutes stubs, TODOs, toys, or mocks"*.
- **Its limits:** *"Silence preferred when agent on track"*. *"NEVER police scope or ambition"*. It *"does not approve actions"* and is *"never a peer"*.
- **Noise control in code:** dedupe, a filler-phrase filter (`lgtm`, `done`), ≤4 non-blocker notes per update, and a 3-turn cooldown after an interrupting concern.
- **Model choice:** the advisor falls back to the `slow` role, *"not simply inherit[ing] the primary model"*.

*(synthesis)* This moves the checker from the end of the loop into the middle of it, closer to pair review than to a gate.

## The reviewer at scale: convergence (Claude Code team)
From [[src-osmani-claude-code-code-review]]. The [[claude-code]] team's PR reviewer is a production maker/checker loop, and it shows a failure the other sources don't: **the loop between an agent author and an agent reviewer may not converge.**
- **Finding pipeline.** Several agents hunt for bugs in parallel, a vote keeps only findings with enough support, and style, diagnostic and cleanup findings are filtered out (the filters were A/B-tested on internal PRs first). Survivors are ranked by severity and labelled *Important*, *Nit* or *Pre-existing*, so authors aren't blamed for bugs they didn't introduce.
- **Comments cost more when the author is an agent.** *"It only takes a second for a human to dismiss a nit, but when an agent has to address it, this results in another commit, and another cycle of review."*
- **The 50-cycle PR.** One CLI PR cycled more than fifty times overnight between agent author and agent reviewer until someone stopped it by hand. Blame showed ~59% of what the reviewer kept flagging was code from the PR's first pass: *"the review system was rarely finding new bugs, but finding a few more old ones on each cycle."* Running several review cycles by default had made it worse.
- **Convergence rules.** Ask the author to re-evaluate the *approach* after three cycles. After the first cycles, re-review only the new diff. Name the **class** of bug so the author fixes every instance, not one line. Don't re-report known issues. Track **cycles-to-pass** alongside recall.
- **Result (fig. E):** passing after one review-and-fix round rose from 65% to 78%, PRs needing five or more rounds fell from 8.9% to 1.5%, and mean reviews to pass fell from 2.08 to 1.32.
- **Stated priorities:** first, detect real bugs; second, reduce review cycles. Noise is measured from how authors resolve each comment and from runs on known-clean PRs.

*(synthesis)* This is the AgentOS 5-round cap ([[src-agentos-docs]]) and Ouroboros's oscillation detection ([[src-ouroboros]]) seen from the checker's side: a checker that drips findings one at a time keeps the loop open, so convergence is partly the checker's job.

## Where it sits in the loop
It is the agent-based half of [[verification]]. The other half is mechanical [[backpressure]].

## Contradictions & open questions
- **Model family or context?** pstack makes cross-family judges mandatory ([[src-inside-pstack-report]]). Pocock grounds the checker's independence in **fresh context** alone ([[src-pocock-ai-coding-dictionary]]). Claude Code ports of pstack keep only context separation and accept that loss ([[src-inside-pstack-report]]). No source measures how much the model family adds on top of fresh context. AgentOS sides with fresh context: its reviewer's *"key property"* is starting *"with no bias from proposal writing"* ([[src-agentos-docs]]). Ouroboros adds a warning about audits: *"Three votes labeled `default` are not three independent reviewers."* Its consensus stage filters out reviewers from the executor's vendor where it can, and *"Separate calls or model labels are not, by themselves, evidence of separate models, vendors, or backends"* ([[src-ouroboros]]). See [[open-questions]].
- **Must the checker be a separate agent?** OpenProse treats executor and evaluator as roles that *"can share an agent unless the contract requires independence"*. When a contract does require it, *"an independent-review requirement calls for actual separation"* ([[src-openprose]]). That makes independence a per-contract requirement. pstack makes it a rule: the judge is *never* the author ([[src-tan-pstack-guide-verify-and-ship]]).
- **Filter or gate?** Pocock calls automated review *"a filter … not a gate"* ([[src-pocock-ai-coding-dictionary]]). The Claude Code team makes every AI finding block the merge until it is fixed or resolved with a reason, and lets automated review alone clear a low-risk change ([[src-osmani-claude-code-code-review]]). See [[layered-code-review]].
- **Gate or shadow?** omp lets the doer grade its own `/goal` completion and adds independence only through the concurrent advisor ([[src-omp]]). Osmani's `/goal` puts the separate model at the stop gate itself ([[src-osmani-loop-engineering]]). See [[goal-loop]].
- **Is the checker optional?** Anthropic's single-loop design makes a goal or verifier check after the answer *optional*, and counts black-box verification among the few good reasons to keep a subagent ([[src-anthropic-fold-subagents]]). Loop engineering sources treat the separate checker as the condition for walking away ([[src-osmani-loop-engineering]]). *(synthesis)* The difference tracks interactive agents (a user in the conversation) vs unattended loops. See [[folding-subagents]].

## Related
[[orchestrator-workers]] · [[budgets-and-cost]]
