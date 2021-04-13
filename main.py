import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title('Fuzzy Logic Implementasi')

try:
    out_name_a=[]
    var_name_a=[]
    sat_name_a=[] 
    min_val=[] 
    max_val=[] 
    min_name=[] 
    max_name=[] 
    fuz = []
    imp = []
    kom = []
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
        jika1_name=[] 
        for i in a[0]:    
            jika1_name.append((i[0],i[1],i[2]))
        return jika1_name

    def get2(a):
        jika2_name=[] 
        for i in a[1]:    
            jika2_name.append(i)
        return jika2_name

    def get3(a):
        jika3_name=[] 
        for i in a:
            for j in i[4]:
                if 'Output' in i[0]:
                    jika3_name.append(j[1])
        return jika3_name


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

    def fuzzy(a, b):
        fuzzy = []
        bn = [a,b]
        return min(bn)

    def min_kom(a, b):
        komp_atu = []
        # for i in b:
        for j in range(len(b)):
            if b[j][2] in a:
                komp_atu.append(b[j][1])
        return min(komp_atu)

    def max_kom(a, b):
        komp_atu = []
        # for i in b:
        for j in range(len(b)):
            if b[j][2] in a:
                komp_atu.append(b[j][1])        
        return max(komp_atu)

    with st.beta_expander("Inisialisasi Variabel dan Data"):
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

    with st.beta_expander("Fuzzifikasi"):
        for i in out_name_a:
            if 'Input' in i[0]:
                st.text('Variabel '+str(i[1]))
                st.text(str(i[4][0][1])+': '+str(calc_fuzz1([i[3]],[i[4][1][0]],[i[4][0][0]])))
                min_rul = i[1],(i[4][0][1]),(calc_fuzz1([i[3]],[i[4][1][0]],[i[4][0][0]]))
                st.text(str(i[4][1][1])+': '+str(calc_fuzz2([i[3]],[i[4][1][0]],[i[4][0][0]])))
                max_rul = i[1],(i[4][1][1]),(calc_fuzz2([i[3]],[i[4][1][0]],[i[4][0][0]]))
                fuz.append((min_rul, max_rul))  
    # st.write(op_fuz[0])
    with st.beta_expander("Rules dan Implikasi"):
        rule_num = st.number_input('Masukan jumlah rules', min_value=0, max_value=10)
        for i in range (int(rule_num)):
            rule = st.text('[R'+str(i+1)+']')
            c1, c2, c3 = st.beta_columns([1,1,1])
            jika1 = c1.selectbox('Jika Variabel '+str(i+1),get(fuz))
            dan1 = c2.selectbox('Dan Variabel '+str(i+1),get2(fuz))
            maka1 = c3.selectbox('Maka Variabel '+str(i+1),get3(out_name_a))
            imp.append(('[R'+str(i+1)+']', fuzzy(jika1[2],dan1[2]), maka1))
        st.write(imp)
    with st.beta_expander("Komposisi Aturan"):
        for i in out_name_a:
            if 'Output' in i[0]:
                min_kom = min_kom((i[4][0][1]), imp)
                # st.write(min_kom)
                max_kom = max_kom((i[4][1][1]),imp)
                # st.write(max_kom)
                kom.append((min_kom, max_kom))
                st.text(str(i[4][0][1])+': '+str(min_kom))
                st.text(str(i[4][1][1])+': '+str(max_kom))
except ZeroDivisionError:
  # Prevent the error from propagating into your Streamlit app.
    pass

except ValueError:
    pass

    # st.write(kom)     
# st.write(imp)   
# st.write(out_name_a)   