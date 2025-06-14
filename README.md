## Customer Churn Prediction using Machine Learning

This project predicts whether a customer will churn (i.e., leave the service) based on their account data. It uses several machine learning classification models and compares their performance to determine the most accurate one.

 **Goal:** Enable telecom providers to proactively identify customers at high risk of churn and take steps to retain them.

---

## Models Used

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest Classifier
- XGBoost Classifier

---

##  Dataset

The dataset used is the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle.  
Each row represents one customer with 21 attributes such as:

- Gender
- SeniorCitizen
- Partner
- Tenure
- InternetService
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- Churn (Target variable)

---

##  Machine Learning Pipeline

- ✅ Loaded and cleaned the dataset using Pandas
- ✅ Handled missing values and dropped irrelevant columns
- ✅ Encoded categorical variables using `LabelEncoder`
- ✅ Scaled numerical features using `StandardScaler`
- ✅ Split dataset using an 80:20 train-test split
- ✅ Trained and evaluated 4 different classification models

---

## 📊 Results

| Model               | Accuracy (%) |
|--------------------|--------------|
| Logistic Regression| 79.5%        |
| SVM                | 78.3%        |
| Random Forest      | 81.6%        |
| XGBoost            | **83.4%**    |

>  **XGBoost** achieved the highest accuracy and is considered the best performing model in this project.

---

##  Deployment (Coming Soon)

This project will be deployed using **Streamlit** so users can:
- Fill in customer details in a form
- Get instant prediction: **"Will this customer churn?" → Yes/No**

🔗 Deployment link will be added soon...

---

##  Tech Stack

- **Languages:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **ML:** scikit-learn, XGBoost
- **Deployment:** Streamlit (planned)

---

##  Future Improvements

- Streamlit-based live web app
- Add SHAP values to explain model decisions
- Add feature importance visualizations
- Use deep learning-based models for comparison

---

## 📁 Repository Structure

