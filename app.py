from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import sqlite3
import joblib
import os

app = Flask(__name__)

app.secret_key = "secretkey"

# Load trained model
model = joblib.load("churn_model.pkl")

# Load model columns
model_columns = joblib.load("model_columns.pkl")

# ====================================
# DATABASE
# ====================================

def create_database():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    conn.commit()

    conn.close()

create_database()

# ====================================
# HOME
# ====================================

@app.route('/')
def home():
    return redirect(url_for('login'))

# ====================================
# SIGNUP
# ====================================

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("users.db")

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
        """, (username, email, password))

        conn.commit()

        conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

# ====================================
# LOGIN
# ====================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("users.db")

        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE email=? AND password=?
        """, (email, password))

        user = cursor.fetchone()

        conn.close()

        if user:

            session['user'] = user[1]

            return redirect(url_for('dashboard'))

        else:
            return "Invalid email or password"

    return render_template('login.html')

# ====================================
# DASHBOARD
# ====================================

@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        username=session['user']
    )

# ====================================
# PREDICT
# ====================================

@app.route('/predict', methods=['POST'])
def predict():

    if 'user' not in session:
        return redirect(url_for('login'))

    file = request.files['file']

    if file.filename == '':
        return "No file selected"

    # Read uploaded CSV
    df = pd.read_csv(file)

    # Remove customerID
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    # Encode categorical columns
    df = pd.get_dummies(df, drop_first=True)

    # Match training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    # Predict
    predictions = model.predict(df)

    # Add predictions
    df['Prediction'] = predictions

    # Save output
    output_path = "static/predictions.csv"

    df.to_csv(output_path, index=False)

    churn_count = (predictions == 1).sum()

    stay_count = (predictions == 0).sum()

    return render_template(
        'result.html',
        churn_count=churn_count,
        stay_count=stay_count,
        total=len(predictions)
    )

# ====================================
# LOGOUT
# ====================================

@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect(url_for('login'))

# ====================================
# RUN APP
# ====================================

if __name__ == '__main__':
    app.run(debug=True)