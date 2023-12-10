class route():
    def __init__(self, coor, hist):
        self.coor = coor
        self.hist = hist

    def advance(self, n):
        self.hist = (n + 2) % 4
        if n == 0: 
            self.coor[0] -= 1
        if n == 1: 
            self.coor[1] += 1
        if n == 2: 
            self.coor[0] += 1
        if n == 3: 
            self.coor[1] -= 1  

file = []
for n, line in enumerate(open('Day10/day10mat.txt', 'r')):
    file.append([i for i in line])
    if line.count('S'): start = [n, line.index('S')]

pipes = {'|':[0,2],'-':[1,3],'L':[0,1],'J':[0,3],'7':[2,3],'F':[1,2]}

routes = [0,3] #I'm lazy, don't look at me like that
r1 = route([*start], -1)
r2 = route([*start], -1)

r1.advance(routes[0])
r2.advance(routes[1])
i = 1
while 1:
    i += 1
    r1n = [i for i in pipes[file[r1.coor[0]][r1.coor[1]]] if i != r1.hist][0]
    r1.advance(r1n)
    if r1.coor == r2.coor: break
    r2n = [i for i in pipes[file[r2.coor[0]][r2.coor[1]]] if i != r2.hist][0]
    r2.advance(r2n)
    if r1.coor == r2.coor: break

print(i)