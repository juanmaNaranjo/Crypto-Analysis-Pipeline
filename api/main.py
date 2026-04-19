from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

DATA_PATH = "data/crypto_data.csv"


@app.get("/")
def home():
    return {"message": "Crypto Analysis API running successfully!"}


@app.get("/signals")
def get_signals():
    if not os.path.exists(DATA_PATH):
        return {"error": "No data available"}

    df = pd.read_csv(DATA_PATH)
    return df.tail(20).to_dict(orient="records")