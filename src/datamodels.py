from typing import Optional

from pydantic import BaseModel


class create_user_datamodel(BaseModel):
    username: str
    nombre_completo: str | None = None
    password: str
    account_status: str # Los valores solo pueden ser "activa", "desactivada"
    rol: int

class update_user_datamodel(BaseModel):
    username: str
    nombre_completo: Optional[str] = None
    password: Optional[str] = None
    rol: Optional[int] = None