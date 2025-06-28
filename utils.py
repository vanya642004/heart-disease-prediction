import pandas as pd
import streamlit as st

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df['ST depression'] = df['ST depression'].astype(int)
    df['Heart Disease'] = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})
    return df

def display_eda(df):
    st.subheader("Dataset Preview")
    st.write(df.head())
    st.subheader("Summary Statistics")
    st.write(df.describe())
    st.subheader("Missing Values")
    st.write(df.isnull().sum())
