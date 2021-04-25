import random

nums = []

print('pension : ', end = '')
jo = random.randrange(1, 6)
print(jo, end = '조 ')

for i in range(6):
    rn = random.randrange(0, 10)
    nums.append(rn)
nums.sort()
print(nums)

nums.clear()
print('lotto : ', end='')
c = 0
while c < 6:
    rn = random.randrange(1, 46)
    if rn in nums:
        continue
    nums.append(rn)
    c=c+1
nums.sort()
print(nums)
