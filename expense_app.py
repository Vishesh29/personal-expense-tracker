from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

expenses = []  # List to hold expenses temporarily

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form['Date']
    description = request.form['Description']
    amount = float(request.form['Amount'])
    category = request.form['Category']

    # Store the expense
    expenses.append({
        'Date': date,
        'Description': description,
        'Amount': amount,
        'Category': category
    })

    return redirect(url_for('index'))

@app.route('/visualize')
def visualize():
    df = pd.DataFrame(expenses)
    category_totals = df.groupby('Category')['Amount'].sum().reset_index()

    # Visualization (simple bar chart)
    plt.figure(figsize=(10, 6))
    plt.bar(category_totals['Category'], category_totals['Amount'], color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45, ha='right')

    # Save chart as static file
    plt.tight_layout()
    plt.savefig('static/visualization.png')

    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(debug=True)
