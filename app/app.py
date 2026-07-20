import streamlit as st

# ==========================
# Konfigurasi Halaman
# ==========================
st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="wide"
)

# ==========================
# Header
# ==========================
st.title("🎬 Movie Review Sentiment Analysis")

st.markdown("""
### Analisis Sentimen Ulasan Film Menggunakan Metode Naïve Bayes

Aplikasi ini dibangun untuk mengklasifikasikan ulasan film menjadi **Positive** atau **Negative** menggunakan algoritma **Multinomial Naïve Bayes**.

Dataset yang digunakan adalah **IMDb Movie Review Dataset** yang terdiri dari **50.000 ulasan film**.
""")

st.divider()

# ==========================
# Informasi Singkat
# ==========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Dataset",
        value="50.000 Review"
    )

with col2:
    st.metric(
        label="Model",
        value="Naïve Bayes"
    )

with col3:
    st.metric(
        label="Accuracy",
        value="84.88%"
    )

st.divider()

# ==========================
# Tentang Proyek
# ==========================
st.header("Tentang Proyek")

st.write("""
Analisis sentimen merupakan salah satu penerapan **Natural Language Processing (NLP)** yang bertujuan untuk mengetahui opini seseorang terhadap suatu objek.

Pada proyek ini dilakukan klasifikasi sentimen terhadap ulasan film menggunakan algoritma **Multinomial Naïve Bayes**.

Dataset berasal dari **IMDb Movie Review Dataset** yang berisi 50.000 ulasan film berbahasa Inggris dengan dua kelas sentimen, yaitu:

- Positive
- Negative
""")

# ==========================
# Tujuan
# ==========================
st.header("Tujuan")

st.markdown("""
- Mengidentifikasi sentimen ulasan film secara otomatis.

- Menerapkan algoritma Multinomial Naïve Bayes pada kasus klasifikasi teks.

- Mengevaluasi performa model menggunakan Accuracy, Precision, Recall, F1-Score, Confusion Matrix, dan ROC Curve.

- Menyediakan aplikasi berbasis Streamlit yang mudah digunakan.
""")

# ==========================
# Workflow
# ==========================
st.header("Alur Sistem")

st.markdown("""
1. Dataset IMDb
2. Text Preprocessing
3. TF-IDF Vectorization
4. Naïve Bayes Classification
5. Sentiment Prediction
""")

st.divider()

# ==========================
# Sidebar Information
# ==========================
st.success("Pilih menu pada sidebar untuk mulai menggunakan aplikasi.")

st.sidebar.title("Navigasi")

st.sidebar.info("""
Gunakan menu berikut:

Home

Dashboard EDA

Prediksi

Evaluasi Model

Interpretasi

Dokumentasi
""")