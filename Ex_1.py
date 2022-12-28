# 1. Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

import math

d = input('Введите точность для константы: точность должна быть ровна от 10^(-1) до 10^(-10) -> ')
flag = False
for i in range(-10, 0):
    if float(d) == 10 ** (i):
        flag = True

count = 0
if flag == True:
    for i in range(2, len(d)):
        count += 1
    print(round(math.pi, count))
else:
    print('Введенная точность неверна')