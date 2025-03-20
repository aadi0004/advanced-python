import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

df = pd.read_csv("Salary_Data.csv")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = np.asanyarray(df[['YearsExperience']])
y = np.asanyarray(df[['Salary']])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        experience = float(request.form['experience'])
        features = np.array([[experience]])
        prediction = lr.predict(features)[0][0]
        return render_template('index.html', prediction_text=f'Predicted Salary: ${prediction:.2f}')
    except Exception as e:
        return render_template('index.html', error_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
