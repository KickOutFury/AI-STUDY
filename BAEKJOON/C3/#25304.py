#25304

X = int(input())
N = int(input())
S = 0

for _ in range(0,N):
    a, b = map(int,input().split())
    S += (a * b)
if X == S:
    print("Yes")
else:
    print("No")