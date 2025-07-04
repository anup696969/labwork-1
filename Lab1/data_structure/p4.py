string=input("Enter a string: ")
d={}
unique=set(string)
for s in unique:
    d[s]=string.count(s)
print(d)
