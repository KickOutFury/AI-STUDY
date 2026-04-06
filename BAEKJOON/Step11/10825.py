import sys
input = sys.stdin.readline

T = int(input())
inf = [list(input().split()) for _ in range(T)]

inf.sort(key= lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for name, a, b, c in inf:
    print(name)