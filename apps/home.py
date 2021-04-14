import streamlit as st

# st.set_page_config(layout="wide")
def app():
    st.title('UTS Pemrograman Simulai')
    st.title('Fuzzy Mamdani')
    co1, co2 = st.beta_columns([1,1])
    co1.subheader('Nama : Muhammad Assidiq Fattah')
    co1.subheader('NRP : 152017015')
    co2.subheader('Nama : Syahrul Fathurrahman Erawan')
    co2.subheader('NRP : 152017030')

    st.write('')
    st.write(
        """
    Sistem implementasi Fuzzy Mamdani ini dibangun menggunakan bahasa pemrograman python dibantu tools distribusi python yang berisikan paket-paket library yaitu anaconda, sistem ini pun dibangun berbasis web menggunakan library streamlit dalam membantu proses pembangunan tampilan antarmuka nya.
        """
    )