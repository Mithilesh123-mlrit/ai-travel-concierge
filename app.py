import streamlit as st

st.set_page_config(
    page_title="AI Travel Concierge",
    page_icon="✈️"
)

st.title("✈️ AI Travel Concierge")
st.write("Welcome to the AI Travel Concierge.")

user_input = st.text_input("Ask a travel-related question:")

if user_input:
    st.write("You asked:")
    st.write(user_input)