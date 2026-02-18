#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ORG_DIR="${ORG_DIR:-/Users/jzhong/sDrive/Jie/course-materials/reveal-slides-work/org-files}"
RE_REVEAL_PATH="${RE_REVEAL_PATH:-$HOME/.emacs.d/.local/straight/repos/org-re-reveal}"

if [[ ! -d "$ORG_DIR" ]]; then
  echo "ORG_DIR not found: $ORG_DIR" >&2
  exit 1
fi

cd "$REPO_ROOT"
count=0
for f in "$ORG_DIR"/*.org; do
  [[ -f "$f" ]] || continue
  emacs --batch \
    -l "$REPO_ROOT/scripts/reveal-export.el" \
    "$f"
  count=$((count+1))
done

echo "Exported $count org files from $ORG_DIR"
