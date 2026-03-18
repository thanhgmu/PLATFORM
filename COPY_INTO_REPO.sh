#!/bin/sh
set -e

if [ -z "$1" ]; then
  echo "Usage: bash COPY_INTO_REPO.sh /path/to/PLATFORM"
  exit 1
fi

TARGET="$1"
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if [ ! -d "$TARGET/.git" ]; then
  echo "Target does not look like a git repo: $TARGET"
  exit 1
fi

rsync -av   --exclude '.git'   --exclude 'PLATFORM_step6b_update_pack.zip'   --exclude 'COPY_INTO_REPO.sh'   "$SCRIPT_DIR/" "$TARGET/"

echo "[OK] Step 6B files copied into $TARGET"
