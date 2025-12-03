import pandas as pd
import streamlit as st

''' 
    ######VERIFICA EL LINK DEL ARCHIVO EN DRIVE ANTES DE USARLO######
    Ejemplo de link real a datos de mi archivo en Google Drive:
    https://drive.google.com/file/d/1DcO7Q9ZcLcJgWqV_YiL8yP0evhBO4ZBy/view?usp=drive_link
    ###############################/-------GOOGLE DRIVE FILE ID------/##########################
    Se requiere el ID del archivo para descargarlo directamente, no todo el link.
    Recuerda que el archivo debe ser público para que se pueda descargar sin problemas 
    (al menos con permiso de visualización).
'''

@st.cache_data
def load_airbnb_data():
    # Reemplaza esto con el ID real del archivo en tu Drive
    FILE_ID = "1DcO7Q9ZcLcJgWqV_YiL8yP0evhBO4ZBy"
    """Carga el CSV de Airbnb directamente desde Google Drive."""
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

    df = pd.read_csv(url)

    return df
