from fastapi import FastAPI

server = FastAPI()

@server.get("/")
async def get_root():
    return {"test"}


'''
TODO

- Meter el proyecto en docker compose
- Modelar tablas y relaciones
- Conexion a la db
- Hacer la logica del login

'''



