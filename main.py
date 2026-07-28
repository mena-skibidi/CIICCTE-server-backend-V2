from fastapi import FastAPI

server = FastAPI()

@server.get("/")
async def get_root():
    return {"test"}