arm=[]
for num in range(100,1000):
    a=num
    s=0
    while(a!=0):
        r=a%10
        s=s+r*r*r
        a=a//10
    if(num==s):
        arm.append(num)
print(f"The armstrong numbers in between 100 to 999 is {arm}")