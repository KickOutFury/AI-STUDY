x = int(input()) #x=7

line = 1
end = 1

while x > end:
    line += 1 #4
    end += line #10

start = end - line + 1 # 이번 대각선 시작값 = 지금 대각선 마무리값 - 누적값(지난 대각선 마무리값) + 1. >> 7
idx = x - start # ex) x = 7 >> 7-7 idx 0  

if line % 2 == 0:
    top = 1 + idx
    bottom = line - idx
else:
    top = line - idx
    bottom = 1 + idx

print(f"{top}/{bottom}")
