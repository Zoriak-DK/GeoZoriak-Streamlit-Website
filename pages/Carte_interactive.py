import streamlit as st
from tools.DisplayFolium import display_folium
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

st.set_page_config(page_title="Zoriak - Carte interactive", page_icon="🗺️", layout="wide")

# Titre et description de la carte
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Carte Interactive de Zoriak")
    st.markdown(
        """
        Explorez cette carte interactive pour ajouter des points géoréférencés.
        Vous pouvez :
        - Cliquer sur la carte pour ajouter un point
        - Entrer des coordonnées manuellement (format Latitude, Longitude)
        """
    )
with col2:
    pass

# Initialisation de Folium et ajout d'une carte basique centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=10)

# Fonction pour ajouter un point à la carte
def add_point_to_map(latitude, longitude):
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        popup=f"Lat: {latitude}, Lon: {longitude}"
    ).add_to(m)

# Zone pour ajouter des coordonnées manuellement
st.sidebar.header("Ajouter un point")
col_sidebar = st.sidebar.columns(2)
with col_sidebar[0]:
    latitude_input = st.text_input("Latitude:", "48.8566", key="latitude_input")
with col_sidebar[1]:
    longitude_input = st.text_input("Longitude:", "2.3522", key="longitude_input")

# Bouton pour ajouter le point manuellement
if st.sidebar.button("Ajouter un point"):
    try:
        latitude, longitude = float(latitude_input), float(longitude_input)
        add_point_to_map(latitude, longitude)
        st.success(f"Point ajouté avec succès à ({latitude}, {longitude})")
    except ValueError:
        st.error("Veuillez entrer des nombres valides pour les coordonnées.")

# Zone pour interagir avec la carte
st.subheader("Carte Interactive")

# Affichage de la carte interactive
display_folium(latitude_input, longitude_input)

# Zone pour afficher les points ajoutés manuellement
st.subheader("Points ajoutés manuellement")
if "new_point" in st.session_state:
    with st.expander("Voir tous les points"):
        for point in st.session_state.get("points", []):
            st.write(f"Latitude: {point['lat']}, Longitude: {point['lon']}")

# Sauvegarde des points dans la session state
if "points" not in st.session_state:
    st.session_state["points"] = []

st.session_state["points"].append({"lat": float(latitude_input), "lon": float(longitude_input)})