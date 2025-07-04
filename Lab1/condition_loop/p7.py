n=int(input("Enter the value of n "))
a=0
b=1
fibo=[]
fibo.append(a)
fibo.append(b)
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    fibo.append(c)
print(fibo)