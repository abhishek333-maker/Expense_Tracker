"""
utils.py
Small reusable helpers for reading and validating user input from the CLI.
Centralizing validation avoids repeating try/except blocks in every menu action.
"""

from datetime import datetime

VALID_CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Health", "Other"]


def read_amount(prompt="Enter amount: "):
    """Keep asking until the user enters a positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Please enter a numeric value (e.g. 250 or 99.50).")


def read_category(prompt=None):
    """Show a numbered list of categories and let the user pick one."""
    if prompt:
        print(prompt)
    for i, cat in enumerate(VALID_CATEGORIES, start=1):
        print(f"  {i}. {cat}")
    while True:
        raw = input(f"Choose category (1-{len(VALID_CATEGORIES)}): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(VALID_CATEGORIES):
            return VALID_CATEGORIES[int(raw) - 1]
        print("Invalid choice. Please enter a valid number from the list.")


def read_date(prompt="Enter date (YYYY-MM-DD): "):
    """Validate a full date string in YYYY-MM-DD format."""
    while True:
        raw = input(prompt).strip()
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g. 2026-08-31).")


def read_month(prompt="Enter month (YYYY-MM): "):
    """Validate a year-month string in YYYY-MM format."""
    while True:
        raw = input(prompt).strip()
        try:
            datetime.strptime(raw, "%Y-%m")
            return raw
        except ValueError:
            print("Invalid month format. Please use YYYY-MM (e.g. 2026-08).")


def read_description(prompt="Enter description (optional): "):
    """Description is optional; just strip whitespace and cap length."""
    raw = input(prompt).strip()
    return raw[:200] if raw else "-"


def read_menu_choice(min_val, max_val, prompt="Enter your choice: "):
    """Generic menu-choice reader used across the app."""
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and min_val <= int(raw) <= max_val:
            return int(raw)
        print(f"Invalid choice. Please enter a number between {min_val} and {max_val}.")
