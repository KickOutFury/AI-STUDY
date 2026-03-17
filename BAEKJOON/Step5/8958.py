n = int(input())

for _ in range(n):
    note = input()
    pa = 0
    s = 0
    for ch in note:
        if ch == "O":
            pa += 1
            s += pa
        else:
            pa = 0
    print(s)
# 축약 버전
# n = int(input())

# for _ in range(n):
#     s = 0
#     pa = 0

#     for ch in input():
#         if ch == "O":
#             pa += 1
#             s += pa
#         else:
#             combo = 0

#     print(s)