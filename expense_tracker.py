expenses = []

def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))

        if amount < 0:
            print("Amount cannot be negative.")
            return

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']:.2f}")

def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses = ₹{total:.2f}")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
