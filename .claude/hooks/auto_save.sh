#!/bin/bash
# Auto-commitea archivos .md nuevos o modificados en sesiones/ y CLAUDE.md
# Se ejecuta automáticamente al final de cada sesión (hook Stop)

REPO="/home/user/tingaod93"
cd "$REPO" || exit 0

git add sesiones/*.md CLAUDE.md 2>/dev/null

if git diff --cached --quiet; then
  exit 0
fi

FECHA=$(date +%Y-%m-%d)
BRANCH=$(git branch --show-current)

git commit -m "Auto-save sesión $FECHA"
git push origin "$BRANCH" 2>/dev/null || true
