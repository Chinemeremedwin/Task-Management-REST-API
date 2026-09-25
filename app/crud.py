from sqlmodel import Session,select

from app.models import Task
from app.schemas import TaskCreate

#---CREATE---
def create_task(session: Session, task_data: TaskCreate):
    task = Task(**task_data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

#--GET-ONE-TASK--
def get_task(session, task_id):
     return session .get(Task,task_id)






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

def get_task(session: Session, task_id: int):
     statement = select(Task).where(Task.id == task_id)
     result = session.exec(statement).first()
     if not result:
          return None
     return result


#---UPDATE--
def update_task(session: Session, task_id: int,task_data: TaskCreate):
     task = get_task(session,task_id)
     if not task:
          return None
     task.title = task_data.title
     task.description = task_data.description 
     task.priority = task_data.priority
     session.add(task)
     session.commit()
     session.refresh(task)
     return task


#--DELETE--
def delete_task(session: Session, task_id: int):
     task = get_task(session, task_id)
     if not task:
          return None
     session.delete(task)
     session.commit()
     return {"Message": "Task deleted succesfully"}


#---Mark---
def complete_task(session: Session, task_id: int):
     task = get_task(session, task_id)
     if not task:
          return None
     task.status = "Completed"
     session.add(task)
     session.commit()
     session.refresh(task)

     return task

#---FILTER TASK 
def get_task_by_status(session: Session, status: str):
     statement = select(Task).where(Task.status == status)
     results = session.exec(statement)
     return results. all()


#--PATCH--
def complete_task(session, task_id):
     task = session.get(Task,task_id)
     if not task:
          return None
     task.status = "Completed"
     session.add(task)
     session.commit()
     session.refresh(task)
     return task
