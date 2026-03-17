n, work = map(int,input().split())

nums =[]

for i in range(n):
    nums.append(i+1)

for _ in range(work): 
    st, fi = map(int,input().split())
    nums[st-1:fi] = reversed(nums[st-1:fi])

print(*nums)

# 좀 더 축약
# n, work = map(int, input().split())
# nums = list(range(1, n+1))

# for _ in range(work):
#     st, fi = map(int, input().split())
#     nums[st-1:fi] = reversed(nums[st-1:fi])

# print(*nums)