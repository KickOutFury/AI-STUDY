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

limit = 246912

# 처음엔 전부 소수라고 가정
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

# 입력 처리
while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            cnt += 1

    print(cnt)

    