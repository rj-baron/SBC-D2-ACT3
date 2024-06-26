import random
accounts = {}

def account_no():
    return str(random.randint(10000, 99999))

def create(acc_num=None):
    if not acc_num:
        acc_num = account_no()
        while acc_num in accounts:
            acc_num = account_no()
    elif acc_num in accounts:
        return None, "Account number already exists. Please try again with a different number."
    
    accounts[acc_num] = {'balance': 1000}
    return acc_num, "Account created successfully."

def check(acc_num):
    return accounts.get(acc_num, {}).get('balance', "Account not found.")

def deposit(acc_num, amount):
    if acc_num in accounts and amount > 0:
        accounts[acc_num]['balance'] += amount
        return f"Deposited {amount}. New balance: {accounts[acc_num]['balance']}"
    return "Invalid account or deposit amount."

def withdraw(acc_num, amount):
    if acc_num in accounts and amount > 0:
        if accounts[acc_num]['balance'] >= amount:
            accounts[acc_num]['balance'] -= amount
            return f"Withdrew {amount}. New balance: {accounts[acc_num]['balance']}"
        return "Insufficient funds."
    return "Invalid account or withdrawal amount."

def delete(acc_num):
    if acc_num in accounts:
        del accounts[acc_num]
        return "Account deleted."
    return "Account not found."

def show():
    print("\nBank System")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")
    return input("Enter your choice: ")

def integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer!")

while True:
    choice = show()
    
    if choice == '1':
        user_id = integer_input("Enter a new account number: ")
        account_id, message = create(str(user_id) if str(user_id) not in accounts else None)
        print(f"Account created with account number: {user_id}" if account_id else message)
    
    elif choice in {'2', '3', '4', '5'}:
        account_number = integer_input("Enter account number: ")
        
        if choice == '2':
            print(f"Balance: {check(str(account_number))}")
        
        elif choice == '3':
            amount = integer_input("Enter amount to deposit: ")
            print(deposit(str(account_number), amount))
        
        elif choice == '4':
            amount = integer_input("Enter amount to withdraw: ")
            print(withdraw(str(account_number), amount))
        
        elif choice == '5':
            print(delete(str(account_number)))
    
    elif choice == '6':
        print("Exiting the system.")
        break
    
    else:
        print("Invalid choice. Please try again.")