# CRUD con FastAPI

## Descripción

Este proyecto muestra cómo construir una API CRUD completa utilizando **FastAPI** Incluye la configuración inicial y la implementación de endpoints para operaciones CRUD básicas.

## Instalación

1. **Instala las dependencias:**

   ```bash
   pip install fastapi
   ```
   ```bash
   pip install uvicorn
   ```
   
3. **Ejecuta la aplicación:**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Accede a la documentación:**

   Abre tu navegador y visita `http://localhost:8000/docs`.

## Uso

- **Crear:** `POST /personas`
- **Leer:** `GET /personas/{id}`
- **Actualizar:** `PUT /personas/{id}`
- **Eliminar:** `DELETE /personas/{id}`

Este README proporciona instrucciones claras para instalar y ejecutar tu aplicación, junto con la información de uso y créditos apropiados.
