#!/bin/sh
set -eu

# Read-only report for Cargo output. It intentionally does not invoke Cargo,
# because a Cargo command can create or grow the very cache being inspected.

target_path=${1:-}

if [ -z "$target_path" ]; then
  if [ -n "${CARGO_TARGET_DIR:-}" ]; then
    target_path=$CARGO_TARGET_DIR
  else
    target_path=target
  fi
fi

case "$target_path" in
  /*) ;;
  *) target_path=$(pwd)/$target_path ;;
esac

printf '%s\n' "Cargo target report (read-only)"
printf 'target-dir: %s\n' "$target_path"

if [ -e "$target_path" ]; then
  du -sh "$target_path"
else
  printf '%s\n' 'size: absent'
  exit 0
fi

for entry in debug release doc package; do
  if [ -e "$target_path/$entry" ]; then
    du -sh "$target_path/$entry"
  fi
done

printf '%s\n' 'largest immediate children:'
du -sh "$target_path"/* 2>/dev/null | sort -h | tail -12 || true

for path in \
  "$target_path/debug/deps" \
  "$target_path/debug/incremental" \
  "$target_path/debug/build" \
  "$target_path/release/deps" \
  "$target_path/release/build"; do
  if [ -e "$path" ]; then
    du -sh "$path"
  fi
done

printf '%s\n' 'active build processes:'
ps aux | grep -E '(^|[[:space:]/])(cargo|rustc|rustdoc|ld|clang)([[:space:]]|$)' || true
