while True:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    print("+ for addition\n- for subtraction\n* for multiplication\n/ for division")
    choice = input("Which operation do you want to perform: ")
    
    if choice == '+':
        print(f"{a} + {b} = {a + b}")
    elif choice == "-":
        print(f"{a} - {b} = {a - b}")
    elif choice == "*":
        print(f"{a} X {b} = {a * b}")
    elif choice == "/":
        if b == 0:
            print("Division by zero is not allowed!")
        else:
            print(f"{a} / {b} = {a / b}")
    else:
        print("Invalid choice!!!")
    
    ch = input("Do you want to try again? (y/n): ")
    ch = ch.lower()
    if ch == 'y':
        continue
    else:
        break

print("Thank you for trying!")
