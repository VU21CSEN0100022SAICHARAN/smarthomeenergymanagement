import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Connect to the MySQL database
engine = create_engine('mysql+pymysql://root:@localhost/energy_management')

# Query the energy_usage table
query = """
SELECT user_id, appliance_id, usage_date, usage_kwh
FROM energy_usage
"""
df = pd.read_sql(query, engine)

# Preprocessing
df['usage_date'] = pd.to_datetime(df['usage_date'])
df['day_of_week'] = df['usage_date'].dt.dayofweek
df['hour'] = df['usage_date'].dt.hour

# Features and target variable
X = df[['user_id', 'appliance_id', 'day_of_week', 'hour']]
y = df['usage_kwh']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the model
import joblib
joblib.dump(model, 'energy_usage_model.pkl')
