from fastapi import FastAPI

server = FastAPI()

@server.get("/")
async def get_root():
    return {"test"}


# Db connection
 
# Login Logic

# Create task (Dockerfile generation)

# Run task (Dockerfile execution and attaching to the container logs or continously streaming log files to the frontend)

