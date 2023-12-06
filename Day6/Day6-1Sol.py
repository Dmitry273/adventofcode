import math

file = []
for line in open('Day6/day6mat.txt', 'r'):
    file.append(list(map(int, line.split()[1:])))

pairs = [[t, d] for t, d in zip(file[0], file[1])]
#pairs = [[44899691, 277113618901768]]

total_ways = 1
for pair in pairs:
    if pair[0] % 2 == 0:
        top = pair[0] // 2
        adj = 1
    else:
        top = (pair[0]-1) // 2
        adj = 0
    local = pair[0]/2 - math.sqrt((pair[0]/2)**2 - pair[1])
    total_ways *= 2*(top - int(local))-adj

print(total_ways)