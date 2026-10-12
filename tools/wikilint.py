#!/usr/bin/env python3
"""Mechanical lint for the wiki: broken links, orphans, index coverage, frontmatter.

Usage: python3 tools/wikilint.py [wiki_dir]
Exits non-zero if any problem is found.
"""
import re
import sys
from pathlib import Path

REQUIRED_KEYS = ("type", "branch", "tags", "sources", "created", "updated", "status")
NO_FRONTMATTER = {"index", "log"}
NO_INBOUND_NEEDED = {"loop-engineering", "index", "log"}
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def frontmatter_keys(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return {line.split(":", 1)[0].strip() for line in text[4:end].splitlines() if ":" in line and not line.startswith(" ")}


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "wiki")
    pages = {}
    for path in sorted(root.rglob("*.md")):
        if path.stem in pages:
            print(f"DUPLICATE  {path.relative_to(root)} (name clashes with {pages[path.stem].relative_to(root)})")
        pages[path.stem] = path

    problems = 0
    inbound = {name: set() for name in pages}
    index_links = set()

    for name, path in pages.items():
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(CODE_RE.sub("", text)):
            target = target.strip()
            if target not in pages:
                print(f"BROKEN     {path.relative_to(root)} -> [[{target}]]")
                problems += 1
            elif target != name:
                inbound[target].add(name)
                if name == "index":
                    index_links.add(target)

        if name not in NO_FRONTMATTER:
            keys = frontmatter_keys(text)
            if keys is None:
                print(f"NO-FM      {path.relative_to(root)}")
                problems += 1
            elif missing := [k for k in REQUIRED_KEYS if k not in keys]:
                print(f"FM-MISSING {path.relative_to(root)}: {', '.join(missing)}")
                problems += 1

    for name, sources in sorted(inbound.items()):
        if name in NO_INBOUND_NEEDED:
            continue
        if not sources - {"index"}:
            print(f"ORPHAN     {pages[name].relative_to(root)} (no inbound links besides index)")
            problems += 1
        if name not in index_links:
            print(f"UNINDEXED  {pages[name].relative_to(root)}")
            problems += 1

    print(f"\n{len(pages)} pages, {problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
