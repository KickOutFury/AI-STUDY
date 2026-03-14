a = input().upper()

letters = list(set(a))
counts = []

for ch in letters:
    counts.append(a.count(ch))

if counts.count(max(counts)) > 1:
    print("?")
else:
    print(letters[counts.index(max(counts))])