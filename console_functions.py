import os
import subprocess


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
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        print("The dirs are: ", dirs)


def view_file_fun():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        print("The fails are: ", files)


def os_fun():
    print(os.name)
    print(os.environ)


def about_creator():
    print('Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
          ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
          'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
          ' Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
          ' Excepteur sint occaecat cupidatat non proident, '
          'sunt in culpa qui officia deserunt mollit anim id est laborum.')


def change_directory():
    choose_new_dir = input('Enter the name of dir: ')
    os.chdir(choose_new_dir)
