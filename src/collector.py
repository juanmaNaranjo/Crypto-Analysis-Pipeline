from binance.client import Client
import pandas as pd

def get_crypto_data(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=200):
    client = Client()

    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)

    df = pd.DataFrame(klines, columns=[
        "time","open","high","low","close","volume",
        "close_time","qav","num_trades",
        "taker_base","taker_quote","ignore"
    ])

    df["time"] = pd.to_datetime(df["time"], unit="ms")
    df["close"] = df["close"].astype(float)

    return df


def save_data(df, path="data/crypto_data.csv"):
    df.to_csv(path, index=False)