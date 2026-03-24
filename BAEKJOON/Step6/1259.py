
while True:
    n = input()
    if n == "0":
        break
    else:
        if n == n[::-1]:
            print("yes")
        else:
            print("no")

# 축약버전
# while True:
#     n = input()
#     if n == "0":
#         break
#     print("yes" if n == n[::-1] else "no")
    

