from collections import defaultdict
import random
import copy

unique = set()
connections = [i[:-1] for i in open('Day25/day25mat.txt', 'r')]
for line in connections:
    for node in line.replace(':', '').split():
        unique |= set([node])

nodes = {}
for node in unique:
    nodes.update({node: set()})

for line in connections:
    head, *others = line.replace(':', '').split()
    for other in others:
        nodes[head].add(other)
        nodes[other].add(head)
mainnodes = copy.deepcopy(nodes)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def find_path(a, b):
    kill = 30 #it's a dense graph, so we can kill search much earlier
    routes_from_a = [(a,)]
    routes_from_b = [(b,)]
    while routes_from_a != [] and routes_from_b != [] and kill > 0:
        kill -= 1
        route_a = routes_from_a.pop(0)
        last_a = route_a[-1]
        route_b = routes_from_b.pop(0)
        last_b = route_b[-1]
        for step in nodes[last_a]:
            if step in route_a: continue
            if any([step in i for i in routes_from_a]): continue
            if step == b:
                return route_a+(step,)
            elif any([step in i for i in routes_from_b]):
                for i in routes_from_b:
                    if step in i:
                        return route_a+i[::-1]
            else:
                routes_from_a.append(route_a+(step,))
                
        for step in nodes[last_b]:
            if step in route_b: continue
            if any([step in i for i in routes_from_b]): continue
            if step == a:
                return (step,)+route_b[::-1]
            elif any([step in i for i in routes_from_a]):
                for i in routes_from_a:
                    if step in i:
                        return i+route_b[::-1]
            else:
                routes_from_b.append(route_b+(step,))
    return []

def measure():
    answ = 1
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for j in range(1,l):
        printProgressBar(j + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        path = find_path(unique[0],unique[j])
        if path: answ += 1
    print(f'{(l-answ)*answ} from {answ} and {(l-answ)}')
    pass

unique = list(unique)
l = len(unique)
freq = defaultdict(lambda: 0)
N = 0
M = 10000
printProgressBar(0, M, prefix = 'Stat collecting Progress:', suffix = 'Complete', length = 50)
while N < M:
    i = random.randint(0,l-1)
    j = random.randint(0,l-1)
    if i == j: continue
    N += 1
    path = find_path(unique[i],unique[j])
    printProgressBar(N, M, prefix = 'Stat collecting Progress:', suffix = 'Complete', length = 50)
    for m in range(len(path)-1):
        names = sorted([path[m],path[m-1]])
        name = f'{names[0]}/{names[1]}'
        freq[name] += 1

print('start measuring')
tops = [[a, b] for a, b in zip(freq, freq.values())]
tops.sort(key= lambda x: -x[1])

pruned = [i[0] for i in tops[0:3]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[0:6]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[0:9]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[0:12]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[1:4]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[0:2]+tops[3:5]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

pruned = [i[0] for i in tops[0:1]+tops[2:4]]
nodes = copy.deepcopy(mainnodes)
for prun in pruned:
    a = prun[0:3]
    b = prun[4:7]
    nodes[a].remove(b)
    nodes[b].remove(a)
pruned = []
measure()

# repeat until it's not 0