import numpy as np
import time

class Brick():
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx+1
        self.dy = dy+1
        self.dz = dz+1

bricks = []
for line in open('Day22/day22mat.txt', 'r'):
    info = map(int, line[:-1].replace('~',',').split(','))
    bricks.append(Brick(*info))

X = [min(map(lambda b: b.x, bricks)),max(map(lambda b: b.dx, bricks))]
Y = [min(map(lambda b: b.y, bricks)),max(map(lambda b: b.dy, bricks))]
Z = [min(map(lambda b: b.z, bricks)),max(map(lambda b: b.dz, bricks))]

Space = [[[0 if z!=0 else 1 for x in range(*X)] for y in range(*Y)] for z in range(Z[1])] #Space[z][y][x]
Space = np.array(Space)

Grounded = []

while bricks:
    lowest = min(bricks, key= lambda b: b.z)
    bricks.remove(lowest)
    while (Space[lowest.z:lowest.dz,lowest.y:lowest.dy,lowest.x:lowest.dx] == 1).sum() == 0:
        lowest.z -= 1
        lowest.dz -= 1
    lowest.z += 1
    lowest.dz += 1
    Grounded.append(lowest)
    Space[lowest.z:lowest.dz,lowest.y:lowest.dy,lowest.x:lowest.dx] = 1

Supports = {}
for target in Grounded:
    depend = []
    for brick in Grounded:
        if brick.z != target.dz: continue
        for x in range(target.x, target.dx):
            for y in range(target.y, target.dy):
                if x in range(brick.x, brick.dx) and y in range(brick.y, brick.dy):
                    depend.append(brick)
                    break
            else:
                continue
            break

    if target.z == 1:
        Supports.update({target: {'standson': ['ground'], 'holds': depend}})
    else:
        support = []
        for brick in Grounded:
            if brick.dz != target.z: continue
            for x in range(brick.x, brick.dx):
                for y in range(brick.y, brick.dy):
                    if x in range(target.x, target.dx) and y in range(target.y, target.dy):
                        support.append(brick)
                        break
                else:
                    continue
                break
        Supports.update({target: {'standson': support, 'holds': depend}})

answ = 0
i = 0
t1 = time.time()
for brick in Supports:
    i += 1
    total = set()
    chain = set([brick])
    collapsed = set([brick])
    while chain:
        next = chain.pop()
        for depend in Supports[next]['holds']:
            if len(set(Supports[depend]['standson'])-collapsed) == 0:
                collapsed.add(depend)
                chain.add(depend)
                total.add(depend)
    l = len(total)
    #print(f'got a total of {l} collapses at {i} brick')
    answ += len(total)
t2 = time.time()
print(f'And the final answer is {answ}, took {t2-t1:.2g} seconds')