from fastapi import FastAPI

from db import db_setup

server = FastAPI()

@server.on_event("startup")
def on_server_start_setup():
    db_setup()


@server.get("/")
async def get_root():
    return "test"


@server.post("/roles")
def create_role():
    return
