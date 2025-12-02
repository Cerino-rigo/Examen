import streamlit as st
import pandas as pd
from utils.data_loader import load_airbnb_data

st.title("📊 Resumen General de Airbnb")

df = load_airbnb_data()

st.subheader("Vista rápida del dataset")
st.write(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
st.dataframe(df.head())

# Ejemplo: seleccionar una variable numérica para resumen
numeric_cols = df.select_dtypes(include="number").columns.tolist()
if numeric_cols:
    col = st.selectbox("Selecciona una variable numérica para resumen:", numeric_cols)

    st.write("Estadísticos descriptivos:")
    st.write(df[col].describe())

    st.bar_chart(df[col].value_counts().head(20))
else:
    st.warning("No se encontraron columnas numéricas en el dataset.")
