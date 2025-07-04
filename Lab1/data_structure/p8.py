names = ["Anup", "Crystal", "Bandhan", "Abhay", "Bandhan", "Abhay"]

counts = {}

for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

print(counts)
