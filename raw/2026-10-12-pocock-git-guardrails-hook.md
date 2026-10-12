---
title: "This Hook Stops Claude Code Running Dangerous Git Commands"
url: https://www.aihero.dev/this-hook-stops-claude-code-running-dangerous-git-commands
author: Matt Pocock
published: 2026-02-10
fetched: 2026-10-12
extraction: "trafilatura HTML→markdown (recall mode); code blocks lost line breaks; diagrams not captured"
---

> Raw source. Immutable; do not edit. Summary lives in the wiki under sources/.

# This Hook Stops Claude Code Running Dangerous Git Commands

Learn how to block dangerous git commands in Claude Code using a PreToolUse hook. Prevent accidental data loss with git guardrails.

## On this page

I've put together a skill to allow you to prevent Claude code from ever running dangerous git commands. Add it via `npx skills add`:

npx skills add mattpocock/skills/skills/misc/git-guardrails-claude-code

Claude will guide you through the setup - choose whether to install it for your current project or globally across all projects, then customize which git commands you want to block.

## [Why This Skill Exists](https://www.aihero.dev#why-this-skill-exists)

### [The Docker Sandbox Story](https://www.aihero.dev#the-docker-sandbox-story)

I've been experimenting with [Ralph-style workflows](https://www.aihero.dev/getting-started-with-ralph) recently, and the most powerful way I've found to get Claude to run autonomously is via [Docker Sandbox](https://docs.docker.com/ai/sandboxes/).

It lets Claude Code run in YOLO without asking permission for every command. And it protects your system by running it inside a microVM. You can let your agent work unattended while you check in every few minutes.

The tradeoff? Docker [Sandbox](https://www.aihero.dev/ai-coding-dictionary/sandbox) doesn't restrict *what* commands Claude can run, it just isolates *where* they run.

### [The Gap Docker Sandbox Leaves](https://www.aihero.dev#the-gap-docker-sandbox-leaves)

Here's the problem: your git history lives inside that sandboxed folder.

Docker Sandbox prevents Claude from reaching outside the project directory, but it can't stop Claude from running destructive git commands *within* that directory. A single `git reset --hard` or `git push --force` can wipe out weeks of work.

This skill fills that gap with a hard guardrail - preventing Claude Code from running dangerous commands.

## [What Gets Blocked](https://www.aihero.dev#what-gets-blocked)

The skill blocks these dangerous patterns by default:

- `git push` (all variants, including `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

These aren't "never allow" rules, they're "safe by default" rules.

You can customize the blocked patterns during installation, or edit them anytime. If your workflow legitimately needs Claude to push to a remote PR, you can allow it.

## [How It Works: The Hook System](https://www.aihero.dev#how-it-works-the-hook-system)

The skill uses a `PreToolUse` hook that intercepts bash commands before Claude executes them.

Here's the filtering script:

#!/bin/bashINPUT=$(cat)COMMAND=$(echo "$INPUT" | jq -r '.tool\_input.command')DANGEROUS\_PATTERNS=("git push""git reset --hard""git clean -fd""git clean -f""git branch -D""git checkout \.""git restore \.""push --force""reset --hard")for pattern in "${DANGEROUS\_PATTERNS\[@\]}"; doif echo "$COMMAND" | grep -qE "$pattern"; thenecho "BLOCKED: '$COMMAND' matches dangerous pattern '$pattern'. The user has prevented you from doing this." >&2exit 2fidoneexit 0

The script reads the incoming command, checks it against the danger list, and blocks execution if it matches.

### [What Claude Sees](https://www.aihero.dev#what-claude-sees)

When Claude tries to run a blocked command, it sees a clear message:

BLOCKED: 'git push origin main' matches dangerous pattern 'git push'.The user has prevented you from doing this.

Claude understands the constraint and adapts. It's a hard guardrail, not a suggestion buried in prose.

## [Verify It's Working](https://www.aihero.dev#verify-its-working)

After installation, test the guardrail:

1. Clear your conversation context
2. Ask Claude to run `git push`
3. Watch it fail and see the blocked message

This confirms the hook is active and Claude can't accidentally bypass it.

## [Conclusion](https://www.aihero.dev#conclusion)

Enjoy! These kinds of skills are great fun to put together, and if you're looking for more of them, join my newsletter.