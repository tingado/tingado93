#!/bin/bash
# setup.sh — Verificar archivos del proyecto Polla Mundialera 2026

echo "╔══════════════════════════════════════╗"
echo "║   POLLA MUNDIALERA 2026 — Setup      ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Verificar archivos
files=("index.html" "Code.gs" "README.md")
all_ok=true

for f in "${files[@]}"; do
  if [ -f "$f" ]; then
    lines=$(wc -l < "$f")
    echo "✅ $f ($lines líneas)"
  else
    echo "❌ $f — NO ENCONTRADO"
    all_ok=false
  fi
done

echo ""

if $all_ok; then
  echo "✅ Todos los archivos están listos."
  echo ""
  echo "PRÓXIMOS PASOS:"
  echo "1. Copia Code.gs → Google Apps Script (desde Sheets)"
  echo "2. Implementa y copia la URL"
  echo "3. Sube index.html a Netlify"
  echo "4. Pega la URL en el banner rojo de la app"
else
  echo "❌ Faltan archivos. Descarga el ZIP completo."
fi
