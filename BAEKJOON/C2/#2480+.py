<<<<<<< HEAD
#2480+
#코테 식 정렬이용
a, b, c = sorted(map(int, input().split()))

if a == c:
    print(10000 + a*1000)
elif a == b or b == c:
    print(1000 + b*100)
else:
    print(c*100)
    
# 정렬하면

# a ≤ b ≤ c

# 그래서

# a==c → 세 개 같음

# a==b 또는 b==c → 두 개 같음

=======
#2480+
#코테 식 정렬이용
a, b, c = sorted(map(int, input().split()))

if a == c:
    print(10000 + a*1000)
elif a == b or b == c:
    print(1000 + b*100)
else:
    print(c*100)
    
# 정렬하면

# a ≤ b ≤ c

# 그래서

# a==c → 세 개 같음

# a==b 또는 b==c → 두 개 같음

>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
# 아니면 c가 최대