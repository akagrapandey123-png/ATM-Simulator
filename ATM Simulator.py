users = {
    "101": {"pin": "1234", "balance": 1000},
    "102": {"pin": "0000", "balance": 500}
}

def login(acc, pin):
    if acc in users and users[acc]["pin"] == pin:
        return True
    return False

def show_balance(acc):
    print("Your balance is:", users[acc]["balance"])

def deposit_money(acc):
    amt = float(input("Enter amount to deposit: "))
    if amt > 0:
        users[acc]["balance"] = users[acc]["balance"] + amt
        print("Done! New balance:", users[acc]["balance"])
    else:
        print("Invalid amount")

def withdraw_money(acc):
    amt = float(input("Enter amount to withdraw: "))
    if amt > users[acc]["balance"]:
        print("Not enough balance!")
    elif amt <= 0:
        print("Invalid amount")
    else:
        users[acc]["balance"] = users[acc]["balance"] - amt
        print("Please take your cash. Remaining balance:", users[acc]["balance"])

acc_input = input("Enter your account number: ")
pin_input = input("Enter your PIN: ")

if login(acc_input, pin_input):
    print("Login successful!")
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            show_balance(acc_input)
        elif choice == "2":
            deposit_money(acc_input)
        elif choice == "3":
            withdraw_money(acc_input)
        elif choice == "4":
            print("Thank you! Bye.")
            break
        else:
            print("Wrong option, try again.")
else:
    print("Wrong account number or PIN.")
