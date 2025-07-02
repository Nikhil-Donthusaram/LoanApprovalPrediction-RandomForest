import streamlit as st
import numpy as np
import pickle
import os

# Load the trained model
with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="🏦 Loan Approval Prediction", layout="centered")
st.title("🏦 Loan Approval Prediction App")
st.markdown("Use this simple form to check loan approval prediction based on applicant details.")

# Sidebar
st.sidebar.header("User Input Parameters")

# Input Fields
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
married = st.sidebar.selectbox("Married", ["Yes", "No"])
dependents = st.sidebar.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.sidebar.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.sidebar.number_input("Applicant Income", min_value=0)
coapplicant_income = st.sidebar.number_input("Coapplicant Income", min_value=0)
loan_amount = st.sidebar.number_input("Loan Amount (in thousands)", min_value=0)
loan_amount_term = st.sidebar.number_input("Loan Amount Term (in days)", min_value=0)
credit_history = st.sidebar.selectbox("Credit History", ["Yes", "No"])
property_area = st.sidebar.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Feature Encoding
gender_male = 1 if gender == "Male" else 0
married_yes = 1 if married == "Yes" else 0
dependents_1 = 1 if dependents == "1" else 0
dependents_2 = 1 if dependents == "2" else 0
dependents_3_plus = 1 if dependents == "3+" else 0
education_not_graduate = 1 if education == "Not Graduate" else 0
self_employed_yes = 1 if self_employed == "Yes" else 0
credit_history = 1 if credit_history == "Yes" else 0
property_area_semiurban = 1 if property_area == "Semiurban" else 0
property_area_urban = 1 if property_area == "Urban" else 0

# Final feature array
features = np.array([[applicant_income, coapplicant_income, loan_amount,
                      loan_amount_term, credit_history, 
                      gender_male, married_yes, dependents_1,
                      dependents_2, dependents_3_plus, 
                      education_not_graduate, self_employed_yes,
                      property_area_semiurban, property_area_urban]])

# Predict Button
st.markdown("### 📊 Prediction Output")
if st.button("🔍 Predict Loan Approval"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ Congratulations! The loan is **Approved**.")
        st.balloons()
    else:
        st.error("❌ Sorry, the loan is **Not Approved** based on the given information.")
model_path = os.path.join(os.path.dirname(__file__), 'loan_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)
