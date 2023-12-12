import itertools

def poten(s: str, nums: list) -> bool:
    ss = s
    if '?' in s: ss = s[:s.index('?')]
    local = []
    for key, group in itertools.groupby(ss, key= lambda x: x =='#'):
        if key: local.append(len(list(group)))
    if local == []: return True

    if len(local) > len(nums): return False
    for i in range(len(local)-1):
        if local[i] != nums[i]: return False
    if ('?' not in s or ss[-1]=='.') and local[len(local)-1] != nums[len(local)-1]: return False
    if local[len(local)-1] > nums[len(local)-1]: return False
    return True

def eater(s: str, nums: list) -> str:
    if '?' not in s: return s
    a = s.replace('?', '#', 1)
    b = s.replace('?', '.', 1)
    if not poten(a, nums):
        return eater(b, nums)
    if not poten(b, nums):
        return eater(a, nums)
    return s

def crurc(s: str, nums: list) -> str:
    return eater(eater(s,nums)[::-1],nums[::-1])[::-1]

def prety(s, nums):
    zalupa = s.replace('.',' ').split()
    i = 0
    for word in zalupa:
        if word.count('?') > 0: break
        i += 1
    else:
        return 'TUT ODNO ZAPOLNENIE'
    zalupa = zalupa[i:]
    answ = nums[i:]
    i = 0
    for word in zalupa[::-1]:
        if word.count('?') > 0: break
        i += 1
    zalupa = zalupa[:len(zalupa)-i]
    answ = answ[:len(answ)-i]

    return ['.'.join(zalupa), answ]

pr9 = ['???#??#??#???????#??#??#???????#??#??#???????#??#??#???????#??#??#???', [6, 3, 1, 6, 3, 1, 6, 3, 1, 6, 3, 1, 6, 3, 1]]


file = []
for line in open('Day12/day12mat.txt'):

    s = '?'.join([line.split()[0]]*5)
    nums = list(map(int, line[:-1].split()[1].split(',')))*5
    file.append(f'recordings are: {s}, engineer notes:{nums}')
    #print(f'recordings are: {s}, engineer notes:{nums}')
    print('....................')
    temp = prety(crurc(s, nums), nums)
    ss, numss = temp[0], temp[1]
    print(ss, numss)
    ss = crurc(ss, nums)
    temp = prety(ss, numss)
    ss, numss = temp[0], temp[1]
    print(ss, numss)
    print('....................')
