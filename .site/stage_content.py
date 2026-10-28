#!/usr/bin/env python3
"""Copy wiki/ into a Quartz content folder, adapting it for the web without touching the vault.

Usage: python3 .site/stage_content.py <wiki_dir> <out_dir>

- The root hub (loop-engineering.md) becomes the homepage (index.md); the old URL redirects to it.
- The catalog (index.md) moves to catalog.md.
- Wikilinks to both pages are rewritten to match.
- Each page's first H1 becomes its `title:` and is removed from the body, so Quartz
  shows the real title once instead of the filename plus a duplicate heading.
"""
import json
import re
import shutil
import sys
from pathlib import Path

RENAMES = {"index": "catalog", "loop-engineering": "index"}
LINK_RE = re.compile(r"\[\[(index|loop-engineering)(#[^\]|\\]*)?(\\?\|[^\]]*)?\]\]")
H1_RE = re.compile(r"^# (.+)\n+", re.M)


def relink(line):
    """Point links at the renamed pages, keeping the original name as visible text."""
    pipe = "\\|" if line.lstrip().startswith("|") else "|"

    def sub(m):
        name, anchor, alias = m.group(1), m.group(2) or "", m.group(3)
        return f"[[{RENAMES[name]}{anchor}{alias or pipe + name}]]"

    return LINK_RE.sub(sub, line)


def stage(text, extra_props):
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        props, body = text[4:end].split("\n"), text[end + 5:]
    else:
        props, body = [], text
    if match := H1_RE.search(body):
        props.insert(0, f"title: {json.dumps(match.group(1).strip())}")
        body = body[:match.start()] + body[match.end():]
    props += extra_props
    body = "".join(relink(line) for line in body.splitlines(keepends=True))
    return "---\n" + "\n".join(props) + "\n---\n" + body


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(src, out)
    (out / "index.md").rename(out / "catalog.md")
    (out / "loop-engineering.md").rename(out / "index.md")
    for path in out.rglob("*.md"):
        extra = ["aliases: [loop-engineering]"] if path == out / "index.md" else []
        path.write_text(stage(path.read_text(encoding="utf-8"), extra), encoding="utf-8")


if __name__ == "__main__":
    main()
