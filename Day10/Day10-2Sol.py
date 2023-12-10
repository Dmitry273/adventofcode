class route():
    def __init__(self, coor, hist, h=0, S=0):
        self.coor = coor
        self.hist = hist
        self.h = h
        self.S = S

    def advance(self, n):
        self.hist = (n + 2) % 4
        if n == 0: 
            self.coor[0] -= 1
            self.h += 1
        if n == 1: 
            self.coor[1] += 1
            self.S += self.h
        if n == 2: 
            self.coor[0] += 1
            self.h -= 1
        if n == 3: 
            self.coor[1] -= 1
            self.S -= self.h  

file = []
for n, line in enumerate(open('Day10/day10mat.txt', 'r')):
    file.append([i for i in line])
    if line.count('S'): start = [n, line.index('S')]

pipes = {'|':[0,2],'-':[1,3],'L':[0,1],'J':[0,3],'7':[2,3],'F':[1,2]}

routes = [0] #I'm lazy, don't look at me like that
r1 = route([*start], -1)

r1.advance(routes[0])
i = 1
while 1:
    i += 1
    r1n = [i for i in pipes[file[r1.coor[0]][r1.coor[1]]] if i != r1.hist][0]
    r1.advance(r1n)
    if r1.coor == start: break

print(abs(r1.S) - i//2 + 1)