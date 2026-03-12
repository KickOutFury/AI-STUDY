#25304+
#코테 스타일 압축버전

X = int(input())
S = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    S += a*b

print("Yes" if X == S else "No")