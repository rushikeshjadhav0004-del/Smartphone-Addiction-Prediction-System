import streamlit as st
import pickle
import pandas as pd

# Load trained pipeline model
model = pickle.load(open("addiction_model.pkl", "rb"))

st.title("😎 Smartphone Addiction Prediction")

st.write("Enter user information")

# -------- INPUTS -------- #

age = st.number_input("Age", 10, 80)

gender = st.selectbox("Gender", ["Male", "Female"])

daily_screen_time_hours = st.slider("Daily Screen Time (hours)", 0.0, 15.0)

social_media_hours = st.slider("Social Media Hours", 0.0, 10.0)

gaming_hours = st.slider("Gaming Hours", 0.0, 10.0)

work_study_hours = st.slider("Work / Study Hours", 0.0, 12.0)

sleep_hours = st.slider("Sleep Hours", 0.0, 12.0)

notifications_per_day = st.number_input("Notifications Per Day", 0, 500, 80)

app_opens_per_day = st.number_input("App Opens Per Day", 0, 300, 60)

weekend_screen_time = st.slider("Weekend Screen Time", 0.0, 20.0)

stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])

academic_work_impact = st.selectbox(
    "Academic / Work Impact",
    ["None",'Yes','No']
)

addiction_level = st.selectbox(
    "Addiction Level",
    [ "Mild", "Moderate", "Severe"]
)

# -------- PREDICTION -------- #

if st.button("Predict"):

    input_data = pd.DataFrame({
        "age":[age],
        "gender":[gender],
        "daily_screen_time_hours":[daily_screen_time_hours],
        "social_media_hours":[social_media_hours],
        "gaming_hours":[gaming_hours],
        "work_study_hours":[work_study_hours],
        "sleep_hours":[sleep_hours],
        "notifications_per_day":[notifications_per_day],
        "app_opens_per_day":[app_opens_per_day],
        "weekend_screen_time":[weekend_screen_time],
        "stress_level":[stress_level],
        "academic_work_impact":[academic_work_impact],
        "addiction_level":[addiction_level]
    })

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ High Smartphone Addiction Risk")
    else:
        st.success("✅ Low Smartphone Addiction Risk")

    st.write("Input Data Sent To Model")
    st.dataframe(input_data)