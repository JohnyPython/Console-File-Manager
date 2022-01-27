import os


def dirs_names_fun():
    result_dir = []
    for item in os.listdir():
        if os.path.isdir(item):
            result_dir.append(item)
    x = ', '.join(result_dir)
    with open('dis.txt', 'w') as f:
        f.write(f'Dirs: {x}\n')


def file_name_fun():
    result_fails = []
    for item in os.listdir():
        if os.path.isfile(item):
            result_fails.append(item)
    x_files = ', '.join(result_fails)
    with open('dis.txt', 'a') as f:
        f.write(f'Files: {x_files}\n')


dirs_names_fun()
file_name_fun()
