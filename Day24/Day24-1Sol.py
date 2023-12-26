Test = [200000000000000.0, 400000000000000.0]

class Particle():
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

def line(a):
    if a.vy != 0.0:
        A = 1.0
        B = -a.vx/a.vy
        C = -a.y*B-a.x
    else:
        A = 0.0
        B = 1.0
        C = -a.y
    return (A,B,C)

def col(a, b):
    A1, B1, C1, A2, B2, C2 = *line(a), *line(b)
    if (A1*B2-A2*B1) != 0.0: return ((C2*B1-C1*B2)/(A1*B2-A2*B1),-(C2*A1-C1*A2)/(A1*B2-A2*B1))
    else: return(float('inf'),float('inf'))

def inside(a, b):
    R = col(a, b)
    if a.vx != 0.0: t1 = (R[0]-a.x)/a.vx
    else: t1 = (R[1]-a.y)/a.vy
    if b.vx != 0.0: t2 = (R[0]-b.x)/b.vx
    else: t2 = (R[1]-b.y)/b.vy
    return Test[0] <= R[0] and R[0] <= Test[1] and Test[0] <= R[1] and R[1] <= Test[1] and t1>=0.0 and t2>=0.0

particles = [Particle(*map(float, i.replace(' @', ',').split(', '))) for i in open('Day24/day24mat.txt', 'r')]

answ = 0
for i in range(len(particles)-1):
    for j in range(i+1,len(particles)):
        if inside(particles[i],particles[j]): answ += 1
print(answ)
for particle in particles:
    print(line(particle))