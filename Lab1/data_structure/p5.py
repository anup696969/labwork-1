s = set()
for i in range(1, 50):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        s.add(i)
print(s)
a = int(input("Enter any number: "))
if a in s:
    print("The input number is in the set!")
else:
    print("Not in set.")
