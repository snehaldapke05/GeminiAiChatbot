import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

st.title("🤖 Gemini AI Chatbot")
st.write("Ask me anything!")

question = st.text_input("You:")

if st.button("Send"):
    if question:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )

        st.write("### Gemini:")
        st.write(response.text)