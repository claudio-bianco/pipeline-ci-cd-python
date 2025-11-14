from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, Base, get_db

# Cria as tabelas no banco (somente em dev; em prod preferir migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")


@app.get("/health", tags=["health"])
def healthcheck():
    return {"status": "ok"}


# CREATE Todo
@app.post("/todos", response_model=schemas.Todo, status_code=status.HTTP_201_CREATED, tags=["todos"])
def create_todo(todo_in: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = models.Todo(
        title=todo_in.title,
        description=todo_in.description,
        completed=todo_in.completed,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


# READ - Listar todos
@app.get("/todos", response_model=List[schemas.Todo], tags=["todos"])
def list_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos


# READ - Obter por ID
@app.get("/todos/{todo_id}", response_model=schemas.Todo, tags=["todos"])
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo não encontrado",
        )
    return todo


# UPDATE - Atualizar todo (parcialmente)
@app.put("/todos/{todo_id}", response_model=schemas.Todo, tags=["todos"])
def update_todo(todo_id: int, todo_in: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo não encontrado",
        )

    # Atualiza apenas campos enviados
    if todo_in.title is not None:
        todo.title = todo_in.title
    if todo_in.description is not None:
        todo.description = todo_in.description
    if todo_in.completed is not None:
        todo.completed = todo_in.completed

    db.commit()
    db.refresh(todo)
    return todo


# DELETE - Remover todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo não encontrado",
        )

    db.delete(todo)
    db.commit()
    return None
