def generate_signals(df):
    def signal(row):
        if row["RSI"] < 30:
            return "BUY"
        elif row["RSI"] > 70:
            return "SELL"
        return "HOLD"

    df["signal"] = df.apply(signal, axis=1)
    return df