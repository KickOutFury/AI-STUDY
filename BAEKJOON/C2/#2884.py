<<<<<<< HEAD
#2884
H, M = map(int, input().split())

M -= 45

if M < 0:
    M += 60
    H -= 1

    if H < 0:
        H = 23

=======
#2884
H, M = map(int, input().split())

M -= 45

if M < 0:
    M += 60
    H -= 1

    if H < 0:
        H = 23

>>>>>>> 24614cf4d2dcb70197acf4f5aba3d3adb0e3f2ef
print(H, M)