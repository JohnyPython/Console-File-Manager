import os
from decorators import decorator_fun


@decorator_fun
def create_folder_fun():
    try:
        folder_name = input('Enter the folder name: ')
        return os.mkdir(folder_name)
    except FileExistsError:
        print('File already exist!')
        folder_name = input('Input another name of a folder: ')
        return os.mkdir(folder_name)


@decorator_fun
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


@decorator_fun
def directory_content():
    return "All folders and files:", os.listdir()


@decorator_fun
def view_folders_fun():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        return dirs


@decorator_fun
def view_file_fun():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        return files


@decorator_fun
def os_fun():
    print(os.name)
    print(os.environ)


@decorator_fun
def about_creator():
    print('Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
          ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '
          'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
          ' Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
          ' Excepteur sint occaecat cupidatat non proident, '
          'sunt in culpa qui officia deserunt mollit anim id est laborum.')


@decorator_fun
def change_directory():
    choose_new_dir = input('Enter the name of dir: ')
    os.chdir(choose_new_dir)
