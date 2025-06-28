from utils import load_and_clean_data, display_eda
from model import train_and_predict
import streamlit as st

st.title("Heart Disease Prediction")

# Load dataset directly from GitHub repo
df = load_and_clean_data("Heart_Disease_Prediction (2).csv")
display_eda(df)

if st.button("Run Prediction"):
    result = train_and_predict(df)
    st.json(result)
