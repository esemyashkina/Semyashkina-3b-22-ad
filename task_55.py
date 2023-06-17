try:
    numbers = input("Введите список целых чисел: ")
    numbers_list = [int(num) for num in numbers.split(",")]
    min_number = min(numbers_list)
    print(f'Минимальное число:" {min_number}')
except ValueError:
    print("Введены не целые числа")