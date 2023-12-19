class Part():
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

instructions = []
parts = []
i = False
for line in open('Day19/day19mat.txt', 'r'):
    if i: parts.append(line[:-1])
    if line[:-1] == '': i=True
    if not i: instructions.append(line[:-1])

for func in instructions:
    name = func[:func.index('{')]
    if name == 'in': name = '_in_'
    ifs = func[func.index('{')+1:-1].split(',')
    func = f'def {name}(x):\n'
    for part in ifs:
        result = part[part.find(':')+1:]
        cond = '\t'
        if '<' in part or '>' in part:
            cond = part[:part.index(':')]
            cond = f'\tif x.{cond}:'
        if result == 'A' or result == 'R':
            cond = f'{cond}return \'{result}\''
        else:
            cond = f'{cond}return {result}(x)'
        cond = f'{cond}\n'
        func += cond
    exec(func)

xmas = 0
for part in parts:
    part = part[1:-1]
    exec(f'x = Part({part})')
    exec(f'answ = _in_(x)')
    if answ == 'A': xmas += x.x + x.m + x.a + x.s

print(xmas)