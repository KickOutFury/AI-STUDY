def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for ch in nums:
    if is_prime(ch):
        cnt += 1

print(cnt)

