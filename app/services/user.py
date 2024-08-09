from app.models.user import User as UserDB
from app.schema.user import User

class UserModel():
    
    def __init__(self, db) -> None:
        self.db = db
        
    def create_user(self, user: User):
        new_user = UserDB(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self, id: int, data: User):
        user= self.db.query(UserDB).filter(UserDB.id==id).first()
        user.username= data.username
        user.email= data.email
        self.db.commit()
        return
    
    def get_user(self, id: int):
        user= self.db.query(UserDB).filter(UserDB.id==id).first()
        return user
    
    def delete_user(self, id: int):
        result = self.db.query(UserDB).filter(UserDB.id==id).first()
        self.db.delete(result)
        self.db.commit()
        return