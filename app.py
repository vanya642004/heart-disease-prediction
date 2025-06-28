import streamlit as st
from utils import load_and_clean_data, display_eda
from model import train_and_predict

st.title("Heart Disease Prediction App")

uploaded_file = st.file_uploader("Upload your Heart Dataset", type=["csv"])
if uploaded_file:
    df = load_and_clean_data(uploaded_file)
    display_eda(df)
    prediction = train_and_predict(df)
    st.write("Model Evaluation Metrics:")
    st.json(prediction)
