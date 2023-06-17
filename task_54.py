try:
    n = int(input("Введите целое число N: "))
    if n > 1:
        total_sum = sum(range(1, n + 1))
        print("Сумма чисел от 1 до", n, "равна", total_sum)
except ValueError:
    print("Ошибка: введено не целое число")