import os

accounts=[]
#admin login 
def Admin_login():
    while True:
        Admin_username = "admin"
        Admin_userpassword = 12345
        print("====Admin Login====")
        try:
            ad_username=input("Enter Admin User Name Is: ")
            ad_userpassword=int(input("Enter Admin Password: "))
            if Admin_username==ad_username and Admin_userpassword==ad_userpassword:
                print("Login Successfully!\n")
                print("🙏Welcome to MK Bank🙏")
                return True
            else:
                print("🚫Invalid login🚫.Try Again.")
                return False
        except ValueError:
            print("Enter password is only numbers.")

#=====================================================================================


#get customers informations

def get_customer_info():
    cus_username=input("Enter the username is: ")
    cus_password=input("Enter the password is: ")
    customer_name=input("Enter the name is: ")
    date_of_birth=input("Enter the date of birth is: ")
    address=input("Enter the address is: ")
    phonenumber=input("Enter the phonenumber is: ")
    email=input("Enter the e-mail is: ")
    return[cus_username,cus_password,customer_name,date_of_birth,address,phonenumber,email]
#===============================================================================================================

#create customers id
def create_next_customer_id():
    if not os.path.exists("customers.txt"):
        return "C001"
    else:
        with open("customers.txt","r")as read_file:
            lines=read_file.readlines()
            last_line=lines[-1].strip()
            if not last_line:
                return "C001"
            last_id=last_line.split(',')[0]
            next_id_num=int(last_id[1:])+1
            return f"C{next_id_num:03d}"
#-------------------------------------------------------------------------------------------     
#create users id
def create_next_user_id():
    if not os.path.exists("users.txt"):
        return "U001"
    else:
        with open("users.txt","r")as reads_file:
            lines = reads_file.readlines()
            last_line = lines[-1].strip()
            if not last_line:
                return "U001"
            last_id = last_line.split(',')[0]  
            next_id_num = int(last_id[1:]) + 1  
            return f"U{next_id_num:03d}"
#--------------------------------------------------------------------------------------------------
#create customers
def create_customers():
    next_id1 = create_next_customer_id()
    next_id2 = create_next_user_id()
    customers = get_customer_info()
    with open("customers.txt","a")as customers_file,open("users.txt","a")as users_file:
        customers_file.write(f"{next_id1}-{customers[2]}-{customers[3]}-{customers[4]}-{customers[5]}-{customers[6]}\n") 
        users_file.write(f"{next_id2}-{customers[0]}-{customers[2]}\n")

#================================================================================================================================

#create next account id
def create_next_account_id():
    if not accounts:
        return "A001"
    else:
        last_id = accounts[-1]['account_id']
        next_id = int(last_id[1:]) + 1
        return f"A{next_id:03d}"
#-----------------------------------------------------------------------------------------------------------------------------------
#create account


def create_account():
    print("==create account==")
    customer_id=input("Enter the customer ID: ")
    account_type=input("Enter account type(Savings/Current):")
    if account_type not in ["Savings","Current"]:
        print("Invalid account type")
        return
    try:
        opening_balance=float(input("Enter opening balance:"))
        account_id=create_next_account_id()

        new_account = {
            "account_id": account_id,
            "customer_id": customer_id,
            "account_type": account_type,
            "opening_balance": opening_balance,
            "status": "Active"
            
        }
        accounts.append(new_account)
        print(f'Account{account_id}created successfully!')
    except ValueError:
        print("Opening balance must be a valid number.")

#===============================================================================
#create view all accounts
def view_all_accounts():
    print("\n==== All Account Details ====")
    if not accounts:
        print("No account records found.")
        return

    for account in accounts:
        print(f"Account ID     : {account['account_id']}")
        print(f"Customer ID    : {account['customer_id']}")
        print(f"Account Type   : {account['account_type']}")
        print(f"Balance        : {account['opening_balance']}")
        print(f"Status         : {account['status']}")
        print("-" * 30)
#===========================================================================================================================
#deposit money
def deposit_money():
    account_id=input("Enter the account id:")
    for account in accounts:
        if account['account_id'] == account_id:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be zero.")
                    return
                account['opening_balance'] += amount
                print(f" Deposited {amount} successfully. New Balance: {account['opening_balance']}")
                return
            except ValueError:
                print("Amount must be a number.")
                return
    print("Account ID not found.")
#================================================================================================================
#withdrawal money
def withdraw_money():
    account_id = input("Enter the Account ID to withdraw from: ")
    for account in accounts:
        if account['account_id'] == account_id:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 100:
                    print("Amount must be hundred.")
                    return
                if amount > account['opening_balance']:
                    print("Insufficient balance.")
                    return
                account['opening_balance'] -= amount
                print(f"Withdrawn {amount} successfully. New Balance: {account['opening_balance']}")
                return
            except ValueError:
                print("Amount must be a number.")
                return
    print("Account ID not found.")
#=================================================================================================================
#check balance
def check_balance():
    account_id = input("Enter the Account ID : ")
    for account in accounts:
        if account['account_id'] == account_id:
            print(f"The current balance for Account {account_id} is: {account['opening_balance']}")
            return
    print("Account ID not found.")
#====================================================================================================================
#Transaction
def view_transaction_history():
    account_id = input("Enter the Account ID to view transactions: ")
    for account in accounts:
        if account['account_id'] == account_id:
            print(f"\n📜 Transaction History for Account {account_id}:")
            tns_list = account.get("transactions", [])
            if not tns_list:
                print("No transactions found.")
            else:
                for tns in tns_list:
                    print(f"- {tns}")
            return
    print("Account ID not found.")



#Admin Menu
def Admin_menu():
    while True:
        print("Admin Menu")
        print("1. Create Customer") 
        print("2. Create Account") 
        print("3. View All Accounts Details") 
        print("4. Deposit Money") 
        print("5. Withdraw Money") 
        print("6. Check Balance") 
        print("7. View Transaction History") 
        
        # print("8. Delete Account") 
        # print("9. Update Account Details") 
        print("10. Exit") 
        choice = input("Enter the choice(1-10): ")
        if choice=="1":
           create_customers()
        elif choice=="2":
            create_account()
        elif choice=="3":
            view_all_accounts()   
        elif choice=="4":
            deposit_money()
        elif choice=="5":
            withdraw_money()
        elif choice=="6":
            check_balance()
        elif choice=="7":
            view_transaction_history()
        
        # elif choice==8:
        #     print(delete_account)
        # elif choice==9:
        #     print(update_account_details)
        elif choice=="10":
            print("\n Thank you for choosing the MK bank.👋bye👋")
            break
        # else:
        #     print("Invalid Please Try Again")
if __name__ == "__main__":
    if Admin_login():
        Admin_menu()























