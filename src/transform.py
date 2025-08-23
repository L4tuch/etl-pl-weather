import pandas as pd
import json
from glob import glob


def run_transform():
    """Read raw JSON files and save one processed CSV snapshot."""
    all_records = []


    # Loop through all raw files and collect records
    for f in glob("./data/raw/*.json"):
        with open(f, "r", encoding="utf-8") as infile:
            data = json.load(infile)   # dict list
            all_records.extend(data)

    df = pd.DataFrame(all_records)
    df = df.set_index(['region', 'date'])

    filename = "data/processed/processed_data.csv"
    df.to_csv(filename, sep=';', index=True, encoding="utf-8-sig")

# Allow standalone execution (python src/transform.py)
if __name__ == "__main__":
    run_transform()
