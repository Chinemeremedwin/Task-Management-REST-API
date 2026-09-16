from sqlmodel import create_engine

DATABASE_URL ="postgresql://postgres:Edwin17@localhost:5432/task_management_db"

engine = create_engine(DATABASE_URL,echo=True)