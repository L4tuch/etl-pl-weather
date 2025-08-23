from pathlib import Path
from datetime import datetime

# List of daily variables you want to download from Open-Meteo
DAILY_VARS = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "wind_speed_10m_max",
]

# Default query settings
TIMEZONE = "Europe/Warsaw"
FORECAST_DAYS = 1   # how many days forecast

# Paths to directories and files
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
DB_PATH = Path("data/weather.db")

TABLE_NAME = "weather_daily"
PROCESSED_CSV = "data/processed/processed_data.csv"
CSV_SEP = ";"
CSV_ENCODING = "utf-8-sig"

today = datetime.today()
formatted_date= today.strftime("%Y-%m-%d")

url = "https://api.open-meteo.com/v1/forecast?"

all_results = []


result = ""
howManyVars = len(DAILY_VARS)

Request_timeout = 60
