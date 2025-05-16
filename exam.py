#current date
from datetime import datetime

def show_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print("Current Date:", current_date)
show_current_date()

# #========================================================
# #display welcome message
# User and customer data
users = {
    "admin": {"password": "admin123", "role": "Admin", "customer_id": "none"},
    "karthika": {"password": "pass123", "role": "Customer", "customer_id": "C001"}
 }

customers = {
    "C001": {"name": "Karthika Nishanth"}
}

# Authentication function
def authenticate():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        customer_id = users[username]["customer_id"]
        return username, role, customer_id
    else:
        print("Invalid login")
        return None, None, None

# # # Welcome message function
def welcome_user(username, role, customer_id):
    if customer_id == "none":  # Admin user
        print(f"Welcome, {username} ({role})")
    else:  # Customer user
        name = customers[customer_id]["name"]
        print(f"Welcome, {name} ({role})")

# # # Main program
def main():
    username, role, customer_id = authenticate()
    if username:
        welcome_user(username, role, customer_id)

# Start the program
main()
# # #====================================================================
# # #upper case
customers = {}

def create_account():
    name = input("Enter full name: ")
    # Convert name to title case
    name = name.title()

    # Validate name: only letters and spaces allowed
    if all(char.isalpha() or char.isspace() for char in name):
        # Create a new customer ID
        customer_id = f"C{len(customers) + 1:03d}"
        customers[customer_id] = {"name": name}
        print(f"Account created for {name} with ID {customer_id}")
    else:
        print("Invalid name. Use letters and spaces only.")

#Example usage
create_account()
# #========================================
# #count total customers
# Sample customers dictionary
customers = {
    "1001": {"name": "Alice", "balance": 500},
    "1002": {"name": "Bob", "balance": 300}
}

# Function definition
def count_customers(customers):
    print(f"Total Customers: {len(customers)}")

count_customers(customers)
# # #==============================================================
import random

def generate_account_number():
    # Generates a random 4-digit positive account number between 1000 and 9999
    return random.randint(1000, 9999)

def create_account(customers):
    name = input("Enter your name: ")
    balance = float(input("Enter opening balance: "))

    # Generate a valid 4-digit account number
    account_number = str(generate_account_number())

    # Save to customers dictionary
    customers[account_number] = {
        "name": name,
        "balance": balance
    }

    print(f"Account created successfully! Account Number: {account_number}")
customers={}
create_account(customers)
#==============================================
#transaction count
#Sample transactions dictionary
transactions = {
    "1001": [100, -50, 200],
    "1002": [500],
    "1003": []
}

# # Function to count transactions for a specific account
def count_transactions(account_number, transactions):
    return len(transactions.get(account_number, []))

# Simple menu
while True:
    print("\n--- Menu ---")
    print("1. Count Transactions")
    print("2. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        acc_num = input("Enter Account Number: ")
        count = count_transactions(acc_num, transactions)
        print(f"Total Transactions for Account {acc_num}: {count}")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
# # #=======================================================
#check username
def create_account(users):
    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already taken. Try another.")
        else:
            break  

    password = input("Enter a password: ")

    
    users[username] = password
    print(f"Account created successfully for user: {username}")
users = {}
create_account(users)
#=====================================
#trabnsaction summmqry
def transaction_type_summary(account_number, transactions):
    # Check if account exists and has transactions
    if account_number not in transactions or not transactions[account_number]:
        print("No transactions found for this account.")
        return

    deposits = 0
    withdrawals = 0

    # Count deposits and withdrawals
    for trans in transactions[account_number]:
        if trans['description'].startswith('Deposited'):
            deposits += 1
        elif trans['description'].startswith('Withdrew'):
            withdrawals += 1

    print(f"Deposits: {deposits}, Withdrawals: {withdrawals}")

# Example usage with menu option:
transactions = {
    "12345": [
        {"timestamp": "2025-05-01 10:00", "description": "Deposited 100"},
        {"timestamp": "2025-05-02 11:00", "description": "Withdrew 50"},
        {"timestamp": "2025-05-03 12:00", "description": "Deposited 200"},
    ]
}

while True:
    print("\nMenu:")
    print("1. Transaction Type Summary")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        acc = input("Enter account number: ")
        transaction_type_summary(acc, transactions)
    elif choice == '2':
        break
    else:
        print("Invalid option. Try again.")
#=================================================
#transaction history
def transaction_history(account_number, transactions):
    
    if account_number not in transactions or not transactions[account_number]:
        print("No transactions found for this account.")
        return

    # Get last 5 transactions using list slicing
    last_five = transactions[account_number][-5:]

    print(f"Last {len(last_five)} transactions for account {account_number}:")
    for trans in last_five:
        print(f"{trans['timestamp']} - {trans['description']}")
transaction_history(account_number, transactions)