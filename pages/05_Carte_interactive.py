import streamlit as st
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium

st.set_page_config(page_title="Zoriak - Carte interactive", page_icon="🗺️", layout="wide")

st.title("Carte Interactive de Zoriak")
st.markdown(
    """
    Explorez cette carte interactive pour ajouter ou visualiser des points géoréférencés.
    - Cliquez sur la carte pour récupérer les coordonnées
    - Utilisez l'outil de dessin pour ajouter des formes
    - Entrez des coordonnées manuellement si besoin
    """
)

m = folium.Map(location=[48.8566, 2.3522], zoom_start=6)
folium.Marker([48.8566, 2.3522], tooltip="Paris").add_to(m)
Draw(export=True, position="topleft").add_to(m)

left_col, right_col = st.columns([2, 1])

with left_col:
    map_data = st_folium(m, key="map", width=700, height=500)

with right_col:
    st.subheader("Informations")

    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]
        st.success(f"Dernier clic : Latitude {lat:.5f}, Longitude {lon:.5f}")
    else:
        st.info("Cliquez sur la carte pour obtenir les coordonnées.")

    if map_data and map_data.get("all_drawings"):
        st.json(map_data["all_drawings"])

    lat_input = st.number_input("Latitude", value=48.8566, min_value=-90.0, max_value=90.0, step=0.0001)
    lon_input = st.number_input("Longitude", value=2.3522, min_value=-180.0, max_value=180.0, step=0.0001)
    if st.button("Centrer la carte"):
        m.location = [lat_input, lon_input]
        st.rerun()