"""
storage.py
Handles all direct reading/writing to the CSV data files.
Keeping file I/O in one place makes it easy to change storage format later
without touching business logic in other modules.
"""

import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.csv")
BUDGET_FILE = os.path.join(DATA_DIR, "budget.csv")

EXPENSE_FIELDS = ["id", "amount", "category", "date", "description"]


def _ensure_data_files():
    """Create the data folder/files with headers if they don't exist yet."""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.isfile(EXPENSES_FILE):
        with open(EXPENSES_FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=EXPENSE_FIELDS).writeheader()

    if not os.path.isfile(BUDGET_FILE):
        with open(BUDGET_FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["month", "amount"])


def load_expenses():
    """Return all expenses as a list of dicts. Never raises on missing file."""
    _ensure_data_files()
    with open(EXPENSES_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def save_expenses(expenses):
    """Overwrite the expenses file with the given list of dicts (used after delete)."""
    _ensure_data_files()
    with open(EXPENSES_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EXPENSE_FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def append_expense(expense):
    """Append a single expense without touching existing rows (safe for large files)."""
    _ensure_data_files()
    with open(EXPENSES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EXPENSE_FIELDS)
        writer.writerow(expense)


def get_next_id():
    """Generate the next sequential expense id based on existing records."""
    expenses = load_expenses()
    if not expenses:
        return 1
    return max(int(e["id"]) for e in expenses) + 1


def load_budgets():
    """Return budgets as a dict: {"YYYY-MM": amount(float)}."""
    _ensure_data_files()
    budgets = {}
    with open(BUDGET_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if len(row) == 2:
                budgets[row[0]] = float(row[1])
    return budgets


def save_budgets(budgets):
    """Overwrite the budget file with the given dict {"YYYY-MM": amount}."""
    _ensure_data_files()
    with open(BUDGET_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "amount"])
        for month, amount in budgets.items():
            writer.writerow([month, amount])
