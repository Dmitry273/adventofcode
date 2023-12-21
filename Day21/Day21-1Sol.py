import time

garden = []
for n, line in enumerate(open('Day21/day21mat.txt', 'r')):
    if 'S' in line: start = (n, line.index('S'))
    garden.append([1 if i!='#' else 0 for i in line[:-1]])

H = len(garden)
W = len(garden[0])
#R, L, U, D = np.array([0,1]), np.array([0,-1]), np.array([-1,0]), np.array([1,0])
R, L, U, D = (0,1), (0,-1), (-1,0), (1,0)

def vadd(a: tuple, b: tuple) -> tuple:
    return (a[0]+b[0], a[1]+b[1])

mem = {}
def neighbors(coor):
    # ind = (coor[0]%H, coor[1]%W)
    # loc = (H*(coor[0]//H), W*(coor[1]//W))
    # if ind not in mem: 
    #     answ = list(filter(lambda x: garden[x[0]%H][x[1]%W] != '#', [vadd(ind, R), vadd(ind, L), vadd(ind, U), vadd(ind, D)]))
    #     mem.update({ind: answ})
    # return set(map(lambda x: vadd(loc, x),mem[ind]))

    #return list(filter(lambda x: garden[x[0]%H][x[1]%W] != '#', [coor+ R, coor+ L, coor+ U, coor+ D]))
    return list(filter(lambda x: garden[x[0]%H][x[1]%W], [vadd(coor, R),vadd(coor, L),vadd(coor, U),vadd(coor, D)]))

positions = [set([]),set([start])]
wb = [0,1]
steps = 0
k = 3
m = 131*k+65
t1 = time.time()
while steps < m:
    color = steps%2
    prev = positions[color]
    steps += 1
    front = set().union(*map(neighbors, positions[not color]))
    front = front.difference(front&prev)
    wb[color] += len(front)
    positions[color] = front
t2 = time.time()
#print(front)
print(wb[color], f'{t2-t1:.2g} seconds, at {(t2-t1)/m:.2g} per step')
k = 202300
m = 131*k+65
print(3784+(29896+29896+(k-1)*29790)*k//2)
# k=0 answ= 3784, k=1 answ= 33680, k=2 answ= 93366, k=3 answ= 182842, k=4 answ= 302108, k=5 answ= 451164, 
# canvas = [['.' for i in range(131)] for j in range(131)]
# for point in front:
#     canvas[point[0]][point[1]] = '0'
#     #print(point)
# for line in canvas:
#     print(''.join(line))