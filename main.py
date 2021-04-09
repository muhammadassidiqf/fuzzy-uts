import streamlit as st

st.title('Fuzzy Logic Implementasi')
col1, col2, col3 = st.beta_columns(3)

home = st.button("Home","Home")
fungsi = st.button("Fungsi","Fungsi")
fuzzy = st.button("Fuzzy","Fuzzy")

if home:
    st.subheader('Nama : Muhammad Assidiq Fattah')
    st.subheader('NRP : 152017015')
elif fungsi:
    st.subheader('Fungsi Fuzzy Logic')