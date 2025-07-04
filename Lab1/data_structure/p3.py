a=[2,8,40,8,5,60,7,9,10]
b=[]
for i in set(a):
    if(i%2==0):
        b.append(i)
b.sort()
print(b)