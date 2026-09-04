"""
budget_manager.py
Handles setting a monthly budget and checking spending status against it.
"""

import storage
import utils
import expense_manager


def set_monthly_budget():
    print("\n--- Set Monthly Budget ---")
    month = utils.read_month()
    amount = utils.read_amount("Enter monthly budget amount: ")

    budgets = storage.load_budgets()
    budgets[month] = amount
    storage.save_budgets(budgets)
    print(f"Budget for {month} set to {amount:.2f} successfully.")


def check_budget_status():
    print("\n--- Check Budget Status ---")
    month = utils.read_month()

    budgets = storage.load_budgets()
    if month not in budgets:
        print(f"No budget has been set for {month}. Please set a budget first.")
        return

    budget = budgets[month]
    spent = expense_manager.get_total_expenses_for_month(month)
    remaining = budget - spent

    print(f"\nMonth        : {month}")
    print(f"Budget       : {budget:.2f}")
    print(f"Total Spent  : {spent:.2f}")
    if remaining >= 0:
        print(f"Remaining    : {remaining:.2f}")
        print("Status       : Within budget")
    else:
        print(f"Over Budget  : {abs(remaining):.2f}")
        print("Status       : Budget exceeded")
