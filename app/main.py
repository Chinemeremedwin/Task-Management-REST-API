from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.database import get_session,create_db_and_tables

from app import crud


app = FastAPI()
create_db_and_tables

@app.get("/task")
def get_task(session: Session = Depends(get_session)): 
    return crud.get_tasks(session)
