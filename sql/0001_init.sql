CREATE TABLE IF NOT EXISTS weather_daily (
  region TEXT NOT NULL,
  date   TEXT NOT NULL,            -- ISO: 'YYYY-MM-DD'
  latitude  REAL,
  longitude REAL,
  temperature_2m_max REAL,
  temperature_2m_min REAL,
  precipitation_sum  REAL,
  wind_speed_10m_max REAL,
  PRIMARY KEY (region, date)       -- Unique key: no duplicates for region+date
);

CREATE INDEX IF NOT EXISTS idx_weather_daily_date ON weather_daily(date);
