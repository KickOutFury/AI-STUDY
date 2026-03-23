a = []
count = 0

for _ in range(10):
    n = int(input())
    a.append(n%42)

for c in set(a):
    count += 1

print(count)

# 축약 {}가 set을 만드는 상황
# print(len({int(input()) % 42 for _ in range(10)})) << 반복하면서 리스트 생성