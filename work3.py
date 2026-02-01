# Simple Banking Application

balance = 0

# Function to deposit amount
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid deposit amount.")

# Function to withdraw amount
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid withdrawal amount.")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")

# Function to check balance
def check_balance():
    print("Current Balance:", balance)

# Main menu
while True:
    print("\n--- Banking Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thank you for using the banking application.")
        break
    else:
        print("Invalid choice. Try again.")