import csv
import matplotlib.pyplot as plt
import os

expenses = []
filename = "expenses.csv"

def load_expenses():
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)

def save_expense_to_file(expense):
    file_exists = os.path.exists(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense)

def add_expense():
    category = input("Expense category (e.g., Food, Transport): ")
    amount = float(input("Amount spent: "))
    date = input("Date (e.g., 2026-08-15): ")
    
    expense = {"category": category, "amount": amount, "date": date}
    expenses.append(expense)
    save_expense_to_file(expense)
    print("Expense added successfully!\n")

def show_summary():
    total = 0
    category_totals = {}
    
    for expense in expenses:
        total += expense["amount"]
        cat = expense["category"]
        if cat in category_totals:
            category_totals[cat] += expense["amount"]
        else:
            category_totals[cat] = expense["amount"]
    
    print(f"\nTotal Spending: {total}")
    print("\nCategory-wise Breakdown:")
    for category, amount in category_totals.items():
        print(f"{category}: {amount}")
        categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, amounts, color=['#2E86AB', '#E63946', '#06A77D', '#F4A261'])
    plt.title('Expense Breakdown by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount (PKR)')
    plt.savefig('expense_chart.png')
    plt.show()

def main():
    load_expenses()
    while True:
        add_expense()
        more = input("Add another expense? (yes/no): ")
        if more.lower() != "yes":
            break
    
    show_summary()

main()