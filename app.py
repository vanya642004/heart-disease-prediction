import streamlit as st
from utils import preprocess_data, show_insights
from model import load_model, make_prediction

st.title("Intelligent Database System for E-Commerce")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = preprocess_data(uploaded_file)
    show_insights(df)

    model = load_model()
    if st.button("Predict"):
        prediction = make_prediction(df, model)
        st.write("Prediction Results:", prediction)
