seq = list(open('Day15/day15mat.txt', 'r'))[0].split(',')

def HASH(s):
    answ = 0
    for ch in s:
        answ += ord(ch)
        answ *= 17
        answ %= 256
    return answ

answ = 0
for s in seq:
    answ += HASH(s)
print(f'answer to the first part is: {answ}')

answ = 0
boxes = [[] for i in range(256)]
for s in seq:
    if '-' in s:
        box = boxes[HASH(s[:-1])]
        for i in range(len(box)):
            if box[i][:-2] == s[:-1]:
                box.pop(i)
                break
    else:
        box = boxes[HASH(s[:-2])]
        for i in range(len(box)):
            if box[i][:-2] == s[:-2]:
                box[i] = box[i][:-1]+s[-1]
                break
        else:
            box.append(s.replace('=', ' '))

for i in range(256):
    box = boxes[i]
    for j in range(len(box)):
        answ += (i+1)*(j+1)*int(box[j][-1])

print(f'answer to the second part is: {answ}')