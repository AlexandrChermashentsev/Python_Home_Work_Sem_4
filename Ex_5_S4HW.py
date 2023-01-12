# #Даны два файла, в каждом из которых находится запись многочлена. 
# # Задача - сформировать файл, содержащий сумму многочленов.

import random 
import os
os.system('clear')

def import_Formula(way: str) -> list: # Функция импорта формулы из файла и конвертация ее в список
    path = way
    data = open(path, 'r')
    for i in data:
        formula_1_str = i
        print(i)
    data.close()
    formula_1_str = formula_1_str[0:-4]
    formula = formula_1_str.split(' + ')
    return formula

def method(list) -> list: # Функция высвобождения цифр из многолчена
    final_list = []
    for i in list:
        if len(i) >= 6:
            i = i.split('*x**')
            final_list.append(i)
        elif len(i) >= 3 and i[-1] == 'x':
            i = i + '**1' 
            i = i.split('*x**')
            final_list.append(i)
        elif len(i) <= 2:
            i = i + '*x**0'
            i = i.split('*x**')
            final_list.append(i)
    return final_list

def reverse_list_in_list(pol_list_1) -> list: # Функция переворачивания списка в списке
    for i in range(len(pol_list_1)):
        if type(pol_list_1[i]) == list:
            pol_list_1[i] = pol_list_1[i][::-1]
    return pol_list_1

def formula(number: int): # Функция генерации многочлена
    elements_of_formula = [] 
    for i in range(number, -1, -1): 
        random_number = random.randint(0, 15) # Взял небольшие значения чтобы проще было перепроверять 
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
    return formula_str

def list_in_string(list_my): # функция превращения листа в строку
    string_formula = list_my[0]
    for i in range(1, len(list_my)):
        string_formula = string_formula + ' + ' + list_my[i]
    return string_formula

# Блок генерации двух формул и запись их в файлы
form = formula(random.randint(2,5))
with open('formula_5_1.txt', 'w') as data: 
    data.write(f'{form}')
form = formula(random.randint(2,5))
with open('formula_5_2.txt', 'w') as data: 
    data.write(f'{form}')

# Вытаскиваю из файла формулу и начинаю с ней работать
pol_list_1 = method(import_Formula('formula_5_1.txt'))
pol_list_2 = method(import_Formula('formula_5_2.txt'))

pol_list_1 = reverse_list_in_list(pol_list_1)
pol_list_2 = reverse_list_in_list(pol_list_2)

dict_pol_1, dict_pol_2 = dict(pol_list_1), dict(pol_list_2)

all_list = []
all_list.append(dict_pol_1), all_list.append(dict_pol_2)

# метод сложения словарей в списке с одинаковыми ключами 
result_dict = {}                                            #  результирующий словарь
for dictionary in all_list:                                 # пробегаем по списку словарей
    for key in dictionary:                                  # пробегаем по ключам словаря
        try:
            dictionary[key] = int(dictionary[key])
            result_dict[key] += dictionary[key]             # складываем значения
        except KeyError:                                    # если ключа еще нет - создаем
            result_dict[key] = dictionary[key]   
all_list = list(map(list, result_dict.items()))

all_list = reverse_list_in_list(all_list)

result_pol = []
for i in all_list:
    if i[-1] == '0':
        i[-1] = i[-1].replace('0', '')
        i[0] = str(i[0])
        result_pol.append(''.join(i))
    elif i[-1] == '1':
        i[-1] = i[-1].replace('1', '*x')
        i[0] = str(i[0])
        result_pol.append(''.join(i))
    else:
        i[0] = str(i[0])
        result_pol.append('*x**'.join(i))


result_form = list_in_string(result_pol)
print('Сумма двух полиномов:')
print(f'{result_form} = 0')

with open('FINAL_Formula.txt', 'w') as data:
    data.write(f'{result_form} = 0')