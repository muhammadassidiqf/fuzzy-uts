import streamlit as st
from main import Main
from apps import home, teori, implementasi

st.set_page_config(layout="wide")
app = Main()
app.add_app("Home", home.app)
app.add_app("Fuzzy Logic", teori.app)
app.add_app("Implementasi Fuzzy Mamdani", implementasi.app)

app.run()