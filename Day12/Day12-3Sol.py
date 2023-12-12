class Branch():
    def __init__(self, text, dupl= 1):
        self.text = text
        self.dupl = dupl

def killer(s: str, nums: list) -> int:
    s = '.'.join(s.replace('.', ' ').split())
    s = s+'.'
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
                if i+num > len(B)-1: break

                fact = B[i:i+num].replace('?','#')+B[i+num].replace('?','.') == chunk
                if fact: newbranches.append(Branch(B[i+num+1:], M))
                if B[i] == '#': break

        cap = sum(nums)+len(nums)
        newbranches = list(filter(lambda x: len(x.text)>=cap, newbranches))
        branches = []

        for un in set([i.text for i in newbranches]):
            candidates = list(filter(lambda x: x.text == un, newbranches))
            branches.append(Branch(un, sum(map(lambda y: y.dupl, candidates))))

    return sum(i.dupl for i in branches)

# s = '.??????#??????????.??????#??????????.??????#??????????.??????#??????????.??????#?????????'
# nums = [3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1]
# # 1256153707
# print(killer(s, nums))



answers = []
for line in open('Day12/day12mat.txt', 'r'):
    s = '?'.join([line.split()[0]]*5)
    nums = list(map(int, line[:-1].split()[1].split(',')))*5
    # print('.........................')
    # print(nums)
    answ = killer(s, nums)
    answers.append(answ)
    # print(s)
    # print(answ)
    # print('.........................')

print(len(answers))
print(sum(answers))
