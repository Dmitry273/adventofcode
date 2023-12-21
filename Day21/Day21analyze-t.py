black = [3784, 33680, 93366, 182842, 302108, 451164]
data = [int(i[:-1]) for i in open('Day21/tryme.txt', 'r')]

j =2
print('.......................')
print(f'At the {j} stage it is:')
black = data[1000:][j::11]
k = 0
print(black)
while not all([nu == black[0] for nu in black]):
    k += 1
    black = [black[i]-black[i-1] for i in range(1, len(black))]
    print(black)
print(f'with total of {k} power')
print('.......................')
#nope