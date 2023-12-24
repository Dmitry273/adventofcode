import time
t0 = time.time()
park = [[j for j in i[:-1]] for i in open('Day23/day23mat.txt', 'r')]
H = len(park)
W = len(park[0])
R, L, U, D = (0,1), (0,-1), (-1,0), (1,0)
start = (0,1)
end = (H-1,W-2)
oneways = ['>','v']
nodes = {}

def inside(coor: tuple) -> bool:
    return coor[0] in range(H) and coor[1] in range(W)
def vadd(a: tuple, b: tuple) -> tuple:
    return (a[0]+b[0], a[1]+b[1])
def neighbors(coor: tuple) -> list:
    return list(filter(lambda x: inside((x[0],x[1])) and park[x[0]][x[1]] != '#', [vadd(coor, R),vadd(coor, L),vadd(coor, U),vadd(coor, D)]))
def is_node(coor: tuple) -> bool:
    return park[coor[0]][coor[1]] == '.' and list(map(lambda x: park[x[0]][x[1]], neighbors(coor))).count('.') == 0

def nodes_from_grid():
    answ = []
    for i in range(W):
        for j in range(H):
            if is_node((i,j)):
                answ.append((i,j))
    return [start]+answ+[end]
for node in nodes_from_grid():
    nodes.update({node: {}})

def connections(node: tuple):
    paths = neighbors(node)
    for path in paths:
        # uncomment to get the answer for first part
        #if vadd(path,R) == node and park[path[0]][path[1]] == '>': continue
        #if vadd(path,D) == node and park[path[0]][path[1]] == 'v': continue 
        route = [node, path]
        while 1:
            curr = route[-1]
            near = neighbors(curr)
            if curr in nodes:
                nodes[node].update({curr: len(route)-1})
                break
            for one in near:
                if one in route: near.remove(one)
            route.append(near[0])
    pass
for node in nodes:
    connections(node)

class Path():
    def __init__(self, route, distance):
        self.route = route
        self.distance = distance

paths = set([Path([start],0)])
answ = []
t1 = time.time()
while paths:
    path = paths.pop()
    history = path.route
    curr = history[-1]
    distance = path.distance
    near = nodes[curr]
    for jump in near:
        if jump in history: continue
        if jump == end:
            answ.append(distance + nodes[curr][jump])
            continue
        paths.add(Path(history+[jump], distance + nodes[curr][jump]))
t2 = time.time()
print(f'and the top one is {max(answ)}. Main part in {(t2-t1):.2g} sec. Warmup {(t1-t0):.2g} sec')
