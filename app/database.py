from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# check_same_thread=False é necessário para SQLite com múltiplas threads (FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependência que será usada nos endpoints para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

