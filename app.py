import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")  # lowercase

summarizer = load_model()

st.title("🧠 AI Text Summarizer (News / Legal)")
st.write("Paste your long news or legal text below and get a smart summary")

text_input = st.text_area("Enter your text here", height=300)

min_length = st.slider("Minimum summary length (words)", 30, 100, 50)
max_length = st.slider("Maximum summary length (words)", 100, 300, 150)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Summarizing........"):
            summary = summarizer(text_input, min_length=min_length, max_length=max_length)[0]['summary_text']
            st.success("Summary: ")
            st.write(summary)
    else:
        st.warning("Please enter some text to summarize")
