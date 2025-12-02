pin = "2020"

def validpin():
    pn=input('Enter a PIN: ')
    while pn == pin:
        print('Correct PIN.')
        return True
    else:
        print('Incorrect PIN.')
        return False
def deposit(bal):
    amount=int(input('Enter amount: '))
    bal += amount
    print(f'amount deposit: {amount}\nNew balance: {bal}')

def withdraw(bal):
    amount=int(input('Enter amount: '))
    bal -= amount
    print(f'amount withdraw: {amount}\nNew balance: {bal}')

def balanceInquire(bal):
    print('Your Balance is: ',bal)

def main():
    bal=100
    if not validpin():
        return
    while True:
        print('=========Main Menu=========')
        print("[1] Deposit\n[2] Withdraw\n[3] Inquire Balance\n[4] Exit")
        print('===========================')
        option=input('enter option: ')
        if option == '1':
            bal=deposit(bal)
        elif option =='2':
            bal=withdraw(bal)
        elif option == '3':
            bal = balanceInquire(bal)
        else:
            print('Goodbye!!')
main()