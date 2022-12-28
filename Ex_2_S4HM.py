# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = abs(int(input('Enter the number: ')))
simple_digit = 2
my_list = []

while n >= simple_digit:
    if n % simple_digit == 0:
        my_list.append(simple_digit)
        n //= simple_digit
    else:
        simple_digit += 1
print(my_list)