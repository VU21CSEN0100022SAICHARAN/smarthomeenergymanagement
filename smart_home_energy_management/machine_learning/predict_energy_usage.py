import sys
import pandas as pd
import joblib

# Load the model
model = joblib.load('energy_usage_model.pkl')

# Get user input from command line arguments
user_id = int(sys.argv[1])
appliance_id = int(sys.argv[2])
day_of_week = int(sys.argv[3])
hour = int(sys.argv[4])

# Create a DataFrame with the input data
input_data = pd.DataFrame({
    'user_id': [user_id],
    'appliance_id': [appliance_id],
    'day_of_week': [day_of_week],
    'hour': [hour]
})

# Predict energy usage
predicted_usage = model.predict(input_data)
print(predicted_usage[0])
