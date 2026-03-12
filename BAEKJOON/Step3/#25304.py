<<<<<<< HEAD
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
=======
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
>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
    print("No")