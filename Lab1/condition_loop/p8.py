num=int(input("Enter a number: "))
s=0
a=num
while (a!=0):
    r=a%10
    s=s*10+r
    a=a//10
if(s==num):
    print("Palindrome")
else:
    print("Not palindrome")