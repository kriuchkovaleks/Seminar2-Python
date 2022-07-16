'''
Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение второго по величине элемента в этой последовательности, 
то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
Пример:
1
7
9
0
Вывод:
7
'''

''''
def Get_second_large_number(num):
    lenght = len(num)
    first_large = num[0]
    second_large = num[1]
    if first_large < second_large:
        first_large = num[1]
        second_large = num[0]
    else:
        for i in range(lenght):
'''


def Input_array(lenght):
    user_array = [i for i in range(lenght)]
    for i in range(lenght):
        print("Input number", i+1)
        user_array[i] = int(input())
    return user_array


def Get_second_large_number(array):
    first_large = array[0]
    second_large = array[1]
    if first_large < second_large:
        first_large = array[1]
        second_large = array[0]
        
    for i in range(len(array)):
        if array[i] > first_large:
            second_large = first_large
            first_large = array[i]
        elif array[i] < first_large and array[i] > second_large:
            second_large = array[i]
    return second_large


print("Imput array lenght:")
array_length = int(input())
array = Input_array(array_length)
print(array)

result = Get_second_large_number(array)
print("Second large number:", result)
