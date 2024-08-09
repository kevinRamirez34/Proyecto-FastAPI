from fastapi import FastAPI
from app.config.database import engine, Base
from app.routers.user import user_router
from app.routers.task import task_router


app = FastAPI()
app.title ="Taller FastAPI"
app.version = "0.0.9"

app.include_router(user_router)
app.include_router(task_router)

Base.metadata.create_all(bind=engine)

