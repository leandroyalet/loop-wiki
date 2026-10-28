---
title: "Ouroboros (ouroboros.page): site, English guide, README, and evaluation/evolution design docs"
url: https://ouroboros.page/
author: Ouro Labs (GitHub Q00 / Q00/ouroboros; top committers Q00, shaun0927)
published: unknown (repo created 2026-01-14; latest release v0.59.0 2026-10-19; site guide "verified 2026-08-14" against v0.51.5)
fetched: 2026-10-19
extraction: "Landing page HTML stripped to text. English guide (ouroboros.page/learn/en/, 12 chapters) extracted from <main>. Verbatim from github.com/Q00/ouroboros@main: README.md; docs/guides/evolution-loop.md, execution-vs-evaluation.md, safe-but-wrong-output.md; docs/hidden-checklist-convergence/requirements.md and architecture.md; excerpts of docs/guides/evaluation-pipeline.md (acceptance authority, Stage 2, Stage 3 simple consensus) and docs/contributing/verifier-evidence-policy.md (core rule, failure classes). Roadmap page text. Fetch notes = GitHub API observations. Not ingested: ko/zh guides, docs/agentos/*, active-conductor, auto-live-kanban, cli/config references, plugins and ourocode repos, roadmap PDF."
---

> Raw source. Immutable; do not edit. Summary lives in the wiki under sources/.


---
<!-- page: https://ouroboros.page/ (landing page) -->

Ouroboros — spec, run, verify AI coding work

Skip to content

Ouroboros

Guide
Roadmap
한국어
中文
GitHub
Theme

OPEN SOURCE · MIT

Your coding agent writes the code.
Ouroboros verifies the result.

Ouroboros manages the requirements, execution, evaluation, and records of AI coding work. It pins the spec before the run and verifies the result after it.

Install
Read the guide

Claude CodeCodex CLIGitHub Copilot CLIOpenCodeHermesGeminiKiro CLIPi CLIZcodeGooseGJCAntigravity CLIGrok Build CLI

Four separate runs, four hosts. Different tasks on purpose — the engine is what is shared, not the prompt.

Terminal CLI — a task-management CLI: ouroboros init start asking about ordering and scope, then reporting an ambiguity score
ChatGPT (Codex) — called as an integration, on a video-publishing harness: the interview, its advisory lanes, and the ambiguity ledger
Claude Code — a YouTube automation task, with the six advisory lanes running in parallel before the interview submits
Hermes (Discord) — a kart-racing game, run as a chat bot, ending at Final ambiguity: 0.15

Install

Run in your terminal:

zsh

claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros

Requires Claude Code. No Python needed. Prefer a standalone CLI? pip install ouroboros-ai — see the install guide.

How it works

The input is an idea. Ouroboros manages the work. The runtime writes the code. The output is code plus records.

Documentation

Guide (English)What it is, install, and every step from Interview to Ralph.
한국어 가이드설치부터 Interview·Seed·실행·평가까지 장별 안내.
中文指南它是什么、怎么装，以及判分断言为什么对 agent 隐藏。
GTM RoadmapEvidence gates, proposed joint validation, and conditional enterprise horizons.
GitHubSource, official docs, CLI Reference, issues.

© 2026 Ouro Labs · MIT LicenseLicenseGitHub Issues


---
<!-- page: fetch notes (GitHub API) -->

Fetched via GitHub API on 2026-10-19 (observations, not part of the published source):
- Repo Q00/ouroboros: description "Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more."; MIT; created 2026-01-14; pushed 2026-10-19; 6,247 stars; topics include "loop-engineering".
- Top contributors by commits: Q00 1,252 · shaun0927 647 · cohemm 52 · dependabot 48.
- Latest releases: v0.59.0 (2026-10-19), v0.58.2 (2026-10-19), v0.58.1 (2026-10-17). The site guide states it was verified against 0.51.5 on 2026-08-14.
- Issue #2449 "Model verdicts grant acceptance in evolve fallback and ouroboros_evaluate without executed verification", closed 2026-09-27 (the evaluation-pipeline doc's "Acceptance Authority" section cites it).
- Issue #2562 "Stage 1 detector persists commands that cannot fail (e.g. `pytest --version`) as verification evidence", open.


---
<!-- page: https://ouroboros.page/learn/en/what-is-ouroboros/ -->

# 1. What is Ouroboros

Ouroboros is an open-source tool that manages the requirements, execution, evaluation, and records of AI coding work.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 1.1 Definition

Ouroboros does not write code itself. Code is written by an AI coding tool such as Claude Code or Codex. Ouroboros works before and after that tool: it pins down requirements, hands off execution, verifies results, and records the process.

The input is an idea. Ouroboros manages the work. The runtime writes the code. The output is code plus records.

## 1.2 What you put in

You describe the feature you want or the problem you want fixed, in plain sentences. You do not need a polished specification. Missing decisions are collected by Ouroboros through questions.

Input | Example | 
 | 

A one-line idea | "A web app that adds to-dos and marks them done" | 

Answers to questions | "The list should survive a page refresh" | 

An existing repository (optional) | A project folder you already have | 

## 1.3 Division of roles

Ouroboros and the AI coding tool do different jobs. Ouroboros is the management layer; the AI coding tool is the execution layer. Ouroboros calls the execution layer the runtime.

Actor | Responsibility | 
 | 

You | Provide the idea, answer questions, approve the Seed, check the result | 

Ouroboros | Ask questions (Interview), write the work spec (Seed), manage execution, evaluate, record | 

runtime (Claude Code, etc.) | Write files, edit code, run commands, run tests | 

The Seed is the work-spec document that connects the two layers. Goal, constraints, and completion criteria are saved as a YAML file, and the runtime works against that file. The Seed is covered in chapter 6.

## 1.4 What remains after a run

More than code remains. The following five things are kept.

Artifact | Content | Location | 
 | 

Code | Files and tests written by the runtime | Your working folder | 

Seed | The work spec used for this run | ~/.ouroboros/seeds/ | 

Test results | Whether lint, build, and tests passed | Evaluation output | 

Evaluation results | Verdict on the completion criteria | Evaluation output | 

Execution records | Every execution event | ~/.ouroboros/data/ouroboros.db | 

Because execution records persist, you can find interrupted work again and check later what was run and why.

## 1.5 Before and after

With an AI coding tool alone, the request, the code, and the verification all flow by inside a chat. With Ouroboros, requirements live in a Seed file, the process lives in records, and completion lives in an evaluation verdict. Why this difference matters is explained in chapter 2.


---
<!-- page: https://ouroboros.page/learn/en/why-ouroboros/ -->

# 2. Why use it

AI coding tools are fast, but pinning down requirements and verifying completion are left to you. Ouroboros turns those two jobs into a procedure.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 2.1 Problems when using an AI coding tool alone

A request like "build a to-do app" says nothing about storage, number of users, or how completion is handled. When the AI picks those values on its own, you fix the code after it is written.

Problem | Consequence | 
 | 

The AI fills in missing decisions by itself | Rework after the code is done | 

Only a "done" message remains | No way to check whether it is actually done | 

Long chats blur the original requirements | A result different from what was agreed | 

A dropped session loses its context | You cannot find where it stopped, so you have to explain everything again | 

Repeated failures leave no record | Fixes do not accumulate | 

## 2.2 What changes with Ouroboros

Left: an AI tool used alone. Right: the same work with Ouroboros.

Change | How | 
 | 

Decisions are fixed before coding | The Interview asks about missing decisions (ch. 5) | 

Completion criteria are written down | Acceptance Criteria are saved in the Seed (ch. 6) | 

Completion is verified | A 3-stage evaluation checks tests and criteria (ch. 8) | 

Interrupted work can resume | Execution events are stored in a local database (ch. 11) | 

Failures feed the next run | Evaluation results update the Seed for re-execution (ch. 9) | 

## 2.3 Tasks that fit

Feature work with several requirements that need sorting out

Work whose completion must be proven by tests

Work that will clearly go through several revisions

Long work that must survive interruptions

## 2.4 Tasks that do not need it

For a typo fix or a one-line change that needs no explanation, an AI coding tool alone is faster. The question-and-evaluation procedure would be bigger than the work itself.


---
<!-- page: https://ouroboros.page/learn/en/architecture/ -->

# 3. Components

Ouroboros splits into a command entry point, a management engine, a work spec, an execution layer, a record store, and an evaluator.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code
Work flows user → ooo command → Core → runtime. Records land in the EventStore and the Ledger.

## 3.1 What each component does

Component | Role | 
 | 

You | Provide the idea, answer questions, approve the Seed and the result. | 

ooo command | The entry point for Ouroboros features inside a Claude Code session, e.g. ooo interview, ooo run. | 

Core | The engine that runs the Interview, generates Seeds, manages execution order, and calls evaluation. Talks to the runtime over MCP (Model Context Protocol). | 

Seed | A YAML work spec holding goal, constraints, completion criteria, and data structure. It does not change during a run. | 

runtime | The AI coding tool that actually touches files and code. Claude Code is the default; Codex CLI, OpenCode, and others are supported. | 

EventStore | A local SQLite database storing every execution event. Used to recover interrupted sessions. | 

Ledger | A record of the assumptions and exclusions confirmed while questioning and writing the Seed. | 

Evaluator | Verifies results in three stages: run the tests, compare against the completion criteria, and cross-check with multiple models when needed. | 

## 3.2 Data flow

You enter an idea through the ooo command.

Core asks about missing decisions in the Interview and turns the answers into a Seed.

Core hands the Seed to the runtime, and the runtime writes the code.

The Evaluator compares the result against the Seed's completion criteria.

Every step's events go to the EventStore; decision grounds go to the Ledger.

Because Core and the runtime are separate, the same Seed can be used with a different runtime.

## 3.3 Storage locations

Ouroboros stores its data under ~/.ouroboros/ in your home folder.

File / folder | Content | 
 | 

config.yaml | Main configuration, including the runtime choice | 

seeds/ | Generated Seed YAML files | 

data/ouroboros.db | EventStore (SQLite) | 

logs/ouroboros.log | Logs | 

data/, worktrees/ | EventStore, auto-session state, and isolated work folders | 

Depending on your choices, the project folder may gain a CLAUDE.md command summary and a .ouroboros/ configuration.


---
<!-- page: https://ouroboros.page/learn/en/install/ -->

# 4. Install

This guide uses the Claude Code plugin as the default path. The order is login, plugin install, ooo setup, then verification.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code
Installation is four steps: login, plugin, setup, verify.

## 4.1 Prerequisites

Claude Code with plugin support must be installed.

You do not need to set up a global Python environment, but you do need uv: the plugin launches its MCP server through uvx. Any of pipx install uv, pip install --user uv, or brew install uv works.

On Windows, follow the Linux steps inside WSL 2. Git Bash is not WSL 2, and running the install commands there can fail; if WSL itself will not install, see the troubleshooting guide.

## 4.2 Claude Code login

Open a Claude Code session in your terminal.

claude

Log in inside the Claude Code session.

/login

Expected result: after browser authentication, the session shows you are logged in. Without login, later ooo commands will not work.

## 4.3 Install the plugin

Run the next two commands in a normal terminal, outside Claude Code.

claude plugin marketplace add Q00/ouroboros
claude plugin install ouroboros@ouroboros

Install output captured on 2026-07-16 on Ubuntu 24.04 with Claude Code 2.1.210 and Ouroboros 0.50.4. This screenshot alone is from 0.50.4; the two commands above are unchanged in 0.51.5.
Expected result: claude plugin list shows ouroboros@ouroboros as enabled.

## 4.4 ooo setup — connect Core over MCP

Open a Claude Code session in the project folder you will work in, and type:

ooo setup

ooo setup selects a runtime profile and saves that choice to ~/.ouroboros/config.yaml. Optionally it adds a command summary to the project's CLAUDE.md. MCP server registration belongs to the plugin you installed in 4.3, so ooo setup leaves ~/.claude/mcp.json untouched.

Expected result: the detected runtimes, Setup complete!, and the config path (~/.ouroboros/config.yaml). Check the MCP connection itself with /mcp in step 4.7. Close Claude Code completely and reopen it after setup.

## 4.5 Verify

Run this inside the Claude Code session.

ooo help

Expected result: a command list including interview, seed, run, and evaluate. If it does not appear, see chapter 11.

## 4.6 Update

Run this inside the Claude Code session.

ooo update

Expected result: the current and latest versions are compared and updated to match your install method. Reopen the Claude Code session afterwards.

## 4.7 Definition of done

claude plugin list shows ouroboros@ouroboros as enabled.

ooo help prints the command list.

Claude Code's /mcp shows the ouroboros server as connected.

Installing from the terminal without Claude Code
The standalone CLI requires Python 3.12 or later and installs from a normal terminal.

pip install ouroboros-ai
ouroboros setup

Other runtimes such as Codex CLI are selected with ouroboros setup --runtime codex. Once that is done, the same ooo commands shown throughout this guide work the same way in that session; the examples are just written from the Claude Code chat window's point of view.


---
<!-- page: https://ouroboros.page/learn/en/interview/ -->

# 5. Interview

The Interview finds the decisions your idea has not made yet and asks about them. From here, one to-do app example continues through chapter 9.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 5.1 What it does

"A to-do app" alone does not decide storage or how completion is handled. The Interview finds decisions like these that change the outcome, asks about them, and collects the answers as the raw material for the next chapter's Seed. A single sentence of input is enough.

## 5.2 Start

Run this inside the Claude Code session. If you installed the Codex CLI or OpenCode plugin instead, the same command works inside that session too; see Install the plugin.

ooo interview "a simple web app to add today's to-dos and mark them done"

Expected result: the first question appears. The number and order of questions depend on the idea.

If you want to try the question flow before real work, run ooo tutorial first. The standalone CLI path without Claude Code uses a different command, ouroboros init start; see chapter 4.

## 5.3 How to answer

Each question pins one decision. For the example, these decisions get confirmed:

Question topic | Example answer | Decision pinned | 
 | 

Data persistence | "It should survive a refresh" | Storage method | 

Completion handling | "Don't delete it, strike it through" | How done state is shown | 

User scope | "Just one person" | Accounts and sync excluded | 

Answer in plain sentences. If you do not know, say so and take a suggestion; that is better than a vague answer.

## 5.4 Ambiguity Score

As answers accumulate the score falls; at 0.2 or below a Seed can be generated.
The Ambiguity Score expresses the remaining ambiguity in the requirements as a value from 0 to 1. The clarity of the goal (weighted 40%), constraints (30%), and success criteria (30%) is averaged, and the score is 1 minus that average. Closer to 0 means clearer.

## 5.5 Exit condition

When the score drops to 0.2 or below, the Interview is considered sufficient and Seed generation can proceed. A low score can still hide wrong content, so review the summary along with the number before generating a Seed.

## 5.6 session_id

When the Interview ends, a session_id remains in the output. Copy it; the next chapter uses it as the input for Seed generation.

## 5.7 One command from questions to execution — auto

To hand questions, Seed generation, and execution to a single command, use ooo auto.

ooo auto "a simple web app to add today's to-dos and mark them done"

Expected result: question rounds run automatically, and execution starts only after the Seed passes grade A. If it stops midway, an auto_session_id and a resume command are shown. Grade A is explained in chapter 6.

To stop after the Seed and check it yourself, add --skip-run. Resume an interrupted session with ooo auto --resume <auto_session_id>.

For your first time we recommend the ooo interview path, where you answer each question yourself and can see what gets decided.


---
<!-- page: https://ouroboros.page/learn/en/seed/ -->

# 6. Seed

The answers from chapter 5's Interview are organized into a work-spec file called the Seed. Before running, confirm this file matches your answers.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 6.1 What it is

The Seed is a YAML file holding the goal, constraints, completion criteria, and data structure. The runtime writes code against this file, and evaluation compares against it too. Once a run starts, the Seed does not change within that run.

The Seed's main fields and where it is stored.

## 6.2 Generate

Inside the Claude Code session, run this with the session_id from chapter 5. Same command in a Codex CLI or OpenCode session once you have set it up.

ooo seed <session_id>

Expected result: a Seed is generated and saved as a YAML file under ~/.ouroboros/seeds/.

Below is a guide example that arranges the sample dialogue into the official Seed field structure. Check the actual result in the saved file.

goal: Build a web app that adds today's to-dos and marks them done
constraints:
  - Single user on a single device
  - Store in browser localStorage
acceptance_criteria:
  - An empty title is not added
  - An added to-do survives a page refresh
  - Checking a to-do shows and stores the done state immediately
ontology_schema:
  name: TodoList
  fields:
    - name: title
      type: string
    - name: completed
      type: boolean
evaluation_principles:
  - name: completeness
    description: every acceptance criterion actually works
exit_conditions:
  - name: all_criteria_met
    description: all acceptance criteria pass
metadata:
  ambiguity_score: 0.15

## 6.3 Field-by-field review

Field | Content | How to review | 
 | 

Goal | What this run should produce | Check it states what a user must be able to do. Fix unjudgeable wording like "a pretty app". | 

Constraints | Limits that must hold | Check the technical, environmental, and scope limits match your answers. In the example: one user, localStorage. | 

Acceptance Criteria | Criteria for judging completion | Check each item can be verified directly on screen or by a test. Chapter 8's evaluation compares against these. | 

Ontology
(YAML key ontology_schema) | Structure of the data handled | Check field names and types match the feature. In the example: title (string) and completed (boolean). | 

Evaluation Principles | Principles weighted in evaluation | Check the emphasis, such as completeness, matches your intent. | 

Exit Conditions | When the work ends | Check it states which state counts as finished. | 

Non-goals (what you agreed not to build) and the assumptions made while questioning are recorded in the Ledger, not in the Seed body. Look there when you want to confirm whether "single user" was your answer or an assumption. Per the official docs, ouroboros auto --show-ledger in a standalone terminal prints this record.

## 6.4 Grade A

Seeds carry a grade that decides whether they may run. ooo auto starts execution only for grade-A Seeds.

Grade | Meaning | 
 | 

A | No blockers and no open findings, and the coverage, ambiguity, testability, feasibility, and risk scores all pass their thresholds. May run | 

B | No blockers, but findings remain to fix. Repair and regrade | 

C | Blockers present. May not run | 

## 6.5 Edit

If the Seed differs from your answers, fix it before running. For example, if you answered "keep completed items" but the Seed says they are deleted, that is a fix. Describe the change in the Claude Code session; a proposal appears, and it is applied once you approve. You can also edit the saved YAML file directly.

## 6.6 Pre-run checklist

The Goal matches what you want to build.

The Constraints match your answers.

You can think of a way to reproduce each Acceptance Criterion yourself.

The Ontology fields match the data the feature needs.

The ambiguity_score is 0.2 or below.

Once everything checks out, run it in chapter 7.


---
<!-- page: https://ouroboros.page/learn/en/execute/ -->

# 7. Execute

Chapter 6 confirmed the Seed. Execution hands that Seed to the runtime to produce actual code.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 7.1 What it does

ooo run validates the Seed and hands execution to the runtime. The runtime writes files and runs commands; Ouroboros manages order and state. The input is the Seed reviewed in chapter 6.

## 7.2 Start

Run this inside the Claude Code session. Same command in a Codex CLI or OpenCode session once you have set it up.

ooo run

Expected result: execution starts and IDs for status queries are printed. The run continues in the background, so starting is not finishing.

A fresh run asks once how it should execute. Efficient execution starts parallel and decomposed work economically and strengthens the route only when recovery requires it; quality-first execution keeps child work at the parent's starting tier. To stop being asked every time, pin a default once from a normal terminal.

ouroboros config set execution.default_policy quality_first

Expected result: execution.default_policy: ask → quality_first, saved to ~/.ouroboros/config.yaml. The only accepted values are ask (the default), efficient, and quality_first; anything else is rejected. With ask, you keep being prompted. It does not apply to a resume — a resumed run keeps whatever the first run fixed.

## 7.3 Phases

Execution follows a four-phase order called the Double Diamond.

Phase | Content | 
 | 

Discover | Examine the repository, the environment, and what the requirements still need confirmed. | 

Define | Decide what to build and what to leave out. | 

Design | Decide the structure and the order of implementation. | 

Deliver | Create files and run tests. | 

This order exists to stop implementation from starting before understanding.

## 7.4 ID types

Each command prints IDs with different roles. Copy the values below from the output.

ID | Shape | Where you get it | Where you use it | 
 | 

session_id | orch_… | Interview and run output | ooo status, ooo evaluate, session resume | 

job_id | job_… | Background job start output | Status and result queries for background jobs | 

execution_id | exec_… | Run start output | ooo cancel | 

auto_session_id | auto_… | ooo auto output | ooo auto --resume | 

lineage_id | lin_… | ooo evolve output | Revision history queries, ooo ralph | 

## 7.5 Status

Run this inside the Claude Code session.

ooo status <session_id>

Expected result: the current phase and progress. In a separate terminal, ouroboros monitor opens a live progress view.

## 7.6 Cancel

Run this inside the Claude Code session.

ooo cancel

Expected result: a list of active executions appears; pick one or pass an ID to cancel. Confirm the state afterwards with ooo status.

## 7.7 Definition of done

The run state shows completed.

The result files exist in the working folder.

You saved the session_id from the completion summary for the next step. It is used in chapter 8.


---
<!-- page: https://ouroboros.page/learn/en/evaluate/ -->

# 8. Evaluate

In chapter 7 the runtime built the to-do app. Evaluation verifies whether that result satisfies the Seed's completion criteria.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 8.1 What it does

ooo evaluate verifies the execution result in three stages. Use it when a run finishes, or when evaluation did not follow automatically. The input is the session_id printed by the run.

## 8.2 Run

Run this inside the Claude Code session. If you installed the Codex CLI or OpenCode plugin instead, the same command works inside that session too; see Install the plugin.

ooo evaluate <session_id>

Expected result: per-stage pass results and a verdict on the completion criteria. Per the official docs, a finished run may still be in an unverified state before formal evaluation, so run this yourself if evaluation did not follow.

## 8.3 The 3 stages

Cheap checks run before expensive ones. Failing an earlier stage skips the later ones.

Stage | Content | Pass condition | 
 | 

1. Mechanical | Auto-detects the project type and runs lint, build, test, static analysis, and coverage commands. No LLM involved. | All checks exit normally. Default coverage threshold 70% | 

2. Semantic | An LLM compares the result against the Acceptance Criteria and scores it. | Criteria judged met, plus a score of 0.8 or higher | 

3. Consensus | Multiple models vote independently on approval. Runs only under specific conditions. | At least a two-thirds majority approves | 

The 6 conditions that trigger Consensus
After stage 2 passes, the conditions below are checked in priority order, and the first match triggers stage 3. If none match, the result is approved immediately.

The Seed was modified

The Ontology (data structure) changed

The Goal was reinterpreted

The Drift score exceeded 0.3

Stage 2's uncertainty exceeded 0.3

An alternative approach was adopted

Separately, if you request Consensus directly, it runs with priority over the conditions above.

Drift is a 0-to-1 value showing how far the result moved from the original Seed's intent. Lower means the original direction was kept. Low drift does not mean the feature is correct, so read it together with the criteria verdict.

## 8.4 Check the result yourself

Do not stop at the pass message. For the to-do example, open the app in a browser and reproduce each Acceptance Criterion.

Check that an empty title is not added.

Add a to-do, refresh, and check it is still there.

Check the done state shows immediately and is stored.

## 8.5 Difference from ooo qa

ooo evaluate is the formal procedure that verifies a whole execution session. ooo qa is a one-shot check comparing a single file or text against a quality bar.

ooo qa

Expected result: one of pass, revise, or fail, with reasons. A score of 0.80 or higher is pass; below 0.40 is fail. Works without an execution session.

## 8.6 Definition of done

The 3-stage evaluation ended in a pass.

You reproduced the Acceptance Criteria on the actual result.

Remaining issues, if any, are noted. They become the input to chapter 9.


---
<!-- page: https://ouroboros.page/learn/en/evolve/ -->

# 9. Iterate

Assume chapter 8's evaluation left a failing criterion. Evolve is the feature that applies those evaluation findings to the Seed and runs again.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 9.1 What it does

Evaluation ending does not always mean the work is done. Evolve uses the problems found in evaluation to propose changes to the Seed's goal, constraints, and completion criteria, then repeats execution with the changed Seed. In the example, the failure "the done state resets after a refresh" is applied to the next Seed.

## 9.2 Run

Run this inside the Claude Code session, with a description of the work. If you installed the Codex CLI or OpenCode plugin instead, the same command works inside that session too; see Install the plugin.

ooo evolve "to-do app: keep the done state after a refresh"

Expected result: a Seed change proposal reflecting the evaluation, the run result, and a lineage_id. One generation proceeds as Wonder (find what is still unknown), Reflect (draft the changes), execute, evaluate.

To see only the Seed changes without rebuilding code, add --no-execute. List the runs that followed with ooo evolve --status <lineage_id>.

## 9.3 lineage — the revision history

The chain of Seed revisions from the same piece of work is called a lineage.
One evolve's new Seed and run is called a generation, and the chain of generations from the same starting Seed is called a lineage. Query lineage state with the printed lineage_id.

## 9.4 Automatic stop conditions

Per the official docs, iteration stops at the first of these conditions.

Condition | Criterion | 
 | 

Convergence | When the Ontology similarity of two consecutive generations is 0.95 or higher, the data structure is considered stable and iteration stops. | 

Stagnation | When similarity stays at or above the Convergence threshold (0.95) for 3 consecutive generations, nothing more is expected to change and iteration stops. | 

Oscillation | Stops when the structure keeps returning to the one from two generations earlier. | 

Generation cap | Stops at a maximum of 30 generations. | 

Convergence checks apply only after at least 2 generations have completed.

## 9.5 Ralph — automatic iteration

Instead of calling evolve yourself each generation, hand the iteration to Ralph until a stop condition is reached. Pass the lineage_id from 9.2.

ooo ralph --lineage-id <lineage_id>

Expected result: a background job starts and its job ID is printed. Generations repeat until one of: QA passes, an automatic stop condition from 9.4 (Convergence, Stagnation, Oscillation, or the generation cap), cancellation, an unrecoverable failure, a regressing grade, or a time limit.

## 9.6 When you should stop it

More automatic iterations do not guarantee quality. Stop the loop and reset direction yourself when:

The completion criteria are already met.

The same question or failure repeats.

The changes are small relative to the cost of running.

The product direction itself needs a human decision.

Stopping an active run works the same as cancelling in chapter 7.


---
<!-- page: https://ouroboros.page/learn/en/existing-project/ -->

# 10. Existing projects

Up to chapter 9 the example was a fresh project. This chapter applies the same procedure to repositories that already have code, and to team work.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code
Top: connecting an existing repository to the Interview. Bottom: from PRD to GitHub Issues.

## 10.1 What differs

An existing repository already has chosen technology and constraints. Register it, and the Interview stops guessing like it would for a new project and asks questions grounded in the current code and constraints.

## 10.2 brownfield — register existing repositories

Run this inside the Claude Code session. If you installed the Codex CLI or OpenCode plugin instead, the same command works inside that session too; see Install the plugin.

ooo brownfield

Expected result: a numbered list of git repositories and worktrees appears, and you pick the ones to use as default Interview context. Select only the repositories you actually work on.

The standalone CLI exposes the same feature as subcommands of ouroboros setup instead (a different name from ooo brownfield; per the official docs and source):

Command | Role | 
 | 

ouroboros setup scan [SCAN_ROOT] | Scan for repositories only | 

ouroboros setup list | List registered repositories | 

ouroboros setup default | Toggle default repositories | 

The MCP tool's action names are scan, register, query, and set_default (per docs/cli-reference.md and mcp/tools/brownfield_handler.py).

## 10.3 pm — organize product requirements

Use this when organizing requirements at the product level rather than for one feature. Run it inside the Claude Code session. Codex CLI and OpenCode work the same way.

ooo pm

Expected result: product-level questions proceed and a PRD (product requirements document) is produced.

A PRD and a Seed are different. A PRD states what the product should be; a Seed is the work spec one run follows. A PRD is not executed as-is; feed its content to ooo interview to produce an execution-level Seed.

## 10.4 publish — hand work to a team

Turns a Seed into GitHub Issues a team can divide. Requires the gh CLI installed and logged in. Run inside the Claude Code session. Codex CLI and OpenCode work the same way.

ooo publish <seed_path>

Expected result: the issue structure to be created is shown first; after confirmation the issues are created in the target repository.

## 10.5 Definition of done

The brownfield defaults point at the repositories you actually work on.

Interview questions reflect the constraints of the existing code.

If team work was needed, Seed-based issues exist in the target repository.


---
<!-- page: https://ouroboros.page/learn/en/troubleshooting/ -->

# 11. Troubleshooting

Find the symptom first, then follow the order: what to check, the command, the expected result.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code
Each section follows the order symptom, check, command, expected result.

## The plugin fails to start with -32000

Symptom: Failed to reconnect to plugin:ouroboros:ouroboros: -32000

Check the version first. This startup failure was fixed in 0.51.1, and it is the first entry under Highlights in that release. Before it, an existing environment could shadow the [mcp] profile's mcp==2.0.0. The fix makes the shipped launchers run uvx --isolated.

ooo update

Expected result: you are on 0.51.1 or later. Close Claude Code completely and reopen it afterwards.

If you installed from a third-party package such as the AUR, check that package's version first. Third-party packaging can lag several releases behind.

## 11.1 The ooo command is not recognized

Check: ooo works inside a Claude Code session (Codex CLI and OpenCode work the same way once you've completed setup — the check commands below are specific to the Claude Code plugin path). Make sure you did not type it in a normal terminal. It also fails without login, so complete /login first.

Check the plugin state in a normal terminal.

claude plugin list

Expected result: ouroboros@ouroboros shows as enabled. If missing or disabled, reinstall:

claude plugin install ouroboros@ouroboros --force

Expected result: after installing, reopen the Claude Code session and ooo help works.

## 11.2 Interview works but run or status fails

Check: the plugin loaded but Core's MCP server may not be connected. Check the ouroboros server state with /mcp in Claude Code.

The MCP server registration belongs to the plugin, not to ooo setup. Reinstall the plugin from a normal terminal first.

claude plugin install ouroboros@ouroboros --force

Expected result: reinstalling the plugin restores the MCP server registration. Close Claude Code completely, reopen it, and check /mcp again.

If it still will not connect, check that uv is installed with uvx --version. The plugin launches its MCP server through uvx, so without uv the connection fails even when the registration is present. For a standalone install, narrow it down with ouroboros mcp doctor, ouroboros mcp info, and ouroboros status health in a normal terminal.

## 11.3 The run seems stuck

Check: runs can take a long time in the background. Query the state first.

ooo status <session_id>

Expected result: the current phase is shown. If you judge there is no progress, cancel with ooo cancel and run again.

## 11.4 Resume an interrupted auto session

Check: when ooo auto stops at a gate or on an error, the output keeps an auto_session_id and a resume command.

ooo auto --resume <auto_session_id>

Expected result: the same auto session continues. If you lost the ID, find the session first with 11.5.

## 11.5 Recover a session from a closed window

Check: execution events remain in the EventStore, so sessions survive a closed window.

ooo resume-session

Expected result: a list of running or paused sessions. Pick the one to re-attach.

## 11.6 The same failure repeats

Check: when repeated runs produce the same structure and the same failure, change the approach instead of adding iterations.

ooo unstuck

Expected result: alternative approaches to the current problem are proposed. You choose which to use.

## 11.7 Uninstall

First preview what would be removed, in a normal terminal.

ouroboros uninstall --dry-run

Expected result: the list of items to remove. Actually remove with ouroboros uninstall; keep the data with --keep-data. Remove the Claude Code plugin separately with claude plugin uninstall ouroboros.

## 11.8 Official channels

Getting Started

CLI Reference

GitHub Issues


---
<!-- page: https://ouroboros.page/learn/en/glossary/ -->

# 12. Glossary

Short definitions of product terms. The link after each entry goes to the page where it is used.

Ouroboros 0.51.5upstream d103058feverified 2026-08-14 against docs and code

## 12.1 Specification

### Interview

The feature that finds and asks about decisions your idea has not made yet. Ch. 5

### Ambiguity Score

A 0-to-1 value for the ambiguity left in the requirements. At 0.2 or below a Seed can be generated. Ch. 5

### Seed

The work-spec YAML file holding goal, constraints, completion criteria, and data structure. Both the runtime and evaluation work against it. Ch. 6

### Goal

The Seed field stating what this run should produce. Ch. 6

### Constraints

The Seed field holding the limits a run must respect. Ch. 6

### Non-goals

What you agreed not to build this time. Recorded in the Ledger, not the Seed body. Ch. 6

### Acceptance Criteria

The list of criteria for judging completion, written so each can be verified on screen or by a test. Ch. 6

### Ontology

The structure naming and typing the data the work handles. Ch. 6

### Grade A

The Seed state with no blockers and quality scores past their thresholds, allowing execution. ooo auto starts execution only at grade A. Ch. 6

### Ledger

The record of assumptions, exclusions, and decision grounds confirmed while questioning. Ch. 6

## 12.2 Execution

### Core

The Ouroboros engine handling the Interview, Seeds, execution management, and evaluation. Ch. 3

### runtime

The AI coding tool that actually touches files and code, such as Claude Code or Codex CLI. Ch. 3

### MCP

The protocol that lets the runtime call Ouroboros Core's features. Ch. 4

### Double Diamond

The execution phases run in the order Discover, Define, Design, Deliver. Ch. 7

## 12.3 Evaluation

### Mechanical

Evaluation stage 1: runs commands such as lint, build, and test and checks the results. Ch. 8

### Semantic

Evaluation stage 2: an LLM judges whether the result meets the Acceptance Criteria. Ch. 8

### Consensus

Evaluation stage 3: multiple models vote independently on approval. Runs only under set conditions. Ch. 8

### Drift

A 0-to-1 value for how far a result moved from the original Seed's intent, weighted Goal 50%, Constraints 30%, Ontology 20%. Ch. 8

## 12.4 Iteration

### Evolve

The feature that applies evaluation findings to the Seed and runs again. Ch. 9

### Wonder · Reflect

The first two steps of one Evolve generation. Wonder finds what is still unknown; Reflect turns that into a Seed change proposal. Ch. 9

### lineage

The history grouping the chain of Seed revisions from the same piece of work. Ch. 9

### Convergence

The state where repeated runs barely change the Seed's data structure. The criterion is an Ontology similarity of 0.95 or higher between consecutive generations. Ch. 9

### Stagnation

The state where iteration no longer improves the result. Used as the signal to stop and change approach. Ch. 9

### Ralph

The feature that repeats revision runs in the background until a stop condition is reached. Ch. 9

## 12.5 Records and IDs

### EventStore

The local SQLite database storing every execution event. Used for session recovery. Ch. 3

### session_id · job_id · execution_id · lineage_id · auto_session_id

IDs used for session queries and evaluation, background-job queries, cancelling runs, revision history, and auto resume, respectively. Ch. 5 · Ch. 7


---
<!-- page: https://github.com/Q00/ouroboros/blob/main/README.md -->

<!-- mcp-name: io.github.Q00/ouroboros -->
<p align="right">
  <strong>English</strong> | <a href="./README.ko.md">한국어</a> | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <br/>
  ◯ ─────────── ◯
  <br/><br/>
  <img src="./docs/images/ouroboros.png" width="420" alt="Ouroboros">
  <br/><br/>
  <strong>O U R O B O R O S</strong>
  <br/><br/>
  ◯ ─────────── ◯
  <br/>
</p>


<p align="center">
  <strong>It gets smarter on its own. We just hold the line.</strong>
  <br/>
  <sub>Skip the prompt engineering. The agent runs, fails, and gets smarter every generation. The grading command and expected result never make it into the success contract we hand it.</sub>
  <br/>
  <sub>The <strong>Agent OS</strong> for replayable AI coding workflows</sub>
</p>

<p align="center">
  <a href="https://github.com/Q00/ouroboros"><img src="https://img.shields.io/github/stars/Q00/ouroboros?color=yellow&logo=github&label=stars" alt="GitHub stars"></a>
  <a href="https://pypi.org/project/ouroboros-ai/"><img src="https://img.shields.io/pypi/v/ouroboros-ai?color=blue" alt="PyPI"></a>
  <a href="https://github.com/Q00/ouroboros/actions/workflows/test.yml"><img src="https://img.shields.io/github/actions/workflow/status/Q00/ouroboros/test.yml?branch=main" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="License"></a>
  <a href="https://github.com/sponsors/Q00"><img src="https://img.shields.io/github/sponsors/Q00?logo=githubsponsors&color=EA4AAA&label=sponsors" alt="GitHub Sponsors"></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/26008?utm_source=repository-badge&utm_medium=badge&utm_campaign=badge-repository-26008" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/26008" alt="Q00%2Fouroboros | Trendshift" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#why-ouroboros">Why</a> ·
  <a href="#what-you-get">Results</a> ·
  <a href="#the-loop">How It Works</a> ·
  <a href="#commands">Commands</a> ·
  <a href="#from-wonder-to-ontology">Philosophy</a> ·
  <a href="https://ouroboros.page/learn/en/">Guide</a>
</p>

```bash
# macOS / Linux / WSL 2
curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | OUROBOROS_INSTALL_REF=readme-hero bash
```

```powershell
# Windows (PowerShell) — no Python needed; installs Git and uv for you
irm https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.ps1 | iex
```

<p align="center"><sub>One command installs it. Then run <code>ooo setup</code> once inside your coding agent — details in <a href="#quick-start">Quick Start</a>.</sub></p>

<p align="center"><sub><b>Separate runs, separate hosts. Different tasks on purpose — the engine is what is shared, not the prompt</b></sub></p>

<table align="center">
<tr>
<td align="center" width="50%"><img src="./docs/images/ooo-interview.gif" alt="Terminal recording of the ouroboros CLI interview reporting an ambiguity score"><br><sub><b>Terminal CLI</b> — a task-management CLI: <code>ouroboros init start</code> asking about ordering and scope, then reporting an ambiguity score</sub></td>
<td align="center" width="50%"><img src="./docs/images/host-codex.gif" alt="Screen recording of the ChatGPT app calling Ouroboros as an integration"><br><sub><b>ChatGPT (Codex)</b> — called as an integration, on a video-publishing harness: the interview, its advisory lanes, and the ambiguity ledger</sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="./docs/images/host-claude.gif" alt="Screen recording of Claude Code running six Ouroboros interview advisory lanes in parallel"><br><sub><b>Claude Code</b> — a YouTube automation task, with the six advisory lanes running in parallel before the interview submits</sub></td>
<td align="center" width="50%"><img src="./docs/images/host-hermes.gif" alt="Screen recording of a Discord bot running the Ouroboros interview and reporting a final ambiguity of 0.15"><br><sub><b>Hermes (Discord)</b> — a kart-racing game, run as a chat bot, ending at <code>Final ambiguity: 0.15</code></sub></td>
</tr>
<tr>
<td align="center" width="50%"><img src="./docs/images/host-dsh.gif" alt="Screen recording of DeepSeek Harness calling the Ouroboros interview tool and submitting advisory fan-out results"><br><sub><b>DeepSeek Harness</b> — an OSS-trend outreach script, driven from a dsh chat: <code>mcp__ouroboros__ouroboros_interview</code> turn by turn, fan-out results submitted between rounds</sub></td>
<td align="center" width="50%"><img src="./docs/images/host-kiro.gif" alt="10x screen recording of Kiro CLI running an Ouroboros interview"><br><sub><b>Kiro</b> — the Kiro CLI running the Ouroboros interview flow, turning a vague request into a structured, testable Seed</sub></td>
</tr>
<tr>
<td align="center" colspan="2"><img src="./docs/images/host-antigravity.gif" width="50%" alt="Screen recording of Antigravity running an Ouroboros interview and submitting the selected answer"><br><sub><b>Antigravity</b> — a YouTube-publishing automation interview: asks what to automate, shows advisory lanes, and submits the selected answer</sub></td>
</tr>
</table>

**Turn a vague idea into a verified, working codebase -- across Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Kiro, Copilot, Pi, OMP, Zcode, Goose, GJC, Antigravity, and Grok.**

Ouroboros is an **Agent OS** for AI coding: a local-first runtime layer that
turns non-deterministic agent work into a replayable, observable, policy-bound
execution contract. It replaces ad-hoc prompting with a structured
specification-first workflow: interview, crystallize, execute, evaluate,
evolve.

---

## The Ouroboros Agent OS Stack

Like any OS, Ouroboros is split into a stable **OS layer** of primitives, an
**application layer** of domain workflows, and a **shell** that humans actually
sit in front of. Three repos, one stack:

| Layer | Repo | Role | What it gives you |
| :--- | :--- | :--- | :--- |
| **Shell** (terminal client) | [`Ouro-labs/ourocode`](https://github.com/Ouro-labs/ourocode) | Native terminal UI for running `ooo` workflows across Claude / Codex / Gemini CLIs in one session | TUI, wonderTool decision pickers, MCP pane state, command discovery |
| **Apps** (domain workflows) | [`Ouro-labs/ouroboros-plugins`](https://github.com/Ouro-labs/ouroboros-plugins) | UserLevel plugin contract — composes core primitives into installable domain programs (PR ops, Jira sync, incidents, releases) | Plugin manifest, scoped permissions, audit/provenance, reference plugins |
| **OS** (this repo) | [`Q00/ouroboros`](https://github.com/Q00/ouroboros) | Agent OS core — Seed, Ledger, Runtime, MCP, safety boundaries | `ooo` commands, spec-first workflow engine, multi-runtime adapter |

**How they connect:**

```
  ourocode  ──►  ooo / ouroboros-plugins  ──►  ouroboros core (Seed · Ledger · MCP · Runtime)
   shell             user-level apps                        kernel
```

- The **kernel** (`ouroboros`) owns the contract: every action becomes a
  Seed-bound, ledger-recorded, replayable event — regardless of which LLM
  executes it.
- **Plugins** (`ouroboros-plugins`) declare scoped capabilities against that
  contract, so domain workflows (review a PR, triage a Linear ticket, run a
  release) stay auditable and policy-bound instead of being one-off prompts.
- **Ourocode** is the terminal shell: it surfaces MCP state, interview
  questions, and wonderTool decisions as first-class TUI elements, so you can
  drive the OS without leaving the keyboard or switching between CLIs.

Use `ouroboros` alone with any supported CLI, layer plugins on for domain
workflows, or install `ourocode` when you want a unified terminal cockpit.

> **Disclaimer.** The Ouroboros project and community are **not affiliated with
> any cryptocurrency, token, memecoin, or trading community** — including, but
> not limited to, any "ouroboros" tickers on pump.fun or other launchpads. This
> is an open-source developer tool. We do not issue, endorse, or hold any
> coins. Any token claiming association with this project is unauthorized.

> **Naming note.** A separate, unaffiliated open-source project also uses the
> name "Ouroboros" — Anton Razzhigaev's self-modifying, autonomous-memory agent
> at `github.com/razzant/ouroboros`. No shared code, no relationship. This
> project locks a specification before executing rather than rewriting its own
> architecture; if you're looking for the latter, that's the other one.

---

## Why Ouroboros?

Most AI coding fails at the **input**, not the output. The bottleneck is not AI capability -- it is human clarity.

| Problem       | What Happens                     | Ouroboros Fix                                 |
| :------------ | :------------------------------- | :-------------------------------------------- |
| Vague prompts | AI guesses, you rework           | Socratic interview exposes hidden assumptions |
| No spec       | Architecture drifts mid-build    | Immutable seed spec locks intent before code  |
| Manual QA     | "Looks good" is not verification | 3-stage automated evaluation gate             |

---

## Quick Start

**Install** — one command, everything auto-detected:

```bash
# macOS / Linux / WSL 2
curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | OUROBOROS_INSTALL_REF=readme bash
```

```powershell
# Windows (PowerShell 5.1+ or pwsh 7+) — nothing to install first
irm https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.ps1 | iex
```

The Windows installer installs Git and uv through winget when they are missing,
lets uv download its own Python, then installs `ouroboros-ai` and wires the
host it finds. Native Windows is experimental and Codex CLI needs WSL 2; see
[platform support](./docs/platform-support.md).

**First command** — open your AI coding agent and run these in order:

```
> ooo setup
> ooo interview "I want to build a task management CLI"
```

`ooo setup` is a one-time configuration step. `ooo interview` is the first
workflow command and starts the Socratic interview. After setup, Codex follows
its currently selected model and Claude Code starts with its recommended model
settings. Choose **Directly configure models** only when you want to pin a
stage to a specific model; it opens the local settings screen in your browser.
You can return to those settings any time with `ooo config`.

Or from a plain terminal, without an agent host:

```
$ ouroboros init start --orchestrator "I want to build a task management CLI tool"
```

<p align="center">
  <sub>That recording is this exact command. It is at the top of this page so you can see the tool before installing it.</sub>
</p>

<p align="center">
  <img src="./docs/images/ooo-setup-refresh.gif" width="760" alt="Terminal recording of ouroboros setup refresh installing Codex rules and skills, Hermes skills, the OpenCode plugin and instruction guide, and the Pi and GJC bridges, ending with the line Refreshed runtime artifacts: codex, hermes, opencode, pi, gjc">
</p>

<p align="center">
  <sub><code>ouroboros setup refresh</code> on one machine. It installs into the hosts that machine actually has, each in the shape that host expects: rules and skills for Codex, skills for Hermes, a plugin and an <code>AGENTS.md</code> for OpenCode, bridges for Pi and GJC. Your machine will show whichever of the thirteen you have installed.</sub>
</p>

> Works with Claude Code, Codex CLI, GitHub Copilot CLI, OpenCode, Hermes, Gemini, Kiro CLI, Pi CLI, OMP CLI, Zcode, Goose, GJC, Antigravity CLI, and Grok Build CLI. The installer detects available runtimes and registers the MCP server where the host supports it. For explicit selection, run `ouroboros setup --runtime <opencode|kiro|copilot|gemini|pi|omp|zcode|goose|gjc|antigravity|grok>` after installation. Copilot live-discovers its subscription catalog via the GitHub Copilot models API; Kiro's settings picker queries the authenticated CLI with `kiro-cli chat --listmodels -f json`, so account and enterprise allow-list changes appear without a hardcoded model table.

> **DeepSeek support.** Ouroboros speaks DeepSeek two ways. Point the interview/Seed/QA pipeline at DeepSeek's own models with `--llm-backend dsh` (`ouroboros mcp serve --runtime claude-cli --llm-backend dsh`, or `OUROBOROS_LLM_BACKEND=dsh`) — this drives [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)'s ACP server under the hood. Or go the other way: install the [`dsh-ouroboros` plugin](./integrations/dsh-plugin) (`dsh plugin --profile <your-profile> add "github:Q00/ouroboros#main&path:integrations/dsh-plugin"`) and type `ooo interview` / `ooo auto` directly in the DeepSeek Harness chat — the same `ouroboros_interview` / `ouroboros_auto` tools run natively inside it, Socratic questions and all. Both directions, including what the `dsh` backend needs beyond the one variable, are in the [DeepSeek Harness guide](./docs/guides/deepseek-harness.md).

<details>
<summary><strong>Codex plugin quick start</strong></summary>

Needs `codex` on your `PATH` and `uvx` on the host (the plugin's MCP descriptor
launches the server with it). Install uv with `pipx install uv`,
`pip install --user uv`, or `brew install uv`.

```bash
codex plugin marketplace add Q00/ouroboros
codex plugin add ouroboros@ouroboros
```

Start a new Codex session, then run these commands in order:

```
ooo setup
ooo interview "Build a task management CLI"
```

`ooo setup` is the one-time runtime preparation. Once ready, Ouroboros follows
Codex's current default model; choose **Directly configure models** only when
you want to pin a specific model for a pipeline stage.

</details>

<details>
<summary><strong>Kiro CLI quick start</strong></summary>

```bash
pipx install 'ouroboros-ai[mcp]'       # or: uv tool install 'ouroboros-ai[mcp]'
ouroboros setup --runtime kiro         # detects Kiro CLI, registers MCP server, and
                                        # writes OUROBOROS_RUNTIME=kiro into
                                        # ~/.kiro/settings/mcp.json (the trusted,
                                        # setup-managed location -- a project .env
                                        # is untrusted input and this key is ignored there)
```

Then use `ooo` commands inside a Kiro CLI session.

</details>

<details>
<summary><strong>GitHub Copilot CLI quick start</strong></summary>

```bash
gh auth login                                # one-time GitHub auth (used for live model discovery)
pipx install 'ouroboros-ai[mcp]'             # or: uv tool install 'ouroboros-ai[mcp]'
ouroboros setup --runtime copilot            # discovers models live, picks a default,
                                             # registers MCP server in ~/.copilot/mcp-config.json
```

Restart your Copilot CLI session, then use `ooo` commands inside it. Model-ID mapping is catalog-gated: the prior direct and OpenRouter Opus 5 pins resolve to `claude-opus-5` when that ID is present; current Anthropic API pins convert only their trailing numeric separator and only when the discovered catalog contains the exact candidate. Unknown IDs remain unchanged so Copilot reports an explicit unavailable-model error instead of silently selecting a different model. Leave role models unset so setup writes a discovered ID, or set a Copilot-valid ID explicitly. See the [Copilot runtime guide](./docs/runtime-guides/copilot.md).

See the [GitHub Copilot CLI runtime guide](./docs/runtime-guides/copilot.md) for full details.

</details>

<details>
<summary><strong>Other install methods</strong></summary>

**Claude Code plugin only** (no Python package or global Python to install; the
host needs uv, which provides both `uvx` for the MCP server and the skills'
Python >= 3.12 fallback):
```bash
claude plugin marketplace add Q00/ouroboros && claude plugin install ouroboros@ouroboros
```
Then run `ooo setup` inside a Claude Code session.

**pip / uv / pipx**:
```bash
pip install 'ouroboros-ai[mcp,tui]' && ouroboros setup --runtime claude-cli  # recommended MCP v2 default
pip install 'ouroboros-ai[claude]'      # Claude Agent SDK profile (MCP 1.x, isolated)
pip install 'ouroboros-ai[claude-cli]'  # dependency-free Claude CLI worker
pip install 'ouroboros-ai[claude-sdk]'  # explicit alias for the Claude SDK profile
pip install 'ouroboros-ai[litellm]'     # + LiteLLM multi-provider; Python 3.12-3.13
pip install 'ouroboros-ai[mcp]'         # MCP v2 server/client without the GUI
pip install 'ouroboros-ai[tui]'         # settings GUI only
pip install 'ouroboros-ai[all]'         # MCP 1.x app bundle; excludes MCP 2 by design
ouroboros setup                         # configure runtime
```

Core and non-LiteLLM installs support Python 3.12-3.14. LiteLLM-bearing installs (`[litellm]`, `[all]`, and source `--extra all`) support Python 3.12-3.13; use Python 3.13 for current examples. See [Platform Support](./docs/platform-support.md#python-profile-matrix).

The recommended standalone installation is `ouroboros-ai[mcp,tui]` followed by
an explicit MCP v2-compatible runtime selection. The example uses
`--runtime claude-cli`; substitute another compatible runtime such as `codex`,
`opencode`, `hermes`, `gemini`, `goose`, `kiro`, `copilot`, `pi`, or `gjc`.
Use `[claude]` and `[claude-sdk]` only in isolated MCP 1.x environments.

`pip install 'ouroboros-ai[mcp]'` is valid for embedding the MCP client/server library in an already isolated Python environment, but host registration requires `uvx --isolated --python '>=3.12'` or `pipx`. Use `pipx install 'ouroboros-ai[mcp]'` or `uv tool install 'ouroboros-ai[mcp]'` before `ouroboros setup --runtime <claude-cli|codex|opencode|hermes|gemini|goose|kiro|copilot|pi|gjc>`; setup exits without changing runtime configuration when neither isolated launcher is available.

Legacy compatibility: `ouroboros-ai[dashboard]` is still accepted as a compatibility alias/no-op; it does not install dashboard runtime payload. `ouroboros-ai[all]` includes that no-op alias only for compatibility.

**Homebrew (macOS/Linux)**:
```bash
brew tap q00/tap
brew install ouroboros-ai
ouroboros setup                         # configure runtime
```
Self-hosted tap, not yet in homebrew-core. Installs the same package published to PyPI.

See runtime guides: [Claude Code](./docs/runtime-guides/claude-code.md) · [Codex CLI](./docs/runtime-guides/codex.md) · [Hermes](./docs/runtime-guides/hermes.md) · [OpenCode](./docs/runtime-guides/opencode.md) · [Kiro CLI](./docs/runtime-guides/kiro.md) · [Gemini CLI](./docs/runtime-guides/gemini.md) · [GitHub Copilot CLI](./docs/runtime-guides/copilot.md) · [Zcode](./docs/runtime-guides/zcode.md) · [Pi JSON mode](https://pi.dev/docs/latest/json) · [OMP (Oh My Pi)](./docs/runtime-guides/omp.md) · [Goose](./docs/runtime-guides/goose.md) · [GJC](./docs/runtime-guides/gjc.md) · [Antigravity CLI](./docs/runtime-guides/antigravity.md) · [Grok Build CLI](./docs/runtime-guides/grok.md)

</details>

<details>
<summary><strong>Uninstall</strong></summary>

```bash
ouroboros uninstall
```

Removes all configuration, MCP registration, and data. See [UNINSTALL.md](./UNINSTALL.md) for details.

</details>

> **Python >= 3.12 required.** LiteLLM-bearing profiles support Python 3.12-3.13. See [Platform Support](./docs/platform-support.md#python-profile-matrix) and [pyproject.toml](./pyproject.toml).
>
> **Installing as an MCP server: use 0.51.1 or later.** Earlier versions can fail at startup with `Failed to reconnect to plugin:ouroboros:ouroboros: -32000` when an existing environment shadows the `[mcp]` profile ([#2012](https://github.com/Q00/ouroboros/issues/2012)). This matters if you install through a downstream package rather than PyPI, since those can lag.

<p align="center">
  <sub>Most people find out they were unclear about three files into the review.<br/>
  If that feels familiar, star <a href="https://github.com/Q00/ouroboros"><strong>Q00/ouroboros on GitHub</strong></a> so the next person it could save can find it.</sub>
</p>

---

## What You Get

After one loop of the Ouroboros cycle, a vague idea becomes a verified codebase:

| Step          | Before                  | After                                                                   |
| :------------ | :---------------------- | :---------------------------------------------------------------------- |
| **Interview** | *"Build me a task CLI"* | 12 hidden assumptions exposed, ambiguity scored to 0.19                 |
| **Seed**      | No spec                 | Immutable specification with acceptance criteria, ontology, constraints |
| **Evaluate**  | Manual review           | 3-stage gate: Mechanical (free) -> Semantic -> Multi-Model Consensus    |

<details>
<summary><strong>What just happened?</strong></summary>

```
interview  ->  Socratic questioning exposed 12 hidden assumptions
seed       ->  Crystallized answers into an immutable spec (Ambiguity: 0.15)
run        ->  Executed via Double Diamond decomposition
evaluate   ->  3-stage verification: Mechanical -> Semantic -> Consensus
```

> Use `ooo <cmd>` inside your AI coding agent session, or `ouroboros init start`, `ouroboros run seed.yaml`, etc. from the terminal.

The serpent completed one loop. Each loop, it knows more than the last.

</details>

---

## How It Compares

AI coding tools are powerful -- but they solve the **wrong problem** when the input is unclear.

|                     | Vanilla AI Coding                        | Ouroboros                                                                       |
| :------------------ | :--------------------------------------- | :------------------------------------------------------------------------------ |
| **Vague prompt**    | AI guesses intent, builds on assumptions | Socratic interview forces clarity *before* code                                 |
| **Spec validation** | No spec -- architecture drifts mid-build | Immutable seed spec locks intent; ambiguity gate (<= 0.2) blocks premature code without explicit `force` |
| **Evaluation**      | "Looks good" / manual QA                 | 3-stage automated gate: Mechanical -> Semantic -> Multi-Model Consensus         |
| **Rework rate**     | High -- wrong assumptions surface late   | Low -- assumptions surface in the interview, not in the PR review               |

---

## The Loop

The ouroboros -- a serpent devouring its own tail -- is not decoration. It IS the architecture:

```
    Interview -> Seed -> Execute -> Evaluate
        ^                           |
        +---- Evolutionary Loop ----+
```

Each cycle does not repeat -- it **evolves**. The output of evaluation feeds back as input for the next generation, until the system truly knows what it is building.

| Phase         | What Happens                                                          |
| :------------ | :-------------------------------------------------------------------- |
| **Interview** | Socratic questioning exposes hidden assumptions                       |
| **Seed**      | Answers crystallize into an immutable specification                   |
| **Execute**   | Double Diamond: Discover -> Define -> Design -> Deliver               |
| **Evaluate**  | 3-stage gate: Mechanical ($0) -> Semantic -> Multi-Model Consensus    |
| **Evolve**    | Wonder *("What do we still not know?")* -> Reflect -> next generation |

> *"This is where the Ouroboros eats its tail: the output of evaluation*
> *becomes the input for the next generation's seed specification."*
> -- `reflect.py`

Convergence is reached when ontology similarity >= 0.95 -- when the system has questioned itself into clarity.

### Ralph: The Loop That Never Stops

`ooo ralph` runs the evolutionary loop persistently -- across session boundaries -- until convergence is reached. Each step is **stateless**: the EventStore reconstructs the full lineage, so even if your machine restarts, the serpent picks up where it left off.

```
Ralph Cycle 1: evolve_step(lineage, seed) -> Gen 1 -> action=CONTINUE
Ralph Cycle 2: evolve_step(lineage)       -> Gen 2 -> action=CONTINUE
Ralph Cycle 3: evolve_step(lineage)       -> Gen 3 -> action=CONVERGED
                                                +-- Ralph stops.
                                                    The ontology has stabilized.
```

---

## Commands

Inside AI coding agent sessions, use `ooo <cmd>` skills. From the terminal, use the `ouroboros` CLI.

| Skill (`ooo`)    | CLI equivalent                                                    | What It Does                                                 |
| :--------------- | :---------------------------------------------------------------- | :----------------------------------------------------------- |
| `ooo setup`      | `ouroboros setup`                                                 | Register runtime and configure project (one-time)            |
| `ooo interview`  | `ouroboros init start`                                            | Socratic questioning -- expose hidden assumptions            |
| `ooo auto`       | `ouroboros auto`                                                  | Goal → A-grade Seed → execution handoff with bounded loops   |
| `ooo seed`       | *(generated by interview)*                                        | Crystallize into immutable spec                              |
| `ooo run`        | `ouroboros run seed.yaml`                                         | Execute via Double Diamond decomposition                     |
| `ooo evaluate`   | *(via MCP)*                                                       | 3-stage verification gate                                    |
| `ooo evolve`     | *(via MCP)*                                                       | Evolutionary loop until ontology converges                   |
| `ooo unstuck`    | *(via MCP)*                                                       | 5 lateral thinking personas when you are stuck               |
| `ooo status`     | `ouroboros status executions` / `ouroboros status execution <id>` | Session tracking + (MCP-only) drift detection                |
| `ooo resume-session` | `ouroboros resume`                                           | List in-flight sessions and re-attach commands              |
| `ooo cancel`     | `ouroboros cancel execution [<id>\|--all]`                        | Cancel stuck or orphaned executions                          |
| `ooo ralph`      | *(via MCP)*                                                       | Persistent loop until verified                               |
| `ooo tutorial`   | *(interactive)*                                                   | Interactive hands-on learning                                |
| `ooo help`       | `ouroboros --help`                                                | Full reference                                               |
| `ooo pm`         | *(via MCP)*                                                       | PM-focused interview + PRD generation                        |
| `ooo qa`         | *(via skill)*                                                     | General-purpose QA verdict for any artifact                  |
| `ooo update`     | `ouroboros update`                                                | Check for updates + upgrade to latest                        |
| `ooo brownfield` | *(via skill)*                                                     | Scan and manage brownfield repo/worktree defaults            |
| `ooo publish`    | *(skill/runtime surface; uses `gh` CLI)*                          | Publish a Seed as GitHub Epic/Task issues for team workflows |

> Not all skills have direct CLI equivalents. Some (`evaluate`, `evolve`, `unstuck`, `ralph`, `publish`) are available through agent skills, runtime rules, or MCP tools rather than a direct `ouroboros <subcommand>` shell command.
> `/resume` is reserved for Claude Code's built-in session picker; use `ooo resume-session` for Ouroboros in-flight sessions.
> Claude Code also reserves `/run`, `/status`, `/help`, and `/config`. The safe
> direct skill forms are `/ouroboros:ouroboros-run`,
> `/ouroboros:ouroboros-status`, `/ouroboros:ouroboros-help`, and
> `/ouroboros:ouroboros-config`; the familiar `ooo run`, `ooo status`,
> `ooo help`, and `ooo config` phrases remain supported.

See the [CLI reference](./docs/cli-reference.md) for full details.

---

## The Nine Minds

Nine highlighted agents below, with 12 more specialized agents available (21 total). All loaded on-demand, never preloaded:

| Agent                    | Role                               | Core Question                                       |
| :----------------------- | :--------------------------------- | :-------------------------------------------------- |
| **Socratic Interviewer** | Questions-only. Never builds.      | *"What are you assuming?"*                          |
| **Ontologist**           | Finds essence, not symptoms        | *"What IS this, really?"*                           |
| **Seed Architect**       | Crystallizes specs from dialogue   | *"Is this complete and unambiguous?"*               |
| **Evaluator**            | 3-stage verification               | *"Did we build the right thing?"*                   |
| **Contrarian**           | Challenges every assumption        | *"What if the opposite were true?"*                 |
| **Hacker**               | Finds unconventional paths         | *"What constraints are actually real?"*             |
| **Simplifier**           | Removes complexity                 | *"What's the simplest thing that could work?"*      |
| **Researcher**           | Stops coding, starts investigating | *"What evidence do we actually have?"*              |
| **Architect**            | Identifies structural causes       | *"If we started over, would we build it this way?"* |

---

## Under the Hood

<details>
<summary><strong>Architecture overview -- Python >= 3.12</strong></summary>

```
src/ouroboros/
+-- bigbang/        Interview, ambiguity scoring, brownfield explorer
+-- routing/        PAL Router -- 3-tier cost optimization (1x / 10x / 30x)
+-- execution/      (deprecated — logic moved to orchestrator/ and mcp/tools/)
+-- evaluation/     Mechanical -> Semantic -> Multi-Model Consensus
+-- evolution/      Wonder / Reflect cycle, convergence detection
+-- resilience/     4-pattern stagnation detection, 5 lateral personas
+-- observability/  3-component drift measurement, auto-retrospective
+-- persistence/    Event sourcing (SQLAlchemy + aiosqlite), checkpoints
+-- orchestrator/   Runtime abstraction layer (Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Kiro, Copilot, Pi, OMP, GJC, Goose, Antigravity, Grok, Zcode)
+-- core/           Types, errors, seed, ontology, security
+-- providers/      LiteLLM adapter (100+ models)
+-- mcp/            MCP client/server integration
+-- plugin/         Plugin system (skill/agent auto-discovery)
+-- tui/            Terminal UI dashboard
+-- cli/            Typer-based CLI
```

**Key internals:**
- **PAL Router** -- Frugal (1x) -> Standard (10x) -> Frontier (30x) with auto-escalation on failure, auto-downgrade on success
- **Drift** -- Goal (50%) + Constraint (30%) + Ontology (20%) weighted measurement, threshold <= 0.3
- **Brownfield** -- Auto-detects config files across multiple language ecosystems
- **Evolution** -- Up to 30 generations, convergence at ontology similarity >= 0.95
- **Stagnation** -- Detects spinning, oscillation, no-drift, and diminishing returns patterns
- **Agent OS runtime** -- Replayable execution contract across capability discovery, policy, directives, event journal, and agent processes
- **Runtime backends** -- Pluggable abstraction layer (`orchestrator.runtime_backend` config) with first-class support for Claude Code, Codex CLI, OpenCode, Hermes, Gemini, Goose, Kiro, Copilot, Pi, and OMP; same workflow spec, different execution engines

See [Architecture](./docs/architecture.md) for the full design document.

</details>

---

## From Wonder to Ontology

<details>
<summary><strong>The philosophical engine behind Ouroboros</strong></summary>

> *Wonder -> "How should I live?" -> "What IS 'live'?" -> Ontology*
> -- Socrates

Every great question leads to a deeper question -- and that deeper question is always **ontological**: not *"how do I do this?"* but *"what IS this, really?"*

```
   Wonder                          Ontology
"What do I want?"    ->    "What IS the thing I want?"
"Build a task CLI"   ->    "What IS a task? What IS priority?"
"Fix the auth bug"   ->    "Is this the root cause, or a symptom?"
```

This is not abstraction for its own sake. When you answer *"What IS a task?"* -- deletable or archivable? solo or team? -- you eliminate an entire class of rework. **The ontological question is the most practical question.**

Ouroboros embeds this into its architecture through the **Double Diamond**:

```
    * Wonder          * Design
   /  (diverge)      /  (diverge)
  /    explore      /    create
 /                 /
* ------------ * ------------ *
 \                 \
  \    define       \    deliver
   \  (converge)     \  (converge)
    * Ontology        * Evaluation
```

The first diamond is **Socratic**: diverge into questions, converge into ontological clarity. The second diamond is **pragmatic**: diverge into design options, converge into verified delivery. Each diamond requires the one before it -- you cannot design what you have not understood.

</details>

<details>
<summary><strong>Ambiguity Score: The Gate Between Wonder and Code</strong></summary>

The Interview does not end when you feel ready -- it ends when the **math** says you are ready. Ouroboros quantifies ambiguity as the inverse of weighted clarity:

```
Ambiguity = 1 - Sum(clarity_i * weight_i)
```

Each dimension is scored 0.0-1.0 by the LLM (temperature 0.1 for reproducibility), then weighted:

| Dimension                                                     | Greenfield | Brownfield |
| :------------------------------------------------------------ | :--------: | :--------: |
| **Goal Clarity** -- *Is the goal specific?*                   |    40%     |    35%     |
| **Constraint Clarity** -- *Are limitations defined?*          |    30%     |    25%     |
| **Success Criteria** -- *Are outcomes measurable?*            |    30%     |    25%     |
| **Context Clarity** -- *Is the existing codebase understood?* |     --     |    15%     |

**Threshold: Ambiguity <= 0.2.** A score above that blocks Seed generation. Passing `force` explicitly is what gets past it, and the CLI puts that choice on screen next to continue and cancel. The gate is a default worth arguing with, not a lock.

```
Example (Greenfield):

  Goal: 0.9 * 0.4  = 0.36
  Constraint: 0.8 * 0.3  = 0.24
  Success: 0.7 * 0.3  = 0.21
                        ------
  Clarity             = 0.81
  Ambiguity = 1 - 0.81 = 0.19  <= 0.2 -> Ready for Seed
```

Why 0.2? Because at 80% weighted clarity, the remaining unknowns are small enough that code-level decisions can resolve them. Above that threshold, you are still guessing at architecture.

</details>

<details>
<summary><strong>Ontology Convergence: When the Serpent Stops</strong></summary>

The evolutionary loop does not run forever. It stops when consecutive generations produce ontologically identical schemas. Similarity is measured as a weighted comparison of schema fields:

```
Similarity = 0.5 * name_overlap + 0.3 * type_match + 0.2 * exact_match
```

| Component        | Weight | What It Measures                                   |
| :--------------- | :----: | :------------------------------------------------- |
| **Name overlap** |  50%   | Do the same field names exist in both generations? |
| **Type match**   |  30%   | Do shared fields have the same types?              |
| **Exact match**  |  20%   | Are name, type, AND description all identical?     |

**Threshold: Similarity >= 0.95** -- the loop converges and stops evolving.

But raw similarity is not the only signal. The system also detects pathological patterns:

| Signal                  | Condition                                        | What It Means                      |
| :---------------------- | :----------------------------------------------- | :--------------------------------- |
| **Stagnation**          | Similarity >= 0.95 for 3 consecutive generations | Ontology has stabilized            |
| **Oscillation**         | Gen N ~ Gen N-2 (period-2 cycle)                 | Stuck bouncing between two designs |
| **Repetitive feedback** | >= 70% question overlap across 3 generations     | Wonder is asking the same things   |
| **Hard cap**            | 30 generations reached                           | Safety valve                       |

```
Gen 1: {Task, Priority, Status}
Gen 2: {Task, Priority, Status, DueDate}     -> similarity 0.78 -> CONTINUE
Gen 3: {Task, Priority, Status, DueDate}     -> similarity 1.00 -> CONVERGED
```

Two mathematical gates, one philosophy: **do not build until you are clear (Ambiguity <= 0.2), do not stop evolving until you are stable (Similarity >= 0.95).**

</details>

---

## Contributing

```bash
git clone https://github.com/Q00/ouroboros
cd ouroboros
uv sync --python 3.13 --all-groups
uv run --python 3.13 --no-sync pytest
```

[Issues](https://github.com/Q00/ouroboros/issues) · [Discussions](https://github.com/Q00/ouroboros/discussions) · [Contributing Guide](./CONTRIBUTING.md)

---

## Sponsors

Ouroboros is MIT-licensed and built in the open. If it saves you rework — or you want the loop to keep evolving — consider sponsoring. Sponsorship directly funds maintenance, new runtime integrations, and sponsor-only deep-dive content.

<p align="center">
  <a href="https://github.com/sponsors/Q00"><img src="https://img.shields.io/badge/%E2%9D%A4%EF%B8%8E%20Sponsor%20on%20GitHub-EA4AAA?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor Q00 on GitHub"></a>
</p>

Every sponsor keeps the serpent evolving. Thank you.

---

## Activity

These numbers are generated from GitHub data and refreshed automatically; caching may delay updates.

<p align="center">
  <a href="https://github.com/Q00/ouroboros/graphs/contributors"><img src="https://img.shields.io/github/contributors/Q00/ouroboros?color=orange" alt="Contributors"></a>
  <a href="https://github.com/Q00/ouroboros/commits/main"><img src="https://img.shields.io/github/commit-activity/m/Q00/ouroboros?color=orange" alt="Commit activity"></a>
  <a href="https://github.com/Q00/ouroboros/pulls?q=is%3Apr+is%3Aclosed"><img src="https://img.shields.io/github/issues-pr-closed/Q00/ouroboros?color=orange" alt="Closed pull requests"></a>
  <a href="https://github.com/Q00/ouroboros/commits/main"><img src="https://img.shields.io/github/last-commit/Q00/ouroboros?color=orange" alt="Last commit"></a>
</p>

---

<p align="center">
  <em>"The beginning is the end, and the end is the beginning."</em>
  <br/><br/>
  <strong>The serpent does not repeat -- it evolves.</strong>
  <br/><br/>
  <code>MIT License</code>
</p>


---
<!-- page: docs/guides/evolution-loop.md -->

<!--
doc_metadata:
  runtime_scope: [all]
-->

# The Evolutionary Loop

> *"This is where the Ouroboros eats its tail: the output of evaluation
> becomes the input for the next generation's seed specification."*
> -- `reflect.py`

The evolutionary loop is the core feedback mechanism that distinguishes Ouroboros from linear AI coding tools. After execution and evaluation, the system **does not stop** -- it asks *"What do we still not know?"* and feeds the answer back into the next generation.

---

## How It Works

```
Gen 1:  Seed(O₁)              → Execute → Evaluate
Gen 2:  Wonder(O₁,E₁) → Reflect → Seed(O₂) → Execute → Evaluate
Gen 3:  Wonder(O₂,E₂) → Reflect → Seed(O₃) → Execute → Evaluate
...until convergence or max_generations (30)
```

**Gen 1** uses the seed from the Socratic interview. **Gen 2+** are fully autonomous -- the Wonder and Reflect engines replace human input.

### The Two Engines

| Engine | Question | Input | Output |
|--------|----------|-------|--------|
| **Wonder** | *"What do we still not know?"* | Current ontology + evaluation results | Questions, tensions, gaps |
| **Reflect** | *"How should the spec evolve?"* | Wonder output + execution artifacts | Refined ACs + ontology mutations |

**Wonder** is philosophical -- it identifies what the system is *assuming* rather than *knowing*. Inspired by Socrates: wonder leads to deeper ontological questions.

**Reflect** is pragmatic -- it takes those gaps and produces concrete changes: new acceptance criteria, modified ontology fields, tightened constraints.

---

## Convergence: When the Serpent Stops

The loop terminates when the ontology stabilizes. Similarity is measured as a weighted comparison:

```
Similarity = 0.5 * name_overlap + 0.3 * type_match + 0.2 * exact_match
```

| Component | Weight | Measures |
|-----------|--------|----------|
| **Name overlap** | 50% | Same field names in both generations? |
| **Type match** | 30% | Shared fields have same types? |
| **Exact match** | 20% | Name, type, AND description identical? |

**Threshold: Similarity >= 0.95** -- the loop converges and stops.

### Termination Signals

The `ConvergenceCriteria` checks four signals (any one triggers termination):

| Signal | Condition | Default |
|--------|-----------|---------|
| **Ontology stability** | `similarity(Oₙ, Oₙ₋₁) >= threshold` | >= 0.95 |
| **Stagnation** | Similarity >= threshold for N consecutive gens | 3 gens |
| **Oscillation** | Gen N ≈ Gen N-2 (period-2 cycle) | Enabled |
| **Hard cap** | Max generations reached | 30 |

A minimum of 2 generations must complete before convergence signals 1-3 are checked.

```
Gen 1: {Task, Priority, Status}
Gen 2: {Task, Priority, Status, DueDate}     → similarity 0.78 → CONTINUE
Gen 3: {Task, Priority, Status, DueDate}     → similarity 1.00 → CONVERGED
```

---

## Ralph: The Persistent Loop

`ooo ralph` is an **MCP-owned loop surface**. In job-backed runtimes, the client starts one `ouroboros_ralph` job and the server runs repeated `evolve_step` generations inside that job until QA passes, convergence is reached, a terminal evolution action occurs, cancellation is requested, or `max_generations` is reached. In OpenCode plugin mode, the same MCP call returns `status=delegated_to_plugin` with `job_id=None`, and the bridge child Task session is the terminal surface. Each generation is still recorded in the EventStore, so lineage history can be inspected and continued, but the client no longer reimplements the multi-generation loop itself.

```
Ralph Cycle 1: evolve_step(lineage, seed) → Gen 1 → action=CONTINUE
Ralph Cycle 2: evolve_step(lineage)       → Gen 2 → action=CONTINUE
Ralph Cycle 3: evolve_step(lineage)       → Gen 3 → action=CONVERGED
                                                 └── Ralph stops.
                                                     The ontology has stabilized.
```

### Ralph vs Evolve

| | `ooo evolve` | `ooo ralph` |
|---|---|---|
| **Scope** | Single evolution step | Loop until convergence |
| **Session** | Within current session | Job-backed runtimes return one Ralph job; OpenCode plugin mode delegates one child Task; both record lineage state in EventStore |
| **Control** | Manual -- you decide when to stop | MCP-owned automation -- job-backed server loop or plugin child Task starts each next generation until convergence/limit |
| **Use case** | Incremental refinement | Full autonomous evolution |

---

## Configuration

Evolution parameters in `~/.ouroboros/config.yaml`:

```yaml
evolution:
  max_generations: 30           # Hard cap on generations
  convergence_threshold: 0.95   # Ontology similarity threshold
  stagnation_window: 3          # Consecutive stable gens before termination
  min_generations: 2            # Minimum gens before convergence check
```

See [Configuration Reference](../config-reference.md) for the full list.

---

## Two Mathematical Gates

The entire Ouroboros workflow is governed by two numerical thresholds:

1. **Ambiguity <= 0.2** -- Do not build until you are clear (interview gate)
2. **Similarity >= 0.95** -- Do not stop evolving until you are stable (convergence gate)

The first gate prevents premature execution. The second prevents premature termination. Together they ensure the system questions itself into clarity before acting, and continues acting until the ontology stabilizes.

---

## Source Code

| Module | Purpose |
|--------|---------|
| `src/ouroboros/evolution/loop.py` | EvolutionaryLoop orchestrator |
| `src/ouroboros/evolution/wonder.py` | WonderEngine -- gap identification |
| `src/ouroboros/evolution/reflect.py` | ReflectEngine -- ontology mutation |
| `src/ouroboros/evolution/convergence.py` | Convergence criteria and signals |
| `src/ouroboros/evolution/projector.py` | Lineage state projection |
| `src/ouroboros/evolution/regression.py` | Regression detection across gens |

---

> See [Architecture](../architecture.md) for the full system design, and the [README philosophy sections](../../README.md#from-wonder-to-ontology) for the Socratic and ontological foundations.


---
<!-- page: docs/guides/evaluation-pipeline.md (excerpts) -->

# Evaluation Pipeline Guide

> 中文说明：[evaluation-pipeline.zh-CN.md](./evaluation-pipeline.zh-CN.md)

Ouroboros Phase 4 runs every execution result through a **three-stage progressive evaluation pipeline** before assigning formal acceptance-criterion (AC) verdicts. Cheaper checks gate the expensive ones: Stage 1 is free, Stage 2 uses one LLM call, and Stage 3 (multi-model consensus) runs only when specifically triggered.

### Acceptance Authority

Model judgment may clarify, construct checks, and withhold approval. It cannot grant acceptance; acceptance comes from executed verification (#2449).

- **Only Stage 1 can grant.** `final_approved` is `true` only when Stage 1 ran at least one configured check and every check passed (`MechanicalResult.has_executed_evidence`).
- **Stage 2 and Stage 3 are advisory.** Each stage that ran may withhold approval: Stage 2 `ac_compliance=false`, a Stage 2 score below `0.8`, a Stage 3 rejection, or the [reward-hacking veto](#reward-hacking-veto). None of them can grant it, and a Stage 3 approval does not lift a Stage 2 block.
- **No executed evidence means unverified, not approved.** When Stage 1 did not run or ran no configured check, the result is `final_approved=false` with `acceptance_state="unverified"`. The model review is still produced and attached as feedback; it is neither a crash nor a silent pass.

`EvaluationResult.acceptance_state` (`approved` / `rejected` / `unverified`) and the `evaluation.pipeline.completed` event's `acceptance_state` field expose the outcome. `ouroboros_evaluate` returns it as `meta.acceptance_state` together with `meta.executed_evidence`, and renders an unverified result as `NOT APPROVED (unverified: no executed verification evidence)` rather than `REJECTED`. The single gate is `decide_final_approval()` in `evaluation/models.py`; `EvaluationPipeline._build_result()` is its only caller in the pipeline.

> **Terminology boundary:** worker task completion is not a formal AC verdict, and task failure is not semantic drift. See [Execution vs. Evaluation Contract](./execution-vs-evaluation.md) for the shared `TaskResult` / `ACResult` distinction.

```
Artifact ready
      │
      ▼
┌─────────────────────────────┐
│  Stage 1: Mechanical ($0)   │ lint / build / test / static / coverage
│  All checks must pass       │ any failure → REJECTED (stop)
└────────────┬────────────────┘
             │ passed (with or without an executed check)
             ▼
┌─────────────────────────────┐
│  Stage 2: Semantic ($$)     │ advisory: may withhold
│  score ≥ 0.8 + ac_compliance│ (non-compliance stops here unless
└────────────┬────────────────┘  trigger_consensus=true)
             │
             ▼
        ┌────┴────┐
        │ Trigger │ ← 7 conditions checked
        │ matrix  │
        └────┬────┘
             │ triggered? → Stage 3: Consensus ($$$, ratio ≥ 0.66), advisory: may withhold
             ▼
┌──────────────────────────────────────────────┐
│  Acceptance gate (decide_final_approval)     │
│  no executed Stage 1 check  → UNVERIFIED     │
│  a model stage withheld     → REJECTED       │
│  otherwise                  → APPROVED       │
└──────────────────────────────────────────────┘
```

> `trigger_consensus=true` sends a Stage 2 AC failure on to Stage 3 as a second opinion. The votes are reported, but a consensus approval cannot lift the Stage 2 block. The [reward-hacking veto](#reward-hacking-veto) is one of the withholding gates.

---


## Stage 2: Semantic Evaluation

Stage 2 calls a Standard-tier LLM (default: `OUROBOROS_SEMANTIC_MODEL` / config value) to evaluate the artifact against the acceptance criterion. The model returns a structured JSON object.

### Scoring Fields

| Field | Type | Range | Meaning |
|-------|------|-------|---------|
| `score` | float | 0.0–1.0 | Overall quality score |
| `ac_compliance` | bool | — | Whether the AC is met |
| `goal_alignment` | float | 0.0–1.0 | Alignment with original seed goal |
| `drift_score` | float | 0.0–1.0 | Deviation from seed intent (lower is better) |
| `uncertainty` | float | 0.0–1.0 | Model's uncertainty about its own evaluation |
| `reasoning` | string | — | Free-text explanation |
| `reward_hacking_risk` | float | 0.0–1.0 | Suspicion that the artifact games the evaluator instead of solving the task. Distinct from `drift_score`, and vetoes approval at `>= 0.7` |
| `questions_used` | list | — | Questions the evaluator asked while verifying the artifact — it has to show its work |
| `evidence` | list | — | File snippets and observations the verdict relied on |

### Approval Logic

Stage 2 is advisory. It never approves; it can only withhold an approval that executed Stage 1 evidence would otherwise grant.

```
if ac_compliance == False and not trigger_consensus  → withheld (Stage 3 not attempted)
if ac_compliance == False and trigger_consensus      → withheld (Stage 3 runs as a reported second opinion)
if score < 0.8                                       → withheld (a Stage 3 approval does not lift this)
if reward_hacking_risk >= 0.7                        → withheld (veto)
otherwise                                            → no objection; approval still requires executed Stage 1 evidence
```

> **The score gate is hardcoded at `0.8`.** `SemanticConfig.satisfaction_threshold` (default `0.8`) exists and is validated, but the pipeline compares against a literal `0.8` and never reads the field. Changing it has no effect on approval today — do not rely on it to loosen or tighten the gate.

> **`ac_compliance=False` with `trigger_consensus=True`.** The pipeline continues to the trigger matrix so Stage 3 can deliver a second opinion, whose votes and disagreements are reported. The Stage 2 withhold still stands: model review is advisory, so a consensus approval cannot overturn it.

> Scores are clamped to 0.0–1.0 after parsing; out-of-range model responses are corrected automatically.

### Reward-Hacking Veto

The acceptance gate (`decide_final_approval()`) treats a Stage 2 `reward_hacking_risk >= 0.7` (`REWARD_HACKING_VETO_THRESHOLD`) as one of the model-review withholds: it blocks an approval that executed Stage 1 evidence would otherwise grant. The threshold is deliberately high so that mild suspicion never blocks a genuine pass.

Like every model gate, the veto only withholds; it never rescues a rejected or unverified result.

`failure_reason` names the first withholding gate in this order: Stage 3 rejection, Stage 2 AC non-compliance, Stage 2 score below `0.8`, then the veto (`model_review_withhold_reason()` in `evaluation/models.py`). So a vetoed result that also had `ac_compliance=False` reports the AC non-compliance. Read `stage2_result.reward_hacking_risk` directly when you need to know whether the veto fired.

### Stage 2 Failure Modes

| Failure mode | Symptom | Cause / Action |
|---|---|---|
| **LLM API error** | `ProviderError` returned | Network issue, rate limit, or invalid API key. Check `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`. The error propagates up — the pipeline stops without marking rejected. |
| **No JSON in response** | `ValidationError: Could not find JSON in response` | The LLM replied without a JSON object. This can happen with certain provider-model combinations. Check model compatibility with `json_schema` response format. |
| **Invalid JSON** | `ValidationError: Invalid JSON in response` | JSON parse error in model output. May indicate model truncation; try increasing `max_tokens`. |
| **Missing required fields** | `ValidationError: Missing required fields: [...]` | Model omitted required fields (`score`, `ac_compliance`, etc.). Usually means a model that does not support structured output reliably. |
| **AC non-compliance** | `Stage 2 failed: AC non-compliance (score=X.XX)` | The LLM determined the artifact does not meet the AC. Inspect `reasoning` in the Stage 2 completed event. |
| **Score below threshold** | `final_approved=False` with high `ac_compliance=True` | Score is between 0.0–0.79. Either the artifact quality is genuinely low, or the AC is too broad. |


## Stage 3: Consensus (Multi-Model or Single-Model Fallback)

Stage 3 is the consensus stage; its simple evaluator has two execution paths. The multi-model path may first filter the configured roster for reviewer independence, then launches the retained vote calls concurrently through the evaluator's one LLM adapter. It compares the approval ratio among the successfully collected votes with `majority_threshold` (default `0.66`) and errors when fewer than two votes succeed. Separate calls or model labels are not, by themselves, evidence of separate models, vendors, or backends. The fallback path queries the adapter's session model three times with different perspective prompts.

### Simple Consensus (Default)

On the multi-model path, the configured roster is the starting point; reviewer-independence filtering may remove entries before the retained slots are queried in parallel through the same adapter. **How the default roster is resolved depends on the configured consensus-role backend**, and that setting need not match an adapter supplied independently by a direct API caller.

**Roster-resolution priority.** `get_consensus_models()` first returns a non-empty `OUROBOROS_CONSENSUS_MODELS` list verbatim. Otherwise it reads `config.consensus.models`: a recognized shipped roster is normalized for the configured backend, while a genuinely custom roster is preserved. If config loading fails or has no roster, the shipped fallback is also normalized for the backend. Outside the sentinel set below, that backend-aware config/default resolution retains these shipped OpenRouter identifiers:

```
openrouter/openai/gpt-4o
openrouter/anthropic/claude-opus-4.8
openrouter/google/gemini-2.5-pro
```

**OpenRouter-routed adapters.** When the adapter already supplied to `ConsensusEvaluator` is LiteLLM/OpenRouter-capable and actually routes these provider-qualified identifiers, the one adapter can dispatch the three calls to three vendors. The roster alone neither selects that adapter nor attests that this routing occurred. `ConsensusConfig(models=None)` resolves `get_llm_backend_for_role("consensus")` and then `get_consensus_models()` at construction time (still subject to the environment-first priority above); it does not inspect the evaluator's adapter. Direct Python callers must keep the resolved roster and their `llm_adapter` aligned and verify actual transport/provider evidence.

**Local adapters that still receive the OpenRouter roster.** `claude_code`, `gemini`, `goose`, and `ourocode` are not in `_SENTINEL_DEFAULT_BACKENDS`, so backend-aware default resolution can hand them the shipped OpenRouter strings. That does not switch adapters. Without an OpenRouter key, simple consensus sees the `openrouter/` entries and falls back to the session model. With a key present incidentally, it takes the multi-model code path but passes those strings through the local adapter, where they may be unsupported or resolve according to that adapter. Deliberative mode has no credential-based single-model fallback.

In all three backend categories, an OpenRouter-looking roster or recorded requested-model label is not proof that three vendors voted.

**Sentinel-model backends.** With no `OUROBOROS_CONSENSUS_MODELS` override, backend-aware config/default resolution maps a recognized shipped roster to the literal string `"default"` for all three slots when the backend is in `_SENTINEL_DEFAULT_BACKENDS` (`config/loader.py:101`, `:2028-2049`, `:2226-2245`). An environment roster or a non-shipped custom config roster is preserved verbatim instead. The sentinel set is Codex, **OpenCode**, Kiro, Copilot, Hermes, Pi, GJC, Antigravity, Grok, and Zcode.

OpenCode is easy to miss here: it is not a separate member of the union, it rides in through `_CODEX_LLM_BACKENDS`, which is `frozenset({"codex", "codex_cli", "opencode", "opencode_cli"})` (`config/loader.py:76`). Therefore its shipped config/default roster normalizes to `("default", "default", "default")` under the same no-environment-override condition as Codex. The unrelated `_OPENCODE_BACKENDS` constant at `config/loader.py:113` is used for permission-mode resolution, not for model defaults.

**Tier-alias backends.** On the Claude CLI family the automatic roster names the frontier alias in every slot (`("opus", "opus", "opus")`). When `ConsensusConfig(models=None)` resolves a roster with one distinct model for such a backend, `_should_use_multi_model()` selects the single-model perspective fallback below, so the three votes differ by perspective prompt rather than repeating one prompt. A pinned roster with distinct entries keeps the multi-model path.

Otherwise, `_should_use_multi_model()` selects the code's `_evaluate_multi_model()` branch for any roster with no `openrouter/` entry, so `"default"` does **not** trigger the single-model perspective fallback below. The branch name does not prove model diversity: on these backends Stage 3 casts three votes labeled `default`, all from the one model that backend is configured to use.

> **Auditing note.** Three votes labeled `default` are not three independent reviewers. If your consensus evidence shows that, the roster resolved to the sentinel and the votes came from one model.

**Reviewer-independence filtering happens before model-profile resolution.** The multi-model path starts with the configured roster and, when `EvaluationContext.executor_backend` is present, passes those requested labels plus `available_runtime_backends()` to `resolve_reviewer_independence()`. Fewer than two distinct vendor families among the detected installed, runtime-capable backends makes filtering a no-op and reports `unavailable`. Otherwise, labels known to share the executor's vendor are removed only if at least two labels would remain. A label's vendor comes from the backend the roster was resolved for only when that backend runs a tier alias such as `opus`, which always names its own vendor's model (`opus` on Claude is Anthropic). A `"default"` label runs whatever the backend is configured to run, which may be another provider (OpenCode, or Codex with a custom provider), so it stays unknown; explicit backends (`litellm`, `copilot`), caller-supplied rosters and `"default"` labels fall back to reading the vendor from the model id. Unknown-vendor labels are retained, and if filtering would leave fewer than two voters the original roster is kept. The `evaluation.stage3.started` event and the concurrent vote-task list both use this post-filter roster.

**Changing or filtering the roster does not change the adapter.** `ConsensusEvaluator` holds one `self._llm`; every retained vote goes through it.

**Actual per-vote resolution chain.** After the reviewer filter, each retained entry becomes `CompletionConfig(model=entry, role="consensus_vote")`. The already-selected adapter then resolves `llm_role_profiles.consensus_vote` and the referenced `llm_profiles` entry for its own backend before dispatching the resulting effective model through that same adapter and transport. With `ConsensusConfig(models=None)`, `models_are_explicit` remains false even when the resolved roster came from `OUROBOROS_CONSENSUS_MODELS` or `config.consensus.models`; a `consensus_vote` profile model can therefore replace every retained entry, collapsing differently named slots onto one effective model. A direct caller that passes `ConsensusConfig(models=(...))` marks non-empty, non-`default` entries as request pins, but still sends all votes through the same adapter.

Setting `OUROBOROS_CONSENSUS_MODELS` or `consensus.models` alone therefore does not replace the adapter or prove cross-vendor routing. An adapter that is already OpenRouter-capable may interpret provider-qualified strings and route the calls to those providers through that same adapter. A local CLI adapter instead receives the profile-resolved model as its own argument; an `openrouter/...` string does not switch the call to OpenRouter, so it may fail as unsupported or remain on that adapter under a different label.

Cross-vendor independence requires the active LLM backend to be one that can actually reach those providers. Pick the roster to match the backend you are on, not the other way round, and verify effective dispatch plus transport/provider response evidence. Reviewer-independence classification is based on the pre-profile requested labels, while consensus parsing records each post-filter requested label in `Vote.model` rather than the provider-returned model. The labels, Stage 3 events, and `reviewer_independence` status are therefore classifications, not routing attestation.

Each successful vote call returns `{ approved, confidence, reasoning }`.

> **Stage 3 is advisory.** A consensus rejection withholds approval; a consensus approval grants nothing on its own. The pipeline result is approved only when executed Stage 1 evidence exists and no model stage withheld.

**Consensus rule:** `approving_votes / successfully_collected_votes >= majority_threshold` (default `0.66`). The denominator is the successful responses from the post-filter roster, not the configured or pre-filter roster size. “Two of three” is only the common three-success example, not an invariant; see [Parallel Consensus Failure Tolerance](#parallel-consensus-failure-tolerance).

> **Single-model fallback.** When the configured roster contains an `openrouter/*` entry but `OPENROUTER_API_KEY` is missing or still a `YOUR_…` placeholder, `ConsensusEvaluator` silently switches to a single-model mode: the session model is queried three times with the advocate, devil's advocate, and judge system prompts, and those perspectives vote. The same `majority_threshold` comparison is applied over the successfully collected perspective votes, and fewer than two successes is an error. The reviewers are the same vendor by construction, so reviewer independence is reported as unavailable. Stage 3 events carry `session/<perspective>` model names and a `single-model-perspectives:` trigger reason; check for those if Stage 3 looks cheaper than expected. The same mode also runs for an automatic single-model roster on a tier-alias backend (see Tier-alias backends above). Any other roster with no `openrouter/*` entry skips the credential check and uses the multi-model code path, still through the same adapter.



---
<!-- page: docs/guides/execution-vs-evaluation.md -->

<!--
doc_metadata:
  runtime_scope: [all]
-->

# Execution vs. Evaluation Contract

Ouroboros keeps worker execution outcomes separate from formal acceptance-criterion verdicts.

This distinction is part of the Agent OS runtime contract:

> **Execution is not evaluation. Completion is not approval. Task failure is not semantic drift.**

## Why this contract exists

A Seed acceptance criterion can produce at least two different runtime artifacts:

1. A **worker task** derived from the AC. This task can complete, fail, block, or be skipped while the worker is trying to produce an artifact.
2. A **formal AC verdict** produced by an evaluator or verifier. This verdict decides whether the resulting artifact satisfies the acceptance criterion.

Those two states answer different questions.

| Question | Contract surface | Example states |
|---|---|---|
| Did the worker finish the assigned execution unit? | `TaskResult` / task progress | `completed`, `failed`, `blocked`, `skipped` |
| Did the artifact satisfy the acceptance criterion? | `ACResult` / evaluator verdict | `pass`, `fail`, `not_evaluated` |
| Did the artifact drift from the Seed intent? | semantic evaluation / drift signal | `drift_score`, drift alerts |

A completed task is only evidence that execution finished. It is not proof that the AC passed.
A failed task is only evidence that execution did not finish. It is not proof of semantic drift.

## Terminology rules

Use these terms consistently in reports, TUI surfaces, events, and docs.

| Use this | For | Do not use it for |
|---|---|---|
| **task** / **subtask** | Worker execution units derived from ACs | Formal acceptance verdicts |
| **completed** / **failed** | Worker execution outcomes | Evaluator approval |
| **acceptance criterion** / **AC** | User-facing success criteria | Internal worker task status |
| **pass** / **fail** | Formal evaluator or verifier verdicts | Worker completion status |
| **drift** / `drift_score` | Semantic divergence from Seed intent | Mechanical task completion ratio |

## Data model boundary

The shared model boundary should keep these surfaces separate:

- `TaskResult` records worker execution outcomes.
- `ACResult` records formal evaluator/verifier verdicts.
- `EvaluationSummary.task_results` contains execution outcomes.
- `EvaluationSummary.ac_results` contains formal AC verdicts.
- `EvaluationSummary.drift_score` is set only when semantic drift evaluation actually ran.

A cheap mechanical execution-completion ratio may be useful as `score`, but it must not synthesize `drift_score`.

## Legacy report compatibility

Older parallel execution reports may render worker completion as:

```text
### AC 1: [PASS] Implement feature
### AC 2: [FAIL] Add tests
```

That legacy syntax remains parseable for backward compatibility, but it should be interpreted as worker task completion:

```text
Task 1: completed
Task 2: failed
```

It should not directly populate formal `ACResult` verdicts.

Formal AC verdicts should come from explicit evaluation or verification. If a verifier only covers a subset of expected ACs, the missing ACs are not approved. They remain `not_evaluated` until a formal verdict exists; if an evaluator or verifier explicitly checks an AC and finds it unsatisfied, record `fail`.

## Reporting guidance

Execution surfaces should prefer task language:

```text
Task Execution Progress: 2/3 completed
Task 1: completed
Task 2: failed
Task 3: completed
```

Evaluation surfaces should prefer AC verdict language:

```text
AC Verdicts: 2/3 passed
AC 1: pass
AC 2: fail
AC 3: pass
```

Combined summaries should show both dimensions instead of collapsing them:

```text
Execution: completed
AC verdict: not_evaluated
Run verdict: FAIL
```

or:

```text
Execution: completed
AC verdict: pass
Run verdict: PASS
```

## Migration guidance for maintainers

When migrating a surface that currently uses AC pass/fail wording for worker execution:

1. Keep legacy parsing backward-compatible.
2. Change newly generated worker reports to task/subtask wording.
3. Store worker outcomes in `task_results` or equivalent.
4. Reserve `ac_results` for formal evaluator/verifier output.
5. Do not set `drift_score` unless semantic drift evaluation ran.
6. Add tests showing task completion does not imply AC approval.
7. Add tests showing partial verifier coverage cannot approve a run.

## Related work

- #608 tracks the repository-wide contract split.
- #613 starts the model and MCP-adapter boundary migration.
- Follow-up PRs should migrate UI/HUD/job-monitor/event/docs terminology without breaking legacy report parsing.


---
<!-- page: docs/guides/safe-but-wrong-output.md -->

# Safe-but-wrong output failure mode

## Summary

A run can be safe, non-destructive, and even useful, while still being wrong for
the user's stated goal.

This document names that failure mode so `ooo auto`, interview, Seed review, and
QA can discuss it directly.

## Definition

A **safe-but-wrong output** happens when the system produces an artifact that is
locally safe and verifiable, but changes a material user-stated requirement.

Common examples:

- user asks for an executable tool, but the run produces only handoff docs;
- user asks for a reusable workflow, but the run produces a one-off checklist;
- user asks for a batch surface, but the run produces a single-case summary;
- user asks to preserve a legacy behavior, but the run creates a new adjacent
  helper that does not cover that behavior;
- missing input data is represented as `OK`, `0`, or empty instead of
  `insufficient data` / `unchecked`.

The key property is that ordinary safety checks may pass. No files were deleted,
no external system was mutated, tests may pass, and the output may be readable.
It is still wrong because the artifact contract drifted.

## Why it matters

Ouroboros focuses on specification-first development. If the Seed or interview
lets a safe-but-wrong artifact class replace the user's goal, later execution can
look successful while solving the wrong problem.

That is worse than a clear blocker because it creates false confidence.

## Detection checklist

Before calling a run complete, compare the produced artifact against the original
contract:

1. **Artifact class** — Did the user ask for code, CLI, web, workflow, document,
   report, dataset, or another specific output type?
2. **Execution surface** — If the user asked for a repeatable tool, can it be run
   again with a new input?
3. **Supporting outputs** — Are checklists, summaries, docs, or handoff packs
   being represented as the final product when they were only supporting outputs?
4. **Missing data semantics** — Are unknowns clearly labeled as missing,
   insufficient, unchecked, or blocked?
5. **User corrections** — Did the user previously correct the same scope or
   artifact assumption?
6. **Verification evidence** — Did verification prove the requested behavior, or
   only prove that some file exists?

## Recommended response

When safe-but-wrong drift is detected, do not continue execution as if the Seed is
valid.

Prefer one of these outcomes:

- **block** if the final artifact class changed without user authority;
- **ask for confirmation** if the user may intentionally want the narrower scope;
- **regenerate the Seed** if the current Seed encoded the wrong artifact;
- **mark the output as supporting material only** if it is useful but not final.

## Example status language

Good:

```text
Generated supporting handoff docs, but the requested CLI/web artifact was not
built. Status: partial/supporting-output, not complete.
```

Bad:

```text
Done. Created the handoff package.
```

## Relationship to other contracts

This failure mode is related to:

- interview convergence;
- intent preservation;
- Seed QA;
- TraceGuard evidence;
- `ooo auto` final status reporting.

It does not require blocking all conservative defaults. A conservative default is
fine when it fills a local reversible gap. It becomes unsafe when it changes what
kind of thing the user asked to receive.


---
<!-- page: docs/hidden-checklist-convergence/requirements.md -->

# Hidden-Checklist Convergence Requirements

> 中文说明：[README.zh-CN.md](./README.zh-CN.md)

> Generated: 2026-08-07
> Status: Implemented

## Original Request

Turn one-shot `ooo run` execution into a bounded convergence chain while keeping
harness-owned grading inputs hidden from implementation workers. Failed but
evaluable runs proceed through formal evaluation and focused Ralph evolution;
the preceding verdict remains authoritative if successor chaining fails.

## Clarified Specification

- Hide every harness-owned `verify_command` and `output_assertion` from every
  Ouroboros-transported worker prompt, context, event, artifact, and retry
  surface without a configuration escape hatch. This contract does not claim
  to sandbox independently accessible raw Seed files.
- Build retry guidance from missing artifacts, sanitized verification output,
  and read-only worker tool/file evidence.
- Formally evaluate completed runs even when AC execution failed, provided an
  evaluable session/artifact exists.
- On explicit evaluation rejection, deterministically project the Seed and
  checklist into generation 1 and delegate convergence to Ralph.
- Preserve fail-open chaining: enqueue/parsing failures never change the run or
  evaluation verdict that preceded them.
- Avoid a second Ralph lineage inside `ooo auto`, which already owns its own
  RALPH_HANDOFF loop.

## Success Criteria

- Hidden contract strings do not appear in worker prompts.
- Run → evaluate → Ralph job IDs are transitively observable.
- Gen1 replay has `lineage.created` plus `lineage.generation.completed`, and the
  next planned generation is 2.
- Concurrent or replayed evaluation completions publish Gen1 and enqueue at most
  one Ralph successor; active and terminal successors are reattached by lineage.
- The resolved Ralph generation budget is snapshotted at evaluation enqueue and
  remains authoritative across configuration changes and successor replay.
- The resolved automatic-evolution enable/disable decision is part of the
  detached evaluation request and cannot flip when configuration changes.
- Approved/unjudged/opted-out evaluations do not enqueue Ralph.
- Static checks and the bounded target test suites pass.
- Builtin runtimes retain and can deterministically close the configured
  composition owner; backend handle aliases do not cause nested runtime creation.


---
<!-- page: docs/hidden-checklist-convergence/architecture.md -->

# Hidden-Checklist Convergence Architecture

> 中文说明：[README.zh-CN.md](./README.zh-CN.md)

> Generated: 2026-08-07
> Approach: Pragmatic reuse of existing evaluation and Ralph owners

## Data Flow

```text
start_execute_seed
  -> execute result (success or evaluable failure)
  -> start_evaluate (30 minute bound)
  -> approved: terminal
  -> rejected: checklist -> EvaluationSummary -> Gen1 lineage events
  -> start_ralph(lineage continuation, max_generations=3 by default)
```

## Components

| Component | Responsibility | Location |
|---|---|---|
| Assertion-safe contract prompt | Show artifact obligations while hiding grader inputs | `src/ouroboros/orchestrator/atomic_prompt_builder.py` |
| Retry hint builder | Sanitize harness output and summarize worker trace facts | `src/ouroboros/orchestrator/retry_hints.py` |
| Evaluation/Ralph bridge | Convert checklist verdicts and seed Gen1 idempotently | `src/ouroboros/mcp/tools/evaluate_ralph_chain.py` |
| Evaluation terminal hook | Enqueue or reconnect Ralph after explicit rejection | `src/ouroboros/mcp/tools/evaluation_handlers.py` |
| Execution chain | Evaluate completed success/failure runs | `src/ouroboros/mcp/tools/execution_handlers.py` |
| Plugin Seed vault | Keep the raw Seed parent-owned and give workers only an opaque, session-bound handle | `src/ouroboros/mcp/tools/seed_handoff.py` |
| Runtime composition adapter | Reuse the production handler graph for builtin runtime interception and retain its explicit resource owner | `src/ouroboros/mcp/tools/runtime_tool_composition.py` |

## Key Decisions

| Decision | Rationale |
|---|---|
| No answer-key configuration knob | Hidden grading is a correctness boundary, not a tuning option. |
| Manifest is read-only coaching input | Retry quality improves without allowing evidence to affect the deliver verdict. |
| Ralph owns convergence | Avoids duplicating loop termination, focus, and budget logic. |
| Deterministic lineage ID | A 120-bit digest of the complete Seed/run tuple fits the event store's 36-character aggregate-ID contract. |
| Durable lineage claims | Cross-process retries elect one Gen1 writer and one Ralph successor owner. |
| Atomic Gen1 publication | The creation and generation-completed events commit together; legacy creation-only state is repaired under the same claim. |
| Terminal successor recovery | Retries reconnect to both active and terminal Ralph jobs, closing the enqueue/result crash gap. |
| Single-AC checklist absence yields no fabricated AC result | Existing full-graph focus fallback remains honest and safe. |
| Raw Seed handoff is process-local | Persisting hidden verifier material in worker-queryable events would defeat the boundary. A server restart invalidates the opaque handle and evaluation fails closed instead of exposing the Seed. |
| Runtime owns the full embedded composition | Handler registries retain their MCP server owner and expose deterministic shutdown, so EventStore, ControlBus, and bridge lifetimes match the builtin runtime instead of an abandoned factory local. |
| Confidentiality is a transport boundary | Worker prompts, contexts, events, artifacts, and retries are sanitized. Filesystem isolation is an operator/runtime sandbox responsibility when raw Seed files are stored in worker-accessible locations. |


---
<!-- page: docs/contributing/verifier-evidence-policy.md (excerpts) -->

# Verifier Evidence Policy

This policy governs fixes to the atomic verifier and fat-harness evidence
boundary.

The core verifier must stay domain- and language-agnostic. It decides whether
typed evidence is backed by the runtime transcript. It must not grow bespoke
parsers for each test runner, language ecosystem, framework, or report format.

## Core rule

When valid work appears to be rejected, first classify the failure shape:

| Shape | Meaning | Correct direction |
| --- | --- | --- |
| No runtime transcript evidence exists for the claim | The claim may be fabricated. | Keep or use `FABRICATION_SUSPECTED`. |
| Related runtime work exists, but the evidence form cannot prove the claim | The evidence contract is mismatched. | Use `EVIDENCE_FORM_MISMATCH` with retry guidance. |
| The evidence needs runner-specific interpretation | The core verifier is the wrong layer. | Add a profile/adapter-level contract or require a runner-agnostic proof form. |


## Failure class semantics

`FABRICATION_SUSPECTED` is reserved for claims with no supporting runtime event
or artifact reference. It should not be used when the transcript clearly shows
related work but the evidence shape is contract-incompatible.

`EVIDENCE_FORM_MISMATCH` means:

- related runtime work is visible;
- the current evidence form cannot prove the typed claim;
- retrying with a contract-compliant proof form is reasonable;
- the verifier must still reject the claim until that proof form exists.

This distinction keeps issue triage honest: the implementer did not necessarily
invent work, but the harness still cannot accept the evidence.



---
<!-- page: https://ouroboros.page/roadmap/ (text) -->

Evidence-gated go-to-market roadmap

# Multiple runtimes.
Expansion earned by evidence." data-ko="하나의 워크플로.
여러 실행 환경.
확장은 증거로 얻습니다.">One workflow.
Multiple runtimes.
Expansion earned by evidence.

  AbstractOuroboros turns ambiguous intent into an approved specification, an evaluated result, and reusable operating assets. This roadmap describes how that workflow moves from an open-source engine and public product surfaces to runtime partnerships and, only after field evidence, enterprise delivery.

  Verified evidencePlanned validationProposed / conditionalNo calendar promises

  00
## Decision brief
A proposal for a controlled Kiro validation, not an open-ended sponsorship.

### Decision requested
Nominate a Kiro technical counterpart and agree to scope one user situation, one representative task, and one twice-run pilot.

### Bounded support
Integration review, controlled usage credits, access to an agreed user cohort, and joint evidence review.

#### Go / no-go gate
Proceed only if the user approves the Seed, the result passes predeclared criteria, the second run reuses prior assets without rebuilding context or procedure, completed requirements remain intact, repeat-use intent appears, and intervention and operating cost can be recorded.

#### Owners and review
Sergio is the proposed Ouroboros owner for implementation and measurement. AWS/Kiro would nominate one counterpart for platform review and pilot access. Public claims require mutual written approval.

  01
## The commercial thesis
The product is the specification-and-evaluation workflow. Platforms are distribution and execution surfaces, not the identity of the product.

    I
### Clarity before execution
The system does not build until the user's intent is explicit enough to become a specification.

    II
### Criteria before approval
A result is judged against declared acceptance criteria, not against whether it merely looks convincing.

    III
### Assets after every loop
Each cycle leaves a Seed, workflow, evaluation record, and lineage that can reduce repeated explanation and setup.

  02
## The invariant workflow
The loop remains stable while the execution environment changes.

    InterviewExpose intent and ambiguity
SeedFreeze the approved specification
ExecutePerform the declared work
EvaluateTest against measurable criteria
EvolveFeed evidence into the next Seed

    ↺ evaluation evidence returns to the next Seed

    Seedcanonical intent
Workflowrepeatable route
Evaluationdecision evidence
Lineagechange history

  03
## Roadmap by evidence, not dates
Each horizon opens only when the preceding evidence exists. Sequence is intentional; timing is not promised.

  VerifiedPlanned validationProposed / conditional

    1
FoundationVerified

### Open engine and multi-runtime execution
The workflow exists as an open-source engine with runtime integrations, including Kiro among the supported environments.
Specification-first core
Evaluation and lineage primitives
Runtime-independent product thesis
Public source and release history

    2
Public proofPlanned validation

### Agree the first pilot contract, then validate public reach
The canonical current gate is to define one user situation, one representative task, a baseline, and observable success and failure criteria. ChatGPT Hosted entry is planned; official directory submission and external activation remain unverified.
First user situation and representative task
One complete user workflow
Second-run reuse evidence
Operating cost and human intervention record

    3
Runtime partnershipsConditional

### Co-validate the same workflow inside partner environments
The proposal for AWS and Kiro is a bounded joint validation: prove that specification quality and evaluation discipline improve completion inside Kiro without making Ouroboros dependent on one platform.
Reference integration
Joint user pilot
Usage credit for controlled testing
Evidence-led case study

    4
Enterprise deliveryConditional

### Add control only when real customers require it
Self-hosting, compliance controls, and service commitments remain candidates until field demand and willingness to pay are observed.
Data-boundary requirements
Audit and approval controls
Service-level requirements
Repeatable deployment economics

    5
Workflow economyConditional

### Distribute workflows only after portability is proven
A marketplace is considered only after workflows are accumulated, reused, and shown to transfer beyond a single user's context.
Portable domain workflows
Third-party contribution controls
Measured reuse
Sustainable distribution model

  04
## What is true now
Claim status is part of the product. Verified facts, active work, and conditional plans are never blended.

  ClaimStatusEvidence / gate

  Ouroboros workflow engineVerifiedPublic source, releases, interview, Seed, execution, evaluation, and evolution primitives.

  Multi-runtime support, including KiroVerifiedRecorded in the GTM canonical technical inventory; partnership is not implied.

  ChatGPT Hosted entryPlannedThe canonical GTM gate is 0/3: submission contract, official directory submission, and first external activation remain unverified.

  AWS / Kiro joint programProposalRequires partner agreement, a bounded pilot, named resources, and shared success criteria.

  Enterprise and marketplace offeringsConditionalRequire observed demand, workflow reuse, control requirements, and viable operating economics.

  05
## A bounded proposal for AWS and Kiro
The ask is not generic sponsorship. It is a proposed controlled validation intended to produce implementation evidence, user evidence, and a publishable decision.

### Joint work
Define one Kiro user situation and one representative task.
Connect the Ouroboros Interview–Seed–Evaluate loop without platform lock-in.
Run the task twice to test reuse, not only first-run completion.
Publish findings only after both parties approve the evidence.

### Requested support
A technical counterpart for Kiro integration review
Controlled usage credits for the pilot
Access to an agreed pilot user cohort
A joint review of the resulting case study

#### Ouroboros contributes
The open workflow engine, the integration boundary, pilot instrumentation, evaluation design, and maintainership.

#### The partnership should produce
A reproducible integration, measured user evidence, an explicit go/no-go decision, and a jointly approved public narrative.

  06
## Success is observed, then priced
No unsupported targets are published. The pilot first defines how each signal is measured; target values follow observed baselines.

  CompletionDid the task satisfy every declared specification item and pass verification?PreservationDid the second run preserve what was already complete?ReuseDid the next run use the previous Seed and workflow without rebuilding context and procedure?Delegated timeHow much agreed manual work did the workflow replace?Human interventionWas intervention an expected approval point or repeated reconstruction?Operating costCan runtime, support, and maintenance cost be attributed per workflow?

  07
## Publication and negotiation policy
Conservative language protects both the product and the counterparty.

### We will
Label every claim as verified, active, proposed, or conditional.
Link expansion to a measurable gate.
Keep Ouroboros independent of any one model, runtime, or cloud.
Seek mutual review before publishing partner claims.

### Not Todo
No invented launch dates, market sizes, savings, or adoption numbers.
No implication of OpenAI, AWS, or Kiro approval, sponsorship, or endorsement.
No enterprise security, compliance, SLA, or self-hosting promise before requirements are contracted.
No marketplace timeline before workflow portability is demonstrated.
No token economics, cryptocurrency narrative, or speculative fundraising language.

  08
## Sources and status note

  Product philosophy, workflow, success measures, and roadmap gates follow the canonical Ouro-labs GTM repository.
Open-source implementation evidence is maintained in Q00/ouroboros.
Platform and partner names identify compatibility or a proposed validation surface. They do not imply endorsement or a commercial relationship.
This public roadmap is a decision framework, not a commitment to ship on a fixed date.
