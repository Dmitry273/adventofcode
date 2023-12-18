file = [i[:-1].split() for i in open('Day18/day18mat.txt', 'r')]

turns = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
decoder = {'0': 'R','1': 'D','2': 'L','3': 'U'}
Area = 0
Deep = 0
Peri = 0
for instruction in file:
    inst1 = int(instruction[2][2:7], base= 16)
    inst2 = decoder[instruction[2][7]]
    Area += turns[inst2][0]*Deep*int(inst1)
    Deep += turns[inst2][1]*int(inst1)
    Peri += int(inst1)
print(Area+Peri//2+1)
