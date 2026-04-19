# Crypto Analysis Pipeline

[![Python](https://img.shields.io/badge/Python-3.12-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()
[![Status](https://img.shields.io/badge/Status-Active-success)]()

---

## Description

This project implements a data pipeline for cryptocurrency analysis using Python. It collects historical market data from Binance, processes and transforms it, computes technical indicators, generates trading signals, and exposes the results through a REST API and an interactive dashboard.

The main goal of this project is to demonstrate skills in data engineering, API consumption, data processing, and backend development in a real-world scenario.

---

## Architecture

The system workflow is composed of the following stages:

1. Data collection from Binance
2. Data processing and transformation
3. Technical indicator computation
4. Trading signal generation
5. Local data persistence (CSV)
6. API exposure
7. Data visualization through a dashboard

Data flow:

Binance API
→ Data Collector
→ Data Processing
→ Indicators Calculation
→ Signal Generation
→ Storage (CSV)
→ API (FastAPI)
→ Dashboard (Streamlit)

---

## Project Structure

```
crypto-analysis/
│
├── data/
├── src/
│   ├── collector.py
│   ├── indicators.py
│   ├── signals.py
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python 3.12
* python-binance
* pandas
* FastAPI
* Uvicorn
* Streamlit

---

## Installation

Clone the repository:

```
git clone <your-repo-url>
cd crypto-analysis
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### 1. Run data pipeline

```
python run_pipeline.py
```

This generates:

```
data/crypto_data.csv
```

---

### 2. Run API

```
uvicorn api.main:app --reload
```

Available endpoints:

* http://127.0.0.1:8000/
* http://127.0.0.1:8000/signals
* http://127.0.0.1:8000/docs

---

### 3. Run dashboard

```
streamlit run dashboard/app.py
```

Access:

```
http://localhost:8501
```

---

## Indicators

### Simple Moving Average (SMA)

Calculates the average closing price over a defined window.

### Relative Strength Index (RSI)

A momentum indicator that measures the speed and magnitude of price movements to identify overbought and oversold conditions.

---

## Signal Generation

Signals are generated based on RSI values:

* RSI < 30 → BUY
* RSI > 70 → SELL
* Otherwise → HOLD

---

## Technical Considerations

* Uses public data from Binance
* No authentication required for basic endpoints
* Data is stored locally in CSV format
* Modular architecture allows easy extension and scalability

---

## Engineering Highlights

* Clean and modular architecture
* Clear separation of concerns (data collection, processing, API, visualization)
* Reusable and maintainable components
* Lightweight and efficient execution
* Ready for scaling (database integration, async processing, cloud deployment)

---

## Potential Improvements

* Database integration (PostgreSQL, MongoDB)
* Strategy backtesting engine
* Real-time data streaming with WebSockets
* Deployment using Docker, AWS, or Railway
* Machine Learning models for price prediction
* Automated scheduling (cron jobs or task schedulers)

---

## Limitations

* No real trading execution
* Basic strategy (RSI-based)
* No advanced error handling or retry mechanisms

---

## Disclaimer

This project is for educational purposes only and does not constitute financial advice.

---

## References

* Binance API Documentation
* python-binance Documentation
* pandas Documentation
* FastAPI Documentation
* Streamlit Documentation

---

## Project Status

Actively maintained and open for improvements and extensions.
