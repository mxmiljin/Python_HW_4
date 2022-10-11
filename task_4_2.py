# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list_length = random.randint(10, 20)            # Строки 5-11 - создание исходного списка генератором псевдослучайных чисел 
my_list = []
count = 0

while count < list_length:
    my_list.append(random.randint(1, 10))
    count += 1

print(f'Исходный список: {my_list}.')           # Создание нового списка из уникальных элементов исходного списка

result_list = []
for item in my_list:
    if item not in result_list:
        result_list.append(item)

print(f'Список неповторяющихся элементов: {result_list}.')
