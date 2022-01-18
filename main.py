from console_functions import create_folder_fun, change_directory, delete_folder_or_file, directory_content
from console_functions import view_folders_fun, view_file_fun
from personal_acc import bank_account
from quiz import play_quiz


def return_to_main_menu():
    to_main_menu = input('Return the main menu? (yes/no) :')
    if to_main_menu == 'yes':
        console_menu_points()
    elif to_main_menu == 'no':
        print('Good luck!!!!')
    else:
        print('Incorrect input! Try again!')


def console_menu_points():
    print('***********')
    print('1  *Create (folder/file)*')
    print('2  *Delete(folder/file)*')
    print('3  *View content of the directory*')
    print('4  *View folders*')
    print('5  *View only files*')
    print('6  *About OS*')
    print('7  *About creator*')
    print('8  *Play quiz*')
    print('9  *Bank account*')
    print('10 *Change directory*')
    print('11 *Exit*\n***********')

    console_fail_manager()


def console_fail_manager():
    while True:
        choose = input('Enter the menu number: ')
        if choose == '1':
            create_folder_fun()
            return_to_main_menu()
            break
        elif choose == '2':
            delete_folder_or_file()
            return_to_main_menu()
            break
        elif choose == '3':
            directory_content()
            return_to_main_menu()
            break
        elif choose == '4':
            view_folders_fun()
            return_to_main_menu()
            break
        elif choose == '5':
            view_file_fun()
            return_to_main_menu()
            break
        elif choose == '6':
            os_fun()
            return_to_main_menu()
            break
        elif choose == '7':
            about_creator()
            return_to_main_menu()
            break
        elif choose == '8':
            play_quiz()
            return_to_main_menu()
            break
        elif choose == '9':
            bank_account()
            return_to_main_menu()
            break
        elif choose == '10':
            change_directory()
            return_to_main_menu()
            break
        elif choose == '11':
            print('Good luck!!!!')
            break
        else:
            print('Not correct input!\nTry again!')


console_menu_points()



