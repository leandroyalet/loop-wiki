---
title: "Here's How To Stream Claude Code With AFK Ralph"
url: https://www.aihero.dev/heres-how-to-stream-claude-code-with-afk-ralph
author: Matt Pocock
published: 2026-01-22
fetched: 2026-10-12
extraction: "trafilatura HTML→markdown (recall mode); code blocks lost line breaks; diagrams not captured"
---

> Raw source. Immutable; do not edit. Summary lives in the wiki under sources/.

# Here's How To Stream Claude Code With AFK Ralph

Stream Claude code in real-time while running AFK Ralph. Learn how to use jq to get visibility into Claude's output instead of staring at a blank screen.

## On this page

This guide is for people who've tried Ralph with Claude Code and hit that frustration point: running the [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) script and ending up staring at a blank screen.

If you've never heard of Ralph, start here:

## [The Problem: A Blank Screen](https://www.aihero.dev#the-problem-a-blank-screen)

When you want Ralph to run while you're away from your keyboard, you might use a script like this:

#!/bin/bashset -eif \[ -z "$1" \]; thenecho "Usage: $0 \<iterations>"exit 1fifor ((i=1; i\<=$1; i++)); doresult=$(docker sandbox run --credentials host claude \--print \"\<your prompt here>")if \[\[ "$result" == \*"\<promise>COMPLETE\</promise>"\* \]\]; thenecho "Ralph complete after $i iterations."exit 0fidone

The issue here is frustrating: when you run Claude with the `--print` flag, you get zero streaming output. Your terminal goes blank.

You walk away, and you have absolutely no idea what's happening. Is Claude working? Is it stuck? Did something break? You won't know until it's finished.

The dream with AFK Ralph is to get the best of both worlds: you want real-time visibility into what Claude is doing, but you also want to leave it running while you step away.

## [The Solution: Streaming with jq](https://www.aihero.dev#the-solution-streaming-with-jq)

Claude can output `stream-json` format, which gives you every single message as it happens. But that output is extremely verbose and unreadable.

By combining `stream-json` with `jq` filtering, you can extract just the useful information and stream it to your terminal in real-time. At the same time, you capture the final result to check for the `<promise>COMPLETE</promise>` marker.

Here's the complete script:

#!/bin/bashset -eif \[ -z "$1" \]; thenecho "Usage: $0 \<iterations>"exit 1fi# jq filter to extract streaming text from assistant messagesstream\_text='select(.type == "assistant").message.content\[\]? | select(.type == "text").text // empty | gsub("\n"; "\r\n") | . + "\r\n\n"'# jq filter to extract final resultfinal\_result='select(.type == "result").result // empty'for ((i=1; i\<=$1; i++)); dotmpfile=$(mktemp)trap "rm -f $tmpfile" EXITdocker sandbox run --credentials host claude \--verbose \--print \--output-format stream-json \"\<your prompt here>" \| grep --line-buffered '^{' \| tee "$tmpfile" \| jq --unbuffered -rj "$stream\_text"result=$(jq -r "$final\_result" "$tmpfile")if \[\[ "$result" == \*"\<promise>COMPLETE\</promise>"\* \]\]; thenecho "Ralph complete after $i iterations."exit 0fidone

This script accepts one argument: the number of iterations to run.

## [Walking Through the Script Structure](https://www.aihero.dev#walking-through-the-script-structure)

### [Breaking Down the Stream Filter](https://www.aihero.dev#breaking-down-the-stream-filter)

The stream filter does several important things:

1. **Selects assistant messages**: `select(.type == "assistant")` grabs only Claude's responses
2. **Extracts text content**: `.message.content[]? | select(.type == "text").text` pulls out just the text portions
3. **Fixes line endings**: `gsub("\n"; "\r\n")` replaces newlines with carriage return + newline
4. **Adds spacing**: `. + "\r\n\n"` inserts extra space between messages

The carriage return replacement fixes a bug where the cursor wasn't returning to the first character of the line properly.

### [The Data Pipeline](https://www.aihero.dev#the-data-pipeline)

Here's how data flows through the script:

Docker streams out `stream-json` formatted data, but it includes some non-JSON lines just for noise. The `grep --line-buffered '^{'` filter ensures only valid JSON lines get processed.

The `tee "$tmpfile"` command writes everything to a temporary file without stopping the stream. You need this file later to check if Claude has finished.

Finally, `jq --unbuffered -rj "$stream_text"` applies the streaming filter and displays the text in real-time to your terminal.

## [Conclusion](https://www.aihero.dev#conclusion)

My hope is that relatively soon I'll be able to delete this article because Claude Code will have shipped a feature that allows you to stream the responses while still capturing the final output.

OpenCode already has this, and so there's no need to write an article like this for OpenCode. But until then, this is a workable solution to get real-time streaming output from Claude while running AFK Ralph.