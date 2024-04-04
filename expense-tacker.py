import datetime

expenses = {}

# Function to add an expense
def add_expense(amount, category, date):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({"amount": amount, "category": category})

# Function to view spending patterns
def view_spending_pattern():
    print("\n---- Spending Patterns ----")
    for date, expense_list in expenses.items():
        total_spent = sum(expense["amount"] for expense in expense_list)
        print(f"{date}: Total Spent: ₹{total_spent}")
        for expense in expense_list:
            print(f"   - ₹{expense['amount']} in {expense['category']}")

# Function to delete an expense
def delete_expense(date, expense_index):
    if date in expenses and expense_index < len(expenses[date]):
        del expenses[date][expense_index]
        print("Expense deleted successfully!")
    else:
        print("Invalid date or expense index. Please try again.")

# Main function
def main():
    while True:
        print("\n---- Expense Tracking System ----")
        print("1. Add Expense")
        print("2. View Spending Patterns")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the amount spent: ₹"))
            category = input("Enter the category: ")
            date = datetime.date.today().strftime("%Y-%m-%d")
            add_expense(amount, category, date)
            print("Expense added successfully!")
        elif choice == "2":
            view_spending_pattern()
        elif choice == "3":
            date = input("Enter the date of the expense (YYYY-MM-DD): ")
            expense_index = int(input("Enter the index of the expense to delete: ")) - 1
            delete_expense(date, expense_index)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Entry point of the program
if __name__ == "__main__":
    main()