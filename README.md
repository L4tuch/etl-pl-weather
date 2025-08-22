# etl-pl-weather
ETL: Open-Meteo API → Pandas → SQLite → charts
This project implements a simple **ETL pipeline** to collect daily weather data from the [Open-Meteo API](https://open-meteo.com/), transform it using **Pandas**, load it into a **SQLite database**, and finally present the results through visualizations in Jupyter Notebooks.  

The project is designed as a **learning and portfolio exercise** to demonstrate basic skills of a Data Engineer:  
- Working with APIs  
- Data extraction and archival (raw JSON)  
- Data cleaning, transformation, and aggregation with Pandas  
- Loading data into SQL databases  
- Visualization and analysis of the processed data  

---

## 🎯 Project Goals

- **Extract:**  
  Fetch daily weather data (temperature, precipitation, wind speed, etc.) for all **16 Polish regions** from the Open-Meteo public API.  
  Archive the raw JSON responses for reproducibility.  

- **Transform:**  
  Clean and normalize the data using Pandas, ensure proper data types, and enrich records with metadata (e.g., timestamp, region).  

- **Load:**  
  Save the processed dataset to a **SQLite database** with uniqueness on `(date, region)` and indexing for fast queries.  

- **Present:**  
  Perform basic analysis and create visualizations (charts, comparisons between regions, rankings).  
  Provide results in a Jupyter Notebook.  

- **Automate:**  
  Schedule the pipeline to run **daily** using GitHub Actions, automatically ingesting and persisting fresh data.  

---

## 📂 Repository Structure

etl-pl-weather/
├── data/
│ ├── raw/ # raw JSON responses from API
│ └── processed/ # processed CSV data
│
├── notebooks/ # Jupyter Notebooks for analysis & charts
│
├── src/ # source code
│ ├── extract_open_meteo.py # extract step
│ ├── transform.py # transform step
│ ├── load_sql.py # load step
│ ├── regions.py # region → coordinates mapping
│ └── main.py # pipeline entrypoint
│
├── .github/workflows/ # GitHub Actions automation
│
├── requirements.txt # dependencies
├── README.md # project description
└── .gitignore