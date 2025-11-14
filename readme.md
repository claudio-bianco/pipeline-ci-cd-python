# 🟦 **Todo API – FastAPI + SQLite + Testes + Docker + CI/CD + SonarCloud**

> API REST completa para gerenciamento de tarefas (Todo List), construída com **Python + FastAPI**, persistência com **SQLite + SQLAlchemy**, testes automatizados com **pytest + coverage**, pipeline de **CI no GitHub Actions**, containerização com **Docker** e análise de qualidade via **SonarCloud**.
> 
> Este projeto foi desenvolvido para compor meu **portfólio profissional** como DevOps / Platform Engineer.

* * *

# 📌 **Objetivos do Projeto**

Este projeto foi criado para demonstrar, de forma prática:

* Construção de APIs REST com FastAPI
    
* Testes automatizados com alta cobertura (99%)
    
* Pipelines CI bem estruturados
    
* Qualidade contínua com SonarCloud
    
* Containerização com Docker
    
* Boas práticas de organização, padrões e documentação
    
* Scripts de automação
    
* Versionamento e estrutura de projeto limpos
    

* * *

# 🏗️ **Arquitetura do Projeto**

```
crud-python/
├── app/
│   ├── main.py          # Rotas e inicialização da API
│   ├── database.py      # Conexão SQLite via SQLAlchemy
│   ├── models.py        # Tabela Todo
│   ├── schemas.py       # Schemas Pydantic
│   └── __init__.py
├── tests/
│   └── test_todos.py    # Testes unitários e de integração
├── scripts/
│   ├── test_api.sh      # Teste completo via curl
│   └── seed_todos.sh    # Gera 100 tasks automaticamente
├── Dockerfile           # Container da API
├── requirements.txt     # Dependências
├── sonar-project.properties
└── .github/workflows/ci.yml
```

* * *

# 🚀 **Tecnologias Utilizadas**

| Categoria | Ferramenta |
| --- | --- |
| Linguagem | Python 3.12 |
| Framework | FastAPI |
| Banco | SQLite |
| ORM | SQLAlchemy |
| Validação | Pydantic |
| Testes | pytest + pytest-cov |
| CI/CD | GitHub Actions |
| Qualidade | SonarCloud |
| Containerização | Docker |
| Estilo REST | JSON, HTTP verbs, status codes |

* * *

# 🔄 **Endpoints da API**

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/health` | Verifica status da API |
| POST | `/todos` | Cria um novo Todo |
| GET | `/todos` | Lista todos os Todos |
| GET | `/todos/{id}` | Consulta por ID |
| PUT | `/todos/{id}` | Atualiza parcialmente/completamente |
| DELETE | `/todos/{id}` | Remove Todo |

* * *

# 🧪 **Testes Automatizados**

Os testes utilizam:

* **pytest**
    
* **pytest-cov**
    
* **FastAPI TestClient**
    

Cobertura atual:

```
TOTAL: 99%
```

Rodando localmente:

```bash
pytest -v --cov=app --cov-report=term-missing
```

Gera também o `coverage.xml` para integração com o SonarCloud.

* * *

# 🔍 **Análise de Qualidade – SonarCloud**

Este repositório é analisado pelo SonarCloud em todo push/PR.

Relatórios gerados:

* Cobertura de testes
    
* Bugs
    
* Vulnerabilidades
    
* Code Smells
    
* Duplicações
    

Badges (exemplo — posso substituir pelos seus reais):

  

* * *

# 🐳 **Docker**

Build:

```bash
docker build -t todo-python-api .
```

Executar:

```bash
docker run -p 8000:8000 todo-python-api
```

Acessar:

```
http://localhost:8000/docs
```

* * *

# 🧰 **Scripts de Automação**

## Testar todas as rotas (curl)

```bash
./scripts/test_api.sh
```

## Criar 100 TODOs rapidamente

```bash
./scripts/seed_todos.sh
```

* * *

# 📝 **Exemplos de consumo via CURL**

## Criar Todo

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar CI/CD", "description": "Pipeline GitHub", "completed": false}'
```

## Atualizar

```bash
curl -X PUT http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"description": "Atualizado via curl"}'
```

## Listar

```bash
curl http://localhost:8000/todos
```

## Deletar

```bash
curl -X DELETE http://localhost:8000/todos/1
```

* * *

# ⚙️ **Pipeline CI – GitHub Actions**

Fluxo executado a cada push/PR:

1. Instala dependências
    
2. Roda testes + coverage
    
3. Publica relatório `coverage.xml`
    
4. Executa análise do SonarCloud
    
5. Aplica Quality Gate
    

Workflow (`ci.yml`):

```yaml
name: CI - Todo API

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-test-sonar:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests with coverage
        env:
          PYTHONPATH: .
        run: |
          pytest -v --cov=app --cov-report=xml --cov-report=term-missing

      - name: SonarCloud Scan
        uses: SonarSource/sonarqube-scan-action@v5.0.0
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

* * *

# 🎯 **Aprendizados e Boas Práticas Demonstradas**

Este projeto demonstra:

* Arquitetura limpa e modular
    
* Testes automatizados com cobertura alta
    
* Pipeline de CI profissional
    
* Automação de qualidade (Quality Gate)
    
* Containerização
    
* Documentação clara e completa
    
* Uso de scripts shell para automação
    
* Boas práticas de API REST
    

Ideal para demonstrar habilidades de **DevOps**, **Platform Engineering**, **Python Backend** e **CI/CD**.

* * *

# 📄 **Licença**

MIT License.

* * *

# 🙌 **Contribuições**

Pull requests e sugestões são bem-vindas!

* * *


## 🔍 Análise de Qualidade (SonarCloud)

O projeto é analisado pelo **SonarCloud** em cada push e pull request.

A análise inclui:

- Cobertura de testes (pytest + pytest-cov)
- Code Smells
- Bugs potenciais
- Vulnerabilidades


[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=claudio-bianco_pipeline-ci-cd-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=claudio-bianco_pipeline-ci-cd-python)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=claudio-bianco_pipeline-ci-cd-python&metric=coverage)](https://sonarcloud.io/summary/new_code?id=claudio-bianco_pipeline-ci-cd-python)
