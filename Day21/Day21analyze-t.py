black = [3784, 33680, 93366, 182842, 302108, 451164]
print(black)
while not all([nu == black[0] for nu in black]):
    black = [black[i]-black[i-1] for i in range(1, len(black))]
    print(black)
#nope