import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Diabetes Prediction App", layout="centered")
st.title("🩺 Diabetes Prediction App")
st.markdown("Enter your health details below to check your diabetes risk.")

# 1. Train model inside the app (avoids .pkl errors on deployment)
@st.cache_data
def load_training_data():
    df = pd.read_csv("user_friendly_diabetes_data.csv")
    label_cols = ["Frequent_Urination", "Excessive_Thirst", "Fatigue", "Exercise_Level", "Family_History"]
    for col in label_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    X = df.drop("Diabetes", axis=1)
    y = df["Diabetes"]
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    return model

model = load_training_data()

# 2. Input form
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

# 3. Encoding helper
def encode_inputs(urination, thirst, fatigue, exercise, family_history):
    return (
        1 if urination == "Yes" else 0,
        1 if thirst == "Yes" else 0,
        1 if fatigue == "Yes" else 0,
        {"Low": 0, "Moderate": 1, "High": 2}[exercise],
        1 if family_history == "Yes" else 0
    )

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

# 4. On form submit
if submitted:
    urin, thir, fat, ex, fam = encode_inputs(urination, thirst, fatigue, exercise, family_history)
    bmi = calculate_bmi(weight, height)

    input_data = pd.DataFrame([[age, weight, height, urin, thir, fat, ex, fam]], columns=[
        "Age", "Weight", "Height", "Frequent_Urination",
        "Excessive_Thirst", "Fatigue", "Exercise_Level", "Family_History"
    ])

    prediction = model.predict(input_data)[0]

    st.subheader("📊 Result")
    st.markdown(f"**Your BMI:** `{bmi}`")

    if prediction == 1:
        st.error("⚠️ You may be at **high risk** of diabetes.")
        st.markdown("### 🩺 Health Tips:\n- Visit a doctor for blood sugar test.\n- Eat fiber-rich, low-sugar foods.\n- Exercise daily.\n- Avoid sugary drinks.")
    else:
        st.success("✅ You are **unlikely** to have diabetes.")
        st.markdown("### ✅ Prevention Tips:\n- Maintain an active lifestyle.\n- Eat healthy.\n- Stay hydrated.\n- Get regular checkups.")
