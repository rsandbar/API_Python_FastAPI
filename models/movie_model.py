from pydantic import BaseModel
from typing import Optional

class movieSchema(BaseModel):
    autor: str
    descripcion: str
    fecha_estreno: str

