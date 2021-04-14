import streamlit as st
from PIL import Image

# st.title('Teori Fuzzy Logic')
# st.set_page_config(layout="wide")   
def app():
    with st.beta_expander("⚙️ Definisi Logika Fuzzy ", expanded=False):
        st.write(
            """    
    - Logika fuzzy yang pertama kali diperkenalkan oleh Lotfi A. Zadeh, memiliki derajat keanggotaan dalam rentang 0(nol) hingga 1(satu), berbeda dengan logika digital yang hanya memiliki dua nilai yaitu 1(satu) atau 0(nol).
    - Logika fuzzy digunakan untuk menerjemahkan suatu besaran yang diekspresikan menggunakan bahasa (linguistic), misalkan besaran kecepatan laju kendaraan yang diekspresikan dengan pelan, agak cepat, cepat dan sangat cepat.
            """
        )

    with st.beta_expander("⚙️ Pengertian Fuzzy ", expanded=False):
        st.write(
            """    
    - Secara teknis, sistem fuzzy adalah sistem yang terdefinisi secara akurat.
    - Fuzzy logic bukan suatu logika yang fuzzy, tetapi logika yang menjelaskan ke-fuzzy-an.
    - Fuzzy logic meletakkan ide bahwa segala sesuatu hal mengenal/memiliki derajat:
        - Misal : suhu, jarak, kecantikan, kebahagiaan; yang seluruhnya memiliki ‘sliding scale’ tertentu.
            """
        )

    with st.beta_expander("⚙️ Latar Belakang ", expanded=False):
        st.write(
            """    
    - Logika fuzzy adalah teknologi yang dibuat sekaligus diabaikan di U.S. Jepang mengambil dan mengembangkan teknologi tersebut menjadi suatu keuntungan, kemudian dijual kembali ke U.S.
    - Logika fuzzy ditemukan pada tahun 1964 oleh Lotfi Zadeh.
            """
        )

    with st.beta_expander("⚙️ Alasan Menggunakan Fuzzy ", expanded=False):
        st.write(
            """    
    - Konsep logika fuzzy mudah dimengerti.
    - Logika fuzzy sangat fleksibel.
    - Memiliki toleransi terhadap data-data yang tidak tepat.
    - Dapat membangun dan mengaplikasikan pengalaman-pengalaman para pakar secara langsung tanpa harus melalui proses pelatihan.
            """
        )

    with st.beta_expander("⚙️ Proses Inferensi Fuzzy ", expanded=False):
        st.write(
            """    
    - Menginterpretasikan nilai-nilai pada vektor masukan dan menentukan nilai-nilai pada vektor keluaran berdasarkan beberapa aturan if-then fuzzy.
    - Keseluruhan aturan dievaluasi secara paralel dan urutan setiap aturan tidak penting.
    - Aturan if-then dikumpulkan dari berbagai kepakaran manusia.
    - Logika fuzzy merefleksikan cara berpikir manusia:
        - Memodelkan ‘human sense of words’.
        - Memodelkan cara manusia mengambil keputusan.
        - Memodelkan cara mengenali sesuatu yang terlihat dan terdengar.
        - Mencerminkan fungsi otak : mendeteksi warna dan membedakan suatu fenomena.
            """
        )

    with st.beta_expander("⚙️ Manfaat Logika Fuzzy ", expanded=False):
        st.write(
            """    
    - Menurut Bart Kosko, profesor di University of Southern California, logika fuzzy dapat menghasilkan sesuatu yang mengagumkan, seperti:
        - Ahli pengambil keputusan, secara teori dapat membuat pertimbangan berdasarkan seluruh dokumen yang pernah ditulis.
        - Kendaraan cerdas dengan perangkat sonar yang dapat mengatur pengereman mendadak. Dengan fuzzy navigator, peta terkomputerisasi, serta perangkat transmitter dan receiver pada aspal, suatu kendaraan dapat mengendalikan dirinya sendiri.
        - Robot seperti manusia, yang dapat meniru perilaku manusia.
            """
        )

    with st.beta_expander("⚙️ Sistem Berbasis Aturan Fuzzy ", expanded=False):
        st.write(
            """    
    - Sistem berbasis aturan fuzzy yang lengkap terdiri dari tuga komponen utama:
        - Fuzzification
        - Inference
        - Defuzzification
            """
        )
        st.write(
            """    
    - Diagram Blok
            """
        )
        image = Image.open('AturanFuzzy.png')
        st.image(image, caption='Sunrise by the mountains')
        st.write(
            """    
    - Penjelasan Diagram Blok:
        - Fuzzification mengubah input-input yang nilai kebenarannya bersifat pasti (crisp input) ke dalam bentuk fuzzy input, yang berupa nilai linguistik yang semantiknya ditentukan berdasarkan fungsi keanggotaan tertentu. 
        - Inference melakukan penalaran menggunakan fuzzy input dan fuzzy rules yang telah ditentukan sehingga menghasilkan fuzzy output.
        - Defuzzification mengubah fuzzy output menjadi crisp value berdasarkan fungsi keanggotaan yang telah ditentukan.
            """
        )

    with st.beta_expander("⚙️ Fuzzy Mamdani ", expanded=False):
        st.write(
            """    
    - Pada model ini, aturan fuzzy didefinisikan sebagai : 
        - IF x1 is A1 AND…AND xn is An THEN y is B.
    - Dimana A1…..An dan B adalah nilai-nilai linguistik (atau fuzzy set) dan “x1 is A1” menyatakan bahwa nilai variabel x1 adalah anggota fuzzy set A1.
            """
        )

