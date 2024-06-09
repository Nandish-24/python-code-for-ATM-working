from datetime import datetime

class Atm:
    def __init__(self):
        self.pin = " "
        self.balance = 0
        self.transaction_history = []  
        self.menu_atm()

    def menu_atm(self):
        while True:
            print("""Welcome to ATM. How would you like to proceed?
            1. Enter 1 to create a PIN
            2. Enter 2 to Deposit
            3. Enter 3 to Withdraw
            4. Enter 4 to Check Balance
            5. Enter 5 to View Transaction History
            6. Enter 6 to Exit""")
            choice = input("Enter the choice: ")

            if choice == '1':
                self.create_pin()
            elif choice == '2':
                self.deposit_amount()
            elif choice == '3':
                self.withdraw_atm()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.view_transaction_history()
            elif choice == '6':
                print("Goodbye. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def create_pin(self):
        self.pin = input("Enter a 4-digit PIN: ")
        print("Create PIN successful")

    def deposit_amount(self):
        temp = input("Enter your PIN: ")
        if self.pin == temp:
            amt = int(input("Enter the deposit amount: "))
            self.balance += amt
            self.transaction_history.append(f"Deposited ${amt} at {datetime.now()}")
            print("Deposit successful")
        else:
            print("Invalid PIN")

    def withdraw_atm(self):
        temp = input("Enter your PIN: ")
        if self.pin == temp:
            amt = int(input("Enter the withdrawal amount: "))
            if amt <= self.balance:
                self.balance -= amt
                self.transaction_history.append(f"Withdrew ${amt} at {datetime.now()}")
                print("Withdrawal successful")
            else:
                print("Insufficient balance for withdrawal")
        else:
            print("Invalid PIN")

    def check_balance(self):
        print(f"Your account balance is: ${self.balance}. Manage your funds wisely!")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

atm = Atm()





OUTPUT:



Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 1
Enter a 4-digit PIN: 1234
Create PIN successful

Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 2
Enter your PIN: 1234
Enter the deposit amount: 200
Deposit successful

Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 3
Enter your PIN: 1234
Enter the withdrawal amount: 50
Withdrawal successful

Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 4
Your account balance is: $150. Manage your funds wisely!

Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 5
Transaction History:
Deposited $200 at 2023-11-07 15:45:00.123456
Withdrew $50 at 2023-11-07 15:46:00.654321

Welcome to ATM. How would you like to proceed?
1. Enter 1 to create a PIN
2. Enter 2 to Deposit
3. Enter 3 to Withdraw
4. Enter 4 to Check Balance
5. Enter 5 to View Transaction History
6. Enter 6 to Exit
Enter the choice: 6
Goodbye. Thank you!
