import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
df=pd.read_csv('customer_churn.csv')
# Vieew dataset
df.head()

#check dataset info
df.info()
# Handle missing values
df.isnull().sum()
#data clean
df = df.dropna()

# convert churn column 
df['Churn']=df['Churn'].map({'Yes': 1, 'No': 0})
#remove customerID column
df = df.drop(['customerID'], axis=1)
#convert categorical columns into numbers
df = pd.get_dummies(df, drop_first=True)
# Split the data into features and target variable
X = df.drop('Churn', axis=1)
y = df['Churn']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
# Make predictions
predictions = model.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
# Visualize the results
df['Churn'].value_counts().plot(kind='bar')
plt.title('Customer Churn Distribution')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()
# Monthyly charges visualization
plt.hist(df['MonthlyCharges'])
plt.title('Monthly Charges Distribution')
plt.xlabel('Monthly Charges')
plt.ylabel('Customers')
plt.show()