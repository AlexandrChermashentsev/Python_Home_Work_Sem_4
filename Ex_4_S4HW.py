# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: 
# k=2 => 
# 2*x² + 4*x + 5 = 0     A=2 B=4 C=5
# x² + 5 = 0             A=1 B=0 C=5
# 10*x² = 0              A=10 B=0 C=0
# k=5 -> x^5 + x^4 + x^3 + x^2 + x^1 + x^0 = 0
#        a      b    c      e     f
# randint(0,100)

import random

user_degree = int(input('Enter degree: '))
elements_of_formula = []
for i in range(user_degree, -1, -1):
    random_number = random.randint(0, 100)
    if i > 1 and random_number != 0:
        elements_of_formula.append(str(random_number) + '*x**'+ str(i))
    elif i == 1 and random_number != 0: 
        elements_of_formula.append(str(random_number) + '*x')
    elif i == 0 and random_number != 0:
        elements_of_formula.append(str(random_number))

formula_str = elements_of_formula[0]
for i in range(1, len(elements_of_formula)):
    formula_str = formula_str + ' + ' + elements_of_formula[i]
formula_str += ' = 0'

print(elements_of_formula)
print(formula_str)

with open('formula.txt', 'a') as data:
    data.write(f'{formula_str}\n')