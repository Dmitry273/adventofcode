import itertools

def valid(s, answ):
    s = str(s)
    if sum([int(i) for i in s]) != sum(answ): return False
    local = []
    for key, group in itertools.groupby(s, key= lambda x: x=='1'):
        if key: local.append(len(list(group)))
    return answ == local

file = []
D = {'.':[0],'#':[1],'?':[0,1]}
for line in open('Day12/day12mat.txt'):

    s = line.split()[0]
    nums = list(map(int, line[:-1].split()[1].split(',')))
    # s = '?'.join([line.split()[0]]*5)
    # nums = list(map(int, line[:-1].split()[1].split(',')))*5
    branches = [0]
    for ch in s:
        newbranches = []
        for i in D[ch]:
            for brach in branches:
                newbranches.append(10*brach+i) 
        branches = newbranches

    i = 0
    for brach in branches:
        if valid(brach, nums): i += 1
    file.append(i)
    print(i)
print(sum(file))