import numpy as np

ex = 999999 #ex = 1 for 1 part, 999999 for 2 part
file = []
for i, line in enumerate(open('Day11/day11mat.txt', 'r')):
    file.append([x for x in line][:-1])

universe = np.array(file)
empty_x = np.where(np.all(universe == '.', axis=1))
universe = np.rot90(universe, -1)
empty_y = np.where(np.all(universe == '.', axis=1))
universe = np.rot90(universe, 1)

ii = np.where(universe == '#')
total = 0
for i in range(len(ii[0])):
    for j in range(i+1, len(ii[1])):
        total += abs(ii[0][i]-ii[0][j])+abs(ii[1][i]-ii[1][j])
        iii = sorted([ii[0][i],ii[0][j]])
        jjj = sorted([ii[1][i],ii[1][j]])
        total += ex*(len([m for m in empty_x[0] if m in range(iii[0],iii[1])]))
        total += ex*(len([m for m in empty_y[0] if m in range(jjj[0],jjj[1])]))

print(total)