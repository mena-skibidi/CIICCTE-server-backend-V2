from fastapi import FastAPI

from db import create_base_roles, create_tables

server = FastAPI()

@server.on_event("startup")
def on_server_start_setup():
    create_tables()
    create_base_roles()


@server.get("/")
async def get_root():
    return "test"


@server.post("/roles")
def create_role():
    return
