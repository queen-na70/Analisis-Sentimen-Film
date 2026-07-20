import re
import string
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ==========================================================
# Inisialisasi
# ==========================================================

tokenizer = ToktokTokenizer()

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


# ==========================================================
# Fungsi Preprocessing
# ==========================================================

def preprocess_text(text):

    # Lowercase
    text = text.lower()

    # Remove HTML
    text = re.sub(r"<.*?>", "", text)

    # Remove URL
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove Punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove Numbers
    text = re.sub(r"\d+", "", text)

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenization
    tokens = tokenizer.tokenize(text)

    # Stopword Removal
    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    # Lemmatization
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return " ".join(tokens)