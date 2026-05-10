import streamlit as st
import mgrs
import folium
from streamlit_folium import st_folium
st.title("Convertisseur de coordonnées DMS vers MGRS")
st.write("Entrez les coordonnées en degrés, minutes et secondes (DMS) pour les convertir en coordonnées MGRS.")
st.divider()
# Champs de saisie pour les coordonnées DMS
latitude_dms = st.text_input("Latitude (DMS)", "48°51'29\"N")
longitude_dms = st.text_input("Longitude (DMS)", "2°17'40\"E")
# Bouton de conversion
if st.button("Convertir en MGRS"):
    try:
        # Convertir les coordonnées DMS en degrés décimaux
        def dms_to_decimal(dms):
            parts = dms[:-1].split('°')
            degrees = float(parts[0])
            if len(parts) > 1:
                minutes = float(parts[1].split("'")[0]) if "'" in parts[1] else 0
            else:
                minutes = 0
            if len(parts) > 2:
                seconds = float(parts[2].split('"')[0]) if '"' in parts[2] else 0
            else:
                seconds = 0
            decimal = degrees + (minutes / 60) + (seconds / 3600)
            if dms.endswith('S') or dms.endswith('W'):
                decimal *= -1
            return decimal
        
        lat_decimal = dms_to_decimal(latitude_dms)
        lon_decimal = dms_to_decimal(longitude_dms)
        
        # Convertir les coordonnées décimales en MGRS
        m = mgrs.MGRS()
        mgrs_coord = m.toMGRS(lat_decimal, lon_decimal)
        
        st.success(f"Coordonnées MGRS : {mgrs_coord}")
        st.divider()
        st.header("Visualisation sur la carte")
        # Créer une carte centrée sur les coordonnées
        m = folium.Map(location=[lat_decimal, lon_decimal], zoom_start=15)
        # Ajouter un marqueur pour les coordonnées
        folium.Marker(
            [lat_decimal, lon_decimal],
            popup="Coordonnées DMS",
            tooltip="Coordonnées DMS"
            ).add_to(m)
        # Afficher la carte dans Streamlit
        st_data = st_folium(m, width=700, height=700)
    except Exception as e:
        st.error(f"Erreur lors de la conversion : {e}")

