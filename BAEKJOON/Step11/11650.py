import sys

input = sys.stdin.readline

T = int(input())

gps = [list(map(int,input().split())) for _ in range(T)]

gps.sort(key = lambda x: (x[0], x[1])) # x[0] << x축을 먼저 정렬하고 x[1]<< x축이 같을경우 y축을 정렬해라.

print("\n".join(f"{x} {y}" for x,y in gps)) # join이 문자열을 받아서 이어붙여주기 때문에 컴프리헨션같이 안에서 반복문을 처리해서 출력하는것이 가능.