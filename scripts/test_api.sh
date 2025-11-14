#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"

echo "==> Healthcheck"
curl -s -X GET "$BASE_URL/health"
echo -e "\n"

echo "==> Criando TODO 1"
curl -s -X POST "$BASE_URL/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar CI/CD",
    "description": "Ler documentação do GitHub Actions",
    "completed": false
  }'
echo -e "\n"

echo "==> Criando TODO 2"
curl -s -X POST "$BASE_URL/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar Terraform",
    "description": "HCL básico",
    "completed": false
  }'
echo -e "\n"

echo "==> Listando todos"
curl -s -X GET "$BASE_URL/todos"
echo -e "\n"

echo "==> Buscando TODO id=1"
curl -s -X GET "$BASE_URL/todos/1"
echo -e "\n"

echo "==> Atualizando TODO id=1 (completed=true)"
curl -s -X PUT "$BASE_URL/todos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
echo -e "\n"

echo "==> Buscando TODO id=1 após update"
curl -s -X GET "$BASE_URL/todos/1"
echo -e "\n"

echo "==> Deletando TODO id=2"
curl -s -X DELETE "$BASE_URL/todos/2"
echo -e "\n"

echo "==> Listando todos após delete"
curl -s -X GET "$BASE_URL/todos"
echo -e "\n"

echo "==> Fim dos testes manuais com curl ✅"

