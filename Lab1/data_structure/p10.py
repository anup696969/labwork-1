d = {}
n = int(input("How many key-value pairs do you want to enter? "))
for i in range(n):
    key = input(f"Enter key #{i+1}: ")
    value = input(f"Enter value for key '{key}': ")
    d[key] = value
print("\nThe dictionary is:")
print(d)
search = input("\nEnter the key you want to search for: ")
if search in d:
    print(f"The value for key '{search}' is: {d[search]}")
else:
    print(f"Key '{search}' not found in the dictionary.")
