import pandas as pd
import streamlit as st

# Reemplaza esto con el ID real del archivo en tu Drive

#https://drive.google.com/file/d/1ZqfDMY2HeWqqnRp3Sun9l3uWpvMNMhX6
#https://drive.google.com/file/d/1ZqfDMY2HeWqqnRp3Sun9l3uWpvMNMhX6


@st.cache_data
def load_airbnb_data():
    FILE_ID = "1DcO7Q9ZcLcJgWqV_YiL8yP0evhBO4ZBy"
    """Carga el CSV de Airbnb directamente desde Google Drive."""
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

    df = pd.read_csv(url)

    return df
