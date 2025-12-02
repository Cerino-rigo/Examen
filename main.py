import streamlit as st 
st.set_page_config(page_title="Data manager", page_icon="📈", layout="wide")

# Sidebar
#st.sidebar.write(
#    "<h1 style='text-align: center;'>🎮 Menú del Examen</h1>",
#    unsafe_allow_html=True
#)

Home = st.Page("Menu/page1.py", title="Análisis por Usuario", icon=":material/home:")
Predicciones = st.Page("Menu/page2.py", title= "Análisis General", icon=":material/track_changes:")
Airbnb = st.Page("Menu/page3.py", title="Resumen General de Airbnb", icon=":material/analytics:")

pg = st.navigation(
        {
            "MENÚ PRINCIPAL": [Home, Predicciones, Airbnb],
            
        })
    
#pg = st.navigation([Home, Predicciones])

pg.run()

#st.title("Página principal")