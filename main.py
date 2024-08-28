from fastapi import FastAPI
from routers.articulo import router as articulo_router

app = FastAPI()

# Incluir los routers
app.include_router(articulo_router)
