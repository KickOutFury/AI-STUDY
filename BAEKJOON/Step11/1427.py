import sys
input = sys.stdin.readline

n = list(input().strip())

n.sort(key= lambda x: -int(x))

print("".join(n))

# 더 축약 버전
# n = input().strip()
# print("".join(sorted(n, reverse=True)))