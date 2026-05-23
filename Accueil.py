# Zoriak - Outils et Ressources
# Importation des bibliothèques nécessaires
import streamlit as st
# Configuration de la page
st.set_page_config(page_title="Zoriak - Outils et Ressources", page_icon=":star:", layout="wide")
# Contenu de la page
st.title("Bienvenue sur le site de Zoriak ❤️")
st.write(
    "Vous trouverez ici des outils et des liens vers des ressources utiles."
)
st.divider()
st.header("Liens utiles")
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("GitHub du projet", "https://github.com/Zoriak-DK/Zoriak_WebSite")
with col2:
    st.link_button("OpenStreetMap", "https://www.openstreetmap.org/")
with col3:
    st.link_button("Documentation de Streamlit", "https://docs.streamlit.io/")