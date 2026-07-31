from fastapi import FastAPI

server = FastAPI()

@server.get("/")
async def get_root():
    return {"test"}


'''
TODO

- Modelar tablas y relaciones
- Conexion a la db
- Hacer la logica del login

'''



