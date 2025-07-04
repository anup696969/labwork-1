l=[]
p=0
z=0
n=0
print("Enter 10 integers:")
for i in range(1,11):
    num=int(input())
    l.append(num)
    if(num>0):
        p+=1
    elif(num==0):
        z+=1
    else:
        n+=1
print(f"Among {l}\nPositive = {p}\nNegative = {n}\nZero = {z}")
