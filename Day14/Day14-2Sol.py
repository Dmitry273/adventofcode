import numpy as np

file = []
for line in open('Day14/day14mat.txt', 'r'):
    file.append([i for i in line[:-1]])

plane = np.array(file)
W = len(plane[0])
H = len(plane)

class Rock():
    plane = plane
    W = len(plane[0])
    H = len(plane)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rollN(self, plane = plane):
        obst = np.where(plane[:self.y, self.x] == '#')[0]
        ahead = len(np.where(plane[obst[-1]:self.y, self.x] == 'O')[0]) if len(obst) else len(np.where(plane[:self.y, self.x] == 'O')[0])
        if len(obst) == 0: self.y = 0 + ahead
        else: self.y = (obst[-1]+1) + ahead

    def rollW(self, plane = plane):
        obst = np.where(plane[self.y, :self.x] == '#')[0]
        ahead = len(np.where(plane[self.y, obst[-1]:self.x] == 'O')[0]) if len(obst) else len(np.where(plane[self.y, :self.x] == 'O')[0])
        if len(obst) == 0: self.x = 0 + ahead
        else: self.x = (obst[-1]+1) + ahead

    def rollS(self, plane = plane, H=H):
        obst = np.where(plane[self.y:, self.x] == '#')[0]
        ahead = len(np.where(plane[self.y+1:self.y+obst[0], self.x] == 'O')[0]) if len(obst) else len(np.where(plane[self.y+1:, self.x] == 'O')[0])
        if len(obst) == 0: self.y = (H-1) - ahead
        else: self.y += (obst[0]-1) - ahead

    def rollE(self, plane = plane, W=W):
        obst = np.where(plane[self.y, self.x:] == '#')[0]
        ahead = len(np.where(plane[self.y, self.x+1:self.x+obst[0]] == 'O')[0]) if len(obst) else len(np.where(plane[self.y, self.x+1:] == 'O')[0])
        if len(obst) == 0: self.x = (W-1) - ahead
        else: self.x += (obst[0]-1) - ahead

rockspos = np.where(plane=='O')
rocks = []
for y, x in zip(rockspos[0], rockspos[1]):
    rocks.append(Rock(x, y))

Seen = {''.join(plane.flatten(order='C')) : 0}
num = 0
while num<1000:
    num += 1
    for rock in rocks:
        rock.rollN()
    plane[plane == 'O'] = '.'
    for rock in rocks:
        plane[rock.y][rock.x] = 'O'
    
    for rock in rocks:
        rock.rollW()
    plane[plane == 'O'] = '.'
    for rock in rocks:
        plane[rock.y][rock.x] = 'O'

    for rock in rocks:
        rock.rollS()
    plane[plane == 'O'] = '.'
    for rock in rocks:
        plane[rock.y][rock.x] = 'O'

    for rock in rocks:
        rock.rollE()
    plane[plane == 'O'] = '.'
    for rock in rocks:
        plane[rock.y][rock.x] = 'O'
    res = ''.join(plane.flatten(order='C'))
    if res in Seen.keys(): break
    else: Seen.update({res : num})

print(Seen[res], num)
final = Seen[res] + (1000000000-Seen[res]) % (num-Seen[res])
for key, value in zip(Seen.keys(), Seen.values()):
    if value == final:
        dish = np.array([i for i in key]).reshape(W,W)
print(dish)
load = 0
for i in range(W):
    load += (W-i)*list(dish[i]).count('O')
print(load)
