from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.config.database import Session
from app.schema.user import User
from app.services.user import UserModel
from fastapi.encoders import jsonable_encoder

user_router = APIRouter()

@user_router.post('/users/', tags=['users'], response_model=dict, status_code=201)
def create_user(user:User)-> dict:
    db=Session()
    UserModel(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "User created successfully"})

@user_router.put('/users/{id}', tags=['users'])
def update_users(id: int, user: User):
    db=Session()
    result= UserModel(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder({'message': "No se puede encontrar el usuario"}))
    UserModel(db).update_user(id, user)
    return JSONResponse (status_code=200, content=jsonable_encoder({'message': "Se ha modificado correctamente"}))

@user_router.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_user(id: int):
    db=Session()
    result= UserModel(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder({'message': "No se puede encontrar el usuario"}))
    UserModel(db).delete_user(id)
    return JSONResponse(status_code=200, content=jsonable_encoder({'message': "Se ha eliminado el usuario"}))