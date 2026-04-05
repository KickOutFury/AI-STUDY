import sys

input = sys.stdin.readline

T = int(input())

cnt = [0] * 10001

for _ in range(T):
    n = int(input())
    cnt[n] += 1

for i in range(10001):
        if cnt[i] != 0:
            for _ in range(cnt[i]):
                print(i)

# 최대 10000까지 숫자를 입력받는 코드 기준이기 때문에 일반정렬로 리스트를 받을경우 리스트 메모리 크기가 너무 커질수 있어 10000개로 수를 제한하고 카운팅 정렬 방법을 사용함.
# 리스트의 인덱스 그 자체를 "숫자"로 판단하고 리스트에 들어오는 값은 그 숫자가 몇번 나왔는지 누적하여 반복문과 조건문을 이용하여 출력을 하는 방식으로 코드작성.