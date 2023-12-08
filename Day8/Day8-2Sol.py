file = []
for line in open('Day8/day8mat.txt', 'r'):
    file.append(line)

instructions = file[0]
nodes = file[2:]
D = {}
for node in nodes:
    D.update({node[:3]: [node[7:10], node[12:15]]})

start = [i for i in D.keys() if i[2] == 'A']
lengths = [0 for _ in start]
s_copy = [i for i in start]

i = 0
t = 1
j = 0
l = len(instructions) - 1

while j < 200000:
    j += 1
    turn = instructions[i % l]
    i += 1
    t = 0 if turn == 'L' else 1
    for m in range(len(start)):
        start[m] = D[start[m]][t]
        if start[m][2] == 'Z':
            if lengths[m] == 0:
                lengths[m] = j
            elif j % lengths[m] != 0:
                print('OH GOD, OH NO')
print(lengths)
