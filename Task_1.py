'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11

'''


def Get_digit_sum(num):
    lenght = len(num)
    sum = 0
    for i in range(lenght):
        if num[i] == '.':
            sum = sum + 0
        else:
            sum = sum + int(num[i])
    return sum


print("Input number")

number = input()

result = Get_digit_sum(number)

print(result)
