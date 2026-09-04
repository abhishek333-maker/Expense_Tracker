"""
expense_manager.py
Core business logic for adding, viewing, searching, deleting expenses,
and generating monthly / category-wise summaries.
"""

import storage
import utils


def add_expense():
    print("\n--- Add Expense ---")
    amount = utils.read_amount()
    category = utils.read_category()
    date = utils.read_date()
    description = utils.read_description()

    expense = {
        "id": storage.get_next_id(),
        "amount": amount,
        "category": category,
        "date": date,
        "description": description,
    }
    storage.append_expense(expense)
    print(f"Expense added successfully (ID: {expense['id']}).")


def view_all_expenses():
    print("\n--- All Expenses ---")
    expenses = storage.load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    _print_table(expenses)


def search_expenses():
    print("\n--- Search Expenses ---")
    print("Search by: 1. Category   2. Date")
    choice = utils.read_menu_choice(1, 2)

    expenses = storage.load_expenses()
    if choice == 1:
        category = utils.read_category("Select category to search:")
        results = [e for e in expenses if e["category"] == category]
    else:
        date = utils.read_date("Enter date to search (YYYY-MM-DD): ")
        results = [e for e in expenses if e["date"] == date]

    if not results:
        print("No matching expenses found.")
        return
    _print_table(results)


def delete_expense():
    print("\n--- Delete Expense ---")
    expenses = storage.load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    _print_table(expenses)
    raw_id = input("Enter the ID of the expense to delete: ").strip()

    if not raw_id.isdigit():
        print("Invalid ID. Please enter a numeric ID.")
        return

    target_id = raw_id
    remaining = [e for e in expenses if e["id"] != target_id]

    if len(remaining) == len(expenses):
        print(f"No expense found with ID {target_id}.")
        return

    storage.save_expenses(remaining)
    print(f"Expense with ID {target_id} deleted successfully.")


def monthly_summary():
    print("\n--- Monthly Summary ---")
    month = utils.read_month()
    expenses = storage.load_expenses()
    month_expenses = [e for e in expenses if e["date"].startswith(month)]

    if not month_expenses:
        print(f"No expenses found for {month}.")
        return

    total = sum(float(e["amount"]) for e in month_expenses)
    _print_table(month_expenses)
    print(f"\nTotal expenses for {month}: {total:.2f}")


def category_report():
    print("\n--- Category-wise Report ---")
    expenses = storage.load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + float(e["amount"])

    print(f"{'Category':<15}{'Total Amount':>15}")
    print("-" * 30)
    for category, total in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{category:<15}{total:>15.2f}")


def get_total_expenses_for_month(month):
    """Helper used by budget_manager to compute total spend for a given month."""
    expenses = storage.load_expenses()
    return sum(float(e["amount"]) for e in expenses if e["date"].startswith(month))


def _print_table(expenses):
    print(f"{'ID':<5}{'Amount':>10}  {'Category':<14}{'Date':<12}{'Description'}")
    print("-" * 65)
    for e in expenses:
        print(f"{e['id']:<5}{float(e['amount']):>10.2f}  {e['category']:<14}{e['date']:<12}{e['description']}")
