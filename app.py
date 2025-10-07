
import streamlit as st
from sentiment_model import analyze_sentiment
from text_generator import generate_text

st.set_page_config(page_title="AI Text Generator", page_icon="🤖", layout="centered")

st.title("🧠 AI Text Generator Based on Sentiment")

prompt = st.text_area("Enter your prompt here:")
generate_btn = st.button("Generate Text")

if generate_btn and prompt.strip():
    with st.spinner("Analyzing sentiment..."):
        sentiment = analyze_sentiment(prompt)
    st.write(f"**Detected Sentiment:** {sentiment.capitalize()}")

    with st.spinner("Generating text..."):
        generated = generate_text(prompt, sentiment)

    st.subheader("✨ Generated Output:")
    st.write(generated)
