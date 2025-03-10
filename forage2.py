import pandas as pd
from flask import Flask, request, jsonify

# Sample financial data (this would normally come from a CSV or database)
financial_data = {
    "total_revenue": "$1,000,000",
    "net_income_change": "increased by $100,000",
    "operating_expenses": "$500,000",
    "profit_margin": "25%"
}

# Flask app setup
app = Flask(__name__)

# Simple chatbot function
def simple_chatbot(user_query):
    user_query = user_query.lower()
    if "total revenue" in user_query:
        return f"The total revenue is {financial_data['total_revenue']}."
    elif "net income" in user_query:
        return f"The net income has {financial_data['net_income_change']} over the last year."
    elif "operating expenses" in user_query:
        return f"The operating expenses are {financial_data['operating_expenses']}."
    elif "profit margin" in user_query:
        return f"The profit margin is {financial_data['profit_margin']}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Flask route to handle chatbot interaction
@app.route('/chat', methods=['GET'])
def chat():
    user_query = request.args.get('query')
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

# Documentation:
# This is a simple financial chatbot prototype using Flask and Python.
# It responds to predefined queries like total revenue, net income change, operating expenses, and profit margin.
# Limitations: Only handles specific hardcoded questions, lacks natural language processing, and advanced AI capabilities.
