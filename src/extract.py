import json
import requests
from regions import REGIONS
from config import (
    DAILY_VARS, TIMEZONE, FORECAST_DAYS, RAW_DIR,
    formatted_date, url, Request_timeout,
)

def run_extract(how_many_vars: int | None = None):
    """Fetch daily weather for all regions and save a flattened JSON file."""

    # 1) Choose variables (all, or first N if provided)
    vars_to_use = DAILY_VARS if how_many_vars is None else DAILY_VARS[:how_many_vars]
    daily_param = ",".join(vars_to_use)

    # 2) Collect raw API responses (fresh list per run)
    all_results = []

    # 3) Single loop over regions (do NOT wrap it in any other loop)
    for region_name, (lat, lon) in REGIONS.items():
        # Build API URL
        url_query = (
            f"{url}&latitude={lat}&longitude={lon}"
            f"&daily={daily_param}&timezone={TIMEZONE}&forecast_days={FORECAST_DAYS}"
        )

        # Call API with timeout
        resp = requests.get(url_query, timeout=Request_timeout)
        resp.raise_for_status()  # raise if HTTP error

        data = resp.json()
        data["region"] = region_name
        all_results.append(data)

    # 4) Flatten nested JSON → list of row-like dicts
    flat_rows = []
    for rec in all_results:
        reg = rec.get("region")
        lat = rec.get("latitude")
        lon = rec.get("longitude")
        daily = rec.get("daily", {})
        times = daily.get("time", [])

        for i, t in enumerate(times):
            row = {
                "region": reg,
                "date": t,
                "latitude": lat,
                "longitude": lon,
            }
            # Add each selected variable for this index
            for var in vars_to_use:
                vals = daily.get(var, [])
                row[var] = vals[i] if i < len(vals) else None
            flat_rows.append(row)

    # 5) Save to RAW_DIR / YYYY-MM-DD.json
    out_path = f"{RAW_DIR}/{formatted_date}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(flat_rows, f, ensure_ascii=False, indent=2)

    print(f"[Extract] Saved {len(flat_rows)} rows to {out_path}")


# Allow standalone execution (python src/extract.py)
if __name__ == "__main__":
    run_extract()            # all variables
    # run_extract(2)         # or: first N variables