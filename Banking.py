import tkinter as tk
from tkinter import messagebox

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0):
        super().__init__(account_number, account_holder, initial_balance)

class BankingSystemGUI:
    def __init__(self, root):
        self.accounts = {}
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("500x600")  # Set window size

        # Set background color for the root window
        self.root.config(bg="#f0f0f0")  # Light gray background

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(padx=10, pady=10)

        # Create a larger label with bigger font and background color
        self.label = tk.Label(self.frame, text="Banking System Menu", font=("Arial", 40), bg="#f0f0f0")
        self.label.pack(pady=20)

        # Buttons with increased size and background color
        self.create_account_btn = tk.Button(self.frame, text="Create Account", font=("Arial", 14), width=30, height=2, command=self.create_account, bg="#4CAF50", fg="white")
        self.create_account_btn.pack(pady=5)

        self.deposit_btn = tk.Button(self.frame, text="Deposit Money", font=("Arial", 14), width=30, height=2, command=self.deposit_money, bg="#4CAF50", fg="white")
        self.deposit_btn.pack(pady=5)

        self.withdraw_btn = tk.Button(self.frame, text="Withdraw Money", font=("Arial", 14), width=30, height=2, command=self.withdraw_money, bg="#4CAF50", fg="white")
        self.withdraw_btn.pack(pady=5)

        self.transfer_btn = tk.Button(self.frame, text="Transfer Money", font=("Arial", 14), width=30, height=2, command=self.transfer_money, bg="#4CAF50", fg="white")
        self.transfer_btn.pack(pady=5)

        self.calculate_interest_btn = tk.Button(self.frame, text="Calculate Interest (Savings Account)", font=("Arial", 14), width=30, height=2, command=self.calculate_interest, bg="#4CAF50", fg="white")
        self.calculate_interest_btn.pack(pady=5)

        self.display_info_btn = tk.Button(self.frame, text="Display Account Info", font=("Arial", 14), width=30, height=2, command=self.display_account_info, bg="#4CAF50", fg="white")
        self.display_info_btn.pack(pady=5)

        self.exit_btn = tk.Button(self.frame, text="Exit", font=("Arial", 14), width=30, height=2, command=root.quit, bg="#f44336", fg="white")
        self.exit_btn.pack(pady=10)

    def create_account(self):
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Account")
        create_account_window.geometry("400x400")  # Set size of the new window

        # Set background color for the new window
        create_account_window.config(bg="#f0f0f0")

        # Labels and entries with increased font and box size
        tk.Label(create_account_window, text="Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_number_entry = tk.Entry(create_account_window, font=("Arial", 12), width=30)
        account_number_entry.pack(pady=5)

        tk.Label(create_account_window, text="Account Holder:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_holder_entry = tk.Entry(create_account_window, font=("Arial", 12), width=30)
        account_holder_entry.pack(pady=5)

        tk.Label(create_account_window, text="Account Type (savings/checking):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_type_entry = tk.Entry(create_account_window, font=("Arial", 12), width=30)
        account_type_entry.pack(pady=5)

        tk.Label(create_account_window, text="Initial Balance:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        initial_balance_entry = tk.Entry(create_account_window, font=("Arial", 12), width=30)
        initial_balance_entry.pack(pady=5)

        tk.Label(create_account_window, text="Interest Rate (for savings):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        interest_rate_entry = tk.Entry(create_account_window, font=("Arial", 12), width=30)
        interest_rate_entry.pack(pady=5)

        def submit_account():
            account_number = account_number_entry.get()
            account_holder = account_holder_entry.get()
            account_type = account_type_entry.get().lower()
            initial_balance = float(initial_balance_entry.get())
            interest_rate = float(interest_rate_entry.get())

            if account_type == "savings":
                self.accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
            elif account_type == "checking":
                self.accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)
            else:
                messagebox.showerror("Error", "Invalid account type!")

            create_account_window.destroy()

        tk.Button(create_account_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_account, bg="#4CAF50", fg="white").pack(pady=10)

    def deposit_money(self):
        deposit_window = tk.Toplevel(self.root)
        deposit_window.title("Deposit Money")
        deposit_window.geometry("400x300")  # Set size of the new window

        # Set background color for the new window
        deposit_window.config(bg="#f0f0f0")

        # Labels and entries with increased font and box size
        tk.Label(deposit_window, text="Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_number_entry = tk.Entry(deposit_window, font=("Arial", 12), width=30)
        account_number_entry.pack(pady=5)

        tk.Label(deposit_window, text="Amount:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        amount_entry = tk.Entry(deposit_window, font=("Arial", 12), width=30)
        amount_entry.pack(pady=5)

        def submit_deposit():
            account_number = account_number_entry.get()
            amount = float(amount_entry.get())
            if account_number in self.accounts:
                try:
                    self.accounts[account_number].deposit(amount)
                    messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[account_number].get_balance()}.")
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", "Account not found!")

            deposit_window.destroy()

        tk.Button(deposit_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_deposit, bg="#4CAF50", fg="white").pack(pady=10)

    def withdraw_money(self):
        withdraw_window = tk.Toplevel(self.root)
        withdraw_window.title("Withdraw Money")
        withdraw_window.geometry("400x300")  # Set size of the new window

        # Set background color for the new window
        withdraw_window.config(bg="#f0f0f0")

        # Labels and entries with increased font and box size
        tk.Label(withdraw_window, text="Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_number_entry = tk.Entry(withdraw_window, font=("Arial", 12), width=30)
        account_number_entry.pack(pady=5)

        tk.Label(withdraw_window, text="Amount:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        amount_entry = tk.Entry(withdraw_window, font=("Arial", 12), width=30)
        amount_entry.pack(pady=5)

        def submit_withdrawal():
            account_number = account_number_entry.get()
            amount = float(amount_entry.get())
            if account_number in self.accounts:
                try:
                    self.accounts[account_number].withdraw(amount)
                    messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[account_number].get_balance()}.")
                except InsufficientFundsError as e:
                    messagebox.showerror("Error", str(e))
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", "Account not found!")

            withdraw_window.destroy()

        tk.Button(withdraw_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_withdrawal, bg="#4CAF50", fg="white").pack(pady=10)

    def transfer_money(self):
        transfer_window = tk.Toplevel(self.root)
        transfer_window.title("Transfer Money")
        transfer_window.geometry("400x400")  # Set size of the new window

        # Set background color for the new window
        transfer_window.config(bg="#f0f0f0")

        # Labels and entries with increased font and box size
        tk.Label(transfer_window, text="From Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        from_account_entry = tk.Entry(transfer_window, font=("Arial", 12), width=30)
        from_account_entry.pack(pady=5)

        tk.Label(transfer_window, text="To Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        to_account_entry = tk.Entry(transfer_window, font=("Arial", 12), width=30)
        to_account_entry.pack(pady=5)

        tk.Label(transfer_window, text="Amount:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        amount_entry = tk.Entry(transfer_window, font=("Arial", 12), width=30)
        amount_entry.pack(pady=5)

        def submit_transfer():
            from_account = from_account_entry.get()
            to_account = to_account_entry.get()
            amount = float(amount_entry.get())
            if from_account in self.accounts and to_account in self.accounts:
                try:
                    self.accounts[from_account].withdraw(amount)
                    self.accounts[to_account].deposit(amount)
                    messagebox.showinfo("Success", f"Transferred {amount} from {from_account} to {to_account}.")
                except InsufficientFundsError as e:
                    messagebox.showerror("Error", str(e))
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showerror("Error", "One or both accounts not found!")

            transfer_window.destroy()

        tk.Button(transfer_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_transfer, bg="#4CAF50", fg="white").pack(pady=10)

    def calculate_interest(self):
        interest_window = tk.Toplevel(self.root)
        interest_window.title("Calculate Interest")
        interest_window.geometry("400x300")  # Set size of the new window

        # Set background color for the new window
        interest_window.config(bg="#f0f0f0")

        tk.Label(interest_window, text="Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_number_entry = tk.Entry(interest_window, font=("Arial", 12), width=30)
        account_number_entry.pack(pady=5)

        def submit_interest():
            account_number = account_number_entry.get()
            if account_number in self.accounts:
                if isinstance(self.accounts[account_number], SavingsAccount):
                    self.accounts[account_number].calculate_interest()
                    messagebox.showinfo("Success", f"Interest calculated. New balance is {self.accounts[account_number].get_balance()}.")
                else:
                    messagebox.showerror("Error", "Interest calculation is only available for savings accounts!")
            else:
                messagebox.showerror("Error", "Account not found!")

            interest_window.destroy()

        tk.Button(interest_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_interest, bg="#4CAF50", fg="white").pack(pady=10)

    def display_account_info(self):
        display_info_window = tk.Toplevel(self.root)
        display_info_window.title("Display Account Info")
        display_info_window.geometry("400x300")  # Set size of the new window

        # Set background color for the new window
        display_info_window.config(bg="#f0f0f0")

        tk.Label(display_info_window, text="Account Number:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        account_number_entry = tk.Entry(display_info_window, font=("Arial", 12), width=30)
        account_number_entry.pack(pady=5)

        def submit_display_info():
            account_number = account_number_entry.get()
            if account_number in self.accounts:
                info = self.accounts[account_number].display_account_info()
                messagebox.showinfo("Account Info", info)
            else:
                messagebox.showerror("Error", "Account not found!")

            display_info_window.destroy()

        tk.Button(display_info_window, text="Submit", font=("Arial", 14), width=20, height=2, command=submit_display_info, bg="#4CAF50", fg="white").pack(pady=10)

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    banking_system_gui = BankingSystemGUI(root)
    root.mainloop()
