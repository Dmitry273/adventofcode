import copy

file = [[j for j in i[:-1]] for i in open('Day16/day16mat.txt', 'r')]
H, W = len(file), len(file[0])

def hor(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 0
        case 3:
            return -1
    return 'opa'

def ver(n):
    match n:
        case 0:
            return -1
        case 1:
            return 0
        case 2:
            return 1
        case 3:
            return 0
    return 'mda'

def insideBoundary(H, W, cell):
    return True if 0 <= cell[0] <= H-1 and 0 <= cell[1] <= W-1 else False

def rlmirr(n):
    match n:
        case 0:
            return 1
        case 1:
            return 0
        case 2:
            return 3
        case 3:
            return 2
    return 'oh'

def lrmirr(n):
    match n:
        case 0:
            return 3
        case 1:
            return 2
        case 2:
            return 1
        case 3:
            return 0
    return 'oh'
     
class Beam():
    def __init__(self, direction, history):
        self.direction = direction
        self.history = history
    
def energy(start, direction):
    beams = [Beam(direction,[(start[0]-ver(direction),start[1]-hor(direction),direction)])]
    fullbeams = []
    collective = set()
    while beams:
        newbeams = []
        for beam in beams:
            collective = collective | set(beam.history)
        for beam in beams:
            oldcell = beam.history[-1][0:2]
            n = beam.direction
            newcell = (oldcell[0]+ver(n),oldcell[1]+hor(n), n)
            if not insideBoundary(H, W, newcell) or newcell in beam.history:
                fullbeams.append(copy.deepcopy(beam))
                continue
            if newcell in collective:
                fullbeams.append(copy.deepcopy(beam))
                continue
            beam.history.append(newcell)
            env = file[newcell[0]][newcell[1]]
            match env:
                case '.':
                    newbeams.append(copy.deepcopy(beam))
                case '-':
                    if hor(n):
                        newbeams.append(copy.deepcopy(beam))
                    else:
                        beam.direction = 1
                        newbeams.append(copy.deepcopy(beam))
                        beam.direction = 3
                        newbeams.append(copy.deepcopy(beam))
                case '|':
                    if ver(n):
                        newbeams.append(copy.deepcopy(beam))
                    else:
                        beam.direction = 0
                        newbeams.append(copy.deepcopy(beam))
                        beam.direction = 2
                        newbeams.append(copy.deepcopy(beam))
                case '/':
                    beam.direction = rlmirr(beam.direction)
                    newbeams.append(copy.deepcopy(beam))
                case '\\':
                    beam.direction = lrmirr(beam.direction)
                    newbeams.append(copy.deepcopy(beam))
        beams = [copy.deepcopy(i) for i in newbeams]

    energized = set()
    for beam in fullbeams:
        energized = energized | set(map(lambda x: (x[0], x[1]), beam.history))
    return len(energized)-1

print(f'default energy is {energy([0,0],1)}')

top = 0
for i in range(H):
    E = energy([i,0],1)
    print(f'{E} with {i} and 0 as start and 1 as direction')
    top = max(E, top)
for i in range(W):
    E = energy([0,i],2)
    print(f'{E} with 0 and {i} as start and 2 as direction')
    top = max(E, top)
for i in range(H):
    E = energy([i,W-1],3)
    print(f'{E} with {i} and {W-1} as start and 3 as direction')
    top = max(E, top)
for i in range(W):
    E = energy([H-1,i],0)
    print(f'{E} with {H-1} and {i} as start and 0 as direction')
    top = max(E, top)
print(f'Done, top configuration will provide: {top}')