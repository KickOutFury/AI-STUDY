#15552+
#코테식 빠른 입출력을 위해 sys 모듈 이용

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(a+b)