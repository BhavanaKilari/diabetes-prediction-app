import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# ✅ MUST be the first Streamlit command
st.set_page_config(
    page_title="Diabetes Prediction App",
    layout="centered",
    initial_sidebar_state="auto"
)

# ✅ Styling with background image and result font
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://img.freepik.com/free-vector/health-medical-blue-background_1017-26807.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.75);
    }
    .big-font {
        font-size: 28px !important;
        font-weight: bold;
        color: #1e90ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Title and description
st.markdown("<h1 style='text-align: center; color: #333;'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Enter your health details below to check your diabetes risk.</p>", unsafe_allow_html=True)

# ✅ Load and train model from CSV
@st.cache_data
def load_model():
    df = pd.read_csv("user_friendly_diabetes_data.csv")
    label_cols = ["Frequent_Urination", "Excessive_Thirst", "Fatigue", "Exercise_Level", "Family_History"]
    for col in label_cols:
        df[col] = LabelEncoder().fit_transform(df[col])
    X = df.drop("Diabetes", axis=1)
    y = df["Diabetes"]
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    return model

model = load_model()

# ✅ Input form
with st.form("diabetes_form"):
    age = st.text_input("Age", placeholder="Enter your age (e.g., 45)")
    weight = st.text_input("Weight in kg", placeholder="e.g., 70")
    height = st.text_input("Height in cm", placeholder="e.g., 165")

    urination = st.radio("Do you experience frequent urination?", ["Yes", "No"])
    thirst = st.radio("Do you feel excessive thirst?", ["Yes", "No"])
    fatigue = st.radio("Do you often feel fatigued?", ["Yes", "No"])
    exercise = st.selectbox("Your physical activity level:", ["Low", "Moderate", "High"])
    family_history = st.radio("Any family history of diabetes?", ["Yes", "No"])

    submitted = st.form_submit_button("🔍 Check My Diabetes Risk")

# ✅ Encoding helpers
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

# ✅ Prediction logic
if submitted:
    try:
        age = int(age)
        weight = float(weight)
        height = float(height)

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
            st.markdown('<p class="big-font">⚠️ You may be at <strong>high risk</strong> of diabetes.</p>', unsafe_allow_html=True)
            st.error("Please consult a doctor. Here are some tips:")
            st.markdown("""
            - Eat fiber-rich, low-sugar foods  
            - Exercise daily  
            - Avoid sugary drinks and processed foods  
            - Monitor your blood sugar regularly  
            """)
        else:
            st.markdown('<p class="big-font">✅ You are <strong>unlikely</strong> to have diabetes.</p>', unsafe_allow_html=True)
            st.success("Keep up your healthy habits!")
            st.markdown("""
            - Maintain regular exercise  
            - Keep a balanced diet  
            - Stay hydrated  
            - Get regular checkups  
            """)
    except:
        st.warning("⚠️ Please enter valid numbers for Age, Weight, and Height.")
