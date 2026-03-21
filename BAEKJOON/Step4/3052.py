a = []
count = 0

for _ in range(10):
    n = int(input())
    a.append(n%42)

for c in set(a):
    count += 1

print(count)