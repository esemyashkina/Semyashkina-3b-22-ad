num1 = input()
num2 = input()
try:
    print(float(num1) / float(num2))
except Exception:
    print('Ошибка')