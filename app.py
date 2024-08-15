import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Predicting Customer Churn')
st.markdown('Model to classify if a customer is more likely to churn or not')

# Header for the feature input
st.header("Customer Features")

col1, col2 = st.columns(2)

with col1:
    st.text("Basic Information")
    gender = st.selectbox('Gender', ['Male', 'Female'])
    phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
    paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])

with col2:
    st.text("Service Information")
    streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
    monthly_charges = st.slider('Monthly Charges ($)', 0.0, 120.0, 50.0)
    total_charges = st.slider('Total Charges ($)', 0.0, 8000.0, 2000.0)

if st.button("Predict Customer Behavior"):
    # Encode categorical variables
    gender_encoded = 1 if gender == 'Male' else 0
    phone_service_encoded = 1 if phone_service == 'Yes' else 0
    paperless_billing_encoded = 1 if paperless_billing == 'Yes' else 0
    streaming_tv_encoded = 2 if streaming_tv == 'Yes' else (1 if streaming_tv == 'No internet service' else 0)
    
    # Create input DataFrame with column names and correct data types
    input_features_df = pd.DataFrame([[gender_encoded, phone_service_encoded, paperless_billing_encoded, 
                                       streaming_tv_encoded, monthly_charges, str(total_charges)]],
                                     columns=['gender', 'PhoneService', 'PaperlessBilling', 'StreamingTV', 
                                              'MonthlyCharges', 'TotalCharges'])
    
    # Predict and display the result
    result = predict(input_features_df)
    
    # Map prediction output to "No" and "Yes"
    prediction_text = "This customer is likely to churn" if result[0] == 1 else "This customer will not churn"
    
    st.text(f"Prediction: {prediction_text}")
