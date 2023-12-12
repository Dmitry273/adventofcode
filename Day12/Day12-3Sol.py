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

s = '????.?#?.##'
nums = [1, 2]
#got 10 instead of 1

print(killer(s, nums))

"""
file = []
answers = []
for line in open('Day12/day12mat.txt', 'r'):
    s = '?'.join([line.split()[0]]*5)
    nums = list(map(int, line[:-1].split()[1].split(',')))*5
    s = line.split()[0]
    nums = list(map(int, line[:-1].split()[1].split(',')))
    file.append([s, [i for i in nums]])
    # print('.........................')
    # print(nums)
    answ = killer(s, nums)
    answers.append(answ)
    # print(s)
    # print(answ)
    # print('.........................')

print(len(answers))
print(sum(answers))

for i, line in enumerate(open('Day12/day12-1corransw.txt', 'r')):
    if int(line[:-1]) != answers[i]:
        print(file[i])
        print(f'got {answers[i]} instead of {int(line[:-1])}')
"""

# ['??.????.????.?#..?', [1, 1]]
# got 49 instead of 11
# ['#?.?.#??.?????#', [2, 1, 1, 1, 1]]
# got 22 instead of 12
# ['##?.??.???#', [3, 1, 1]]
# got 8 instead of 4
# ['?.?.?????#?#?#?', [1, 8]]
# got 9 instead of 7
# ['?...??.?##?????#???', [3, 2]]
# got 7 instead of 4
# ['??.?#??????#??', [1, 4, 2]]
# got 11 instead of 9
# ['.???.#??#??', [1, 1, 2]]
# got 7 instead of 6
# ['#??????#?#.?.#?', [1, 1, 3, 1, 1]]
# got 8 instead of 6
# ['??..?.???#??.', [1, 1]]
# got 14 instead of 6
# ['#??#?.??#??', [5, 1]]
# got 2 instead of 1
# ['?#??#???????????##??', [3, 1, 1, 2, 1, 2]]
# got 21 instead of 20
# ['?????????.#..', [3, 2, 1]]
# got 14 instead of 10
# ['?.??.??.#??.', [1, 1, 1]]
# got 17 instead of 13
# ['?.???????#?#?.', [1, 7]]
# got 8 instead of 7
# ['????.#???#?', [1, 1, 3]]
# got 11 instead of 8
# ['??????##?###', [1, 6]]
# got 6 instead of 5
# ['#?.?.???#.', [2, 1, 1]]
# got 5 instead of 3
# ['.?#????..###?????#?', [2, 1, 1, 3, 1, 1]]
# got 4 instead of 3
# ['?.??.???.#??', [1, 1, 1, 1]]
# got 23 instead of 21
# ['?..###?#??..??..#???', [5, 1]]
# got 4 instead of 1
# ['??????.??????#.', [1, 1, 1, 3]]
# got 62 instead of 40
# ['.???????#?', [1, 1, 2]]
# got 17 instead of 16
# ['.??#?.???.#', [3, 1]]
# got 8 instead of 2
# ['..??##?????.#???', [4, 2, 1]]
# got 10 instead of 9
# ['???#.??????#???????#', [1, 1, 1, 5, 3, 1]]
# got 23 instead of 21
# ['??????#????', [1, 2]]
# got 14 instead of 11
# ['.???#.???.#.', [1, 1, 1, 1]]
# got 9 instead of 7
# ['??????#???##???#?', [2, 1, 7]]
# got 13 instead of 9
# ['.??.#?#???##??#..', [1, 9]]
# got 3 instead of 1
# ['?????.?????#?#???', [2, 1, 6]]
# got 56 instead of 53
# ['??.?.??????##???##', [2, 1, 1, 8]]
# got 8 instead of 7
# ['???#???#?#???#?#?', [2, 11]]
# got 4 instead of 3
# ['?..?????#??.???.?#?', [1, 6, 1, 1, 1]]
# got 8 instead of 7
# ['.???????#??#??', [1, 7]]
# got 13 instead of 12
# ['??#???#??????#?', [8, 3]]
# got 7 instead of 6
# ['.???????#?.', [3, 1]]
# got 7 instead of 4
# ['##??.#???????#', [4, 1, 1, 2]]
# got 7 instead of 4
# ['????#????#????#???#?', [2, 7, 6]]
# got 8 instead of 7
# ['??.??.??##????????#', [1, 1, 4, 1, 1, 2]]
# got 48 instead of 44
# ['??.##?.?#?', [2, 2]]
# got 3 instead of 2
# ['?##.?#???#?#.?.??#.', [3, 1, 4, 1, 1]]
# got 3 instead of 2
# ['?????.????#???.', [2, 1, 1]]
# got 40 instead of 27
# ['?#?..??????????#', [2, 1, 1, 4]]
# got 28 instead of 20
# ['#???????#?.', [2, 4]]
# got 3 instead of 2
# ['??????.###?.??????#?', [1, 1, 3, 5]]
# got 30 instead of 20
# ['?#..?.?.?#', [1, 1, 1]]
# got 3 instead of 2
# ['.??????#.?', [1, 3]]
# got 4 instead of 3
# ['???????#?..', [3, 2]]
# got 8 instead of 7
# ['?.#???.????#????#??', [1, 7]]
# got 4 instead of 2
# ['.?#???.????#??', [1, 2, 3]]
# got 7 instead of 6
# ['.#?#??#??????#.', [1, 1, 3, 1, 1]]
# got 6 instead of 5
# ['??????.??.#', [4, 1]]
# got 10 instead of 3
# ['??#.???#??.?#????#?', [2, 1, 1, 1, 2, 2]]
# got 13 instead of 11
# ['??#?.?.??#', [1, 1, 1]]
# got 6 instead of 3
# ['???.???#?..', [2, 2]]
# got 7 instead of 5
# ['??????#??#', [2, 1, 2]]
# got 8 instead of 4
# ['?..?#?.?????##', [2, 4]]
# got 4 instead of 2
# ['??.#?...#??', [1, 2]]
# got 3 instead of 1
# ['?###???????#', [6, 3]]
# got 3 instead of 2
# ['???##???#??', [2, 4]]
# got 3 instead of 2
# ['??#??????#?.???', [4, 2]]
# got 9 instead of 6
# ['??.?#?..#.?????#', [1, 2, 1, 2]]
# got 16 instead of 4
# ['????????.???#??', [1, 3, 1, 1]]
# got 42 instead of 34
# ['..???#??.#.#', [1, 2, 1, 1]]
# got 4 instead of 3
# ['???#?.??#?', [2, 2, 1]]
# got 2 instead of 1
# ['?#??#?????#?#?.', [2, 2, 1, 1, 1]]
# got 8 instead of 7
# ['?.??##??.#???', [3, 1]]
# got 3 instead of 2
# ['.???#???##???????##?', [1, 3, 3, 1, 3]]
# got 32 instead of 31
# ['???????#????#.', [5, 3]]
# got 5 instead of 2
# ['???#???.#?', [4, 1]]
# got 7 instead of 4
# ['?.??????#?????#', [1, 2, 5, 1]]
# got 18 instead of 14
# ['.?.##????#?.', [1, 2, 2]]
# got 3 instead of 2
# ['????.?#?.##', [1, 2]]
# got 10 instead of 1
# ['???#?????#?.', [2, 3]]
# got 6 instead of 4
# ['#.#??????#????#.', [1, 2, 1, 1, 3]]
# got 4 instead of 3
# ['??.#??.?#?', [1, 1, 1]]
# got 5 instead of 3
# ['???##???.??#.??', [7, 1]]
# got 4 instead of 2
# ['??#??????.????#?', [7, 1, 1]]
# got 16 instead of 10
# ['#???#?#??#??#..??#.', [13, 1]]
# got 2 instead of 1
# ['??????????.?????#??', [10, 3]]
# got 5 instead of 3
# ['????#????#?', [2, 1, 1]]
# got 9 instead of 5
# ['.???#??.?#.???????#', [3, 1, 1, 2, 1, 1]]
# got 10 instead of 9
# ['?????????#??.?', [2, 5]]
# got 13 instead of 12
# ['?????.?#??.#', [3, 2, 1]]
# got 9 instead of 6
# ['.?????.???#.', [1, 1, 2]]
# got 17 instead of 11
# ['?.#?#?#?#???', [1, 5]]
# got 2 instead of 1
# ['???????#???????#', [9, 2]]
# got 11 instead of 5
# ['.#?.???#?#??', [2, 1, 2]]
# got 2 instead of 1
# ['.?????##??#????#', [1, 7, 1]]
# got 16 instead of 9
# ['??.?#??#????##.?', [5, 2]]
# got 3 instead of 2
# ['???####?#.?..?.#.', [8, 1, 1]]
# got 3 instead of 2
# ['??????????.?????#?', [1, 1, 3, 1, 1, 1]]
# got 95 instead of 80
# ['???.???#???#', [1, 5]]
# got 11 instead of 5
# ['?????##??#?##...', [1, 8]]
# got 5 instead of 4
# ['#????.??#?????#?.', [1, 3, 1, 2, 1]]
# got 5 instead of 3
# ['?????#???#?#?##.??#.', [12, 2]]
# got 2 instead of 1
# ['??????#???##????.?#', [2, 1, 4, 2, 1]]
# got 16 instead of 13
# ['.##???#??????#?##?', [7, 5]]
# got 3 instead of 2
# ['?.#.???#???', [1, 1, 1]]
# got 7 instead of 5
# ['??????#????#??????.#', [14, 1, 1]]
# got 7 instead of 6
# ['#??.?#????###', [1, 1, 4]]
# got 3 instead of 1
# ['?.#...???##.?????', [1, 2]]
# got 2 instead of 1
# ['?????....?#', [1, 1]]
# got 11 instead of 5
# ['?????????#?', [4, 1, 1]]
# got 7 instead of 6
# ['????.????#????????', [1, 3]]
# got 27 instead of 23
# ['?.??#?????#??.', [1, 5]]
# got 7 instead of 3
# ['..?????????.??#', [4, 1, 1, 1]]
# got 18 instead of 14
# ['??.?????#???', [1, 1, 2]]
# got 26 instead of 24
# ['.?.#???#.?', [1, 1, 1]]
# got 4 instead of 3
# ['????????#?.', [3, 3]]
# got 8 instead of 7
# ['???????.#?#????.?', [1, 5]]
# got 9 instead of 8
# ['??#????..??#??#?.#', [1, 1, 1, 1, 4, 1]]
# got 6 instead of 5
# ['??????.??.#????.', [3, 1]]
# got 16 instead of 5
# ['???????#?#?', [3, 4]]
# got 8 instead of 7
# ['.??.??????.#??', [2, 2, 2]]
# got 11 instead of 8
# ['...#???.##?.??', [1, 2]]
# got 2 instead of 1
# ['???#????.????#??.', [2, 2, 2, 3]]
# got 16 instead of 15
# ['?#????.#.????????#?#', [1, 1, 1, 1, 9]]
# got 5 instead of 4
# ['##???#???.?#??.?#???', [6, 2, 1, 1]]
# got 7 instead of 6
# ['?????#???##?????.?#', [6, 7, 1]]
# got 7 instead of 6
# ['?????.??.#??.', [3, 1]]
# got 10 instead of 3