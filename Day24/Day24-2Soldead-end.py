import math

class Particle():
    def __init__(self, x, y, z, vx, vy, vz, t = None):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.t = t

particles = [Particle(*map(float, i.replace(' @', ',').split(', '))) for i in open('Day24/day24mat-t.txt', 'r')]

A,B,C = *particles[0:3],

R = Particle(24.01, 13.01, 10.01, -3.01, 1.01, 2.01, 0.0)
#R = Particle(1850480.12, 6233888.90, 112015828.28, 22327335.74, 19979683.48, 12043064.02, 0.0)
A.t, B.t, C.t = 1.01, 3.01, 6.01
#A.t, B.t, C.t = 7688892.54, 9140461.62, 15435900.22
learning_rate = 0.05
def loss(R, p):
    x = (R.x-p.x) + (p.t-R.t)*(R.vx-p.vx)
    y = (R.y-p.y) + (p.t-R.t)*(R.vy-p.vy)
    z = (R.z-p.z) + (p.t-R.t)*(R.vz-p.vz)
    return math.sqrt(x**2+y**2+z**2)

def rloss(R, *P):
    lx, ly, lz = *map(lambda p: loss(R, p), P),
    x = sum(map(lambda p: (R.x-p.x) + (p.t-R.t)*(R.vx-p.vx), P))
    y = sum(map(lambda p: (R.y-p.y) + (p.t-R.t)*(R.vy-p.vy), P))
    z = sum(map(lambda p: (R.z-p.z) + (p.t-R.t)*(R.vz-p.vz), P))
    return [(x*learning_rate)/lx, (y*learning_rate)/ly, (z*learning_rate)/lz]

def vloss(R, *P):
    lx, ly, lz = *map(lambda p: loss(R, p), P),
    vx = sum(map(lambda p: ((R.x-p.x) + (p.t-R.t)*(R.vx-p.vx))*p.t, P))
    vy = sum(map(lambda p: ((R.y-p.y) + (p.t-R.t)*(R.vy-p.vy))*p.t, P))
    vz = sum(map(lambda p: ((R.z-p.z) + (p.t-R.t)*(R.vz-p.vz))*p.t, P))
    return [(vx*learning_rate)/lx, (vy*learning_rate)/ly, (vz*learning_rate)/lz]

def tloss(R, *P):
    answ = []
    for p in P:
        answ.append(((((R.x-p.x) + (p.t-R.t)*(R.vx-p.vx))*(R.vx-p.vx))*learning_rate)/loss(R, p))
    return answ

i = 0
while 1:
    dr = rloss(R, A, B, C)
    R.x -= dr[0]
    R.y -= dr[1]
    R.z -= dr[2]

    dv = vloss(R, A, B, C)
    R.vx -= dv[0]
    R.vy -= dv[1]
    R.vz -= dv[2]

    dt = tloss(R, A, B, C)
    A.t -= dt[0]
    B.t -= dt[1]
    C.t -= dt[2]

    if i%100000 == 0:
        print(f'currently at the loss of {loss(R,A)+loss(R,B)+loss(R,C)}, step {i}')
        print(f'best guess for r is {R.x},{R.y},{R.z}')
        print(f'best guess for v is {R.vx},{R.vy},{R.vz}')
        print(f'best guess for t is {A.t},{B.t},{C.t}')
    i += 1

"""
best guess for r is 55.66320145024265,156603.97858952443,1055710.2353211374
best guess for v is 19846285.91987923,19705509.98752874,25369656.500381913
best guess for t is 7688892.548093021,9140461.62031985,15435900.220292669
"""
"""
best guess for r is 1850480.121130088,6233888.907335338,112015828.28027381
best guess for v is 22327335.748932008,19979683.486849114,12043064.026548464
best guess for t is 10605718.301005721,9203472.485604009,17161323.97059961
"""