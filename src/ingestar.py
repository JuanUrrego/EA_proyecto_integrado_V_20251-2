import os
import sqlite3
import pandas as pd
from pathlib import Path
from typing import Optional, List, Union

class Ingestar:
    """
    Flujo base para el proyecto:
    - Cargar dataset local (CSV/XLSX) a DataFrame.
    - Limpieza básica opcional.
    - Persistir DataFrame en SQLite.
    - Exportar CSV resultante des de SQLite (no del original).
    """

    def __init__(self):
        pass

    # ---------- CARGA ----------
    def load_local(self, path: Union[str, Path]) -> pd.DataFrame:
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"No se encuentra el archivo: {path}")

        if path.suffix.lower() == ".csv":
            df = pd.read_csv(path)
        elif path.suffix.lower() in [".xlsx", ".xls"]:
            df = pd.read_excel(path)
        else:
            raise ValueError("Formato no soportado. Usa .csv o .xlsx")
        return df

    # ---------- LIMPIEZA BÁSICA ----------
    def normalize_text_columns(self, df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
        df = df.copy()
        for col in cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.lower()
        return df

    def coerce_numeric(self, df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
        df = df.copy()
        for col in cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        return df

    # ---------- SQLITE ----------
    def to_sqlite(self, df: pd.DataFrame, db_path: Union[str, Path], table: str):
        db_path = Path(db_path)
        os.makedirs(db_path.parent, exist_ok=True)
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table, conn, if_exists="replace", index=False)

    def export_from_sqlite(
        self,
        db_path: Union[str, Path],
        table: str,
        export_csv: Union[str, Path],
        limit: Optional[int] = None
    ):
        db_path = Path(db_path)
        export_csv = Path(export_csv)
        os.makedirs(export_csv.parent, exist_ok=True)

        query = f"SELECT * FROM {table}"
        if limit is not None:
            query += f" LIMIT {limit}"

        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(query, conn)
        df.to_csv(export_csv, index=False)

    # ---------- VERIFICACIONES ----------
    def get_table_count(self, db_path: Union[str, Path], table: str) -> int:
        with sqlite3.connect(db_path) as conn:
            q = f"SELECT COUNT(*) as c FROM {table}"
            c = pd.read_sql_query(q, conn).iloc[0, 0]
        return int(c)
