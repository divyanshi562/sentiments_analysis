import streamlit as st
import requests

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")
st.title("💬 Social Media Sentiment Analyzer")

user_input = st.text_area("Enter a social media post or comment:")

if st.button("Analyze Sentiment"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        # Call the API
        response = requests.post(
            "https://your-backend-api-url.onrender.com/predict",
            json={"text": user_input},
        )
        if response.status_code == 200:
            result = response.json()
            st.success(f"**Sentiment:** {result['label']} ({result['score']:.2f})")
        else:
            st.error("API call failed.")
