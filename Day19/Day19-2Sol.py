import copy
instructions = []
for line in open('Day19/day19mat.txt', 'r'):
    if line[:-1] == '': break
    instructions.append(line[:-1])

xmas = {'x':[1,4001], 'm':[1,4001], 'a':[1,4001], 's':[1,4001]}

def mult(xmas):
    segm = list(map(lambda x: x[1]-x[0], xmas.values()))
    answ = 1
    for i in segm:
        answ *= i
    return answ

def finder(name):
    for func in instructions:
        if name == func[:func.find('{')]: return func[func.index('{')+1:-1]

def splitter(xmas: dict, target: str, more: bool, num: int) -> tuple:
    passed = copy.deepcopy(xmas)
    notpas = copy.deepcopy(xmas)
    if more:
        passed[target][0] = max(passed[target][0],num+1)
        notpas[target][1] = min(notpas[target][1],num+1)
    else:
        passed[target][1] = min(passed[target][1],num)
        notpas[target][0] = max(notpas[target][0],num)
    if passed[target][0] > passed[target][1]: passed = {'x':[1,1], 'm':[1,1], 'a':[1,1], 's':[1,1]}
    if notpas[target][0] > notpas[target][1]: notpas = {'x':[1,1], 'm':[1,1], 'a':[1,1], 's':[1,1]}
    return (passed, notpas)

def compilator(instruction: str, xmas: dict) -> int:
    if xmas == {'x':[1,1], 'm':[1,1], 'a':[1,1], 's':[1,1]}: return 0
    if instruction == 'A': return mult(xmas)
    if instruction == 'R': return 0
    if ':' not in instruction: return compilator(finder(instruction),xmas)
    next = instruction.split(',')[0]
    last = ','.join(instruction.split(',')[1:])
    cond = next[:next.find(':')]
    result = next[next.find(':')+1:]
    target, more, num = (cond[0],cond[1] == '>',int(cond[2:]))
    passed, notpas = splitter(xmas, target, more, num)
    return compilator(result, passed) + compilator(last, notpas)

print(compilator('in', xmas))