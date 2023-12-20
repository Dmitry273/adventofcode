class Broadcaster():
    def __init__(self, state= False, received= []):
        self.state = state
        self.received = received
    
    def react(self):
        return self.received[-1]
    
    def add(self, signal):
        self.received.append(signal)
    
class Flipflop():
    def __init__(self, state= False, received= []):
        self.state = state
        self.received = received
    
    def react(self):
        for _ in range(self.received.count(0)):
            self.state = not self.state
        self.state = not self.state
        self.received = []
        return int(self.state)
    
    def add(self, signal):
        self.received.append(signal)
    
class Conjunction():
    def __init__(self, state= False, received= []):
        self.state = state
        self.received = received
    
    def react(self):
        result = 1
        for signal in self.received:
            result *= signal
        self.received = []
        return int(not result)
    
    def add(self, signal):
        self.received.append(signal)

class Output():
    def __init__(self, state= False, received= []):
        self.state = state
        self.received = received
    
    def react(self):
        return -1
    
    def add(self, signal):
        self.received.append(signal)

elements = [i[:-1] for i in open('Day20/day20mat-t.txt', 'r')]

def finder(name):
    for i in elements:
        if name == i[1:i.index(' ')]: return [i[0]]+i[i.index(' ')+4:].split(', ')

modules = {'output': Output(), 'button': Broadcaster()}
modules['button'].add(0)
active = ['button']
answ = []
for line in elements:
    itype, initiator = line[0], line[1:line.index(' ')]
    if initiator not in modules:
        if itype == '@':
            modules.update({initiator: Broadcaster()})
        elif itype == '%':
            modules.update({initiator: Flipflop()})
        elif itype == '&':
            modules.update({initiator: Conjunction()})
print(modules)
active = ['button']
answ = []
while active:
    initiator = active.pop(0)
    signal = modules[initiator].react()
    if signal == -1:
        answ += [signal]
        continue
    itype, *affected = *finder(initiator),
    for part in affected:
        modules[part].add(signal)
    active += affected

for i in modules:
    print(i, modules[i].state)
    