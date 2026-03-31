T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    A,B = a,b
    while b != 0:
        a, b = b, a%b
    
    gcd = a
    lcm = (A*B) // gcd

    print(lcm)