ct = 0

word = input()

crt = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in crt:
    word = word.replace(c,"*")

print(len(word))