import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Bhutan Tourism Predictor", page_icon="🇧🇹", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-size: cover;
        opacity: 0.7;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }

    label {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }

    .block-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }

    input[type=number] {
        width: 100px !important;
        padding: 5px !important;
        font-size: 16px !important;
    }

    .predicted-output {
        font-size: 2rem;
        color: #008000;
        font-weight: bold;
        margin-top: 20px;
    }

    .predicted-label {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 5px;
    }

    .stButton>button {
        background-color: #FFCC00;
        color: #0033A0;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://flagcdn.com/w2560/bt.png", width=100)

st.title("Bhutan Tourism Predictor")
st.write("Predict the number of tourists for Bhutan based on the year input.")

year = st.number_input("Enter the year:", min_value=2024, max_value=2100, value=2024, step=1)

predicted_income = 200

st.markdown(f"""
    <div class="predicted-label">Predicted number of tourists for the year {year}:</div>
    <div class="predicted-output">{predicted_income}</div>
""", unsafe_allow_html=True)
