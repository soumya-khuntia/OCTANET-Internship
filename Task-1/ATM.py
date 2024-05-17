import datetime

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

class Bank:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_id, pin):
        self.users[user_id] = User(user_id, pin)
    
    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return user
        return None

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None
    
    def login(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        user = self.bank.authenticate_user(user_id, pin)
        if user:
            self.current_user = user
            print("\nLogin successful!")
            self.main_menu()
        else:
            print("\nInvalid user ID or PIN.")
    
    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Transaction History")
            print("5. Transfer")
            print("6. Quit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.show_transaction_history()
            elif choice == '5':
                self.transfer()
            elif choice == '6':
                print("\nThank you for using our ATM. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please try again.")
                
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("\nInvalid amount.")
        else:
            self.current_user.balance += amount
            transaction = f"\n{datetime.datetime.now()} - Deposit: ${amount:.2f}"
            self.current_user.transaction_history.append(transaction)
            print(f"\nDeposited ${amount:.2f} successfully!.\n\nCurrent balanace: ${self.current_user.balance:.2f}")

    
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("\nInvalid amount.")
        elif amount > self.current_user.balance:
            print("\nInsufficient balance.")
        else:
            self.current_user.balance -= amount
            transaction = f"\n{datetime.datetime.now()} - Withdraw: ${amount:.2f}"
            self.current_user.transaction_history.append(transaction)
            print(f"\nWithdrew ${amount:.2f} successfully!.\n\nCurrent balance: ${self.current_user.balance:.2f}")
    
    def check_balance(self):
        print(f"\nCurrent balance: ${self.current_user.balance:.2f}")

    def show_transaction_history(self):
        if not self.current_user.transaction_history:
            print("\nNo transactions yet.")
        else:
            for transaction in self.current_user.transaction_history:
                print(transaction)

    def transfer(self):
        recipient_id = input("Enter recipient user ID: ")
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("\nInvalid amount.")
        elif amount > self.current_user.balance:
            print("\nInsufficient balance.")
        else:
            recipient = self.bank.users.get(recipient_id)
            if recipient:
                self.current_user.balance -= amount
                recipient.balance += amount
                transaction_sender = f"\n{datetime.datetime.now()} - Transfer to {recipient_id}: ${amount:.2f}"
                transaction_recipient = f"\n{datetime.datetime.now()} - Transfer from {self.current_user.user_id}: ${amount:.2f}"
                self.current_user.transaction_history.append(transaction_sender)
                recipient.transaction_history.append(transaction_recipient)
                print(f"\nTransferred ${amount:.2f} to {recipient_id} successfully!.\n\nCurrent balance: ${self.current_user.balance:.2f}")
            else:
                print("\nRecipient not found.")
    

# Main program
def main():
    bank = Bank()
    # Adding some users for testing
    bank.add_user("user1", "1234")
    bank.add_user("user2", "5678")
    
    atm = ATM(bank)
    while True:
        atm.login()

if __name__ == "__main__":
    main()
