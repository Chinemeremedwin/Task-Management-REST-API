from sqlmodel import create_engine, Session, SQLModel
from app.models import Task

DATABASE_URL = "postgresql://postgres:Edwin17@localhost:5432/task_management_db"


engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session