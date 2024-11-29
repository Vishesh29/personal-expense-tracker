import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# Create a DataFrame to simulate the expense data (initially empty)
expense_data = []

# Route to display the form and expenses
@app.route('/')
def index():
    return render_template('index.html', expenses=expense_data)

# Route to add a new expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Get the form data
    date = request.form['Date']
    description = request.form['Description']
    amount = float(request.form['Amount'])
    category = request.form['Category']

    # Add new expense to the expense data list
    expense_data.append({'Date': date, 'Description': description, 'Amount': amount, 'Category': category})
    
    # Redirect back to the index page
    return redirect(url_for('index'))

# Route to generate the visualization of expenses
@app.route('/visualize')
def visualize():
    # Convert the expense data list to a DataFrame
    df = pd.DataFrame(expense_data)

    # Check if 'Category' column exists and handle missing categories
    if 'Category' not in df.columns:
        return "Error: 'Category' column is missing in the data!", 400

    # Fill missing 'Category' values with 'Uncategorized'
    df['Category'] = df['Category'].fillna('Uncategorized')

    # Group expenses by category and sum the amounts
    category_totals = df.groupby('Category')['Amount'].sum().reset_index()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(category_totals['Category'], category_totals['Amount'], color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.title('Total Expenses by Category')
    
    # Save the plot as a PNG file in the 'static' directory
    plt.savefig('static/visualization.png')

    # Return the visualization to the user
    return render_template('visualization.html')

if __name__ == '__main__':
    # Ensure the static folder exists
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
