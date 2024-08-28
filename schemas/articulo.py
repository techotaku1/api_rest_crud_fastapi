from pydantic import BaseModel
from typing import Optional
from datetime import date

class ArticuloBase(BaseModel):
    id: Optional[int]  # Permitir id opcionalmente en la entrada
    nombre: str
    edad: int
    fecha: Optional[date]

class Articulo(ArticuloBase):
    pass

class ArticuloCreate(BaseModel):
    nombre: str
    edad: int
    fecha: Optional[date]

class ArticuloUpdate(BaseModel):
    nombre: str
    edad: int
    fecha: Optional[date]
