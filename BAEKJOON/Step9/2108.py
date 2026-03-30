import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))

counter = Counter(nums)
max_freq = max(counter.values())

modes = [k for k, v in counter.items() if v == max_freq]
modes.sort()

nums.sort()
median = nums[len(nums)//2]

print(round(sum(nums)/n))

print(median)

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(max(nums)-min(nums))