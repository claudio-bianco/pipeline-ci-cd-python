from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_crud_todo_caminho_feliz():
    # CREATE
    payload = {
        "title": "Todo de teste",
        "description": "Criado pelo pytest",
        "completed": False,
    }
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    data = r.json()
    todo_id = data["id"]
    assert data["title"] == payload["title"]
    assert data["completed"] is False

    # LIST
    r = client.get("/todos")
    assert r.status_code == 200
    todos = r.json()
    assert any(t["id"] == todo_id for t in todos)

    # GET BY ID
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 200
    assert r.json()["id"] == todo_id

    # UPDATE
    r = client.put(f"/todos/{todo_id}", json={"completed": True})
    assert r.status_code == 200
    data = r.json()
    assert data["completed"] is True

    # DELETE
    r = client.delete(f"/todos/{todo_id}")
    assert r.status_code == 204

    # GET after delete -> 404
    r = client.get(f"/todos/{todo_id}")
    assert r.status_code == 404


def test_get_todo_nao_encontrado():
    # ID bem alto para garantir que não exista
    r = client.get("/todos/999999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo não encontrado"


def test_update_todo_nao_encontrado():
    r = client.put("/todos/999999", json={"title": "x"})
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo não encontrado"


def test_delete_todo_nao_encontrado():
    r = client.delete("/todos/999999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Todo não encontrado"


def test_update_apenas_title():
    # 1) Cria um todo novo
    payload = {
        "title": "Titulo original",
        "description": "Desc original",
        "completed": False,
    }
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    data = r.json()
    todo_id = data["id"]

    # 2) Atualiza apenas o título
    update_payload = {
        "title": "Titulo atualizado via teste",
    }
    r = client.put(f"/todos/{todo_id}", json=update_payload)
    assert r.status_code == 200
    data = r.json()

    # 3) Valida que só o title mudou
    assert data["title"] == "Titulo atualizado via teste"
    assert data["description"] == "Desc original"
    assert data["completed"] is False


def test_update_apenas_description():
    # 1) Cria um todo novo
    payload = {
        "title": "Todo original",
        "description": "Descr. original",
        "completed": False,
    }
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    data = r.json()
    todo_id = data["id"]

    # 2) Atualiza apenas a description (title/completed não vão no payload)
    update_payload = {
        "description": "Descrição atualizada via teste",
    }
    r = client.put(f"/todos/{todo_id}", json=update_payload)
    assert r.status_code == 200
    data = r.json()

    # 3) Valida que só a description mudou
    assert data["title"] == "Todo original"
    assert data["completed"] is False
    assert data["description"] == "Descrição atualizada via teste"


def test_update_apenas_completed_false_para_true():
    # Cria um todo com completed=False
    payload = {
        "title": "Todo para completed",
        "description": "Testando completed",
        "completed": False,
    }
    r = client.post("/todos", json=payload)
    assert r.status_code == 201
    data = r.json()
    todo_id = data["id"]

    # Atualiza só o completed
    update_payload = {
        "completed": True,
    }
    r = client.put(f"/todos/{todo_id}", json=update_payload)
    assert r.status_code == 200
    data = r.json()
    assert data["completed"] is True
