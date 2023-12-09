
def genDer(nums):
    while not all(nu == nums[0] for nu in nums):
        yield nums[0]
        nums = [nums[i]-nums[i-1] for i in range(1, len(nums))]
    else:
        yield nums[0]
lal = []
for line in open('Day9/day9mat.txt', 'r'):
    kek = genDer([int(i) for i in line.split()])
    mem = [a for a in kek]
    lal.append(sum(mem[0::2])-sum(mem[1::2]))
print(sum(lal))