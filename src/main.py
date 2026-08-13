from fastapi import FastAPI
from db import db_setup, create_user
from pydantic import BaseModel

server = FastAPI()

@server.on_event("startup")
def on_server_start_setup():
    db_setup()


@server.get("/")
async def get_root():
    return "test"


class create_user_datamodel(BaseModel):
    username: str
    nombre_completo: str | None = None
    password: str
    rol: int

@server.post("/users")
def create_role(data: create_user_datamodel):
    create_user(data.username, data.nombre_completo, data.password, data.rol)