import numpy as np

file = []
for line in open('Day14/day14mat.txt', 'r'):
    file.append([i for i in line[:-1]])

dish = np.rot90(np.array(file), k= -1)

l = len(dish[0])
load = 0
for line in dish:
    n = 0
    for i in range(l):
        if line[i] == '#':
            load += ((i + (i - (n-1)))*n)//2
            n = 0
        elif line[i] == 'O':
            n += 1
    else:
        i = l
        load += ((i + (i - (n-1)))*n)//2
print(load)