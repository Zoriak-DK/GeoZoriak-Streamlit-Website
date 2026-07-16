import streamlit as st
import mgrs
import folium
from streamlit_folium import st_folium
from tools.Conversions import *
from tools.DisplayFolium import display_folium

st.title("Convertisseur de coordonnées DMS vers MGRS")
st.write("Entrez les coordonnées en degrés, minutes et secondes (DMS) pour les convertir en coordonnées MGRS.")
st.divider()
# Champs de saisie pour les coordonnées DMS
latitude_dms = st.text_input("Latitude (DMS)", "48°51'29\"N")
longitude_dms = st.text_input("Longitude (DMS)", "2°17'40\"E")
# Bouton de conversion
if st.button("Convertir en MGRS"):
    try:
        lat_decimal = dms_to_decimal(latitude_dms)
        lon_decimal = dms_to_decimal(longitude_dms)
        
        # Convertir les coordonnées décimales en MGRS
        mgrs_coord = decimal_to_mgrs(lat_decimal, lon_decimal)
        
        st.success(f"Coordonnées MGRS : {mgrs_coord}")
        st.divider()

        display_folium(lat_decimal, lon_decimal)

    except Exception as e:
        st.error(f"Erreur lors de la conversion : {e}")

