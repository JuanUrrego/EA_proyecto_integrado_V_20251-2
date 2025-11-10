import sys
from pathlib import Path
from config import INPUT_FILE, SQLITE_DB, SQLITE_TABLE, EXPORT_CSV, EXPORT_LIMIT
from ingestar import Ingestar

def main():
    print("== Proyecto Integrado V: Flujo dataset -> SQLite -> CSV ==")
    ing = Ingestar()

    # 1) Cargar dataset local
    print(f"Cargando dataset desde: {INPUT_FILE}")
    df = ing.load_local(INPUT_FILE)
    print(f"Filas cargadas: {len(df):,} | Columnas: {len(df.columns)}")

    # 2) Limpieza mínima (ajusta los nombres a tu dataset real)
    text_cols = ["smoking_status", "alcohol_intake", "physical_activity_level", "gender"]
    numeric_cols = ["age", "height", "weight", "bmi"]  # ajusta si existen
    df = ing.normalize_text_columns(df, text_cols)
    df = ing.coerce_numeric(df, numeric_cols)

    # 3) Persistir en SQLite
    print(f"Escribiendo en SQLite: {SQLITE_DB} tabla: {SQLITE_TABLE}")
    ing.to_sqlite(df, SQLITE_DB, SQLITE_TABLE)
    count = ing.get_table_count(SQLITE_DB, SQLITE_TABLE)
    print(f"Conteo en SQLite[{SQLITE_TABLE}]: {count:,}")

    # 4) Exportar CSV DESDE SQLite (no del original)
    print(f"Exportando CSV desde SQLite hacia: {EXPORT_CSV} (limit={EXPORT_LIMIT})")
    ing.export_from_sqlite(SQLITE_DB, SQLITE_TABLE, EXPORT_CSV, limit=EXPORT_LIMIT)

    print("✅ Flujo completado con éxito.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ Error:", e)
        sys.exit(1)
