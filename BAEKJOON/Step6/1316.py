n = int(input())
ct = 0

for _ in range(n):
    word = input()
    seen = []
    group = True

    for i in range(len(word)):
        if i == 0:
            seen.append(word[i])
        else:
            if word[i] != word[i-1]:
                if word[i] in seen:
                    group = False
                    break
                seen.append(word[i])
    if group:
        ct += 1

print(ct)