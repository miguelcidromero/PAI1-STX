# Esquemas de tablas

CREATE_TABLE_USUARIOS = """ 
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        failed_attempts INTEGER DEFAULT 0,
        lockout_until INTEGER DEFAULT 0
    ) 
"""

CREATE_TABLE_NONCES = """
    CREATE TABLE IF NOT EXISTS nonces(
        nonce INTEGER PRIMARY KEY,
        timestamp INTEGER NOT NULL,
        received_at INTEGER NOT NULL
    )
"""

CREATE_TABLE_TRANSACCIONES = """
    CREATE TABLE IF NOT EXISTS transacciones(
        tx_id TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        hmac TEXT NOT NULL,
        origin_account TEXT NOT NULL,
        destination_account TEXT NOT NULL,
        amount INTEGER NOT NULL,
        currency TEXT NOT NULL,
        timestamp INTEGER NOT NULL,
        created_at INTEGER NOT NULL,
        status TEXT NOT NULL
    )
"""

CREATE_TABLE_SERSIONES = """
    CREATE TABLE IF NOT EXISTS sesiones(
        token TEXT PRIMARY KEY,
        user_id INTEGER UNIQUE NOT NULL,
        session_key TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        last_activity_at INTEGER NOT NULL
    )
"""

ALL_TABLES = [CREATE_TABLE_USUARIOS,CREATE_TABLE_NONCES,CREATE_TABLE_TRANSACCIONES,CREATE_TABLE_SERSIONES]