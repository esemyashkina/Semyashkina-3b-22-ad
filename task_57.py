import os


def find_files_with_extension(directory, extension):
    try:
        file_list = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_list.append(os.path.join(root, file))
        return file_list
    except FileNotFoundError:
        raise FileNotFoundError("Директория не найдена.")


try:
    directory = input("Введите путь к директории: ")
    extension = input("Введите расширение файлов ")
    file_list = find_files_with_extension(directory, extension)
    if file_list:
        print("Найденные файлы:")
        for file in file_list:
            print(file)
    else:
        print("Файлы с заданным расширением не найдены.")
except FileNotFoundError as e:
    print(e)