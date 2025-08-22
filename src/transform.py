import pandas as pd
import json
from glob import glob

all_records = []

for f in glob("./data/raw/*.json"):
    with open(f, "r", encoding="utf-8") as infile:
        data = json.load(infile)   # to jest lista słowników
        all_records.extend(data)

df = pd.DataFrame(all_records)
df = df.set_index(['region', 'date'])


filename = "data/processed/processed_data.csv"
df.to_csv(filename,sep=';',index=True,encoding="utf-8-sig")
