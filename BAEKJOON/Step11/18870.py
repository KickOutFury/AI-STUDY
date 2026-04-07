import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr)) # 정렬 + 중복제거

dic = {}
for i in range(len(sorted_arr)): # 딕셔너리에 키(arr값):밸류(인덱스값) 맵핑
    dic[sorted_arr[i]] = i

for x in arr: 
    print(dic[x], end=' ') # 원본에서 딕셔너리 키값과 비교해서 밸류값 출력.