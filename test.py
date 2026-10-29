expenses = []

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added!")


def view_expenses():
    print("\n=== EXPENSE LIST ===")

    if len(expenses) == 0:
        print("No expenses yet.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['name']} - {expense['amount']:.2f} THB")


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: {total:.2f} THB")


while True:
    print("\n=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
