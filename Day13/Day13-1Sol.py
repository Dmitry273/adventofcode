import numpy as np

def diff(arra,arrb):
    err = 0
    for a, b in zip(arra,arrb):
        if a != b: err += 1
    return err

def findMirr(arr):
    for i in range(1,len(arr)):
        l = arr[:i]
        r = arr[i:]
        s = min(len(l),len(r))
        l = l[::-1][:s][::-1]
        r = r[:s]
        answ = 0
        for j in range(s):
            answ += diff(l[j],r[::-1][j])
        if answ == 1: return i # change to answ == 0 for 1 part
    return -1
answ = 0
currh = []
for line in open('Day13/day13mat.txt', 'r'):
    content = line[:-1]
    if content != '': currh.append([i for i in content])
    else: 
        data = np.array(currh)
        currh = np.rot90(currh,0)
        currv = np.rot90(currh,-1)

        H = findMirr(currh.tolist())
        V = findMirr(currv.tolist())
        if H != -1:
            answ += H*100
        elif V != -1:
            answ += V
        else:
            print('blyaa, pizdez')
            break
        currh = []
print(answ)