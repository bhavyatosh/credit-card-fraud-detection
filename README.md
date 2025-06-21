# 💳 Credit Card Fraud Detection App

This is a Streamlit-based web application that predicts whether a credit card transaction is **fraudulent** or **legitimate** using a trained **Random Forest Classifier**.

---

## 🔍 Features

- Predicts fraud using input features from the original Kaggle dataset (`V1` to `V28` + `Amount`)
- Model weights are securely loaded from Google Drive using `gdown`
- User-friendly web UI built with Streamlit
- Can be extended with CSV uploads or prediction logs

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- joblib
- gdown

---

## 🚀 How to Run Locally

1. **Clone this repository:**

```bash
git clone https://github.com/bhavyatosh/credit-card-fraud-app.git
cd credit-card-fraud-app
