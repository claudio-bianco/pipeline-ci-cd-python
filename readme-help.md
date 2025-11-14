cd todo-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# instale pacotes
pip install fastapi uvicorn

# Healthcheck
curl -X GET http://127.0.0.1:8000/health

# Criar um Todo (POST)
curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar CI/CD",
    "description": "Ler documentação do GitHub Actions",
    "completed": false
  }'

curl -X POST http://127.0.0.1:8000/todos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Deploy em produção",
    "description": "Testar pipeline antes",
    "completed": false
  }'

# Listar todos os Todos (GET)
curl -X GET http://127.0.0.1:8000/todos

# Buscar um Todo por ID (GET)
curl -X GET http://127.0.0.1:8000/todos/1

# Atualização completa (PUT)
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar Terraform",
    "description": "Começar pelo HCL básico",
    "completed": true
  }'

# Atualização parcial (somente um campo) (PUT)
curl -X PUT http://127.0.0.1:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'

# Deletar Todo (DELETE)
curl -X DELETE http://127.0.0.1:8000/todos/1

# Criar 5 Todos automaticamente (loop)
for i in {1..5}; do
  curl -X POST http://127.0.0.1:8000/todos \
    -H "Content-Type: application/json" \
    -d "{\"title\":\"Todo $i\", \"description\":\"Teste número $i\", \"completed\": false}";
  echo;
done

# scripts
chmod +x scripts/test_api.sh
# com a API rodando em uvicorn app.main:app --reload
./scripts/test_api.sh
# Se quiser apontar para outro host (ex: dentro do container)
BASE_URL=http://localhost:8000 ./scripts/test_api.sh


chmod +x scripts/seed_todos.sh
# cria 100
./scripts/seed_todos.sh
# cria 50
TOTAL=50 ./scripts/seed_todos.sh

# Rodar testes localmente
pytest -v



# Build
docker build -t todo-api-python .

# Run
docker run --rm -p 8000:8000 todo-api-python

# testes contra o container (já está apontando para http://127.0.0.1:8000)
./scripts/test_api.sh

# rodar o seed_todos.sh direto no host, com o container rodando
./scripts/seed_todos.sh




pytest -v --cov=app --cov-report=term-missing
