class Branch():
    def __init__(self, text, dupl= 1):
        self.text = text
        self.dupl = dupl

def killer(s: str, nums: list) -> int:
    s = '.'.join(s.replace('.', ' ').split())   # get rid of useless dots
    s = s+'.'                                   # add dot at the end for easier construction of branches at the end
    branches = [Branch(s)]
    while nums:
        num = nums[0]                           # get the first number in queue, we will try to construct a branch with it
        nums.pop(0)
        chunk = '#'*num+'.'                     # i.e. 6 means we want to insert chunk: ######. somewhere in the beginning
        newbranches = []
        for branch in branches:
            B = branch.text                     # B is current state ahead in this branch
            M = branch.dupl                     # M is how many braches were behore that lead to the same result
            for i in range(len(B)):
                if i+num > len(B)-1: break      # too far, won't fit

                fact = B[i:i+num].replace('?','#')+B[i+num].replace('?','.') == chunk
                if fact: newbranches.append(Branch(B[i+num+1:], M))

                if B[i] == '#': break           # reached #, going further is pointless

        cap = sum(nums)+len(nums)
        newbranches = list(filter(lambda x: len(x.text)>=cap, newbranches))

        branches = []
        for un in set([i.text for i in newbranches]):
            candidates = list(filter(lambda x: x.text == un, newbranches))
            branches.append(Branch(un, sum(map(lambda y: y.dupl, candidates))))

    branches = list(filter(lambda x: x.text.count('#')==0, branches))
    return sum(i.dupl for i in branches)

answers = []
for line in open('Day12/day12mat.txt', 'r'):
    s = '?'.join([line.split()[0]]*5)
    nums = list(map(int, line[:-1].split()[1].split(',')))*5
    answ = killer(s, nums)
    answers.append(answ)

print(sum(answers))