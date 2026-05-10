import streamlit as st
st.title("Convertisseur de coordonnées DMS vers DD")
st.write("Entrez les coordonnées en degrés, minutes et secondes (DMS) pour les convertir en degrés décimaux (DD).")
st.divider()
# Champs de saisie pour les coordonnées DMS
latitude_dms = st.text_input("Latitude (DMS)", "48°51'29\"N")
longitude_dms = st.text_input("Longitude (DMS)", "2°17'40\"E")
# Bouton de conversion
if st.button("Convertir en DD"):
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
        
        st.success(f"Coordonnées en degrés décimaux : Latitude {lat_decimal:.3f}, Longitude {lon_decimal:.3f}")
    except Exception as e:
        st.error(f"Erreur lors de la conversion : {e}")