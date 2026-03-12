<<<<<<< HEAD
#2525
A, B = map(int, input().split())
C = int(input())

B = B + C
if B>=60:
    D = B//60
    B = B-(D*60)
    A = A + D
    
    if A>24:
        print((0+D%24),B)
    elif A==24:
        print(0,B)
    else: print(A,B)
    
elif B<60:
=======
#2525
A, B = map(int, input().split())
C = int(input())

B = B + C
if B>=60:
    D = B//60
    B = B-(D*60)
    A = A + D
    
    if A>24:
        print((0+D%24),B)
    elif A==24:
        print(0,B)
    else: print(A,B)
    
elif B<60:
>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
    print(A,B)