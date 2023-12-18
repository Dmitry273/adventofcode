from collections import defaultdict
from queue import PriorityQueue

factory = [[int(i) for i in j[:-1]] for j in open('Day17/day17mat.txt', 'r')]
H = len(factory)
W = len(factory[0])

start = (0,0)
end = (H-1,W-1)

def inside(coor: tuple) -> bool:
    return coor[0] in range(H) and coor[1] in range(W)

R, L, U, D = (0,1), (0,-1), (-1,0), (1,0)
turns = {R:[U,D], L:[U,D], U:[R,L], D:[R,L]}    

open = PriorityQueue()
open.put((0,start,R))
open.put((0,start,D))

distances = defaultdict(lambda: defaultdict(lambda: float('inf')))
distances[start][R] = 0
distances[start][L] = 0
distances[start][D] = 0
distances[start][U] = 0

while not open.empty():
    heat, curr, dire = open.get()
    if heat > distances[curr][dire]: continue

    x, y = curr
    for _ in range(10):
        x, y = x + dire[0], y + dire[1]
        if not inside((x,y)): break

        heat += factory[x][y]
        if _ < 3: continue

        for new_dire in turns[dire]:
            if heat >= distances[(x,y)][new_dire]: continue
            distances[(x,y)][new_dire] = heat
            open.put((heat, (x,y), new_dire))

print(min(distances[end].values()))
