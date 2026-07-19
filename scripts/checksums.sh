#!/bin/sh
# Generate SHA-256 checksums for the published data artifacts.
#
# Writes checksums.txt at the repository root in the standard `sha256sum`
# format (one "<hash>  <path>" line per file), so it can be verified with:
#
#     sha256sum -c checksums.txt
#
# Run from anywhere; paths are resolved relative to the repository root.
set -eu

# Resolve the repository root (parent of this script's directory).
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
cd "$ROOT"

OUT="checksums.txt"

FILES="data/ai-glasses.json data/ai-glasses.csv data/sources.json schema/ai-glasses.schema.json"

# Fail early if any expected file is missing.
for f in $FILES; do
    if [ ! -f "$f" ]; then
        echo "ERROR: missing file: $f" >&2
        exit 1
    fi
done

sha256sum $FILES > "$OUT"

echo "Wrote $ROOT/$OUT:"
cat "$OUT"
