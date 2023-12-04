copies = {i:1 for i in range(196)}

for j, line in enumerate(open('Day4/day4mat.txt', 'r')):
    winning, ticket = line[10:].split('|')[0].split(), line[10:].split('|')[1].split()
    points = sum([1 for num in ticket if num in winning])
    for n in range(points):
        copies[j+1+n] += copies[j]
print(sum(copies.values()))
