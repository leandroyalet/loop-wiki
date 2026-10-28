#!/usr/bin/env bash
# Build wiki/ into a static site in public/, using Quartz as external tooling.
# Quartz is cloned at a pinned tag into .quartz-build/ (gitignored); this repo only
# keeps its config (.site/quartz.config.yaml) and plugin lockfile (.site/quartz.lock.json).
#
# Usage: .site/build.sh            build into public/
#        .site/build.sh --serve    local preview with live reload (extra args go to `quartz build`)
set -euo pipefail

QUARTZ_REF="${QUARTZ_REF:-v5.0.0}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$ROOT/.quartz-build"
QUARTZ="$WORK/quartz"
# Staged outside the repo: Quartz skips anything gitignored, and .quartz-build/ is.
STAGE="$(mktemp -d)"
CONTENT="$STAGE/content"
trap 'rm -rf "$STAGE"' EXIT

mkdir -p "$WORK"

# 1. Fetch and install Quartz, only when the pinned ref changed.
if [[ "$(cat "$WORK/ref" 2>/dev/null)" != "$QUARTZ_REF" ]]; then
  rm -rf "$QUARTZ"
  git clone --quiet --depth 1 --branch "$QUARTZ_REF" https://github.com/jackyzha0/quartz.git "$QUARTZ"
  (cd "$QUARTZ" && npm ci --no-audit --no-fund)
  echo "$QUARTZ_REF" > "$WORK/ref"
fi

# 2. Apply our config and restore plugins to the commits in our lockfile.
cp "$ROOT/.site/quartz.config.yaml" "$ROOT/.site/quartz.lock.json" "$QUARTZ/"
(cd "$QUARTZ" && npx quartz plugin restore)

# 3. Stage a web copy of the wiki (homepage swap, titles), then build.
python3 "$ROOT/.site/stage_content.py" "$ROOT/wiki" "$CONTENT"
(cd "$QUARTZ" && npx quartz build -d "$CONTENT" -o "$ROOT/public" "$@")
