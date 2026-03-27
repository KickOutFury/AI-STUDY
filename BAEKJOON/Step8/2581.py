def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

nums = []
a = int(input())
b = int(input())


for i in range(a,b+1):
    if is_prime(i):
        nums.append(i)

if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))