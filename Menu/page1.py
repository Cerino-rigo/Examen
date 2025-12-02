import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from utils.data_loader import load_data

# Cargar datos


df = load_data()

st.title("👤 Análisis por Usuario")

usuarios = df["Usuario"].unique()
usuario_seleccionado = st.sidebar.selectbox("Selecciona un usuario", usuarios)

df_usuario = df[df["Usuario"] == usuario_seleccionado]

st.subheader(f"Resumen de {usuario_seleccionado}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Interacciones", df_usuario["número de interacción"].count())
col2.metric("Tiempo Prom. Interacción", round(df_usuario["tiempo de interacción"].mean(), 2))
col3.metric("Mini Juego Más Usado", df_usuario["mini juego"].mode()[0])

st.markdown("### 🎨 Colores presionados (Conteo)")
colores = df_usuario["color presionado"].value_counts()
st.bar_chart(colores)
st.markdown("### ⏱️ Evolución del tiempo de interacción")
df_usuario_sorted = df_usuario.sort_values(by="fecha")
st.line_chart(df_usuario["tiempo de interacción"].reset_index(drop=True))

st.markdown("### 🕹️ Filtro por tiempo de interacción (segundos)")
max_tiempo = int(df_usuario["tiempo de interacción"].max())
tiempo_max = st.slider("Mostrar interacciones menores a:", 0, max_tiempo, value=max_tiempo)
df_filtrado = df_usuario[df_usuario["tiempo de interacción"] <= tiempo_max]
st.write(f"Interacciones con tiempo menor o igual a {tiempo_max} segundos: {len(df_filtrado)}")
st.dataframe(df_filtrado)
