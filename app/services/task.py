from app.models.task import Task as TaskDB
from app.schema.task import TaskBase
from app.models.user import User as UserDB

class TaskModel():
    
    def __init__(self, db) -> None:
        self.db = db
        
    def create_task(self, task: TaskBase):
        new_task = TaskDB(**task.dict())
        self.db.add(new_task)
        self.db.commit()
        return
    
    def update_task(self, id: int, data: TaskBase):
        task= self.db.query(TaskDB).filter(TaskDB.id==id).first()
        task.title= data.title
        task.description= data.description
        task.to_do= data.to_do
        self.db.commit()
        return
    
    def get_task(self, id: int):
        task= self.db.query(TaskDB).filter(TaskDB.id==id).first()
        return task
    
    def delete_task(self, id: int):
        result = self.db.query(TaskDB).filter(TaskDB.id==id).first()
        self.db.delete(result)
        self.db.commit()
        return
    
    def get_user_tasks(self, id: int):
        tasks= self.db.query(TaskDB).filter(TaskDB.user_id==id).all()
        return tasks