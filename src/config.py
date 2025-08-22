from pathlib import Path

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
DB_PATH = Path("data/weather.sqlite")