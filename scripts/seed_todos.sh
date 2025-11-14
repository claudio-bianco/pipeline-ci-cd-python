#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"
TOTAL="${TOTAL:-100}"

echo "==> Criando $TOTAL todos de teste em $BASE_URL"

for i in $(seq 1 "$TOTAL"); do
  TITLE="Todo $i"
  DESC="Tarefa de teste número $i"

  curl -s -X POST "$BASE_URL/todos" \
    -H "Content-Type: application/json" \
    -d "{
      \"title\": \"${TITLE}\",
      \"description\": \"${DESC}\",
      \"completed\": false
    }" > /dev/null

  echo "Criado: $TITLE"
done

echo "==> Concluído ✅"

