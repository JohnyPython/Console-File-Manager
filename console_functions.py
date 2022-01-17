

def console_menu_points():
    print('***********')
    print('1  *Create folder*')
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
            break
        elif choose == '2':
            delete_folder_or_file()
            break
        elif choose == '3':
            directory_content()
            break
        elif choose == '4':
            view_folders_fun()
            break
        elif choose == '5':
            view_file_fun()
            break
        elif choose == '6':
            os_fun()
            break
        elif choose == '7':
            about_creator()
            break
        elif choose == '8':
            play_quiz()
            break
        elif choose == '9':
            bank_account()
            break
        elif choose == '10':
            change_directory()
            break
        elif choose == '11':
            print('Good luck!!!!')
            break
        else:
            print('Not correct input!\nTry again!')




console_menu_points()


def create_folder_fun():
    pass


def delete_folder_or_file():
    pass


def directory_content():
    pass


def view_folders_fun():
    pass


def view_file_fun():
    pass


def os_fun():
    pass


def about_creator():
    pass


def play_quiz():
    pass


def bank_account():
    pass


def change_directory():
    pass

