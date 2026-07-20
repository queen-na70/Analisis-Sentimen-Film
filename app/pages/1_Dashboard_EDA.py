import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ==========================
# Konfigurasi Halaman
# ==========================
st.set_page_config(
    page_title="Dashboard EDA",
    page_icon="📊",
    layout="wide"
)

st.title("Dashboard Exploratory Data Analysis")

st.write(
    "Halaman ini menampilkan hasil eksplorasi data (EDA) "
    "pada dataset IMDb Movie Review."
)

# ==========================
# Load Dataset
# ==========================
@st.cache_data
def load_data():
    df = pd.read_csv("../data/raw/IMDB Dataset.csv")
    return df

df = load_data()

# ==========================
# Ringkasan Dataset
# ==========================
st.header("Ringkasan Dataset")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Jumlah Data", len(df))

with col2:
    st.metric("Jumlah Fitur", df.shape[1])

with col3:
    st.metric(
        "Review Positif",
        df[df["sentiment"] == "positive"].shape[0]
    )

with col4:
    st.metric(
        "Review Negatif",
        df[df["sentiment"] == "negative"].shape[0]
    )

# ==========================
# Preview Dataset
# ==========================
st.header("Preview Dataset")

st.dataframe(df.head())

# ==========================
# Distribusi Sentimen
# ==========================
st.header("Distribusi Sentimen")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(
    data=df,
    x="sentiment",
    hue="sentiment",
    palette="Set2",
    legend=False,
    ax=ax
)

ax.set_xlabel("Sentimen")
ax.set_ylabel("Jumlah")
ax.set_title("Distribusi Sentimen")

st.pyplot(fig)

# ==========================
# Pie Chart
# ==========================
st.header("Persentase Sentimen")

fig, ax = plt.subplots(figsize=(6,6))

df["sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# ==========================
# Histogram Panjang Review
# ==========================
st.header("Distribusi Panjang Ulasan")

df["panjang_review"] = df["review"].apply(len)

fig, ax = plt.subplots(figsize=(10,5))

sns.histplot(
    data=df,
    x="panjang_review",
    bins=40,
    kde=True,
    ax=ax
)

ax.set_xlabel("Jumlah Karakter")
ax.set_ylabel("Frekuensi")

st.pyplot(fig)

# ==========================
# WordCloud Positif
# ==========================
st.header("WordCloud Ulasan Positif")

positive_text = " ".join(
    df[df["sentiment"]=="positive"]["review"]
)

wordcloud_positive = WordCloud(
    width=900,
    height=500,
    background_color="white"
).generate(positive_text)

fig, ax = plt.subplots(figsize=(12,6))

ax.imshow(wordcloud_positive)

ax.axis("off")

st.pyplot(fig)

# ==========================
# WordCloud Negatif
# ==========================
st.header("WordCloud Ulasan Negatif")

negative_text = " ".join(
    df[df["sentiment"]=="negative"]["review"]
)

wordcloud_negative = WordCloud(
    width=900,
    height=500,
    background_color="white"
).generate(negative_text)

fig, ax = plt.subplots(figsize=(12,6))

ax.imshow(wordcloud_negative)

ax.axis("off")

st.pyplot(fig)