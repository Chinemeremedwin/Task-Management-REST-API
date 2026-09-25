from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session,create_db_and_tables
from app import crud
from app.models import Task
from app.schemas import TaskCreate

app = FastAPI()



#--GET--

@app.get("/task")
def get_task(
    status: str = None,
    session: Session = Depends(get_session)):
    if status:
        return crud.get_task_by_status(session, status)

    return crud.get_tasks(session)

#--GET-ONE-TASK
@app.get("/tasks/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.get_task(session, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task 

#--POST--
@app.post("/task/")
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    return crud.create_task(session, task)



#--PUT--
@app.put("/task/{task_id}")
def update_task(
    task_id: int,
    task: Task,
    session: Session = Depends(get_session)):
    return crud.update_task(session, task_id, task)


#--DELETE--
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.delete_task(session, task_id)

    if not task:
        raise  HTTPException (status_code=404, detail = "Task not found")

    return {"message": "Task deleted succesfully"}

#--PATCH-- 
@app.patch("/task/{task_id}/complete")
def complete_task(task_id: int, session: Session = Depends(get_session)):
    task = crud.complete_task(session, task_id)
    if not task:
        raise HTTPException (status_code=404, detail = "Task not found")
    return task
