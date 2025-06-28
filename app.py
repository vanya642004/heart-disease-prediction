import streamlit as st
from model import predict_from_inputs

st.title("🔍 Heart Disease Risk Predictor")

st.markdown("Enter patient data below to check heart disease risk.")

age = st.slider("Age", min_value=1, max_value=120, value=45)
sex = st.radio("Sex", ["Male", "Female"])
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

if st.button("🧠 Predict"):
    input_data = [
        age, 1 if sex == "Male" else 0, cp, trestbps, chol,
        fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    ]
    result = predict_from_inputs(input_data)
    st.success("✅ Risk of Heart Disease Detected" if result == 1 else "❎ No Risk of Heart Disease")

