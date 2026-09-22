# Expense Tracker

## Explanation

The Expense Tracker is a simple Python application used to record and manage daily expenses. Users can add expenses, view all recorded expenses, and calculate the total amount spent.

## Problem Statement

Create a Python program that allows users to enter their expenses and provides a summary of their total spending.

## Features

* Add an expense
* View all expenses
* Calculate total expenses
* Menu-driven interface
* Simple and easy to use

## How It Works

1. The program displays a menu.
2. The user chooses an option.
3. Expense details are stored in a list.
4. The program displays the recorded expenses or calculates the total.
5. The menu continues until the user chooses Exit.

## Technologies Used

* Python
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements

## Data Structure Used

* List
* Dictionary

## Methods Used

* `add_expense()`
* `view_expenses()`
* `calculate_total()`
* `main()`

## Program Flow

```text
Start
  ↓
Display Menu
  ↓
Choose Option
  ↓
Add / View / Calculate Total
  ↓
Return to Menu
  ↓
Exit
  ↓
End
```

## Sample Input

```text
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit

Enter your choice: 1
Enter expense name: Food
Enter amount: 250
```

## Sample Output

```text
Expense added successfully!

Expenses:
1. Food - ₹250.00

Total Expenses = ₹250.00
```

## Time Complexity

* Add Expense: O(1)
* View Expenses: O(n)
* Calculate Total: O(n)

## Space Complexity

O(n)

## Key Learning

* Working with lists and dictionaries
* Using functions
* Handling numerical input
* Calculating totals
* Creating menu-driven Python applications

## File Location

`expense_tracker.py`

## Repository Structure

```text
python-expense-tracker/
│
├── expense_tracker.py
└── README.md
```

## Author

V.Harini
