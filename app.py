import streamlit as st
from model import predict_from_inputs

st.set_page_config(page_title="Heart Disease Predictor", page_icon="🫀")
st.title("🔍 Heart Disease Risk Predictor")
st.markdown("Enter patient data below to check risk of heart disease.")

# ℹ️ Explain categorical values
with st.expander("ℹ️ Click here to see what the numbers mean"):
    st.markdown("""
    ### 🔢 Feature Value Guide

    | Feature | Values |
    |--------|--------|
    | **Sex** | `0 = Female`, `1 = Male` |
    | **Chest Pain Type (cp)** | `0 = Typical`, `1 = Atypical`, `2 = Non-anginal`, `3 = Asymptomatic` |
    | **Fasting Blood Sugar (fbs)** | `0 = ≤120`, `1 = >120` |
    | **ECG (restecg)** | `0 = Normal`, `1 = ST-T Abnormality`, `2 = LVH` |
    | **Exercise Angina (exang)** | `0 = No`, `1 = Yes` |
    | **Slope** | `0 = Upsloping`, `1 = Flat`, `2 = Downsloping` |
    | **Major Vessels (ca)** | `0`, `1`, `2`, `3` |
    | **Thal** | `0 = Normal`, `1 = Fixed Defect`, `2 = Reversible Defect` |
    """)

# 🔢 Input section
st.subheader("📝 Enter Patient Data")

age = st.slider("Age", min_value=1, max_value=120, value=45)
sex = st.radio("Sex", ["Female", "Male"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3], help="0: Typical, 1: Atypical, 2: Non-anginal, 3: Asymptomatic")
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, value=120)
chol = st.number_input("Cholesterol (chol)", 100, 600, value=240)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.slider("Max Heart Rate Achieved (thalach)", 70, 250, value=150)
exang = st.radio("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2], help="0: Normal, 1: Fixed defect, 2: Reversible defect")

# 🧠 Predict
if st.button("🧠 Predict"):
    input_data = [
        age, 1 if sex == "Male" else 0, cp, trestbps, chol,
        fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    ]
    result = predict_from_inputs(input_data)
    if result == 1:
        st.error("⚠️ High Risk of Heart Disease Detected")
    else:
        st.success("✅ No Risk of Heart Disease Detected")
