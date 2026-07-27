import streamlit as st
import pandas as pd

st.set_page_config(page_title="Zoriak - Colocalisation d'éléments", page_icon="🔎", layout="wide")
st.title("Colocalisation d'éléments")
st.header("Détecter les éléments se trouvant au même endroit, au même moment dans un fichier CSV")
st.divider()

csv = st.file_uploader("Fichier CSV en entrée", type="csv")
if csv is not None:
    df = pd.read_csv(csv, sep=";")
    st.dataframe(df.head())
    col = st.multiselect("Champs à conserver", df.columns)
    df_filtered = df.filter(items=col)
    st.dataframe(df_filtered.head())
    st.divider()
    st.subheader("Paramétrage de l'outil")
    st.write("Sélectionnez les options qui vous intéresse pour le traitement.")
    type_coloc = st.selectbox("Colocalisation spatial ou spatio-temporel", {"spatial", "spatio-temporel"})
    if type_coloc == "spatio-temporel":
        ecart_temp = st.number_input("Intervalle de temps maximum (minutes)", 0, 60)
    ecart_distance = st.number_input("Intervalle de distance maximum (mètres)", 0, 1000)