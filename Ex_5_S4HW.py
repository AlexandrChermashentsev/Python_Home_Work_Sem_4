# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
 
import random 
import os 
os.system('clear') 

def formula(number: int) -> str: 
    elements_of_formula = [] 
    for i in range(number, -1, -1): 
        random_number = random.randint(0, 15) 
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
    return formula_str, elements_of_formula
 
formula_str_1, el_of_form_1 = formula(6) #int(input('Enter degree for FIRST formula: '))) 
formula_str_2, el_of_form_2 = formula(4) #int(input('Enter degree for SECOND formula: ')))
 
with open('formula_5_1.txt', 'w') as data: 
    data.write(f'{formula_str_1}') 
with open('formula_5_2.txt', 'w') as data: 
    data.write(f'{formula_str_2}') 
 
formula_str_1 = formula_str_1.replace(' = 0', '') 
formula_str_2 = formula_str_2.replace(' = 0', '') 
 
with open('formula_5_3.txt', 'w') as data: 
    data.write(f'({formula_str_1}) + ({formula_str_2}) = 0') 
 
print(el_of_form_1, el_of_form_2) 


if len(el_of_form_1) >= len(el_of_form_2):
    len_el = (len(el_of_form_1) - 1)
else:
    len_el = (len(el_of_form_2) - 1)
print(len_el)


# first_str = ['4x^5', '10x^4', '10x^3', '14x^2', '11x', '18']
# second = ['10x^5', '12x^3', '6x^2', '3x', '3']
all_str = []
for i in el_of_form_1:
    for j in el_of_form_2:
        if i[-1] == 'x' and j[-1] =='x':
            all_str.append(f'({i} + {j})')
        elif i[-1] == str(len_el) and j[-1] == str(len_el) and\
len(i) >= 4 and len(j) >= 4:
            all_str.append(f'({i} + {j})')
        elif not 'x' in i and not 'x' in j:
            all_str.append(f'({i} + {j})')
    len_el -= 1
print(all_str)

