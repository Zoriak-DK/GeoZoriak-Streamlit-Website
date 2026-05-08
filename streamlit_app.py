import streamlit as st

st.title("Bienvenue sur le site de Zoriak ❤️")
st.write(
    "Vous trouverez ici des outils et des liens vers des ressources utiles."
)
st.divider()
st.header("Liens utiles")
st.link_button("GitHub du projet", "https://github.com/Zoriak-DK/Zoriak_WebSite")
st.link_button("OpenStreetMap", "https://www.openstreetmap.org/")
st.link_button("Documentation de Streamlit", "https://docs.streamlit.io/")
st.divider()
st.header("Outils")
st.write("Voici quelques outils que vous pouvez utiliser :")
st.button("Outil 1")
st.button("Outil 2")
st.button("Outil 3")