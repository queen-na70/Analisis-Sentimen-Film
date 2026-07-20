import os
from PIL import Image
import streamlit as st

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))

st.subheader("Interpretasi Menggunakan LIME")

lime_path = os.path.join(
    PROJECT_ROOT,
    "models",
    "lime_interpretation.png"
)

if os.path.exists(lime_path):

    st.image(
        Image.open(lime_path),
        caption="Interpretasi Prediksi Menggunakan LIME",
        use_container_width=True
    )

else:

    st.warning("Gambar LIME belum tersedia.")

    st.markdown("""
### Penjelasan

Visualisasi LIME menunjukkan kata-kata yang paling memengaruhi
keputusan model dalam menentukan sentimen.

- **Warna hijau** menunjukkan kata yang mendukung prediksi model.
- **Warna merah** menunjukkan kata yang melemahkan prediksi model.

Sebagai contoh, kata seperti *excellent*, *great*, dan *amazing*
berkontribusi terhadap prediksi sentimen positif, sedangkan kata
seperti *boring*, *bad*, dan *worst* lebih mendukung sentimen negatif.
""")