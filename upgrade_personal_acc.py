import os

FILE = 'saving_bill.txt'
HISTORY = 'history_of_purchases.txt'
wallet = []
history_of_purchases = {}

# начало программы - проверяем есть ли файлы


def start_fun():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            f.read()
        with open(HISTORY, 'r') as f:
            f.read()
        menu_points()
    else:
        with open(FILE, 'w') as f:
            f.write('Balance : 0 btc\n')
        with open(HISTORY, 'w') as f:
            f.write('HISTORY OF PURCHASES:\n')
        menu_points()

# цикл с основными командами


def manager_menu_fun():
    while True:
        choice = input('Choose menu section: ')
# пополнение счета и запись в файл
        if choice == '1':
            add_money = float(input(f'Enter the deposit amount: '))
            wallet.append(add_money)
            balance_wallet = str(sum(wallet))
            with open('saving_bill.txt', 'a') as fail:
                fail.write(f"Replenishment: {add_money} btc --> balance : {balance_wallet} btc\n {11*'*'}\n")
            manager_menu_fun()
            break
        elif choice == '2':
            add = float(input(f'Enter the price of your purchase: '))
            if add > sum(wallet):
                print('There is not enough money in your account! Deposit money!')
                manager_menu_fun()
            else:
                purchase = input(f'Enter the name of the purchase: ')
                wallet.append(add * -1)
                balance = str(sum(wallet))
                with open(FILE, 'a') as fail:
                    fail.write(f'Transaction: {add} --> balance: {balance}\n')
                with open(HISTORY, 'a') as f:
                    f.write(f'purchase: {purchase} --> price: {add} btc\n')
                history_of_purchases[purchase] = add
                manager_menu_fun()
            break
        elif choice == '3':
            with open(HISTORY, 'r') as f:
                f.read()
            break
        elif choice == '4':
            with open(FILE, 'r') as fail:
                fail.read()
            menu_points()
            break
        elif choice == '5':
            print('See you later!')
            break
        else:
            print('Incorrect input, try again!')


def menu_points():
    print('************')
    print('1 - *Replenishment*')
    print('2 - *Purchase*')
    print('3 - *History of purchases*')
    print('4 - *Balance*')
    print('5 - *Exit*\n***********')
    manager_menu_fun()


start_fun()
