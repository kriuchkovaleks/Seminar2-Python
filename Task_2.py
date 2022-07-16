'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
5! = 120
'''




def Get_factorial(num):
    factorial = 1
    for i in range(1, num):
        factorial = factorial*(i+1)
    return factorial

print("Input number")
number = int(input())

result = Get_factorial(number)
print(result)

## from math import factorial

## number = int(input())
## print(factorial(number))