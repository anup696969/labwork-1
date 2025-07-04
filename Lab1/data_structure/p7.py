dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 40}
new = dict1.copy()
for key, value in dict2.items():
    if key in new:
        new[key] += value
    else:
        new[key] = value

print(new)
