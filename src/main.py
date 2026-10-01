#---main.py---

# Importamos la clase FastAPI, que es el framework principal.
from fastapi import FastAPI
# asynccontextmanager permite crear un "gestor de contexto asíncrono":un bloque de código que se ejecuta en dos momentos (antes y después de un 'yield'), útil para lógica de inicio/apagado de la aplicación
from contextlib import asynccontextmanager
# Importamos nuestro módulo de base de datos (db/database.py), que contiene la función init_db() para crear las tablas.
from .db import database

# Definimos la función de "lifespan" (ciclo de vida) de la aplicación.
# FastAPI la ejecuta automáticamente al arrancar y al apagar el servidor.
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Todo lo que va ANTES del yield se ejecuta al ARRANCAR el servidor
    database.init_db() # Crea las tablas si no existen
    yield
     # Todo lo que fuera DESPUÉS del yield se ejecutaría al APAGAR el servidor


# Creamos la instancia principal de la aplicación FastAPI, indicándole que use nuestra función lifespan para el arranque/apagado
app = FastAPI(lifespan=lifespan)
