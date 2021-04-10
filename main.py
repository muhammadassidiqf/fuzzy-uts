import streamlit as st
import pandas as pd
import numpy as np

st.title('Fuzzy Logic Implementasi')

# home = col1.button("Home","Home")
# fungsi = col2.button("Fungsi","Fungsi")
# fuzzy = col3.button("Fuzzy","Fuzzy")

# if home:
#     col1, col2 = st.beta_columns([1,1])
#     col1.subheader('Nama : Muhammad Assidiq Fattah')
#     col1.subheader('NRP : 152017015')
#     col2.subheader('Nama : Syahrul Fathurahman Erawan')
#     col2.subheader('NRP : 152017030')
# elif fungsi:
#     st.subheader('Fungsi Fuzzy Logic')
# elif fuzzy:
#     st.subheader('Implementasi Fuzzy Logic')
out_name_a=[]
var_name_a=[]
sat_name_a=[] 
def himp(e,r):
    co1, co2, co3, co4 = st.beta_columns([.5,.5,.5,.5])
    himp_num_a=[] 
    for i in range(int(e)):
        nilai_min = co1.number_input('Nilai Minimum '+str(r)+' '+str(i+1), min_value=0)
        istilah_min = co2.text_input('Istilah Minimum '+str(r)+' '+str(i+1))
        nilai_max = co3.number_input('Nilai Maximum '+str(r)+' '+str(i+1), min_value=0)
        istilah_max = co4.text_input('Istilah Maximum '+str(r)+' '+str(i+1))
        himp_num_a.append(((nilai_min,istilah_min),(nilai_max,istilah_max)))
    return himp_num_a

var_number = st.number_input('Masukan jumlah Variabel', min_value=0, max_value=10)
col1, col2, col3, col4 = st.beta_columns([.5,.5,.5,.6])
for i in range(int(var_number)):
    out_name = col1.selectbox('Tipe Variabel '+str(i+1),('Output ','Input '))
    var_name = col2.text_input('Nama Variabel '+str(i+1))
    sat_name = col3.text_input('Satuan '+str(i+1))
    himp_num = col4.number_input('Masukan Jumlah Himpunan '+str(i+1), min_value=0, max_value=10)
    a = himp(himp_num, var_name)
    out_name_a.append(((out_name, var_name, sat_name, a)))
   
    # var_name_a.append((out_name_a[i], himp(himp_num)))
    # sat_name_a.append(sat_name)
    # b = var_name_a.append(himp_num)
    # himp(b,a)

rule_num = st.number_input('Masukan jumlah rules', min_value=0, max_value=10)
for i in range(int(rule_num)):
    out_name = col1.selectbox('Jika '+str(i+1),(i[1]))

out_name_ab = np.array([out_name_a])  
col1.write('Tabel Tipe Variabel')
st.write(out_name_a)
for i in out_name_a:    
    st.write(i[1])
# var_name_ab = np.array([var_name_a])  
# col2.write('Tabel Variabel Name')
# col2.write(var_name_a)
# sat_name_ab = np.array([sat_name_a])  
# col3.write('Tabel Satuan Name')
# col3.write(sat_name_a)
# col4.write(himp_num_a)