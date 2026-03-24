T  = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())

    if N % H == 0:
        fl = H
        no = N // H
    else:
        no = (N//H) +1
        fl = N % H

    print(f"{fl}{no:02d}")