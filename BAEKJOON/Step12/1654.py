# 이분 탐색
arr = []

K, N = map(int,input().split())

for _ in range(K):
    arr.append(int(input()))
    

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2

    # mid 길이로 잘랐을 때 몇 개 나오는지 계산
    total = sum(x // mid for x in arr)

    if total >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)