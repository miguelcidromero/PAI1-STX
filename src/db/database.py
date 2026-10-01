# Conexión SQLite

#Importamos libreria SQLite
import sqlite3
#Importamos la ruta de la BD de config.py
from ..config import DATABASE_URL
#Importamos la lista de tablas de tables.py
from .tables import ALL_TABLES

def init_db():
    # Abrir el canal usando 'WITH'
    # Al usar 'with', Python se encarga de hacer el conn.close() automáticamente al salir del bloque
    with sqlite3.connect(DATABASE_URL) as conexion:
        # Crear el intermediario (Cursor)
        cursor = conexion.cursor()

        for query in ALL_TABLES:
            cursor.execute(query)

    # El commit es automático --> El bloque 'with sqlite3.connect' en Python puede:
    # Si todo sale bien dentro del bloque, Python hace el conn.commit() por ti al final.
    # Si algo falla (un error de código o SQL), hace un rollback (cancela los cambios).

    print("¡Conexión cerrada y cambios guardados automáticamente!")


