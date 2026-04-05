import sys

input = sys.stdin.readline

T = int(input())

inf = [list(input().split()) for _ in range(T)]

inf.sort(key = lambda x: int(x[0])) # 나이를 int형으로 바꿔서 정렬

print("\n".join(f"{x} {y}" for x, y in inf))