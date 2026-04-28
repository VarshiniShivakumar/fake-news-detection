import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Cleaning function
def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)

# Prediction
def predict_news(text):
    text = clean_text(text)
    text = vectorizer.transform([text]).toarray()
    result = model.predict(text)

    return "✅ Real News" if result[0] == 1 else "❌ Fake News"

# UI
st.title("📰 Fake News Detection System")

user_input = st.text_area("Enter News Text")

if st.button("Predict"):
    if user_input:
        st.write(predict_news(user_input))
    else:
        st.warning("Enter some text")