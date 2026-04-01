T = int(input())
data = []

for _ in range(T):
    w, h = map(int,input().split())
    data.append((w,h))

for i in range(T): # 현재 사람
    rank = 1

    for j in range(T): # 모든 사람과 비교
        if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
            rank += 1

    print(rank, end=" ") # 첫 데이터 부터 순서대로 쭈르륵 순위가 나옴
    