# 1 Good (Lower Risk) 0 Bad (Higher Risk)

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("xgb_credit_model.pkl")
encoders = {col : joblib.load(f"{col}_encoder.pkl") for col in ["Sex", "Housing", "Saving accounts", "Checking account"]}

st.title("Credit Risk Prediction App")
st.write("Enter the details to predict credit risk:")

age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", options=["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", options=["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", options=["little", "moderate", "quite rich", "rich"])
checking_account = st.selectbox("Checking account", options=["little", "moderate", "rich"])
credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Duration": [duration],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
    "Credit amount": [credit_amount]
    
})

if st.button("Predict Risk"):

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("The predicted credit risk is: **LOW (Good Credit).**")
    else:
        st.error("The credit risk is: **HIGH (Bad Credit).**")