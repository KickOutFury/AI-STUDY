n = int(input())

for _ in range(n):
    R,S = input().split()
    R = int(R)

    for ch in S:
        print(ch * R, end= "")
    print()