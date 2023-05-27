try:
    with open('test.txt', 'r'):
        print('Файл существует')
except FileNotFoundError:
    print('Файл не найден')