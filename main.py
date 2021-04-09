import streamlit as st

st.title('Fuzzy Logic Implementasi')
col1, col2, col3 = st.beta_columns([.1,.1,.1])

home = col1.button("Home","Home")
fungsi = col2.button("Fungsi","Fungsi")
fuzzy = col3.button("Fuzzy","Fuzzy")

if home:
    col1, col2 = st.beta_columns([1,1])
    col1.subheader('Nama : Muhammad Assidiq Fattah')
    col1.subheader('NRP : 152017015')
    col2.subheader('Nama : Syahrul Fathurahman Erawan')
    col2.subheader('NRP : 152017030')
elif fungsi:
    st.subheader('Fungsi Fuzzy Logic')
elif fuzzy:
    st.subheader('Implementasi Fuzzy Logic')