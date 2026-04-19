import streamlit as st
import pandas as pd
import os

DATA_PATH = "data/crypto_data.csv"

st.title("Crypto Dashboard")

if not os.path.exists(DATA_PATH):
    st.warning("No hay datos aún. Ejecuta el collector primero.")
else:
    df = pd.read_csv(DATA_PATH)

    st.subheader("Precio de cierre")
    st.line_chart(df["close"])

    st.subheader("Señales recientes")
    st.write(df.tail(20))