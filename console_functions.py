import os
import re


def create_folder_fun():
    folder_name = input('Enter the folder name: ')
    os.mkdir(folder_name)


def delete_folder_or_file():
    file_or_folder_del = input('You want delete folder or file?:  ')
    if file_or_folder_del == 'file':
        try:
            fail_name = input('Enter the fail name(example:fail.txt): ')
            os.remove(fail_name)
            print(f'{fail_name} was successfully deleted!')
        except FileNotFoundError:
            print('That file was not found!')
    elif file_or_folder_del == 'folder':
        try:
            folder_name = input('Enter the folder name: ')
            os.rmdir(folder_name)
            print(f'{folder_name} was successfully deleted!')
        except FileNotFoundError:
            print('That folder was not found!')
    else:
        print('Incorrect input!Try again!')
        delete_folder_or_file()


def directory_content():
    os.listdir()
    print("All folders and files:", os.listdir())


def view_folders_fun():
    folders_and_files_list = os.listdir()
    only_fails_list = [x for x in folders_and_files_list if '.' in x]
    print(only_fails_list)



def view_file_fun():
    path = os.getcwd()
    for files in os.walk(path):
        print("The fails are: ", files)


def os_fun():
    pass


def about_creator():
    pass


def play_quiz():
    pass


def bank_account():
    pass


def change_directory():
    choose_new_dir = input('Enter the name of dir: ')
    os.chdir(choose_new_dir)
