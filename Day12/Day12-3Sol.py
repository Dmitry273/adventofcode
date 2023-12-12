class Branch():
    def __init__(self, text, dupl= 1):
        self.text = text
        self.dupl = dupl

s = '???#??#??#???????#??#??#???????#??#??#???????#??#??#???????#??#??#???'
s = '?###??????????###??????????###??????????###??????????###????????'
s = s+'.'
nums = [6, 3, 1, 6, 3, 1, 6, 3, 1, 6, 3, 1, 6, 3, 1]
nums = [3,2,1,3,2,1,3,2,1,3,2,1,3,2,1]

branches = [Branch(s)]
while nums:
    num = nums[0]
    nums.pop(0)
    chunk = '#'*num+'.'
    newbranches = []
    for branch in branches:
        B = branch.text
        M = branch.dupl
        for i in range(len(B)):
            if B[i] == '#':
                if B[i:i+num].replace('?','#')+B[i+num:i+num+1].replace('?','.') == chunk:
                    newbranches.append(Branch(B[i+num+1:], M))
                break
            if B[i:i+num].replace('?','#')+B[i+num:i+num+1].replace('?','.') == chunk:
                newbranches.append(Branch(B[i+num+1:], M))
    cap = sum(nums)+len(nums)
    newbranches = list(filter(lambda x: len(x.text)>=cap, newbranches))
    final = []

    for un in set([i.text for i in newbranches]):
        final.append(Branch(un, sum(map(lambda y: y.dupl, list(filter(lambda x: x.text == un, newbranches))))))
    branches = final
for i in range(len(branches)):
    print(branches[i].text, branches[i].dupl)
print(sum(i.dupl for i in branches))