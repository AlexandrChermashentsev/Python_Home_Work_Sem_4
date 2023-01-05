import os 
os.system('clear') 

first_str = ['4x^5', '10x^4', '10x^3', '14x^2', '11x', '18']
second = ['10x^5', '12x^3', '6x^2', '3x', '3']
all_str = []
degree = 5
for i in first_str:
    for j in second:
        if i[-1] == 'x' and j[-1] =='x':
            all_str.append(f'({i} + {j})')
        elif i[-1] == str(degree) and j[-1] == str(degree) and len(i) >= 4 and len(j) >= 4:
            all_str.append(f'({i} + {j})')
        elif not 'x' in i and not 'x' in j:
            all_str.append(f'({i} + {j})')
    degree -= 1
print(all_str)


