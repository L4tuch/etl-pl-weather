# Orchestrate ETL: extract -> transform -> load

from extract import run_extract
from transform import run_transform
from load_sql import init_db, load_processed_csv


def run_pipeline():
    """Run the full ETL pipeline end-to-end."""
    print("=== ETL Pipeline Started ===")

    # Step 1: Extract raw data
    run_extract()

    # Step 2: Transform raw -> processed CSV
    run_transform()

    # Step 3: Load processed CSV -> SQLite
    init_db()
    load_processed_csv()

    print("=== ETL Pipeline Finished ===")


if __name__ == "__main__":
    run_pipeline()