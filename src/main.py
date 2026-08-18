from fastapi import FastAPI

from datamodels import create_user_datamodel, login_data, update_user_datamodel
from db import (
    create_user_db,
    db_setup,
    delete_user_db,
    login_process_db,
    update_user_db,
)

server = FastAPI()


@server.on_event("startup")
def on_server_start_setup():
    db_setup()


@server.post("/users")
def create_user(data: create_user_datamodel):
    create_user_db(data.username, data.nombre_completo, data.password, data.rol)


@server.delete("/users")
def delete_user(username: str):
    delete_user_db(username)


@server.put("/users")
def update_user(data: update_user_datamodel):
    filtered_data = data.model_dump(exclude_unset=True)
    update_user_db(data.username, filtered_data)


@server.post("/login")
def login_process(data: login_data):
    login_process_db(data.username, data.password)
