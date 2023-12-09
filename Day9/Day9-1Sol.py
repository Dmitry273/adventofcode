
def genDer(nums):
    while not all(nu == nums[0] for nu in nums):
        yield nums[-1]
        nums = [nums[i]-nums[i-1] for i in range(1, len(nums))]
    else:
        yield nums[-1]
lal = []
for line in open('Day9/day9mat.txt', 'r'):
    kek = genDer([int(i) for i in line.split()])
    mem = [a for a in kek]
    lal.append(sum(mem))

print(sum(lal))