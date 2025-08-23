from config import DAILY_VARS, TIMEZONE, FORECAST_DAYS, RAW_DIR, formatted_date, url, all_results, result, howManyVars, Request_timeout
from regions import REGIONS
import requests
import json

for n in range(howManyVars):
    result = ",".join(DAILY_VARS)

for region, (lan, lon) in REGIONS.items():
    region_name = region
    latitude = lan
    longitude = lon
    urlQuery = f"{url}&latitude={latitude}&longitude={longitude}&daily={result}&timezone={TIMEZONE}&forecast_days={FORECAST_DAYS}"
    response = requests.get(urlQuery, timeout=Request_timeout)
    question = response.json()
    question['region'] = region_name
    all_results.append(question)

flat_rows = []

for rec in all_results:
    reg = rec.get("region")
    lat = rec.get("latitude")
    lon = rec.get("longitude")
    day = rec.get("daily", {})
    times = day.get("time", [])
    for i, t in enumerate(times):
        row = {
            "region": reg,
            "date": t,
            "latitude": lat,
            "longitude": lon,
        }
        for var in DAILY_VARS:
            vals = day.get(var, [])
            row[var] = vals[i] if len(vals) else None
        flat_rows.append(row)



filename = f"{RAW_DIR}/{formatted_date}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(flat_rows, f, ensure_ascii=False, indent=2)
