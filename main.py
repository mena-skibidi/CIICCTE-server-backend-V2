from fastapi import FastAPI
from sqlmodel import create_engine, Field, SQLModel

server = FastAPI()


class roles(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nombre_rol: str


class usuarios(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    nombre_completo: str
    password_encriptada: str


class cuenta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    usuarios_id: int = Field(default=None, foreign_key="usuarios.id")
    roles_id: int = Field(default=None, foreign_key="roles.id")


engine = create_engine("postgresql://dbuser:labtest321@db:5432/labdb", echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


@server.get("/")
async def get_root():
    return "test"


@server.post("/roles")
async def create_role():
    return
