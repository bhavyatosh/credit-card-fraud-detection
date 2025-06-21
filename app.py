# app.py

import streamlit as st
import pandas as pd
from model import load_model

# 🔄 Load model from model.py
model = load_model()

# 🌐 App title
st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction details (V1 to V28, Amount) to detect fraud.")

# 🔡 Input form for V1–V28 and Amount
feature_names = [f'V{i}' for i in range(1, 29)] + ['Amount']
input_data = []

with st.form("fraud_form"):
    for feature in feature_names:
        value = st.number_input(f"Enter {feature}", format="%.4f")
        input_data.append(value)

    submitted = st.form_submit_button("Predict")

# 🔮 Predict fraud or not
if submitted:
    input_df = pd.DataFrame([input_data], columns=feature_names)
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ This transaction is predicted as FRAUDULENT.")
    else:
        st.success("✅ This transaction is predicted as NON-FRAUDULENT.")
