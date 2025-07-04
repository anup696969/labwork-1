l = []
print("Enter list elements: ")
i = 1

while True:
    num = int(input(f"Enter {i} element: "))
    l.append(num)
    ch = input("Do you want to add more? (y/n): ")
    ch = ch.lower()
    if ch == 'y':
        i += 1
        continue
    else:
        break
print(f"The list is {l}")
largest=l[0]
smallest=l[0]
for num in l:
    if(num<smallest):
        smallest=num
    if(num>largest):
        largest= num
print(f"Among {l}\nLargest = {largest}\nSmallest = {smallest}")