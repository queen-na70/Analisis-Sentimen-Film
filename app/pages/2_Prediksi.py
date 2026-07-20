import streamlit as st
import joblib
import nltk
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

from preprocessing import preprocess_text

# ==========================================================
# DOWNLOAD NLTK
# ==========================================================

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("corpora/omw-1.4")
except LookupError:
    nltk.download("omw-1.4")

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Prediksi Sentimen",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

textarea{
    font-size:16px !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    model = joblib.load(
        os.path.join(PROJECT_ROOT, "models", "best_model.pkl")
    )

    vectorizer = joblib.load(
        os.path.join(PROJECT_ROOT, "models", "tfidf_vectorizer.pkl")
    )

    return model, vectorizer

model, vectorizer = load_model()

# ==========================================================
# HEADER
# ==========================================================

st.title("Prediksi Sentimen Film")

st.write("""
Masukkan ulasan film **berbahasa Inggris** untuk mengetahui apakah
sentimennya **positif** atau **negatif** menggunakan model Machine Learning.
""")

st.divider()

# ==========================================================
# CONTOH REVIEW
# ==========================================================

with st.expander("📌 Contoh Review"):

    st.code("""
Positive :
This movie was absolutely amazing. I loved every scene.

Negative :
This movie was boring and a complete waste of time.
""")

# ==========================================================
# INPUT REVIEW
# ==========================================================

review = st.text_area(

    "Masukkan Review",

    height=220,

    placeholder="Example : This movie was amazing!"
)

st.write(f"Jumlah karakter : **{len(review)}**")

st.divider()

# ==========================================================
# TOMBOL PREDIKSI
# ==========================================================

predict_button = st.button(
    "Prediksi Sentimen",
    use_container_width=True
)

# ==========================================================
# PROSES PREDIKSI
# ==========================================================

if predict_button:

    if review.strip() == "":

        st.warning("Silakan masukkan review terlebih dahulu.")

    else:

        with st.spinner("Sedang melakukan prediksi..."):

            clean_review = preprocess_text(review)

            vector = vectorizer.transform([clean_review])

            prediction = model.predict(vector)[0]

            probability = model.predict_proba(vector)[0]


        st.success("Prediksi berhasil dilakukan!")

        st.divider()

        st.subheader("Hasil Prediksi")
        # ==========================================================
        # MENGAMBIL PROBABILITAS DENGAN AMAN
        # ==========================================================

        classes = model.classes_

        prob_dict = dict(zip(classes, probability))

        positive_prob = prob_dict.get("positive", 0)

        negative_prob = prob_dict.get("negative", 0)

        confidence = max(positive_prob, negative_prob)

        # ==========================================================
        # HASIL PREDIKSI
        # ==========================================================

        if prediction == "positive":

            st.success("😊 Sentimen Positif")

            interpretasi = """
Model memprediksi bahwa review ini memiliki sentimen positif.
Review mengandung lebih banyak kata yang menunjukkan kepuasan,
apresiasi, atau penilaian baik terhadap film.
"""

        else:

            st.error("😞 Sentimen Negatif")

            interpretasi = """
Model memprediksi bahwa review ini memiliki sentimen negatif.
Review mengandung lebih banyak kata yang menunjukkan kritik,
ketidakpuasan, atau penilaian buruk terhadap film.
"""

        st.divider()

        # ==========================================================
        # CONFIDENCE SCORE
        # ==========================================================

        st.subheader("Confidence Score")

        st.metric(
            "Keyakinan Model",
            f"{confidence:.2%}"
        )

        st.progress(float(confidence))

        st.caption(
            "Semakin tinggi nilai confidence, semakin yakin model terhadap hasil prediksi."
        )

        st.divider()

        # ==========================================================
        # PROBABILITAS MASING-MASING KELAS
        # ==========================================================

        st.subheader("Probabilitas Prediksi")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "😊 Positive",
                f"{positive_prob:.2%}"
            )

        with col2:

            st.metric(
                "😞 Negative",
                f"{negative_prob:.2%}"
            )

        st.divider()

        # ==========================================================
        # HASIL PREPROCESSING
        # ==========================================================

        st.subheader("🧹 Hasil Preprocessing")

        st.code(
            clean_review,
            language="text"
        )

        st.divider()

        # ==========================================================
        # INTERPRETASI
        # ==========================================================

        st.subheader("Interpretasi")

        st.info(interpretasi)

        st.divider()

        # ==========================================================
        # REVIEW ASLI
        # ==========================================================

        st.subheader("Review Asli")

        st.write(review)

        st.divider()

        # ==========================================================
        # RINGKASAN HASIL
        # ==========================================================

        st.subheader("Ringkasan Hasil")

        hasil = {
            "Review Asli": review,
            "Review Setelah Preprocessing": clean_review,
            "Prediksi": prediction.capitalize(),
            "Confidence Score": f"{confidence:.2%}",
            "Probabilitas Positif": f"{positive_prob:.2%}",
            "Probabilitas Negatif": f"{negative_prob:.2%}"
        }

        st.json(hasil)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("Cara Menggunakan")

    st.write("""
1. Masukkan review film berbahasa Inggris.

2. Klik tombol **Prediksi Sentimen**.

3. Tunggu beberapa saat hingga proses selesai.

4. Hasil prediksi akan ditampilkan beserta confidence score.
""")

    st.divider()

    st.subheader("Model")

    st.write("""
**Algoritma :** Logistic Regression

**Vectorizer :** TF-IDF

**Dataset :** IMDb Movie Reviews

**Kelas :**
- Positive
- Negative
""")

    st.divider()

    st.info(
        "Model ini dibuat untuk mengklasifikasikan sentimen ulasan film berdasarkan teks yang dimasukkan pengguna."
    )

    st.divider()

    st.caption("© 2026 Analisis Sentimen Film IMDb")
