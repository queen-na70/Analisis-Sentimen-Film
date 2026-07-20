import streamlit as st
from PIL import Image
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

st.set_page_config(
    page_title="Evaluasi Model",
    page_icon="📊"
)

st.title("Evaluasi Model")

st.markdown("""
Halaman ini menampilkan hasil evaluasi model **Multinomial Naive Bayes**
yang digunakan untuk analisis sentimen ulasan film IMDb.
""")

st.divider()

# ==========================
# METRIK MODEL
# ==========================

st.subheader("Performa Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "85%")

with col2:
    st.metric("Precision", "85%")

with col3:
    st.metric("Recall", "85%")

col4, col5 = st.columns(2)

with col4:
    st.metric("F1-Score", "85%")

with col5:
    st.metric("ROC-AUC", "92%")

st.divider()

# ==========================
# CONFUSION MATRIX
# ==========================

st.subheader("Confusion Matrix")

cm_path = os.path.join(
    PROJECT_ROOT,
    "models",
    "confusion_matrix_naive_bayes.png"
)

if os.path.exists(cm_path):

    st.image(
        Image.open(cm_path),
        caption="Confusion Matrix",
        use_container_width=True
    )

else:

    st.warning("Gambar Confusion Matrix belum tersedia.")

st.divider()

# ==========================
# ROC CURVE
# ==========================

st.subheader("ROC Curve")

roc_path = os.path.join(
    PROJECT_ROOT,
    "models",
    "ROC_curve.png"
)
if os.path.exists(roc_path):

    st.image(
        Image.open(roc_path),
        caption="ROC Curve",
        use_container_width=True
    )

else:

    st.warning("Gambar ROC Curve belum tersedia.")

st.divider()

# ==========================
# KESIMPULAN
# ==========================

st.subheader("Kesimpulan")

st.success("""
Model **Multinomial Naive Bayes** berhasil melakukan klasifikasi
sentimen ulasan film dengan performa yang baik.

Berdasarkan hasil evaluasi menggunakan Accuracy, Precision,
Recall, F1-Score, ROC-AUC, Confusion Matrix,
dan ROC Curve, model mampu membedakan
review positif dan negatif secara efektif.
""")