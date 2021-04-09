import streamlit as st
import pandas as pd
import numpy as np

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

var_number = st.number_input('Masukan jumlah Variabel')
var_number = int(var_number)

var_name_a=[]
for i in range(var_number):
    var_name = st.text_input('Variabel Name' +" "+str(i)+" = ")
    var_name_a.append(var_name)

var_name_ab = np.array([var_name_a])  
st.write('Tabel Variabel Name')
st.write(var_name_ab)


