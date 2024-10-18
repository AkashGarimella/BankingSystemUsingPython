"""
Develop a banking system where the user can create and account, deposit money, withdraw money, and check their balance. Use classes to represent the account and its methods.

Sample output:
Options: deposit, withdraw, check balance, exit
What would you like to do? deposit
Enter amount to deposit: 500
Deposited: $500.00.  New Balance: $500.00.

"""


class Bank:
    def __init__(self):
        # Dictionary to store account details (username: password)
        self.accounts = {}
        # Dictionary to store account balances (username: balance)
        self.balances = {}

    def create_acc(self, username, password):
        # Check if the account already exists
        if username in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[username] = password
            self.balances[username] = 0  # New account starts with a zero balance
            print(f"Account created. | Username: {username} | Password: {password}")

    def deposit(self, username):
        # Ensure the account exists
        if username in self.accounts:
            amount = float(input("Enter amount to deposit: "))
            self.balances[username] += amount
            print(f"Deposited: ${amount:.2f}. New Balance: ${self.balances[username]:.2f}")
        else:
            print("Account does not exist.")

    def withdraw(self, username):
        # Ensure the account exists
        if username in self.accounts:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.balances[username]:
                print("Insufficient funds.")
            else:
                self.balances[username] -= amount
                print(f"Withdrawn: ${amount:.2f}. New Balance: ${self.balances[username]:.2f}")
        else:
            print("Account does not exist.")

    def check_balance(self, username):
        # Ensure the account exists
        if username in self.accounts:
            print(f"Current Balance: ${self.balances[username]:.2f}")
        else:
            print("Account does not exist.")

    def options(self, username):
        # Ensure the account exists before offering options
        if username in self.accounts:
            while True:
                print("\nOptions: deposit, withdraw, check balance, exit")
                choice = input("What would you like to do? ").lower()

                if choice == 'deposit':
                    self.deposit(username)
                elif choice == 'withdraw':
                    self.withdraw(username)
                elif choice == 'check balance':
                    self.check_balance(username)
                elif choice == 'exit':
                    print("Thank you for using the banking system!")
                    break
                else:
                    print("Invalid option, please choose again.")
        else:
            print("Please create an account first.")

# Example usage:

bank_system = Bank()
bank_system.create_acc("Akash", "123")
bank_system.options("Akash")
