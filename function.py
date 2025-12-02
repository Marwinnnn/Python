print('Function ATM Manchine\n')
pn="1234"
def validPinn():
    pin=input('Enter you PIN: ')
    while pin == pn:
        print("PIN Validation Successfull.")
        return True
    else:
        print("Invalid PIN")
        return False

def menuop():
    print('=========Main Menu=========')
    print("[1] Deposit\n[2] Withdraw\n[3] Inquire Balance\n[4] Exit")
    print('===========================')

def deposit(bal):
    amount=float(input('Enter amount: '))
    bal+=amount
    print(f'Deposit Amount: {amount}\nNew Balance: {bal}\nTransaction Successfull')
    return bal

def withdraw(bal):
    amount=float(input('Enter ammount: '))
    if amount < bal:
        bal -= amount
        print(f'Withdraw Amount: {amount}\nNew Balance: {bal}\nTransaction Successfull')
        return bal
    else:
        print("Insufficient Ammount!!")

def inquiry(bal):
    print(f'Your balance is {bal}\nTransaction Successfull234')

def base():
    bal = 0
    if not validPinn():
        return
    while True:
        menuop()
        choice = input("Enter your option: ")

        if choice == "1":
            bal = deposit(bal)
        elif choice == "2":
            bal = withdraw(bal)
        elif choice == "3":
            bal = inquiry(bal)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
base()




