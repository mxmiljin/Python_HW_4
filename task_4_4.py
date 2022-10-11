# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

user_num = int(input("Введите степень многочлена: "))

polynom = []
count = user_num

while count > 1:
    element = f'{random.randint(0, 100)}x^{count}'
    polynom.append(element)
    polynom.append(" + ")
    count -= 1

polynom.append(f'{random.randint(0, 100)}x + ')
polynom.append(f'{random.randint(0, 100)} = 0')

result = open("task_4_4.txt", "w")
result.write(''.join(polynom))
result.close()


