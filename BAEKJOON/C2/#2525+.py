<<<<<<< HEAD
#2525+
# 초고퀄 코테 분으로 단위 통일
A, B = map(int, input().split())
C = int(input())

time = A*60 + B + C

=======
#2525+
# 초고퀄 코테 분으로 단위 통일
A, B = map(int, input().split())
C = int(input())

time = A*60 + B + C

>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
print((time // 60) % 24, time % 60)