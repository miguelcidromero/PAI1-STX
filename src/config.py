#---config.py---

# Importamos la clase Path (libreria pathlib) para crear y manipular rutas de archivos de forma compatible con cualquier SO.
from pathlib import Path

# Localizar el directorio raíz del proyecto:
# Path(__file__) es src/config.py
# .resolve().parent es src/
# .resolve().parent.parent es la raíz del proyecto (C:\dev\PAI1-STX)
BASE_DIR = Path(__file__).resolve().parent.parent

# Directorio para datos persistentes
DATA_DIR = BASE_DIR / "data"

# Asegura que la carpeta 'data/' exista (no da error si ya existe)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Ruta completa al archivo de SQLite
DB_PATH = DATA_DIR / "secbank.db"

# URL de conexión (necesaria si utilizas SQLAlchemy)
# En SQLite la URL requiere el prefijo 'sqlite:///'
DATABASE_URL = str(DB_PATH)