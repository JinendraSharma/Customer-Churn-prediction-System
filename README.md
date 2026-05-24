# Customer Churn Prediction System

## Project Overview
This project is a Full Stack Machine Learning based Customer Churn Prediction System built using Python, Flask, SQLite, and Scikit-learn.

The system predicts whether a customer is likely to leave the company based on customer behavior and service-related features.

Users can:
- Create accounts
- Login securely
- Upload customer datasets
- Predict customer churn using a trained ML model
- View churn prediction results

---

## Features

- User Signup & Login Authentication
- SQLite Database Integration
- Customer Dataset Upload
- Machine Learning Based Churn Prediction
- Feature Encoding using One-Hot Encoding
- Logistic Regression Model
- Prediction Result Dashboard
- CSV Prediction File Generation
- Data Visualization
- Flask Backend Integration

---

## Technologies Used

### Frontend
- HTML
- CSS

### Backend
- Flask (Python)

### Database
- SQLite

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Machine Learning Workflow

```text
Customer Dataset
        ↓
Data Cleaning
        ↓
Feature Encoding
        ↓
Model Training
        ↓
Trained Model (.pkl)
        ↓
Flask Backend
        ↓
User Uploads CSV
        ↓
Prediction
        ↓
Result Dashboard
```

---

## Dataset Features

The model uses customer behavior features such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Tech Support
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

Dataset Size:
- 7043 Customer Records

---

## Model Information

Algorithm Used:
- Logistic Regression

Model Accuracy:
```text
~81% Accuracy
```

---

## Authentication System

The project includes:

- User Signup
- User Login
- Session Management
- Logout Functionality

User credentials are stored using SQLite Database.

---

## File Upload System

Users can upload their own customer datasets in CSV format.

The backend:
- Reads uploaded CSV files
- Applies preprocessing
- Encodes categorical features
- Loads pretrained ML model
- Predicts customer churn
- Generates prediction results

---

## Project Structure

```text
customer-churn-project/
│
├── app.py
├── train_model.py
├── customer_churn.csv
├── churn_model.pkl
├── model_columns.pkl
├── users.db
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Application Architecture

```text
Frontend (HTML/CSS)
        ↓
Flask Backend
        ↓
SQLite Database
        ↓
ML Prediction Engine
        ↓
Prediction Results
```

---

## Future Improvements

- Add Advanced ML Models
- Add Password Hashing
- Deploy on Cloud
- Add Interactive Dashboard
- Add Real-Time Predictions
- Add Charts and Analytics
- Add Admin Panel

---

## Conclusion

This project demonstrates a complete Full Stack Machine Learning workflow including:

- Frontend Development
- Backend Development
- Database Integration
- Authentication System
- File Upload Handling
- Data Preprocessing
- Feature Engineering
- Machine Learning Model Training
- Prediction System

The application predicts customer churn using customer behavioral data and Logistic Regression.
