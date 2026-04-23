import time

balance=10000
correct_pin="1234"
transaction_history=[]

MAX_LIMIT=10000


def check_balance():
    print("\n💰 Current Balance : ₹",balance)


def deposit():
    global balance
    amount=float(input("Enter amount to deposit : ₹"))

    if amount<=0:
        print("❌ Invalid amount")
    elif amount> MAX_LIMIT:
        print("Limit exceeded (max ₹",MAX_LIMIT,")")
    else:
        balance=balance+amount
        transaction_history.append("Deposited ₹"+str(amount))
        print("₹",amount," deposited")


def withdraw():
    global balance
    amt=float(input("Enter amount to withdraw : ₹"))

    if amt<=0:
        print("❌ Invalid")
    elif amt>MAX_LIMIT:
        print("Max limit is ₹",MAX_LIMIT)
    elif amt>balance:
        print("❌ Not enough balance")
    else:
        balance=balance-amt
        transaction_history.append("Withdrew ₹"+str(amt))
        print("₹",amt," withdrawn")


def show_history():
    print("\nTransaction History :")
    if len(transaction_history)==0:
        print("No transactions")
    else:
        i=1
        for t in transaction_history:
            print(i,".",t)
            i+=1


def atm():

    while True:

        print("\n--- Welcome ---")
        print("1. Enter ATM")
        print("2. Exit")

        start=input("Select option : ")

        if start=="2":
            print("Exiting...")
            break

        elif start!="1":
            print("Invalid option")
            continue

        print("\n--- ATM ---")
        pin=input("Enter PIN : ")

        if pin!=correct_pin:
            print("Wrong PIN")
            continue

        print("Login done")

        while True:

            print("\n1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.History")
            print("5.Cancel")
            print("6.Exit")

            ch=input("Choice : ")

            if ch=="1":
                check_balance()

            elif ch=="2":
                deposit()

            elif ch=="3":
                withdraw()

            elif ch=="4":
                show_history()

            elif ch=="5":
                print("Cancelling...")
                time.sleep(1)
                break

            elif ch=="6":
                print("Bye")
                exit()

            else:
                print("Invalid choice")


atm()
