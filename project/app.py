import streamlit as st
import joblib
import numpy as np

model = joblib.load("cardio_model.pkl")

st.title("Cardiovascular Disease Prediction")

age = st.number_input("Age")
gender = st.selectbox("Gender", [1,2])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
ap_hi = st.number_input("Systolic BP")
ap_lo = st.number_input("Diastolic BP")
cholesterol = st.selectbox("Cholesterol Level", [1,2,3])
gluc = st.selectbox("Glucose Level", [1,2,3])
smoke = st.selectbox("Smoke", [0,1])
alco = st.selectbox("Alcohol", [0,1])
active = st.selectbox("Physical Activity", [0,1])

if st.button("Predict"):

    BMI = weight / ((height/100)**2)

    data = np.array([[age, gender, height, weight, ap_hi, ap_lo,
                      cholesterol, gluc, smoke, alco, active, BMI]])

    result = model.predict(data)

    if result[0] == 1:
        st.error("High Risk of Cardiovascular Disease")
    else:
        st.success("Low Risk of Cardiovascular Disease")