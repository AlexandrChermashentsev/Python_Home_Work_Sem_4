# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def formula(number: int) -> str:
    elements_of_formula = []
    for i in range(number, -1, -1):
        random_number = random.randint(0, 100)
        if i > 1 and random_number != 0:
            elements_of_formula.append(str(random_number) + 'x^'+ str(i))
        elif i == 1 and random_number != 0: 
            elements_of_formula.append(str(random_number) + 'x')
        elif i == 0 and random_number != 0:
            elements_of_formula.append(str(random_number))

    formula_str = elements_of_formula[0]
    for i in range(1, len(elements_of_formula)):
        formula_str = formula_str + ' + ' + elements_of_formula[i]
    formula_str += ' = 0'
    return formula_str

formula_str_1 = formula(int(input('Enter degree for FIRST formula: ')))
formula_str_2 = formula(int(input('Enter degree for SECOND formula: ')))

with open('formula_5_1.txt', 'a') as data:
    data.write(f'{formula_str_1}\n')
with open('formula_')

