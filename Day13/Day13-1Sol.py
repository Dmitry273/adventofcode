import numpy as np

def findMirr(arr):
    for i in range(1,len(arr)):
        l = arr[:i]
        r = arr[i:]
        s = min(len(l),len(r))
        l = l[::-1][:s][::-1]
        r = r[:s]
        if l == r[::-1]: return i
    return -1
answ = 0
currh = []
for line in open('Day13/day13mat.txt', 'r'):
    content = line[:-1]
    bina = [content.replace('#','1').replace('.','0')]
    bina = [1 if i=='#' else 0 for i in content]
    if content != '': currh.append(bina)
    else: 
        data = np.array(currh)
        currh = np.rot90(currh,0)
        currv = np.rot90(currh,-1)
        ch = []
        cv = []
        for l in currh:
            ch.append(sum(l[k]*2**k for k in range(len(l))))
        for l in currv:
            cv.append(sum(l[k]*2**k for k in range(len(l))))
        print(currh)
        H = findMirr(ch)
        V = findMirr(cv)
        if H != -1:
            answ += H*100
        elif V != -1:
            answ += V
        else:
            print('blyaa, pizdez')
            break
        currh = []
print(answ)