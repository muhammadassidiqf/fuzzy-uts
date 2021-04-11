import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title('Fuzzy Logic Implementasi')

out_name_a=[]
var_name_a=[]
sat_name_a=[] 
jika1_name=[] 
jika2_name=[] 
min_val=[] 
max_val=[] 
min_name=[] 
max_name=[] 
op_fuz = []
# op_fuz2 = []
def himp(e,r):
    co1, co2, co3, co4 = st.beta_columns([.5,.5,.5,.5])
    nilai_min = 0
    nilai_max = 0
    istilah_min = ''
    istilah_max = ''
    for i in range(int(e)):
        nilai_min = co1.number_input('Nilai Minimum '+str(r)+' '+str(i+1), min_value=0)
        istilah_min = co2.text_input('Istilah Minimum '+str(r)+' '+str(i+1))
        nilai_max = co3.number_input('Nilai Maximum '+str(r)+' '+str(i+1), min_value=0)
        istilah_max = co4.text_input('Istilah Maximum '+str(r)+' '+str(i+1))
    return ((nilai_min,istilah_min),(nilai_max,istilah_max))


def get(a):
    for i in a[0]:    
        jika1_name.append((i[0],i[1],i[2]))
    return jika1_name

def get2(a):
    for i in a[1]:    
        jika2_name.append(i)
    return jika2_name

def calc_fuzz1(e, f, g):
    res = 0
    for i in range(len(e)):
        res = (f[i]-e[i])/(f[i]-g[i])
    return res

def calc_fuzz2(e, f, g):
    res = 0
    for i in range(len(e)):
        res = (e[i]-g[i])/(f[i]-g[i])
    return res



var_number = st.number_input('Masukan jumlah Variabel', min_value=0, max_value=10)
col1, col2, col3, col4,col5 = st.beta_columns([.5,.5,.5,.5,.5])
for i in range(int(var_number)):
    out_name = col1.selectbox('Tipe Variabel '+str(i+1),('Output ','Input '))
    var_name = col2.text_input('Nama Variabel '+str(i+1))
    sat_name = col3.text_input('Satuan '+str(i+1))
    case_num = col4.number_input('Masukan Jumlah Case '+str(i+1), min_value=0)
    himp_num = col5.number_input('Masukan Jumlah Himpunan '+str(i+1), min_value=0, max_value=10)
    a = himp(himp_num, var_name)
    out_name_a.append((out_name, var_name, sat_name, case_num, a))

for i in out_name_a:
    if 'Input' in i[0]:
        st.text('Variabel '+str(i[1]))
        st.text(str(i[4][0][1])+': '+str(calc_fuzz1([i[3]],[i[4][1][0]],[i[4][0][0]])))
        min_rul = i[1],(i[4][0][1]),(calc_fuzz1([i[3]],[i[4][1][0]],[i[4][0][0]]))
        st.text(str(i[4][1][1])+': '+str(calc_fuzz2([i[3]],[i[4][1][0]],[i[4][0][0]])))
        max_rul = i[1],(i[4][1][1]),(calc_fuzz2([i[3]],[i[4][1][0]],[i[4][0][0]]))
        op_fuz.append((min_rul, max_rul))
# st.write(op_fuz[0])
   
# st.write(get(op_fuz))
# st.write(get2(op_fuz))
# st.text(str(get(op_fuz)))

rule_num = st.number_input('Masukan jumlah rules', min_value=0, max_value=10)
for i in range (int(rule_num)):
    c1, c2, c3 = st.beta_columns([1,1,1])
    jika1 = c1.selectbox('Jika Variabel '+str(i+1),get(op_fuz))
    dan1 = c2.selectbox('Dan Variabel '+str(i+1),get2(op_fuz))
    # maka1 = c3.selectbox('Maka Variabel '+str(i+1),get(out_name_a))


# st.write(out_name_a)
   