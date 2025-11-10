from pathlib import Path

# Rutas base
DATA_DIR = Path("data")
DB_DIR = Path("db")

# Archivo de entrada 
INPUT_FILE = DATA_DIR / "lifestyle_health_kaggle.csv"  

# SQLite y exportación
SQLITE_DB = DB_DIR / "proyecto.db"
SQLITE_TABLE = "lifestyle"
EXPORT_CSV = DB_DIR / "export.csv"

# Límite de filas
EXPORT_LIMIT = None