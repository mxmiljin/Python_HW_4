# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

fraction_length = int(input('Уажите желаемое количество цифр после запятой: '))

print(int(math.pi * 10 ** fraction_length) / 10 ** fraction_length)



