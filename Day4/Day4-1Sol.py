total = 0

for line in open('Day4/day4mat.txt', 'r'):
    winning, ticket = line[10:].split('|')[0].split(), line[10:].split('|')[1].split()
    points = 0
    for num in winning:
        if num in ticket:
            points += 1
    score = 2**(points-1) if points else 0
    total += score

print(total)