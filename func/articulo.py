from typing import List, Optional
from schemas.articulo import Articulo, ArticuloBase, ArticuloUpdate
from datetime import date

# Base de datos simulada
db_articulos = [
    Articulo(id=1, nombre="Articulo 1", edad=20, fecha=date(2024, 8, 28)),
    Articulo(id=2, nombre="Articulo 2", edad=30, fecha=date(2024, 8, 28)),
]

def obtener_articulos() -> List[Articulo]:
    return db_articulos

def obtener_articulo(articulo_id: int) -> Optional[Articulo]:
    for articulo in db_articulos:
        if articulo.id == articulo_id:
            return articulo
    return None

def crear_articulo(articulo_create: ArticuloBase) -> Articulo:
    if articulo_create.id is not None:
        # Verificar si el id ya existe
        if any(a.id == articulo_create.id for a in db_articulos):
            raise ValueError("El ID ya existe")
        nuevo_articulo = Articulo(id=articulo_create.id, **articulo_create.dict(exclude={"id"}))
    else:
        nuevo_id = max(a.id for a in db_articulos) + 1 if db_articulos else 1
        nuevo_articulo = Articulo(id=nuevo_id, **articulo_create.dict())
    
    db_articulos.append(nuevo_articulo)
    return nuevo_articulo

def actualizar_articulo(articulo_id: int, articulo_update: ArticuloUpdate) -> Optional[Articulo]:
    for index, articulo in enumerate(db_articulos):
        if articulo.id == articulo_id:
            # Crear un nuevo Articulo con los datos actualizados
            actualizado = Articulo(id=articulo_id, **articulo_update.dict())
            db_articulos[index] = actualizado
            return actualizado
    return None

def eliminar_articulo(articulo_id: int) -> Optional[List[Articulo]]:
    global db_articulos
    for index, articulo in enumerate(db_articulos):
        if articulo.id == articulo_id:
            db_articulos.pop(index)
            return db_articulos  # Devolver la lista completa después de la eliminación
    return None  # Devolver None si no se encontró el artículo