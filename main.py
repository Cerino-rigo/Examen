import streamlit as st 
st.set_page_config(page_title="Data manager", page_icon="📈", layout="wide")

Airbnb = st.Page("Menu/page3.py", title="Resumen General de Airbnb", icon=":material/analytics:")

pg = st.navigation(
        {
            "MENÚ PRINCIPAL": [Airbnb],
            
        })
    

pg.run()
