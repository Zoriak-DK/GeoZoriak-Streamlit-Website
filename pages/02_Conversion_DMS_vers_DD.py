import streamlit as st
from tools.Conversions import dms_to_decimal

st.set_page_config(page_title="Zoriak - Conversion de coordonnées", page_icon="🌍", layout="wide")
st.title("Convertisseur de coordonnées DMS vers DD")
st.write("Entrez les coordonnées en degrés, minutes et secondes (DMS) pour les convertir en degrés décimaux (DD).")
st.divider()

# Champs de saisie pour les coordonnées DMS
latitude_dms = st.text_input("Latitude (DMS)", "48°51'29\"N")
longitude_dms = st.text_input("Longitude (DMS)", "2°17'40\"E")

# Bouton de conversion
if st.button("Convertir en DD"):
    try:
        lat_decimal = dms_to_decimal(latitude_dms)
        lon_decimal = dms_to_decimal(longitude_dms)

        st.success(f"Coordonnées en degrés décimaux : Latitude {lat_decimal:.6f}, Longitude {lon_decimal:.6f}")

    except Exception as e:
        st.error(f"Erreur lors de la conversion : {e}")