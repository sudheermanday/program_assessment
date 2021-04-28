a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
b=[]
j=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        b.insert(j,a[i])
        j+=1
b.insert(j,a[len(a)-1])
print(b)