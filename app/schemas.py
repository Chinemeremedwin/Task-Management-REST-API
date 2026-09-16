from sqlmodel import SQLModel
class TaskCreate(SQLModel):
    title:str
    description:str
    priority:str

class TaskResponse(SQLModel):
    id:int
    title:str
    description:str
    priority:str
    status:str