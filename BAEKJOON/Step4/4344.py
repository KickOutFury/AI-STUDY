n = int(input())


for _ in range(n):
    data = list(map(int, input().split()))
    stu = data[0]
    scores = data[1:]

    avg = sum(scores) / stu
    ct = 0
    
    for score in scores:
        if score > avg:
            ct += 1
    print(f"{ct/stu *100:.3f}%")
    