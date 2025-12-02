import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("📊 Análisis General de los Juegos")

# Cargar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("DataAnalytics.csv")
    df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True, errors='coerce')
    return df

df = cargar_datos()

# --- KPIs dinámicos con placeholders ---
placeholder = st.empty()
btn_actualizar = st.sidebar.button("Actualizar KPIs")

if btn_actualizar:
    col1, col2, col3 = st.columns(3)
    col1.metric("Usuarios únicos", df["Usuario"].nunique())
    col2.metric("Mini juego más usado", df["mini juego"].mode()[0])
    col3.metric("Dificultad más frecuente", df["dificultad"].mode()[0])

st.markdown("### 🧠 Tiempo promedio por dificultad y mini juego")

df_agrupado = df.groupby(["dificultad", "mini juego"])["tiempo de interacción"].mean().reset_index()


chart = alt.Chart(df_agrupado).mark_bar().encode(
        x=alt.X("dificultad:N", title="Dificultad"),
        y=alt.Y("tiempo de interacción:Q", title="Tiempo Promedio de Interacción"),
        color="mini juego:N",
        tooltip=["dificultad", "mini juego", "tiempo de interacción"]
    ).properties(width=700, height=400)

st.altair_chart(chart)