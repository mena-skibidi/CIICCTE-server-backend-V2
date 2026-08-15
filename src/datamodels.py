
from pydantic import BaseModel


class create_user_datamodel(BaseModel):
    username: str
    nombre_completo: str | None = None
    password: str
    rol: int

class update_user_datamodel(BaseModel):
    username: str
    nombre_completo: str | None = None
    password: str | None = None
    rol: int | None = None