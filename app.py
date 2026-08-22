import os

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="AI Travel Concierge",
    page_icon="✈️"
)

st.title("✈️ AI Travel Concierge")
st.write("Ask me a travel-related question.")

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not configured.")
    st.stop()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key=api_key
)

# User input
user_input = st.text_input(
    "Ask a travel-related question:"
)

if st.button("Ask"):

    if not user_input.strip():
        st.warning("Please enter a question.")

    else:
        try:
            with st.spinner("Thinking..."):
                response = llm.invoke(user_input)

            st.subheader("AI Response")
            st.write(response.content)

        except Exception as error:
            st.error(f"Something went wrong: {error}")