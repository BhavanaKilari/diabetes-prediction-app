# 🩺 Diabetes Prediction Web App

This is a **Machine Learning-based Diabetes Prediction App** built using **Python**, **scikit-learn**, and **Streamlit**.  
It predicts whether a person is at risk of diabetes based on easily known input attributes — no lab test values required!


### 🚀 Live Demo  
👉 [Click here to use the app](https://bhavanakilari-diabetes-prediction-app.streamlit.app)





---

## 🎯 Features

- ✅ Built using a **Decision Tree Classifier**
- ✅ User-friendly inputs like age, weight, fatigue, thirst, etc.
- ✅ **BMI calculation** displayed along with result
- ✅ Health tips are shown based on the prediction
- ✅ Streamlit Cloud Deployment – open to all

---

## 🧠 Inputs Used for Prediction

| Feature              | Type     |
|----------------------|----------|
| Age                  | Numeric  |
| Weight (kg)          | Numeric  |
| Height (cm)          | Numeric  |
| Frequent Urination   | Yes / No |
| Excessive Thirst     | Yes / No |
| Fatigue              | Yes / No |
| Physical Activity    | Low / Moderate / High |
| Family History       | Yes / No |

---

## 💡 Technologies Used

- Python
- scikit-learn
- pandas
- Streamlit

---

## 📁 Project Structure

```text
diabetes-prediction-app/
│
├── diabetes_app_user_friendly.py        # Streamlit app
├── user_friendly_diabetes_data.csv      # Training data
└── requirements.txt                     # Dependencies for deployment


---

## 💻 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app
   
2.Install dependencies:
  pip install -r requirements.txt

3.Run the app:
  streamlit run diabetes_app_user_friendly.py
  
## Deployment
This app is deployed using Streamlit Cloud.
Steps:

1.Push your code to GitHub
2.Go to [Streamlit](https://streamlit.io/cloud)
3.Log in with GitHub → Click "New App"
4.Select your repo and the main .py file
5.Click Deploy

## Snapshots
![App Screenshot](screenshots/home.png)
![Prediction Example](screenshots/result.png)

📌## Note
This project is a simplified, educational ML deployment meant for beginner-friendly exploration of:

1.ML training
2.App development
3.Streamlit deployment

🙋‍♀️ Author
Bhavana Kilari
Student, East Point College of Engineering and Technology


 






