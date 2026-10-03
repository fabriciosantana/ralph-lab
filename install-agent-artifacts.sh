#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${AGENT_ARTIFACTS_HOME:-$HOME/.agent-artifacts}"
MARKER="# managed-by-ralph-lab"
mkdir -p "$TARGET/hooks" "$TARGET/skills/evidence"
cp "$ROOT/AGENTS.md" "$TARGET/AGENTS.md"
cp "$ROOT/hooks/pretooluse-hook.sh" "$ROOT/hooks/posttooluse-hook.sh" "$TARGET/hooks/"
cp "$ROOT/skills/evidence/SKILL.md" "$TARGET/skills/evidence/"
if [ -f "$TARGET/settings.json" ]; then
  if grep -q "$MARKER" "$TARGET/settings.json"; then echo "already installed: settings marker present"; else cp "$TARGET/settings.json" "$TARGET/settings.json.bak"; printf '\n%s\n' "$MARKER" >> "$TARGET/settings.json"; echo "merged settings; backup=$TARGET/settings.json.bak"; fi
else
  printf '{"managed":true,"note":"%s"}\n' "$MARKER" > "$TARGET/settings.json"
  echo "created settings=$TARGET/settings.json"
fi
echo "installed target=$TARGET"
if [ "${1:-}" = "--uninstall" ]; then
  rm -rf "$TARGET/hooks" "$TARGET/skills/evidence" "$TARGET/AGENTS.md"
  if [ -f "$TARGET/settings.json.bak" ]; then mv "$TARGET/settings.json.bak" "$TARGET/settings.json"; else rm -f "$TARGET/settings.json"; fi
  rmdir "$TARGET" 2>/dev/null || true
  echo "uninstalled target=$TARGET restored_backup=$TARGET/settings.json"
fi
