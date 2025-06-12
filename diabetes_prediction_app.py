# diabetes_prediction_app.py

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib  # For saving/loading model

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv('diabetes.csv')

df = load_data()

# Split data
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))

# Streamlit UI
st.title("🩺 Diabetes Prediction App")
st.markdown("Predict the likelihood of having diabetes using simple medical inputs.")

st.sidebar.header("User Input Parameters")

# Function to take user inputs
def user_input():
    pregnancies = st.sidebar.slider("Pregnancies", 0, 20, 1)
    glucose = st.sidebar.slider("Glucose", 40, 200, 100)
    blood_pressure = st.sidebar.slider("Blood Pressure", 30, 130, 70)
    skin_thickness = st.sidebar.slider("Skin Thickness", 0, 100, 20)
    insulin = st.sidebar.slider("Insulin", 0, 850, 80)
    bmi = st.sidebar.slider("BMI", 10.0, 70.0, 30.0)
    dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.sidebar.slider("Age", 10, 90, 25)

    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Predict
prediction = model.predict(input_df)[0]
result_text = "🔴 You may be at risk of diabetes." if prediction == 1 else "🟢 You are unlikely to have diabetes."

# Output
st.subheader("Prediction Result")
st.write(result_text)

st.subheader("Model Accuracy")
st.write(f"{accuracy:.2%}")

