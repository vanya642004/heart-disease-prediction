import pandas as pd
import streamlit as st

def preprocess_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview", df.head())
    return df

def show_insights(df):
    st.write("Summary Stats", df.describe())
    st.write("Null Values", df.isnull().sum())
