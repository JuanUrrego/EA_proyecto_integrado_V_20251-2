import sqlite3
import pandas as pd
from config import SQLITE_DB, SQLITE_TABLE

def main():
    with sqlite3.connect(SQLITE_DB) as conn:
        print("Tablas en la DB:")
        tables = pd.read_sql_query(
            "SELECT name FROM sqlite_master WHERE type='table';", conn
        )
        print(tables)

        print(f"\nConteo de filas en {SQLITE_TABLE}:")
        c = pd.read_sql_query(f"SELECT COUNT(*) as c FROM {SQLITE_TABLE};", conn)
        print(c)

        print(f"\nMuestra de 5 filas:")
        sample = pd.read_sql_query(f"SELECT * FROM {SQLITE_TABLE} LIMIT 5;", conn)
        print(sample.head())

if __name__ == "__main__":
    main()
