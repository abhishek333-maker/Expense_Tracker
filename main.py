"""
main.py
Entry point for the Expense Tracker CLI application.
Displays the main menu and routes user choices to the relevant modules.
"""

import expense_manager
import budget_manager

MENU_TEXT = """
========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Delete Expense
5. Monthly Summary
6. Category-wise Report
7. Set Monthly Budget
8. Check Budget Status
9. Exit
======================================
"""


def main():
    while True:
        print(MENU_TEXT)
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            expense_manager.add_expense()
        elif choice == "2":
            expense_manager.view_all_expenses()
        elif choice == "3":
            expense_manager.search_expenses()
        elif choice == "4":
            expense_manager.delete_expense()
        elif choice == "5":
            expense_manager.monthly_summary()
        elif choice == "6":
            expense_manager.category_report()
        elif choice == "7":
            budget_manager.set_monthly_budget()
        elif choice == "8":
            budget_manager.check_budget_status()
        elif choice == "9":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting safely.")
