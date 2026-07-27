import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import Draw

st.set_page_config(page_title="Zoriak - Carte interactive", page_icon="🗺️", layout="wide")

# Titre et description de la carte
st.title("Carte Interactive de Zoriak")
st.markdown(
    """
    Explorez cette carte interactive pour ajouter des points géoréférencés.
    Vous pouvez :
    - Cliquer sur la carte pour ajouter un point
    - Entrer des coordonnées manuellement (format Latitude, Longitude)
    """
)

# Initialisation de Folium et ajout d'une carte basique centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=10)
Draw(export=True).add_to(m)

c1, c2 = st.columns(2)
with c1:
    output = st_folium(m, width=700, height=500)

with c2:
    st.write(output)