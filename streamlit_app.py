import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Bhutan Tourism Predictor", page_icon="🇧🇹", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url();
        background-size: cover;
        opacity: 0.7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://flagcdn.com/w2560/bt.png", width=100)

st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #FFCC00;
        color: #0033A0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Bhutan Tourism Predictor")
st.write("Predict the number of tourists for Bhutan based on the year input.")

year = st.number_input("Enter the year:", min_value=2024, max_value=2100, value=2024, step=1)

predicted_income = 200
st.write(f"Predicted number of tourist for the year {year}: {predicted_income}")
