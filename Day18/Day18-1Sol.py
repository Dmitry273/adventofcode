file = [i[:-1].split() for i in open('Day18/day18mat.txt', 'r')]

turns = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
Area = 0
Deep = 0
Peri = 0
for instruction in file:
    Area += turns[instruction[0]][0]*Deep*int(instruction[1])
    Deep += turns[instruction[0]][1]*int(instruction[1])
    Peri += int(instruction[1])
print(Area+Peri//2+1)
