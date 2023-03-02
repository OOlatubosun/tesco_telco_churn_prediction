## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Tesco Telco Churn Prediction')

StreamingMovies = st.selectbox("StreamingMovies", options=["yes", "no"])
PaperlessBilling = st.selectbox("PaperlessBilling", options=["yes", "no"])
MonthlyCharges = st.number_input("MonthlyCharges", 0, 100)
TotalCharges = st.slider("TotalCharges", 0, 1000)
Churn = st.selectbox("Churn", options=["yes", "no"])
SeniorCitizen = st.selectbox("SeniorCitizen", options=["yes", "no"])
Partner = st.selectbox("Partner", options=["yes", "no"])
Dependents = st.selectbox("Dependents", options=["yes", "no"])
tenure = st.slider("tenure", 16, 100)
PhoneService = st.selectbox("PhoneService", options=["yes", "no"])
MultipleLines = st.selectbox("MultipleLines", options=["yes", "no"])
InternetService = st.selectbox("InternetService", options=["yes", "no"])
OnlineSecurity = st.selectbox('OnlineSecurity', options=["yes", "no"])
OnlineBackup = st.selectbox("OnlineBackup", options=["yes", "no"])
DeviceProtection = st.selectbox("DeviceProtection", options=["yes", "no"])
TechSupport = st.selectbox("TechSupport", options=["yes", "no"])
StreamingTV = st.selectbox("StreamingTV", options=["yes", "no"])
Male = st.selectbox("Male", options=["yes", "no"])
Card = st.selectbox("Card", options=["yes", "no"])
Check = st.selectbox("Check", options=["yes", "no"])
OY = st.selectbox("OY", options=["yes", "no"])
TY = st.selectbox("TY", options=["yes", "no"])

input_data_dict = {
    "StreamingMovies": StreamingMovies,
    "PaperlessBilling": PaperlessBilling,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "Churn": Churn,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "Male": Male,
    "Card": Card,
    "Check": Check,
    "OY": OY,
    "TY": TY,
}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = 'models'

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("CLICK TO PREDICT TESCO TELCO CHURN")

if submit:

    tesco_telco_churn = save_model_predictor.predict(input_data)[0]
    st.write(f"The predicted tesco telco churn is: {tesco_telco_churn}")