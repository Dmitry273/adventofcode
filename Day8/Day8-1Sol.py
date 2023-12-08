file = []
for line in open('Day8/day8mat.txt', 'r'):
    file.append(line)

instructions = file[0]
nodes = file[2:]
D = {}
for node in nodes:
    D.update({node[:3]: [node[7:10], node[12:15]]})

start = 'AAA'
i = 0
t = 1
j = 0
l = len(instructions) -1
while j < 50000:
    j += 1
    turn = instructions[i % l]
    i += 1
    t = 0 if turn == 'L' else 1
    start = D[start][t]
    if start == 'ZZZ':
        print(f'Oh jeez, what was that, it took: {j} steps')
        break
print('stop')