from sqlmodel import Session,select

from models import Task
from schemas import TaskCreate

#---CREATE---
def create_task(session: Session, task_data: TaskCreate):
    task = Task(**task_data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

#---READ---#
def create_task(session: Session, task_data: TaskCreate):
     task = Task(**task_data.model_dump())
     session.add(task)
     session.commit()
     session.refresh(task)
     return task
def get_tasks(session: Session):
     statement = select(Task)
     results = session.exec(statement)
     return results.all()

def get_tasks(session: Session, task_id: int):
     statement = select(Task).where(Task.id == task_id)
     result = session.exec(statement).first()
     if not result:
          return None
     return result


#---UPDATE--