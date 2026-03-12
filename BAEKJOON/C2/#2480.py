<<<<<<< HEAD
#2480
a, b, c = map(int, input().split())

if a==b==c: print(10000+(a*1000))
elif a==b or b==c: print(1000+(b*100))
elif a==c: print(1000+(c*100))
=======
#2480
a, b, c = map(int, input().split())

if a==b==c: print(10000+(a*1000))
elif a==b or b==c: print(1000+(b*100))
elif a==c: print(1000+(c*100))
>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
else: print (max(a,b,c)*100)