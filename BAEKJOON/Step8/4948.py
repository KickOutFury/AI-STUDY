# def is_prime(n):
#     if n == 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
        
#     return True

# while True:
#     cnt = 0
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         for i in range(n+1,(2*n)+1):
#             if is_prime(i):
#                 cnt += 1
#     print(cnt)

# 시간초과로 에라토스테네스의 체 사용
limit = 246912

prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            cnt += 1

    print(cnt)