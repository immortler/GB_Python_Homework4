"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем
пользователь вводит сами элементы множеств.
"""

len_of_first_list = int(input('Enter length of first set of integer numbers: '))
first_list = [0] * len_of_first_list
len_of_second_list = int(input('Enter length of second set of integer numbers: '))
second_list = [0] * len_of_first_list
for i in range(len_of_first_list):
    first_list[i] = int(input(f'Enter {i+1} element of first set: '))
first_set = set(first_list)
for i in range(len_of_second_list):
    second_list[i] = int(input(f'Enter {i+1} element of second set: '))
second_set = set(second_list)
result_set = first_set.intersection(second_set)
print(f'Result sorted set: {sorted(result_set)}.')
