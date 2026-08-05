#  Python Banking Program
from unittest import case


def show_balance(balance):
    print("*********************************")
    print(f"Your balance is $ {balance:.2f}💰")
    print("*********************************")

def deposit():
    print("*********************************")
    amount = float(input("Enter amount to be deposited :💸 "))
    print("*********************************")
    if amount <= 0:
        print("*********************************")
        print("That's not a valid amount🤦🤦🤦")
        print("*********************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn🏧 : "))
    if amount > balance:
        print("Insufficient funds!🥲")
        return 0
    elif amount <= 0:
        print("Amount must be greater than zero ")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************************")
        print("  Welcome to the Bank of Baroda!🏦  ")
        print("**********************************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************************")

        choice = int(input("Enter your choice (1-4) : "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("*********************************")
            print("Enter a valid choice💩")
            print("*********************************")
    print("**********************************")
    print("Thank you for using Bank of Baroda! Have a nice day!🏦")
    print("***********************************")

if __name__ == "__main__":
    main()








