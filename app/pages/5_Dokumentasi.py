import streamlit as st

st.set_page_config(
    page_title="Dokumentasi",
    page_icon="📄"
)

st.title("Dokumentasi Proyek")

st.markdown("""
Halaman ini menjelaskan informasi lengkap mengenai proyek
**Analisis Sentimen Ulasan Film IMDb Menggunakan Multinomial Naive Bayes**,
mulai dari dataset, metodologi, hingga cara menggunakan aplikasi.
""")

st.divider()

# =====================================================
# DESKRIPSI PROYEK
# =====================================================

st.header("1. Deskripsi Proyek")

st.write("""
Proyek ini bertujuan untuk membangun sistem analisis sentimen
yang mampu mengklasifikasikan ulasan film IMDb menjadi
**sentimen positif** atau **sentimen negatif**.

Model yang digunakan adalah **Multinomial Naive Bayes**
dengan representasi fitur menggunakan **TF-IDF Vectorizer**.
Model ini dipilih karena memiliki performa yang baik
dalam klasifikasi teks serta proses pelatihan yang cepat.
""")

st.divider()

# =====================================================
# DATASET
# =====================================================

st.header("2. Dataset")

st.markdown("""
**Nama Dataset**
- IMDb Movie Reviews Dataset

**Sumber Dataset**
- https://ai.stanford.edu/~amaas/data/sentiment/

**Informasi Dataset**
- Jumlah data: **50.000 ulasan film**
- Kelas: **Positive** dan **Negative**
- Format data: Teks
- Bahasa: Inggris
- Distribusi kelas: Seimbang (Balanced Dataset)
""")

st.divider()

# =====================================================
# METODOLOGI
# =====================================================

st.header("3. Metodologi")

st.markdown("""
Tahapan pengembangan model:

1. Pengumpulan Dataset
2. Exploratory Data Analysis (EDA)
3. Text Preprocessing
4. TF-IDF Vectorization
5. Training Model Multinomial Naive Bayes
6. Evaluasi Model
7. Deployment menggunakan Streamlit
""")

st.divider()

# =====================================================
# PREPROCESSING
# =====================================================

st.header("4. Tahapan Preprocessing")

st.markdown("""
Tahapan preprocessing yang dilakukan meliputi:

- Mengubah seluruh huruf menjadi lowercase
- Menghapus HTML Tag
- Menghapus URL
- Menghapus angka
- Menghapus tanda baca
- Menghapus karakter khusus
- Tokenisasi
- Stopword Removal
- Lemmatization

Tahapan tersebut bertujuan menghasilkan data teks yang lebih bersih
agar performa model menjadi lebih baik.
""")

st.divider()

# =====================================================
# MODEL
# =====================================================

st.header("5. Model Machine Learning")

st.markdown("""
Model yang digunakan:

- Algoritma : **Multinomial Naive Bayes**
- Feature Extraction : **TF-IDF Vectorizer**
- Jenis Klasifikasi : **Binary Classification**
- Output :
  - Sentimen Positif
  - Sentimen Negatif

Model dilatih menggunakan data latih kemudian dievaluasi
menggunakan data uji.
""")

st.divider()

# =====================================================
# HASIL EVALUASI
# =====================================================

st.header("6. Hasil Evaluasi Model")

st.table({
    "Metrik": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score",
        "ROC-AUC"
    ],
    "Nilai": [
        "85%",
        "85%",
        "85%",
        "85%",
        "92%"
    ]
})

st.info("""
Model menunjukkan performa yang baik dalam membedakan
ulasan positif dan negatif berdasarkan metrik evaluasi
yang telah diperoleh.
""")

st.divider()

# =====================================================
# STRUKTUR PROJECT
# =====================================================

st.header("7. Struktur Proyek")

st.code("""
project/
│
├── app/
│   ├── app.py
│   ├── pages/
│   └── assets/
│
├── data/
├── models/
├── notebooks/
├── src/
├── requirements.txt
└── README.md
""")

st.divider()

# =====================================================
# LIBRARY
# =====================================================

st.header("8. Library yang Digunakan")

st.code("""
pandas
numpy
matplotlib
seaborn
scikit-learn
nltk
streamlit
pickle
""")

st.divider()

# =====================================================
# MENJALANKAN APLIKASI
# =====================================================

st.header("9. Cara Menjalankan Aplikasi")

st.write("Install seluruh library:")

st.code("pip install -r requirements.txt", language="bash")

st.write("Jalankan aplikasi:")

st.code("streamlit run app/app.py", language="bash")

st.divider()

# =====================================================
# PENGGUNAAN
# =====================================================

st.header("10. Cara Menggunakan Aplikasi")

st.markdown("""
1. Buka halaman **Dashboard**.
2. Lihat hasil Exploratory Data Analysis (EDA).
3. Buka halaman **Prediksi Sentimen**.
4. Masukkan ulasan film pada kotak teks.
5. Klik tombol **Prediksi**.
6. Sistem akan menampilkan hasil sentimen.
7. Buka halaman **Evaluasi Model** untuk melihat performa model.
8. Buka halaman **Interpretasi Hasil** untuk memahami cara kerja model.
""")

st.divider()

# =====================================================
# KESIMPULAN
# =====================================================

st.header("11. Kesimpulan")

st.success("""
Aplikasi ini berhasil mengimplementasikan proses Machine Learning
secara end-to-end mulai dari pengumpulan data, preprocessing,
pelatihan model, evaluasi, hingga deployment menggunakan
Streamlit.

Model Multinomial Naive Bayes dengan TF-IDF Vectorizer
mampu melakukan klasifikasi sentimen ulasan film
dengan performa yang baik sehingga dapat digunakan
untuk membantu analisis opini pengguna secara otomatis.
""")