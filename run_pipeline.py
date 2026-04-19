from src.collector import get_crypto_data, save_data
from src.indicators import add_sma, compute_rsi
from src.signals import generate_signals

df = get_crypto_data()
df = add_sma(df)
df = compute_rsi(df)
df = generate_signals(df)

save_data(df)
print("Pipeline ejecutado correctamente y datos guardados en data/crypto_data.csv")