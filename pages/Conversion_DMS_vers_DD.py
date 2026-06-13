import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Convertisseur de coordonnées DMS vers DD")
st.write("Entrez les coordonnées en degrés, minutes et secondes (DMS) pour les convertir en degrés décimaux (DD).")
st.divider()

# Champs de saisie pour les coordonnées DMS
latitude_dms = st.text_input("Latitude (DMS)", "48°51'29\"N")
longitude_dms = st.text_input("Longitude (DMS)", "2°17'40\"E")

# Fonction de conversion DMS -> DD
def dms_to_decimal(dms: str) -> float:
    dms = dms.strip().upper().replace(' ', '')
    if not dms:
        raise ValueError("Veuillez saisir une coordonnée DMS.")
    if dms[-1] not in ['N', 'S', 'E', 'W']:
        raise ValueError("Le format DMS doit se terminer par N, S, E ou W.")

    direction = dms[-1]
    value = dms[:-1]

    if '°' not in value:
        raise ValueError("Le format DMS doit contenir des degrés (°).")

    degrees_part, rest = value.split('°', 1)
    degrees = float(degrees_part) if degrees_part else 0.0
    minutes = 0.0
    seconds = 0.0

    if "'" in rest:
        minutes_part, rest = rest.split("'", 1)
        minutes = float(minutes_part) if minutes_part else 0.0
    if '"' in rest:
        seconds_part = rest.split('"', 1)[0]
        seconds = float(seconds_part) if seconds_part else 0.0

    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# Bouton de conversion
if st.button("Convertir en DD"):
    try:
        lat_decimal = dms_to_decimal(latitude_dms)
        lon_decimal = dms_to_decimal(longitude_dms)

        st.success(f"Coordonnées en degrés décimaux : Latitude {lat_decimal:.6f}, Longitude {lon_decimal:.6f}")

        # Carte interactive pour afficher le point converti
        map_center = [lat_decimal, lon_decimal]
        m = folium.Map(location=map_center, zoom_start=12)
        folium.Marker(
            location=map_center,
            popup=f"Latitude : {lat_decimal:.6f}<br>Longitude : {lon_decimal:.6f}",
            tooltip="Position convertie"
        ).add_to(m)

        st.write("### Visualisation sur la carte")
        st_folium(m, width=700, height=450)

    except Exception as e:
        st.error(f"Erreur lors de la conversion : {e}")