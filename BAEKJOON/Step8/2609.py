# 유클리드 호제법, a % b의 나머지를 b로 저장하고 원래 b를 a로 저장 b가 0이 될때까지 반복하고 0이 나오면 a는 최대공약수, 원본 a,b의 곱 나누기 최대공약수는 최소공배수이다.
a,b = map(int,input().split())
A,B = a,b

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (A * B) // gcd

print(gcd)
print(lcm)