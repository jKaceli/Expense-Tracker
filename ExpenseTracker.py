import tkinter as tk
from tkinter import messagebox


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Expense input variables
        self.expense_amount = tk.DoubleVar()
        self.expense_category = tk.StringVar()

        # Expense data
        self.expenses = []

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Expense Entry
        tk.Label(self.root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.root, textvariable=self.expense_amount)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(self.root, textvariable=self.expense_category)
        self.category_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, pady=10)

        # Expense List
        self.expense_listbox = tk.Listbox(self.root, width=50)
        self.expense_listbox.grid(row=3, column=0, columnspan=2)

    def add_expense(self):
        amount = self.expense_amount.get()
        category = self.expense_category.get()

        if amount <= 0:
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        if not category:
            messagebox.showerror("Error", "Please enter a category")
            return

        self.expenses.append((amount, category))
        self.update_expense_listbox()
        self.clear_entries()

    def update_expense_listbox(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, f"${expense[0]} - {expense[1]}")

    def clear_entries(self):
        self.expense_amount.set(0.0)
        self.expense_category.set("")


def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

