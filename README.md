# Personal Expense Tracker
A simple web-based personal expense tracker built with Flask and HTML. This project allows users to input their daily expenses, categorize them, and visualize spending patterns. It also includes a date picker for easy date selection.

## Features
- Add Expense: Users can enter their expenses along with a description, amount, and category.
- Date Picker: A calendar-based input field allows users to select the date of the expense.
- Categories: Users can categorize their expenses into predefined categories such as Education, Groceries, Rent, Entertainment, and Others.
- Data Visualization: Generate visual summaries of spending patterns.
- User-Friendly Interface: The form is easy to use, with input validation to ensure all required fields are filled out.

## Project Setup
Follow these steps to run the application on your local machine.

### Prerequisites
- Python 3.x
- Flask
- Pandas
- Matplotlib (optional for visualization)

### Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/Vishesh29/personal-expense-tracker.git
cd personal-expense-tracker
```

2. Create and activate a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

### Running the Application
1. Start the Flask app:
```
python expense_app.py
```

2. Open your browser and visit http://127.0.0.1:5000/ to start using the expense tracker.


### File Structure
```
expense-tracker/
│
├── expense_app.py            # Main Flask application file
├── templates/
│   └── index.html          # HTML file for the input form
│   └── visualization.html  # HTML file for the visualization
│
├── static/
│   └── style.css           # CSS file for styling the form
│   └── visualization.png   # Placeholder for any generated visualization (optional)
│
├── requirements.txt        # List of project dependencies
└── README.md               # This README file
```

### Usage
1. Input Expense:
  - Use the input form to enter the date, description, amount, and category of your expense.
  - Select the date from the calendar input field.

2. Data Visualization (Optional):
  - Visualize your expenses with graphs or charts (matplotlib functionality).

### Contributions
Feel free to fork the repository and submit pull requests. If you have any suggestions or improvements, please open an issue or create a pull request.

### License
This project is licensed under the MIT License.
