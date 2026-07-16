import streamlit as st
import streamlit_folium as stf
import folium as f

def display_folium(lat_decimal, lon_decimal):
    st.title("Affichage géographique avec Folium")
    folium_map = f.Map([lat_decimal, lon_decimal], zoom_start=10)
    stf.folium_static(folium_map)

