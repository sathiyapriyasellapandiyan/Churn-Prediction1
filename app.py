import streamlit as st
import joblib
import pandas as pd

# Load the preprocessing and model from pickle files
preprocessor_file = r'artifacts/preprocessor.joblib'
preprocessing = joblib.load(preprocessor_file)
model_file = r'artifacts/model.joblib'
model = joblib.load(model_file)

# Function to make predictions
def predict_churn(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    input_df.columns = [i.lower() for i in input_df.columns]
    print(input_df.columns)
    # Preprocess the input data
    preprocessed_data = preprocessing.transform(input_df)
    
    # Make predictions
    predictions = model.predict(preprocessed_data)
    
    return predictions[0]  # Return the first prediction

# Streamlit application layout
st.title("Customer Churn Prediction")
st.write("Please provide the following information:")

# User inputs
gender = st.selectbox("Gender", ["male", "female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["yes","no"])
dependents = st.selectbox("Dependents", ["yes","no"])
tenure = st.number_input("Tenure (months)", min_value=1, max_value=72, value=12)
phone_service = st.selectbox("Phone Service", ["yes","no"])
multiple_lines = st.selectbox("Multiple Lines", ["yes", "no", "no phone service"])
internet_service = st.selectbox("Internet Service", ["fiber optic", "dsl", "no"])
online_security = st.selectbox("Online Security", ["yes", "no", "no internet service"])
online_backup = st.selectbox("Online Backup", ["yes", "no", "no internet service"])
device_protection = st.selectbox("Device Protection", ["yes", "no", "no internet service"])
tech_support = st.selectbox("Tech Support", ["yes", "no", "no internet service"])
streaming_tv = st.selectbox("Streaming TV", ["yes", "no", "no internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["yes", "no", "no internet service"])
contract = st.selectbox("Contract", ["month-to-month", "one year", "two year"])
paperless_billing = st.selectbox("Paperless Billing", ["yes","no"])
payment_method = st.selectbox("Payment Method", 
    ["electronic check", "mailed check", "bank transfer (automatic)", "credit card (automatic)"])
monthly_charges = st.number_input("Monthly Charges", min_value=19.65, max_value=118.75, step=0.05)
total_charges = st.number_input("Total Charges", min_value=19.65, max_value=8684.80, step=0.05)

# Prepare input data for prediction
input_data = {
    "gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

# Button to make a prediction
if st.button("Predict Churn"):
    prediction = predict_churn(input_data)
    if prediction == 1:
        st.success("The model predicts that the customer will churn.")
    else:
        st.success("The model predicts that the customer will not churn.")
