from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.articulo import Articulo, ArticuloCreate, ArticuloUpdate, ArticuloBase
from func.articulo import obtener_articulos, obtener_articulo, crear_articulo, actualizar_articulo, eliminar_articulo

router = APIRouter()

@router.get("/articulos", response_model=list[Articulo])
async def leer_articulos():
    return JSONResponse(content=jsonable_encoder(obtener_articulos()))

@router.get("/articulos/{articulo_id}", response_model=Articulo)
async def leer_articulo(articulo_id: int):
    articulo = obtener_articulo(articulo_id)
    if articulo is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return JSONResponse(content=jsonable_encoder(articulo))

@router.post("/articulos", response_model=Articulo)
async def crear_nuevo_articulo(articulo: ArticuloBase):
    try:
        nuevo_articulo = crear_articulo(articulo)
        return JSONResponse(
            content=jsonable_encoder(nuevo_articulo),status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/articulos/{articulo_id}", response_model=Articulo)
async def actualizar_articulo_existente(articulo_id: int, articulo: ArticuloUpdate):
    actualizado = actualizar_articulo(articulo_id, articulo)
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return JSONResponse(content=jsonable_encoder(actualizado))

@router.delete("/articulos/{articulo_id}", response_model=Articulo)
async def eliminar_un_articulo(articulo_id: int):
    eliminado = eliminar_articulo(articulo_id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return JSONResponse(content=jsonable_encoder(eliminado))
