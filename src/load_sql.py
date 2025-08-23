import sqlite3
import pandas as pd
from config import DB_PATH, PROCESSED_CSV, CSV_SEP, CSV_ENCODING, TABLE_NAME

def init_db():
    """Initialize the SQLite database and create table if it does not exist"""
    with sqlite3.connect(DB_PATH) as conn:
        with open("sql/0001_init.sql", "r", encoding="utf-8") as f:
            schema = f.read()
        conn.executescript(schema)  # Execute schema script


def load_processed_csv():
    """Load processed CSV file into SQLite database (idempotent insert)"""
    # Load processed CSV with region+date as index
    df = pd.read_csv(PROCESSED_CSV, sep=CSV_SEP, encoding=CSV_ENCODING, index_col=["region", "date"])
    df = df.reset_index()  # Reset index so region and date become normal columns

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Iterate through rows and insert into DB
        for _, row in df.iterrows():
            cursor.execute(
                f"""
                INSERT OR IGNORE INTO {TABLE_NAME}
                (region, date, latitude, longitude, temperature_2m_max, temperature_2m_min,
                 precipitation_sum, wind_speed_10m_max)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    row["region"], row["date"], row["latitude"], row["longitude"],
                    row["temperature_2m_max"], row["temperature_2m_min"],
                    row["precipitation_sum"], row["wind_speed_10m_max"],
                ),
            )
        conn.commit()  # Save changes


if __name__ == "__main__":
    # Step 1: create table if not exists
    init_db()
    # Step 2: load CSV into database
    load_processed_csv()
