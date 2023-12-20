connections = [i[:-1] for i in open('Day20/day20mat.txt', 'r')]
def finder(name):
    for i in connections:
        if name == i[1:i.index(' ')]: return i[i.index(' ')+4:].split(', ')

class Broadcast():
    def __init__(self, name):
        self.name = name
        self.state = 0
    
    def react(self, signal=None, initiator=None):
        return 0

class Flipflop():
    def __init__(self, name, state= None):
        self.name = name
        self.state = False
    
    def react(self, signal=None, initiator=None):
        if signal == 1: return -1
        if signal != None: self.state = not self.state
        return int(self.state)
    
class Conjunction():
    def __init__(self, name, state= None):
        self.name = name
        self.state = {}
    
    def react(self, signal=None, initiator=None):
        if signal != None: self.state[initiator] = signal
        return int(not all(self.state.values()))

class Output():
    def __init__(self, name, state=None):
        self.name = name
        self.state = []
    
    def react(self, signal=None, initiator=None):
        if signal == 0: return 10
        return -1
        

modules = {'roadcaster': Broadcast('roadcaster')}
for line in connections:
    if line.startswith('broadcaster'): continue
    name = line[1:line.index(' ')]
    if line[0] == '%':
        modules.update({name: Flipflop(name)})
    elif line[0] == '&':
        modules.update({name: Conjunction(name)})

for line in connections:
    if line.startswith('broadcaster'): continue
    name = line[1:line.index(' ')]
    affected = line[line.index(' ')+4:].split(', ')
    for module in affected:
        if module not in modules:
            modules.update({module: Output(module)})
        if type(modules[module]) is Conjunction:
            modules[module].state.update({name: 0})

# for module in modules:
#     print(type(modules[module]), modules[module].name, modules[module].state)

#answ = [0,0]
Gothim = [0]
def push():
    active = ['roadcaster']
    #answ[0] += 1
    while active:
        initiator = active.pop(0)
        affected = finder(initiator)
        signal = modules[initiator].react()
        if initiator == 'hf':
            if list(modules[initiator].state.values()).count(0) == 0:
                print('Yay')
                Gothim[0] += 1
        #answ[signal] += len(affected)
        for module in affected:
            if module == 'rx' and signal == 0:
                Gothim[0] += 1
                print('Gotcha')
                break
            if modules[module].react(signal, initiator) != -1:
                active.append(module)
        else:
            continue
        break

# for module in modules:
#     print(type(modules[module]), modules[module].name, modules[module].state)
i = 0
for i in range(2**13):
    # if i%1000000 == 0:
    #     print(f'still alive, {i//1000000}m out 100 done')
    push()
    if Gothim[0]:
        Gothim[0] = 0
        print(i+1)
    # if list(modules['lq'].state.values()).count(0) == 0:
    #     print(i+1)
    # if modules['lq'].state['lr'] and modules['lq'].state['sx'] and modules['lq'].state['xn'] and modules['lq'].state['fn']:
    #     print(i+1)
    #     print(modules['lq'].state)
    #     break
print(modules['lq'].state)
print(2**5+2**10+2**11+2**4+2**2+2**12+2**1+2**8)
#lq -> 3739, hb -> 3919, dl -> 3797, hf -> 4003
#print(answ)
#print(answ[0]*answ[1])

import math
print(math.lcm(3739, 3919, 3797, 4003))