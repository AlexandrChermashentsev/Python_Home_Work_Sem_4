# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = []
for _ in range(10):
    my_list.append(random.randint(0, 9))
print(my_list)

new_list =[]
for i in range(10):
    if i in my_list:
        new_list.append(i)

print(new_list)