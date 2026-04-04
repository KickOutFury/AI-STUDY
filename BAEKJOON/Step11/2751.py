import sys

input = sys.stdin.readline

T = int(input())

a = [int(input().strip()) for _ in range(T)]

a.sort()

print("\n".join(map(str,a)))