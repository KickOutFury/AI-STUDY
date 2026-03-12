#2525+
# 초고퀄 코테 분으로 단위 통일
A, B = map(int, input().split())
C = int(input())

time = A*60 + B + C

print((time // 60) % 24, time % 60)