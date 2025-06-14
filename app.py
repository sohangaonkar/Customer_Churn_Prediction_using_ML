import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
model = pickle.load(open("churn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction App")

st.markdown("Fill in the customer details below:")

# Input fields — add more if needed based on your model
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has a Partner?", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1500.0)
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# Encode inputs manually (example — match your preprocessing)
gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
partner = 1 if partner == "Yes" else 0
internet = {"DSL": 0, "Fiber optic": 1, "No": 2}[internet]

# Construct input array
input_data = np.array([[gender, senior, partner, tenure, monthly_charges, total_charges, internet]])

# Scale input
scaled_input = scaler.transform(input_data)

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(scaled_input)
    result = "🔴 Likely to Churn" if prediction[0] == 1 else "🟢 Not Likely to Churn"
    st.success(result)
