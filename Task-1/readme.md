# ATM Console-Based Application

This is a console-based ATM application written in Python. It allows users to perform various banking operations such as depositing money, withdrawing money, viewing balance, viewing transaction history, and transferring money between users. The application uses five different classes to manage these functionalities.

## Features

1. **User Authentication:** Users must enter their user ID and PIN to access the ATM functionalities.
2. **Deposit:** Users can deposit money into their account.
3. **Withdraw:** Users can withdraw money from their account.
4. **Balance:** Users can view their account balance.
5. **Transaction History:** Users can view a history of their transactions.
6. **Transfer:** Users can transfer money to another user's account.
7. **Quit:** Users can exit the application.

## Classes

### User
- **Attributes:**
  - `user_id`: User ID
  - `pin`: User PIN
  - `balance`: User account balance
  - `transaction_history`: List of user's transactions

### Bank
- **Attributes:**
  - `users`: Dictionary of users
  
- **Methods:**
  - `add_user(user_id, pin)`: Adds a new user to the bank
  - `authenticate_user(user_id, pin)`: Authenticates a user by user ID and PIN

### ATM
- **Attributes:**
  - `bank`: Instance of the Bank class
  - `current_user`: Currently logged in user
  
- **Methods:**
  - `login()`: Prompts the user for user ID and PIN and logs in the user
  - `main_menu()`: Displays the main menu and handles user choices
  - `deposit()`: Handles money deposit
  - `withdraw()`: Handles money withdrawal
  - `Check_balance()`: Handles checking the account balance
  - `show_transaction_history()`: Displays the user's transaction history
  - `transfer()`: Handles money transfer between users

## Usage

1. **Clone the repository** (if applicable) or copy the code to your local machine.
2. **Run the application** by executing the `ATM.py` file:
   ```bash
   python ATM.py

3. **Sample Output**
   ```bash
    Enter your user ID: user1
    Enter your PIN: 1234
    Login successful!

    --- Main Menu ---
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Transfer
    6. Quit
    Enter your choice: 1
    Enter amount to Deposit: 10000

    Deposited $10000.00 successfully!.
    
    Current balance: $10000.00

    --- Main Menu ---
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Transfer
    6. Quit
    Enter your choice: 2
    Enter amount to Withdraw: 2000

    Withdraw $2000.00 successfully!.

    Current balance: $8000.00

    --- Main Menu ---
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Transfer
    6. Quit
    Enter your choice: 4
    2024-05-17 13:53:07.236120 - Deposit: $10000.00

    2024-05-17 13:53:25.003763 - Withdraw: $2000.00

    --- Main Menu ---
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Transfer
    6. Quit
    Enter your choice: 5
    Enter recipient user ID: user2
    Enter amount to transfer: 5000

    Transferred $5000.00 to user2 successfully!.

    Current balance: $3000.00

    --- Main Menu ---
    1. Deposit
    2. Withdraw
    3. Balance
    4. Transaction History
    5. Transfer
    6. Quit
    Enter your choice: 6
    
    Thank you for using our ATM. Goodbye!
