import sys

input = sys.stdin.readline

best = 0

T, m = map(int,input().split())

card = list(map(int, input().split()))

for i in range(T):
    for j in range(i+1,T):
        for k in range(j+1, T):
            s = card[i] + card[j] + card[k]
            if s <= m:
                best = max(best, s)

print(best)