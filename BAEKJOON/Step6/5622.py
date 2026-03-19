A = {2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PQRS",8:"TUV",9:"WXYZ"}

ct = 0

a = input()

for ch in a:
    for num,lt in A.items():
        if ch in lt:
            ct += num + 1
print(ct)