import streamlit as st
from datetime import datetime

# Set the page config at the very beginning
st.set_page_config(page_title="Bhutan Tourism Income Predictor", page_icon="🇧🇹", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://flagcdn.com/w2560/bt.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://example.com/bhutan-flag.png", width=100)

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

st.title("Bhutan Tourism Income Predictor")
st.write("Predict the tourism income for Bhutan based on the year input.")

year = st.number_input("Enter the year:", min_value=2024, max_value=2100, value=2024, step=1)

predicted_income = 200
st.write(f"Predicted tourism income for the year {year}: Nu. {predicted_income:,.2f}")
