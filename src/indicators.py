import pandas as pd

def add_sma(df, window=20):
    df[f"SMA_{window}"] = df["close"].rolling(window=window).mean()
    return df


def compute_rsi(df, window=14):
    delta = df["close"].diff()
    gain = delta.clip(lower=0).rolling(window).mean()
    loss = -delta.clip(upper=0).rolling(window).mean()

    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    return df