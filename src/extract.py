from numpy import long
from config import DAILY_VARS, TIMEZONE, FORECAST_DAYS, RAW_DIR, today,formatted_date,url,all_results,result,howManyVars
from regions import REGIONS
from datetime import datetime
import requests
import json

for n in range(howManyVars):
    result = ",".join(DAILY_VARS)

for region, (lan, lon) in REGIONS.items():
    region_name = region
    latitude = lan
    longitude = lon
    urlQuery = f"{url}&latitude={latitude}&longitude={longitude}&daily={result}&timezone={TIMEZONE}&forecast_days={FORECAST_DAYS}"
    #print(f"URL dla {region_name}:{urlQuery}")
    response = requests.get(urlQuery, timeout=60)
    question = response.json()
    question['region'] = region_name
    all_results.append(question)

flat_rows = []

for rec in all_results:
    reg = rec.get("region")
    lat = rec.get("latitude")
    lon = rec.get("longitude")
    day = rec.get("daily",{})
    times = day.get("time",[])
    for i, t in enumerate(times):
        row = {
            "region" : reg,
            "date" : t,
            "latitude" : lat,
            "longitude" : lon,
        }
        for var in DAILY_VARS:
            vals = day.get(var,[])
            #print(f"{var}: {vals}")
            row[var]=vals[i] if len(vals) else None
        flat_rows.append(row)

print(flat_rows)

filename = f"data/raw/{formatted_date}.json"

with open(filename,"w",encoding="utf-8") as f:
    json.dump(flat_rows,f,ensure_ascii=False,indent=2)