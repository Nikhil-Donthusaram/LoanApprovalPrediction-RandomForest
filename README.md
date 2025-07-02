# 🏦 Loan Approval Prediction using Random Forest

This project is a **machine learning-based web application** that predicts whether a loan application will be approved or not using the **Random Forest Classification algorithm**. The model is trained using historical loan application data and deployed using **Streamlit Cloud**.

🔗 **Live App:**  
👉 [Click here to open the app](https://loanapprovalprediction-randomforest-n4shtqpajwyebptmvotkxf.streamlit.app/)

---

## 📌 Problem Statement

Financial institutions receive thousands of loan applications every day. Manually reviewing each application is time-consuming and inefficient. This project aims to **automate the loan approval process** using machine learning by predicting the outcome of a loan application based on various features.

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Random Forest Classifier  
- **Accuracy Achieved:** ~82%
- **Evaluation Metrics:**
  - Accuracy Score
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-Score)

---

## 📊 Features Used

| Feature               | Description                               |
|----------------------|-------------------------------------------|
| ApplicantIncome      | Income of the applicant                   |
| CoapplicantIncome    | Income of the co-applicant                |
| LoanAmount           | Total loan amount                         |
| Loan_Amount_Term     | Term of the loan (in months)              |
| Credit_History       | Whether applicant has credit history      |
| Gender               | Male / Female                             |
| Married              | Applicant’s marital status                |
| Dependents           | Number of dependents                      |
| Education            | Graduate / Not Graduate                   |
| Self_Employed        | Employment status                         |
| Property_Area        | Urban / Semiurban / Rural                 |

---

## ⚙️ How the App Works

1. User opens the Streamlit app.
2. Fills in the form with loan application details.
3. Clicks the **"Predict Loan Status"** button.
4. The app displays the prediction: ✅ Loan Approved or ❌ Loan Rejected.
5. Prediction is made using a trained Random Forest Classifier.

---

## 🛠 Tech Stack

- **Language:** Python
- **ML Library:** Scikit-learn
- **Web App:** Streamlit
- **Version Control:** Git + GitHub
- **Deployment:** Streamlit Cloud


### ✅ 1. Clone the Repo

```bash
git clone https://github.com/Nikhil-Donthusaram/LoanApprovalPrediction-RandomForest.git
cd LoanApprovalPrediction-RandomForest
