def fib(num):
    first = 1
    second = 1
    print(first)
    print(second)
    for i in range(num-2):
        print(first + second)
        first, second = second, first + second


number = int(input())
fib(number)