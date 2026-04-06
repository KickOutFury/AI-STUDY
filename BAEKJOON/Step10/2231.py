import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    s = i + sum(map(int, str(i))) # str 문자열은 하나하나씩 나눠져있는 것 예를들어 "128"이라면 '1','2','8' 이렇게 되어있어 정수형으로 변환시 각각 따로따로 합산 가능함.
    if s == n:
        print(i)
        break
else:
    print(0)