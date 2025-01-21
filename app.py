import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
file_path = "C:\\Users\\asd\\Downloads\\insurance.csv"
df = pd.read_csv(file_path)

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['sex']= lb.fit_transform(df['sex'])
df['smoker']= lb.fit_transform(df['smoker'])
df['region']= lb.fit_transform(df['region'])


x = df.drop(columns= ['charges'])
y =df['charges']

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a linear regression model
lr = LinearRegression()
lr.fit(x_train, y_train)

# Make predictions on the test data
y_pred = lr.predict(x_test)

# Calculate and display the R2 score
r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2}")
