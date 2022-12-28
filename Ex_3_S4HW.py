# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = [random.randint(0, 9) for i in range(10)]
print(my_list)

uniqe_list = [] # Метод поиска уникальных объектов в списке
count = 0
for i in my_list:
    count = 0
    for j in range(10):
        if i == my_list[j]:
            count += 1
    if count <= 1:
        uniqe_list.append(i)
print(uniqe_list)