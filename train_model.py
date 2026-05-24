import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Remove missing values
df = df.dropna()

# Convert target column
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Remove customerID
df = df.drop('customerID', axis=1)

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "churn_model.pkl")

# Save training columns
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("Model trained successfully!")