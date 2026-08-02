from fastapi import FastAPI
from sqlmodel import create_engine, Session, Field, select, SQLModel

server = FastAPI()

# Habria que esconder la connection string en un .env o en las variables de entorno
engine = create_engine("postgresql://dbuser:labtest321@db:5432/labdb", echo=True)

class Test(SQLModel, table = True):
    id: int = Field(primary_key=True)
    text: str


@server.get("/")
async def get_root():
    with Session(engine) as session:
        statement = select(Test)
        results = session.exec(statement).all()
        return results


'''
TODO

x Modelar tablas y relaciones
o Conexion a la db
x Hacer la logica del login

'''



