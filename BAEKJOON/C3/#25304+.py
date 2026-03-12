<<<<<<< HEAD
#25304+
#코테 스타일 압축버전

X = int(input())
S = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    S += a*b

=======
#25304+
#코테 스타일 압축버전

X = int(input())
S = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    S += a*b

>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
print("Yes" if X == S else "No")