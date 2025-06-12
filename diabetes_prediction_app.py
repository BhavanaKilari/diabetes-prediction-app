import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("diabetes_decision_tree_model.pkl")

# App layout
st.set_page_config(page_title="Diabetes Prediction App", layout="centered")
st.title("🩺 Diabetes Prediction App")
st.markdown("Enter your health details below to check your diabetes risk.")

# Input form
with st.form("diabetes_form"):
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
    height = st.number_input("Height (in cm)", min_value=100, max_value=250)

    urination = st.radio("Do you experience frequent urination?", ["Yes", "No"])
    thirst = st.radio("Do you feel excessive thirst?", ["Yes", "No"])
    fatigue = st.radio("Do you often feel fatigued?", ["Yes", "No"])
    exercise = st.selectbox("Your physical activity level:", ["Low", "Moderate", "High"])
    family_history = st.radio("Any family history of diabetes?", ["Yes", "No"])

    submitted = st.form_submit_button("Check My Diabetes Risk")

# Encoding function
def encode_inputs(urination, thirst, fatigue, exercise, family_history):
    urination_val = 1 if urination == "Yes" else 0
    thirst_val = 1 if thirst == "Yes" else 0
    fatigue_val = 1 if fatigue == "Yes" else 0
    exercise_val = {"Low": 0, "Moderate": 1, "High": 2}[exercise]
    family_val = 1 if family_history == "Yes" else 0
    return urination_val, thirst_val, fatigue_val, exercise_val, family_val

# BMI Calculation
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

# Submit logic
if submitted:
    urin, thir, fat, ex, fam = encode_inputs(urination, thirst, fatigue, exercise, family_history)
    bmi = calculate_bmi(weight, height)

    input_data = pd.DataFrame([[
        age, weight, height, urin, thir, fat, ex, fam
    ]], columns=[
        "Age", "Weight", "Height", "Frequent_Urination",
        "Excessive_Thirst", "Fatigue", "Exercise_Level", "Family_History"
    ])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Result")
    st.markdown(f"**Your BMI:** `{bmi}`")

    if prediction == 1:
        st.error("⚠️ You may be at **high risk** of diabetes.")
        st.markdown("""
        ### 🩺 Health Tips:
        - Visit a doctor for a blood sugar test.
        - Eat low-sugar, high-fiber meals.
        - Exercise 30–45 mins daily.
        - Avoid sugary drinks and junk food.
        """)
    else:
        st.success("✅ You are **unlikely** to have diabetes.")
        st.markdown("""
        ### ✅ Prevention Tips:
        - Stay active and eat healthy.
        - Drink water regularly.
        - Track your weight and lifestyle.
        """)
