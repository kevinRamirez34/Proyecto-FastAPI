from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.config.database import Session
from app.schema.task import TaskBase
from app.services.task import TaskModel
from fastapi.encoders import jsonable_encoder

task_router = APIRouter()

@task_router.post('/tasks/', tags=['tasks'], response_model=dict, status_code=201)
def create_task(task:TaskBase)-> dict:
    db=Session()
    TaskModel(db).create_task(task)
    return JSONResponse(status_code=201, content={"message": "task created successfully"})

@task_router.put('/tasks/{id}', tags=['tasks'], response_model=dict, status_code=200)
def update_tasks(task: TaskBase):
    db=Session()
    result= TaskModel(db).get_task(task.id)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder({'message': "No se puede encontrar la tarea"}))
    id=task.id
    TaskModel(db).update_task(id, task)
    return JSONResponse (status_code=200, content=jsonable_encoder({'message': "Se ha modificado correctamente"}))

@task_router.delete('/tasks/{id}', tags=['tasks'], response_model=dict, status_code=200)
def delete_task(id: int):
    db=Session()
    result= TaskModel(db).get_task(id)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder({'message': "No se puede encontrar la tarea"}))
    TaskModel(db).delete_task(id)
    return JSONResponse(status_code=200, content=jsonable_encoder({'message': "Se ha eliminado la tarea"}))

@task_router.get('/tasks_by_user/{user_id}', tags=['tasks'], response_model=dict)
def get_tasks_by_user(user_id: int) -> TaskModel:
    db = Session()
    result= TaskModel(db).get_user_tasks(user_id)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder({'message': "No se puede encontrar la tarea"}))
    return JSONResponse(status_code=200 ,content=jsonable_encoder(result))