# Python Expense Tracker

## Project Overview
A command-line personal expense tracker built in Python. The application lets users log daily expenses by category, permanently saves them to a CSV file, and generates a visual breakdown of spending by category.

## Features
- Add expenses with category, amount, and date
- Automatically saves all expenses to a CSV file (data persists across sessions)
- Loads previously saved expenses when the program restarts
- Calculates total spending and category-wise breakdown
- Generates a bar chart visualizing spending by category

## Tools & Libraries Used
- Python
- CSV module (for reading/writing expense data)
- OS module (for file handling)
- Matplotlib (for data visualization)

## How It Works
1. User enters expenses one at a time (category, amount, date)
2. Each expense is saved immediately to `expenses.csv`
3. Once the user is done adding expenses, the program calculates:
   - Total spending across all categories
   - A breakdown of spending per category
4. A bar chart is generated showing the spending distribution across categories

## Concepts Practiced
- Functions and modular code structure
- Loops and user input handling
- Dictionaries for organizing structured data
- File handling (reading/writing CSV files)
- Data visualization with Matplotlib

## How to Run
1. Make sure Python is installed, along with the `matplotlib` library (`pip install matplotlib`)
2. Run `expense_tracker.py`
3. Follow the prompts to add expenses
4. View the summary and generated chart (`expense_chart.png`)

## Author
Independent Python project built to practice core programming concepts including file handling and data visualization.
